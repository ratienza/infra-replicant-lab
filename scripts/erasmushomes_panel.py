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
FIELDS = {"id", "title", "phase", "week_start", "week_end", "status", "owner", "objective", "definition_of_done", "weekend_validation", "evidence", "risks", "blocker_reason", "updated_at", "notes"}
DOCX_RELATIVE_PATH = Path("docs/source/Roadmap_ErasmusHomes_MVP_Diciembre_2026.docx")
STANDALONE_CSS = r"""
:root{color-scheme:light;--ink:#172033;--muted:#667085;--line:#d9e1eb;--paper:#fff;--soft:#f4f7fb;--brand:#3457d5;--done:#18864b;--progress:#2768d8;--pending:#778195;--blocked:#c93645;--shadow:0 18px 50px rgba(29,45,78,.10)}
*{box-sizing:border-box}html{background:#eef3f9}body{margin:0;color:var(--ink);background:linear-gradient(180deg,#edf3fb 0,#f8fafc 24rem,#f4f7fb 100%);font:15px/1.55 Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}a{color:var(--brand)}code{overflow-wrap:anywhere;font:600 .86em ui-monospace,SFMono-Regular,Consolas,monospace}.shell{width:min(1440px,calc(100% - 48px));margin:auto;padding:32px 0 64px}.topbar{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-bottom:22px}.brand{display:flex;align-items:center;gap:12px;font-weight:800}.brand-mark{display:grid;width:38px;height:38px;place-items:center;border-radius:12px;color:#fff;background:var(--brand);box-shadow:var(--shadow)}.sync{padding:7px 12px;border-radius:999px;color:#fff;background:var(--done);font-size:13px;font-weight:800}.hero{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(300px,.55fr);gap:22px;padding:clamp(24px,4vw,52px);border:1px solid #d6e0ee;border-radius:24px;background:rgba(255,255,255,.94);box-shadow:var(--shadow)}.eyebrow{margin:0 0 9px;color:var(--brand);font-size:12px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}.hero h1{max-width:840px;margin:0;font-size:clamp(32px,5vw,62px);line-height:1.04;letter-spacing:-.045em}.hero-copy{max-width:760px;margin:18px 0 0;color:var(--muted);font-size:clamp(16px,1.5vw,20px)}.source-card{align-self:stretch;padding:22px;border:1px solid var(--line);border-radius:18px;background:var(--soft)}.source-card h2{margin:0 0 14px;font-size:17px}.docx-button{display:inline-flex;align-items:center;justify-content:center;width:100%;min-height:48px;padding:11px 15px;border-radius:12px;color:#fff;background:var(--brand);font-weight:900;text-align:center;text-decoration:none}.meta{display:grid;gap:8px;margin:16px 0 0}.meta div{min-width:0}.meta dt{color:var(--muted);font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}.meta dd{margin:1px 0 0;overflow-wrap:anywhere}.metrics{display:grid;grid-template-columns:1.25fr repeat(4,1fr);gap:14px;margin:22px 0}.metric{min-width:0;padding:20px;border:1px solid var(--line);border-radius:17px;background:var(--paper)}.metric strong{display:block;font-size:31px;line-height:1}.metric span{display:block;margin-top:7px;color:var(--muted);font-size:13px}.metric.primary{color:#fff;border:0;background:linear-gradient(135deg,#253f9b,#4771ea)}.metric.primary span{color:#dfe7ff}.workspace{display:grid;grid-template-columns:minmax(0,1.55fr) minmax(300px,.45fr);gap:20px}.panel{padding:24px;border:1px solid var(--line);border-radius:20px;background:var(--paper)}.panel-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:17px}.panel h2{margin:0;font-size:22px;letter-spacing:-.02em}.panel-note{margin:3px 0 0;color:var(--muted);font-size:13px}.gate{padding:18px;border-left:5px solid var(--brand);border-radius:12px;background:#f2f5ff}.gate strong{display:block;margin-bottom:4px}.priorities{display:grid;gap:12px;margin-top:14px}.priority{padding:16px;border:1px solid var(--line);border-radius:14px}.priority b{color:var(--brand)}.kanban{display:grid;grid-template-columns:repeat(4,minmax(230px,1fr));gap:14px;overflow-x:auto;padding:2px 2px 10px}.column{min-width:230px;padding:14px;border-top:4px solid var(--color);border-radius:14px;background:var(--soft)}.column h3{display:flex;justify-content:space-between;margin:0 0 12px;color:var(--color);font-size:15px}.task{margin-top:10px;padding:14px;border:1px solid var(--line);border-radius:12px;background:#fff}.task-id{color:var(--color);font-size:11px;font-weight:900}.task h4{margin:4px 0 8px;font-size:14px;line-height:1.25}.task p{margin:6px 0;color:var(--muted);font-size:12px}.timeline{display:grid;gap:8px;margin:0;padding:0;list-style:none}.timeline li{display:grid;grid-template-columns:165px minmax(0,1fr) auto;gap:12px;align-items:center;padding:11px 13px;border-left:4px solid var(--color);border-radius:9px;background:var(--soft)}.timeline time,.timeline span{color:var(--muted);font-size:12px}.footer{margin-top:24px;color:var(--muted);font-size:12px;text-align:center}.status-done{--color:var(--done)}.status-in_progress{--color:var(--progress)}.status-pending{--color:var(--pending)}.status-blocked{--color:var(--blocked)}
@media(max-width:1100px){.hero,.workspace{grid-template-columns:1fr}.metrics{grid-template-columns:repeat(5,minmax(145px,1fr));overflow-x:auto}.source-card{display:grid;grid-template-columns:minmax(220px,.65fr) 1fr;gap:16px;align-items:start}.source-card h2{grid-column:1/-1}.kanban{grid-template-columns:repeat(2,minmax(0,1fr));overflow:visible}.column{min-width:0}}
@media(max-width:820px){.shell{width:min(100% - 28px,1440px);padding-top:18px}.hero{padding:25px;border-radius:18px}.source-card{grid-template-columns:1fr}.metrics{grid-template-columns:repeat(2,1fr);overflow:visible}.metric.primary{grid-column:1/-1}.panel{padding:18px}.timeline li{grid-template-columns:1fr}.timeline span{justify-self:start}.topbar{align-items:flex-start}}
@media(max-width:520px){body{font-size:14px}.shell{width:min(100% - 20px,1440px)}.brand-copy small{display:none}.hero{padding:20px}.hero h1{font-size:34px}.metrics{gap:10px}.metric{padding:16px}.metric strong{font-size:27px}.panel-head{display:block}.kanban{grid-template-columns:1fr;overflow:visible}.column{min-width:0}.source-card{padding:17px}.docx-button{font-size:14px}.sync{font-size:11px}.timeline li{padding:10px}.workspace{gap:14px}}
"""


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-c", f"safe.directory={repo}", "-C", str(repo), *args], text=True).strip()


