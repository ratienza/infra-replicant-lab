# Host · Nexus

| Campo | Valor |
|---|---|
| Hostname | `nexus` |
| SO | Ubuntu Server 24.04.4 LTS |
| IP | `192.168.18.220/24` |
| Gateway | `192.168.18.1` |
| Interfaz | `eth0` |
| MAC | `00:15:5d:12:7b:00` |
| Plataforma | VM Hyper-V Gen2 |

## Software base

- OpenSSH Server.
- Docker Engine CE.
- Docker Compose.
- Git.
- UFW.
- Nano.
- unattended-upgrades.

## Estructura

```text
/opt/apps      repositorios y aplicaciones
/opt/data      datos persistentes
/opt/backups   copias
/opt/compose   composiciones separadas si hacen falta
/opt/secrets   secretos y .env fuera de Git
```

## Seguridad

!!! success "Estado"
    SSH por clave, UFW activo y actualizaciones automáticas de seguridad habilitadas.

## Puertos conocidos

| Puerto | Uso | Ámbito |
|---|---|---|
| `22/tcp` | SSH | LAN |
| `8081/tcp` | Salones AV | LAN |
| `8082/tcp` | Replicant Lab · Nginx estático | LAN |
| `8083/tcp` | Reserva-Pistas-UTP · Nginx | LAN |
| `53` | systemd-resolved | localhost |

## Estado observado el 10/08/2026

- Docker y `unattended-upgrades` activos.
- Replicant Lab ejecutándose como sitio estático en Nginx, construido desde el `Dockerfile` y publicado en `192.168.18.220:8082 → 80`, sin bind mounts ni servidor de desarrollo.
- Salones AV accesible mediante Nginx en `192.168.18.220:8081`.
- Reserva-Pistas-UTP ejecutándose como backend privado y proxy Nginx en `192.168.18.220:8083`, con autenticación, datos persistentes separados y canal saliente SSH restringido hacia DigitalOcean.

Esta observación confirma el estado del laboratorio privado en esa fecha. DigitalOcean se validó por separado y de forma acotada para el cierre de Reserva-Pistas-UTP; cada repositorio conserva sus definiciones operativas.

## Runtime documental validado en Nexus

El PR #9 fusionado sustituye `mkdocs serve` y los bind mounts por una imagen construida desde el `Dockerfile`: MkDocs estricto en la etapa builder y Nginx estático en runtime, manteniendo `192.168.18.220:8082`. El 09/08/2026 se reconstruyó y recreó exclusivamente este servicio en Nexus y se validaron HTTP, navegación, recursos, cinco diagramas Mermaid y descargas HTML/PDF idénticas byte a byte a los artefactos versionados. El HTML funciona offline sin dependencias esenciales externas y el PDF conserva la documentación completa.