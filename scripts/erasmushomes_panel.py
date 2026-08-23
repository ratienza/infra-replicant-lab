#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
STATUSES = ("done", "in_progress", "pending", "blocked")
LABELS = {"done": "Completado", "in_progress": "En ejecución", "pending": "Pendiente", "blocked": "Bloqueado"}
FIELDS = {"id", "title", "phase", "sprint", "week_start", "week_end", "status", "owner", "objective", "definition_of_done", "weekend_validation", "evidence", "risks", "blocker_reason", "next_decision", "updated_at", "notes"}
PDF_RELATIVE_PATH = Path("docs/source/Roadmap_ErasmusHomes_MVP_Diciembre_2026.pdf")
STANDALONE_CSS = r"""
:root{color-scheme:light;--ink:#172033;--muted:#667085;--line:#d9e1eb;--paper:#fff;--soft:#f4f7fb;--brand:#3457d5;--done:#18864b;--progress:#2768d8;--pending:#778195;--blocked:#c93645;--shadow:0 18px 50px rgba(29,45,78,.10)}
*{box-sizing:border-box}html{background:#eef3f9}body{margin:0;color:var(--ink);background:linear-gradient(180deg,#edf3fb 0,#f8fafc 24rem,#f4f7fb 100%);font:15px/1.55 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}a{color:var(--brand)}code{overflow-wrap:anywhere;font:600 .86em ui-monospace,SFMono-Regular,Consolas,monospace}.shell{width:min(1440px,calc(100% - 48px));margin:auto;padding:32px 0 64px}.topbar{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:22px}.brand{display:flex;align-items:center;gap:12px;font-weight:800}.brand-mark{display:grid;width:38px;height:38px;place-items:center;border-radius:12px;color:#fff;background:var(--brand);box-shadow:var(--shadow)}.sync{padding:7px 12px;border-radius:999px;color:#fff;background:var(--done);font-size:13px;font-weight:800}.hero{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(300px,.55fr);gap:22px;padding:clamp(24px,4vw,52px);border:1px solid #d6e0ee;border-radius:24px;background:rgba(255,255,255,.94);box-shadow:var(--shadow)}.eyebrow{margin:0 0 9px;color:var(--brand);font-size:12px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.hero h1{max-width:840px;margin:0;font-size:clamp(32px,5vw,62px);line-height:1.04;letter-spacing:-.045em}.hero-copy{max-width:760px;margin:18px 0 0;color:var(--muted);font-size:clamp(16px,1.5vw,20px)}.source-card{align-self:stretch;padding:22px;border:1px solid var(--line);border-radius:18px;background:var(--soft)}.source-card h2{margin:0 0 14px;font-size:17px}.docx-button{display:inline-flex;align-items:center;justify-content:center;width:100%;min-height:48px;padding:11px 15px;border-radius:12px;color:#fff;background:var(--brand);font-weight:900;text-align:center;text-decoration:none}.meta{display:grid;gap:8px;margin:16px 0 0}.meta div{min-width:0}.meta dt{color:var(--muted);font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}.meta dd{margin:1px 0 0;overflow-wrap:anywhere}.metrics{display:grid;grid-template-columns:1.25fr repeat(4,1fr);gap:14px;margin:22px 0}.metric{min-width:0;padding:20px;border:1px solid var(--line);border-radius:17px;background:var(--paper)}.metric strong{display:block;font-size:31px;line-height:1}.metric span{display:block;margin-top:7px;color:var(--muted);font-size:13px}.metric.primary{color:#fff;border:0;background:linear-gradient(135deg,#253f9b,#4771ea)}.metric.primary span{color:#dfe7ff}.workspace{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(300px,.45fr);gap:20px}.panel{padding:24px;border:1px solid var(--line);border-radius:20px;background:var(--paper)}.panel-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:17px}.panel h2{margin:0;font-size:22px;letter-spacing:-.02em}.panel-note{margin:3px 0 0;color:var(--muted);font-size:13px}.gate{padding:18px;border-left:5px solid var(--brand);border-radius:12px;background:#f2f5ff}.gate strong{display:block;margin-bottom:4px}.priorities{display:grid;gap:12px;margin-top:14px}.priority{padding:16px;border:1px solid var(--line);border-radius:14px}.priority b{color:var(--brand)}.kanban{display:grid;grid-template-columns:repeat(4,minmax(230px,1fr));gap:14px;overflow-x:auto;padding:2px 2px 10px}.column{min-width:230px;padding:14px;border-top:4px solid var(--color);border-radius:14px;background:var(--soft)}.column h3{display:flex;justify-content:space-between;margin:0 0 12px;color:var(--color);font-size:15px}.task{margin-top:10px;padding:14px;border:1px solid var(--line);border-radius:12px;background:#fff}.task-id{color:var(--color);font-size:11px;font-weight:900}.task h4{margin:4px 0 8px;font-size:14px;line-height:1.25}.task p{margin:6px 0;color:var(--muted);font-size:12px}.timeline{display:grid;gap:8px;margin:0;padding:0;list-style:none}.timeline li{display:grid;grid-template-columns:165px minmax(0,1fr) auto;gap:12px;align-items:center;padding:11px 13px;border-left:4px solid var(--color);border-radius:9px;background:var(--soft)}.timeline time,.timeline span{color:var(--muted);font-size:12px}.footer{margin-top:24px;color:var(--muted);font-size:12px;text-align:center}.status-done{--color:var(--done)}.status-in_progress{--color:var(--progress)}.status-pending{--color:var(--pending)}.status-blocked{--color:var(--blocked)}
@media(max-width:1100px){.hero,.workspace{grid-template-columns:1fr}.metrics{grid-template-columns:repeat(5,minmax(145px,1fr));overflow-x:auto}.source-card{display:grid;grid-template-columns:minmax(220px,.65fr) 1fr;gap:16px;align-items:start}.source-card h2{grid-column:1/-1}.kanban{grid-template-columns:repeat(2,minmax(0,1fr));overflow:visible}.column{min-width:0}}
@media(max-width:820px){.shell{width:min(100% - 28px,1440px);padding-top:18px}.hero{padding:25px;border-radius:18px}.source-card{grid-template-columns:1fr}.metrics{grid-template-columns:repeat(2,1fr);overflow:visible}.metric.primary{grid-column:1/-1}.panel{padding:18px}.timeline li{grid-template-columns:1fr}.timeline span{justify-self:start}.topbar{align-items:flex-start}}
@media(max-width:520px){body{font-size:14px}.shell{width:min(100% - 20px,1440px)}.brand-copy small{display:none}.hero{padding:20px}.hero h1{font-size:34px}.metrics{gap:10px}.metric{padding:16px}.metric strong{font-size:27px}.panel-head{display:block}.kanban{grid-template-columns:1fr;overflow:visible}.column{min-width:0}.source-card{padding:17px}.docx-button{font-size:14px}.sync{font-size:11px}.timeline li{padding:10px}.workspace{gap:14px}}
"""

