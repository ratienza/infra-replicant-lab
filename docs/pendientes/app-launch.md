# Pendientes · App Launch

## Mejoras opcionales

- Limpiar assets PWA históricos no utilizados mediante un cambio versionado y verificable.
- Añadir filtros locales por ubicación y tecnología si el número de tarjetas crece.
- Incorporar un estado visual verde/amarillo/rojo solo cuando exista un workflow versionado de comprobaciones reales. Debe diferenciar enlace, runtime y documentación; nunca inferir salud por la mera existencia de una tarjeta.

Estas mejoras no reabren las fases ya cerradas ni representan un fallo de producción.

## Seguridad externa

Cloudflare Access + Google ya está implantado para Launch, Salones, Docs, Pádel y Red, con autorización independiente por hostname.

Pendiente:

- Fusionar y desplegar `Apps_Lauch#15` para que el catálogo Nexus use los hostnames protegidos.
- Validar desde móvil cada aplicación tras el despliegue.
- Auditar el Launch duplicado de DigitalOcean antes de retirarlo, redirigirlo o cambiar enlaces.
