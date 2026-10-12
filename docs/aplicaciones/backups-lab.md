# Aplicación · Backups Lab v1.1.2

Versión 1.1.2, 12/10/2026. Aceptada definitivamente por Raúl, fusionada y publicada. Repositorio [ratienza/backups-lab](https://github.com/ratienza/backups-lab), [release v1.1.2](https://github.com/ratienza/backups-lab/releases/tag/v1.1.2), PR funcional [#28](https://github.com/ratienza/backups-lab/pull/28) y evidencia [#29](https://github.com/ratienza/backups-lab/pull/29). Código funcional `8f703237…`; runtime y release comprobados en `69c2957a99137bfe48bb9e97859c1e161a243e1d`. El sello documental posterior no cambia el runtime; las versiones anteriores permanecen históricas e inmutables.

## v1.1.2 · Fichas de descubrimiento y visibilidad

Aplicaciones conserva la cuadrícula compacta aceptada. Solo candidatas independientes pendientes llevan «NUEVA CANDIDATA» y cuentan en Dashboard; ruta, estado y acciones permanecen visibles y el detalle técnico queda plegado. Los siete orígenes vinculados aparecen al final en «Carpetas vinculadas (7)», cerrada por defecto, identifican su aplicación y no participan como aplicaciones independientes en contadores o copias.

«Ignorar esta carpeta» corresponde a candidatas pendientes y «Ocultar del descubrimiento» a orígenes vinculados. Las dos acciones son persistentes y reversibles; si falta acceso, conservan la intención, ofrecen autorización y continúan después. Ocultar no borra carpetas de Nexus ni modifica vínculos, adaptadores, cobertura, horarios, retención, copias o historial. Redescubrir conserva lo oculto y no duplica filas.

La comprobación publicada fue de solo lectura: 20 capturas de cinco vistas más 4 de vinculadas desplegadas, claro/oscuro y 1440/390, sin mutaciones, errores ni desbordamiento. Observación de cierre a las 22:53 CEST: 55 registros, cero trabajos activos, programación global ON, seis horarios ON, retención ON 7/4/12/3, Facility detenida, previews excluidas, BL-002 y Restore V2. No se ejecutaron copias, purgas o restauraciones productivas.

Runtime privado en Nexus, puerto LAN **8087**.

## v1.1.1 · Descubrimiento e incorporación segura

Descubrimiento guarda candidatas fuera del catálogo operativo y conserva primera detección, última comprobación, clasificación y decisiones de ignorar, reincorporar o vincular. Repetir la búsqueda no duplica filas ni reabre decisiones. El aviso del Dashboard aparece solo si queda una candidata independiente pendiente y abre directamente su revisión.

Las seis rutas solicitadas quedaron resueltas: `Apps_Lauch` se vincula a Launch; `CV-Raul-IA-Estudio-Google-`, `ErasmusHomes` y `Pula` son repositorios sin persistencia operativa adicional; `cartera-estrategica` se vincula a Cartera y mantiene la base Windows fuera; `backups-lab` es independiente. Cinco checkouts versionados adicionales de Cartera y Replicant Lab se vincularon expresamente, sin contarlos como aplicaciones nuevas. Resultado final: 11 carpetas clasificadas y 0 pendientes.

Backups Lab se incorporó como novena aplicación mediante un backup SQLite consistente de su estado operativo. OAuth, clave de operador, temporales, staging, recuperaciones, rollbacks y socket quedan excluidos. La primera copia `backups-lab-production-20261012T152703Z-471491a9ab` completó subida inmutable, comprobación remota, descarga, manifiesto SHA-256 `4272723b255d6f684d09b6e616cd7c44fe5d822885d2a68072e0b79e1baf65e5` y recuperación funcional en una API aislada. Solo entonces quedó diaria a las 05:00 Europe/Madrid.

El cierre preserva 55 copias, BL-002, programación global ON, retención ON con política 7/4/12/3, seis aplicaciones ON05 y tres OFF05. Facility continúa completamente detenida, preview y Cartera Windows fuera y Restore en V2. La publicación verificó 20 layouts reales y no repitió OAuth, lotes anteriores, borrados ni restauraciones productivas.

## v1.1.0 · Copias manuales y controles finales

«Copiar seleccionadas» y «Copiar todas» vuelven a completar el recorrido real. Si falta autorización, la aplicación conserva la selección o la intención de copiar todas, explica lo que falta y permite autorizar sin abandonar Aplicaciones; después continúa con la revisión protegida. La confirmación ejecuta exactamente las aplicaciones revisadas, con `request_id` estable y guardas contra doble clic o reintentos duplicados. «Todas» incluye las ocho admitidas, activas o inactivas, y excluye previews.

La comprobación publicada ejecutó dos lotes reales autorizados: `manual-6fca8984d688de47f781c95ee3344411` para Control Red, 1/1 verificada y recuperada; y `manual-a17f628f32b43a65faac19734addf205` para todas las admitidas, 8/8 verificadas y recuperadas, cero previews y una sola copia efectiva en ejecución. Los resultados aparecen en Copias. Al cierre había 52 registros y ningún trabajo activo.

El Dashboard muestra ON/OFF informativo por aplicación desde el mismo `operational_state` de Aplicaciones y aclara que no es el horario. En cada grupo, las aplicaciones en ejecución aparecen primero y «Aplicaciones detenidas» después, sin duplicados. La política permite editar diarias, semanales, mensuales y anuales; guardar exige autorización, persiste los valores y recalcula la previsualización, pero no ejecuta limpieza ni cambia el ON/OFF. Política observada y persistida tras reiniciar la API: 7/4/12/3.

## Corrección v1.0.1 · Configuración y controles globales

Configuración → Origen y descubrimiento muestra las carpetas guardadas, inicialmente `/opt/apps` (sin `$`). Añadir, editar y quitar → Guardar carpetas persiste la lista; Buscar nuevas aplicaciones reconcilia carpetas inmediatas de Nexus con aplicaciones, rutas vinculadas, exclusiones y decisiones persistentes. No sigue symlinks. Rutas inválidas, de sistema o no accesibles muestran causas concretas. Se admite una lista vacía para suspender el descubrimiento. NEW no activa ni copia; las previews siguen excluidas. Guardar o buscar no modifica adaptadores existentes, sus orígenes, horarios, exclusiones ni historial.

Cada aplicación tiene fuentes propias. Aplicaciones → Ver aplicación/Ver pendiente muestra las rutas efectivas del contrato; Cartera y Reserva usan `/opt/data`, Launch `/home/raul/app-launch`, Facility los volúmenes `docker-volume:facility-fac001_pg` y `docker-volume:facility-fac001_minio`. Descubrimiento no es el origen global de las copias ni amplía su cobertura.

Programación global ON/OFF requiere acceso autorizado y persiste separadamente de «Copias automáticas» por aplicación. OFF pausa reservas y ejecución automática pendiente; no cancela una copia ya iniciada y las manuales siguen disponibles. Conserva horarios y preferencias. ON reanuda solo las habilitadas desde ese instante, sin ejecutar copias inmediatas ni recuperar horas vencidas durante la pausa. La interfaz muestra su número. Seis aplicaciones habilitadas y tres deshabilitadas se preservan, sin modificar sus horas.

Retención ON/OFF de Configuración y Retención comparte estado real y confirmación. ON abre revisión de la política guardada y alcance de nueve aplicaciones sin previews; exige acceso autorizado y casilla explícita. Cancelar no activa. OFF detiene futuras ejecuciones, no una operación manual ya aceptada. En la observación de cierre v1.1.1 ya estaba ON y se mantuvo ON: este encargo no la activó, pausó ni aplicó manualmente. La última copia válida y las copias protegidas se conservan siempre.

Junto al campo de operaciones se muestra **Pista: raemda**. Es exclusivamente el recordatorio aprobado; no se utiliza como clave, no cambia la credencial ni revela su valor. Restore permanece diferido a V2.0.

## Acceso y seguridad

Aplicación: [HTTPS](https://backups.thereplicantlab.com/) y [LAN](http://192.168.18.220:8087/). Documentación canónica: [Replicant Lab](https://docs.thereplicantlab.com/aplicaciones/backups-lab/), [Nexus LAN](http://192.168.18.220:8082/aplicaciones/backups-lab/).

HTTPS exige Cloudflare Access existente y, además, autorización de operaciones propia de Backups Lab. Configuración → Autorizar operaciones con la clave conocida. La pista recordatoria no es una credencial y nunca se usa como clave. No introducir ni guardar claves en chat, Git, capturas o logs.

Configuración → Establecer o cambiar mi clave → descargar la herramienta privada → abrir Establecer clave.cmd → elegir/confirmar una clave propia en la ventana enmascarada. SSH usa el alias autenticado nexus y stdin, escritura atómica con permisos 0600 y comprobación de la API; cambiarla invalida las sesiones anteriores. [Procedimiento privado completo](https://github.com/ratienza/backups-lab/blob/main/docs/operator-access-private.md).

La interfaz muestra Acceso autorizado o causa y solución concretas: clave incorrecta401, origen rechazado403, configuración ausente/inválida503 o conexión fallida. Sesión firmada HttpOnly/SameSiteStrict de 8 horas, Secure en HTTPS, conservada en recarga/pantallas. La clave verdadera permanece privada en Nexus; no se exportó ni restableció para cerrar. El navegador HTTPS autorizado, previsualización real de ocho y persistencia tras recarga quedaron comprobados el 12/10/2026. No se cambió Cloudflare ni OAuth.

## Aplicaciones, cobertura y controles

Nueve aptas dentro de contratos verificados, no nueve respaldos integrales de todos los datos. El panel muestra Cobertura de las copias antes del gráfico, alcance, exclusiones y captura→Drive→recuperación aislada; sin porcentajes inventados. Datos, secretos y temporales permanecen fuera de Git.

| Aplicación | Alcance respaldado | Fuera del alcance |
|---|---|---|
| Backups Lab | SQLite de inventario, historial, horarios, retención y evidencias | OAuth, clave de operador, temporales/staging, recuperaciones, rollbacks y socket |
| Launch | Publicación estática activa, recursos y configuración no secreta | Credenciales, sesiones y datos externos |
| Salones AV | Páginas y recursos publicados | localStorage/estado del navegador |
| Control Red | Demo publicada de solo lectura | Inventarios/dispositivos externos; sin escaneo de red |
| Replicant Lab | Fuentes, 13 PDF revisados en Nexus, reconstrucción MkDocs | Git, builds, credenciales y datos externos |
| CryptoWallet producción | Estado nativo, bases, operaciones, catálogo y ajustes no secretos bajo bloqueos | Seguridad/PIN/OAuth/sesiones/cachés y fuentes externas no persistidas |
| Cartera Nexus | Base efectiva SQLite y evidencias Indexa | Base Windows, seguridad/PIN/OIDC/credenciales |
| Reserva Pistas | Tareas, sincronización y auditoría con bloqueos compartidos | Credenciales, SSH, Telegram, procesos; no ejecuta reservas |
| Facility | PostgreSQL y objetos/buckets MinIO de servicios detenidos | IAM, identidades, proveedores, credenciales/sesiones; cobertura parcial, reprovisión necesaria |

Previews excluidas de nuevas copias, horarios y retención, con historial conservado. Facility está en «Aplicaciones detenidas», cuenta en Copiar todas y puede configurar copias sin arrancar sus diez contenedores originales. Candidatas pendientes sin adaptador validado no son seleccionables, tienen causa y siguiente acción y conservan historial. Validar una candidata requiere su propio alcance autorizado y recorrido Drive.

Copiar una, seleccionadas o todas las aptas → autorizar en contexto si falta acceso → revisar incluidos/excluidos → cancelar o confirmar. El cierre v1.1.0 ejecutó los dos lotes reales descritos arriba; no ejecutó purgas. Los lotes comparten cola global de una ejecución y reserva/idempotencia en SQLite; cada aplicación tiene resultado independiente. El favicon caja fuerte, enlace Ver en Drive a la raíz configurada y menú móvil de cinco vistas reutilizan la identidad corporativa aprobada. Escape, foco y320px sin desbordamiento comprobados.

«Copias automáticas» significa programación ON/OFF y no arranca la aplicación. OFF conserva copia manual e historial. Configurar horario es accesible sin horario o en OFF; ON sin horario abre días/hora; Guardar y activar requiere autorización explícita y horario válido. Aptitud/cliente OAuth propio verificado son requisitos; el estado operativo detenido no bloquea el horario.

El11/10 se aplicó una sola vez la autorización inicial de las ocho diariamente05:00 Europe/Madrid, sustituyendo Launch03:00. El arranque/deploy/discovery no reaplica valores. Al cierre v1.1.1 hay seis ON05 y tres OFF05: Control Red, Facility y Salones conservan OFF con05 guardada; no se reactivan. Backups Lab propuso05 y solo se activó tras su validación completa. Reservas programadas app+instanteUTC únicas, incluidas aun con motor ocupado, cola pendiente durable tras restart y ejecución de una en una. Un cambio posterior cancela slots que ya no corresponden. Hora de primavera inexistente → primer minuto válido; hora repetida → primera ocurrencia. Recupera como máximo la última vencida en 24 horas, nunca anterior a activación. Próxima copia usa el mínimo real de las incluidas activas.

## Arquitectura y recuperación V1

Navegador React/Vite → Nginx → API FastAPI. SQLite persiste catálogo, horarios, reservas, eventos y diario de operaciones. Planificador reserva slots; trabajador global de una ejecución coordina copias, recuperación y retención. Captura consistente mediante adaptadores de archivos/SQLite/métodos nativos. Ayudante fijo en socket Unix con permisos 0600 valida UID y contratos; API no tiene socket Docker. rclone con cliente OAuth propio y raíz aprobada: subida inmutable → comprobación remota → descarga a directorio nuevo → manifiesto/conjunto/SHA256 iguales → lectores nativos/HTTP aislado. Solo esta evidencia permite aptitud; no se amplía por ocultar avisos.

Copias → Detalle → resultado de recuperación o Probar recuperación aislada cuando no esté ya verificada. Ensayo en directorio independiente: no sobrescribe producción, no reintegra secretos excluidos. El historial anterior de ocho recorridos Drive se reutiliza; las ocho últimas copias válidas observadas también tienen recuperación verificada. Evidencia y límites en [contratos](https://github.com/ratienza/backups-lab/blob/main/docs/operational-contracts.md), [matriz](https://github.com/ratienza/backups-lab/blob/main/docs/operational-matrix.md) y [recibo fechado](https://github.com/ratienza/backups-lab/blob/main/artifacts/v1-release/runtime-before.json). Repetir solo si cambia el contrato/método o la evidencia resulta insuficiente.

La sustitución de originales y rollback de aplicaciones fueron diferidos expresamente a v2.0 por Raúl el 11/10, no desplazados para ocultar un incumplimiento. En V1 no hay acciones operativas y API/ayudante rechazan preparación/confirmación/rollback (409). Código, 16 variantes de clones, diarios y snapshots se conservan. [Backlog V2.0](../pendientes/backups-drive.md) y [procedimiento futuro](https://github.com/ratienza/backups-lab/blob/main/docs/operational-lifecycle.md). El rollback de publicación de Backups Lab, descrito abajo, sí pertenece a V1.

## Retención e historial

Automática **ON en la observación de cierre**, independiente de horarios y sin que este encargo cambiara ese estado. Política editable guardada: 7 diarias / 4 semanales / 12 mensuales / 3 anuales por aplicación, unión sin duplicar IDs. Conserva siempre última válida aun OFF/antigua fuera de bandas, BL-002, referencias de aptitud y registros usados en restauración. Excluye previews, objetos ajenos, originales y copias nativas fuera de gestión. Guardar parámetros no limpia ni cambia ON/OFF. Aplicación manual exige acceso, casilla, hash del inventario e ID estable; revalida antes de borrar. En v1.1.0 no se aplicó retención ni se ejecutaron borrados de verificación.

- Fallo manual randomUUID: en HTTP sin contexto seguro la función no existía; falló antes delPOST y no reservó operación. Corregido con generador central getRandomValues, confirmación, useRef contra doble envío e ID estable tras error/respuesta perdida. Restauración/rollback tienen IDs de servidor.
- Automática retention-auto-20261011: 11/10/2026 20:20:01UTC =22:20:01Madrid, succeeded, eliminó dos antiguas de Cartera y Launch. Auditoría remota de solo lectura confirmó ausencia; no se atribuye identidad a los cambios ON/OFF/ON.
- Manual retention-91413a6646a6d87e72ad5a68130d5213:20:53:13UTC del 11/10, succeeded, cero eliminaciones.
- Manual retention-81a56f35ed64306375f4ba48dfbcc160: iniciada22:02:21UTC del 11/10 =00:02:21Madrid del 12/10, ya running al comenzar este cierre; terminó succeeded con ocho eliminaciones. No fue una prueba de este encargo ni se atribuye autoría sin evidencia. No ocultarla ni confundirla con las dos automáticas anteriores. Se pausó la automática al observar ON según la instrucción vigente; esa pausa no cancela una manual ya aceptada.

Historial durable completo, sin reintroducir copias ni borrar registros. Los contadores y nuevas operaciones normales pueden cambiar; consultar API/recibo fechado. El estado OFF citado en cierres anteriores es histórico; v1.1.0 encontró retención ON y la preservó, con cuatro operaciones históricas sin cambios durante la comprobación final.

## Despliegue, SHA y rollback

Release/tag v1.1.2; versiones anteriores históricas sin sobrescritura. VERSION, API/OpenAPI y paquete frontend 1.1.2. `/api/status` y labels OCI de API/web identifican el mismo SHA desplegado `69c2957a99137bfe48bb9e97859c1e161a243e1d`. CI de [#28](https://github.com/ratienza/backups-lab/actions/runs/38284107972) y [#29](https://github.com/ratienza/backups-lab/actions/runs/38284814489) verde. No hubo migración destructiva ni repetición de OAuth.

Antes de desplegar: snapshots SQLite consistentes con permisos 0600 privados, imágenes/API/web/documentación anteriores etiquetadas y script privado de rollback. Rollback rechaza trabajo en curso, restaura solo código/imágenes y documentación; conserva historial actual y elecciones posteriores de horarios. No restaura aplicaciones originales ni borra Drive. El snapshot de DB es protección separada, no se restaura automáticamente. Seguir el recibo de publicación; no ejecutar rollback como prueba sobre producción.

## Verificación y continuidad

CI aplicable v1.1.1: suite backend 103 correctas y 4 omitidas, build, siete recorridos del frontend, Compose, imágenes y etiquetas. La UI publicada cubre cinco vistas, claro/oscuro y 1440/390: 20 layouts sin errores ni desbordamiento. Compatibilidad HTTP sin randomUUID, confirmación/error/doble envío/ID, cola, persistencia/DST, protecciones, selección y orden siguen cubiertos. La comprobación de v1.1.1 ejecutó solo la primera copia necesaria de Backups Lab; las dos acciones manuales y ocho recuperaciones de v1.1.0 permanecen como evidencia reutilizada. Horarios, cuatro operaciones históricas de retención y ON/OFF quedaron preservados; ninguna clave aparece en evidencias.

Alcance v1.1.2 aceptado definitivamente, fusionado, desplegado y verificado. V2 solo backlog, sin implementación nueva. Informe diario por correo, log exportable, cifrado adicional, agentes externos, nuevos adaptadores y recuperación integral del host son propuestas anteriores pendientes de decisión/contrato, no se presentan como entregadas.

[Changelog v1.1.2](https://github.com/ratienza/backups-lab/blob/main/CHANGELOG.md) · [Recibo y capturas publicadas](https://github.com/ratienza/backups-lab/tree/main/artifacts/v1.1.2/published) · [Backlog canónico V2.0](https://github.com/ratienza/backups-lab/blob/main/BACKLOG_V2.md) · [HANDOFF](https://github.com/ratienza/backups-lab/blob/main/HANDOFF.md).
