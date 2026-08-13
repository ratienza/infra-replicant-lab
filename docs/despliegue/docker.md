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
servicios
```

## Buenas prácticas del lab

- Preferir imágenes oficiales cuando sea razonable.
- Minimizar paquetes instalados en el host.
- Persistencia fuera del contenedor.
- Secretos fuera de Git.
- Publicar solo puertos necesarios.
- Cuando proceda, ligar puertos a `192.168.18.220` en vez de `0.0.0.0`.
- Separar proxy, backend y datos cuando cada pieza tenga una responsabilidad clara.
- Ejecutar los procesos de aplicación con un usuario no root siempre que sea viable.
- Usar `restart: unless-stopped` para servicios que deben recuperarse tras reiniciar Nexus.
- No añadir paneles de administración si no resuelven un problema real.

## Convención de puertos en Nexus

| Puerto | Servicio | Estado |
|---:|---|---|
| `80` | App Launch Nexus | Operativo |
| `8080` | Sin asignar | Libre |
| `8081` | Salones AV | Operativo |
| `8082` | Replicant Lab · documentación | Operativo |
| `8083` | Reserva-Pistas-UTP | Operativo |
| `8084+` | Próximos servicios | Asignación secuencial |

Reglas:

- App Launch usa el puerto estándar `80`, sin puerto explícito en la URL.
- `8080` queda libre y no se reserva para App Launch.
- A partir de `8081`, los servicios se numeran consecutivamente salvo necesidad técnica justificada.
- Cada nuevo servicio debe quedar documentado aquí al asignar su puerto.
- Siempre que sea posible, publicar el servicio ligado a `192.168.18.220` y no a `0.0.0.0`.

App Launch es la excepción deliberada: publica `80` en todas las interfaces de Nexus para actuar como entrada de la LAN. No se publica por HTTPS.

Salones AV aplica explícitamente la regla LAN mediante `192.168.18.220:8081:80`. El PR `salones-av-valencia-palace#2` incorporó el bind a `main`; desde `8c0bc08` el checkout Nexus está limpio y la configuración es reproducible desde GitHub.

## Reserva-Pistas-UTP · patrón validado

Reserva-Pistas utiliza un Compose de dos servicios:

```text
LAN :8083
   ↓
nginx
   ↓
red privada Compose
   ↓
app:8765
```

El backend no publica `8765` hacia el host. Nginx lo alcanza mediante el DNS interno de Docker usando el nombre de servicio `app`.

Los datos se desacoplan del ciclo de vida del contenedor mediante:

```text
/opt/data/reserva-pistas:/app/data
```

La aplicación recibe por entorno:

```text
APP_HOST=0.0.0.0
APP_PORT=8765
APP_DATA_DIR=/app/data
```

El código conserva valores por defecto compatibles con despliegues no Docker.

## Operación estándar

```bash
cd /opt/apps/<proyecto>
git switch main
git pull
docker compose up -d --build
```

Comprobaciones habituales:

```bash
docker compose ps
docker compose logs --tail 50
```

Parada y recreación:

```bash
docker compose down
docker compose up -d
```

Un `down` elimina contenedores y la red del proyecto, pero no debe eliminar datos persistentes alojados fuera del contenedor.

## Autoarranque

Docker Engine arranca con Ubuntu. Los contenedores existentes con `restart: unless-stopped` se recuperan automáticamente después de reiniciar Nexus.

Compose no necesita ejecutarse manualmente durante el arranque para recuperar esos contenedores ya creados; su fichero YAML sigue siendo la definición reproducible para recrearlos o actualizarlos.

## Replicant Lab · sitio estático reproducible

La definición versionada converge en un único modelo:

```text
mkdocs.yml + docs/
        ↓
Dockerfile · MkDocs build --strict
        ↓
sitio estático
        ↓
Nginx :80
        ↓
192.168.18.220:8082
```

`compose.yml` construye el `Dockerfile`, publica únicamente `192.168.18.220:8082 → 80` y no monta fuentes ni ejecuta `mkdocs serve`.

### Actualización desplegada

```bash
cd /opt/apps/infra-replicant-lab
git switch main
git pull --ff-only origin main
docker compose up -d --build
```

Cada cambio documental desplegado requiere reconstruir la imagen porque Nginx sirve la copia estática incluida durante el build. Las dependencias viven en las etapas versionadas; no se instalan en Nexus.

### Separación de estados

El modelo estático está implementado, probado localmente y validado en Nexus. La validación del 09/08/2026 incluyó el contenedor Nginx estable, HTTP y navegación, cinco diagramas Mermaid, descargas reales idénticas a Git, HTML offline y PDF completo. No implica validación en producción.
