# Aplicación · App Launch

Catálogo **multientorno** y capa de navegación para acceder a aplicaciones públicas y servicios internos. Se publica en Nexus y DigitalOcean; la presentación es común, pero cada entorno puede recibir un catálogo diferente. App Launch no es el runtime de las aplicaciones enlazadas.

## Estado auditado

| Campo | DigitalOcean | Nexus |
|---|---|---|
| Desarrollo | Codex · HTML/CSS/JavaScript | Mismo origen |
| Repositorio | `ratienza/Apps_Lauch` · `main` · `2d265ee1caf3c370e662cdc99cb923f4db457465` | Mismo origen |
| URL | `http://app.raulatienza.com` y `https://app.raulatienza.com` | `http://192.168.18.220` |
| Publicación | Nginx del host · `/opt/portal` | Compose `app-launch` · Nginx `1.27-alpine` |
| Puerto | `80/443`, sin puerto explícito | `80 → 80/tcp` |
| Catálogo activo | `catalogs/public.json → apps.json` | `catalogs/nexus.json → apps.json` |
| Validación | HTTP/HTTPS, HTML, PNG y JSON: `200` | HTML, PNG y JSON: `200`; servicios enlazados sanos |

Validación final: **21/08/2026**. GitHub y el checkout local coincidían en el SHA indicado; ambos catálogos desplegados respondieron `200` y conservaron exactamente el contenido versionado.

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

El catálogo público contiene Reservas, Consumos Cupra, Multimedia VPalace, CV y PULA. El catálogo Nexus contiene Replicant Lab, Reservas, Multimedia VPalace y enlaces externos a Consumos, CV y PULA. En ambos casos PULA apunta a `https://pula-erasmus-housing-automator.ai.studio/`. Un enlace presente en un catálogo no implica que su aplicación se ejecute en el host del launcher.

EH-002 añade únicamente al catálogo Nexus una tarjeta interna **ErasmusHomes · Control del MVP**, dirigida a la página derivada dentro del runtime documental existente de Replicant Lab. El catálogo público y todas las tarjetas preexistentes permanecen sin cambios.

!!! important "Regla"
    `Tarjeta App Launch ≠ Runtime local`.

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