def validate(data: dict) -> list[dict]:
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or not tasks:
        raise ValueError("roadmap.yaml requires a non-empty tasks list")
    seen: set[str] = set()
    for task in tasks:
        if set(task) != FIELDS:
            raise ValueError(f"{task.get('id', '?')}: invalid fields")
        task_id = str(task["id"])
        if task_id in seen or not re.fullmatch(r"(?:EH-\d{3}|W-\d{4}-\d{2}-\d{2})", task_id):
            raise ValueError(f"invalid or duplicate id: {task_id}")
        seen.add(task_id)
        if task["status"] not in STATUSES:
            raise ValueError(f"{task_id}: unknown status")
        evidence = task["evidence"]
        if set(evidence) != {"pr", "commit", "url"}:
            raise ValueError(f"{task_id}: invalid evidence")
        if task["status"] == "done" and not all(str(value).strip() for value in evidence.values()):
            raise ValueError(f"{task_id}: done without complete evidence")
        if task["status"] == "blocked" and not str(task["blocker_reason"]).strip():
            raise ValueError(f"{task_id}: blocked without reason")
        url = str(evidence["url"]).strip()
        if url:
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.hostname != "github.com" or not parsed.path.startswith("/ratienza/ErasmusHomes/"):
                raise ValueError(f"{task_id}: evidence URL is not an approved GitHub URL")
    return tasks


def esc(value: object) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def validate_document(document: dict, sha: str) -> None:
    required = {"name", "sha256", "version_date", "url", "source_url"}
    if set(document) != required:
        raise ValueError("invalid agreed roadmap document metadata")
    if document["name"] != DOCX_RELATIVE_PATH.name:
        raise ValueError("unexpected agreed roadmap filename")
    if not re.fullmatch(r"[0-9a-f]{64}", document["sha256"]):
        raise ValueError("invalid agreed roadmap SHA-256")
    if document["url"] != f"/downloads/erasmushomes/{DOCX_RELATIVE_PATH.name}":
        raise ValueError("unexpected published agreed roadmap URL")
    expected_source_url = f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/{DOCX_RELATIVE_PATH.as_posix()}"
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
        f'<section class="eh-hero"><p class="eh-kicker">Objetivo diciembre</p><h2>{esc(data.get("target", "Piloto comercial público"))}</h2><div class="eh-sync eh-sync--{sync_state}">{state_label}</div><dl><dt>SHA ErasmusHomes main</dt><dd><code>{esc(sha)}</code></dd><dt>Última sincronización</dt><dd>{esc(synced_at)}</dd></dl><div class="eh-agreed-document"><a href="{esc(document["url"])}" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (DOCX)</a><span><b>Archivo:</b> {esc(document["name"])}</span><span><b>Git:</b> <code>{esc(sha[:8])}</code> · <a href="{esc(document["source_url"])}" target="_blank" rel="noopener noreferrer">ver fuente versionada</a></span><span><b>SHA-256:</b> <code>{esc(document["sha256"])}</code></span><span><b>Fecha:</b> {esc(document["version_date"])}</span></div></section>',
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
        lines.append(f'<li class="eh-status--{task["status"]}"><time>{esc(task["week_start"])} - {esc(task["week_end"])}</time><strong>{esc(task["title"])}</strong><span>{LABELS[task["status"]]}</span></li>')
    lines += ["</ol></section>", "</div>", "", "La fuente canónica es `ratienza/ErasmusHomes/docs/board/roadmap.yaml`. Esta página es un artefacto derivado.", ""]
    return "\n".join(lines)


