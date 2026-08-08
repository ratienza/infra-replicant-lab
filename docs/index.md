# Infra Replicant Lab

Documentación viva de la infraestructura local y cloud del laboratorio.

!!! info "Objetivo"
    Mantener una visión única, entendible y versionada de **concepto, hosts, red, seguridad, Git, Docker y operación**. La documentación funcional de cada aplicación vive en su propio repositorio.

## Arquitectura de un vistazo

```mermaid
flowchart LR
    O2[Router O2\n192.168.18.1] --> MESH[Linksys Mesh\nBridge / Wi-Fi]
    O2 --> R[Replicant\nWindows 11 Pro\n192.168.18.200]
    R -->|Hyper-V| N[Nexus\nUbuntu 24.04 LTS\n192.168.18.220]
    GH[GitHub\nFuente de verdad] --> N
    GH --> DO[DigitalOcean\napp.raulatienza.com]
    N --> D[Docker]
    D --> SA[Salones AV\n8081]
    N --> DATA[/opt/data · /opt/secrets]
```

## Principios

- **Minimalismo:** pocas piezas y cada una con una función clara.
- **Git como fuente de verdad:** código y configuración versionable viven en GitHub.
- **Separación:** Windows para trabajo interactivo; Ubuntu para servicios; cloud para disponibilidad pública/24x7.
- **Persistencia fuera de Git:** datos, secretos y backups no se mezclan con repositorios.
- **Seguridad práctica:** SSH por clave, UFW y puertos publicados de forma explícita.
- **Reproducibilidad:** un host debe poder reconstruirse sin depender de cambios manuales no documentados.

## Estado actual

| Componente | Estado |
|---|---|
| Replicant | ✅ Operativo |
| Nexus | ✅ Operativo |
| SSH por clave | ✅ Operativo |
| UFW | ✅ Activo |
| Docker / Compose | ✅ Operativo |
| GitHub desde Nexus | ✅ Operativo |
| Salones AV | ✅ PoC desplegada |
| Backups | ⏳ Pendiente |
| DNS local | ⏳ Pendiente |
| Reverse proxy | ⏳ Pendiente |

## Cómo usar esta documentación

- **Arquitectura** explica cómo encajan las piezas.
- **Fases** conserva el recorrido y las decisiones que llevaron al estado actual.
- **Hosts** describe cada máquina.
- **Red** documenta direccionamiento e inventario.
- **Despliegue** fija los patrones Git/Docker.
- **Aplicaciones** contiene solo la ficha de infraestructura de cada app.
- **Operación** concentra comandos y procedimientos cortos.
- **Decisiones** registra criterios que no conviene redescubrir cada vez.
