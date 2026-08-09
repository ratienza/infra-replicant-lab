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
| `8082/tcp` | Replicant Lab · MkDocs en vivo | LAN |
| `8083/tcp` | Reserva-Pistas-UTP · Nginx | LAN |
| `53` | systemd-resolved | localhost |

## Estado observado el 09/08/2026

- Docker y `unattended-upgrades` activos.
- Replicant Lab ejecutándose con `mkdocs-material:9`, publicación `192.168.18.220:8082 → 8000` y montajes de `mkdocs.yml` y `docs/` en solo lectura.
- Salones AV accesible mediante Nginx en `192.168.18.220:8081`.
- Reserva-Pistas-UTP ejecutándose como backend privado y proxy Nginx en `192.168.18.220:8083`.

Esta observación confirma el estado del laboratorio privado en esa fecha; no valida DigitalOcean ni sustituye las definiciones versionadas de cada repositorio.
## Runtime documental previsto tras 2B.1

La rama 2B.1 sustituye `mkdocs serve` y los bind mounts por una imagen construida desde el `Dockerfile`: MkDocs estricto en la etapa builder y Nginx estático en runtime, manteniendo `192.168.18.220:8082`. Este estado está implementado y probado localmente, pero permanece pendiente de merge, despliegue y validación en Nexus mediante el Encargo 2B.2.