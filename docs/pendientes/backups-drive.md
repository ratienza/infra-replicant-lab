# Backlog V2.0 · Backups Lab

Derivado de propuestas previas y del aplazamiento expreso de sustitución el 11/10/2026. No implementa V2 ni convierte requisitos v1.1.3 cumplidos en mejoras. v1.1.3 está publicada y verificada técnicamente con nueve alcances/Drive/recuperación aislada, compatibilidad versionada, manual/cola/horarios, descubrimiento persistente, retención protegida y editable, acceso HTTP/HTTPS, interfaz y documentación. No queda ningún requisito terminado etiquetado como bloqueado; esta página conserva solo limitaciones de cobertura y propuestas V2 reales. Cierre y evidencia: [v1.1.3](../aplicaciones/backups-lab.md).

| ID / prioridad | Qué falta / problema | Dependencias y decisión | Criterio de aceptación |
|---|---|---|---|
| V2-001 · P1 | Habilitar sustitución y rollback originales en producto V2; hoy API/ayudante V1 bloqueados | Decisión explícita de Raúl sobre destino/ventana/riesgo; código, 16 variantes y snapshots existentes | Revisión vinculada a copia/destino/hash, backup previo consistente, confirmación, idempotencia, bloqueos, reanudación solo de servicios antes activos y fallos con rollback probados en aislamiento; operación original solo tras elección/confirmación futura |
| V2-002 · P1 | Adaptadores futuros y fuentes fuera de Nexus, incluida base Windows hoy excluida | Raúl decide apps/rutas/agente/transporte/disponibilidad; contrato y exclusiones de secretos | Captura consistente, Drive remota, descarga y hashes iguales, lectores/HTTP aislado y originales preservados por adaptador; no previews/aptitud implícita; incorporación05 propuesta con autorización |
| V2-003 · P1 | Evaluar cifrado adicional de archivos financieros con rclone crypt propuesto; V1 no promete cifrado de cliente extremo a extremo | Decisión de Raúl sobre alcance, clave/custodia externa, cuota y recuperación; no modificar copias actuales sin protocolo | Dataset sintético cifrado/subido/descargado/descifrado con hashes iguales, recuperación de clave probada y ausencia de valores sensibles en Git/logs/capturas; evidencia separada del transporte V1 |
| V2-004 · P2 | Informe diario por correo y log exportable propuestos en 09/10 | Destinatario, hora, proveedor/canal y campos/exportación por decidir por Raúl; no hay envío autorizado | Diferenciar captura ausente, transferencia fallida y remota verificada; informe derivado de eventos reales, exportación sin secretos, deduplicación y ensayo aislado sin enviar a terceros no autorizados |
| V2-005 · P2 | Reintentos/avisos de réplica de la propuesta inicial más allá de los comportamientos actuales | Raúl define límites de reintento/alerta/canal; respetar política latest-only de 24 horas y unicidad | Caídas/red/origen ausente probados sintéticamente, estados/cause claras, retorno de conexión sin duplicar copia/slot ni eliminar destino por desaparición local |
| V2-006 · P1 | Recuperación integral del host Nexus y reprovisión de secretos/IAM excluidos | Política global del host separada, fuentes de secretos privadas y runbook/ventana elegidos por Raúl | Inventario autorizado y ensayo de desastre aislado de host/secretos con recuperación segura; no confundir nueve alcances de apps con respaldo integral Nexus |

P1: seguridad/recuperación y alcance; P2: operación y observabilidad. Las prioridades ordenan el backlog, no autorizan ejecución. Propuesta09/10 de sondeo15-60min no se activa: V1 mantiene horarios explícitos elegidos, sin reaplicar al iniciar/desplegar/descubrir. Identidad corporativa aprobada existente se conserva; no reabrir diseño de banners ni inventar variantes.

## Histórico · Propuesta del09/10/2026

> La propuesta inicial se conserva como historial; sus estados «no implementado» no describen Backups Lab v1.1.3 ni la implementación posterior. El alcance cerrado y las decisiones necesarias de V2 se declaran arriba.

# Pendiente · Réplica automática de copias en Google Drive

**Propuesta anotada por Raúl el 09/10/2026; no implementada, desplegada ni programada.** Proyecto independiente de CryptoWallet y Cartera. No bloquea sus versiones cerradas.

## Objetivo

Servicio siempre en ejecución que lea los directorios de copias de varias aplicaciones, deje una copia en la carpeta Drive indicada para cada una, funcione sin intervención cotidiana y envíe un informe diario por correo. Mantendrá un log exportable.

## Diseño acordado a grandes rasgos

| Pieza | Función propuesta |
|---|---|
| Coordinador en Nexus | Aplicaciones, directorios origen, carpetas destino, horarios y estado |
| rclone | Motor de transferencia a Drive; evitar desarrollar de cero el conector |
| Copias de cada aplicación | Producir conjuntos completos y consistentes; el servicio replica copias finalizadas, no bases vivas |
| Orígenes en otro equipo | Agente o transferencia segura; resolver disponibilidad sin suponer acceso permanente al disco local |
| Registro exportable | Fecha, aplicación, archivo, tamaño, resultado, reintentos y verificación |
| Informe diario | Separar copia local ausente, transferencia fallida y réplica remota verificada |

Frecuencia orientativa de 15–60 minutos, por decidir. Reintentos y verificación remota; evitar archivos parciales y duplicados. Retención remota independiente, sin propagar automáticamente borrados locales. El correo destinatario, hora, proveedor y canal se confirmarán en el encargo específico; no se ha enviado ningún informe.

## Seguridad y aceptación futura

Credenciales propias del servicio y autorización privada de Drive, independientes del login Google de las aplicaciones y del conector de Work. Cifrar archivos financieros antes de subirlos; conservar una copia de la clave fuera de Nexus. No depender de que Work esté abierto. Rutas privadas, tokens, claves y contenido de copias fuera de Git.

La aceptación exigirá descargar una copia remota, verificarla, descifrarla y restaurarla en aislamiento; comprobar pérdida de red, reintentos, ausencia de copia local, reinicio y avisos. Definir coste/cuota, política de retención, directorios, permisos y recuperación de credenciales antes de desplegar.

rclone es una herramienta de línea de comandos para copiar y gestionar archivos en servicios de almacenamiento. Referencias oficiales: [Google Drive](https://rclone.org/drive/), [copy](https://rclone.org/commands/rclone_copy/) y [crypt](https://rclone.org/crypt/). `copy` replica sin borrar el destino por la desaparición del origen; la política de conservación deberá implementarse y validarse expresamente.

[Pendientes Nexus](nexus.md) · [Copias locales de CryptoWallet](../aplicaciones/cryptowallet.md#copias-locales-y-restauracion-v168).
