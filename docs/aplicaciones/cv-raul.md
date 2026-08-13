# Aplicación · CV de Raúl

Currículum y portafolio profesional interactivo de Raúl Atienza, con descarga de PDF generada durante la compilación.

## Estado auditado

| Campo | Valor |
|---|---|
| Repositorio | `ratienza/CV-Raul-IA-Estudio-Google-` · privado |
| `main` | `0da08cfa98e5ad9e5e81ed48ac4cd4428360d618` |
| Nexus | Checkout de solo lectura en `/opt/apps/CV-Raul-IA-Estudio-Google-`; sin contenedor ni puerto |
| Producción | Google Cloud/Firebase, no Nexus |
| URL comprobada | `https://ais-pre-unrkdmpgbtoiyyarc3mwzd-499871679551.europe-west2.run.app/` |
| Respuesta observada | `200` tras redirección a comprobación de cookies |

## Arquitectura y funciones comprobadas

La aplicación usa Vite, Tailwind y una etapa de generación PDF con PDFKit. El build crea `public/cv.pdf`, lo integra en la descarga del sitio y produce un frontend estático. El Dockerfile construye con Node y sirve el resultado con Nginx en el puerto interno `8080`.

La compilación aislada `pnpm run build` terminó correctamente y generó tanto el PDF como el bundle Vite. No se modificó ni desplegó Firebase, Cloud Run o la configuración DNS.

## Despliegue y rollback

`firebase.json` define una reescritura hacia Cloud Run en `europe-west2`; `cloudbuild.yaml` describe otro nombre de servicio y `europe-west1`. La URL realmente enlazada usa además un servicio `ais-pre` de `europe-west2`. Esta divergencia impide afirmar qué fichero reproduce por sí solo la producción actual.

El rollback debe realizarse en Google Cloud/Firebase a una revisión conocida, nunca desde el checkout de Nexus. El checkout interno sirve para consulta y no constituye un despliegue.

## Seguridad y pendientes

- El CV es público y contiene datos profesionales; no deben añadirse datos privados no destinados a publicación.
- No se le atribuye persistencia ni secretos en Nexus.
- Pendiente: reconciliar en su repositorio la ruta real Firebase/Cloud Run, región, nombre de servicio y procedimiento de rollback.
- La pantalla de comprobación de cookies fue validada; no se afirma que la página final se renderizara en esa sesión.
