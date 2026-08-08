# Fase 05 · PoC Salones AV

## Objetivo

Validar el patrón completo con una aplicación real y simple.

## Flujo probado

```mermaid
flowchart LR
    GH[GitHub] --> C[Clone en /opt/apps]
    C --> B[Rama deploy/docker-nginx]
    B --> PR[Pull Request]
    PR --> MAIN[Merge a main]
    MAIN --> PULL[git pull en Nexus]
    PULL --> DC[docker compose up -d]
    DC --> LAN[Servicio visible en la LAN]
```

## Resultado

- Repo: `ratienza/salones-av-valencia-palace`.
- Ruta: `/opt/apps/salones-av-valencia-palace`.
- Imagen: `nginx:alpine`.
- Contenedor: `salones-av`.
- Puerto: `192.168.18.220:8081 → 80/tcp`.
- HTML montado en solo lectura desde `proyecto_html`.

El PoC confirma el patrón **GitHub → Nexus → Docker → LAN**.
