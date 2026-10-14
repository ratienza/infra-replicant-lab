# Evolución del laboratorio

La historia detallada se conserva en el [Change Log](../cambios/index.md). Para operar el laboratorio basta con estos hitos:

| Etapa | Resultado |
|---|---|
| Construcción inicial | Replicant quedó como estación principal y host Hyper-V; Nexus como laboratorio Ubuntu/Docker. |
| Auditoría y normalización | Se inventariaron hosts, red, aplicaciones, checkouts y runtimes sin confundir presencia de código con ejecución. |
| Remediaciones | Salones AV quedó reconciliado en Git/Nexus; Consumos Cupra quedó trazado y restaurado en Cloud Run; el CV quedó identificado en Firebase Hosting. |
| Publicación externa | Un único Tunnel publica Launch, Salones, Docs, Pádel y Red sin puertos entrantes; Google y Access autorizan cada hostname de forma independiente. |
| CryptoWallet V1.0 · 08/10/2026 | Aceptada y en producción privada Nexus; previa independiente, copia consistente y documentación vigente. Importación nueva en V2. |
| CryptoWallet V1.5 · 09/10/2026 | Google interno activo, PIN 24 h, privacidad inicial ON, copias multibase y navegación adaptable desplegados; recorrido autorizado confirmado manualmente. Réplica Drive independiente. |
| CryptoWallet V1.6.2 · 14/10/2026 | Logbook V1.6.1 preservado; favicon BTC SVG e identidad corporativa oficial desplegados en cabecera y pie, con título/navegación centrados y respuesta claro/oscuro/móvil. Datos y único borrador BTC activo preservados. |
| Backups Lab v1.1.2 ·12/10/2026 | Aceptada definitivamente y publicada: fichas compactas, 0 candidatas pendientes, 7 vinculadas plegadas y visibilidad reversible; nueve adaptadores y copia/recuperación preservadas; [manual y límites](../aplicaciones/backups-lab.md). |
| Estado actual | Las fases 2A, 2B y 2C están cerradas. No hay una incidencia crítica abierta en esas aplicaciones. |
| Trabajo futuro | La deuda aceptada se concentra en [Pendientes](../pendientes/index.md); Cartera v2.1.0 y CryptoWallet V1.6.2 ya están cerradas. Un nuevo bloque requiere encargo. |

## Criterio de validación

Cada aplicación se valida con los mecanismos apropiados para su tecnología: tests, lint, build, configuración, Compose, healthchecks, runtime o HTTP. La evidencia concreta vive en su [ficha técnica](../aplicaciones/index.md), sin duplicar aquí los listados de pruebas.

Backups Lab **v1.1.2** cierra fichas e inventario visible: candidatas independientes y vinculadas separadas, con ocultación reversible. Se preservaron retención ON 7/4/12/3, seis horarios ON/tres OFF, Facility detenida y Restore V2. [Manual vigente](../aplicaciones/backups-lab.md).
