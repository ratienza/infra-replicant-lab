# Arquitectura

## Modelo general

Replicant Lab separa cuatro planos: **desarrollo y código**, **runtimes**, **navegación** y **acceso externo**. App Launch es un catálogo; no ejecuta las aplicaciones enlazadas.

```mermaid
flowchart LR
    DEV["Desarrollo<br/>Replicant / AI Studio"] --> GH["GitHub<br/>fuente versionable"]

    GH --> CB["Cloud Build"]
    CB --> CR["Cloud Run"]
    GH --> FH["Firebase Hosting"]

    GH --> NX["Nexus<br/>Docker / Compose"]
    GH --> DO["DigitalOcean<br/>Nginx / servicios"]

    NX --> ALN["App Launch Nexus<br/>catálogo / navegación"]
    DO --> ALP["App Launch público<br/>catálogo / navegación"]

    ALN --> APPS["Aplicaciones locales o remotas"]
    ALP --> APPS
    CR --> APPS
    FH --> APPS
```

### Lectura del diagrama

- **GitHub** es la fuente versionable.
- **Nexus**, **DigitalOcean**, **Cloud Run** y **Firebase Hosting** son destinos de ejecución o publicación; no son intercambiables.
- **App Launch** es navegación. Una tarjeta puede apuntar a un servicio local, a un hostname protegido por Cloudflare o a un servicio cloud.
- **Cloudflare** no es un runtime de las aplicaciones: aporta publicación, seguridad perimetral e identidad para los servicios seleccionados de Nexus.

## Acceso externo seguro a Nexus

La publicación externa de Nexus usa **un único Cloudflare Tunnel**. El conector `cloudflared` se ejecuta en Nexus y mantiene una conexión saliente; el router doméstico no publica puertos entrantes.

```mermaid
flowchart TB
    U["Usuario externo"] --> C["Cloudflare DNS y HTTPS"]
    C --> A["Access: política del hostname"]
    A <--> G["Google IdP"]
    A --> T["Tunnel replicant-launch"]
    T --> F["cloudflared en Nexus"]
    F --> L["Launch y documentación"]
    F --> S["Salones, Pádel y Red"]
    F --> E["Cartera: 8085, OIDC y PIN"]
    F --> W["CryptoWallet: 8516 y previa 8517"]
```

El orden lógico es **HTTPS/DNS → Access → Google IdP → política Access → Tunnel → origen Nexus**. El Tunnel transporta tráfico; **no autentica usuarios**.

Cada hostname tiene una aplicación y una política Access independientes. Compartir el mismo Tunnel no implica compartir autorización.

| Servicio Nexus | Hostname externo | Origen |
|---|---|---|
| App Launch | `launch.thereplicantlab.com` | `http://localhost:80` |
| Salones AV | `salones.thereplicantlab.com` | `http://192.168.18.220:8081` |
| Replicant Lab | `docs.thereplicantlab.com` | `http://192.168.18.220:8082` |
| Reserva Pistas UTP | `padel.thereplicantlab.com` | `http://192.168.18.220:8083` |
| Control de Red | `red.thereplicantlab.com` | `http://192.168.18.220:8084` |
| Cartera Estratégica | `cartera.thereplicantlab.com` | `http://192.168.18.220:8085` |
| CryptoWallet producción | `cryptowallet.thereplicantlab.com` | `http://127.0.0.1:8516` |
| CryptoWallet previa | `cryptowallet-preview.thereplicantlab.com` | `http://127.0.0.1:8517` |

## LAN y host físico

```mermaid
flowchart TB
    subgraph LAN["LAN 192.168.18.0/24"]
        R["Replicant<br/>Windows 11 Pro<br/>192.168.18.200"]
        N["Nexus<br/>Ubuntu 24.04 LTS<br/>192.168.18.220"]
        R -->|Hyper-V| N
        N --> NR["Docker / servicios internos"]
        NR --> CE["Cartera Estratégica v2.0.0<br/>Streamlit :8085 · LAN + origen Tunnel"]
        CE --> DB["SQLite privada real<br/>CARTERA_DB_PATH"]
        API["API oficial Indexa"] --> CE
    end

    GH["GitHub<br/>fuente versionable"] --> N
    GH --> DO["DigitalOcean<br/>servicios públicos"]
    GH --> GC["Google Cloud<br/>Cloud Run / Firebase"]
```

