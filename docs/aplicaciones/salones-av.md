# Aplicación · Salones AV

Documentación operativa audiovisual interna para el personal del SH Valencia Palace: panel, pantallas LED, traslado, conexión de cliente, sonido, música ambiental, streaming, mapas PL1/PL6, sincronización de micrófonos y diagnóstico guiado.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/salones-av.html)
- **Aplicación / Nexus:** [Salones AV](http://192.168.18.220:8081/)
- **Aplicación / producción:** [Salones AV](https://app.raulatienza.com/salones/) — requiere autenticación.

## Ficha de infraestructura

| Campo | Nexus | DigitalOcean |
|---|---|---|
| Repo | ratienza/salones-av-valencia-palace | Mismo repositorio privado |
| Rama / SHA | main · b88de54a1fe1c42d359fd7dd83b2048ca7d86bb2 | Mismo SHA |
| Runtime | Contenedor salones-av, imagen nginx:alpine | Nginx del host |
| Publicación | 192.168.18.220:8081 → 80/tcp | /salones/ sobre HTTPS y autenticación |
| Contenido | proyecto_html por bind mount de solo lectura | Release estática extraída únicamente de proyecto_html |
| Inicio | restart: unless-stopped | Nginx habilitado al arranque |
| Persistencia | Sin base de datos; preferencia de tema en el navegador | Igual |

## Funcionalidad consolidada

La revisión de septiembre añadió panel renovado, modo claro/oscuro, música ambiental, streaming, guía de sincronización de micros, diagnóstico interactivo con búsqueda y filtros, y acceso al asistente AV externo. También actualizó sonido, conexiones, mapas, recursos gráficos y checklists imprimibles.

El PR salones-av-valencia-palace#4 incorporó la corrección y la validación automatizada. El PR #5 ajustó la documentación del mecanismo de despliegue.

## Despliegue y rollback

Nexus sirve el checkout mediante bind mount. Un avance rápido de main actualiza el contenido sin reconstruir la imagen cuando Compose, la imagen y las dependencias no cambian.

DigitalOcean recibe un bundle Git completo y verificado del main canónico. Un script extrae solo proyecto_html, crea una release con manifiesto SHA-256 y activa la release. Se conservan la copia anterior y las releases previas para rollback. Credenciales, certificados y configuración Nginx permanecen fuera de Git.

## Compose y bind mounts

La deriva histórica permanece resuelta. Compose publica únicamente en la IP LAN de Nexus y monta ./proyecto_html:/usr/share/nginx/html:ro. El mount no oculta código incluido en una imagen propia: nginx:alpine aporta el servidor y Git aporta deliberadamente todo el contenido estático.

## Validación del 05/09/2026

- GitHub, Replicant, Nexus y el checkout de DigitalOcean quedaron en b88de54a1fe1c42d359fd7dd83b2048ca7d86bb2.
- Los 42 blobs publicables de Git, Nexus y DigitalOcean compartieron el mismo hash agregado.
- El check de GitHub pasó en los PR #4 y #5.
- La suite Playwright pasó 84 comprobaciones sobre las 13 páginas en local y en Nexus: rutas, assets, anclas, escritorio, móvil, tema, checklists, impresión y todas las ramas del diagnóstico.
- Las siete salidas de impresión comprobadas usaron tamaño A4.
- Nexus respondió 200 en 8081; el contenedor permaneció activo, sin recreación, y Compose validó correctamente.
- DigitalOcean redirigió HTTP a HTTPS y respondió 401 sin credenciales en portada, Streaming y assets. El portal principal siguió respondiendo 200.
- Nginx validó su configuración; el certificado observado para app.raulatienza.com era válido hasta el 28/11/2026.
- No se validaron físicamente cámaras, micrófonos, pantallas, tablets, patching ni procedimientos sobre hardware.

## Seguridad y límites

La aplicación contiene inventario y direcciones internas necesarias para la operación. El repositorio es privado, Nexus limita el bind a la LAN y DigitalOcean exige autenticación. No se versionan credenciales ni configuración privada del proxy.

## Alcance de esta ficha

La documentación funcional y los procedimientos detallados permanecen en el repositorio de la aplicación.
