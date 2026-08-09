#!/usr/bin/env node

import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { chromium } from "playwright";

function argumentsMap(argv) {
  const result = new Map();
  for (let index = 0; index < argv.length; index += 2) {
    if (!argv[index]?.startsWith("--") || argv[index + 1] == null) throw new Error(`Invalid arguments near ${argv[index]}`);
    result.set(argv[index].slice(2), argv[index + 1]);
  }
  return result;
}

const args = argumentsMap(process.argv.slice(2));
const base = new URL(args.get("base"));
const root = path.resolve(args.get("root"));
const reportPath = path.resolve(args.get("report"));
const screenshots = args.get("screenshots") ? path.resolve(args.get("screenshots")) : null;
const routes = [
  { route: "/", name: "home", diagrams: 0 },
  { route: "/arquitectura/", name: "architecture", diagrams: 1 },
  { route: "/hosts/nexus/", name: "nexus", diagrams: 0 },
  { route: "/aplicaciones/", name: "applications", diagrams: 0 },
  { route: "/pendientes-codex/", name: "pending", diagrams: 0 },
  { route: "/cambios/", name: "changelog-index", diagrams: 0 },
  { route: "/cambios/2026-08-09/", name: "changelog", diagrams: 0 },
  { route: "/cambios/2026-08-08/", name: "changelog-previous", diagrams: 0 },
  { route: "/descargas/", name: "downloads", diagrams: 0 },
  { route: "/fases/05-poc-salones/", name: "mermaid-salones", diagrams: 1 },
  { route: "/red/overview/", name: "mermaid-network", diagrams: 1 },
  { route: "/despliegue/git/", name: "mermaid-git", diagrams: 1 },
  { route: "/autodocumentacion/", name: "mermaid-autodoc", diagrams: 1 },
];

if (screenshots) await fs.mkdir(screenshots, { recursive: true });
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
const failures = [];
let totalDiagrams = 0;

for (const item of routes) {
  const consoleErrors = [];
  const requestFailures = [];
  const responseFailures = [];
  const onConsole = message => { if (message.type() === "error") consoleErrors.push(message.text()); };
  const onRequest = request => requestFailures.push(`${request.url()} :: ${request.failure()?.errorText ?? "failed"}`);
  const onResponse = response => { if (response.status() >= 400) responseFailures.push(`${response.status()} ${response.url()}`); };
  page.on("console", onConsole);
  page.on("requestfailed", onRequest);
  page.on("response", onResponse);
  const response = await page.goto(new URL(item.route.replace(/^\//, ""), base).href, { waitUntil: "networkidle" });
  if (!response?.ok()) failures.push(`${item.route}: HTTP ${response?.status() ?? "none"}`);
  if (item.diagrams) {
    try {
      await page.waitForFunction(expected => document.querySelectorAll('.mermaid-rendered svg').length === expected, item.diagrams, { timeout: 20_000 });
    } catch (error) {
      const detail = await page.evaluate(() => ({ state: document.documentElement.dataset.mermaid, markup: document.querySelector('.mermaid, .mermaid-rendered')?.innerHTML.slice(0, 200) }));
      failures.push(`${item.route}: Mermaid timeout ${JSON.stringify(detail)}`);
    }
  }
  if (item.name === "pending") {
    const details = await page.locator(".status-panel details").count();
    const initiallyOpen = await page.locator(".status-panel details[open]").count();
    if (details !== 8 || initiallyOpen !== 0) failures.push(`${item.route}: compact details ${details}/${initiallyOpen}`);
    await page.locator(".status-panel details summary").first().click();
    if (!await page.locator(".status-panel details").first().evaluate(element => element.open)) {
      failures.push(`${item.route}: detail did not open`);
    }
  }
  const state = await page.evaluate(() => ({
    title: document.title,
    diagrams: document.querySelectorAll('.mermaid-rendered svg').length,
    rawMermaid: document.querySelectorAll('.mermaid').length,
    horizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 2,
  }));
  totalDiagrams += state.diagrams;
  if (state.diagrams !== item.diagrams || state.rawMermaid) failures.push(`${item.route}: Mermaid ${JSON.stringify(state)}`);
  if (state.horizontalOverflow) failures.push(`${item.route}: desktop horizontal overflow`);
  if (consoleErrors.length) failures.push(`${item.route}: console ${consoleErrors.join(" | ")}`);
  if (requestFailures.length) failures.push(`${item.route}: requests ${requestFailures.join(" | ")}`);
  if (responseFailures.length) failures.push(`${item.route}: responses ${responseFailures.join(" | ")}`);
  if (screenshots && ["home", "architecture", "nexus", "applications", "pending", "changelog", "downloads"].includes(item.name)) {
    await page.screenshot({ path: path.join(screenshots, `${item.name}-desktop.png`), fullPage: true });
  }
  page.off("console", onConsole);
  page.off("requestfailed", onRequest);
  page.off("response", onResponse);
}

for (const item of [{ route: "/", name: "home" }, { route: "/descargas/", name: "downloads" }]) {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(new URL(item.route.replace(/^\//, ""), base).href, { waitUntil: "networkidle" });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 2);
  if (overflow) failures.push(`${item.route}: mobile horizontal overflow`);
  if (screenshots) await page.screenshot({ path: path.join(screenshots, `${item.name}-mobile.png`), fullPage: true });
}

async function compareDownload(relative) {
  const response = await fetch(new URL(relative, base));
  if (!response.ok) throw new Error(`${relative}: HTTP ${response.status}`);
  const served = Buffer.from(await response.arrayBuffer());
  const tracked = await fs.readFile(path.join(root, relative));
  const digest = value => crypto.createHash("sha256").update(value).digest("hex");
  if (!served.equals(tracked)) throw new Error(`${relative}: served bytes differ from generated artifact`);
  return { bytes: served.length, sha256: digest(served) };
}

const downloads = {
  html: await compareDownload("downloads/Replicant-Lab.html"),
  pdf: await compareDownload("downloads/Replicant-Lab.pdf"),
};
if (totalDiagrams !== 5) failures.push(`Expected five Mermaid diagrams across site, got ${totalDiagrams}`);
if (failures.length) throw new Error(failures.join("\n"));

const report = { routes: routes.length, desktopScreenshots: screenshots ? 7 : 0, mobileScreenshots: screenshots ? 2 : 0, mermaid: totalDiagrams, downloads };
await fs.mkdir(path.dirname(reportPath), { recursive: true });
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
await browser.close();
console.log(JSON.stringify(report));