FINAL_CSS = r"""
:root{color-scheme:light;--ink:#182133;--muted:#647084;--line:#dce3ed;--paper:#fff;--soft:#f5f7fb;--brand:#315bd6;--done:#168653;--progress:#2868d7;--pending:#687386;--blocked:#c63b4a;--shadow:0 16px 48px rgba(31,47,78,.09)}
*{box-sizing:border-box}html{background:#eef3f8;scroll-behavior:smooth}body{margin:0;color:var(--ink);background:linear-gradient(180deg,#edf3fb,#f8fafc 32rem,#f3f6fa);font:15px/1.5 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}button,a{font:inherit}a{color:var(--brand)}code{overflow-wrap:anywhere;font:.82em ui-monospace,SFMono-Regular,Consolas,monospace}.shell{width:min(1420px,calc(100% - 40px));margin:auto;padding:24px 0 56px}.topbar,.topbar-left,.statusline,.compact-counts,.tabs{display:flex;align-items:center}.topbar{justify-content:space-between;gap:16px;margin-bottom:16px}.topbar-left{gap:11px;font-weight:800}.mark{display:grid;width:40px;height:40px;place-items:center;border-radius:12px;color:#fff;background:var(--brand)}.sync{padding:7px 11px;border-radius:99px;color:#fff;background:var(--done);font-size:12px;font-weight:800}.hero,.panel{border:1px solid var(--line);border-radius:20px;background:rgba(255,255,255,.96);box-shadow:var(--shadow)}.hero{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(330px,.65fr);gap:24px;padding:clamp(24px,3.5vw,46px)}.eyebrow{margin:0 0 8px;color:var(--brand);font-size:11px;font-weight:900;letter-spacing:.11em;text-transform:uppercase}.hero h1{margin:0;max-width:780px;font-size:clamp(31px,4vw,54px);line-height:1.04;letter-spacing:-.04em}.hero-copy{margin:14px 0 0;color:var(--muted);font-size:17px}.progressline{margin-top:22px;font-size:20px;font-weight:900}.statusline{flex-wrap:wrap;gap:8px 18px;margin-top:10px;color:var(--muted);font-size:12px}.source{padding:20px;border-radius:16px;background:var(--soft)}.source h2{margin:0 0 12px;font-size:16px}.pdf-button{display:flex;min-height:48px;align-items:center;justify-content:center;padding:10px;border-radius:11px;color:#fff;background:var(--brand);font-weight:900;text-align:center;text-decoration:none}.meta{display:grid;gap:6px;margin:14px 0 0}.meta div{min-width:0}.meta dt{color:var(--muted);font-size:10px;font-weight:800;text-transform:uppercase}.meta dd{margin:0;overflow-wrap:anywhere}.trace-links{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px;font-size:12px}.now{margin-top:18px;padding:24px;border-left:6px solid var(--progress)}.now-grid{display:grid;grid-template-columns:1.2fr repeat(3,minmax(150px,.6fr));gap:18px}.now h2,.section-title{margin:0}.now .active-title{margin:5px 0;font-size:25px}.label{color:var(--muted);font-size:10px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}.value{margin-top:4px;font-weight:750}.summary{display:grid;grid-template-columns:1.2fr .8fr;gap:18px;margin-top:18px}.panel{padding:22px}.compact-counts{flex-wrap:wrap;gap:8px;margin:14px 0}.count{padding:7px 10px;border-radius:999px;background:var(--soft);font-size:12px;font-weight:800}.priorities{display:grid;gap:10px;margin-top:12px}.priority{padding:13px;border:1px solid var(--line);border-radius:12px}.priority strong{display:block}.priority small{color:var(--muted)}.risks{margin:12px 0 0;padding-left:18px}.board{margin-top:18px}.tabs{gap:8px;overflow-x:auto;padding:4px 0 14px}.tab{flex:0 0 auto;min-height:44px;padding:9px 14px;border:1px solid var(--line);border-radius:11px;color:var(--ink);background:var(--soft);font-weight:850;cursor:pointer}.tab[aria-selected="true"]{color:#fff;border-color:var(--brand);background:var(--brand)}.tab-panel[hidden]{display:none}.task-browser{display:grid;grid-template-columns:minmax(280px,.38fr) minmax(0,.62fr);gap:16px}.task-list{display:grid;align-content:start;gap:8px}.task-select{width:100%;padding:13px;text-align:left;border:1px solid var(--line);border-radius:11px;color:var(--ink);background:#fff;cursor:pointer}.task-select[aria-selected="true"]{border-color:var(--brand);box-shadow:0 0 0 2px rgba(49,91,214,.12)}.task-select b,.task-select span{display:block}.task-select span{margin-top:3px;color:var(--muted);font-size:12px}.task-detail{min-width:0;padding:20px;border-radius:14px;background:var(--soft)}.task-detail h3{margin:4px 0 12px;font-size:24px}.detail-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px}.detail-box{padding:13px;border-radius:10px;background:#fff}.detail-box p{margin:5px 0}.evidence a{overflow-wrap:anywhere}.timeline{display:grid;gap:7px;margin:0;padding:0;list-style:none}.timeline li{display:grid;grid-template-columns:190px minmax(0,1fr) auto;gap:10px;padding:10px 12px;border-left:4px solid var(--pending);border-radius:8px;background:var(--soft)}.timeline .done{border-color:var(--done)}.timeline .in_progress{border-color:var(--progress)}.timeline .blocked{border-color:var(--blocked)}.timeline time,.timeline span{color:var(--muted);font-size:12px}.footer{margin-top:20px;color:var(--muted);font-size:11px;text-align:center}
@media(max-width:1000px){.hero,.summary{grid-template-columns:1fr}.now-grid{grid-template-columns:1fr 1fr}.task-browser{grid-template-columns:minmax(240px,.42fr) minmax(0,.58fr)}}
@media(max-width:720px){.shell{width:min(100% - 24px,1420px);padding-top:14px}.hero,.panel{border-radius:16px}.hero{padding:22px}.now{padding:19px}.now-grid,.detail-grid{grid-template-columns:1fr}.tabs{display:grid;grid-template-columns:1fr 1fr;overflow:visible}.tab{width:100%}.task-browser{display:block}.task-list{gap:7px}.task-select{min-height:48px}.task-detail{display:none;margin:7px 0 12px}.task-detail.mobile-open{display:block}.timeline li{grid-template-columns:1fr}.topbar{align-items:flex-start}.brand-small{display:none}}
@media(max-width:420px){.shell{width:min(100% - 16px,1420px)}.hero{padding:18px}.hero h1{font-size:32px}.source{padding:16px}.panel{padding:16px}.now .active-title{font-size:21px}.tab{min-height:48px;padding:10px 12px}.task-detail{padding:15px}.timeline li{padding:9px}}
"""


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-c", f"safe.directory={repo}", "-C", str(repo), *args], text=True).strip()


