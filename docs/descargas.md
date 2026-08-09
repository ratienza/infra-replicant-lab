# Descargas

Desde esta página se descargan directamente las versiones portables servidas por **Replicant Lab en Nexus**, sin pasar por GitHub.

<div style="display:flex;gap:12px;flex-wrap:wrap;margin:1rem 0 1.5rem 0">
  <a href="/downloads/Replicant-Lab.html" download class="md-button md-button--primary">⬇ Descargar índice HTML autónomo</a>
  <a href="/downloads/Replicant-Lab.pdf" download class="md-button">⬇ Descargar PDF Pro</a>
</div>

## Qué contiene cada versión

- **HTML autónomo**: una copia independiente que puede abrirse en cualquier navegador sin MkDocs ni servidor. El propio HTML incluye además botones para volver a descargarse y para descargar el PDF Pro que esté en su misma carpeta.
- **PDF Pro**: versión cerrada y portable de la documentación del laboratorio para consulta, archivo o envío.

## Regla de mantenimiento

Cada cierre documental de una aplicación debe regenerar ambos ficheros y comprobar que estos enlaces responden desde la propia aplicación de documentación:

```text
http://192.168.18.220:8082/downloads/Replicant-Lab.html
http://192.168.18.220:8082/downloads/Replicant-Lab.pdf
```

No se considera cerrada la documentación si alguno de los dos enlaces falta, está desactualizado o devuelve 404.
