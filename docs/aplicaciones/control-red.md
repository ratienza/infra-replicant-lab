# Aplicación · Control de Red

Panel PowerShell para inventariar, nombrar y revisar dispositivos de la red local desde Replicant/Windows.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/control-red.html)
- **Runtime:** local en Replicant · sin URL publicada.
- **Demo Nexus:** [escaneo read-only](http://192.168.18.220:8084/)

## Estado auditado

| Campo | Valor |
|---|---|
| Desarrollo | PowerShell + Codex |
| Repositorio | `ratienza/control-red` · privado |
| `main` | `0e285d26f10ccb58e58d3ebbef35379b00a4b41d` |
| Replicant | Herramienta local; no se ejecutó un escaneo durante la auditoría |
| Nexus | Demo Docker `control-red-demo` en `192.168.18.220:8084`; checkout en `/opt/apps/control-red` |
| Entrada | `ABRIR_PANEL.cmd` → `panel-control-red.ps1` |
| Persistencia | Inventario JSON y snapshots versionados en el repositorio actual |

## Funcionalidad comprobada

El código implementa una interfaz PowerShell para descubrimiento, inventario, alias y snapshots de red. La sintaxis completa del script se analizó correctamente sin ejecutarlo, evitando escaneos o cambios sobre dispositivos.

## Operación y rollback

La herramienta operativa debe ejecutarse desde Replicant, donde existen PowerShell y el inventario real. Nexus aloja una demo Docker distinta: ejecuta ping concurrente solo sobre `192.168.18.0/24`, puede mostrar MAC ya observadas en ARP y no persiste resultados. No permite renombrar, enriquecer, abrir puertos ni Wake-on-LAN.

El rollback de código consiste en volver a un commit conocido mediante rama/PR. Los inventarios y snapshots no deben reemplazarse ni eliminarse automáticamente: requieren copia y revisión específica por contener estado del entorno.

## Seguridad y pendientes

- El repositorio privado contiene inventario y snapshots reales versionados. Esto contradice el criterio global de mantener datos vivos fuera de Git, aunque su visibilidad sea privada.
- No se exponen aquí direcciones MAC, nombres de personas ni detalles del inventario.
- Pendiente: separar datos operativos del código, añadir ejemplos anonimizados y documentar backup/recuperación antes de cualquier limpieza.
- La demo Nexus no sustituye el panel operativo de Replicant ni su inventario.
