#!/usr/bin/env python3
"""Build and validate the canonical MkDocs site and derived portable artifacts."""

from __future__ import annotations

import argparse
import functools
import hashlib
import html
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import threading
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

import markdown
import pymdownx.superfences
from mkdocs.config import load_config
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BUILD = ROOT / ".build" / "docs-pipeline"
SITE = BUILD / "site"
CANONICAL_HTML = DOCS / "downloads" / "Replicant-Lab.html"
CANONICAL_PDF = DOCS / "downloads" / "Replicant-Lab.pdf"
MERMAID_RUNTIME = DOCS / "javascripts" / "mermaid.min.js"
MERMAID_PACKAGE_RUNTIME = ROOT / "node_modules" / "mermaid" / "dist" / "mermaid.min.js"
PORTABLE_CSS = ROOT / "scripts" / "portable.css"
NODE_RENDERER = ROOT / "scripts" / "render_portables.mjs"
EXPECTED_MERMAID = 5
EXPECTED_PDF_PAGES = 42
PIPELINE_VERSION = "2"

MERMAID_FENCE = re.compile(r"^```mermaid\s*$\n(.*?)^```\s*$", re.MULTILINE | re.DOTALL)
ID_ATTR = re.compile(r'\bid="([^"]+)"')
HREF_ANCHOR = re.compile(r'href="#([^"]+)"')

class ResourceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.references: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name.lower() in {"src", "href"} and value:
                self.references.append((tag.lower(), name.lower(), value))


def resource_references(document: str) -> list[tuple[str, str, str]]:
    parser = ResourceParser()
    parser.feed(document)
    return parser.references


def run(command: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None) -> None:
    printable = " ".join(command)
    print(f"+ {printable}")
    subprocess.run(command, cwd=cwd, env=env, check=True)


