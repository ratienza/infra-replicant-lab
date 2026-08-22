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


def generate(repo: Path, output: Path, cache: Path, metadata: Path, document_output: Path) -> dict:
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
    meta = {"source": "ratienza/ErasmusHomes/docs/board/roadmap.yaml", "sha": sha, "main_sha": main_sha, "branch": branch, "synced_at": synced_at, "state": sync_state, "document": document}
    atomic_write(output, page.encode())
    atomic_write(cache, source.read_bytes())
    atomic_write(metadata, (json.dumps(meta, ensure_ascii=False, indent=2) + "\n").encode())
    atomic_write(document_output, docx_path.read_bytes())
    return meta


def check(output: Path, cache: Path, metadata: Path, document_output: Path) -> None:
    data = yaml.safe_load(cache.read_text(encoding="utf-8"))
    meta = json.loads(metadata.read_text(encoding="utf-8"))
    expected = render(data, meta["sha"], meta["synced_at"], meta["state"], meta["document"])
    if output.read_text(encoding="utf-8") != expected:
        raise ValueError("generated ErasmusHomes panel is stale")
    if hashlib.sha256(document_output.read_bytes()).hexdigest() != meta["document"]["sha256"]:
        raise ValueError("published agreed roadmap DOCX hash differs from metadata")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["generate", "check"])
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT / "docs/aplicaciones/erasmushomes-control.md")
    parser.add_argument("--cache", type=Path, default=ROOT / "data/erasmushomes/roadmap.yaml")
    parser.add_argument("--metadata", type=Path, default=ROOT / "data/erasmushomes/sync.json")
    parser.add_argument("--document-output", type=Path, default=ROOT / f"docs/downloads/erasmushomes/{DOCX_RELATIVE_PATH.name}")
    args = parser.parse_args()
    if args.command == "generate":
        if not args.repo:
            parser.error("generate requires --repo")
        print(json.dumps(generate(args.repo.resolve(), args.output, args.cache, args.metadata, args.document_output), ensure_ascii=False))
    else:
        check(args.output, args.cache, args.metadata, args.document_output)
        print("ErasmusHomes panel synchronized")


if __name__ == "__main__":
    main()
