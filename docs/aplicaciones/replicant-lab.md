# Aplicación · Replicant Lab

Documentación canónica del laboratorio: arquitectura, hosts, red, despliegues, operación, decisiones, pendientes y fichas técnicas de aplicaciones.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/replicant-lab.html)
- **Aplicación / Nexus:** [Replicant Lab](http://192.168.18.220:8082/)

## Estado auditado

| Campo | Valor |
|---|---|
| Desarrollo | Codex / MkDocs / Mermaid |
| Repositorio | `ratienza/infra-replicant-lab` · `main` |
| Punto de partida del cierre | `0134f5bdf932128de47545a03acab593027f797f` |
| Nexus | `/opt/apps/infra-replicant-lab` · checkout limpio observado |
| Servicio | Compose `docs` · contenedor `infra-replicant-docs` |
| Imagen | `infra-replicant-docs:local`, construida desde el `Dockerfile` |
| URL / puerto | `http://192.168.18.220:8082` · `192.168.18.220:8082 → 80/tcp` |
| Reinicio | `restart: unless-stopped` |

## Arquitectura y funcionamiento

Markdown, `mkdocs.yml` y los recursos de `docs/` son la fuente de verdad. El pipeline calcula una huella SHA-256, construye MkDocs en modo estricto y genera el dossier global y las fichas HTML/PDF individuales.

El Dockerfile usa dos etapas: Python/MkDocs construye el sitio y Nginx `1.27.4-alpine` sirve únicamente el resultado estático. El runtime no usa `mkdocs serve`, bind mounts, base de datos ni almacenamiento persistente.

## Actualización y rollback

```bash
cd /opt/apps/infra-replicant-lab
git switch main
git pull --ff-only origin main
docker compose up -d --build
```

La actualización se realiza solo después de integrar el PR. Para rollback se revierte el cambio mediante GitHub, se actualiza de nuevo `main` y se reconstruye exclusivamente este servicio; no se recupera código desde el contenedor.

## Pruebas realizadas

- `python scripts/docs_pipeline.py generate --screenshots`: correcto.
- `python scripts/docs_pipeline.py check`: sincronía correcta.
- 32 páginas fuente y seis diagramas Mermaid validados por el pipeline.
- Dossier global de 52 páginas y ocho fichas individuales HTML/PDF sincronizadas.
- Runtime Nexus observado con respuesta `200` el 13/08/2026; la nueva versión se valida de nuevo tras el merge.

## Seguridad, dependencias y pendientes

- No almacena secretos, datos vivos ni backups; GitHub contiene solo documentación y configuración versionable.
- La tipografía remota del tema es opcional: una caída de Google Fonts no bloquea el contenido ni los recursos locales.
- Depende de GitHub para actualización y de Docker para reconstrucción; no depende de las aplicaciones documentadas para servir el sitio.
- Pendiente transversal: definir y probar la política de backup/restauración de Nexus. La documentación está en Git, pero eso no sustituye los backups de datos de otras aplicaciones.