def nav_pages() -> list[tuple[list[str], str]]:
    config = load_config(config_file=str(ROOT / "mkdocs.yml"))
    result: list[tuple[list[str], str]] = []

    def walk(items: list[object], parents: list[str]) -> None:
        for item in items:
            if isinstance(item, str):
                result.append((parents + [Path(item).stem], item))
            elif isinstance(item, dict):
                for label, value in item.items():
                    if isinstance(value, str):
                        result.append((parents + [str(label)], value))
                    elif isinstance(value, list):
                        walk(value, parents + [str(label)])
                    else:
                        raise ValueError(f"Unsupported nav entry for {label!r}: {value!r}")
            else:
                raise ValueError(f"Unsupported nav item: {item!r}")

    walk(config["nav"], [])
    missing = [path for _, path in result if not (DOCS / path).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing nav sources: {missing}")
    return result


def source_inputs() -> list[Path]:
    pages = [DOCS / path for _, path in nav_pages()]
    resources = [
        ROOT / "mkdocs.yml",
        ROOT / "requirements-docs.txt",
        ROOT / "package.json",
        ROOT / "pnpm-lock.yaml",
        ROOT / "scripts" / "docs_pipeline.py",
        ROOT / "scripts" / "render_portables.mjs",
        ROOT / "scripts" / "validate_site.mjs",
        PORTABLE_CSS,
        DOCS / "assets" / "favicon.svg",
        DOCS / "javascripts" / "downloads.js",
        DOCS / "javascripts" / "mermaid-init.js",
        MERMAID_RUNTIME,
    ]
    return pages + resources


def source_fingerprint() -> str:
    digest = hashlib.sha256()
    digest.update(f"replicant-docs-pipeline:{PIPELINE_VERSION}\n".encode())
    for path in source_inputs():
        relative = path.relative_to(ROOT).as_posix()
        digest.update(relative.encode("utf-8") + b"\0")
        source_bytes = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        digest.update(source_bytes)
        digest.update(b"\0")
    return digest.hexdigest()


def replace_mermaid(markdown_source: str) -> tuple[str, int]:
    count = 0

    def replacement(match: re.Match[str]) -> str:
        nonlocal count
        count += 1
        diagram = html.escape(match.group(1).strip())
        return f'<pre class="mermaid" data-mermaid-source="{count}">{diagram}</pre>'

    return MERMAID_FENCE.sub(replacement, markdown_source), count


def render_markdown(source: str, page_number: int) -> tuple[str, int]:
    source, mermaid_count = replace_mermaid(source)
    rendered = markdown.markdown(
        source,
        extensions=[
            "admonition",
            "attr_list",
            "md_in_html",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.tabbed",
            "tables",
            "toc",
        ],
        extension_configs={"pymdownx.tabbed": {"alternate_style": True}},
        output_format="html5",
    )
    prefix = f"p{page_number}-"
    rendered = ID_ATTR.sub(lambda m: f'id="{prefix}{m.group(1)}"', rendered)
    rendered = HREF_ANCHOR.sub(lambda m: f'href="#{prefix}{m.group(1)}"', rendered)
    return rendered, mermaid_count


def portable_html_bytes() -> tuple[bytes, str, list[str]]:
    pages = nav_pages()
    fingerprint = source_fingerprint()
    toc_items: list[str] = []
    sections: list[str] = []
    sources: list[str] = []
    mermaid_total = 0

    for index, (trail, relative) in enumerate(pages, start=1):
        label = " › ".join(trail)
        source = (DOCS / relative).read_text(encoding="utf-8")
        rendered, mermaid_count = render_markdown(source, index)
        mermaid_total += mermaid_count
        sources.append(relative)
        search_text = html.escape(f"{label} {relative}", quote=True)
        toc_items.append(
            f'<li data-search="{search_text}"><a href="#page-{index}" data-page-link="page-{index}">'
            f'{html.escape(label)}</a></li>'
        )
        if index > 1:
            previous_label = " › ".join(pages[index - 2][0])
            previous_link = (
                f'<a class="previous" href="#page-{index - 1}">← {html.escape(previous_label)}</a>'
            )
        else:
            previous_link = '<span class="previous disabled">Inicio de la documentación</span>'
        if index < len(pages):
            next_label = " › ".join(pages[index][0])
            next_link = f'<a class="next" href="#page-{index + 1}">{html.escape(next_label)} →</a>'
        else:
            next_link = '<span class="next disabled">Fin de la documentación</span>'
        sections.append(
            f'<section class="doc-page" id="page-{index}" data-source="{html.escape(relative)}" '
            f'data-page-label="{html.escape(label, quote=True)}">'
            f'<p class="source-path">{index:02d} · {html.escape(label)} · {html.escape(relative)}</p>'
            f'<div class="doc-content">{rendered}</div>'
            f'<nav class="page-controls" aria-label="Navegación entre páginas">'
            f'{previous_link}{next_link}</nav></section>'
        )

    if mermaid_total != EXPECTED_MERMAID:
        raise ValueError(f"Expected {EXPECTED_MERMAID} Mermaid diagrams, found {mermaid_total}")

    css = PORTABLE_CSS.read_text(encoding="utf-8")
    mermaid = "\n".join(line.rstrip() for line in MERMAID_RUNTIME.read_text(encoding="utf-8").splitlines())
    document = f"""<!doctype html>
<html lang="es" data-source-fingerprint="{fingerprint}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="generator" content="Replicant documentation pipeline {PIPELINE_VERSION}">
  <meta name="source-fingerprint" content="sha256:{fingerprint}">
  <title>Replicant Lab · Documentación completa · {fingerprint[:12]}</title>
  <style>{css}</style>
</head>
<body>
  <header class="cover">
    <p class="eyebrow">RAUL LAB · DOCUMENTACIÓN CANÓNICA DERIVADA DE MKDOCS</p>
    <h1>Replicant Lab</h1>
    <p class="lead">Infraestructura, hosts, red, despliegues y operación.</p>
    <dl class="build-meta"><dt>Versión reproducible</dt><dd>sha256:{fingerprint}</dd><dt>Páginas fuente</dt><dd>{len(pages)}</dd><dt>Diagramas Mermaid</dt><dd>{mermaid_total}</dd></dl>
  </header>
  <div class="portable-layout">
    <aside class="portable-sidebar">
      <button class="portable-menu-button" type="button" aria-expanded="false" aria-controls="portable-nav">☰ Índice y búsqueda</button>
      <nav class="portable-nav" id="portable-nav" aria-label="Índice completo">
        <h2>Índice</h2>
        <label class="portable-search" for="portable-search">Buscar en la documentación
          <input id="portable-search" type="search" autocomplete="off" placeholder="Página o contenido">
        </label>
        <p class="search-status" id="portable-search-status" aria-live="polite"></p>
        <ol>{''.join(toc_items)}</ol>
      </nav>
    </aside>
    <main class="portable-main" id="portable-content">{''.join(sections)}</main>
  </div>
  <footer class="document-footer">Generado exclusivamente desde <code>mkdocs.yml</code>, <code>docs/</code> y recursos versionados · sha256:{fingerprint}</footer>
  <script>{mermaid}</script>
  <script>
  (() => {{
    const root = document.documentElement;
    const pages = [...document.querySelectorAll('.doc-page')];
    const links = [...document.querySelectorAll('[data-page-link]')];
    const sidebar = document.querySelector('.portable-sidebar');
    const menuButton = document.querySelector('.portable-menu-button');
    const search = document.querySelector('#portable-search');
    const searchStatus = document.querySelector('#portable-search-status');
    const baseTitle = 'Replicant Lab · Documentación completa';
    const done = (ok, detail) => {{
      root.dataset.mermaid = ok ? 'ready' : 'error';
      root.dataset.mermaidDetail = detail || '';
    }};
    const targetPage = target => {{
      if (!target) return pages[0];
      const element = document.getElementById(target);
      return element?.classList.contains('doc-page') ? element : element?.closest('.doc-page') || pages[0];
    }};
    const showPage = (target, scroll) => {{
      const page = targetPage(target);
      pages.forEach(item => item.classList.toggle('is-active', item === page));
      links.forEach(link => {{
        if (link.dataset.pageLink === page.id) link.setAttribute('aria-current', 'page');
        else link.removeAttribute('aria-current');
      }});
      root.dataset.activePage = page.id;
      document.title = (page.dataset.pageLabel || baseTitle) + ' · Replicant Lab';
      if (scroll) requestAnimationFrame(() => (document.getElementById(target) || page).scrollIntoView({{ block: 'start' }}));
    }};
    const route = () => {{
      const target = decodeURIComponent(location.hash.slice(1));
      showPage(target || pages[0].id, Boolean(target));
    }};
    window.addEventListener('hashchange', route);
    menuButton.addEventListener('click', () => {{
      const open = sidebar.classList.toggle('is-open');
      menuButton.setAttribute('aria-expanded', String(open));
    }});
    links.forEach(link => link.addEventListener('click', () => {{
      if (matchMedia('(max-width: 760px)').matches) {{
        sidebar.classList.remove('is-open');
        menuButton.setAttribute('aria-expanded', 'false');
      }}
    }}));
    search.addEventListener('input', () => {{
      const query = search.value.trim().toLocaleLowerCase('es');
      let visible = 0;
      document.querySelectorAll('.portable-nav li').forEach(item => {{
        const page = targetPage(item.querySelector('a').dataset.pageLink);
        const haystack = (item.dataset.search + ' ' + page.textContent).toLocaleLowerCase('es');
        item.hidden = Boolean(query) && !haystack.includes(query);
        if (!item.hidden) visible += 1;
      }});
      searchStatus.textContent = query ? visible + ' página(s) coincidente(s)' : '';
    }});
    showPage(decodeURIComponent(location.hash.slice(1)) || pages[0].id, false);
    mermaid.initialize({{
      startOnLoad: false,
      securityLevel: 'loose',
      theme: 'base',
      fontFamily: 'Arial, sans-serif',
      flowchart: {{ htmlLabels: true, useMaxWidth: true }},
      themeVariables: {{ primaryColor: '#e8f1f8', primaryTextColor: '#173f65', primaryBorderColor: '#52728d', lineColor: '#667085', fontSize: '15px' }}
    }});
    mermaid.run({{ querySelector: '.mermaid', suppressErrors: false }})
      .then(() => {{
        done(true, String(document.querySelectorAll('.mermaid svg').length));
        root.dataset.portable = 'ready';
        route();
      }})
      .catch(error => {{ done(false, String(error)); console.error(error); }});
  }})();
  </script>
</body>
</html>
"""
    return document.replace("\r\n", "\n").encode("utf-8"), fingerprint, sources


def sync_mermaid_runtime(*, write: bool) -> None:
    if not MERMAID_PACKAGE_RUNTIME.is_file():
        raise FileNotFoundError("node_modules missing; run pnpm install --frozen-lockfile")
    packaged_text = MERMAID_PACKAGE_RUNTIME.read_text(encoding="utf-8")
    packaged = ("\n".join(line.rstrip() for line in packaged_text.splitlines()) + "\n").encode("utf-8")
    if write:
        MERMAID_RUNTIME.parent.mkdir(parents=True, exist_ok=True)
        MERMAID_RUNTIME.write_bytes(packaged)
    elif not MERMAID_RUNTIME.is_file() or MERMAID_RUNTIME.read_bytes() != packaged:
        raise ValueError("docs/javascripts/mermaid.min.js is not synchronized with mermaid@11.16.1")


def build_site() -> None:
    SITE.parent.mkdir(parents=True, exist_ok=True)
    run([sys.executable, "-m", "mkdocs", "build", "--strict", "--clean", "--site-dir", str(SITE)])


class QuietStaticHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: object) -> None:
        pass


