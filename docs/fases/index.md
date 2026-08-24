# Evolución del laboratorio

La historia detallada se conserva en el [Change Log](../cambios/index.md). Para operar el laboratorio basta con estos hitos:

| Etapa | Resultado |
|---|---|
| Construcción inicial | Replicant quedó como estación principal y host Hyper-V; Nexus como laboratorio Ubuntu/Docker. |
| Auditoría y normalización | Se inventariaron hosts, red, aplicaciones, checkouts y runtimes sin confundir presencia de código con ejecución. |
| Remediaciones | Salones AV quedó reconciliado en Git/Nexus; Consumos Cupra quedó trazado y restaurado en Cloud Run; el CV quedó identificado en Firebase Hosting. |
| Estado actual | Las fases 2A, 2B y 2C están cerradas. No hay una incidencia crítica abierta en esas aplicaciones. |
| Trabajo futuro | La deuda aceptada se concentra en [Pendientes](../pendientes/index.md) y se retomará después de Cartera Estratégica. |

## Criterio de validación

Cada aplicación se valida con los mecanismos apropiados para su tecnología: tests, lint, build, configuración, Compose, healthchecks, runtime o HTTP. La evidencia concreta vive en su [ficha técnica](../aplicaciones/index.md), sin duplicar aquí los listados de pruebas.
