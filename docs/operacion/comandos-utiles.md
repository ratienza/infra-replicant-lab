# Operación · Comandos útiles

## Host

```bash
ip addr
ip route
sudo ss -tulpn
```

## Firewall

```bash
sudo ufw status verbose
```

## Docker

```bash
docker ps
docker compose up -d
docker compose down
docker compose logs
```

## Git

```bash
git status
git switch main
git pull
```

## Actualizaciones

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
```

## Filosofía

Este documento evita convertirse en un recetario infinito. Solo se incluyen comandos frecuentes y útiles para operar el lab.

## Cloudflare Tunnel (solo consulta)

```bash
cloudflared --version
systemctl is-active cloudflared
systemctl is-enabled cloudflared
systemctl status cloudflared --no-pager
curl -I http://localhost:80/
curl -I https://launch.thereplicantlab.com/
```

No incluir tokens en comandos compartidos. Instalar, vincular, actualizar, reiniciar o eliminar `cloudflared` requiere un encargo operativo específico.
