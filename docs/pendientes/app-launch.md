# Pendientes · App Launch

## Mejoras opcionales

- Limpiar assets PWA históricos no utilizados mediante un cambio versionado y verificable.
- Añadir filtros locales por ubicación y tecnología si el número de tarjetas crece.
- Incorporar un estado visual verde/amarillo/rojo solo cuando exista un workflow versionado de comprobaciones reales. Debe diferenciar enlace, runtime y documentación; nunca inferir salud por la mera existencia de una tarjeta.

Estas mejoras no reabren las fases ya cerradas ni representan un fallo de producción.

## Seguridad externa

Cloudflare Access + Google ya está implantado para Launch, Salones, Docs, Pádel y Red, con autorización independiente por hostname.

Pendiente:

- `Apps_Lauch#15` ya fusionado; catálogo servido el 08/10/2026 con hostnames protegidos. No sigue pendiente.
- Ajustar metadatos de CryptoWallet a V1.0 (descripción y enlace secundario a la ficha); la tarjeta ya abre producción. Hacerlo en su repositorio y validar el catálogo, sin alterar datos financieros.
- Validar desde móvil cada aplicación tras el despliegue.
- Auditar el Launch duplicado de DigitalOcean antes de retirarlo, redirigirlo o cambiar enlaces.

## Comprobación acotada del 08/10/2026

El catálogo Nexus servido contiene diez tarjetas, incluida CryptoWallet con URL productiva. Checkout en `27a1a179158f874dea52a2748f1bcd20c2091c6a`; existen archivos de despliegue locales no versionados y no se modifican en este encargo. Esta observación no certifica igualdad completa catálogo/Git ni revalida DigitalOcean. La descripción CryptoWallet todavía menciona borradores y falta enlace documental secundario.
