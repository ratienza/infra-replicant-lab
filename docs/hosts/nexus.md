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
| Acceso | `ssh raul@nexus` |
| Función | Laboratorio Linux, Docker, servicios internos y copias de consulta |

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
| `80/tcp` | App Launch | LAN |
| `8080/tcp` | Libre | Sin listener |
| `8081/tcp` | Salones AV | LAN |
| `8082/tcp` | Replicant Lab · Nginx estático | LAN |
| `8083/tcp` | Reserva-Pistas-UTP · Nginx | LAN |
| `53` | systemd-resolved | localhost |

## Estado observado el 13/08/2026

- Docker y `unattended-upgrades` activos.
- Replicant Lab ejecutándose como sitio estático en Nginx, construido desde el `Dockerfile` y publicado en `192.168.18.220:8082 → 80`, sin bind mounts ni servidor de desarrollo.
- Salones AV accesible mediante Nginx en `192.168.18.220:8081`; checkout limpio e idéntico a GitHub `main` en `8c0bc08` después de la Fase 2A.
- Reserva-Pistas-UTP ejecutándose como backend privado y proxy Nginx en `192.168.18.220:8083`, con autenticación, datos persistentes separados y canal saliente SSH restringido hacia DigitalOcean.
- App Launch ejecutándose en el puerto `80` mediante Nginx `1.27-alpine`, con sitio y configuración montados en solo lectura.
- `8080` sin listener.
- CV y Control de Red presentes solo como checkouts; no son servicios Nexus.
- Consumos Cupra y Cartera Estratégica sin checkout servido ni puerto Nexus.
- Una tarjeta de App Launch puede apuntar a una aplicación externa; no implica ejecución en Nexus.

Esta observación confirma el estado del laboratorio privado en esa fecha. DigitalOcean se validó por separado y de forma acotada para el cierre de Reserva-Pistas-UTP; cada repositorio conserva sus definiciones operativas.

## Runtime documental validado en Nexus

El PR #9 fusionado sustituye `mkdocs serve` y los bind mounts por una imagen construida desde el `Dockerfile`: MkDocs estricto en la etapa builder y Nginx estático en runtime, manteniendo `192.168.18.220:8082`. El 09/08/2026 se reconstruyó y recreó exclusivamente este servicio en Nexus y se validaron HTTP, navegación, recursos, cinco diagramas Mermaid y descargas HTML/PDF idénticas byte a byte a los artefactos versionados. El HTML funciona offline sin dependencias esenciales externas y el PDF conserva la documentación completa.
