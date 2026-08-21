#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { chromium } from "playwright";

function argumentsMap(argv) {
  const result = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    if (!argv[index]?.startsWith("--") || argv[index + 1] == null) {
      throw new Error(`Invalid arguments near ${argv[index]}`);
    }
    result.set(argv[index].slice(2), argv[index + 1]);
  }
  return result;
}

const args = argumentsMap(process.argv.slice(2));
const htmlPath = path.resolve(args.get("html"));
const pdfPath = path.resolve(args.get("pdf"));
const reportPath = path.resolve(args.get("report"));

await fs.mkdir(path.dirname(pdfPath), { recursive: true });
await fs.mkdir(path.dirname(reportPath), { recursive: true });

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
const consoleErrors = [];
const failedRequests = [];
page.on("console", message => {
  if (message.type() === "error") consoleErrors.push(message.text());
});
page.on("requestfailed", request => {
  failedRequests.push(`${request.url()} :: ${request.failure()?.errorText ?? "failed"}`);
});

await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "load" });
await page.waitForFunction(() => document.documentElement.dataset.portable === "ready", null, { timeout: 20_000 });
const desktop = await page.evaluate(() => ({
  title: document.title,
  source: document.querySelector("[data-source]")?.getAttribute("data-source") ?? "",
  fingerprint: document.querySelector('meta[name="source-fingerprint"]')?.content ?? "",
  overflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
  externalResources: performance.getEntriesByType("resource")
    .map(entry => entry.name)
    .filter(url => /^https?:|^wss?:/i.test(url)),
  contentVisible: getComputedStyle(document.querySelector(".portable-main")).visibility === "visible",
  technicalSections: document.querySelectorAll(".doc-content h2").length,
  technicalCharacters: document.querySelector(".doc-content")?.innerText.trim().length ?? 0,
  diagrams: document.querySelectorAll(".mermaid svg").length,
  mermaidSources: document.querySelectorAll(".mermaid").length,
}));

await page.setViewportSize({ width: 390, height: 844 });
const mobileOverflow = await page.evaluate(
  () => document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
);
if (
  desktop.overflow || mobileOverflow || !desktop.source || !desktop.fingerprint
  || !desktop.contentVisible || desktop.technicalSections < 3 || desktop.technicalCharacters < 1_200
  || desktop.diagrams !== desktop.mermaidSources
) {
  throw new Error(`Invalid individual portable layout: ${JSON.stringify({ desktop, mobileOverflow })}`);
}
if (desktop.externalResources.length || consoleErrors.length || failedRequests.length) {
  throw new Error(`Individual portable is not offline-safe: ${JSON.stringify({ desktop, consoleErrors, failedRequests })}`);
}

await page.setViewportSize({ width: 1440, height: 1000 });
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: pdfPath,
  format: "A4",
  scale: 0.96,
  printBackground: true,
  displayHeaderFooter: true,
  preferCSSPageSize: true,
  margin: { top: "14mm", right: "12mm", bottom: "16mm", left: "12mm" },
  headerTemplate: '<div style="font:8px Arial;color:#667085;width:100%;padding:0 12mm;text-align:right">Replicant Lab · Ficha técnica</div>',
  footerTemplate: '<div style="font:8px Arial;color:#667085;width:100%;padding:0 12mm;display:flex;justify-content:space-between"><span>Documento derivado</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
});

const report = {
  ...desktop,
  mobileOverflow,
  consoleErrors,
  failedRequests,
  pdfBytes: (await fs.stat(pdfPath)).size,
};
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
await browser.close();
console.log(JSON.stringify(report));
