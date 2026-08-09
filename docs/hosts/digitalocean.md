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

## Nivel de validación

La configuración de producción descrita en este proyecto procede de la documentación versionada del repositorio de Reserva-Pistas-UTP. DigitalOcean no se inspeccionó durante la reconciliación documental del 09/08/2026, por lo que no se afirma una validación viva de su servicio, datos, procesos o configuración.