def validate(data: dict) -> list[dict]:
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise ValueError("roadmap.yaml requires a non-empty tasks list")
    seen: set[str] = set()
    active = []
    for task in tasks:
        if set(task) != FIELDS:
            raise ValueError(f"{task.get('id', '?')}: invalid fields")
        task_id = str(task["id"])
        if task_id in seen or not re.fullmatch(r"(?:EH-\d{3}(?:R-C)?|WK-\d{2})", task_id):
            raise ValueError(f"invalid or duplicate id: {task_id}")
        seen.add(task_id)
        if task["status"] not in STATUSES:
            raise ValueError(f"{task_id}: unknown status")
        if task["status"] == "in_progress":
            active.append(task_id)
        evidence = task["evidence"]
        if set(evidence) != {"pr", "commit", "url"}:
            raise ValueError(f"{task_id}: invalid evidence")
        if task["status"] == "done" and not all(str(value).strip() for value in evidence.values()):
            raise ValueError(f"{task_id}: done without complete evidence")
        if task["status"] == "blocked" and (not str(task["blocker_reason"]).strip() or not str(task["next_decision"]).strip()):
            raise ValueError(f"{task_id}: blocked without reason and next decision")
        url = str(evidence["url"]).strip()
        if url:
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.hostname != "github.com" or not parsed.path.startswith("/ratienza/ErasmusHomes/"):
                raise ValueError(f"{task_id}: evidence URL is not an approved GitHub URL")
    if len(active) > 1:
        raise ValueError(f"only one in_progress task is allowed: {active}")
    return tasks


