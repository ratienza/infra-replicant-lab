# Aplicación · CryptoWallet

CryptoWallet **V1.6.11 / 1.6.11** está cerrada y desplegada en producción privada Nexus desde el **17/10/2026**. Conserva la apertura financiera aceptada y los cierres anteriores. Una regularización valida saldo previo, delta y objetivo al confirmar; en replay aplica el delta aceptado y conserva saldo previo/objetivo como evidencia, sin reinterpretarlos como el saldo corriente. La previa conserva un entorno independiente; no se presume actualizada a V1.6.11.

La evidencia operativa procede del [HANDOFF privado](https://github.com/ratienza/cryptowallet/blob/main/HANDOFF.md) y de la [release V1.6.11](https://github.com/ratienza/cryptowallet/blob/v1.6.11/docs/releases/v1.6.md). La activación de Google y el recorrido Google → PIN → cartera siguen atribuidos a la confirmación manual de Raúl en incógnito el 09/10/2026. En este cierre el origen productivo, la identidad de imagen y la puerta Access se comprobaron. El flujo completo se confirmó en dos copias restauradas e independientes del estado productivo; producción no se montó en esos contenedores y la compra real continúa pendiente.

## Accesos

- **Producción protegida:** [CryptoWallet](https://cryptowallet.thereplicantlab.com/).
- **Previa protegida:** [Revisión independiente](https://cryptowallet-preview.thereplicantlab.com/).
- **Pruebas de operaciones:** [Demo ficticia aislada de la previa](https://cryptowallet-preview.thereplicantlab.com/?datos=sinteticos).
- **Ficha técnica:** [HTML autocontenido](/downloads/apps/cryptowallet.html) · [PDF](/downloads/apps/cryptowallet.pdf).
- **Documentación funcional/técnica:** [Manual vigente V1.6.11](https://github.com/ratienza/cryptowallet/tree/main/docs/v1), repositorio privado.
- **Código y release:** [ratienza/cryptowallet · v1.6.11](https://github.com/ratienza/cryptowallet/tree/v1.6.11).
- **App Launch:** tarjeta productiva existente en el catálogo Nexus. El catálogo no ejecuta la aplicación.

## Estado validado

| Campo | Estado |
|---|---|
| Producto | V1.6.11 cerrada; PR #44 funcional y PR #45 documental fusionados |
| Código ejecutable / tag | `45d83c7ffc7d6267df0f8926968826de948b4b94` · `v1.6.11` |
| Main documental del producto | Documentación de cierre posterior; no desplaza el tag funcional |
| Imagen productiva | `cryptowallet:1.6.11-45d83c7ffc7d` |
| ID de imagen | `sha256:ff9ae36f5ad5507dfa59be8b574c94d17e15b6ae856d555cbd6ffb4d0585fa8c` |
| Runtime | Nexus · Docker Compose · `cryptowallet-app` · usuario `1000:1000` |
| Origen productivo | `127.0.0.1:8516 → 8501`; sin acceso directo por IP LAN |
| Previa | `cryptowallet-preview-app` · localhost `8517`; almacenamiento y versión independientes |
| Persistencia | Conjunto financiero, copias y seguridad en montajes privados separados |
| Seguridad efectiva | Cloudflare Access/Tunnel + Google interno activo + PIN activo; 24 horas; privacidad inicial ON |
| Recuperación | Copias multibase verificadas; seguridad respaldada aparte; restauración probada en aislamiento |
| Pruebas de entrega | 430 pruebas localmente y 430 dentro de la imagen final sin red; dos copias restauradas, compra retroactiva exacta, borrador recuperado y reintentos sin duplicado |
| Evidencia de promoción 17/10 | Healthy, versión/SHA/imagen correctos; copia protegida de 35 componentes y 5 operaciones, con estado idéntico antes/después; regularización y borrador reales intactos |
| Aceptación exterior | Respuesta anónima 302 de Access; Google → PIN → cartera sigue siendo la confirmación manual previa de Raúl, no una nueva aceptación humana |
| Cobertura no verificada | Cuenta no autorizada, cancelación/error OIDC y recorrido móvil exterior; límite aceptado sin bloquear el cierre |

No se publican bases, importes, lotes reales, originales, capturas, manifiestos financieros, credenciales ni ubicaciones privadas de respaldos en este repositorio público.

## Funcionalidades aceptadas

Dashboard, Cartera actual, Logbook y Tokens mantienen temas, privacidad y USD/EUR. **Ajustes** agrupa tres pestañas: **Generales** (tema, frescura de cotizaciones, tokens y preferencias existentes), **Seguridad** y **Backup**. En móvil la hamburguesa arranca cerrada, indica la sección activa y se cierra al navegar; en escritorio se conserva el menú horizontal. Revisión sintética en claro/oscuro, escritorio y móvil 390 × 844, sin desbordamiento horizontal. Dashboard distingue BTC, Altcoins, **Liquidez** y **Patrimonio**. Liquidez presenta **Total → Estables → FIAT**, identifica Stable Coin por marca del catálogo y conserva la valoración disponible sin asumir paridad.

Las valoraciones muestran su peso sobre el mismo patrimonio total completo que aparece en la aplicación. En las fichas, `Peso` ocupa una fila completa con el mismo formato que `Invertido` y `Valor actual`; Liquidez presenta filas completas separadas para Estables/FIAT y sus pesos. P&G muestra rentabilidad sobre coste con signo y color financiero; `Invertido FIFO` no presenta peso. El gráfico de distribución conserva colores y disposición con porcentajes visibles en las etiquetas; `Peso por red` y `Activos por red` permanecen en el Dashboard. Si el total completo es cero o no está disponible, no se publica un porcentaje derivado de un subtotal. La cabecera identifica `Mi cartera crypto · v1.6.11`; Dashboard y Cartera ordenan Patrimonio, BTC, Altcoins y Liquidez.

La revisión de operaciones conserva el último campo editado en Precio–Cantidad–Importe. En Compra se puede elegir `Precio y cantidad` o `Total pagado y cantidad neta`: en el segundo modo, Activo, total, moneda, cantidad neta y origen comparten una línea de escritorio y el coste unitario efectivo se calcula en el servidor. El justificante puede conservar precio mostrado y spread como datos informativos, sin sustituir los hechos autoritativos. Las comisiones distinguen importe incluido del total y cargo adicional, incluso en otra moneda, evitando doble contabilización. Tarjeta/Otros no descuentan principal interno; Liquidez sí. USDC adquirido se incorpora a Liquidez.

Los hechos de compra, el FX documentado y la valoración histórica se muestran por separado. No se deriva un EUR/USD ausente ni se equipara USDC con USD. Si falta una conversión imprescindible, la operación queda como borrador recuperable fuera de contabilidad, saldos, FIFO y P&G. Al volver o recuperarlo, el bloque visible restaura referencia, fecha, fuente, total y cantidad. La consulta BCE selecciona la publicación exacta o la última anterior, nunca una posterior; la entrada manual sigue disponible. Un hecho real ya truncado no se amplía con precisión inventada. En móvil, el formulario se apila sin desbordamiento.

Cartera conserva la tabla financiera, cobertura, lotes y procedencia; gráficos preceden a la tabla. Tokens añade composición por custodia y red. Cantidades aparecen en las ayudas del Dashboard respetando privacidad.

Compras, ventas, rotaciones, depósitos/retiradas fiat y traslados propios **contabilizan al confirmar**. Guardar borrador no mueve saldo/FIFO. En compras, **Tarjeta** y **Otros** no descuentan principal de liquidez; **Liquidez** sí exige y descuenta el saldo interno. La comisión declara por separado si es **Externa** o sale de **Cartera**. BTC parte de Tarjeta y el resto de Otros. Alta, borradores anteriores y correcciones contabilizadas reproducen la misma historia efectiva y usan exactamente tres bloques: datos, pago/origen/comisiones y resultado/confirmación; no muestran proyecciones futuras. Si una corrección vuelve incoherente una operación posterior, se rechaza sin escribir.

P&G comparable usa coste y valor de las mismas unidades. xN conserva esa cobertura. P&G realizado se distingue del principal retirado en fiat. Valoración EUR de pantalla no constituye base fiscal histórica.

## Arquitectura y acceso

Python/Streamlit consume la apertura aceptada, catálogo y confirmaciones nuevas. El motor Decimal valida disponibilidad física por custodia y FIFO global del titular por activo. La apertura y `finance.sqlite3` permanecen inmutables; `purchase-payment.sqlite3` conserva origen visible y efecto histórico real, mientras `operation-changes.sqlite3` registra revisiones y tombstones append-only con CAS e identificadores idempotentes. El motor ordena por fecha de ejecución —con la revisión inmutable como desempate— y reproduce la historia efectiva sin duplicar ni reescribir confirmaciones.

Las regularizaciones positivas conservan en la cadena el saldo previo, delta y objetivo aceptados. La confirmación valida esa igualdad bajo bloqueo y transacción. Las reproducciones posteriores validan la coherencia interna de la evidencia y aplican el delta fijo al saldo vigente; nunca recalculan el ajuste para absorber una operación retroactiva.

La ruta externa pasa por Cloudflare Access y el Tunnel saliente de Nexus. Los orígenes productivo y previo están ligados a localhost. Cloudflare Access es la barrera exterior; Google OIDC interno y el PIN son capas propias de la aplicación. El cliente Web OAuth dedicado y sus credenciales privadas quedaron instalados y Google interno está activo. La privacidad oculta cifras; no sustituye al control de acceso.

Producción monta únicamente el conjunto real. La demo sintética se monta solo en la previa; no sigue ni se mezcla con producción. La copia real de la previa tampoco se sincroniza con las confirmaciones productivas posteriores.

## Datos y protección

Originales importados permanecen protegidos. Las seis clases manuales contabilizadas pueden corregirse o eliminarse de forma reversible sin reescribir su confirmación original: la vista efectiva procede de eventos auditables y el borrado es un tombstone. Los borradores manuales pueden editarse o retirarse de forma recuperable. La compra USDC real de este encargo conserva sus hechos guardados y sigue pendiente; solo se recuperó y confirmó en una copia aislada.

Costes e ingresos desconocidos mantienen cobertura explícita. CW-004 permanece cerrado, el regalo PEPE sigue excluido y los límites históricos aceptados de TAO no se rellenan con cero ni nuevos supuestos.

## Seguridad y privacidad V1.6.11

PIN ASCII de seis cifras, conservado como hash scrypt con sal. El desbloqueo firmado queda ligado a identidad y revisión, con caducidad absoluta de **24 horas** por defecto; persiste tras recarga, reapertura y reinicio. El servidor conserva intentos, bloqueo y revocaciones: **5 intentos / 30 segundos** por defecto. El PIN muestra cuenta atrás y reactiva las casillas automáticamente, con validación del servidor en cada envío.

**Bloquear ahora**, cierre de sesión, caducidad y cambios de seguridad invalidan el desbloqueo correspondiente. La privacidad inicial **ON** se aplica antes del primer render financiero y se repone al volver a acceder; el ojo funciona normalmente durante la sesión. Los parámetros son modificables en Seguridad; credenciales y ajustes técnicos quedan en Configuración avanzada, plegada por defecto. Secretos, PIN y sesiones no se versionan.

El alta del cliente Web OAuth, callbacks, credenciales privadas, activación y recorrido autorizado Google → PIN → cartera ya no son pendientes. Conservar secretos fuera de Git y no reutilizar los de Cartera. Cuenta no autorizada, cancelación/error OIDC y recorrido móvil exterior no constan probados; se registran como cobertura no verificada aceptada. [Procedimiento privado](https://github.com/ratienza/cryptowallet/blob/main/docs/v1/operacion.md).

## Copias locales y restauración V1.6.11

**Ajustes → Backup** permite crear, inspeccionar, proteger, descargar y restaurar copias del conjunto completo. Cada `.cwbak.zip` incluye manifiesto, versiones, entorno, componentes, tamaños, SHA-256, esquemas, integridad SQLite y cadena de confirmaciones. Incluye apertura, catálogo, bases financieras presentes, borradores/revisiones, decisiones, fuentes y configuración funcional. Las SQLite usan su API de backup bajo el bloqueo coordinado compartido con las escrituras; no se copian WAL/SHM en bruto.

| Tipo | Comportamiento | Retención efectiva |
|---|---|---|
| Manual | Solicitada desde Backup | 10 |
| Diaria | Solo si cambia el estado; una por fecha, sin duplicarse al recargar | 7 |
| Previa | Verificada antes de confirmaciones, restauración e integración/migración | 10 |
| Protegida | Conservación explícita; fuera de caducidad ordinaria | Se conserva |

Consultar, previsualizar o cancelar no crea copias. Si falla una previa, se bloquea la escritura; un fallo diario posterior no convierte una operación ya confirmada en una invitación a repetirla. Nunca se elimina la única recuperación válida. Las copias locales no acreditan todavía una réplica automática remota en Drive.

Restaurar exige validar compatibilidad, huellas, integridad y cadena, revisar las operaciones posteriores que se perderían y confirmar; hay confirmación adicional ante copia vacía. Se crea `pre_restore`, se prepara el candidato bajo el montaje vivo escribible y se instala el conjunto completo con escrituras bloqueadas. Un fallo previo informa que no modificó el conjunto; un fallo parcial recupera y verifica el conjunto anterior. Éxito, fallo previo y recuperación parcial se probaron **solo en aislamiento**, con raíz de solo lectura y montajes separados, nunca sobre producción.

Seguridad se respalda separadamente: credenciales, PIN, estado y secretos no aparecen en descargas financieras. Restaurar finanzas preserva la seguridad actual y no revive sesiones revocadas. Antes de V1.6.11 se protegió una copia de 35 componentes y 5 operaciones; su huella coincidió con producción después de promover. Referencias privadas de recuperación en el manual del producto, sin publicar rutas ni manifiestos financieros aquí.

## Operación segura y rollback

Antes de un cambio funcional, identificar imagen/esquema y conjunto vivo, detener escrituras para obtener un corte coherente, usar backup SQLite consistente y preservar catálogo, apertura, permiso, borradores y decisiones. Verificar integridad, huellas y restauración aislada; no basta copiar un archivo activo ignorando WAL.

Después del cambio, comprobar imagen aprobada, mismo montaje real, bind localhost, salud Streamlit, cadena y comparación financiera. El procedimiento completo vive en el repositorio privado. La publicación documental recrea únicamente el sitio de Replicant Lab; no reinicia CryptoWallet.

**Rollback de código y recuperación de datos son decisiones distintas.** Tras nuevas confirmaciones reales, conservar el conjunto vivo y usar una imagen de esquema 1 compatible o reparación hacia delante. No restaurar la apertura perdiendo movimientos posteriores. V1.6.11 mantiene formato y modelo de copia 1; la imagen V1.6.10 y la composición anterior se conservan como rollback de código, no como autorización para sustituir datos. La copia puntual de aceptación V1.0 queda como evidencia histórica. La previa no es una réplica de recuperación. La recuperación de seguridad es una intervención privada separada.

## Pendientes y límites

[Importación funcional CSV/Excel y reconciliación nueva](../pendientes/cryptowallet.md) quedan para **V2**. V1.6.11 conserva la trazabilidad, edición y eliminación reversible, pero no importa nuevos archivos desde la pantalla. PIN, respaldo funcional y Google interno ya están activos. Las variantes OIDC no probadas son límites aceptados, no funciones pendientes; preventas y otras ampliaciones siguen separadas.

No hay bridge/cambio de red ni inserción anterior a la apertura aceptada. Las operaciones manuales anteriores a la última confirmación sí pueden prepararse o corregirse, pero solo si la reproducción completa mantiene saldos, custodia y FIFO coherentes. Una regularización confirmada aporta su delta fijo; no se recalcula para forzar esa coherencia. La identidad corporativa queda cerrada con el bitmap y la composición oficial ya aprobados; no autoriza nuevas variantes. No se declara conformidad fiscal nueva. Estos límites no reabren la aceptación financiera V1.0 ni los cierres anteriores.

La evidencia de promoción del producto registra runtime, salud y sesión autenticada con privacidad activa. No certifica el contenido actual de todas las políticas Cloudflare ni una prueba autenticada móvil. [Cloudflare](../red/cloudflare-tunnel.md) distingue la evidencia histórica y los controles pendientes.

## Revisión de vigencia · 31/10/2026

Se conserva **V1.6.11**. [HANDOFF](https://github.com/ratienza/cryptowallet/blob/main/HANDOFF.md) acredita identidad TRL publicada el 30/10, PR #46, funcional `9cf8f17`, cierre `3162835`, 430 pruebas registradas y preservación de módulos financieros/seguridad. Son evidencias del repositorio, no una batería repetida hoy.
