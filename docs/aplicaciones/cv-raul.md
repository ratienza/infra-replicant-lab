# Aplicación · CV de Raúl

Currículum y portfolio profesional público creado con AI Studio, con frontend Vite/Tailwind y descarga de PDF generada durante la compilación.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/cv-raul.html)
- **Aplicación / producción:** [CV de Raúl](https://cv.raulatienza.com)

## Estado actual

| Campo | Valor |
|---|---|
| Repositorio | `ratienza/CV-Raul-IA-Estudio-Google-` · privado |
| `main` | `0da08cfa98e5ad9e5e81ed48ac4cd4428360d618` |
| Producción | Firebase Hosting · proyecto `replicant-lab` |
| Versión activa observada | `092bfc` |
| Backend público identificado | `cv-backend` |
| URL | `https://cv.raulatienza.com` · HTTP `200` |
| Nexus | Checkout limpio de consulta; sin contenedor, servicio o puerto |

## Arquitectura real

La cadena demostrada actualmente es:

```text
despliegue manual Firebase Hosting → infraestructura Google/Firebase → cv.raulatienza.com
```

No está demostrada una cadena automática GitHub → producción ni la relación exacta entre el SHA actual y la versión Firebase `092bfc`.

El servicio Cloud Run `cv-raulatienza-com` del proyecto `consumos-cupra`, región `europe-west1`, conserva una revisión placeholder y un trigger fallido. Es residual y no constituye la producción pública. La reescritura Cloud Run declarada en `firebase.json` tampoco corresponde al servicio público observado.

## Build, validación y rollback

El proyecto usa Vite, Tailwind, Node 20 y una generación PDF con PDFKit. El Dockerfile disponible construye con Node y sirve el resultado mediante Nginx, pero no describe el runtime canónico actual.

Producción, `/health` y `/manifest.json` respondieron `200`; las dos últimas rutas son fallback de la SPA, no healthcheck ni manifest independientes. Firebase conserva versiones anteriores, por lo que existe capacidad de rollback desde Hosting.

## Seguridad y deuda POST-CARTERA

No existe un problema crítico actual. Queda aceptado para después de Cartera:

- reconciliar Firebase, Cloud Build y configuraciones residuales;
- retirar o corregir el trigger obsoleto y demostrar trazabilidad SHA → versión Firebase;
- lockfile, reproducibilidad, CI, tests y typecheck;
- restos React, metadata Gemini, artefactos residuales, cabeceras, caché, protección de `main` y UX de revelado de contacto.

El checkout de Nexus no debe ejecutarse ni utilizarse para desplegar o restaurar producción.

## Revisión de vigencia · 31/10/2026

Main `4f04ef2` del 30/10 incorpora etiqueta Google Analytics al CV. [Commit](https://github.com/ratienza/CV-Raul-IA-Estudio-Google-/commit/4f04ef2129fa87da038014fa40b72382be35688b). La lectura HTTPS registrada el 30/10 acredita instalación del código, no recepción de eventos. Launch Nexus servido el 31/10 enlaza un placeholder Cloud Run: contradicción de catálogo pendiente, sin cambiar la producción Firebase.