def esc(value: object) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def human_date(value: object) -> str:
    parsed = value if isinstance(value, dt.date) else dt.date.fromisoformat(str(value))
    return parsed.strftime("%d-%m-%Y")


def human_datetime(value: str) -> str:
    return dt.datetime.fromisoformat(value).strftime("%d-%m-%Y %H:%M")


def validate_document(document: dict, sha: str) -> None:
    required = {"name", "sha256", "version_date", "url", "source_url", "markdown_url", "yaml_url"}
    if set(document) != required:
        raise ValueError("invalid agreed roadmap document metadata")
    if document["name"] != PDF_RELATIVE_PATH.name:
        raise ValueError("unexpected agreed roadmap filename")
    if not re.fullmatch(r"[0-9a-f]{64}", document["sha256"]):
        raise ValueError("invalid agreed roadmap SHA-256")
    if document["url"] != f"/downloads/erasmushomes/{PDF_RELATIVE_PATH.name}":
        raise ValueError("unexpected published agreed roadmap URL")
    expected_source_url = f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/{PDF_RELATIVE_PATH.as_posix()}"
    if document["source_url"] != expected_source_url:
        raise ValueError("agreed roadmap Git source is not pinned to the panel SHA")
    dt.date.fromisoformat(document["version_date"])


def render(data: dict, sha: str, synced_at: str, sync_state: str, document: dict) -> str:
    tasks = validate(data)
    validate_document(document, sha)
    counts = {status: sum(task["status"] == status for task in tasks) for status in STATUSES}
    completed = counts["done"]
    percent = round(completed * 100 / len(tasks))
    active = [task for task in tasks if task["status"] == "in_progress"][:3]
    next_gate = next((task for task in tasks if task["status"] in {"in_progress", "pending", "blocked"}), None)
    state_label = {"synchronized": "Sincronizado", "stale": "Desactualizado", "error": "Error de sincronización"}[sync_state]
    lines = [
        "# ErasmusHomes · Control del MVP", "",
        "<!-- GENERATED: edit ratienza/ErasmusHomes docs/board/roadmap.yaml, never this file -->", "",
        "## Accesos", "",
        "- **Panel de control:** [Control MVP autónomo](/control/erasmushomes/)",
        "- **Ficha técnica:** [HTML autocontenido](/downloads/apps/erasmushomes-control.html)",
        "- **Aplicación / producción:** no hay una URL de producto ErasmusHomes desplegada.", "",
        '<div class="eh-dashboard">',
        f'<section class="eh-hero"><p class="eh-kicker">Objetivo diciembre</p><h2>{esc(data.get("target", "Piloto comercial público"))}</h2><div class="eh-sync eh-sync--{sync_state}">{state_label}</div><dl><dt>SHA ErasmusHomes main</dt><dd><code>{esc(sha)}</code></dd><dt>Última sincronización</dt><dd>{esc(human_datetime(synced_at))}</dd></dl><div class="eh-agreed-document"><a href="{esc(document["url"])}" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (PDF)</a><span><b>Archivo:</b> {esc(document["name"])}</span><span><b>Git:</b> <code>{esc(sha[:8])}</code> · <a href="{esc(document["source_url"])}" target="_blank" rel="noopener noreferrer">ver fuente versionada</a></span><span><b>SHA-256:</b> <code>{esc(document["sha256"])}</code></span><span><b>Fecha:</b> {esc(human_date(document["version_date"]))}</span></div></section>',
        '<section class="eh-metrics">',
        f'<article><strong>{percent}%</strong><span>completado</span></article>',
    ]
    for status in STATUSES:
        lines.append(f'<article class="eh-metric eh-status--{status}"><strong>{counts[status]}</strong><span>{LABELS[status]}</span></article>')
    lines += ["</section>", '<section class="eh-gate"><h2>Próximo gate</h2>']
    if next_gate:
        lines.append(f'<p><strong>{esc(next_gate["id"])} · {esc(next_gate["title"])}</strong><br>{esc(next_gate["weekend_validation"])}</p>')
    lines += ["</section>", '<section><h2>Esta semana</h2><div class="eh-priorities">']
    for task in active:
        lines.append(f'<article><strong>{esc(task["id"])}</strong><h3>{esc(task["title"])}</h3><p>{esc(task["objective"])}</p><p><b>Validación sábado/domingo:</b> {esc(task["weekend_validation"])}</p></article>')
    if not active:
        lines.append("<p>No hay tareas en ejecución.</p>")
    lines += ["</div></section>", '<section><h2>Kanban</h2><div class="eh-kanban">']
    for status in STATUSES:
        lines.append(f'<div class="eh-column eh-status--{status}"><h3>{LABELS[status]} · {counts[status]}</h3>')
        for task in [item for item in tasks if item["status"] == status]:
            risks = ", ".join(map(str, task["risks"])) or "Sin riesgo declarado"
            evidence = task["evidence"]
            link = f'<a href="{esc(evidence["url"])}">Evidencia</a>' if evidence["url"] else "Evidencia pendiente"
            blocked = f'<p><b>Bloqueo:</b> {esc(task["blocker_reason"])}</p>' if task["blocker_reason"] else ""
            lines.append(f'<article class="eh-task"><span>{esc(task["id"])}</span><h4>{esc(task["title"])}</h4><p><b>Objetivo:</b> {esc(task["objective"])}</p><p><b>Terminado:</b> {esc(task["definition_of_done"])}</p><p><b>Riesgos:</b> {esc(risks)}</p>{blocked}<p>{link}</p></article>')
        lines.append("</div>")
    lines += ["</div></section>", '<section><h2>Línea temporal hasta el 20 de diciembre</h2><ol class="eh-timeline">']
    for task in tasks:
        lines.append(f'<li class="eh-status--{task["status"]}"><time>{human_date(task["week_start"])} - {human_date(task["week_end"])}</time><strong>{esc(task["title"])}</strong><span>{LABELS[task["status"]]}</span></li>')
    lines += ["</ol></section>", "</div>", "", "La fuente canónica es `ratienza/ErasmusHomes/docs/board/roadmap.yaml`. Esta página es un artefacto derivado.", ""]
    return "\n".join(lines)


