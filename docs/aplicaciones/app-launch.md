# Aplicación · App Launch

Catálogo **multientorno** y capa de navegación para acceder a aplicaciones públicas y servicios internos. Se publica en Nexus y DigitalOcean; la presentación es común, pero cada entorno puede recibir un catálogo diferente. App Launch no es el runtime de las aplicaciones enlazadas.

## Accesos

- **Ficha técnica:** [HTML autocontenido](/downloads/apps/app-launch.html)
- **Aplicación / Nexus:** [App Launch interno](http://192.168.18.220/)
- **Aplicación / producción:** [App Launch público](https://app.raulatienza.com/)

## Estado auditado

| Campo | DigitalOcean | Nexus |
|---|---|---|
| Desarrollo | Codex · HTML/CSS/JavaScript | Mismo origen |
| Repositorio | `ratienza/Apps_Lauch` · `main` · `bf6ba47` | Mismo origen |
| URL | `http://app.raulatienza.com` y `https://app.raulatienza.com` | `http://192.168.18.220` |
| Publicación | Nginx del host · `/opt/portal` | Compose `app-launch` · Nginx `1.27-alpine` |
| Puerto | `80/443`, sin puerto explícito | `80 → 80/tcp` |
| Catálogo activo | `catalogs/public.json → apps.json` | `catalogs/nexus.json → apps.json` |
| Validación | HTTP/HTTPS, HTML, PNG y JSON: `200` | HTML, PNG y JSON: `200`; servicios enlazados sanos |

Validación final: **29/08/2026**. GitHub y el checkout local coincidieron en el SHA indicado; ambos catálogos desplegados respondieron `200` y conservaron exactamente el contenido versionado.

## Arquitectura y funcionamiento

`index.html` carga `./apps.json` en tiempo de ejecución y crea las tarjetas mediante nodos DOM. Nombre, descripción y acción se asignan con `textContent`; el manifiesto no se interpreta como HTML.

El despliegue publica solo `index.html`, el fondo y el catálogo seleccionado renombrado como `apps.json`. DigitalOcean no recibió `catalogs/nexus.json`, direcciones `192.168.18.220`, puertos `8081–8083` ni nombres exclusivos del laboratorio.

En Nexus el contenedor monta en solo lectura:

```text
/home/raul/app-launch/site       → /usr/share/nginx/html
/home/raul/app-launch/nginx.conf → /etc/nginx/conf.d/default.conf
```

Usa una red Compose propia, no tiene persistencia funcional y se recupera con `restart: unless-stopped`.

## Catálogos y cápsulas comprobados

El catálogo público contiene Reservas, Consumos Cupra, Multimedia VPalace, CV y PULA. El catálogo Nexus contiene Replicant Lab, ErasmusHomes · Control del MVP, Control de Red, Reservas, Multimedia VPalace y enlaces externos a Consumos, CV y PULA. En ambos casos PULA apunta a `https://pula-erasmus-housing-automator.ai.studio/`.

Las tarjetas usan la acción uniforme **Entrar** y cápsulas breves: `NEXUS`, `DIGITAL` o `REPLICANT` indican ubicación; el resto describe tecnologías relevantes, como `DOCKER`, `NGINX`, `PYTHON`, `FIREBASE APP HOSTING`, `CLOUD RUN` o `POWERSHELL`. CV se presenta correctamente como **Firebase App Hosting** sobre Cloud Run. Las cápsulas son informativas, no healthchecks.

**ErasmusHomes · Control del MVP** abre su panel derivado dentro del runtime documental de Replicant Lab. **Control de Red** aparece únicamente en Nexus: `Entrar` abre su demo Docker read-only en `192.168.18.220:8084` y el acceso secundario abre la ficha técnica. El panel operativo y su inventario siguen siendo locales de Replicant/Windows. Un enlace presente en un catálogo no implica que su aplicación se ejecute en el host del launcher.

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

## Flujo de cambio

```text
catálogos versionados → validación local → rama/PR/checks → main → despliegue del destino → verify.ps1
```

`catalogs/inventory.json` protege el inventario esperado y `scripts/validate_catalogs.py` evita deriva entre los catálogos, enlaces, acciones y cápsulas. Todo cambio debe validar el destino público y/o Nexus que alcance; el flujo general de gobierno permanece en [Work–Codex–Git](/gobierno/flujo-work-codex-git/).

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