def render_standalone(data: dict, sha: str, synced_at: str, sync_state: str, document: dict) -> str:
    tasks = validate(data)
    validate_document(document, sha)
    counts = {status: sum(task["status"] == status for task in tasks) for status in STATUSES}
    percent = round(counts["done"] * 100 / len(tasks))
    active = [task for task in tasks if task["status"] == "in_progress"][:3]
    next_gate = next((task for task in tasks if task["status"] in {"in_progress", "pending", "blocked"}), None)
    state_label = {"synchronized": "Sincronizado", "stale": "Desactualizado", "error": "Error de sincronización"}[sync_state]
    content = [
        '<!doctype html><html lang="es"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        '<title>ErasmusHomes · Control del MVP</title>',
        f'<style>{STANDALONE_CSS}</style></head><body><main class="shell">',
        f'<header class="topbar"><div class="brand"><span class="brand-mark">EH</span><span class="brand-copy">ErasmusHomes<br><small>Control interno del MVP</small></span></div><span class="sync">{state_label}</span></header>',
        '<section class="hero"><div><p class="eyebrow">Dirección · horizonte diciembre 2026</p>',
        f'<h1>{esc(data.get("target", "Piloto comercial público"))}</h1>',
        '<p class="hero-copy">Una vista ejecutiva del trabajo real: qué está terminado, qué viene ahora y qué evidencia sostiene cada decisión.</p></div>',
        '<aside class="source-card"><h2>Documento acordado</h2>',
        f'<a class="docx-button" href="{esc(document["url"])}" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (DOCX)</a>',
        f'<dl class="meta"><div><dt>Archivo</dt><dd>{esc(document["name"])}</dd></div><div><dt>Git</dt><dd><code>{esc(sha[:8])}</code> · <a href="{esc(document["source_url"])}" target="_blank" rel="noopener noreferrer">fuente versionada</a></dd></div><div><dt>SHA-256</dt><dd><code>{esc(document["sha256"])}</code></dd></div><div><dt>Fecha</dt><dd>{esc(document["version_date"])}</dd></div><div><dt>Última sincronización</dt><dd>{esc(synced_at)}</dd></div></dl></aside></section>',
        '<section class="metrics" aria-label="Resumen de progreso">',
        f'<article class="metric primary"><strong>{percent}%</strong><span>del roadmap completado</span></article>',
    ]
    for status in STATUSES:
        content.append(f'<article class="metric status-{status}"><strong>{counts[status]}</strong><span>{LABELS[status]}</span></article>')
    content += ['</section><section class="workspace"><div class="panel"><div class="panel-head"><div><h2>Foco inmediato</h2><p class="panel-note">La siguiente decisión que mueve el MVP.</p></div></div>']
    if next_gate:
        content.append(f'<div class="gate"><strong>{esc(next_gate["id"])} · {esc(next_gate["title"])}</strong>{esc(next_gate["weekend_validation"])}</div>')
    content.append('<div class="priorities">')
    if active:
        for task in active:
            content.append(f'<article class="priority"><b>{esc(task["id"])}</b><h3>{esc(task["title"])}</h3><p>{esc(task["objective"])}</p><small><b>Validación:</b> {esc(task["weekend_validation"])}</small></article>')
    else:
        content.append('<article class="priority"><b>Sin tareas en ejecución</b><p>El siguiente gate pendiente queda preparado para priorización.</p></article>')
    content += ['</div></div><aside class="panel"><h2>Lectura rápida</h2><p class="panel-note">Este panel se genera desde Git. No se edita en Nexus.</p>', f'<dl class="meta"><div><dt>SHA ErasmusHomes main</dt><dd><code>{esc(sha)}</code></dd></div><div><dt>Fuente</dt><dd><code>docs/board/roadmap.yaml</code></dd></div><div><dt>Tareas</dt><dd>{len(tasks)} en total</dd></div></dl></aside></section>', '<section class="panel" style="margin-top:20px"><div class="panel-head"><div><h2>Tablero de ejecución</h2><p class="panel-note">Objetivo, criterio de terminado, riesgo y evidencia en un solo lugar.</p></div></div><div class="kanban">']
    for status in STATUSES:
        content.append(f'<section class="column status-{status}"><h3><span>{LABELS[status]}</span><span>{counts[status]}</span></h3>')
        for task in (item for item in tasks if item["status"] == status):
            risks = ", ".join(map(str, task["risks"])) or "Sin riesgo declarado"
            evidence = task["evidence"]
            link = f'<a href="{esc(evidence["url"])}" target="_blank" rel="noopener noreferrer">Ver evidencia</a>' if evidence["url"] else "Evidencia pendiente"
            content.append(f'<article class="task"><span class="task-id">{esc(task["id"])}</span><h4>{esc(task["title"])}</h4><p><b>Objetivo:</b> {esc(task["objective"])}</p><p><b>Terminado:</b> {esc(task["definition_of_done"])}</p><p><b>Riesgo:</b> {esc(risks)}</p><p>{link}</p></article>')
        content.append('</section>')
    content += ['</div></section><section class="panel" style="margin-top:20px"><div class="panel-head"><div><h2>Camino hasta el 20 de diciembre</h2><p class="panel-note">Secuencia de validación, construcción y lanzamiento.</p></div></div><ol class="timeline">']
    for task in tasks:
        content.append(f'<li class="status-{task["status"]}"><time>{esc(task["week_start"])} → {esc(task["week_end"])}</time><strong>{esc(task["title"])}</strong><span>{LABELS[task["status"]]}</span></li>')
    content += ['</ol></section><footer class="footer">Panel autónomo generado desde ErasmusHomes Git main · sin edición manual en Nexus</footer></main></body></html>']
    return "".join(content)


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    temporary.replace(path)


