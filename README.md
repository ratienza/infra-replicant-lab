# Replicant Lab

Documentación viva de infraestructura, hosts, red, despliegues y operación del laboratorio.

La documentación se escribe en **Markdown**, se construye con **MkDocs Material** y usa **Mermaid** para diagramas mantenibles como código. `mkdocs.yml`, `docs/` y sus recursos son la fuente canónica de contenido, estructura y presentación documental.

El repositorio contiene también salidas HTML y PDF portables. Son artefactos derivados: no sustituyen a MkDocs y, hasta disponer de un generador reproducible, su sincronización debe verificarse expresamente.

## Alcance

Este repositorio documenta el **laboratorio como sistema**: arquitectura, hosts, red, seguridad, Git, Docker, operación y fichas de infraestructura de aplicaciones.

La documentación funcional y de desarrollo de cada aplicación permanece en su repositorio propio.

## Ejecutar la documentación en Nexus

### Primer arranque o recreación necesaria

```bash
cd /opt/apps/infra-replicant-lab
git switch main
git pull --ff-only origin main
docker compose up -d
```

`docker compose up -d` inicia el servicio y lo recrea cuando hayan cambiado `compose.yml`, la imagen, los montajes o los parámetros de ejecución. El Compose vigente usa directamente `squidfunk/mkdocs-material:9`, por lo que no requiere `--build` ni construye el `Dockerfile`.

La web queda disponible en:

```text
http://192.168.18.220:8082
```

### Actualización documental ordinaria

```bash
cd /opt/apps/infra-replicant-lab
git switch main
git pull --ff-only origin main
```

Si el contenedor ya está activo, los cambios normales en `docs/` o `mkdocs.yml` se detectan mediante los bind mounts y `mkdocs serve`, sin reconstruir ni reiniciar el servicio.

## Copia offline

La copia HTML autocontenida se conserva en:

```text
standalone/Replicant-Lab.html
```

La web publicada ofrece además copias en `docs/downloads/`. El HTML y el PDF actuales deben tratarse como referencias derivadas con limitaciones conocidas, descritas en la página **Descargas**.

## Flujo de cambios

```text
main → rama de cambio → commits → PR → revisión → merge
```

Las ramas representan **cambios lógicos**, no archivos individuales. Ejemplos:

- `docs/bootstrap-infra`
- `docs/app-salones`
- `docs/app-cartera`
- `docs/network`
- `docs/backups`

## Principio de seguridad

No almacenar aquí contraseñas, tokens, claves privadas, bases de datos ni secretos reales.
