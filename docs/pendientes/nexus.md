# Pendientes · Nexus

## Backups

Definir una política global de backups y ejecutar una prueba de restauración.

## Checkouts

- Inventariar y gestionar los checkouts que son solo copias de consulta.
- Mantener explícito `Checkout ≠ Runtime`; el CV en Nexus no es un despliegue.

## Cloudflare Tunnel y recuperación

- Mantener y probar Cloudflare Access + Google para el tráfico externo, conservando LAN sin cambios.
- Definir monitorización, alertas y prueba controlada de recuperación del servicio `cloudflared`.
- Revisar periódicamente las identidades autorizadas y confirmar que no aparezcan políticas `Bypass`.
- Decidir qué servicios de Nexus se publicarán y no crear rutas/hostnames sin encargo específico.