def document_manifest(repo: Path, docx_path: Path) -> tuple[str, str]:
    digest = hashlib.sha256(docx_path.read_bytes()).hexdigest()
    manifest = repo / "docs/source/SHA256SUMS"
    for raw_line in manifest.read_text(encoding="utf-8").splitlines():
        parts = [part.strip() for part in raw_line.split("|")]
        if len(parts) == 4 and parts[1] == docx_path.name:
            if parts[0] != digest:
                raise ValueError("agreed roadmap DOCX differs from its SHA256SUMS entry")
            dt.date.fromisoformat(parts[3])
            return digest, parts[3]
    raise ValueError("agreed roadmap DOCX is missing from SHA256SUMS")


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
    docx_path = repo / DOCX_RELATIVE_PATH
    if not docx_path.is_file():
        raise ValueError(f"agreed roadmap document is missing: {DOCX_RELATIVE_PATH}")
    document_sha256, document_version_date = document_manifest(repo, docx_path)
    document = {
        "name": docx_path.name,
        "sha256": document_sha256,
        "version_date": document_version_date,
        "url": f"/downloads/erasmushomes/{DOCX_RELATIVE_PATH.name}",
        "source_url": f"https://github.com/ratienza/ErasmusHomes/blob/{sha}/{DOCX_RELATIVE_PATH.as_posix()}",
    }
    page = render(data, sha, synced_at, sync_state, document)
    standalone = render_standalone(data, sha, synced_at, sync_state, document)
    meta = {"source": "ratienza/ErasmusHomes/docs/board/roadmap.yaml", "sha": sha, "main_sha": main_sha, "branch": branch, "synced_at": synced_at, "state": sync_state, "document": document}
    atomic_write(output, page.encode())
    atomic_write(cache, source.read_bytes())
    atomic_write(metadata, (json.dumps(meta, ensure_ascii=False, indent=2) + "\n").encode())
    atomic_write(document_output, docx_path.read_bytes())
    atomic_write(standalone_output, standalone.encode())
    return meta


def check(output: Path, cache: Path, metadata: Path, document_output: Path, standalone_output: Path) -> None:
    data = yaml.safe_load(cache.read_text(encoding="utf-8"))
    meta = json.loads(metadata.read_text(encoding="utf-8"))
    expected = render(data, meta["sha"], meta["synced_at"], meta["state"], meta["document"])
    if output.read_text(encoding="utf-8") != expected:
        raise ValueError("generated ErasmusHomes panel is stale")
    if hashlib.sha256(document_output.read_bytes()).hexdigest() != meta["document"]["sha256"]:
        raise ValueError("published agreed roadmap DOCX hash differs from metadata")
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
    parser.add_argument("--document-output", type=Path, default=ROOT / f"docs/downloads/erasmushomes/{DOCX_RELATIVE_PATH.name}")
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
