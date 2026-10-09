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

## CryptoWallet V1.5

Producción privada en localhost `8516`; previa independiente en `8517`. Identidad vigente y fuentes en la [ficha](../aplicaciones/cryptowallet.md). Google interno activo, PIN 24 horas y privacidad inicial ON. La confirmación manual de Raúl acredita el recorrido autorizado; no sustituirla por una supuesta prueba del agente. Un cambio documental recrea únicamente Replicant Lab; conserva servicios y datos financieros.

Antes de actualizar código: identificar imagen/esquema y conjunto vivo; obtener copia previa completa y verificar huellas, integridad y restauración aislada; respaldar seguridad separadamente. Tras promover código compatible, comprobar montajes, usuario, salud, cadena y comparación financiera. Conservar imagen y compose previos; rollback de código no autoriza restaurar datos antiguos sobre movimientos nuevos.

Copias locales desde **Ajustes → Backup**: manuales, diarias solo si cambia el estado y previas verificadas que bloquean la escritura si fallan. Retención 7 / 10 / 10; protegidas conservadas. Restaurar requiere previsualización, confirmación, `pre_restore`, candidato aislado e instalación completa con recuperación ante fallo. No ensayar sobre producción. Seguridad excluida de las descargas financieras y preservada al restaurar finanzas. [Procedimiento privado](https://github.com/ratienza/cryptowallet/blob/main/docs/v1/operacion.md).

La previa no es réplica de recuperación. La [réplica automática Drive](../pendientes/backups-drive.md) y sus avisos son un proyecto futuro independiente; las copias locales no acreditan recuperación remota del host. Cuenta no autorizada, cancelación/error OIDC y recorrido móvil exterior quedan como [cobertura no verificada aceptada](../pendientes/cryptowallet.md).
