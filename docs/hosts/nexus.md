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
| `53` | systemd-resolved | localhost |
