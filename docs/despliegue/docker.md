# Despliegue · Docker

## Patrón

```text
GitHub
  ↓
/opt/apps/<repo>
  ↓
compose.yml
  ↓
docker compose up -d
  ↓
servicio
```

## Buenas prácticas del lab

- Preferir imágenes oficiales.
- Minimizar paquetes instalados en el host.
- Persistencia fuera del contenedor.
- Secretos fuera de Git.
- Publicar solo puertos necesarios.
- Cuando proceda, ligar puertos a `192.168.18.220` en vez de `0.0.0.0`.
- No añadir paneles de administración si no resuelven un problema real.

## Operación estándar

```bash
cd /opt/apps/<proyecto>
git switch main
git pull
docker compose up -d
```
