# Evidencias · RL-CF-002

Evidencia resumida y deliberadamente no secreta de la implantación realizada el 06/09/2026.

## Cloudflare

- Tunnel existente reutilizado: `replicant-launch`.
- Configuración final: versión 4.
- Reglas: cinco hostnames y fallback `http_status:404`.
- DNS: CNAME proxied para Launch, Salones, Docs, Pádel y Red.
- Access: una aplicación y política independiente por hostname.
- IdP: Google, con redirección directa.
- Router/NAT: sin cambios y sin puertos entrantes.

### Secuencia inicial preservada

- Versión 2: dos ingress idénticos para `launch.thereplicantlab.com`.
- Versión 3: retirada de la regla duplicada, sin cambiar el origen Launch.
- Versión 4: estado final con cinco hostnames y fallback `http_status:404`.
- Callback OAuth aceptado: `https://shy-pine-78cc.cloudflareaccess.com/cdn-cgi/access/callback`.
- Política inicial: `Allow · Replicant Launch · authorized emails`; decisión `Allow`, prioridad y reglas sin cambios.
- Peticiones sin sesión a `/` y `/apps.json`: mismo HTTP `302` hacia Access.

Rollback documentado: restaurar la versión de ingress anterior si la eliminación de la ruta duplicada provoca una regresión; restaurar solo el nombre anterior de la política si fuese necesario; y retirar exclusivamente el callback añadido si se abandona por completo Access, sin tocar otros URI ni ningún secreto OAuth.

## Aplicación

- El frontend carga `./apps.json` con caché desactivada y credenciales same-origin implícitas.
- La carga del catálogo no requería un cambio de JavaScript.
- La indisponibilidad exterior de las tarjetas Nexus procedía de enlaces privados `192.168.18.220:8081-8084`.
- La propuesta de corrección se encuentra en `ratienza/Apps_Lauch#15`.

## Pruebas

- Origen Launch LAN: HTTP 200.
- Catálogo LAN: HTTP 200 y `application/json`.
- Orígenes 8081-8083: HTTP 200.
- Control de Red `/health`: HTTP 200.
- Inventario: 5 entradas públicas y 8 internas.
- OAuth: callback exacto aceptado por Google; desapareció `redirect_uri_mismatch`.
- Logs Access revisados: tres eventos permitidos de Launch, todos del único usuario esperado y desde España.

No se incluyen cookies, tokens, secretos OAuth ni direcciones de correo completas adicionales.
