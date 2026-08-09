# Aplicación · Salones AV

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

## Comportamiento de despliegue

El contenido HTML se sirve mediante un bind mount. Por tanto, un `git pull` actualiza los ficheros visibles sin necesidad de reconstruir una imagen.

## Diferencia observada entre Git y Nexus

El `compose.yml` vigente en `main` publica `8081:80`, mientras el checkout desplegado en Nexus contiene un cambio local no versionado que lo restringe a `192.168.18.220:8081:80`. El contenedor observado usa efectivamente el bind a la IP de Nexus.

La restricción local mejora el alcance de red, pero constituye deriva respecto a GitHub. Debe reconciliarse en el repositorio propio de Salones AV antes de considerar el despliegue plenamente reproducible; esta documentación no corrige ni adopta silenciosamente ese cambio.

## Alcance de esta ficha

La documentación técnica/funcional específica de los salones permanece en el repo de la aplicación.