def render_standalone(data: dict, sha: str, synced_at: str, sync_state: str, document: dict) -> str:
    tasks = validate(data)
    validate_document(document, sha)
    counts = {status: sum(task["status"] == status for task in tasks) for status in STATUSES}
    percent = round(counts["done"] * 100 / len(tasks))
    active = next((task for task in tasks if task["status"] == "in_progress"), None)
    next_step = next((task for task in tasks if task["status"] == "pending"), None)
    priorities = [task for task in tasks if task["status"] == "pending"][:3]
    blockers = [task for task in tasks if task["status"] == "blocked"]
    state_label = {"synchronized": "Sincronizado", "stale": "Desactualizado", "error": "Error de sincronización"}[sync_state]
    content = [
        '<!doctype html><html lang="es"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<title>ErasmusHomes · Control del MVP</title>',
        f'<style>{FINAL_CSS}</style></head><body><main class="shell">',
        f'<header class="topbar"><div class="topbar-left"><span class="mark">EH</span><span>ErasmusHomes<br><small class="brand-small">Control del MVP</small></span></div><span class="sync">{state_label}</span></header>',
        '<section class="hero"><div><p class="eyebrow">Dirección del piloto · diciembre 2026</p>',
        '<h1>ErasmusHomes · Control del MVP</h1>',
        '<p class="hero-copy">Objetivo: piloto público durante la semana del <b>30-11-2026</b>.</p>',
        f'<p class="progressline">{counts["done"]} de {len(tasks)} hitos cerrados · {percent}%</p>',
        f'<div class="statusline"><span>SHA <code>{esc(sha[:8])}</code></span><span>Generado {human_datetime(synced_at)}</span><span>Fuente: GitHub main</span></div></div>',
        '<aside class="source"><h2>Documento de contraste</h2>',
        f'<a class="pdf-button" href="{esc(document["url"])}" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (PDF) ↗</a>',
        f'<dl class="meta"><div><dt>Archivo</dt><dd>{esc(document["name"])}</dd></div><div><dt>Fecha</dt><dd>{human_date(document["version_date"])}</dd></div><div><dt>Git</dt><dd><code>{esc(sha[:8])}</code> · <a href="{esc(document["source_url"])}" target="_blank" rel="noopener noreferrer">PDF versionado</a></dd></div><div><dt>SHA-256</dt><dd><code>{esc(document["sha256"])}</code></dd></div></dl>',
        f'<nav class="trace-links" aria-label="Fuentes canónicas"><a href="{esc(document["markdown_url"])}" target="_blank" rel="noopener noreferrer">Markdown ↗</a><a href="{esc(document["yaml_url"])}" target="_blank" rel="noopener noreferrer">YAML ↗</a></nav></aside></section>',
        '<section class="panel now"><p class="eyebrow">Ahora</p><div class="now-grid">',
    ]
    if active:
        content.append(f'<div><span class="label">Tarea activa</span><h2 class="active-title">{esc(active["id"])} · {esc(active["title"])}</h2><p>{esc(active["objective"])}</p></div><div><span class="label">Sprint activo</span><div class="value">{esc(active["sprint"])}</div><small>{human_date(active["week_start"])} - {human_date(active["week_end"])}</small></div><div><span class="label">Próximo gate</span><div class="value">{esc(active["next_decision"])}</div></div><div><span class="label">Validación sábado/domingo</span><div class="value">{esc(active["weekend_validation"])}</div></div>')
    else:
        content.append(f'<div><span class="label">Tarea activa</span><h2 class="active-title">Sin tarea activa</h2><p><b>Próximo paso</b><br>{esc(next_step["id"])} · {esc(next_step["title"])}</p></div><div><span class="label">Sprint</span><div class="value">Pendiente de inicio</div></div><div><span class="label">Próximo gate</span><div class="value">{esc(next_step["next_decision"])}</div></div><div><span class="label">Validación sábado/domingo</span><div class="value">{esc(next_step["weekend_validation"])}</div></div>')
    content += ['</div></section><section class="summary"><div class="panel"><h2 class="section-title">Resumen y próximos objetivos</h2><div class="compact-counts">']
    for status in STATUSES:
        content.append(f'<span class="count">{LABELS[status]} {counts[status]}</span>')
    content.append('</div><div class="priorities">')
    for task in priorities:
        content.append(f'<article class="priority"><strong>{esc(task["id"])} · {esc(task["title"])}</strong><small>{human_date(task["week_start"])} - {human_date(task["week_end"])} · {LABELS[task["status"]]}</small><p>{esc(task["objective"])}</p><small><b>Validación:</b> {esc(task["weekend_validation"])}</small></article>')
    content.append('</div></div><aside class="panel"><h2 class="section-title">Riesgos y bloqueos activos</h2>')
    if blockers:
        content.append('<ul class="risks">' + ''.join(f'<li><b>{esc(task["id"])}</b>: {esc(task["blocker_reason"])} · {esc(task["next_decision"])}</li>' for task in blockers) + '</ul>')
    else:
        content.append('<p>Sin bloqueos activos. La aceptación visual de EH-002R-C es la decisión pendiente.</p>')
    content.append(f'<p><b>Próximo gate:</b> {esc(active["next_decision"] if active else next_step["next_decision"])}</p></aside></section>')
    content.append('<section class="panel board"><p class="eyebrow">Explorar por estado</p><h2 class="section-title">Tablero Scrum-lite</h2><div class="tabs" role="tablist">')
    for index, status in enumerate(STATUSES):
        content.append(f'<button class="tab" role="tab" id="tab-{status}" aria-controls="panel-{status}" aria-selected="{"true" if index == 1 else "false"}" data-status="{status}">{LABELS[status]} ({counts[status]})</button>')
    content.append('</div>')
    for status in STATUSES:
        status_tasks = [task for task in tasks if task["status"] == status]
        content.append(f'<section class="tab-panel" id="panel-{status}" role="tabpanel" aria-labelledby="tab-{status}" {"hidden" if status != "in_progress" else ""}><div class="task-browser"><div class="task-list">')
        for index, task in enumerate(status_tasks):
            selected = "true" if index == 0 else "false"
            content.append(f'<button class="task-select" aria-selected="{selected}" data-detail="{status}-{index}"><b>{esc(task["id"])} · {esc(task["title"])}</b><span>{esc(task["sprint"])} · {human_date(task["week_start"])} - {human_date(task["week_end"])}</span></button>')
        content.append('</div><div>')
        for index, task in enumerate(status_tasks):
            risks = ", ".join(map(str, task["risks"])) or "Sin riesgos declarados"
            evidence = task["evidence"]
            evidence_html = f'<a href="{esc(evidence["url"])}" target="_blank" rel="noopener noreferrer">PR {esc(evidence["pr"])} · {esc(str(evidence["commit"])[:8])} ↗</a>' if evidence["url"] else "Evidencia pendiente"
            content.append(f'<article class="task-detail {"mobile-open" if index == 0 else ""}" id="detail-{status}-{index}" {"hidden" if index != 0 else ""}><span class="label">{esc(task["id"])} · {LABELS[status]}</span><h3>{esc(task["title"])}</h3><div class="detail-grid"><div class="detail-box"><span class="label">Objetivo</span><p>{esc(task["objective"])}</p></div><div class="detail-box"><span class="label">Definición de terminado</span><p>{esc(task["definition_of_done"])}</p></div><div class="detail-box"><span class="label">Validación sábado/domingo</span><p>{esc(task["weekend_validation"])}</p></div><div class="detail-box"><span class="label">Riesgos / bloqueo</span><p>{esc(risks)}</p><p>{esc(task["blocker_reason"] or "Sin bloqueo activo")}</p></div><div class="detail-box"><span class="label">Decisión siguiente</span><p>{esc(task["next_decision"])}</p></div><div class="detail-box evidence"><span class="label">Evidencia</span><p>{evidence_html}</p></div></div></article>')
        content.append('</div></div></section>')
    content.append('</section><section class="panel" style="margin-top:18px"><p class="eyebrow">Horizonte</p><h2 class="section-title">Timeline hasta diciembre</h2><ol class="timeline">')
    for task in tasks:
        content.append(f'<li class="{task["status"]}"><time>{human_date(task["week_start"])} - {human_date(task["week_end"])}</time><strong>{esc(task["title"])}</strong><span>{LABELS[task["status"]]}</span></li>')
    content += ['</ol></section><footer class="footer">Artefacto derivado de ErasmusHomes Git main · Nexus no es fuente de edición</footer></main>',
        '<script>const tabs=[...document.querySelectorAll(".tab")];tabs.forEach(tab=>tab.addEventListener("click",()=>{tabs.forEach(t=>t.setAttribute("aria-selected",String(t===tab)));document.querySelectorAll(".tab-panel").forEach(p=>p.hidden=p.id!=="panel-"+tab.dataset.status)}));document.querySelectorAll(".task-select").forEach(button=>button.addEventListener("click",()=>{const panel=button.closest(".tab-panel");panel.querySelectorAll(".task-select").forEach(b=>b.setAttribute("aria-selected",String(b===button)));panel.querySelectorAll(".task-detail").forEach(d=>{const selected=d.id==="detail-"+button.dataset.detail;d.hidden=!selected;d.classList.toggle("mobile-open",selected)});button.scrollIntoView({block:"nearest"})}));</script></body></html>']
    return "".join(content)


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def document_manifest(repo: Path, pdf_path: Path) -> tuple[str, str]:
    digest = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    manifest = repo / "docs/source/SHA256SUMS"
    for raw_line in manifest.read_text(encoding="utf-8").splitlines():
        parts = [part.strip() for part in raw_line.split("|")]
        if len(parts) == 4 and parts[1] == pdf_path.name:
            if parts[0] != digest:
                raise ValueError("agreed roadmap PDF differs from its SHA256SUMS entry")
            dt.date.fromisoformat(parts[3])
            return digest, parts[3]
    raise ValueError("agreed roadmap PDF is missing from SHA256SUMS")


