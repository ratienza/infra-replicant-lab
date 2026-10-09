# Pendientes · CryptoWallet

**V1.5 cerrada y desplegada el 09/10/2026.** PIN, privacidad inicial, copias multibase, pestañas de Ajustes y hamburguesa móvil están entregados. La apertura financiera V1.0 sigue aceptada; CW-004 y CW-005 no se reabren.

## Controles operativos reales

| Tema | Estado | Acción siguiente |
|---|---|---|
| Google OIDC interno | Implementado, OFF en producción | Crear/completar cliente Web OAuth dedicado, registrar callbacks y cargar credenciales por canal privado; reiniciar y comprobar readiness antes de activar |
| Pruebas OIDC reales | Pendientes | Google → PIN, autorizado/no autorizado, cancelación/error e ida/vuelta a través de Access |
| Exterior autenticado | Pendiente de sesión de Raúl | Repetir recorrido completo Access → aplicación → PIN en escritorio/móvil; el 302 no prueba el interior |
| Access/Tunnel transversales | Pendientes operativos del Lab | Revisión administrativa por hostname, monitorización, alertas y recuperación controlada |
| Metadatos de tarjeta App Launch | Ajuste independiente | Revisar descripción vigente y enlace a ficha, sin cambiar runtime financiero |

PIN ya configurado: no solicitar uno nuevo para documentar ni activarlo de nuevo. Duración efectiva 24 horas, privacidad inicial ON y Google interno OFF. No compartir secretos por chat o Git. [Alta y recuperación privadas](https://github.com/ratienza/cryptowallet/blob/main/docs/v1/operacion.md).

## Desarrollo futuro, con otro encargo

| Tema | Estado / alcance |
|---|---|
| Importar CSV/Excel | V2: análisis, mapeo, errores, revisión e idempotencia |
| Reconciliación nueva | V2: nuevas fuentes sin duplicar apertura ni modificar cierres |
| Nuevos cálculos antes/después | Aplazados: simulación, medias posteriores y comparación calculada; la pantalla propia con datos existentes ya está entregada |
| Preventas / otras ampliaciones | Aplazadas |
| Corrección/reversión de contabilizadas | Sin implementación autorizada |
| Bridge/cambio de red y retroactividad | No habilitados; sin reescritura histórica |
| Réplica automática remota en Drive | [Proyecto independiente del Lab](backups-drive.md); propuesta anotada, no implementada |

Las copias manuales, diarias por cambios y previas, retención y restauración aislada **ya están implementadas y desplegadas**. No mantenerlas como deuda. La réplica externa y el informe diario no forman parte del cierre V1.5.

## Límites conservados

Producción, previa y demo son independientes; movimientos de prueba exclusivamente sintéticos. Los desconocidos históricos siguen no disponibles, nunca cero; no reabrir decisiones financieras aceptadas ni pedir históricos ya cerrados. USD/EUR de pantalla no es una base fiscal histórica. Datos y respaldos permanecen privados.

[Ficha vigente](../aplicaciones/cryptowallet.md) · [Manual privado](https://github.com/ratienza/cryptowallet/tree/main/docs/v1) · [Aceptación V1.5](https://github.com/ratienza/cryptowallet/blob/17489d38ab5398de80c37d4985b15f23f131874f/docs/evidence/CW-V15/acceptance.md).
