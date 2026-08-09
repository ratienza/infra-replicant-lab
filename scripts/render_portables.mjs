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

await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "load" });
await page.waitForFunction(() => document.documentElement.dataset.mermaid === "ready", null, { timeout: 30_000 });

const report = await page.evaluate(() => {
  const diagrams = [...document.querySelectorAll(".mermaid")];
  const metrics = diagrams.map((element, index) => {
    const svg = element.querySelector("svg");
    const box = svg?.getBoundingClientRect();
    const parent = element.getBoundingClientRect();
    return {
      index: index + 1,
      hasSvg: Boolean(svg),
      width: Math.round(box?.width ?? 0),
      height: Math.round(box?.height ?? 0),
      containerWidth: Math.round(parent.width),
      overflowX: element.scrollWidth > element.clientWidth + 2,
      overflowY: element.scrollHeight > element.clientHeight + 2,
      text: (svg?.textContent ?? "").replace(/\s+/g, " ").trim().slice(0, 240),
    };
  });
  return {
    title: document.title,
    fingerprint: document.querySelector('meta[name="source-fingerprint"]')?.content ?? "",
    sourcePages: document.querySelectorAll(".doc-page").length,
    mermaidState: document.documentElement.dataset.mermaid,
    diagrams: metrics,
    externalResources: performance.getEntriesByType("resource")
      .map(entry => entry.name)
      .filter(url => /^https?:|^wss?:/i.test(url)),
  };
});

if (report.sourcePages < 1) throw new Error("Portable HTML contains no source pages");
if (report.diagrams.length !== 5) throw new Error(`Expected 5 Mermaid diagrams, got ${report.diagrams.length}`);
if (report.diagrams.some(item => !item.hasSvg || item.width < 100 || item.height < 40 || item.overflowX || item.overflowY)) {
  throw new Error(`Invalid Mermaid layout: ${JSON.stringify(report.diagrams)}`);
}
if (report.externalResources.length) throw new Error(`Offline HTML requested external resources: ${report.externalResources.join(", ")}`);
if (consoleErrors.length) throw new Error(`Browser console errors: ${consoleErrors.join(" | ")}`);
if (failedRequests.length) throw new Error(`Failed requests: ${failedRequests.join(" | ")}`);

if (screenshots) {
  await page.screenshot({ path: path.join(screenshots, "portable-desktop.png"), fullPage: true });
  await page.setViewportSize({ width: 390, height: 844 });
  await page.screenshot({ path: path.join(screenshots, "portable-mobile.png"), fullPage: true });
  await page.setViewportSize({ width: 1440, height: 1000 });
}

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

report.consoleErrors = consoleErrors;
report.failedRequests = failedRequests;
report.pdfBytes = (await fs.stat(pdfPath)).size;
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
await browser.close();
console.log(JSON.stringify(report));
