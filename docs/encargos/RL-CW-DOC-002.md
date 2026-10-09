# RL-CW-DOC-002 · Cierre documental CryptoWallet V1.5

!!! note "Registro histórico"
    Este encargo conserva la publicación inicial con Google interno OFF. El cierre posterior de activación y aceptación manual se tramita en [RL-CW-DOC-003](RL-CW-DOC-003.md); no se reescribe la evidencia observada de este despliegue.

## Estado

`done` · etapa documental CryptoWallet V1.5 cerrada. El contenido de PR #51 está integrado y publicado en Nexus, con origen HTTP, páginas de cierre y descargables verificados. Google interno, el recorrido exterior autenticado y la réplica Drive conservan su estado pendiente y no forman parte de este cierre.

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

La integración en Git y la publicación Nexus son estados separados; se verificaron ambas expresamente. Rollback documental disponible mediante la imagen etiquetada antes de la reconstrucción, o mediante revert Git y reconstrucción exclusiva del sitio; nunca mediante recuperación de bases financieras.

## Resultado verificado en Nexus · 09/10/2026

| Control | Resultado |
|---|---|
| Git canónico | PR [#51](https://github.com/ratienza/infra-replicant-lab/pull/51) fusionado en `b113043a511bd01d78e5654c62ad1d42d39f8f5f` |
| CI de #51 | `Docs check / build` correcto: [run 37940044934, job 113851805773](https://github.com/ratienza/infra-replicant-lab/actions/runs/37940044934/job/113851805773) |
| Checkout Nexus publicado | `/opt/apps/infra-replicant-lab`, rama `main`, limpio y alineado con `origin/main` en `b113043a511bd01d78e5654c62ad1d42d39f8f5f` |
| Publicación | Solo servicio Compose `docs`; contenedor `infra-replicant-docs`; origen [http://192.168.18.220:8082/](http://192.168.18.220:8082/) |
| Imagen publicada | `sha256:1d76508fdce99d723653d357956d6e2386ed94722b91aeeb7f592ba0e397c138` |
| Recuperación | Imagen anterior `sha256:b4c8804eff74637d6db955afe882aa4bdfe3fdb8e65ac036419680ef39db3861`, conservada como `infra-replicant-docs:rollback-8701f03-before-b113043` |

Comprobaciones realizadas tras `docker compose up -d --build docs`:

- HTTP 200 en portada, ficha CryptoWallet, pendientes CryptoWallet, Change Log del 09/10/2026 y propuesta Drive.
- El contenido servido muestra V1.5, PIN activo 24 horas, privacidad inicial ON y copias locales entregadas.
- Google interno figura preparado pero OFF; OIDC real y recorrido exterior autenticado continúan pendientes.
- Drive figura como proyecto futuro independiente, no implementado ni programado.
- Las doce parejas HTML/PDF contractuales, 24 archivos, coinciden byte a byte por SHA-256 con el checkout publicado.
- El contenedor activo usa la imagen reconstruida desde el checkout citado. No se redeplegaron CryptoWallet, Cartera ni otros servicios, y no se modificaron bases, datos, secretos, PIN, OAuth, Access, Tunnel, DNS o puertos.

El cierre operativo se tramita en una PR posterior de alcance único. Su SHA de merge, CI y la repetición de estas comprobaciones sobre el contenido final se registran en la propia PR para evitar una referencia circular dentro del documento versionado.
