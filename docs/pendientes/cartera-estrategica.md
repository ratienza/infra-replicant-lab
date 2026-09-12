# Pendientes · Cartera Estratégica

## Estado

La v1.0 LAN está cerrada, desplegada y validada en Nexus. CE-SEC-001 está implementado y probado: PIN independiente y Google OIDC preparado. Google permanece desactivado mientras la aplicación solo sea LAN; Codex no creó ni registró el PIN del usuario.

## Único bloque pendiente para publicación externa

1. Publicar Cartera mediante el Tunnel ya existente, sin abrir puertos en el router.
2. Fijar la URL HTTPS definitiva.
3. Registrar en Google Cloud el callback exacto `<URL_HTTPS_PUBLICA>/oauth2callback`.
4. Guardar `client_id`, `client_secret` y `cookie_secret` como secretos privados de Nexus, fuera de Git.
5. Configurar la allowlist con el correo Google exacto del usuario.
6. Activar `Habilitar Google OAuth`.
7. Validar desde una red externa HTTPS, login, allowlist, sesión, logout y el orden Google → PIN cuando ambos estén activos.

Este bloque no debe requerir cambios de código, migraciones ni rediseño. Hasta completarlo, Google OAuth no se declara activo ni validado y Cartera no se incorpora a Cloudflare, DNS, Access ni al catálogo público.

## Operación LAN pendiente del usuario

El usuario puede configurar y activar su PIN manualmente en `Configuración → Seguridad → PIN`. El PIN funciona de forma independiente aunque Google OAuth siga desactivado. No se documentará ni almacenará su valor.