def validate_site_browser(*, screenshots: bool = False) -> None:
    handler = functools.partial(QuietStaticHandler, directory=str(SITE))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        command = [
            find_node(),
            str(ROOT / "scripts" / "validate_site.mjs"),
            "--base",
            f"http://{host}:{port}/",
            "--root",
            str(SITE),
            "--report",
            str(BUILD / "site-report.json"),
        ]
        if screenshots:
            command.extend(["--screenshots", str(BUILD / "site-screenshots")])
        run(command)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def find_node() -> str:
    explicit = os.environ.get("DOCS_NODE")
    if explicit:
        return explicit
    node = shutil.which("node")
    if not node:
        raise FileNotFoundError("Node.js 24.14.0 not found; set DOCS_NODE or add node to PATH")
    return node


def render_pdf(html_path: Path, pdf_path: Path, report_path: Path, screenshot_dir: Path | None = None) -> None:
    command = [find_node(), str(NODE_RENDERER), "--html", str(html_path), "--pdf", str(pdf_path), "--report", str(report_path)]
    if screenshot_dir:
        command.extend(["--screenshots", str(screenshot_dir)])
    run(command)


def validate_portable_html(path: Path, expected_fingerprint: str, expected_sources: list[str]) -> None:
    data = path.read_text(encoding="utf-8")
    if f'sha256:{expected_fingerprint}' not in data:
        raise ValueError(f"{path} has a stale source fingerprint")
    if data.count('class="doc-page"') != len(expected_sources):
        raise ValueError(f"{path} does not contain all {len(expected_sources)} nav pages")
    for source in expected_sources:
        if f'data-source="{source}"' not in data:
            raise ValueError(f"{path} is missing {source}")
    if data.count('class="mermaid"') != EXPECTED_MERMAID:
        raise ValueError(f"{path} does not contain exactly {EXPECTED_MERMAID} Mermaid sources")
    if data.count('data-page-link=') != len(expected_sources):
        raise ValueError(f"{path} does not contain one navigation link per source page")
    if data.count('class="page-controls"') != len(expected_sources):
        raise ValueError(f"{path} does not contain one previous/next control per source page")
    required_multipage = ['id="portable-search"', "hashchange", "data-portable", "activePage"]
    missing_multipage = [token for token in required_multipage if token not in data]
    if missing_multipage:
        raise ValueError(f"Portable multipage controls missing in {path}: {missing_multipage}")
    forbidden = ["livereload", "ws://", "wss://", "127.0.0.1:", "localhost:"]
    lowered = data.lower()
    found = [token for token in forbidden if token in lowered]
    if found:
        raise ValueError(f"Development residue in {path}: {found}")
    for tag, attribute, reference in resource_references(data):
        parsed = urlparse(html.unescape(reference))
        external = parsed.scheme in {"http", "https", "ws", "wss"} or reference.startswith("//")
        if external and tag != "a":
            raise ValueError(f"External resource in offline HTML: {tag}[{attribute}]={reference}")


