# Host · DigitalOcean

| Campo | Valor |
|---|---|
| Alias SSH | `docean` |
| Host | `app.raulatienza.com` |
| Usuario actual | `root` |
| Rol | Servicios públicos / 24x7 |

## Patrón esperado

DigitalOcean debe seguir el mismo principio que Nexus: **despliegue desde Git**, separación de secretos y mínima configuración manual irreproducible.

## Límite importante

No existe sincronización automática. El operador solicita una vista previa en el panel, revisa altas, cambios y conflictos, y confirma explícitamente una sola dirección. Credenciales, notificaciones, claves y secretos quedan excluidos.

## Nivel de validación

DigitalOcean se inspeccionó de forma acotada el **10/08/2026** durante el cierre de Reserva-Pistas-UTP:

- `reserva-pistas.service` y Nginx estaban activos; la configuración Nginx superó su validación.
- El backend local respondió correctamente y la ruta pública mantuvo la autenticación previa.
- El estado vivo contenía 18 registros —12 cancelados y 6 reservados—, sin tareas activas ni duplicados.
- La migración eliminó credenciales heredadas de las tareas sin alterar su contenido funcional; los ficheros locales de credenciales y notificaciones conservaron sus hashes.
- Nexus accede únicamente mediante una clave dedicada y un comando SSH forzado que ejecuta el peer como usuario `reserva`, sin shell, TTY ni forwarding.
- Tras la primera réplica DigitalOcean → Nexus, las vistas previas de ambas direcciones mostraron 18 elementos sin cambios y cero conflictos.

La inspección no modificó DNS, certificados, puertos ni la topología pública. El detalle operativo y de recuperación está en la ficha de la aplicación.

## Revalidación del 13/08/2026

- App Launch respondió `200` por HTTP y HTTPS, sin puerto explícito.
- `index.html`, `apps.json` y el fondo PNG respondieron correctamente.
- El catálogo público coincidió exactamente con `catalogs/public.json` y no contenía referencias internas de Nexus.
- `reserva-pistas.service`, `consumos-cupra.service` y Nginx estaban activos.
- `/padel/` y `/consumos/` devolvieron `401` sin credenciales; `/salones/` devolvió `200`.
- No se modificaron servicios, datos, autenticación, certificados ni configuración Nginx durante esta revalidación.
