# Aplicación · Salones AV

Documentación operativa audiovisual para el personal del SH Valencia Palace: panel general, pantallas LED, traslado, conexión de cliente, sonido y mapas de las plantas PL1 y PL6.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/salones-av.html)
- **Aplicación / Nexus:** [Salones AV](http://192.168.18.220:8081/)

## Ficha de infraestructura

| Campo | Valor |
|---|---|
| Desarrollo | Codex / GitHub |
| Repo | `ratienza/salones-av-valencia-palace` |
| Host | Nexus |
| Ruta | `/opt/apps/salones-av-valencia-palace` |
| Contenedor | `salones-av` |
| Imagen | `nginx:alpine` |
| Puerto | `192.168.18.220:8081 → 80/tcp` |
| Contenido | `proyecto_html` montado en solo lectura |
| Rama / SHA | `main` · `8c0bc08446256974b7efa57c730cbeb1b6e81520` |
| Red | Compose propia, sin dependencias con otros contenedores |
| Inicio | `restart: unless-stopped` |

## Comportamiento de despliegue

El contenido HTML se sirve mediante un bind mount. Por tanto, un `git pull` actualiza los ficheros visibles sin necesidad de reconstruir una imagen.

La actualización segura exige revisar primero el working tree, actualizar desde `main` y comprobar enlaces y páginas. El rollback consiste en volver a un commit aprobado y restaurar el contenido estático; no tiene base de datos ni persistencia funcional.

## Reconciliación Git y Nexus

La Fase 2A corrigió mediante el PR `salones-av-valencia-palace#2` la única deriva del checkout: `main` ahora versiona `192.168.18.220:8081:80`. El cambio se reconstruyó conscientemente en una rama; no se copió el checkout del servidor hacia GitHub.

Antes del avance rápido se demostró que el blob preparado, el archivo vivo y el stash preservativo eran idénticos: `686cfdd506fbd67b624bffae5f49ca640a799da6`. Después del merge, GitHub `main`, `origin/main` y el checkout Nexus quedaron en `8c0bc08446256974b7efa57c730cbeb1b6e81520`, sin cambios locales.

## Validación del 13/08/2026

- Contenedor `salones-av` activo con imagen `nginx:alpine`.
- `http://192.168.18.220:8081/` respondió `200`.
- Las siete páginas del menú respondieron `200`.
- Los enlaces HTML locales pasaron la comprobación estática.
- `docker compose config --quiet` aceptó la definición versionada.
- Docker confirmó el bind efectivo `192.168.18.220:8081`; no existe publicación de Salones en `0.0.0.0:8081`.
- GitHub `main == checkout Nexus` en `8c0bc08` tras el despliegue dirigido al servicio `web`.
- La copia pública `https://app.raulatienza.com/salones/` respondió `200`.
- No se validaron equipos AV físicos, números de tomas ni procedimientos sobre hardware.

## Seguridad y límites

El contenido operativo puede incluir topología e inventario de salas. No deben incorporarse credenciales ni datos de red sensibles a un repositorio público. El servicio es estático y no implementa autenticación propia; su alcance depende del bind LAN y del control del host.

## Alcance de esta ficha

La documentación técnica/funcional específica de los salones permanece en el repo de la aplicación.