def validate_pdf(path: Path, expected_fingerprint: str) -> dict[str, int]:
    reader = PdfReader(str(path))
    if len(reader.pages) != EXPECTED_PDF_PAGES:
        raise ValueError(f"PDF page count drift: expected={EXPECTED_PDF_PAGES}, actual={len(reader.pages)}")
    text = "\n".join((page.extract_text() or "") for page in reader.pages)
    required = [
        "Replicant Lab",
        "Índice",
        "Arquitectura",
        "Host · Nexus",
        "Aplicaciones",
        "Pendientes",
        "Descargas",
    ]
    compact_text = "".join(text.split())
    if f"sha256:{expected_fingerprint}" not in compact_text:
        raise ValueError("PDF text is missing its source fingerprint")
    missing = [item for item in required if item not in text]
    if missing:
        raise ValueError(f"PDF text is missing: {missing}")
    links = 0
    for page in reader.pages:
        for annotation in page.get("/Annots", []):
            obj = annotation.get_object()
            if obj.get("/Subtype") == "/Link":
                links += 1
    if links < 5:
        raise ValueError(f"PDF has too few clickable links: {links}")
    return {"pages": len(reader.pages), "characters": len(text), "links": links}


def validate_site_resources() -> None:
    html_files = list(SITE.rglob("*.html"))
    if len(html_files) < len(nav_pages()):
        raise ValueError("Static site has fewer HTML pages than MkDocs nav")
    for page in html_files:
        data = page.read_text(encoding="utf-8")
        lowered = data.lower()
        if "livereload" in lowered or "ws://" in lowered or "wss://" in lowered:
            raise ValueError(f"Development residue in static site: {page}")
        for _tag, _attribute, reference in resource_references(data):
            reference = html.unescape(reference).split("#", 1)[0].split("?", 1)[0]
            if not reference or reference.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
                continue
            parsed = urlparse(reference)
            if parsed.scheme in {"http", "https"} or reference.startswith("//"):
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            if parsed.path.startswith("/"):
                target = SITE / parsed.path.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                raise FileNotFoundError(f"Broken resource from {page.relative_to(SITE)}: {reference}")


