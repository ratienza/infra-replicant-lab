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
