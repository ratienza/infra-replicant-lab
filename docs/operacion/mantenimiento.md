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

## Cloudflare Tunnel

El mantenimiento del Tunnel empieza por consulta segura: estado del servicio, origen local y hostname público. No se abre port forwarding como mecanismo de recuperación. Cualquier reinicio, actualización o cambio de ruta se planifica con rollback y se valida desde una red externa; Access + Google sigue pendiente y no debe declararse activo.
