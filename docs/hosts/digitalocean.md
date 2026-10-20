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


## Actualización web comercial v1.0.1 — Analytics (20/10/2026)

**Versión pública activa:** `/var/www/thereplicantlab.com/current` apunta a `releases/v1.0.1/site`. V1.0 se preserva para rollback. Este cambio no afecta a App Launch, Nexus ni a Nginx/HTTPS.

- Artefacto: `ratienza/replicant-lab-business/docs/06-web/releases/v1.0.1/The_Replicant_Lab_Web_v1.0.1.zip`
- Integridad: **13.927.402 bytes**, 27 entradas con separadores POSIX; SHA-256 `f9e9779f31bec2d5efe2a01f385b92f3ae7e387fb605a992ee5dcf63b84038de`. El PR comercial #24 corrigió rutas Linux antes del despliegue.
- GA4: `G-PF31D9G91C`. Consent Mode v2 **básico**: no hay etiquetas de Google ni peticiones antes de aceptación. Rechazar y revocar desactivan analítica; nueva ruta pública `/cookies.html`.
- Validación: HTTPS raíz, página de cookies, `assets/consent.js`, `assets/consent.css`, Inter e imagen original devuelven 200 con TLS válido; Playwright escritorio 1440/móvil 390 confirmó 0 peticiones antes de aceptar o tras rechazar, peticiones tras aceptar y desactivación al retirar.
- **Pendiente fuera de infraestructura:** identidad legal y privacidad, confirmación de eventos en panel GA4 Tiempo real, contacto con envío directo. No equivale a conformidad legal.
- Rollback operativo: volver a apuntar el symlink `current` a `releases/v1.0/site` sin eliminar versiones. Nginx conserva mismo vhost y certificado de Let's Encrypt.


## Actualización 20/10/2026 — Web pública v1.0.2 (pie y páginas mínimas)

**Versión activa comprobada:** `/var/www/thereplicantlab.com/current` → `releases/v1.0.2/site`. Nginx/HTTPS y el resto de servicios no cambiaron. Las releases `v1.0` y `v1.0.1` siguen disponibles para rollback.

- Fuente Git privada: `ratienza/replicant-lab-business/docs/06-web/releases/v1.0.2/The_Replicant_Lab_Web_v1.0.2.zip` (PR #27).
- ZIP: 30 archivos · 14.211.802 bytes · SHA-256 `3c914c93f6a1eda4530a537f6a94e53d3b17bc5e8a9a4b0d47ddda7fd3aebfce`.
- Cambios permitidos: logo corporativo central-R4 original sobre fondo oscuro en el pie FAQ, enlaces `/aviso-legal.html`, `/privacidad.html` y Cookies, texto del aviso de cookies abreviado; GA4 `G-PF31D9G91C` y el mailto del formulario permanecen sin cambios funcionales.
- Validación productiva: HTTPS y certificado correctos, página raíz + aviso legal + privacidad + cookies + logo HTTP 200, Playwright 1440/390 px sin desbordamiento horizontal ni errores JS, rechazo sin peticiones a Google. App Launch sigue HTTP 200.
- **Decisión de privacidad:** no publicar datos personales del propietario (nombre, NIF/DNI ni domicilio). Las páginas informativas actuales NO constituyen regularización legal completa: identificación del prestador y del responsable de tratamiento **pendientes**.
- Para rollback, apuntar `current` a `releases/v1.0.1/site` y verificar HTTPS; no borrar releases conservadas.


## Web comercial v1.0.3 — Corrección del pie en todas las secciones (20/10/2026)

- **Versión activa comprobada:** `/var/www/thereplicantlab.com/current` apunta a `releases/v1.0.3/site`. Las versiones v1.0.2 y anteriores siguen almacenadas para rollback.
- **Motivo:** la v1.0.2 tenía el pie corporativo exclusivamente en FAQ; no era visible desde Inicio, Servicios, Contacto ni las otras secciones. La v1.0.3 distribuye el mismo pie original, con logo central-R4 y enlaces legales, en los siete paneles del sitio.
- **Artefacto canónico:** `ratienza/replicant-lab-business/docs/06-web/releases/v1.0.3/The_Replicant_Lab_Web_v1.0.3.zip`, 30 recursos, 14.212.089 bytes, SHA-256 `1e0aae303fb9680b862fcd7a979f19d58d1fc49bc446ff4a9060db5e6114f30d` (PR comercial #28).
- **Validación en producción:** navegador Playwright 1440 y 390 píxeles; un pie y un enlace funcional de Cookies por cada sección, logo cargado, cero solicitudes a Google tras rechazar analítica, sin errores JS o desbordamiento horizontal. El funcionamiento y certificado HTTPS de Nginx no se cambiaron.
- **Pendientes intactos:** regularización de identidad legal del prestador y responsable de tratamiento, y formulario con envío directo; se conserva la actual decisión del propietario de no publicar nombre, NIF ni dirección.

