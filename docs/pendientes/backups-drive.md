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

[Pendientes Nexus](nexus.md) · [Copias locales de CryptoWallet](../aplicaciones/cryptowallet.md#copias-locales-y-restauracion-v15).