def generate(repo: Path, output: Path, cache: Path, metadata: Path, document_output: Path, standalone_output: Path) -> dict:
    source = repo / "docs" / "board" / "roadmap.yaml"
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    validate(data)
    sha = git(repo, "rev-parse", "HEAD")
    branch = git(repo, "branch", "--show-current")
    try:
        main_sha = git(repo, "rev-parse", "origin/main")
    except subprocess.CalledProcessError:
        main_sha = ""
    sync_state = "synchronized" if branch == "main" and sha == main_sha else "stale"
    synced_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    pdf_path = repo / PDF_RELATIVE_PATH
    if not pdf_path.is_file():
        raise ValueError(f"agreed roadmap document is missing: {PDF_RELATIVE_PATH}")
    document_sha256, document_version_date = document_manifest(repo, pdf_path)
    document = {
        "name": pdf_path.name,
        "sha256": document_sha256,
        "version_date": document_version_date,
        "url": f"/downloads/erasmushomes/{PDF_RELATIVE_PATH.name}",
        "source_url": f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/{PDF_RELATIVE_PATH.as_posix()}",
        "markdown_url": f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/docs/ROADMAP_MVP_DICIEMBRE_2026.md",
        "yaml_url": f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/docs/board/roadmap.yaml",
    }
    page = render(data, sha, synced_at, sync_state, document)
    standalone = render_standalone(data, sha, synced_at, sync_state, document)
    meta = {"source": "ratienza/ErasmusHomes/docs/board/roadmap.yaml", "sha": sha, "main_sha": main_sha, "branch": branch, "synced_at": synced_at, "state": sync_state, "document": document}
    atomic_write(output, page.encode())
    atomic_write(cache, source.read_bytes())
    atomic_write(metadata, (json.dumps(meta, ensure_ascii=False, indent=2) + "\n").encode())
    atomic_write(document_output, pdf_path.read_bytes())
    atomic_write(standalone_output, standalone.encode())
    return meta


