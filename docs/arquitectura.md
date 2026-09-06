# Arquitectura

## Modelo general

```mermaid
flowchart TB
    U["Usuario externo"] --> CF["Cloudflare<br/>DNS + HTTPS"]
    CF --> CA["Cloudflare Access<br/>política por hostname"]
    CA --> GI["Google IdP<br/>autenticación"]
    GI --> CA
    CA --> T["Cloudflare Tunnel<br/>replicant-launch"]
    T --> F["cloudflared<br/>conexión saliente desde Nexus"]
    F --> NS["Servicios Nexus<br/>Launch · Salones · Docs · Pádel · Red"]

    subgraph LAN["LAN 192.168.18.0/24"]
        R["Replicant<br/>Windows 11 Pro<br/>192.168.18.200"]
        N["Nexus<br/>Ubuntu 24.04 LTS<br/>192.168.18.220"]
        R -->|Hyper-V| N
        N --> F
        N --> NR["Docker / servicios internos"]
        NR --> NS
    end

    GH["GitHub<br/>fuente versionable"] --> N
    GH --> DO["DigitalOcean<br/>Nginx / servicios públicos"]
    DO --> DAL["App Launch público"]
    NS --> LINKS["Enlaces locales y remotos"]
    DAL --> LINKS
    LINKS --> GC["Google Cloud<br/>Cloud Run / Firebase"]
```

App Launch es catálogo y capa de acceso. No ejecuta las aplicaciones enlazadas ni demuestra que residan en el mismo host.

## App Launch multientorno

```mermaid
flowchart TD
    CODE["Código común"] --> PUB["Deploy público"]
    CODE --> LAB["Deploy Nexus"]
    PC["Catálogo público"] --> PUB
    NC["Catálogo Nexus"] --> LAB
    PUB --> DO["DigitalOcean / Nginx"]
    LAB --> NX["Nexus / Nginx"]
    DO --> PURL["Enlaces públicos"]
    NX --> NURL["Enlaces internos y externos"]
```

El catálogo se selecciona durante el despliegue. Cada host recibe únicamente su `apps.json`; la lógica visual es común.

## Responsabilidades

| Elemento | Responsabilidad |
|---|---|
| Replicant | Estación principal Windows, desarrollo local, Hyper-V y administración |
| Nexus | Laboratorio Linux, Docker, servicios internos y copias de consulta |
| GitHub | Código, configuración versionable e histórico |
| DigitalOcean | App Launch público, Reservas y otros servicios publicados en el VPS |
| Google Cloud Run | Producción canónica de Consumos Cupra |
| Firebase Hosting | Producción pública del CV |
| App Launch | Catálogo y navegación hacia aplicaciones locales o remotas |
| `/opt/data`, `/opt/secrets`, `/opt/backups` | Datos, secretos y copias fuera de Git |

!!! important "Dos reglas de lectura"
    `Checkout ≠ Runtime` y `Tarjeta App Launch ≠ Runtime local`.

Docker es el patrón preferido para servicios internos de Nexus cuando encaja, no un requisito universal para todas las aplicaciones.

## Publicación externa mediante Cloudflare Tunnel

Nexus mantiene los servicios internos en la LAN. Cloudflare termina DNS/HTTPS, Google identifica al usuario y Access autoriza cada aplicación. El único Tunnel `replicant-launch` transporta mediante la conexión saliente de `cloudflared` las rutas de Launch (`80`), Salones (`8081`), documentación (`8082`), Pádel (`8083`) y Control de Red (`8084`). El router no abre puertos entrantes.

El Tunnel no autentica usuarios: cada hostname tiene su aplicación y política Access independiente. [Cloudflare Tunnel](red/cloudflare-tunnel.md) contiene la topología, operación, recuperación y límites.
