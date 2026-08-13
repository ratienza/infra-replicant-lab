# Aplicación · Control de Red

Panel PowerShell para inventariar, nombrar y revisar dispositivos de la red local desde Replicant/Windows.

## Estado auditado

| Campo | Valor |
|---|---|
| Repositorio | `ratienza/control-red` · privado |
| `main` | `0e285d26f10ccb58e58d3ebbef35379b00a4b41d` |
| Replicant | Herramienta local; no se ejecutó un escaneo durante la auditoría |
| Nexus | Checkout en `/opt/apps/control-red`; sin contenedor, servicio o puerto |
| Entrada | `ABRIR_PANEL.cmd` → `panel-control-red.ps1` |
| Persistencia | Inventario JSON y snapshots versionados en el repositorio actual |

## Funcionalidad comprobada

El código implementa una interfaz PowerShell para descubrimiento, inventario, alias y snapshots de red. La sintaxis completa del script se analizó correctamente sin ejecutarlo, evitando escaneos o cambios sobre dispositivos.

## Operación y rollback

La herramienta debe ejecutarse desde Replicant, donde existen PowerShell y acceso a la LAN. El checkout de Nexus es solo una copia de código/datos y no convierte el panel en aplicación web.

El rollback de código consiste en volver a un commit conocido mediante rama/PR. Los inventarios y snapshots no deben reemplazarse ni eliminarse automáticamente: requieren copia y revisión específica por contener estado del entorno.

## Seguridad y pendientes

- El repositorio privado contiene inventario y snapshots reales versionados. Esto contradice el criterio global de mantener datos vivos fuera de Git, aunque su visibilidad sea privada.
- No se exponen aquí direcciones MAC, nombres de personas ni detalles del inventario.
- Pendiente: separar datos operativos del código, añadir ejemplos anonimizados y documentar backup/recuperación antes de cualquier limpieza.
- No está desplegado ni validado como servicio en Nexus.
