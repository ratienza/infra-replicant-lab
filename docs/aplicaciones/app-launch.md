# Aplicación · App Launch

Launchpad común para acceder a las aplicaciones públicas y a los servicios internos de Replicant Lab. La presentación es única; cada entorno recibe exclusivamente su catálogo activo.

## Estado auditado

| Campo | DigitalOcean | Nexus |
|---|---|---|
| Repositorio | `ratienza/Apps_Lauch` · `main` · `ced6e149315ac14338b547a6773dbb817270b84a` | Mismo origen |
| URL | `http://app.raulatienza.com` y `https://app.raulatienza.com` | `http://192.168.18.220` |
| Publicación | Nginx del host · `/opt/portal` | Compose `app-launch` · Nginx `1.27-alpine` |
| Puerto | `80/443`, sin puerto explícito | `80 → 80/tcp` |
| Catálogo activo | `catalogs/public.json → apps.json` | `catalogs/nexus.json → apps.json` |
| Validación | HTTP/HTTPS, HTML, PNG y JSON: `200` | HTML, PNG y JSON: `200`; servicios enlazados sanos |

Validación final: **13/08/2026**. El repositorio, el checkout local y GitHub coincidían en el SHA indicado.

## Arquitectura y funcionamiento

`index.html` carga `./apps.json` en tiempo de ejecución y crea las tarjetas mediante nodos DOM. Nombre, descripción y acción se asignan con `textContent`; el manifiesto no se interpreta como HTML.

El despliegue publica solo `index.html`, el fondo y el catálogo seleccionado renombrado como `apps.json`. DigitalOcean no recibió `catalogs/nexus.json`, direcciones `192.168.18.220`, puertos `8081–8083` ni nombres exclusivos del laboratorio.

En Nexus el contenedor monta en solo lectura:

```text
/home/raul/app-launch/site       → /usr/share/nginx/html
/home/raul/app-launch/nginx.conf → /etc/nginx/conf.d/default.conf
```

Usa una red Compose propia, no tiene persistencia funcional y se recupera con `restart: unless-stopped`.

## Catálogos comprobados

El catálogo público contiene Reservas, Consumos Cupra, Multimedia VPalace y CV. El catálogo Nexus contiene Replicant Lab, Reservas, Multimedia VPalace y enlaces externos a Consumos y CV. Un enlace presente en el catálogo interno no implica que su aplicación se ejecute en Nexus.

## Actualización y rollback

```powershell
powershell -ExecutionPolicy Bypass -File .\deploy\deploy.ps1 -Target public
powershell -ExecutionPolicy Bypass -File .\deploy\verify.ps1 -Target public
powershell -ExecutionPolicy Bypass -File .\deploy\deploy.ps1 -Target nexus
powershell -ExecutionPolicy Bypass -File .\deploy\verify.ps1 -Target nexus
```

La actualización permanente debe partir de `main`. Para rollback se revierte el cambio en Git mediante una rama/PR y se vuelve a desplegar el destino afectado; no se copian ficheros desde un host hacia GitHub.

## Seguridad y límites

- El repositorio no contiene claves ni configuración local real; `deploy/local.settings.psd1` está ignorado.
- La portada pública no solicita contraseña. La autenticación pertenece a cada aplicación enlazada.
- Nexus es HTTP de LAN; no se declara HTTPS interno.
- El puerto `8080` está libre y no pertenece a App Launch.
- El despliegue público conserva algunos assets PWA históricos no versionados en `/opt/portal/assets`; no intervienen en la portada actual y quedan como deriva a limpiar solo mediante un cambio Git deliberado.

## Pruebas realizadas

- Verificación versionada `public`: catálogo exacto, ausencia de referencias Nexus y HTTP/HTTPS correctos.
- Verificación versionada `nexus`: catálogo exacto y salud HTTP de `8081`, `8082` y `8083`.
- `nginx -t` correcto en DigitalOcean.
- Comprobación visual automatizada de escritorio y móvil incluida en el cierre documental.
