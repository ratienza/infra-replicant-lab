# RL-CW-DOC-003 · Cierre OAuth y publicación documental CryptoWallet V1.5

## Estado

`ready_for_review` · fuentes y derivados preparados; pendientes PR, CI, merge, publicación exclusiva de `docs` y verificación final en Nexus.

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

Pendiente de integración y publicación. Los SHA, PR, CI, imagen, rollback y comprobaciones reales se completarán antes de declarar `done`.
