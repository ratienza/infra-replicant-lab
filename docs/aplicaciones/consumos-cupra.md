# Aplicación · Consumos Cupra

Aplicación personal para registrar y analizar consumos de combustible, con entrada manual, estadísticas, lectura y escritura mediante Google Sheets y extracción opcional de datos desde imágenes.

## Estado auditado

| Campo | Valor |
|---|---|
| Repositorio | `ratienza/Consumos_Cupra` · privado |
| `main` | `050535f9f36b1ea4708277e94ffecb9212bcd02a` |
| Nexus | No existe checkout ni servicio; App Launch enlaza a DigitalOcean |
| DigitalOcean | `consumos-cupra.service` activo |
| Ruta / URL | `/opt/consumos-cupra` · `https://app.raulatienza.com/consumos/` |
| Runtime | Node/Express en `127.0.0.1:8766`, publicado por Nginx |
| Acceso observado | `401` sin credenciales HTTP Basic |

## Arquitectura y funciones comprobadas

El frontend usa React 19, Vite, Tailwind y Recharts. El backend Express sirve el frontend y expone endpoints para registros, configuración, pendientes, extracción de imágenes, escritura y diagnóstico de conectividad.

El código versionado contempla Google Sheets/Apps Script, una clave Gemini opcional, webhooks de alertas y almacenamiento local de pendientes. La compilación de producción genera el frontend y `dist/server.cjs`.

No se ejecutaron escrituras, extracción de imágenes, webhooks ni llamadas a servicios externos durante la auditoría.

## Despliegue, persistencia y rollback

DigitalOcean ejecuta el servicio como `www-data:www-data`, con `Restart=on-failure`. Nginx protege y reenvía `/consumos/` al loopback; el proceso Node no está publicado directamente.

Los ficheros principales desplegados coinciden semánticamente con `main`; `server.ts` solo difiere en finales de línea. La ruta desplegada no es un checkout Git, por lo que falta una huella de versión runtime inequívoca y un procedimiento de rollback versionado.

Rollback seguro: recuperar un artefacto construido desde un commit conocido, restaurar la configuración/persistencia separada y reiniciar exclusivamente `consumos-cupra.service`. No debe copiarse el estado vivo a Git.

## Pruebas realizadas

- `pnpm run lint`: correcto.
- `pnpm run build`: correcto.
- Producción pública: `401` sin credenciales, confirmando la barrera de acceso.
- Servicio `systemd`: activo el 13/08/2026.

## Seguridad, dependencias y pendientes

- Gemini, Sheets, Apps Script y webhooks son dependencias externas; sus credenciales deben permanecer fuera de Git.
- El repositorio contiene URL y datos de ejemplo/configuración por defecto que deben tratarse como información privada de la aplicación.
- Los endpoints de configuración y escritura dependen de la protección externa de Nginx; no se validó autorización interna propia.
- No existe servicio de Consumos en Nexus.
- Pendiente: documentar un despliegue reproducible desde `main`, una huella de versión y un rollback probado.
