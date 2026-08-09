# Descargas

La documentación MkDocs de este proyecto es la referencia canónica. Los ficheros descargables son salidas derivadas para consulta offline y no deben usarse como plantilla ni como fuente prioritaria.

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1rem 0 1.5rem 0">
  <button type="button" onclick="replicantDownloadHtml()" class="md-button md-button--primary">⬇ Descargar índice HTML autónomo</button>
  <button type="button" onclick="replicantDownloadPdf()" class="md-button">⬇ Descargar PDF</button>
</div>

## Inventario actual

| Artefacto | Ruta versionada | Alcance comprobado |
|---|---|---|
| HTML descargable | `docs/downloads/Replicant-Lab.html` | Copia autónoma de una página; no representa todo el árbol MkDocs |
| HTML standalone | `standalone/Replicant-Lab.html` | Copia del mismo HTML autónomo |
| PDF | `docs/downloads/Replicant-Lab.pdf` | Resumen de una página; no es una exportación completa de MkDocs |

No existe `standalone/Replicant-Lab.pdf` en el repositorio.

## Limitación observada en Nexus

La página usa `docs/javascripts/downloads.js` para obtener `/downloads/Replicant-Lab.html` y `/downloads/Replicant-Lab.pdf` mediante `fetch()` y forzar la descarga. Ambos recursos respondieron HTTP `200` el 09/08/2026.

Como Nexus sirve toda la carpeta `docs/` mediante `mkdocs serve`, MkDocs inyecta su cliente de recarga en el HTML descargable que entrega el servidor. El HTML versionado no contiene esa inyección, pero la respuesta obtenida desde Nexus sí; por tanto, la descarga servida no puede considerarse una copia offline limpia hasta resolver el proceso de publicación.

## Regla de mantenimiento vigente

El repositorio no contiene todavía un generador reproducible que derive el HTML y el PDF desde MkDocs. Hasta implementarlo:

1. los portables se consideran referencias derivadas con cobertura limitada;
2. ningún cambio en ellos prevalece sobre `mkdocs.yml`, `docs/` y sus recursos;
3. cualquier afirmación de sincronía debe acompañarse de una comprobación concreta;
4. la automatización de generación, validación y publicación queda registrada como pendiente, no como requisito ya satisfecho.
