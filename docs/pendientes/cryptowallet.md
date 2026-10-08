# Pendientes · CryptoWallet

**V1.0 aceptada, integrada y en producción privada desde el 08/10/2026.** Funcionalidad principal, estética y apertura consolidada cerradas. Ninguna nota de revisión anterior mantiene abierto CW-005 ni reabre CW-004.

| Tema | Estado | Próximo alcance, si Raúl lo encarga |
|---|---|---|
| Importar CSV/Excel | Pendiente V2 | Flujo funcional con análisis, mapeo, errores legibles, revisión e idempotencia |
| Reconciliación nueva | Pendiente V2 | Nuevas fuentes sin duplicar apertura ni modificar cierres aceptados |
| OAuth/PIN internos | Aplazado | Diseño específico; Access externo permanece vigente |
| Respaldo desde la app | Aplazado | Consistencia multibase, retención y restauración comprobada |
| Preventas / ampliaciones Configuración | Aplazado | Encargo separado |
| Corrección/reversión de contabilizadas | Limitación V1.0 | Sin implementación autorizada |
| Bridge/cambio de red y retroactividad | No habilitados | Sin simulación ni reescritura histórica |
| Backups automáticos/alertas | Pendiente operativo | La copia puntual V1.0 no constituye automatización |

No siguen pendientes los depósitos/retiradas fiat, contabilización, ajustes estéticos, cálculos recíprocos de rotación ni Liquidez Total/Estables/FIAT: ya fueron entregados y aceptados.

Los desconocidos históricos permanecen no disponibles, nunca cero. El regalo PEPE sigue excluido y no se solicitan históricos para TAO. USD/EUR de pantalla no constituye una base fiscal histórica.

## Operación del Lab

- Mantener producción y previa independientes; practicar movimientos exclusivamente con la demo ficticia de la previa.
- Validación administrativa y móvil de Access por hostname, monitorización y recuperación del Tunnel: controles transversales, no nuevas funciones de CryptoWallet.
- La tarjeta Nexus ya abre producción. Su descripción aún menciona borradores y no incluye enlace secundario a la ficha: actualización de metadatos del catálogo mediante el flujo de App Launch, sin cambiar el runtime financiero.
- Datos y respaldos exclusivamente privados. La ficha pública documenta la infraestructura, no la cartera.

[Ficha vigente](../aplicaciones/cryptowallet.md) · [Documentación funcional privada](https://github.com/ratienza/cryptowallet/tree/main/docs/v1).

## Mejora posterior a V1.0 · anotada 08/10/2026

Raúl solicita que los resúmenes de operaciones se presenten en una **pantalla de revisión separada**, siguiendo Cartera Estratégica, con más contexto y comparación **antes → variación → después**. Incluir activos/custodias, cantidades/importes, comisiones y efectos P&G/FIFO cuando correspondan, con cobertura explícita y acciones de volver/modificar y confirmar accesibles.

**Solo pendiente; no implementar todavía.** La captura es una referencia privada de presentación y sus cifras no se publican. Es mejora posterior, sin reabrir la aceptación V1.0 ni modificar el motor actual.
