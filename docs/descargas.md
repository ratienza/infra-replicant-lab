# Descargas

Desde aquí se descargan las dos versiones portables **desde la propia aplicación Replicant Lab en Nexus**. No se abre GitHub ni se muestra el HTML como código: el navegador recibe el fichero y fuerza su descarga local.

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1rem 0 1.5rem 0">
  <button type="button" onclick="replicantDownloadHtml()" class="md-button md-button--primary">⬇ Descargar índice HTML autónomo</button>
  <button type="button" onclick="replicantDownloadPdf()" class="md-button">⬇ Descargar PDF Pro</button>
</div>

## Qué contiene cada versión

- **HTML autónomo**: copia independiente que puede abrirse en cualquier navegador sin MkDocs ni servidor.
- **PDF Pro**: versión cerrada y portable de la documentación del laboratorio para consulta, archivo o envío.

## Rutas internas

Los ficheros que usa esta página viven dentro de la propia documentación:

```text
/downloads/Replicant-Lab.html
/downloads/Replicant-Lab.pdf
```

El JavaScript de Replicant Lab obtiene cada fichero con `fetch()` y lo entrega al navegador como descarga, evitando depender del comportamiento MIME del servidor o de enlaces `raw` de GitHub.

## Regla de mantenimiento

Cada cierre documental de una aplicación debe regenerar ambos ficheros y comprobar que los dos botones descargan realmente desde la propia app de documentación. No se considera cerrada la documentación si alguno falta, está desactualizado, abre código en pantalla o devuelve error.
