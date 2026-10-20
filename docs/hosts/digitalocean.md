# Host · DigitalOcean

| Campo | Valor |
|---|---|
| Alias SSH | `docean` |
| Host | `app.raulatienza.com` |
| SO | Linux en VPS DigitalOcean |
| Acceso | Desde Replicant: `ssh docean` (SSH administrativo por clave) |
| Función | Nginx, App Launch público y servicios web alojados en el VPS |

## Modelo operativo

DigitalOcean publica App Launch como capa de navegación y aloja Reserva-Pistas-UTP. Debe mantener despliegues desde fuentes versionadas, secretos fuera de Git y mínima configuración manual.

App Launch puede enlazar servicios externos. En particular, Consumos Cupra se ejecuta en Google Cloud Run, el CV en Firebase Hosting y PULA en su publicación pública de Google/AI Studio; sus tarjetas no los convierten en runtimes de DigitalOcean.

## Estado validado

- App Launch respondió `200` por HTTP/HTTPS y sus assets y catálogo público fueron verificados; la tarjeta PULA apunta a la URL pública exacta y figura en el catálogo versionado `2d265ee`.
- Reserva-Pistas-UTP mantiene backend local y publicación mediante Nginx con autenticación.
- El canal de sincronización de Reservas con Nexus usa una clave dedicada y un comando SSH forzado, sin shell, TTY ni forwarding.
- No existe sincronización automática de los datos de Reservas: el operador revisa una vista previa y confirma una dirección.

La documentación no incluye contraseñas, claves privadas ni valores de secretos. Los cambios de DNS, certificados, servicios o datos requieren un encargo específico.

## Relación con Cloudflare Tunnel

DigitalOcean conserva el papel de producción `24×7` y no fue modificado. El Tunnel actual `replicant-launch` termina en Nexus; no convierte Nexus en sustituto automático del VPS ni implica instalar otro Tunnel en DigitalOcean. El Launch duplicado del VPS permanece hasta una auditoría específica de dependencias, redirecciones y rollback.

## Web comercial pública · The Replicant Lab v1.0 (20/10/2026)

**PUBLICADA Y VERIFICADA en DigitalOcean**, independiente de App Launch y de la documentación privada de Nexus.

| Campo | Valor observado |
| --- | --- |
| URL canónica | https://thereplicantlab.com/ |
| WWW | https://www.thereplicantlab.com/ → 301 a raíz |
| VPS IPv4 | `67.205.130.207` |
| DNS Cloudflare | `A @ 67.205.130.207` y `CNAME www thereplicantlab.com`, inicialmente DNS only |
| Nginx vhost | `/etc/nginx/sites-available/thereplicantlab.com`, enlazado en `sites-enabled/` |
| Webroot | `/var/www/thereplicantlab.com/current` → `releases/v1.0/site` |
| Fuente | ZIP canónico en `ratienza/replicant-lab-business`: `docs/06-web/releases/v1.0/The_Replicant_Lab_Web_v1.0.zip` |
| SHA-256 ZIP | `f9e8c07a7e5f5a539671870aa6197cf7c9d22787110a07a9cfeb1b7554153c68` |
| TLS | Let's Encrypt raíz + www; caduca 2027-01-18 |
| Renovación | Certbot timer enabled/active y ensayo `renew --dry-run` satisfactorio |
| HTTP | Redirige 301 a HTTPS; conserva `/.well-known/acme-challenge/` para renovación |
| Publicación estática | 24 recursos públicos; dos archivos internos de revisión movidos a `releases/v1.0/review-internal/` (fuera de webroot) |

**Verificación externa:** HTTPS raíz 200 con cadena TLS válida; WWW/HTTP 301; HTML, Inter local, fotografía, robots y sitemap 200; URL inexistente 404. `nginx -t` correcto. El servicio existente de App Launch (`https://app.raulatienza.com/`) siguió respondiendo 200. Copia de la anterior configuración del nuevo vhost conservada como `.before-https-<timestamp>`; App Launch, Nexus y Tunnel no se cambiaron.

**Operación/rollback:** actualizar solo desde Git/ZIP versionado verificando SHA. Cada siguiente release debe extraerse en un directorio independiente, validarse y promocionarse moviendo el enlace `current`. El rollback revierte ese enlace a la release anterior y valida Nginx. No confundir con el Docker Compose de la biblioteca MkDocs de Nexus.

**Pendientes no cubiertos por este despliegue:** identificación legal, privacidad, Google Analytics con ID real y consentimiento, formulario con envío directo, Search Console y prueba interactiva final. La autorización del propietario para publicar antes del cierre legal no equivale a conformidad jurídica. La web es públicamente indexable aunque no se anuncie.

