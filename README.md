# Replicant Lab

Documentación viva de infraestructura, hosts, red, despliegues y operación del laboratorio.

La documentación se escribe en **Markdown**, se construye con **MkDocs Material** y usa **Mermaid** para diagramas mantenibles como código. `mkdocs.yml`, `docs/` y sus recursos son la fuente canónica de contenido, estructura y presentación documental.

El repositorio contiene también salidas HTML y PDF portables. Son artefactos derivados: no sustituyen a MkDocs y, hasta disponer de un generador reproducible, su sincronización debe verificarse expresamente.

## Alcance

Este repositorio documenta el **laboratorio como sistema**: arquitectura, hosts, red, seguridad, Git, Docker, operación y fichas de infraestructura de aplicaciones.

La documentación funcional y de desarrollo de cada aplicación permanece en su repositorio propio.

## Ejecutar la documentación en Nexus

```bash
cd /opt/apps/infra-replicant-lab
git pull --ff-only
```

La web quedará disponible en:

```text
http://192.168.18.220:8082
```

En Nexus, `compose.yml` ejecuta `mkdocs serve` con `mkdocs.yml` y `docs/` montados en solo lectura. Un cambio normal de contenido se detecta sin reconstruir la imagen ni reiniciar el contenedor. Solo se recrea el servicio cuando cambia su definición, imagen o montaje.

```bash
git pull --ff-only
```

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
