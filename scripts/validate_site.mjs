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
  { route: "/arquitectura/", name: "architecture", diagrams: 2 },
  { route: "/fases/", name: "evolution", diagrams: 0 },
  { route: "/hosts/nexus/", name: "nexus", diagrams: 0 },
  { route: "/aplicaciones/", name: "applications", diagrams: 0 },
  { route: "/aplicaciones/pula/", name: "pula", diagrams: 1 },
  { route: "/aplicaciones/app-launch/", name: "app-launch", diagrams: 0 },
  { route: "/aplicaciones/salones-av/", name: "salones", diagrams: 0 },
  { route: "/aplicaciones/reserva-pistas-utp/", name: "reservas", diagrams: 0 },
  { route: "/aplicaciones/consumos-cupra/", name: "consumos", diagrams: 0 },
  { route: "/aplicaciones/cv-raul/", name: "cv", diagrams: 0 },
  { route: "/aplicaciones/control-red/", name: "control-red", diagrams: 0 },
  { route: "/aplicaciones/cartera-estrategica/", name: "cartera", diagrams: 0 },
  { route: "/aplicaciones/replicant-lab/", name: "replicant-lab", diagrams: 0 },
  { route: "/aplicaciones/erasmushomes-control/", name: "erasmushomes-control", diagrams: 0 },
  { route: "/control/erasmushomes/", name: "erasmushomes-standalone", diagrams: 0 },
  { route: "/pendientes/", name: "pending", diagrams: 0 },
  { route: "/pendientes/cv-firebase/", name: "pending-detail", diagrams: 0 },
  { route: "/cambios/", name: "changelog-index", diagrams: 0 },
  { route: "/cambios/2026-08-21/", name: "changelog", diagrams: 0 },
  { route: "/cambios/2026-08-13/", name: "changelog-previous", diagrams: 0 },
  { route: "/cambios/2026-08-09/", name: "changelog-previous", diagrams: 0 },
  { route: "/cambios/2026-08-08/", name: "changelog-oldest", diagrams: 0 },
  { route: "/descargas/", name: "downloads", diagrams: 0 },
  { route: "/despliegue/modelos/", name: "mermaid-deploy-models", diagrams: 1 },
  { route: "/red/overview/", name: "mermaid-network", diagrams: 1 },
  { route: "/despliegue/git/", name: "mermaid-git", diagrams: 1 },
  { route: "/autodocumentacion/", name: "mermaid-autodoc", diagrams: 1 },
  { route: "/gobierno/flujo-work-codex-git/", name: "governance", diagrams: 3 },
  { route: "/gobierno/instrucciones-proyecto-work/", name: "work-instructions", diagrams: 0 },
  { route: "/encargos/", name: "engagements", diagrams: 0 },
  { route: "/encargos/TEMPLATE/", name: "engagement-template", diagrams: 0 },
  { route: "/encargos/GOV-001/", name: "gov-001", diagrams: 0 },
];

if (screenshots) await fs.mkdir(screenshots, { recursive: true });
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1440, height: 1000 }, deviceScaleFactor: 1 });
const failures = [];
let totalDiagrams = 0;

