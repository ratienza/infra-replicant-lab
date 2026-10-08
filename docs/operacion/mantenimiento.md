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

El mantenimiento del Tunnel empieza por consulta segura: estado del servicio, origen local y hostname público. No se abre port forwarding como mecanismo de recuperación. Cloudflare Access + Google está implantado, con una aplicación y política independiente por hostname. Cualquier reinicio, actualización o cambio de ruta se planifica con rollback y se valida desde una red externa. El catálogo Nexus corregido por #15 ya está integrado y sus enlaces protegidos se observan en el catálogo servido. Permanecen pendientes la validación autenticada desde móvil por hostname, la revisión administrativa de los nuevos accesos, la monitorización y alertas, y una prueba de recuperación.

## Cartera Estratégica

La release productiva v2.0.0 está fijada al tag y SHA `c672eb1cadfcb191aaff6db8aeb1ed783321b692`; un cambio documental de Replicant Lab **no** reinicia Cartera. Para un futuro despliegue funcional, confirmar commit aprobado y checkout limpio, obtener backup SQLite consistente externo mediante su API, probar restauración aislada, registrar huella, tamaño, `integrity_check`, claves foráneas y conteos financieros. Tras promover solo la imagen aprobada, comprobar SHA del contenedor, mismo montaje `CARTERA_DB_PATH`, integridad y conteos, HTTP, Google OAuth y PIN. Evitar migraciones implícitas. El rollback de código recupera la imagen anterior sin sustituir la base; la recuperación de datos requiere decisión separada y copia verificada. Nunca se versionan bases, Excel, CSV, secretos ni backups. La cuenta Indexa se refresca al abrir/recargar sesión o con botón, no por tarea diaria autónoma; una caída de API deja visible el último cierre oficial y su fecha.

## CryptoWallet V1.0

Producción privada aceptada en localhost `8516`; previa independiente en `8517`. Este cierre documental no reinicia servicios financieros. Para una actualización futura, obtener corte coherente del conjunto multibase con API SQLite, apertura/permiso, catálogo, confirmaciones y borradores; verificar huellas, integridad y restauración aislada. Preservar datos vivos y utilizar código compatible con esquema 1. La antigua versión sin motor no es recuperación después de nuevas confirmaciones. No confundir respaldo puntual de aceptación con backups automáticos ni previa con réplica de producción. [Ficha y guía privada enlazada](../aplicaciones/cryptowallet.md).
