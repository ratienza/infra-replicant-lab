# Aplicación · CryptoWallet

CryptoWallet **V1.0** fue aceptada por Raúl y promovida a producción privada el **08/10/2026**. Funcionalidad principal, estética y apertura financiera consolidada están cerradas. Nexus ejecuta esta producción; la previa conserva un entorno independiente.

## Accesos

- **Producción protegida:** [CryptoWallet](https://cryptowallet.thereplicantlab.com/).
- **Previa protegida:** [Revisión independiente](https://cryptowallet-preview.thereplicantlab.com/).
- **Pruebas de operaciones:** [Demo ficticia aislada de la previa](https://cryptowallet-preview.thereplicantlab.com/?datos=sinteticos).
- **Ficha técnica:** [HTML autocontenido](/downloads/apps/cryptowallet.html) · [PDF](/downloads/apps/cryptowallet.pdf).
- **Documentación funcional/técnica:** [Índice V1.0](https://github.com/ratienza/cryptowallet/tree/main/docs/v1), repositorio privado.
- **Código y release:** [ratienza/cryptowallet · v1.0.0](https://github.com/ratienza/cryptowallet/tree/v1.0.0).
- **App Launch:** tarjeta productiva existente en el catálogo Nexus. El catálogo no ejecuta la aplicación.

## Estado validado

| Campo | Estado |
|---|---|
| Producto | V1.0 aceptada; PR #3 fusionado por squash, sin revisión funcional pendiente |
| Código ejecutable | `5e7c3d79c0a6d66f8d6825be965de92d0420b196` |
| Tag funcional | `v1.0.0` en `2dd0eab5d820fa3ea98cd7054bc87885738c4e56`; documentación posterior no cambia ejecutable |
| Imagen productiva | `cryptowallet:1.0.0-5e7c3d79` |
| Runtime | Nexus · Docker Compose · contenedor `cryptowallet-app` |
| Origen productivo | `127.0.0.1:8516 → 8501`; sin acceso directo por IP LAN |
| Previa | `cryptowallet-preview-app` · `127.0.0.1:8517 → 8501`; datos independientes |
| Persistencia | SQLite y conjunto privado fuera de Git y del contenedor |
| Seguridad | Cloudflare Access/Tunnel, usuario no root, raíz de solo lectura y montaje real único |
| Recuperación | Copia consistente de aceptación verificada en Nexus y segunda ubicación privada |
| Pruebas de entrega | 339 superadas en local e imagen aceptada de Nexus; comparación financiera de solo lectura |
| Observación 08/10 | Ambos contenedores saludables; ambos hostnames redirigen a Access sin sesión |

No se publican bases, importes, lotes reales, originales, capturas, manifiestos financieros, credenciales ni ubicaciones privadas de respaldos en este repositorio público.

## Funcionalidades aceptadas

Dashboard, Cartera actual, Logbook, Tokens y Configuración mantienen temas, privacidad y USD/EUR. Dashboard distingue BTC, Altcoins, **Liquidez** y **Patrimonio**. Liquidez presenta **Total → Estables → FIAT**, identifica Stable Coin por marca del catálogo y conserva la valoración disponible sin asumir paridad.

Cartera conserva la tabla financiera, cobertura, lotes y procedencia; gráficos preceden a la tabla. Tokens añade composición por custodia y red. Cantidades aparecen en las ayudas del Dashboard respetando privacidad.

Compras, ventas, rotaciones, depósitos/retiradas fiat y traslados propios **contabilizan al confirmar**. Guardar borrador no mueve saldo/FIFO. Formularios compactos con grupos, cálculos editables, porcentajes de venta por custodia y rotación con precio/cantidad destino recíprocos. Revisar operación muestra bruto/neto, comisiones, referencias, saldos y efectos FIFO.

P&G comparable usa coste y valor de las mismas unidades. xN conserva esa cobertura. P&G realizado se distingue del principal retirado en fiat. Valoración EUR de pantalla no constituye base fiscal histórica.

## Arquitectura y acceso

Python/Streamlit consume la apertura aceptada, catálogo y confirmaciones nuevas. El motor Decimal valida disponibilidad física por custodia y FIFO global del titular por activo. La apertura permanece inmutable; nuevas confirmaciones transaccionales e idempotentes conservan cadena de huellas y revisión.

La ruta externa pasa por Cloudflare Access y el Tunnel saliente de Nexus. Los orígenes productivo y previo están ligados a localhost. El modo de privacidad es visual; V1.0 no añade OAuth/PIN internos como los de Cartera Estratégica.

Producción monta únicamente el conjunto real. La demo sintética se monta solo en la previa; no sigue ni se mezcla con producción. La copia real de la previa tampoco se sincroniza con las confirmaciones productivas posteriores.

## Datos y protección

Originales importados y operaciones contabilizadas están protegidos sin edición/borrado. Los borradores manuales pueden editarse o retirarse de forma recuperable. La primera confirmación real crea la base financiera nueva si aún no existe: una ausencia inicial no se subsana inventando operaciones.

Costes e ingresos desconocidos mantienen cobertura explícita. CW-004 permanece cerrado, el regalo PEPE sigue excluido y los límites históricos aceptados de TAO no se rellenan con cero ni nuevos supuestos.

## Operación segura y rollback

Antes de un cambio funcional, identificar imagen/esquema y conjunto vivo, detener escrituras para obtener un corte coherente, usar backup SQLite consistente y preservar catálogo, apertura, permiso, borradores y decisiones. Verificar integridad, huellas y restauración aislada; no basta copiar un archivo activo ignorando WAL.

Después del cambio, comprobar imagen aprobada, mismo montaje real, bind localhost, salud Streamlit, cadena y comparación financiera. El procedimiento completo vive en el repositorio privado. La publicación documental recrea únicamente el sitio de Replicant Lab; no reinicia CryptoWallet.

**Rollback de código y recuperación de datos son decisiones distintas.** Tras nuevas confirmaciones reales, la versión antigua sin motor no es compatible: conservar conjunto vivo y usar imagen de esquema 1 compatible o reparación hacia delante. No restaurar la apertura perdiendo movimientos posteriores. La copia de aceptación es puntual, no un backup automático; la previa no es una réplica de recuperación.

## Pendientes y límites

[Importación funcional CSV/Excel y reconciliación nueva](../pendientes/cryptowallet.md) quedan para **V2**. V1.0 permite consultar trazabilidad, pero no importar nuevos archivos desde la pantalla. OAuth/PIN internos, respaldo funcional y preventas están aplazados.

No hay bridge/cambio de red, edición/reversión de contabilizadas ni inserción anterior a apertura/última confirmación. No se declara conformidad fiscal nueva. Estos límites no reabren la aceptación V1.0.

La revisión documental confirma runtime y redirección Access, no el contenido actual de todas las políticas del panel Cloudflare ni una nueva prueba autenticada móvil. [Cloudflare](../red/cloudflare-tunnel.md) distingue la evidencia histórica, la observación actual y esos controles pendientes.
