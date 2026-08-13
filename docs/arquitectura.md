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
    N <-->|"Reserva-Pistas · sincronización bajo demanda · SSH restringido"| DO
```

## App Launch multientorno

```mermaid
flowchart TD
    A["Código común<br/>index.html + estilos + scripts"] --> B["Despliegue público"]
    A --> C["Despliegue Nexus"]

    D["catalogs/public.json<br/>Apps públicas"] --> B
    E["catalogs/nexus.json<br/>Apps internas"] --> C

    B --> F["VPS DigitalOcean<br/>app.raulatienza.com"]
    C --> G["Nexus local<br/>192.168.18.220"]

    F --> H["apps.json público"]
    G --> I["apps.json Nexus"]

    H --> J["El navegador muestra<br/>solo apps públicas"]
    I --> K["El navegador muestra<br/>apps internas y públicas"]
```

El catálogo se selecciona durante el despliegue. Cada host recibe únicamente su `apps.json`; la lógica visual no contiene bifurcaciones por entorno.

## Reparto de responsabilidades

| Elemento | Responsabilidad |
|---|---|
| Replicant | Puesto de trabajo, UI, Hyper-V y administración del lab |
| Nexus | Ejecución local de servicios Linux y contenedores |
| GitHub | Código, configuración versionable e histórico |
| DigitalOcean | App Launch público, Reservas, Consumos y copia estática de Salones |
| Google Cloud / Firebase | Producción del CV; no depende de Nexus |
| `/opt/data` | Persistencia local |
| `/opt/secrets` | Secretos y configuración privada fuera de Git |
| `/opt/backups` | Copias; política aún pendiente |

## Regla arquitectónica

!!! success "Regla base"
    Si una necesidad puede resolverse como contenedor sin ensuciar el host, se prefiere Docker. El host Ubuntu se mantiene deliberadamente pequeño.

## Qué no se instala por defecto

- Un servidor DNS local. Replicant usa aliases puntuales en su archivo `hosts`.
- Reverse proxy.
- Portainer, Cockpit o Webmin.
- Fail2ban mientras SSH permanezca restringido a la LAN.
- Suites de monitorización complejas.
- Automatización de backups hasta definir política.
