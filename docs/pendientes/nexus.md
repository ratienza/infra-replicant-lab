# Pendientes · Nexus

## Backups

Definir una política global de backups y ejecutar una prueba de restauración. CryptoWallet V1.5 ya dispone de copias locales multibase verificadas y retención; esto no acredita respaldo remoto del host ni de otras aplicaciones.

[Backups Lab V1.0](../aplicaciones/backups-lab.md) está implementado/publicado con ocho alcances Drive/recuperación aislada y retención automática OFF. No acredita backup integral del host. Informe diario,log exportable y fuentes adicionales quedan en [Backlog V2.0](backups-drive.md), con decisiones pendientes.

## Checkouts

- Inventariar y gestionar los checkouts que son solo copias de consulta.
- Mantener explícito `Checkout ≠ Runtime`; el CV en Nexus no es un despliegue.

## Cloudflare Tunnel y recuperación

- Mantener y probar Cloudflare Access + Google para el tráfico externo, conservando LAN sin cambios.
- Definir monitorización, alertas y prueba controlada de recuperación del servicio `cloudflared`.
- Revisar periódicamente las identidades autorizadas y confirmar que no aparezcan políticas `Bypass`.
- Decidir qué servicios de Nexus se publicarán y no crear rutas/hostnames sin encargo específico.
