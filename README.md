# Replicant Lab

Documentación viva de infraestructura, hosts, red, despliegues y operación del laboratorio.

La documentación se escribe en **Markdown**, se construye con **MkDocs Material** y usa **Mermaid** para diagramas mantenibles como código. `mkdocs.yml`, `docs/` y sus recursos son la fuente canónica de contenido, estructura y presentación documental.

El repositorio mantiene dos salidas portables derivadas y reproducibles: un HTML autocontenido y un PDF completo. Nunca sustituyen a la fuente MkDocs.

## Alcance

Este repositorio documenta el **laboratorio como sistema**: arquitectura, hosts, red, seguridad, Git, Docker, operación y fichas de infraestructura de aplicaciones.

La documentación funcional y de desarrollo de cada aplicación permanece en su repositorio propio.

## Generación reproducible

Dependencias fijadas:

- Python `3.12.10`;
- MkDocs `1.6.1` y Material `9.7.7`;
- Node.js `24.14.0` y pnpm `11.16.0`;
- Mermaid `11.16.1`;
- Playwright `1.62.1` con su Chromium administrado.

Preparación inicial:

```bash
python -m pip install --requirement requirements-docs.txt
pnpm install --frozen-lockfile
pnpm exec playwright install chromium
```

Un único comando construye MkDocs, genera los portables globales y por aplicación, renderiza los seis Mermaid y valida enlaces, recursos, HTML offline y PDF:

```bash
python scripts/docs_pipeline.py generate
```

El panel interno de ErasmusHomes se genera antes desde su única fuente estructurada:

```bash
python scripts/erasmushomes_panel.py generate --repo ../ErasmusHomes
python scripts/erasmushomes_panel.py check
```

`data/erasmushomes/` es un caché derivado con SHA y fecha; nunca se edita manualmente. El generador exige el PDF acordado versionado en `ErasmusHomes/Docs/source/`, contrasta su entrada en `SHA256SUMS`, publica esos mismos bytes bajo `docs/downloads/erasmushomes/` y enlaza PDF, Markdown y YAML fijados al mismo SHA que muestra el panel. ErasmusHomes consolidó su árbol canónico en `Docs/` en `main@d5cabad`, con `Roadmap check` verde. La copia publicada es siempre generada; no se edita manualmente ni en Replicant Lab ni en Nexus.

En Nexus, `scripts/sync_erasmushomes_nexus.sh` actualiza ambos `main` mediante `pull --ff-only`, genera y valida en un directorio temporal y solo entonces reconstruye el servicio documental existente. Conserva la imagen anterior como `last-good` y la restaura si el panel no responde `200` con el SHA esperado.

Para comprobar que los artefactos versionados siguen sincronizados sin reemplazarlos:

```bash
python scripts/docs_pipeline.py check
```

Los temporales se escriben únicamente en `.build/`, que no se versiona.

## Ejecutar la documentación en Nexus

### Primer arranque o actualización desplegada

```bash
cd /opt/apps/infra-replicant-lab
git switch main
git pull --ff-only origin main
docker compose up -d --build
```

Compose construye el sitio MkDocs estricto mediante el `Dockerfile` y ejecuta exclusivamente la etapa final Nginx. La web queda disponible en:

```text
http://192.168.18.220:8082
```

El runtime estático no usa `mkdocs serve` ni bind mounts. Por tanto, cada cambio documental desplegado requiere reconstruir y recrear la imagen con `docker compose up -d --build`.

## Portables canónicos

```text
docs/downloads/Replicant-Lab.html
docs/downloads/Replicant-Lab.pdf
docs/downloads/apps/<aplicacion>.html
docs/downloads/apps/<aplicacion>.pdf
```

El HTML global contiene toda la navegación MkDocs en un único fichero offline. El PDF A4 contiene portada, índice, páginas numeradas, texto seleccionable y los seis diagramas renderizados. Las fichas individuales cubren arquitectura, operación y evidencia de cada aplicación. Todos identifican la misma huella SHA-256 de sus fuentes.

## Flujo de cambios

```text
main → rama de cambio → generación y pruebas → commits → PR → revisión → merge → despliegue
```

Las ramas representan **cambios lógicos**, no archivos individuales.

## Principio de seguridad

No almacenar aquí contraseñas, tokens, claves privadas, bases de datos ni secretos reales.
