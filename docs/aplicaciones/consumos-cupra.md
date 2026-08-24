# Aplicación · Consumos Cupra

Aplicación personal para registrar y analizar consumos de combustible. Fue creada inicialmente con AI Studio y remediada con Codex sin alterar su funcionalidad.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/consumos-cupra.html)
- **Aplicación / producción:** [Consumos Cupra](https://app.raulatienza.com/consumos/)

## Estado actual

| Campo | Valor |
|---|---|
| Repositorio | `ratienza/Consumos_Cupra` · privado |
| `main` desplegado | `9f66a368a1dfd58e5b52741e263e77866397a7f7` |
| Build | `7db2eddf-8b54-46fa-a04b-1abcee75d72c` |
| Imagen | `cosnumos-cupra:9f66a368...` |
| Digest | `sha256:df935d3ace3ce6a319094dccfbae80606bc4a3c6d3044f87251d350443be8ed5` |
| Runtime | Google Cloud Run · revisión `cosnumos-cupra-00009-pon` · tráfico `100 %` |
| Rollback disponible | `cosnumos-cupra-00007-b7b` |
| Nexus / DigitalOcean | Sin runtime canónico; App Launch únicamente enlaza la aplicación |

## Arquitectura y despliegue

```text
AI Studio / Codex → GitHub → Cloud Build → Artifact Registry → Cloud Run
```

React 19, Vite, Tailwind y Recharts forman el frontend. Express sirve el bundle y las APIs de registros, configuración, pendientes y diagnóstico. Google Sheets/Apps Script, Gemini y webhooks son dependencias externas opcionales; sus credenciales permanecen fuera de Git.

El trigger productivo construye desde GitHub y crea una revisión candidata con `--no-traffic`, label `candidate`, `entrypoint: gcloud` y `CLOUD_LOGGING_ONLY`. La promoción de tráfico es un paso controlado posterior.

## Validación y operación

La revisión activa se validó con HTTP `200` en raíz, manifest, health, APIs GET no destructivas, configuración, pendientes, iconos, JavaScript y CSS. El build reproducible usa el lockfile y `npm ci`; lint, build e imagen Docker quedaron validados antes de la promoción.

El rollback consiste en devolver el tráfico a `cosnumos-cupra-00007-b7b` o desplegar de nuevo su imagen conocida. No requiere reconstruir el código ni intervenir DigitalOcean o Nexus.

## Seguridad y deuda

- No mostrar valores de variables, secretos o integraciones externas.
- Los pushes a ramas conectadas pueden activar Cloud Build; los cambios productivos requieren revisar trigger, candidato y tráfico.
- `npm audit` registra cuatro vulnerabilidades conocidas: una baja, una moderada y dos altas. No se ejecutó `npm audit fix`; su tratamiento debe hacerse en un cambio separado y probado.
