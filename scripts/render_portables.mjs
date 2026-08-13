#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { chromium } from "playwright";

function argumentsMap(argv) {
  const result = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    const key = argv[index];
    const value = argv[index + 1];
    if (!key?.startsWith("--") || value == null) throw new Error(`Invalid argument sequence near ${key ?? "<end>"}`);
    result.set(key.slice(2), value);
  }
  return result;
}

const args = argumentsMap(process.argv.slice(2));
const htmlPath = path.resolve(args.get("html"));
const pdfPath = path.resolve(args.get("pdf"));
const reportPath = path.resolve(args.get("report"));
const screenshots = args.get("screenshots") ? path.resolve(args.get("screenshots")) : null;
const fileUrl = pathToFileURL(htmlPath).href;

await fs.mkdir(path.dirname(pdfPath), { recursive: true });
await fs.mkdir(path.dirname(reportPath), { recursive: true });
if (screenshots) await fs.mkdir(screenshots, { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
const consoleErrors = [];
const failedRequests = [];
page.on("console", message => {
  if (message.type() === "error") consoleErrors.push(message.text());
});
page.on("requestfailed", request => failedRequests.push(`${request.url()} :: ${request.failure()?.errorText ?? "failed"}`));

async function waitForActive(expected) {
  await page.waitForFunction(id => {
    const active = [...document.querySelectorAll(".doc-page")].filter(item => getComputedStyle(item).display !== "none");
    return active.length === 1 && active[0].id === id && document.documentElement.dataset.activePage === id;
  }, expected, { timeout: 10_000 });
}

await page.goto(fileUrl, { waitUntil: "load" });
await page.waitForFunction(
  () => document.documentElement.dataset.mermaid === "ready" && document.documentElement.dataset.portable === "ready",
  null,
  { timeout: 30_000 },
);

const baseReport = await page.evaluate(() => {
  const pages = [...document.querySelectorAll(".doc-page")];
  const visible = pages.filter(item => getComputedStyle(item).display !== "none");
  return {
    title: document.title,
    fingerprint: document.querySelector('meta[name="source-fingerprint"]')?.content ?? "",
    sourcePages: pages.length,
    activePages: visible.map(item => item.id),
    pageLinks: document.querySelectorAll("[data-page-link]").length,
    controls: document.querySelectorAll(".page-controls").length,
    hasSearch: Boolean(document.querySelector("#portable-search")),
    externalResources: performance.getEntriesByType("resource")
      .map(entry => entry.name)
      .filter(url => /^https?:|^wss?:/i.test(url)),
  };
});

if (baseReport.sourcePages < 1) throw new Error("Portable HTML contains no source pages");
if (baseReport.activePages.length !== 1 || baseReport.activePages[0] !== "page-1") {
  throw new Error(`Portable must show only page-1 initially: ${JSON.stringify(baseReport.activePages)}`);
}
if (baseReport.pageLinks !== baseReport.sourcePages || baseReport.controls !== baseReport.sourcePages || !baseReport.hasSearch) {
  throw new Error(`Incomplete multipage controls: ${JSON.stringify(baseReport)}`);
}

const diagramPageIds = await page.evaluate(() => [...new Set(
  [...document.querySelectorAll(".mermaid")].map(item => item.closest(".doc-page")?.id).filter(Boolean),
)]);
const diagrams = [];
for (const pageId of diagramPageIds) {
  await page.evaluate(id => { location.hash = id; }, pageId);
  await waitForActive(pageId);
  const metrics = await page.evaluate(id => [...document.querySelectorAll(`#${id} .mermaid`)].map((element, offset) => {
    const svg = element.querySelector("svg");
    const box = svg?.getBoundingClientRect();
    const parent = element.getBoundingClientRect();
    return {
      page: id,
      offset,
      hasSvg: Boolean(svg),
      width: Math.round(box?.width ?? 0),
      height: Math.round(box?.height ?? 0),
      containerWidth: Math.round(parent.width),
      overflowX: element.scrollWidth > element.clientWidth + 2,
      overflowY: element.scrollHeight > element.clientHeight + 2,
      text: (svg?.textContent ?? "").replace(/\s+/g, " ").trim().slice(0, 240),
    };
  }), pageId);
  diagrams.push(...metrics);
}
if (diagrams.length !== 6) throw new Error(`Expected 6 Mermaid diagrams, got ${diagrams.length}`);
if (diagrams.some(item => !item.hasSvg || item.width < 100 || item.height < 35 || item.overflowX || item.overflowY)) {
  throw new Error(`Invalid Mermaid layout: ${JSON.stringify(diagrams)}`);
}

const directTarget = await page.evaluate(() => {
  for (const sourcePage of [...document.querySelectorAll(".doc-page")].slice(1)) {
    const heading = sourcePage.querySelector("h2[id], h3[id]");
    if (heading) return { heading: heading.id, page: sourcePage.id };
  }
  return null;
});
if (!directTarget) throw new Error("No direct heading target found");
await page.goto(fileUrl + "#" + directTarget.heading, { waitUntil: "load" });
await page.waitForFunction(
  expected => document.documentElement.dataset.portable === "ready" && document.documentElement.dataset.activePage === expected,
  directTarget.page,
  { timeout: 30_000 },
);

await page.goto(fileUrl + "#page-2", { waitUntil: "load" });
await waitForActive("page-2");
const nextHref = await page.locator("#page-2 .page-controls a.next").getAttribute("href");
if (!nextHref) throw new Error("Page 2 has no next link");
await page.click("#page-2 .page-controls a.next");
await waitForActive(nextHref.slice(1));
await page.goBack();
await waitForActive("page-2");
await page.goForward();
await waitForActive(nextHref.slice(1));

await page.fill("#portable-search", "Catálogo operativo del laboratorio");
const searchResult = await page.evaluate(() => ({
  visible: [...document.querySelectorAll(".portable-nav [data-page-item]")].filter(item => !item.hidden).length,
  status: document.querySelector("#portable-search-status")?.textContent ?? "",
}));
if (searchResult.visible !== 1 || !searchResult.status) {
  throw new Error(`Portable search is not filtering reliably: ${JSON.stringify(searchResult)}`);
}
await page.fill("#portable-search", "");

const changeLogDates = await page.evaluate(() => {
  const group = [...document.querySelectorAll(".portable-nav .nav-group")]
    .find(item => item.querySelector(":scope > .nav-group-label")?.textContent.trim() === "Change Log");
  return group ? [...group.querySelectorAll(":scope > .nav-children > [data-page-item] > a")].map(item => item.textContent.trim()) : [];
});
if (JSON.stringify(changeLogDates) !== JSON.stringify(["Índice", "13 de agosto de 2026", "9 de agosto de 2026", "8 de agosto de 2026"])) {
  throw new Error(`Change Log hierarchy differs from MkDocs nav: ${JSON.stringify(changeLogDates)}`);
}

const pendingPage = await page.evaluate(() => document.querySelector('[data-source="pendientes-codex.md"]')?.id);
if (!pendingPage) throw new Error("Pending page not found");
await page.goto(fileUrl + "#" + pendingPage, { waitUntil: "load" });
await waitForActive(pendingPage);
const pendingSummary = await page.evaluate(() => ({
  headings: [...document.querySelectorAll(".doc-page.is-active h2")].map(item => item.textContent.trim()),
  postCartera: document.querySelector(".doc-page.is-active")?.textContent.includes("POST-CARTERA") ?? false,
}));
const requiredPendingHeadings = ["Activos", "Deuda POST-CARTERA", "Mejoras opcionales"];
if (!requiredPendingHeadings.every(item => pendingSummary.headings.includes(item)) || !pendingSummary.postCartera) {
  throw new Error(`Pending summary is incomplete: ${JSON.stringify(pendingSummary)}`);
}
await page.goto(fileUrl + "#page-2", { waitUntil: "load" });
await waitForActive("page-2");
if (screenshots) await page.screenshot({ path: path.join(screenshots, "portable-desktop.png"), fullPage: true });

await page.setViewportSize({ width: 390, height: 844 });
await page.goto(fileUrl + "#" + pendingPage, { waitUntil: "load" });
await waitForActive(pendingPage);
const mobile = await page.evaluate(() => ({
  overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
  menuVisible: getComputedStyle(document.querySelector(".portable-menu-button")).display !== "none",
  active: document.documentElement.dataset.activePage,
}));
if (mobile.overflow || !mobile.menuVisible || mobile.active !== pendingPage) {
  throw new Error(`Invalid mobile multipage layout: ${JSON.stringify(mobile)}`);
}
await page.click(".portable-menu-button");
const mobileMenuOpen = await page.evaluate(() => document.querySelector(".portable-sidebar").classList.contains("is-open"));
if (!mobileMenuOpen) throw new Error("Mobile navigation did not open");
if (screenshots) await page.screenshot({ path: path.join(screenshots, "portable-mobile.png"), fullPage: true });

if (baseReport.externalResources.length) throw new Error(`Offline HTML requested external resources: ${baseReport.externalResources.join(", ")}`);
if (consoleErrors.length) throw new Error(`Browser console errors: ${consoleErrors.join(" | ")}`);
if (failedRequests.length) throw new Error(`Failed requests: ${failedRequests.join(" | ")}`);

await page.setViewportSize({ width: 1440, height: 1000 });
await page.evaluate(() => document.querySelectorAll(".status-panel details").forEach(item => { item.open = true; }));
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: pdfPath,
  format: "A4",
  printBackground: true,
  displayHeaderFooter: true,
  preferCSSPageSize: true,
  margin: { top: "14mm", right: "12mm", bottom: "16mm", left: "12mm" },
  headerTemplate: '<div style="font:8px Arial;color:#667085;width:100%;padding:0 12mm;text-align:right">Replicant Lab</div>',
  footerTemplate: '<div style="font:8px Arial;color:#667085;width:100%;padding:0 12mm;display:flex;justify-content:space-between"><span>Documentación reproducible</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
});

const report = {
  ...baseReport,
  mermaidState: "ready",
  diagrams,
  navigation: {
    directFragment: directTarget,
    backForward: true,
    previousNext: true,
    search: searchResult,
    changeLogDates,
    pendingSummary,
    mobile,
  },
  consoleErrors,
  failedRequests,
  pdfBytes: (await fs.stat(pdfPath)).size,
};
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
await browser.close();
console.log(JSON.stringify(report));
