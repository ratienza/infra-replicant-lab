# Reserva-Pistas-UTP

Ficha de infraestructura y operación de la aplicación de reservas de pádel de Torre de Porta-Coeli. La documentación funcional y de desarrollo permanece en `ratienza/Reserva-Pistas-UTP`; esta página registra el montaje real en Raul Lab y producción.

## Estado validado

| Elemento | Valor |
|---|---|
| Repositorio | `ratienza/Reserva-Pistas-UTP` |
| `main` validado | `6fb055e16eb232d47cc2d759bed0ce2caff4cec9` (runtime) + `6df1698d3346db5c35f7d173b5d7dc2567ce8a5e` (guía operativa) |
| Nexus | ✅ Docker Compose operativo |
| Ruta / URL Nexus | `/opt/apps/Reserva-Pistas-UTP` · `http://192.168.18.220:8083` |
| Datos Nexus | `/opt/data/reserva-pistas` → `/app/data` |
| DigitalOcean | ✅ `reserva-pistas.service` en `loopback:8765` |
| Ruta / URL producción | `/opt/reserva-pistas` · `https://app.raulatienza.com/padel/` |
| Publicación | Nginx + HTTPS + HTTP Basic existente |
| Sincronización | ✅ Bidireccional, por registros y exclusivamente bajo demanda |
| Issue de handover | [#2](https://github.com/ratienza/Reserva-Pistas-UTP/issues/2) cerrado con evidencias |

Validación de sincronización: **10/08/2026**. Revalidación de servicio y código: **13/08/2026**. No se cambiaron puertos, UFW, DNS, certificados, Nginx, autenticación pública ni otros servicios.

## Arquitectura real

```text
Nexus · 192.168.18.220:8083
  reserva-pistas-nginx
        ↓ red privada Docker
  reserva-pistas-app · app:8765 · UID/GID 1000
        ↓
  /app/data ↔ /opt/data/reserva-pistas
        │
        │ SSH dedicado: restrict + comando forzado
        │ solo ping/export/apply/backups/restore
        ↕
DigitalOcean · app.raulatienza.com/padel/
  Nginx · HTTPS · HTTP Basic
        ↓
  reserva-pistas.service · reserva:reserva
  loopback · puerto 8765
        ↓
  /opt/reserva-pistas
```

Nexus coordina ambas direcciones. La clave dedicada está montada de solo lectura, la huella del host DigitalOcean fue contrastada con el canal SSH administrativo ya confiable y el `authorized_keys` remoto no concede shell, TTY ni forwarding. El comando forzado baja privilegios a `reserva` antes de ejecutar `sync_peer.py`.

## Datos y exclusiones

| Estado | Clasificación | Sincronización |
|---|---|---|
| Registros de `tasks.local.json` | Funcional e histórico | Sí, por `id` |
| `_sync` por registro | Origen, creación, modificación, revisión, tombstone y hash | Sí |
| `credentials.local.json` | Credencial local | Nunca |
| `notifications.local.json` | Token/configuración local | Nunca |
| `telegram.users.local` | Autorizaciones locales | Nunca |
| `telegram.offset.local`, `telegram.state.local` | Estado efímero | Nunca |
| `sync-state.local.json` | Base de comparación Nexus | No |
| `sync-audit.local.jsonl` | Auditoría sin valores privados | No |
| `backups/`, logs, PID, red y `app.local.env` | Backup/configuración/estado local | Nunca |

La migración idempotente conservó los 18 registros y eliminó `username` y `password` del histórico. Las tareas consultan `credentials.local.json` únicamente al ejecutarse. `/api/settings` ya no devuelve la contraseña al navegador.

## Runtime revalidado el 13/08/2026

| Elemento | Evidencia |
|---|---|
| GitHub / Nexus | `main` · `6df1698d3346db5c35f7d173b5d7dc2567ce8a5e` |
| Contenedores | `reserva-pistas-nginx` y `reserva-pistas-app` activos |
| Publicación Nexus | Nginx `192.168.18.220:8083 → 80`; backend sin puerto host |
| Persistencia | `/opt/data/reserva-pistas → /app/data` en lectura/escritura |
| Usuario de app | UID/GID `1000:1000` |
| Autoarranque | `restart: unless-stopped` |
| DigitalOcean | `reserva-pistas.service` activo como `reserva:reserva` |
| Producción | `/padel/` devolvió `401` sin credenciales, como se esperaba |

Los hashes de `app.py`, `templates/index.html` y `sync_engine.py` desplegados en DigitalOcean coincidieron con `main`. Se ejecutaron **21 pruebas** locales sobre una copia limpia y todas terminaron correctamente. No se hicieron reservas, cancelaciones, sincronizaciones, notificaciones ni escrituras sobre datos reales.

## Fusión y conflictos

El motor valida JSON e identificadores, calcula hashes canónicos por registro y compara cada lado con la base de la última sincronización:

1. incorpora registros presentes solo en el origen;
2. propaga cambios únicamente del origen;
3. conserva e informa cambios únicamente del destino;
4. conserva registros presentes solo en el destino;
5. propaga cancelaciones y tombstones explícitos;
6. si el mismo `id` cambió en ambos lados, no escribe hasta elegir Nexus, DigitalOcean o cancelar;
7. propaga el lado elegido por la persona;
8. una segunda simulación sin cambios no escribe ni crea un backup innecesario.

Los conflictos visibles se limitan a campos operativos no sensibles. Cada escritura usa bloqueo entre procesos, fichero temporal, `fsync`, reemplazo atómico, verificación de la huella simulada y backup previo.

## Tareas activas

El destino no se modifica mientras tenga tareas `queued` o `running`. Si una tarea activa del origen se incorpora al otro servidor, la copia queda neutralizada como `cancelled` / `sync_neutralized`; conserva el histórico pero no inicia un segundo ejecutor. No existe sincronización automática ni periódica.

## Panel administrativo

En **Ajustes → Sincronización administrativa** aparecen:

- `DigitalOcean → Nexus`;
- `Nexus → DigitalOcean`;
- estado del canal seguro;
- simulación con nuevos, actualizados, sin cambios, cancelaciones, conflictos, tareas activas y backup previsto;
- resolución humana por `id`;
- confirmación explícita, protección contra doble clic y una sola operación concurrente;
- listado y restauración confirmada de backups.

En Nexus todo el backend usa Basic Auth local guardado fuera de Git. En DigitalOcean se conserva el Basic Auth de Nginx. Si falta conectividad o permisos, los botones quedan deshabilitados.

## Backups y recuperación

Backups verificados:

| Servidor | Backup | Resultado |
|---|---|---|
| DigitalOcean | `predeploy-20260810T014853+0200` | Datos, configuración, código, plantilla y unidad systemd; JSON y manifiesto SHA-256 válidos |
| Nexus | `tasks.local.json.20260810T015121+0200.bak` | Estado vacío previo a la primera escritura; JSON válido y restaurable |

Restaurar desde el panel exige confirmación y crea antes otro backup del estado reemplazado. Backups, credenciales y logs nunca atraviesan el canal de sincronización.

## Primera sincronización comprobada

| Paso | Resultado real |
|---|---|
| DigitalOcean antes de migrar | 18 registros: 12 cancelados, 6 reservados, 0 activos, 0 duplicados |
| Migración de secretos | Sin credenciales incrustadas; hash funcional anterior y posterior idéntico |
| Simulación DigitalOcean → Nexus | 18 nuevos, 12 cancelaciones históricas, 0 conflictos, 0 activos |
| Simulación Nexus → DigitalOcean | 18 solo en destino, 0 conflictos; producción no se escribió |
| Aplicación | Solo DigitalOcean → Nexus |
| Segunda simulación, ambas direcciones | 18 sin cambios, 0 nuevos, 0 actualizados, 0 conflictos |
| Hash normalizado común | `db9a806429479d9e83c83724ca67b5e072ca2ab29b94fbde9dbd19475342dc09` |
| Configuración local | Credenciales y notificaciones de producción conservaron hash; Nexus no recibió secretos ni estado Telegram |

## Pruebas y entrega

- 21 pruebas: cambios unilaterales, altas en ambos lados, conflictos, cancelaciones, duplicados, repetición, interrupción, JSON inválido, conectividad, tareas activas, confirmación y restauración.
- Compilación Python y sintaxis JavaScript.
- CI con build Docker y ejecución real como UID/GID 1000.
- Nexus: build, Compose, HTTP 401/200, panel, persistencia, responsive CSS y logs sin errores.
- DigitalOcean: systemd, backend, Nginx, HTTP 401 público, migración equivalente y logs sin warnings.
- PR funcional [#4](https://github.com/ratienza/Reserva-Pistas-UTP/pull/4), corrección de runtime [#5](https://github.com/ratienza/Reserva-Pistas-UTP/pull/5) y guía validada [#6](https://github.com/ratienza/Reserva-Pistas-UTP/pull/6), todos fusionados mediante squash.
- El PR borrador #1 quedó cerrado al quedar incorporado y reconciliado en #4.

## Operación

```bash
# Nexus
cd /opt/apps/Reserva-Pistas-UTP
git switch main
git pull --ff-only origin main
docker compose up -d --build

# Estado
curl -I http://192.168.18.220:8083/
docker compose ps

# Producción
systemctl is-active reserva-pistas nginx
nginx -t
journalctl -u reserva-pistas -n 100 --no-pager
```

No ejecutar reservas ni enviar notificaciones para probar el handover. Las comprobaciones de datos se realizan con simulación, hashes, recuentos e identificadores normalizados.
