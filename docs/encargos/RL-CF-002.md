# RL-CF-002 · Consolidar Cloudflare Access y corregir App Launch

## Estado

**Implementado con validación pendiente de usuario/despliegue del catálogo.**

- Base documental: `e0c1795`.
- Rama: `fix/rl-cf-002-access-catalog`.
- Catálogo: PR `Apps_Lauch#15`, sin merge.
- No se han abierto puertos del router ni creado un segundo Tunnel.

## Objetivo

Consolidar la publicación externa de Nexus mediante un único Cloudflare Tunnel, Google como proveedor de identidad y autorización independiente por aplicación. Corregir además el fallo del catálogo y sustituir enlaces LAN por hostnames protegidos.

## Diagnóstico

Se encontraron dos causas diferentes:

1. Google rechazaba inicialmente el callback de Access con `redirect_uri_mismatch`. Se añadió y guardó el callback exacto de la organización de Access.
2. El catálogo Nexus apuntaba a `192.168.18.220:8081-8084`. Esas direcciones funcionan en LAN, pero no son enrutables desde Internet.

También existían dos reglas idénticas para `launch.thereplicantlab.com`; se eliminó la duplicada.

## Estado implantado en Cloudflare

| Aplicación | Hostname | Origen |
|---|---|---|
| Replicant Launch | `launch.thereplicantlab.com` | `http://localhost:80` |
| Replicant Salones | `salones.thereplicantlab.com` | `http://192.168.18.220:8081` |
| Replicant Docs | `docs.thereplicantlab.com` | `http://192.168.18.220:8082` |
| Replicant Padel | `padel.thereplicantlab.com` | `http://192.168.18.220:8083` |
| Replicant Red | `red.thereplicantlab.com` | `http://192.168.18.220:8084` |

Cada hostname tiene:

- registro CNAME proxied hacia el Tunnel;
- aplicación Access `self_hosted`;
- Google como único IdP;
- redirección directa al IdP;
- política `Allow` independiente con la cuenta inicialmente autorizada;
- sesión de 24 horas.

El Tunnel termina con `http_status:404`.

## Validación

- [x] Tunnel remoto sano y configuración actualizada a versión 4.
- [x] Una única ruta de Launch.
- [x] Cuatro CNAME adicionales creados y proxied.
- [x] Cinco aplicaciones Access independientes.
- [x] Políticas por aplicación sin `Bypass`.
- [x] Google dejó de devolver `redirect_uri_mismatch`.
- [x] App Launch y `apps.json` respondieron `200` en LAN.
- [x] Puertos `8081`, `8082`, `8083` y health de `8084` respondieron en LAN.
- [x] Catálogo versionado válido: 5 entradas públicas y 8 internas.
- [x] PR del catálogo sustituye las URLs privadas por hostnames Access.
- [ ] Merge y despliegue de `Apps_Lauch#15` en Nexus.
- [ ] Prueba autenticada desde móvil de cada aplicación tras el despliegue.

## Seguridad

No se documentan secretos, tokens, IDs de cliente completos ni listas de correo. Los logs de Access consultados no mostraron usuarios autenticados distintos del propietario autorizado.
