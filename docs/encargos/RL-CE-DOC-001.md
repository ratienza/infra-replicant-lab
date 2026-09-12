# RL-CE-DOC-001 — Cierre documental de Cartera Estratégica v1.0 LAN

## Estado

`completed`

## Repositorios

- Canónico: `ratienza/infra-replicant-lab`
- Relacionados: `ratienza/cartera-estrategica`, `ratienza/Apps_Lauch`
- No afectados: runtimes, datos privados, Cloudflare, Google Cloud, DNS, Tunnel, Access y router

## Git

- SHA base: `0797b60f9da4f7b4d40382c37091ff01f14da389`
- Rama: `codex/rl-ce-doc-001`

## Objetivo y contexto

Cerrar la documentación canónica de Cartera Estratégica v1.0 tras su migración LAN real a Nexus y regenerar los derivados globales y por aplicación.

## Alcance

- Ficha, catálogo, App Launch, inventarios, puertos, arquitectura, Change Log y pendientes.
- Guía mínima de arranque, actualización, backup, restauración y recuperación.
- Regeneración y validación oficial de HTML/PDF.
- PR, CI, merge y actualización del runtime documental `8082`.

## Fuera de alcance

- Cambios en Cartera, su SQLite, App Launch o sus runtimes.
- Cloudflare, Google, DNS, Tunnel, Access o publicación externa.
- Reinicio de servicios distintos de la documentación, si su imagen estática requiere recreación.

## Restricciones y autorizaciones

- Merge permitido: sí, únicamente esta PR con CI verde.
- Despliegue permitido: sí, exclusivamente documentación en Nexus `8082` mediante el flujo Git canónico.

## Criterios de aceptación

- Fuentes canónicas coherentes con el runtime LAN real.
- CE-SEC-001 documentado según el estado observado en `main`.
- HTML/PDF globales y por aplicación sincronizados.
- Checks oficiales, enlaces, `git diff --check` y CI correctos.
- Sitio vivo `8082`, navegación y descargas validados sin 404.

## Pruebas obligatorias

- `python scripts/erasmushomes_panel.py check`
- `python scripts/docs_pipeline.py check`
- `git diff --check`
- Build y smoke test de la imagen documental.

## Evidencias accesibles

- GitHub `main` de Cartera en `721338b`.
- HTTP `200` en App Launch `:80`, Replicant Lab `:8082` y Cartera `:8085`.
- Catálogo Nexus servido con enlace a `http://192.168.18.220:8085`.

## Impacto documental

| Cambio | Documento que debe actualizarse |
|---|---|
| Runtime y seguridad de Cartera | Ficha de aplicación y pendientes |
| Puerto `8085` | Nexus, inventario y Docker |
| Navegación LAN | App Launch y catálogo de aplicaciones |
| Cierre | Change Log, portada y modelos |

## Riesgos y bloqueos

- No certificar Google OAuth como activo sin HTTPS y prueba real.
- No sobrescribir cambios locales de Nexus.
- No mezclar el pendiente externo de Cartera con la implantación Cloudflare existente.

## Rollback

Revertir la PR mediante Git y reconstruir exclusivamente la imagen estática de documentación desde `main`.

## Resultado

Fuentes canónicas y derivados actualizados. La generación oficial produjo 52 páginas fuente, 17 diagramas Mermaid, el PDF global de 111 páginas y diez fichas HTML/PDF. La validación local recorrió 38 rutas sin errores; el primer ciclo de CI completó además el build Docker y el smoke test Nginx.

## Cierre Git

- SHA documental validado: `1095d8e`
- PR: `ratienza/infra-replicant-lab#45`
- CI: verde · GitHub Actions `34705023529`

## Limitaciones y pendientes

La activación externa de Cartera se mantiene como encargo independiente.

## Siguiente paso

Fusionar únicamente la PR #45 y actualizar el runtime documental Nexus `8082` mediante el flujo Git canónico.
