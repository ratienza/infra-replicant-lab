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

## Alcance de esta ficha

La documentación técnica/funcional específica de los salones permanece en el repo de la aplicación.