function isOptionalFontFailure(value) {
  return /^https:\/\/fonts\.(googleapis|gstatic)\.com\//.test(value);
}

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
    const pendingSummary = await page.evaluate(() => ({
      table: document.querySelector("main table")?.textContent ?? "",
      postCartera: document.querySelector("main")?.textContent.includes("POST-CARTERA") ?? false,
    }));
    const required = ["Cartera Estratégica", "PULA", "CV / Firebase", "Control de Red", "Nexus", "App Launch"];
    if (!required.every(value => pendingSummary.table.includes(value)) || !pendingSummary.postCartera) {
      failures.push(`${item.route}: incomplete pending summary ${JSON.stringify(pendingSummary)}`);
    }
  }
  if (item.name === "pending" || item.name === "pending-detail") {
    const navigation = await page.evaluate(() => ({
      left: [...document.querySelectorAll(".md-sidebar--primary nav a")].map(link => link.textContent.replace(/\s+/g, " ").trim()),
      right: [...document.querySelectorAll(".md-sidebar--secondary nav a")].map(link => link.textContent.replace(/\s+/g, " ").trim()),
    }));
    const expectedLeft = ["Resumen", "Cartera Estratégica", "PULA", "CV / Firebase", "Control de Red", "Nexus", "App Launch"];
    if (!expectedLeft.every(value => navigation.left.includes(value))) failures.push(`${item.route}: incomplete pending navigation ${JSON.stringify(navigation)}`);
    if (item.name === "pending-detail" && ["PULA", "Nexus", "Control de Red"].some(value => navigation.right.includes(value))) {
      failures.push(`${item.route}: unrelated right TOC ${JSON.stringify(navigation.right)}`);
    }
  }
  if (item.name === "applications") {
    const catalog = await page.evaluate(() => ({
      cards: document.querySelectorAll(".app-catalog .app-card").length,
      types: document.querySelectorAll(".app-catalog .app-type").length,
      descriptions: [...document.querySelectorAll(".app-catalog .app-card")].map(card => card.textContent.trim().length),
      links: [...document.querySelectorAll(".app-card .app-accesses a")].filter(link => link.textContent.trim() === "Ficha técnica").map(link => link.getAttribute("href")),
      legacyMarkdownLinks: [...document.querySelectorAll(".app-card a")].filter(link => /aplicaciones\/.+\.md$/.test(link.getAttribute("href") ?? "")).length,
    }));
    if (
      catalog.cards !== 10 || catalog.types !== 10 || catalog.links.length !== 10 || catalog.legacyMarkdownLinks !== 0
      || catalog.descriptions.some(length => length < 250)
      || catalog.links.some(link => !link?.includes("/downloads/apps/") || !link.endsWith(".html"))
    ) {
      failures.push(`${item.route}: invalid application catalog ${JSON.stringify(catalog)}`);
    }
  }
  if (item.route.startsWith("/aplicaciones/") && item.name !== "applications") {
    const application = await page.evaluate(() => ({
      hasAccesses: [...document.querySelectorAll("main h2")].some(heading => heading.textContent.trim() === "Accesos"),
      hasFicha: [...document.querySelectorAll("main a")].some(link => /\/downloads\/apps\/.+\.html$/.test(link.href)),
      left: [...document.querySelectorAll(".md-sidebar--primary nav a")].map(link => link.textContent.replace(/\s+/g, " ").trim()),
    }));
    const expectedApps = ["Índice", "PULA", "App Launch", "ErasmusHomes · Control del MVP", "Salones AV", "Reserva-Pistas-UTP", "Consumos Cupra", "CV de Raúl", "Control de Red", "Cartera Estratégica", "Replicant Lab"];
    if (!application.hasAccesses || !application.hasFicha || !expectedApps.every(value => application.left.includes(value))) {
      failures.push(`${item.route}: incomplete application access/navigation ${JSON.stringify(application)}`);
    }
  }
  if (item.name === "erasmushomes-control") {
    const contrast = await page.evaluate(() => {
      const link = [...document.querySelectorAll("a")].find(element => element.textContent.trim() === "Abrir roadmap acordado (DOCX)");
      const text = document.querySelector(".eh-agreed-document")?.textContent ?? "";
      return {
        href: link?.href ?? "",
        target: link?.target ?? "",
        rel: link?.rel ?? "",
        hasFilename: text.includes("Roadmap_ErasmusHomes_MVP_Diciembre_2026.docx"),
        hasHash: /[0-9a-f]{64}/.test(text),
        hasDate: /\d{4}-\d{2}-\d{2}/.test(text),
      };
    });
    if (
      !/\/downloads\/erasmushomes\/Roadmap_ErasmusHomes_MVP_Diciembre_2026\.docx$/.test(contrast.href)
      || contrast.target !== "_blank" || !contrast.rel.includes("noopener")
      || !contrast.hasFilename || !contrast.hasHash || !contrast.hasDate
    ) {
      failures.push(`${item.route}: invalid agreed DOCX contrast link ${JSON.stringify(contrast)}`);
    }
  }
  if (item.name === "erasmushomes-standalone") {
    const standalone = await page.evaluate(() => {
      const link = [...document.querySelectorAll("a")].find(element => element.textContent.trim() === "Abrir roadmap acordado (DOCX)");
      return {
        title: document.title,
        linkTarget: link?.target ?? "",
        linkHref: link?.href ?? "",
        sha: document.body.innerText.includes("fe867b64") || /Git\s+[0-9a-f]{8}/.test(document.body.innerText),
        metrics: document.querySelectorAll(".metric").length,
        columns: document.querySelectorAll(".column").length,
        tasks: document.querySelectorAll(".task").length,
      };
    });
    if (
      standalone.title !== "ErasmusHomes · Control del MVP"
      || standalone.linkTarget !== "_blank"
      || !/\/downloads\/erasmushomes\/Roadmap_ErasmusHomes_MVP_Diciembre_2026\.docx$/.test(standalone.linkHref)
      || !standalone.sha || standalone.metrics !== 5 || standalone.columns !== 4 || standalone.tasks !== 17
    ) failures.push(`${item.route}: invalid standalone control ${JSON.stringify(standalone)}`);
  }
  if (item.name === "architecture") {
    const architecture = await page.evaluate(() => ({
      concepts: [...document.querySelectorAll(".mermaid-rendered svg")].map(svg => svg.textContent.replace(/\s+/g, " ").trim()),
      scrollable: [...document.querySelectorAll(".mermaid-rendered")].every(diagram => getComputedStyle(diagram).overflowX === "auto"),
    }));
    const expected = ["LAN 192.168.18.0/24", "App Launch Nexus", "App Launch público", "Cloud Run / Firebase", "Catálogo público", "Catálogo Nexus"];
    if (!architecture.scrollable || expected.some(marker => !architecture.concepts.some(text => text.includes(marker)))) {
      failures.push(`${item.route}: incomplete architecture representation ${JSON.stringify(architecture)}`);
    }
  }
  if (item.name === "governance") {
    const governance = await page.evaluate(() => ({
      title: document.querySelector("main h1")?.textContent.trim() ?? "",
      diagrams: document.querySelectorAll(".mermaid-rendered svg").length,
      left: [...document.querySelectorAll(".md-sidebar--primary nav a")].map(link => link.textContent.replace(/\s+/g, " ").trim()),
      required: ["Roles y fuentes de verdad", "Ciclo y estados", "Chats y varios ordenadores", "Coordinación multirrepositorio", "Matriz de impacto documental", "Definición de terminado", "Antipatrones prohibidos"].every(value => document.querySelector("main")?.textContent.includes(value)),
    }));
    if (governance.title !== "Gobierno del trabajo" || governance.diagrams !== 3 || !governance.left.includes("Flujo Work–Codex–Git") || !governance.required) {
      failures.push(`${item.route}: incomplete governance contract ${JSON.stringify(governance)}`);
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
  const optionalFontFailures = requestFailures.filter(isOptionalFontFailure);
  const actionableRequestFailures = requestFailures.filter(value => !isOptionalFontFailure(value));
  const actionableConsoleErrors = consoleErrors.filter(value => !(
    optionalFontFailures.length
    && value === "Failed to load resource: net::ERR_NETWORK_ACCESS_DENIED"
  ));
  if (actionableConsoleErrors.length) failures.push(`${item.route}: console ${actionableConsoleErrors.join(" | ")}`);
  if (actionableRequestFailures.length) failures.push(`${item.route}: requests ${actionableRequestFailures.join(" | ")}`);
  if (responseFailures.length) failures.push(`${item.route}: responses ${responseFailures.join(" | ")}`);
  if (screenshots && ["home", "architecture", "nexus", "applications", "pending", "changelog", "downloads", "governance"].includes(item.name)) {
    await page.screenshot({ path: path.join(screenshots, `${item.name}-desktop.png`), fullPage: true });
  }
  page.off("console", onConsole);
  page.off("requestfailed", onRequest);
  page.off("response", onResponse);
}

for (const item of [
  { route: "/", name: "home" },
  { route: "/descargas/", name: "downloads" },
  { route: "/aplicaciones/", name: "applications" },
  { route: "/aplicaciones/erasmushomes-control/", name: "erasmushomes-control" },
  { route: "/control/erasmushomes/", name: "erasmushomes-standalone" },
  { route: "/gobierno/flujo-work-codex-git/", name: "governance" },
]) {
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
  apps: {},
};
for (const slug of [
  "pula",
  "app-launch",
  "salones-av",
  "reserva-pistas-utp",
  "consumos-cupra",
  "cv-raul",
  "control-red",
  "cartera-estrategica",
  "replicant-lab",
  "erasmushomes-control",
]) {
  downloads.apps[slug] = {
    html: await compareDownload(`downloads/apps/${slug}.html`),
    pdf: await compareDownload(`downloads/apps/${slug}.pdf`),
  };
}
if (totalDiagrams !== 10) failures.push(`Expected ten Mermaid diagrams across site, got ${totalDiagrams}`);
if (failures.length) throw new Error(failures.join("\n"));

const report = { routes: routes.length, desktopScreenshots: screenshots ? 8 : 0, mobileScreenshots: screenshots ? 6 : 0, mermaid: totalDiagrams, downloads };
await fs.mkdir(path.dirname(reportPath), { recursive: true });
await fs.writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, "utf8");
await browser.close();
console.log(JSON.stringify(report));
