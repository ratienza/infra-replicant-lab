# RL-CW-DOC-002 · Cierre documental CryptoWallet V1.5

## Estado

`blocked` · cierre documental preparado para integración por PR; publicación Nexus pendiente de recuperar el canal remoto: RAN-CASA observado desconectado. Las referencias de commit, PR y CI se registran en GitHub. No se declara publicado este cambio.

## Repositorios y Git

Canónico: `ratienza/infra-replicant-lab`; base `8701f03e4b5c2f5812a8362206a58f2b1cbbfeae`; rama `docs/cryptowallet-v1.5-close`. Producto relacionado, solo lectura: `ratienza/cryptowallet`, aceptación y HANDOFF fijados al main documental `17489d38ab5398de80c37d4985b15f23f131874f`. No modificar otros repositorios.

## Objetivo y autorización

Raúl solicita el 09/10/2026: «Documentar todo en nexus, en la docu general, pendientes, ficha [...] documenta todo y cerramos etapa». Autoriza actualización documental, Git/PR, integración tras validación y publicación exclusiva del servicio Replicant Lab. No autoriza nuevos desarrollos, activación Google, restauraciones ni redepliegue financiero.

## Alcance y fuentes

| Impacto | Fuentes canónicas actualizadas |
|---|---|
| Estado global y catálogo | README, portada, aplicaciones, evolución |
| Identidad, funciones, seguridad y copias V1.5 | Ficha CryptoWallet |
| Infraestructura y operación | Arquitectura, Nexus, inventario, modelos, mantenimiento, Cloudflare |
| Deuda vigente | Pendientes CryptoWallet, Nexus, resumen; nueva propuesta Drive |
| Historia y continuidad | Decisiones, Change Log 09/10, este encargo |
| Derivados | Doce parejas HTML/PDF mediante generador existente |

[HANDOFF del producto](https://github.com/ratienza/cryptowallet/blob/17489d38ab5398de80c37d4985b15f23f131874f/HANDOFF.md) y [aceptación CW-V15](https://github.com/ratienza/cryptowallet/blob/17489d38ab5398de80c37d4985b15f23f131874f/docs/evidence/CW-V15/acceptance.md). Se distingue evidencia de promoción aportada por el producto de una nueva inspección remota, que este trabajo no ha realizado.

## Gates de aceptación

1. Fuentes coherentes con V1.5; sin marcar PIN/copias locales como aplazados ni Google/Drive como operativos.
2. Pipeline `generate` y `check`, panel ErasmusHomes `check`, diff limpio y CI oficial verde. Derivados sincronizados con una misma huella; sin refrescar roadmap ErasmusHomes.
3. PR revisable, merge autorizado solo tras checks; referencias finales en el PR para evitar autorreferencia circular.
4. Publicar desde main reconstruyendo **solo** `infra-replicant-docs`; conservar imagen anterior y validar HTTP, ficha, pendientes y descargas idénticas a Git.
5. Registrar SHA servido y evidencia de publicación antes de declarar `done`.

## Riesgos, pendientes y recuperación

Repositorio público: sin saldos, datos privados, cuentas autorizadas, rutas privadas de copias, manifiestos financieros ni secretos. No cambiar bases, aplicaciones, permisos, Access/Tunnel, DNS ni puertos. La propuesta Drive es futura; no se crea una tarea ni se envía correo.

Canal privado Nexus no disponible durante la preparación. La integración en Git y la publicación Nexus son estados separados; no extrapolar uno al otro. Rollback documental con imagen previa o revert Git y reconstrucción exclusiva del sitio, nunca recuperación de bases financieras.

## Siguiente paso

Completar los gates de Git/CI registrados en el PR y publicar cuando el canal Nexus esté disponible. La etapa funcional V1.5 está cerrada; el gate documental Nexus permanece pendiente hasta comprobar el sitio servido.
