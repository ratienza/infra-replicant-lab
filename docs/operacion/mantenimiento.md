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

El mantenimiento del Tunnel empieza por consulta segura: estado del servicio, origen local y hostname público. No se abre port forwarding como mecanismo de recuperación. Cloudflare Access + Google está implantado, con una aplicación y política independiente por hostname. Cualquier reinicio, actualización o cambio de ruta se planifica con rollback y se valida desde una red externa. Permanecen pendientes el despliegue del catálogo Nexus corregido, la validación autenticada desde móvil, la monitorización y alertas, y una prueba de recuperación.

## Cartera Estratégica

Antes de actualizar el contenedor se confirma que el checkout está limpio y se obtiene una copia consistente mediante la API de backup de SQLite. La copia se valida en staging —integridad, claves foráneas, conteos e invariantes— antes de cualquier promoción atómica. Tras recrear únicamente el proyecto Compose `cartera-estrategica`, se comprueban HTTP `200`, seguridad y datos en modo solo lectura. Ante una diferencia se conserva o restaura el estado anterior; nunca se versionan bases, Excel, CSV, secretos ni backups.
