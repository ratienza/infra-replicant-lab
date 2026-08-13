# Host · DigitalOcean

| Campo | Valor |
|---|---|
| Alias SSH | `docean` |
| Host | `app.raulatienza.com` |
| SO | Linux en VPS DigitalOcean |
| Acceso | SSH administrativo por clave |
| Función | Nginx, App Launch público y servicios web alojados en el VPS |

## Modelo operativo

DigitalOcean publica App Launch como capa de navegación y aloja Reserva-Pistas-UTP. Debe mantener despliegues desde fuentes versionadas, secretos fuera de Git y mínima configuración manual.

App Launch puede enlazar servicios externos. En particular, Consumos Cupra se ejecuta en Google Cloud Run y el CV en Firebase Hosting; sus tarjetas no los convierten en runtimes de DigitalOcean.

## Estado validado

- App Launch respondió `200` por HTTP/HTTPS y sus assets y catálogo público fueron verificados.
- Reserva-Pistas-UTP mantiene backend local y publicación mediante Nginx con autenticación.
- El canal de sincronización de Reservas con Nexus usa una clave dedicada y un comando SSH forzado, sin shell, TTY ni forwarding.
- No existe sincronización automática de los datos de Reservas: el operador revisa una vista previa y confirma una dirección.

La documentación no incluye contraseñas, claves privadas ni valores de secretos. Los cambios de DNS, certificados, servicios o datos requieren un encargo específico.
