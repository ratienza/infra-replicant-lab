# Aplicación · CryptoWallet

CryptoWallet **V1.5 / 1.5.0** está cerrada y desplegada en producción privada Nexus desde el **09/10/2026**. Conserva la apertura financiera aceptada y añade PIN persistente, privacidad inicial, copias multibase y navegación adaptable. La previa conserva un entorno independiente; no se presume actualizada a V1.5.

La evidencia operativa procede del [HANDOFF privado](https://github.com/ratienza/cryptowallet/blob/17489d38ab5398de80c37d4985b15f23f131874f/HANDOFF.md) y de la [aceptación CW-V15](https://github.com/ratienza/cryptowallet/blob/17489d38ab5398de80c37d4985b15f23f131874f/docs/evidence/CW-V15/acceptance.md). Este cierre documental contrasta esas fuentes; no constituye una nueva inspección del runtime de Nexus.

## Accesos

- **Producción protegida:** [CryptoWallet](https://cryptowallet.thereplicantlab.com/).
- **Previa protegida:** [Revisión independiente](https://cryptowallet-preview.thereplicantlab.com/).
- **Pruebas de operaciones:** [Demo ficticia aislada de la previa](https://cryptowallet-preview.thereplicantlab.com/?datos=sinteticos).
- **Ficha técnica:** [HTML autocontenido](/downloads/apps/cryptowallet.html) · [PDF](/downloads/apps/cryptowallet.pdf).
- **Documentación funcional/técnica:** [Manual vigente V1.5](https://github.com/ratienza/cryptowallet/tree/main/docs/v1), repositorio privado.
- **Código y release:** [ratienza/cryptowallet · v1.5.0](https://github.com/ratienza/cryptowallet/tree/v1.5.0).
- **App Launch:** tarjeta productiva existente en el catálogo Nexus. El catálogo no ejecuta la aplicación.

## Estado validado

| Campo | Estado |
|---|---|
| Producto | V1.5 cerrada; PR #13–#17 fusionados |
| Código ejecutable / tag | `d7aac669b5f905933558c3a7ffa7b42cdae9741e` · `v1.5.0` |
| Main documental del producto | `17489d38ab5398de80c37d4985b15f23f131874f`; distinto del ejecutable |
| Imagen productiva | `cryptowallet:1.5.0-d7aac669b5f9` |
| ID de imagen | `sha256:d764f7f40619b6229e4b1db8bd7db7c04863598babe00b982b47dc9ce9d2cdc5` |
| Runtime | Nexus · Docker Compose · `cryptowallet-app` · usuario `1000:1000` |
| Origen productivo | `127.0.0.1:8516 → 8501`; sin acceso directo por IP LAN |
| Previa | `cryptowallet-preview-app` · localhost `8517`; almacenamiento y versión independientes |
| Persistencia | Conjunto financiero, copias y seguridad en montajes privados separados |
| Seguridad efectiva | Cloudflare Access/Tunnel + PIN activo; 24 horas; privacidad inicial ON; Google interno OFF |
| Recuperación | Copias multibase verificadas; seguridad respaldada aparte; restauración probada en aislamiento |
| Pruebas de entrega | 379 pruebas + 68 subpruebas locales; 379 pruebas dentro de la imagen sin red |
| Evidencia de promoción 09/10 | Healthy, origen privado OK, Tunnel activo; 27 componentes financieros idénticos antes/después |
| Límite exterior | HTTP 302 sin sesión acredita Access; recorrido autenticado de Raúl pendiente |

No se publican bases, importes, lotes reales, originales, capturas, manifiestos financieros, credenciales ni ubicaciones privadas de respaldos en este repositorio público.

## Funcionalidades aceptadas

Dashboard, Cartera actual, Logbook y Tokens mantienen temas, privacidad y USD/EUR. **Ajustes** agrupa tres pestañas: **Generales** (tema, frescura de cotizaciones, tokens y preferencias existentes), **Seguridad** y **Backup**. En móvil la hamburguesa arranca cerrada, indica la sección activa y se cierra al navegar; en escritorio se conserva el menú horizontal. Revisión sintética en claro/oscuro, escritorio y móvil 390 × 844, sin desbordamiento horizontal. Dashboard distingue BTC, Altcoins, **Liquidez** y **Patrimonio**. Liquidez presenta **Total → Estables → FIAT**, identifica Stable Coin por marca del catálogo y conserva la valoración disponible sin asumir paridad.

Cartera conserva la tabla financiera, cobertura, lotes y procedencia; gráficos preceden a la tabla. Tokens añade composición por custodia y red. Cantidades aparecen en las ayudas del Dashboard respetando privacidad.

Compras, ventas, rotaciones, depósitos/retiradas fiat y traslados propios **contabilizan al confirmar**. Guardar borrador no mueve saldo/FIFO. Formularios compactos con grupos, cálculos editables, porcentajes de venta por custodia y rotación con precio/cantidad destino recíprocos. Revisar operación muestra bruto/neto, comisiones, referencias, saldos y efectos FIFO.

P&G comparable usa coste y valor de las mismas unidades. xN conserva esa cobertura. P&G realizado se distingue del principal retirado en fiat. Valoración EUR de pantalla no constituye base fiscal histórica.

## Arquitectura y acceso

Python/Streamlit consume la apertura aceptada, catálogo y confirmaciones nuevas. El motor Decimal valida disponibilidad física por custodia y FIFO global del titular por activo. La apertura permanece inmutable; nuevas confirmaciones transaccionales e idempotentes conservan cadena de huellas y revisión.

La ruta externa pasa por Cloudflare Access y el Tunnel saliente de Nexus. Los orígenes productivo y previo están ligados a localhost. Cloudflare Access es la barrera exterior; el PIN de la aplicación es una capa independiente. Google OIDC interno está implementado con correo verificado y cuentas autorizadas, pero permanece **desactivado** hasta instalar y probar un cliente OAuth dedicado. La privacidad oculta cifras; no sustituye al control de acceso.

Producción monta únicamente el conjunto real. La demo sintética se monta solo en la previa; no sigue ni se mezcla con producción. La copia real de la previa tampoco se sincroniza con las confirmaciones productivas posteriores.

## Datos y protección

Originales importados y operaciones contabilizadas están protegidos sin edición/borrado. Los borradores manuales pueden editarse o retirarse de forma recuperable. La primera confirmación real crea la base financiera nueva si aún no existe: una ausencia inicial no se subsana inventando operaciones.

Costes e ingresos desconocidos mantienen cobertura explícita. CW-004 permanece cerrado, el regalo PEPE sigue excluido y los límites históricos aceptados de TAO no se rellenan con cero ni nuevos supuestos.

## Seguridad y privacidad V1.5

PIN ASCII de seis cifras, conservado como hash scrypt con sal. El desbloqueo firmado queda ligado a identidad y revisión, con caducidad absoluta de **24 horas** por defecto; persiste tras recarga, reapertura y reinicio. El servidor conserva intentos, bloqueo y revocaciones: **5 intentos / 30 segundos** por defecto. El PIN muestra cuenta atrás y reactiva las casillas automáticamente, con validación del servidor en cada envío.

**Bloquear ahora**, cierre de sesión, caducidad y cambios de seguridad invalidan el desbloqueo correspondiente. La privacidad inicial **ON** se aplica antes del primer render financiero y se repone al volver a acceder; el ojo funciona normalmente durante la sesión. Los parámetros son modificables en Seguridad; credenciales y ajustes técnicos quedan en Configuración avanzada, plegada por defecto. Secretos, PIN y sesiones no se versionan.

Para completar Google: cliente Web OAuth exclusivo de CryptoWallet, callbacks local y productivo registrados, credenciales por canal privado, carga del TOML en Streamlit y reinicio controlado. Después comprobar Google → PIN, cuenta no autorizada, cancelación/error y recorrido exterior sin bucles. No reutilizar secretos ni almacenamiento de Cartera. [Procedimiento privado](https://github.com/ratienza/cryptowallet/blob/main/docs/v1/operacion.md).

## Copias locales y restauración V1.5

**Ajustes → Backup** permite crear, inspeccionar, proteger, descargar y restaurar copias del conjunto completo. Cada `.cwbak.zip` incluye manifiesto, versiones, entorno, componentes, tamaños, SHA-256, esquemas, integridad SQLite y cadena de confirmaciones. Incluye apertura, catálogo, bases financieras presentes, borradores/revisiones, decisiones, fuentes y configuración funcional. Las SQLite usan su API de backup bajo el bloqueo coordinado compartido con las escrituras; no se copian WAL/SHM en bruto.

| Tipo | Comportamiento | Retención efectiva |
|---|---|---|
| Manual | Solicitada desde Backup | 10 |
| Diaria | Solo si cambia el estado; una por fecha, sin duplicarse al recargar | 7 |
| Previa | Verificada antes de confirmaciones, restauración e integración/migración | 10 |
| Protegida | Conservación explícita; fuera de caducidad ordinaria | Se conserva |

Consultar, previsualizar o cancelar no crea copias. Si falla una previa, se bloquea la escritura; un fallo diario posterior no convierte una operación ya confirmada en una invitación a repetirla. Nunca se elimina la única recuperación válida. Las copias locales no acreditan todavía una réplica automática remota en Drive.

Restaurar exige validar compatibilidad, huellas, integridad y cadena, revisar las operaciones posteriores que se perderían y confirmar; hay confirmación adicional ante copia vacía. Se crea `pre_restore`, se prepara el candidato aislado y se instala el conjunto completo con escrituras bloqueadas. Un fallo parcial recupera y verifica el conjunto anterior. La restauración completa se probó **solo en aislamiento**, nunca sobre producción.

Seguridad se respalda separadamente: credenciales, PIN, estado y secretos no aparecen en descargas financieras. Restaurar finanzas preserva la seguridad actual y no revive sesiones revocadas. Antes de V1.5 se verificó una copia protegida y el estado financiero permaneció idéntico antes/después. Referencias privadas de recuperación en el manual del producto, sin publicar rutas ni manifiestos financieros aquí.

## Operación segura y rollback

Antes de un cambio funcional, identificar imagen/esquema y conjunto vivo, detener escrituras para obtener un corte coherente, usar backup SQLite consistente y preservar catálogo, apertura, permiso, borradores y decisiones. Verificar integridad, huellas y restauración aislada; no basta copiar un archivo activo ignorando WAL.

Después del cambio, comprobar imagen aprobada, mismo montaje real, bind localhost, salud Streamlit, cadena y comparación financiera. El procedimiento completo vive en el repositorio privado. La publicación documental recrea únicamente el sitio de Replicant Lab; no reinicia CryptoWallet.

**Rollback de código y recuperación de datos son decisiones distintas.** Tras nuevas confirmaciones reales, la versión antigua sin motor no es compatible: conservar conjunto vivo y usar imagen de esquema 1 compatible o reparación hacia delante. No restaurar la apertura perdiendo movimientos posteriores. V1.5 añade las copias locales descritas arriba; la copia puntual de aceptación V1.0 queda como evidencia histórica. La previa no es una réplica de recuperación. La recuperación de seguridad es una intervención privada separada.

## Pendientes y límites

[Importación funcional CSV/Excel y reconciliación nueva](../pendientes/cryptowallet.md) quedan para **V2**. V1.5 permite consultar trazabilidad, pero no importar nuevos archivos desde la pantalla. PIN y respaldo funcional ya están desplegados. Google interno está preparado pero pendiente de activación y verificación; preventas y otras ampliaciones siguen separadas.

No hay bridge/cambio de red, edición/reversión de contabilizadas ni inserción anterior a apertura/última confirmación. No se declara conformidad fiscal nueva. Estos límites no reabren la aceptación financiera V1.0 ni el cierre de V1.5.

La evidencia de promoción del producto registra runtime y redirección Access. Esta actualización consulta esa evidencia versionada; no certifica una nueva inspección de Nexus, el contenido actual de todas las políticas Cloudflare ni una prueba autenticada móvil. [Cloudflare](../red/cloudflare-tunnel.md) distingue la evidencia histórica y los controles pendientes.
