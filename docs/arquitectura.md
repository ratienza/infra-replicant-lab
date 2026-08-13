# Arquitectura

## Modelo general

```mermaid
flowchart TB
    subgraph LAN["LAN 192.168.18.0/24"]
        R["Replicant<br/>Windows 11 Pro<br/>192.168.18.200"]
        N["Nexus<br/>Ubuntu 24.04 LTS<br/>192.168.18.220"]
        R -->|Hyper-V| N
        N --> NR["Docker / servicios internos"]
        NR --> NAL["App Launch Nexus"]
    end
    GH["GitHub<br/>fuente versionable"]
    DO["DigitalOcean<br/>Nginx / servicios públicos"]
    DAL["App Launch público"]
    GC["Google Cloud<br/>Cloud Run / Firebase"]
    GH --> N
    GH --> DO
    GH --> GC
    DO --> DAL
    NAL --> LINKS["Enlaces locales y remotos"]
    DAL --> LINKS
    LINKS --> GC
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
