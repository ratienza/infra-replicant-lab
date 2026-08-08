# Operación · Mantenimiento

## Actualizaciones

`unattended-upgrades` está activo y habilitado. Ubuntu puede diferir ciertos paquetes mediante phased rollout; no se fuerzan salvo necesidad.

Comprobación:

```bash
systemctl status unattended-upgrades --no-pager
```

## Limpieza

`apt autoremove` puede utilizarse tras revisar qué paquetes se eliminarán.

## Criterio de mantenimiento

- Actualizar con regularidad.
- No instalar herramientas "por si acaso".
- Revisar servicios expuestos con `ss -tulpn`.
- Mantener `main` coherente con la realidad.
