# Pendientes · Cartera Estratégica

## Estado

La publicación privada está completada y validada: Cartera se mantiene operativa en Nexus, responde por LAN y su hostname público está protegido por Cloudflare Access, Google OIDC interno y PIN de seis cifras. SQLite, migraciones y datos financieros permanecen íntegros y privados.

No existe un pendiente bloqueante específico de publicación, OIDC o PIN de Cartera.

## Límites permanentes

- La URL LAN y la URL pública son rutas distintas; Cloudflare protege únicamente el hostname externo.
- La SQLite no se expone por ninguna ruta y no se almacena en Git.
- App Launch y los servicios `8081–8084` no cambiaron durante esta publicación.
- La configuración sensible y las rutas privadas no se documentan.

## Mejora no bloqueante · privacidad visual

Añadir un botón de ojo abierto/cerrado, abierto por defecto. Al cerrarlo, debe ocultar con asteriscos todos los importes absolutos y cualquier dato que permita reconstruirlos: saldos, patrimonio, cash, ganancias/pérdidas en euros, precios, cantidades, ejes y tooltips monetarios. Debe conservar porcentajes y datos no financieros. Análisis técnico, SMC y Rotaciones no se ven afectados. Esta mejora no está implementada y no bloquea la publicación actual.
