# Arquitectura

## Modelo general

```mermaid
flowchart TB
    subgraph LAN["LAN 192.168.18.0/24"]
        O2["Router O2<br/>Gateway / DHCP<br/>192.168.18.1"]
        M["Linksys Mesh<br/>modo bridge"]
        R["Replicant<br/>192.168.18.200<br/>Windows 11 Pro"]
        N["Nexus<br/>192.168.18.220<br/>Ubuntu 24.04 LTS"]
        O2 --> M
        O2 --> R
        R -->|Hyper-V + switch externo| N
    end

    GH["GitHub<br/>source of truth"]
    DO["DigitalOcean<br/>app.raulatienza.com"]

    GH -->|clone / pull| N
    GH -->|deploy| DO
    N -->|Docker| APPS["Aplicaciones locales"]
```

## Reparto de responsabilidades

| Elemento | Responsabilidad |
|---|---|
| Replicant | Puesto de trabajo, UI, Hyper-V y administración del lab |
| Nexus | Ejecución local de servicios Linux y contenedores |
| GitHub | Código, configuración versionable e histórico |
| DigitalOcean | Servicios públicos o que necesiten disponibilidad 24x7 |
| `/opt/data` | Persistencia local |
| `/opt/secrets` | Secretos y configuración privada fuera de Git |
| `/opt/backups` | Copias; política aún pendiente |

## Regla arquitectónica

!!! success "Regla base"
    Si una necesidad puede resolverse como contenedor sin ensuciar el host, se prefiere Docker. El host Ubuntu se mantiene deliberadamente pequeño.

## Qué no se instala por defecto

- DNS local.
- Reverse proxy.
- Portainer, Cockpit o Webmin.
- Fail2ban mientras SSH permanezca restringido a la LAN.
- Suites de monitorización complejas.
- Automatización de backups hasta definir política.