def generate(*, screenshots: bool = False) -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    sync_mermaid_runtime(write=True)
    html_bytes, fingerprint, sources = portable_html_bytes()
    CANONICAL_HTML.parent.mkdir(parents=True, exist_ok=True)
    CANONICAL_HTML.write_bytes(html_bytes)
    render_pdf(
        CANONICAL_HTML,
        CANONICAL_PDF,
        BUILD / "render-report.json",
        BUILD / "screenshots" if screenshots else None,
    )
    build_site()
    validate_site_browser(screenshots=screenshots)
    validate_portable_html(CANONICAL_HTML, fingerprint, sources)
    validate_site_resources()
    pdf = validate_pdf(CANONICAL_PDF, fingerprint)
    print(json.dumps({"fingerprint": fingerprint, "sources": len(sources), "mermaid": EXPECTED_MERMAID, "pdf": pdf}, ensure_ascii=False, indent=2))


def check() -> None:
    BUILD.mkdir(parents=True, exist_ok=True)
    sync_mermaid_runtime(write=False)
    build_site()
    validate_site_browser()
    expected_html, fingerprint, sources = portable_html_bytes()
    if not CANONICAL_HTML.is_file() or CANONICAL_HTML.read_bytes() != expected_html:
        raise ValueError("Canonical HTML is stale; run python scripts/docs_pipeline.py generate")
    temp_pdf = BUILD / "Replicant-Lab.check.pdf"
    render_pdf(CANONICAL_HTML, temp_pdf, BUILD / "render-report.check.json")
    validate_portable_html(CANONICAL_HTML, fingerprint, sources)
    validate_site_resources()
    canonical = validate_pdf(CANONICAL_PDF, fingerprint)
    regenerated = validate_pdf(temp_pdf, fingerprint)
    if canonical["pages"] != regenerated["pages"]:
        raise ValueError(f"PDF page count drift: canonical={canonical['pages']} regenerated={regenerated['pages']}")
    print(json.dumps({"status": "synchronized", "fingerprint": fingerprint, "sources": len(sources), "mermaid": EXPECTED_MERMAID, "pdf": canonical}, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["generate", "check", "build-site"])
    parser.add_argument("--screenshots", action="store_true", help="Capture representative browser screenshots during generation")
    args = parser.parse_args()
    if args.command == "generate":
        generate(screenshots=args.screenshots)
    elif args.command == "check":
        check()
    else:
        sync_mermaid_runtime(write=False)
        build_site()
        validate_site_browser(screenshots=args.screenshots)
        validate_site_resources()


if __name__ == "__main__":
    main()
