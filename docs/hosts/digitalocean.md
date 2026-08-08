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

Los datos sensibles no se sincronizan automáticamente entre Nexus y DigitalOcean. Solo se trasladan cuando exista una decisión explícita.
