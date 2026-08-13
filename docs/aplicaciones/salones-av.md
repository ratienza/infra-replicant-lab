# Aplicación · Salones AV

Documentación operativa audiovisual para el personal del SH Valencia Palace: panel general, pantallas LED, traslado, conexión de cliente, sonido y mapas de las plantas PL1 y PL6.

## Ficha de infraestructura

| Campo | Valor |
|---|---|
| Repo | `ratienza/salones-av-valencia-palace` |
| Host | Nexus |
| Ruta | `/opt/apps/salones-av-valencia-palace` |
| Contenedor | `salones-av` |
| Imagen | `nginx:alpine` |
| Puerto | `192.168.18.220:8081 → 80/tcp` |
| Contenido | `proyecto_html` montado en solo lectura |
| Rama / SHA | `main` · `da941d232fa937433c109f4c3daf3854711957f9` |
| Red | Compose propia, sin dependencias con otros contenedores |
| Inicio | `restart: unless-stopped` |

## Comportamiento de despliegue

El contenido HTML se sirve mediante un bind mount. Por tanto, un `git pull` actualiza los ficheros visibles sin necesidad de reconstruir una imagen.

La actualización segura exige revisar primero el working tree, actualizar desde `main` y comprobar enlaces y páginas. El rollback consiste en volver a un commit aprobado y restaurar el contenido estático; no tiene base de datos ni persistencia funcional.

## Diferencia observada entre Git y Nexus

El `compose.yml` vigente en `main` publica `8081:80`, mientras el checkout desplegado en Nexus contiene un cambio local no versionado que lo restringe a `192.168.18.220:8081:80`. El contenedor observado usa efectivamente el bind a la IP de Nexus.

La restricción local mejora el alcance de red, pero constituye deriva respecto a GitHub. Debe reconciliarse en el repositorio propio de Salones AV antes de considerar el despliegue plenamente reproducible; esta documentación no corrige ni adopta silenciosamente ese cambio.

## Validación del 13/08/2026

- Contenedor `salones-av` activo con imagen `nginx:alpine`.
- `http://192.168.18.220:8081/` respondió `200`.
- Las siete páginas del menú respondieron `200`.
- Los enlaces HTML locales pasaron la comprobación estática.
- La copia pública `https://app.raulatienza.com/salones/` respondió `200`.
- No se validaron equipos AV físicos, números de tomas ni procedimientos sobre hardware.

## Seguridad y límites

El contenido operativo puede incluir topología e inventario de salas. No deben incorporarse credenciales ni datos de red sensibles a un repositorio público. El servicio es estático y no implementa autenticación propia; su alcance depende del bind LAN y del control del host.

## Alcance de esta ficha

La documentación técnica/funcional específica de los salones permanece en el repo de la aplicación.
