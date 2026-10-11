# Aplicación · Backups Lab V1.0

Versión 1.0.1, 12/10/2026. Cierre técnico autorizado por Raúl; no sustituye su aceptación humana. Repositorio [ratienza/backups-lab](https://github.com/ratienza/backups-lab), [release v1.0.1](https://github.com/ratienza/backups-lab/releases/tag/v1.0.1). [v1.0.0 histórica e inmutable](https://github.com/ratienza/backups-lab/releases/tag/v1.0.0). La referencia d2c7e1c/PR21 es histórica: PR22/main4c63ac1 ya integró cobertura, Drive, menú móvil, cola durable y la decisión explícita de diferir sustitución a v2.0.

Runtime privado en Nexus, puerto LAN **8087**.

## Corrección v1.0.1 · Configuración y controles globales

Configuración → Origen y descubrimiento muestra las carpetas guardadas, inicialmente `/opt/apps` (sin `$`). Añadir, editar y quitar → Guardar carpetas persiste la lista; Buscar nuevas aplicaciones enumera únicamente carpetas inmediatas de Nexus, sin leer archivos ni escanear la red. No sigue symlinks. Rutas inválidas, de sistema o no accesibles muestran causas concretas. Se admite una lista vacía para suspender el descubrimiento. Las candidatas nuevas aparecen NEW, pendientes de preparar: ninguna se activa ni copia; las previews siguen excluidas. Guardar o buscar no modifica adaptadores existentes, sus orígenes, horarios, exclusiones ni historial.

Cada aplicación tiene fuentes propias. Aplicaciones → Ver aplicación/Ver pendiente muestra las rutas efectivas del contrato; Cartera y Reserva usan `/opt/data`, Launch `/home/raul/app-launch`, Facility los volúmenes `docker-volume:facility-fac001_pg` y `docker-volume:facility-fac001_minio`. Descubrimiento no es el origen global de las copias ni amplía su cobertura.

Programación global ON/OFF requiere acceso autorizado y persiste separadamente de Activa por aplicación. OFF pausa reservas y ejecución automática pendiente; no cancela una copia ya iniciada y las manuales siguen disponibles. Conserva horarios y preferencias. ON reanuda solo las habilitadas desde ese instante, sin ejecutar copias inmediatas ni recuperar horas vencidas durante la pausa. La interfaz muestra su número. Siete aplicaciones habilitadas y Control Red OFF se preservan, sin modificar sus horas.

Retención ON/OFF de Configuración y Retención comparte estado real y confirmación. ON abre revisión de política 7/4/12/3 y alcance de ocho aplicaciones sin previews; exige acceso autorizado y casilla explícita. Cancelar no activa. OFF detiene futuras ejecuciones, no una operación manual ya aceptada. Inicialmente OFF; la última copia válida sigue protegida con programación global o individual OFF. La activación y borrado se prueban únicamente con estado sintético aislado.

Junto al campo de operaciones se muestra **Pista: raemda**. Es exclusivamente el recordatorio aprobado; no se utiliza como clave, no cambia la credencial ni revela su valor. Restore permanece diferido a V2.0.

## Acceso y seguridad

Aplicación: [HTTPS](https://backups.thereplicantlab.com/) y [LAN](http://192.168.18.220:8087/). Documentación canónica: [Replicant Lab](https://docs.thereplicantlab.com/aplicaciones/backups-lab/), [Nexus LAN](http://192.168.18.220:8082/aplicaciones/backups-lab/).

HTTPS exige Cloudflare Access existente y, además, autorización de operaciones propia de Backups Lab. Configuración → Autorizar operaciones con la clave conocida. La pista recordatoria no es una credencial y nunca se usa como clave. No introducir ni guardar claves en chat, Git, capturas o logs.

Configuración → Establecer o cambiar mi clave → descargar la herramienta privada → abrir Establecer clave.cmd → elegir/confirmar una clave propia en la ventana enmascarada. SSH usa el alias autenticado nexus y stdin, escritura atómica con permisos 0600 y comprobación de la API; cambiarla invalida las sesiones anteriores. [Procedimiento privado completo](https://github.com/ratienza/backups-lab/blob/main/docs/operator-access-private.md).

La interfaz muestra Acceso autorizado o causa y solución concretas: clave incorrecta401, origen rechazado403, configuración ausente/inválida503 o conexión fallida. Sesión firmada HttpOnly/SameSiteStrict de 8 horas, Secure en HTTPS, conservada en recarga/pantallas. La clave verdadera permanece privada en Nexus; no se exportó ni restableció para cerrar. El navegador HTTPS autorizado, previsualización real de ocho y persistencia tras recarga quedaron comprobados el 12/10/2026. No se cambió Cloudflare ni OAuth.

## Aplicaciones, cobertura y controles

Ocho aptas dentro de contratos verificados, no ocho respaldos integrales de todos los datos. El panel muestra Cobertura de las copias antes del gráfico, alcance, exclusiones y captura→Drive→recuperación aislada; sin porcentajes inventados. Datos, secretos y temporales permanecen fuera de Git.

| Aplicación | Alcance respaldado | Fuera del alcance |
|---|---|---|
| Launch | Publicación estática activa, recursos y configuración no secreta | Credenciales, sesiones y datos externos |
| Salones AV | Páginas y recursos publicados | localStorage/estado del navegador |
| Control Red | Demo publicada de solo lectura | Inventarios/dispositivos externos; sin escaneo de red |
| Replicant Lab | Fuentes, 13 PDF revisados en Nexus, reconstrucción MkDocs | Git, builds, credenciales y datos externos |
| CryptoWallet producción | Estado nativo, bases, operaciones, catálogo y ajustes no secretos bajo bloqueos | Seguridad/PIN/OAuth/sesiones/cachés y fuentes externas no persistidas |
| Cartera Nexus | Base efectiva SQLite y evidencias Indexa | Base Windows, seguridad/PIN/OIDC/credenciales |
| Reserva Pistas | Tareas, sincronización y auditoría con bloqueos compartidos | Credenciales, SSH, Telegram, procesos; no ejecuta reservas |
| Facility | PostgreSQL y objetos/buckets MinIO de servicios detenidos | IAM, identidades, proveedores, credenciales/sesiones; cobertura parcial, reprovisión necesaria |

Previews excluidas de nuevas copias, horarios y retención, con historial conservado. Facility está en el bloque plegable de inactivas, cuenta en Copiar todas y puede configurar copias sin arrancar sus diez contenedores originales. Candidatas pendientes sin adaptador validado no son seleccionables, tienen causa/Ver pendiente y conservan historial. Validar una candidata requiere su propio alcance autorizado y recorrido Drive.

Copiar una, seleccionadas o todas las aptas → revisar incluidos/excluidos → cancelar o confirmar. La verificación de cierre usa solo revisión/cancelación; no crea copias para probar ni ejecuta purgas. Los lotes comparten cola global de una ejecución y reserva/idempotencia en SQLite; cada aplicación tiene resultado independiente. El favicon caja fuerte, enlace Ver en Drive a la raíz configurada y menú móvil de cinco vistas reutilizan la identidad corporativa aprobada. Escape, foco y320px sin desbordamiento comprobados.

Activa significa programación automática ON/OFF. OFF conserva copia manual e historial. Configurar horario es accesible sin horario o en OFF; ON sin horario abre días/hora; Guardar y activar requiere autorización explícita y horario válido. Aptitud/cliente OAuth propio verificado son requisitos; el estado operativo detenido no bloquea el horario.

El11/10 se aplicó una sola vez la autorización de las ocho diariamente05:00 Europe/Madrid, sustituyendo Launch03:00. El arranque/deploy/discovery no reaplica valores. Al cierre se observa una pausa posterior persistida de Control Red: siete ON05 y Control Red OFF con05 guardada; se respeta sin reactivarla. Las nuevas incorporaciones validadas proponen05 y requieren incorporación autorizada. Reservas programadas app+instanteUTC únicas, incluidas aun con motor ocupado, cola pendiente durable tras restart y ejecución de una en una. Un cambio posterior cancela slots que ya no corresponden. Hora de primavera inexistente → primer minuto válido; hora repetida → primera ocurrencia. Recupera como máximo la última vencida en 24 horas, nunca anterior a activación. Próxima copia usa el mínimo real de las incluidas activas.

## Arquitectura y recuperación V1

Navegador React/Vite → Nginx → API FastAPI. SQLite persiste catálogo, horarios, reservas, eventos y diario de operaciones. Planificador reserva slots; trabajador global de una ejecución coordina copias, recuperación y retención. Captura consistente mediante adaptadores de archivos/SQLite/métodos nativos. Ayudante fijo en socket Unix con permisos 0600 valida UID y contratos; API no tiene socket Docker. rclone con cliente OAuth propio y raíz aprobada: subida inmutable → comprobación remota → descarga a directorio nuevo → manifiesto/conjunto/SHA256 iguales → lectores nativos/HTTP aislado. Solo esta evidencia permite aptitud; no se amplía por ocultar avisos.

Copias → Detalle → resultado de recuperación o Probar recuperación aislada cuando no esté ya verificada. Ensayo en directorio independiente: no sobrescribe producción, no reintegra secretos excluidos. El historial anterior de ocho recorridos Drive se reutiliza; las ocho últimas copias válidas observadas también tienen recuperación verificada. Evidencia y límites en [contratos](https://github.com/ratienza/backups-lab/blob/main/docs/operational-contracts.md), [matriz](https://github.com/ratienza/backups-lab/blob/main/docs/operational-matrix.md) y [recibo fechado](https://github.com/ratienza/backups-lab/blob/main/artifacts/v1-release/runtime-before.json). Repetir solo si cambia el contrato/método o la evidencia resulta insuficiente.

La sustitución de originales y rollback de aplicaciones fueron diferidos expresamente a v2.0 por Raúl el 11/10, no desplazados para ocultar un incumplimiento. En V1 no hay acciones operativas y API/ayudante rechazan preparación/confirmación/rollback (409). Código, 16 variantes de clones, diarios y snapshots se conservan. [Backlog V2.0](../pendientes/backups-drive.md) y [procedimiento futuro](https://github.com/ratienza/backups-lab/blob/main/docs/operational-lifecycle.md). El rollback de publicación de Backups Lab, descrito abajo, sí pertenece a V1.

## Retención e incidente

Automática **OFF**, independiente de horarios. Política7 diarias / 4 semanales / 12 mensuales / 3 anuales por aplicación, unión sin duplicar IDs. Conserva siempre última válida aun OFF/antigua fuera de bandas, BL-002, referencias de aptitud y registros usados en restauración. Excluye previews, objetos ajenos, originales y copias nativas fuera de gestión. Ensayo → revisar conservadas/eliminables/excluidas y motivos. Aplicación manual exige acceso, casilla, hash del inventario e ID estable; revalida antes de borrar. No aplicar retención para probar el cierre. Activación automática necesita elección explícita separada.

- Fallo manual randomUUID: en HTTP sin contexto seguro la función no existía; falló antes delPOST y no reservó operación. Corregido con generador central getRandomValues, confirmación, useRef contra doble envío e ID estable tras error/respuesta perdida. Restauración/rollback tienen IDs de servidor.
- Automática retention-auto-20261011: 11/10/2026 20:20:01UTC =22:20:01Madrid, succeeded, eliminó dos antiguas de Cartera y Launch. Auditoría remota de solo lectura confirmó ausencia; no se atribuye identidad a los cambios ON/OFF/ON.
- Manual retention-91413a6646a6d87e72ad5a68130d5213:20:53:13UTC del 11/10, succeeded, cero eliminaciones.
- Manual retention-81a56f35ed64306375f4ba48dfbcc160: iniciada22:02:21UTC del 11/10 =00:02:21Madrid del 12/10, ya running al comenzar este cierre; terminó succeeded con ocho eliminaciones. No fue una prueba de este encargo ni se atribuye autoría sin evidencia. No ocultarla ni confundirla con las dos automáticas anteriores. Se pausó la automática al observar ON según la instrucción vigente; esa pausa no cancela una manual ya aceptada.

Historial durable completo, sin reintroducir copias ni borrar registros. Los contadores y nuevas operaciones normales pueden cambiar; consultar API/recibo fechado en vez de congelar el total histórico19. Retención OFF y protecciones verificadas al publicar.

## Despliegue, SHA y rollback

Release/tag v1.0.1; v1.0.0 histórico sin sobrescritura. VERSION, API/OpenAPI y paquete frontend1.0.1. /api/status identifica versión y source_sha de la imagen; labels OCI de API/web identifican el mismo SHA construido. Construir con BACKUPS_LAB_REVISION del commit verificado, validar CI/Compose y recursos servidos contra bytes de la imagen. No requiere migración destructiva ni repite OAuth. Esperar que terminen copias/operaciones antes de recrear API o desplegar documentación.

Antes de desplegar: snapshots SQLite consistentes con permisos 0600 privados, imágenes/API/web/documentación anteriores etiquetadas y script privado de rollback. Rollback rechaza trabajo en curso, restaura solo código/imágenes y documentación; conserva historial actual y elecciones posteriores de horarios. No restaura aplicaciones originales ni borra Drive. El snapshot de DB es protección separada, no se restaura automáticamente. Seguir el recibo de publicación; no ejecutar rollback como prueba sobre producción.

## Verificación y continuidad

CI aplicable: 97 pruebas backend previas y cuatro nuevas dirigidas en Linux, build, compatibilidad HTTP sin randomUUID, confirmación/error/doble envío/ID, colaocho slots/persistencia/DST, última válidaOFF/1990/política cero, móvil/selección/orden/Drive y bloqueo v1. Evidencias reales previas de captura/Drive/descarga/hashes/recuperación reutilizadas. API aislada ya verificó ocho guardar/activar/pausar/restart sin trabajadores. HTTP/LAN y sesión HTTPS autorizada, recarga/pantallas, previsualización/cancelación y controles principales verificados; ningún valor de clave en evidencias. Los fixtures no sustituyen la prueba de Drive.

Alcance V1 técnico entregado; aceptación humana independiente. V2 solo backlog, sin implementación nueva. Informe diario por correo, log exportable, cifrado adicional, agentes externos, nuevos adaptadores y recuperación integral del host son propuestas anteriores pendientes de decisión/contrato, no se presentan como entregadas.

[Changelog V1.0](https://github.com/ratienza/backups-lab/blob/main/CHANGELOG.md) · [Backlog canónico V2.0](https://github.com/ratienza/backups-lab/blob/main/BACKLOG_V2.md) · [HANDOFF](https://github.com/ratienza/backups-lab/blob/main/HANDOFF.md).
