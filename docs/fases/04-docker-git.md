# Fase 04 · Docker y Git

## Docker

Se instala Docker CE desde el repositorio oficial y Docker Compose. El usuario `raul` pertenece al grupo `docker` y puede operar sin `sudo` para comandos Docker.

## Git

Git queda configurado en Nexus con identidad propia. Se genera una clave SSH específica **Nexus → GitHub** y se valida el acceso.

## Estructura `/opt`

```text
/opt/
├── apps/
├── data/
├── backups/
├── compose/
└── secrets/
```

## Seguridad básica

- UFW activo.
- Política: `deny incoming`, `allow outgoing`.
- SSH permitido solo desde `192.168.18.0/24`.
- `unattended-upgrades` activo y habilitado.

## Resultado

Nexus queda listo como host de aplicaciones reproducibles y versionadas.
