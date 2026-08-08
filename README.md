# Replicant Lab

Documentación viva de infraestructura, hosts, red, despliegues y operación del laboratorio.

La documentación se escribe en **Markdown**, se construye con **MkDocs Material** y usa **Mermaid** para diagramas mantenibles como código. El resultado se sirve como sitio estático con **Nginx**.

Además, el repositorio mantiene una copia **HTML autónoma** para poder consultar toda la documentación sin depender de Nexus ni de ningún servicio.

## Alcance

Este repositorio documenta el **laboratorio como sistema**: arquitectura, hosts, red, seguridad, Git, Docker, operación y fichas de infraestructura de aplicaciones.

La documentación funcional y de desarrollo de cada aplicación permanece en su repositorio propio.

## Ejecutar la documentación en Nexus

```bash
cd /opt/apps/infra-replicant-lab
docker compose up -d --build
```

La web quedará disponible en:

```text
http://192.168.18.220:8088
```

Cada cambio documental requiere reconstruir la imagen estática:

```bash
git pull
docker compose up -d --build
```

## Copia offline

La copia autocontenida se conserva en:

```text
standalone/Replicant-Lab.html
```

Debe poder abrirse directamente en cualquier navegador sin Nexus y sin dependencias externas.

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
