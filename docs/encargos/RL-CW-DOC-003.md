# RL-CW-DOC-003 · Cierre OAuth y publicación documental CryptoWallet V1.5

## Estado

`done` · cambios de producto y Lab integrados; contenido publicado reconstruyendo exclusivamente `docs`; HTTP, marcadores, SHA y doce parejas HTML/PDF verificados en Nexus. La confirmación real Google → PIN → cartera sigue atribuida únicamente a Raúl.

## Repositorios y fuentes

| Repositorio | Fuente / rama |
|---|---|
| `ratienza/cryptowallet` | PR [#18](https://github.com/ratienza/cryptowallet/pull/18), `main@118577c7cf60f7f5733e6f4822f7194f7d37cd72`; fuente inicial `HANDOFF.md@7efc887d39a2e209734a2a2fa84535da9ee96ace` |
| `ratienza/infra-replicant-lab` | base `main@ca6a9708ce24ac5098ebc55203f37de38e3235f3`; rama `docs/rl-cw-doc-003-oauth-close` |

## Autorización y hechos aceptados

Raúl autoriza cambios documentales en ambos repositorios, Git, PR, merge y publicación exclusiva del servicio documental de Replicant Lab. V1.5 ya está desplegada. Google interno está activo y Raúl confirmó manualmente en incógnito Google → PIN → cartera el 09/10/2026 a las 22:33 Europe/Madrid. Raúl acepta cerrar la etapa.

PIN existente, política de 24 horas, privacidad inicial ON y copias locales multibase se conservan. Drive y ampliaciones funcionales son proyectos futuros independientes. Cuenta no autorizada, cancelación/error OIDC y recorrido móvil exterior no constan probados: son cobertura no verificada aceptada y no bloquean este cierre.

La confirmación real se atribuye a Raúl. El trabajo documental no inventa una inspección independiente, no ejecuta nuevas pruebas de OAuth, no lee secretos y no reinicia la aplicación.

## Alcance

- actualizar portada, arquitectura, operación, ficha, pendientes, decisiones, fases y Change Log;
- preservar RL-CW-DOC-002 y el Change Log inicial como registros históricos;
- retirar como pendientes alta OAuth, instalación de credenciales, activación Google y recorrido autorizado;
- regenerar las doce parejas HTML/PDF con el pipeline existente y revisar visualmente los PDF afectados;
- publicar desde `main` reconstruyendo únicamente el servicio Compose `docs`;
- verificar HTTP, contenido, SHA servido y coincidencia byte a byte de derivados con Git.

## Gates

1. Fuentes coherentes con el cierre manual y límites no verificados explícitos.
2. `python scripts/docs_pipeline.py generate` y `check`, sin refrescar roadmap ni cachés de ErasmusHomes.
3. PR revisable, CI `Docs check / build` correcto y merge autorizado.
4. Imagen documental previa conservada; checkout Nexus limpio y actualizado por fast-forward.
5. `docker compose up -d --build docs` ejecutado solo para `docs`.
6. HTTP 200, marcadores de cierre y doce parejas HTML/PDF idénticas a Git.
7. Evidencia final versionada y segunda publicación si el propio cierre cambia las fuentes.

## Límites

No redeplegar ni reiniciar CryptoWallet o Cartera. No modificar datos, PIN, credenciales, OAuth, Cloudflare Access, Tunnel, DNS o puertos. No leer ni publicar secretos. No implementar Drive ni ampliaciones funcionales. Rollback documental mediante la imagen conservada o revert Git y reconstrucción exclusiva de `docs`; nunca mediante restauración financiera.

## Resultado

| Control | Resultado |
|---|---|
| Producto | PR [CryptoWallet #18](https://github.com/ratienza/cryptowallet/pull/18) fusionado en `118577c7cf60f7f5733e6f4822f7194f7d37cd72` |
| CI del producto | El repositorio no tiene workflows/checks asociados a la PR; `statusCheckRollup` vacío, registrado sin fingir CI |
| Documentación | PR [Replicant Lab #53](https://github.com/ratienza/infra-replicant-lab/pull/53) fusionado en `8fd8efd7b5ad4b6399980846a5b501b5f94dec7c` |
| CI documental | `build` correcto en [run 37998259323, job 114049692950](https://github.com/ratienza/infra-replicant-lab/actions/runs/37998259323/job/114049692950) |
| Pipeline | `generate` y `check` correctos; `synchronized`; huella `edcaf44d3f01bf1c923b3850a527bc3c1a4af69be44e97c42f9e68e91598e759` |
| Publicación Nexus | Solo servicio `docs`; [http://192.168.18.220:8082/](http://192.168.18.220:8082/); checkout limpio y alineado en `8fd8efd7b5ad4b6399980846a5b501b5f94dec7c` |
| Imagen inicial del cierre | `sha256:4dd544159d77417c366bf4d96e8a2ab26db869848c86845c7596cf62e0a37190` |
| Recuperación | `infra-replicant-docs:rollback-ca6a970-before-8fd8efd` → `sha256:524c09cb59cdfe95b4161fe32bacf2340172d45e88f5b25c52612bb629613206` |

Comprobaciones realizadas tras `docker compose up -d --build docs`:

- HTTP 200 en portada, ficha CryptoWallet, pendientes, operación, Change Log 10/10, RL-CW-DOC-003 y propuesta Drive.
- Contenido servido: Google interno activo; confirmación manual de Raúl a las 22:33; PIN 24 horas; privacidad inicial ON; copias locales entregadas; límites OIDC/móvil no verificados y Drive independiente.
- Las doce parejas contractuales, 24 archivos, coinciden byte a byte con Git por SHA-256 (`MISMATCH=0`).
- Contenedor `infra-replicant-docs` en ejecución. No se reiniciaron ni redeplegaron CryptoWallet, Cartera u otros servicios.
- No se modificaron datos, PIN, credenciales, OAuth, Access, Tunnel, DNS, puertos, roadmap ni cachés de ErasmusHomes.

Esta actualización de cierre cambia de nuevo la fuente y sus derivados. Su PR, CI, SHA final servido, imagen final y repetición de las comprobaciones se registran en la propia PR para evitar una autorreferencia circular dentro del documento versionado.