def check(output: Path, cache: Path, metadata: Path, document_output: Path, standalone_output: Path) -> None:
    data = yaml.safe_load(cache.read_text(encoding="utf-8"))
    meta = json.loads(metadata.read_text(encoding="utf-8"))
    expected = render(data, meta["sha"], meta["synced_at"], meta["state"], meta["document"])
    if output.read_text(encoding="utf-8") != expected:
        raise ValueError("generated ErasmusHomes panel is stale")
    if hashlib.sha256(document_output.read_bytes()).hexdigest() != meta["document"]["sha256"]:
        raise ValueError("published agreed roadmap PDF hash differs from metadata")
    expected_standalone = render_standalone(data, meta["sha"], meta["synced_at"], meta["state"], meta["document"])
    if standalone_output.read_text(encoding="utf-8") != expected_standalone:
        raise ValueError("standalone ErasmusHomes control is stale")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["generate", "check"])
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/aplicaciones/erasmushomes-control.md")
    parser.add_argument("--cache", type=Path, default=ROOT / "data/erasmushomes/roadmap.yaml")
    parser.add_argument("--metadata", type=Path, default=ROOT / "data/erasmushomes/sync.json")
    parser.add_argument("--document-output", type=Path, default=ROOT / f"docs/downloads/erasmushomes/{PDF_RELATIVE_PATH.name}")
    parser.add_argument("--standalone-output", type=Path, default=ROOT / "docs/control/erasmushomes/index.html")
    args = parser.parse_args()
    if args.command == "generate":
        if not args.repo:
            parser.error("generate requires --repo")
        print(json.dumps(generate(args.repo.resolve(), args.output, args.cache, args.metadata, args.document_output, args.standalone_output), ensure_ascii=False))
    else:
        check(args.output, args.cache, args.metadata, args.document_output, args.standalone_output)
        print("ErasmusHomes panel synchronized")


if __name__ == "__main__":
    main()
