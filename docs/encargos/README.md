# Sistema de encargos

Cada encargo lógico vive en `docs/encargos/<ID>.md`. El archivo es el contrato durable entre Work, Codex y Git; el chat aporta conversación, no sustituye al contrato.

## Flujo mínimo

1. Work prepara el encargo en estado `draft`.
2. Raúl lo aprueba como `ready` y fija rama, SHA base y permisos.
3. Codex lo lee antes de modificar archivos y pasa a `in_progress` cuando corresponde.
4. La rama y el PR reúnen implementación, pruebas y evidencias accesibles.
5. `ready_for_review` permite revisar; no significa `accepted`.
6. Merge, despliegue, verificación y `done` requieren sus gates y evidencias propios.

Estados permitidos: `draft`, `ready`, `in_progress`, `ready_for_review`, `accepted`, `merged`, `deployed`, `verified`, `done`, `blocked`, `rejected` y `cancelled`.

Usa [la plantilla](TEMPLATE.md). [GOV-001](GOV-001.md) es el primer encargo real versionado.