Los accesos LAN por IP y puerto permanecen independientes de Cloudflare Access. No se ha introducido HTTPS interno ni un DNS local nuevo. Cartera Estratégica v2.0.0 se ejecuta en Nexus, mantiene su bind LAN `:8085` y se publica por el Tunnel solo mediante `cartera.thereplicantlab.com`. App Launch `:80` enlaza el acceso protegido y la ficha técnica; no ejecuta la app. La SQLite montada es la base privada real aunque su archivo se llame `cartera-demo.db`.

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
    NX --> NURL["Enlaces internos o hostnames Access"]
```

El catálogo se selecciona durante el despliegue. Cada host recibe únicamente su `apps.json`; la lógica visual es común.

## Responsabilidades

| Elemento | Responsabilidad |
|---|---|
| Replicant | Estación principal Windows, desarrollo local, Hyper-V y administración |
| Nexus | Laboratorio Linux, Docker, servicios internos y origen de servicios publicados mediante Tunnel |
| GitHub | Código, configuración versionable e histórico |
| DigitalOcean | Servicios públicos 24×7 y App Launch público |
| Google Cloud Run | Producción canónica de Consumos Cupra |
| Firebase Hosting | Producción pública del CV |
| Cloudflare DNS / HTTPS | Entrada pública y terminación HTTPS de los hostnames del Lab |
| Cloudflare Access | Autorización independiente por aplicación/hostname |
| Google IdP | Autenticación de identidad para Access |
| Cloudflare Tunnel | Transporte saliente seguro entre Cloudflare y Nexus |
| App Launch | Catálogo y navegación hacia aplicaciones locales o remotas |
| Cartera Estratégica | v2.0.0 privada en Nexus `:8085`; SQLite real, Google OAuth + PIN y cuenta Indexa desde su API oficial |
| `/opt/data`, `/opt/secrets`, `/opt/backups` | Datos, secretos y copias fuera de Git |

!!! important "Reglas de lectura"
    `Checkout ≠ Runtime` · `Tarjeta App Launch ≠ Runtime local` · `Tunnel ≠ Autenticación`.

Docker es el patrón preferido para servicios internos de Nexus cuando encaja, no un requisito universal para todas las aplicaciones.

## Estado actual de seguridad externa

**Implementado:** Cloudflare Tunnel con seis hostnames históricos y producción/previa CryptoWallet. Google como IdP y separación de políticas documentadas en el despliegue histórico. Los nuevos accesos redirigen a Access sin sesión; no se infiere de esa respuesta el contenido administrativo actual de sus políticas. Cartera añade además Google OIDC interno y PIN de seis cifras.

**Pendiente operativo general:** validar desde móvil cada aplicación protegida y añadir monitorización/alertas del Tunnel. La actualización del catálogo Cartera v2.0.0 se documenta por separado.

Authentik queda como evolución opcional futura; no forma parte del runtime actual.

La guía operativa y de recuperación está en [Cloudflare Tunnel](red/cloudflare-tunnel.md).

## Producción privada CryptoWallet

Nexus ejecuta V1.5 cerrada con origen localhost `8516`, datos reales independientes y ningún montaje sintético. La previa localhost `8517` permanece separada. Manual y modelo financiero en el repositorio privado; [ficha de infraestructura](aplicaciones/cryptowallet.md). PIN activo con persistencia 24 horas, privacidad inicial ON y copias locales multibase; Google OIDC interno preparado y OFF. La réplica Drive es una propuesta independiente. La actualización documental no toca operaciones ni runtimes financieros.
