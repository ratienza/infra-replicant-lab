# Descargas

La documentación MkDocs de este proyecto es la única referencia canónica. Los dos ficheros siguientes se generan exclusivamente desde `mkdocs.yml`, las páginas de `docs/` incluidas en `nav` y sus recursos versionados.

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1rem 0 1.5rem 0">
  <button type="button" onclick="replicantDownloadHtml()" class="md-button md-button--primary">⬇ Descargar documentación HTML offline</button>
  <button type="button" onclick="replicantDownloadPdf()" class="md-button">⬇ Descargar documentación PDF</button>
</div>

## Rutas canónicas únicas

| Artefacto | Ruta | Cobertura |
|---|---|---|
| HTML autocontenido | `docs/downloads/Replicant-Lab.html` | Toda la navegación MkDocs, índice interno y cinco Mermaid |
| PDF A4 | `docs/downloads/Replicant-Lab.pdf` | Portada, índice, documentación completa, numeración y cinco Mermaid |

No se mantiene ninguna copia alternativa.

## Propiedades verificables

- Ambos artefactos muestran la misma huella SHA-256 de las fuentes.
- El HTML incorpora CSS, JavaScript y Mermaid localmente y funciona mediante `file://` sin red.
- El HTML no solicita CDN ni contiene clientes de recarga, conexiones dinámicas o referencias al servidor de desarrollo.
- El PDF mantiene texto seleccionable, enlaces, tablas, código, avisos y diagramas.
- El JavaScript del sitio calcula las rutas desde su propio recurso y funciona con el sitio estático en `/`.

## Regeneración y sincronía

Después de preparar las dependencias fijadas, un único comando regenera y valida todo:

```bash
python scripts/docs_pipeline.py generate
```

CI ejecuta el modo `check`, vuelve a renderizar un PDF de control, verifica la huella y cobertura, construye la imagen Docker final, arranca Nginx temporalmente y compara byte a byte las descargas servidas con los artefactos versionados.

## Estado de despliegue

El pipeline y el runtime estático están implementados, probados localmente y validados en Nexus. El 09/08/2026 se comprobaron el sitio publicado, los cinco diagramas y las descargas reales; los ficheros servidos coincidieron byte a byte con los artefactos versionados. Esta validación corresponde al laboratorio privado y no se extrapola a producción.
