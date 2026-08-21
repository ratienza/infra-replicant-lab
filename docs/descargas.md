# Descargas

La documentación MkDocs de este proyecto es la única referencia canónica. Los dos ficheros siguientes se generan exclusivamente desde `mkdocs.yml`, las páginas de `docs/` incluidas en `nav` y sus recursos versionados.

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1rem 0 1.5rem 0">
  <button type="button" onclick="replicantDownloadHtml()" class="md-button md-button--primary">⬇ Descargar documentación HTML offline</button>
  <button type="button" onclick="replicantDownloadPdf()" class="md-button">⬇ Descargar documentación PDF</button>
</div>

## Rutas canónicas únicas

| Artefacto | Ruta | Cobertura |
|---|---|---|
| HTML autocontenido | `docs/downloads/Replicant-Lab.html` | Toda la navegación MkDocs, índice interno y siete Mermaid |
| PDF A4 | `docs/downloads/Replicant-Lab.pdf` | Portada, índice, documentación completa, numeración y siete Mermaid |

No se mantiene ninguna copia alternativa.

## Fichas técnicas individuales

Cada pareja HTML/PDF se genera desde la misma página Markdown incluida en la navegación. El HTML funciona offline y el PDF está preparado para consulta o archivo.

| Aplicación | HTML | PDF |
|---|---|---|
| PULA | [Descargar](downloads/apps/pula.html) | [Descargar](downloads/apps/pula.pdf) |
| App Launch | [Descargar](downloads/apps/app-launch.html) | [Descargar](downloads/apps/app-launch.pdf) |
| Salones AV | [Descargar](downloads/apps/salones-av.html) | [Descargar](downloads/apps/salones-av.pdf) |
| Reserva-Pistas-UTP | [Descargar](downloads/apps/reserva-pistas-utp.html) | [Descargar](downloads/apps/reserva-pistas-utp.pdf) |
| Consumos Cupra | [Descargar](downloads/apps/consumos-cupra.html) | [Descargar](downloads/apps/consumos-cupra.pdf) |
| CV de Raúl | [Descargar](downloads/apps/cv-raul.html) | [Descargar](downloads/apps/cv-raul.pdf) |
| Control de Red | [Descargar](downloads/apps/control-red.html) | [Descargar](downloads/apps/control-red.pdf) |
| Cartera Estratégica | [Descargar](downloads/apps/cartera-estrategica.html) | [Descargar](downloads/apps/cartera-estrategica.pdf) |
| Replicant Lab | [Descargar](downloads/apps/replicant-lab.html) | [Descargar](downloads/apps/replicant-lab.pdf) |

## Propiedades verificables

- Todos los artefactos muestran la misma huella SHA-256 de las fuentes.
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

El pipeline y el runtime estático están implementados y probados localmente. El 21/08/2026 se comprobó el dossier global y las nueve parejas de fichas individuales, incluida PULA; los ficheros servidos por el entorno de validación coincidieron byte a byte con los artefactos generados. La publicación en Nexus se valida de nuevo después de integrar el cambio en `main`; esta evidencia corresponde al laboratorio privado y no se extrapola a producción.
