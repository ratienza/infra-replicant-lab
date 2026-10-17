# Pendientes · CryptoWallet

**V1.6.10 cerrada y desplegada el 17/10/2026.** Los borradores pendientes restauran referencia USD/EUR, fecha, fuente, total y cantidad; BCE propone la publicación exacta o la última anterior. La compra sintética completa se confirmó una vez y el reintento no duplicó; el borrador real mantiene la precisión ya persistida y sigue pendiente. Restauración read-only, fallo previo y rollback parcial están verificados en aislamiento. Google interno, PIN, privacidad inicial y copias multibase permanecen activos. La apertura financiera V1.0 sigue aceptada; CW-004 y CW-005 no se reabren.

## Controles operativos reales

| Tema | Estado | Acción siguiente |
|---|---|---|
| Google OIDC interno | Activo; alta y credenciales privadas completadas | Conservar configuración privada; no repetir ni exponer el alta para documentar |
| Recorrido autorizado | Cerrado por confirmación manual de Raúl | Google → PIN → cartera confirmado en incógnito; no atribuir prueba independiente al agente |
| Cobertura OIDC no verificada | Límite aceptado | Cuenta no autorizada y cancelación/error no constan probados; no afirmar que se ejecutaron |
| Exterior móvil | Límite aceptado | No consta probado; no bloquea el cierre aceptado |
| Access/Tunnel transversales | Pendientes operativos del Lab | Revisión administrativa por hostname, monitorización, alertas y recuperación controlada |
| Metadatos de tarjeta App Launch | Ajuste independiente | Revisar descripción vigente y enlace a ficha, sin cambiar runtime financiero |

PIN ya configurado: no solicitar uno nuevo para documentar ni activarlo de nuevo. Duración efectiva 24 horas, privacidad inicial ON y Google interno activo. No compartir secretos por chat o Git. [Alta y recuperación privadas](https://github.com/ratienza/cryptowallet/blob/main/docs/v1/operacion.md).

## Desarrollo futuro, con otro encargo

| Tema | Estado / alcance |
|---|---|
| Importar CSV/Excel | V2: análisis, mapeo, errores, revisión e idempotencia |
| Reconciliación nueva | V2: nuevas fuentes sin duplicar apertura ni modificar cierres |
| Nuevos cálculos antes/después | Aplazados: simulación, medias posteriores y comparación calculada; la pantalla propia con datos existentes ya está entregada |
| Preventas / otras ampliaciones | Aplazadas |
| Corrección/reversión de contabilizadas | Cerrada en V1.6.1 para las seis clases manuales mediante revisiones auditables y borrado lógico; la confirmación original no se reescribe |
| Identidad corporativa aprobada | Cerrada en V1.6.2 con el bitmap y la composición oficial de The Replicant Lab usados por Cartera Estratégica |
| Bridge/cambio de red y retroactividad | No habilitados; sin reescritura histórica |
| Réplica automática remota en Drive | [Proyecto independiente del Lab](backups-drive.md); propuesta anotada, no implementada |

Las copias manuales, diarias por cambios y previas, retención y restauración aislada **ya están implementadas y desplegadas**. No mantenerlas como deuda. La réplica externa y el informe diario no forman parte del cierre V1.6.10.

## Límites conservados

Producción, previa y demo son independientes; movimientos de prueba exclusivamente sintéticos. Los desconocidos históricos siguen no disponibles, nunca cero; no reabrir decisiones financieras aceptadas ni pedir históricos ya cerrados. USD/EUR de pantalla no es una base fiscal histórica. Datos y respaldos permanecen privados.

[Ficha vigente](../aplicaciones/cryptowallet.md) · [Manual privado V1.6.10](https://github.com/ratienza/cryptowallet/tree/v1.6.10/docs/v1) · [Release V1.6.10](https://github.com/ratienza/cryptowallet/blob/v1.6.10/docs/releases/v1.6.md).
