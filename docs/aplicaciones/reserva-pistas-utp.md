# Reserva-Pistas-UTP

Ficha de infraestructura de la aplicación de reservas de pádel de Torre de Porta-Coeli.

La documentación funcional y de negocio permanece en el repositorio de la aplicación: `ratienza/Reserva-Pistas-UTP`. Esta ficha describe exclusivamente cómo se despliega y opera dentro de Replicant Lab y cómo se diferencia de producción.

## Estado

| Elemento | Valor |
|---|---|
| Repositorio | `ratienza/Reserva-Pistas-UTP` |
| Nexus | ✅ Operativo en Docker Compose |
| Ruta Nexus | `/opt/apps/Reserva-Pistas-UTP` |
| URL LAN | `http://192.168.18.220:8083` |
| Backend interno Docker | `app:8765` |
| Datos persistentes Nexus | `/opt/data/reserva-pistas` |
| Producción | DigitalOcean |
| URL producción | `https://app.raulatienza.com/padel/` |
| Producción modificada durante la adaptación | No |

## Arquitectura Nexus

La versión de Nexus se ejecuta completamente en Docker Compose con dos servicios:

```text
Replicant / LAN
      ↓
192.168.18.220:8083
      ↓
reserva-pistas-nginx
      ↓
red privada Docker
      ↓
app:8765
      ↓
reserva-pistas-app
      ↓
/app/data
      ↓ bind mount
/opt/data/reserva-pistas
```

Solo Nginx publica un puerto hacia la LAN. El backend Python no se publica directamente.

### Servicio `app`

- Imagen propia construida desde `Dockerfile` sobre `python:3.12-slim`.
- Ejecuta `python app.py`.
- Escucha en `0.0.0.0:8765` dentro del contenedor mediante variables de entorno.
- Ejecuta con UID/GID `1000:1000`, evitando crear datos persistentes como `root`.
- Usa `restart: unless-stopped`.

### Servicio `nginx`

- Imagen oficial `nginx:alpine`.
- Publica `192.168.18.220:8083 -> 80/tcp`.
- Resuelve el backend mediante el nombre de servicio Docker `app:8765`.
- Usa `restart: unless-stopped`.

## Qué aprendimos del montaje

La primera prueba se hizo con Python ejecutado manualmente en Nexus y un Nginx temporal con `--network host`. Sirvió para validar compatibilidad Linux sin tocar producción, pero no era un despliegue autónomo.

El montaje definitivo elimina esa dependencia manual:

1. `Dockerfile` empaqueta el backend Python.
2. `compose.yml` define backend y proxy como una sola aplicación desplegable.
3. Compose crea una red privada y registra los nombres de servicio.
4. Nginx puede resolver `app` sin conocer una IP fija del contenedor.
5. Solo Nginx publica `8083` en la LAN.
6. El estado vive fuera de los contenedores.
7. Docker reinicia ambos servicios automáticamente después de reiniciar Nexus.

## Configuración por entorno

`app.py` conserva compatibilidad con el despliegue previo usando valores por defecto y permite cambiar el comportamiento mediante variables de entorno:

```text
APP_HOST
APP_PORT
APP_DATA_DIR
```

Valores por defecto:

```text
APP_HOST=127.0.0.1
APP_PORT=8765
APP_DATA_DIR=.
```

En Nexus, Compose define:

```text
APP_HOST=0.0.0.0
APP_PORT=8765
APP_DATA_DIR=/app/data
```

Esto permite que el mismo código sirva para distintos entornos sin mantener dos variantes de `app.py`.

## Persistencia

Los datos locales no forman parte de la imagen ni del repositorio Git.

En Nexus:

```text
/opt/data/reserva-pistas
        ↓
/app/data
```

El bind mount contiene los ficheros de estado/configuración local que la aplicación utiliza:

```text
credentials.local.json
notifications.local.json
tasks.local.json
telegram.offset.local
telegram.state.local
```

La persistencia se validó recreando contenedores y comprobando que los datos permanecían disponibles.

## Seguridad y Git

`.gitignore` protege los ficheros locales de la aplicación y `.dockerignore` evita que `.git`, `.venv`, bytecode y ficheros `*.local*` entren en el contexto de construcción de Docker.

Los secretos, credenciales, estado y datos reales permanecen fuera de Git.

## Firewall

UFW permite `8083/tcp` exclusivamente desde la LAN:

```text
8083/tcp    ALLOW    192.168.18.0/24
```

Regla aplicada:

```bash
sudo ufw allow from 192.168.18.0/24 to any port 8083 proto tcp
```

## Operación Nexus

### Arranque / actualización

```bash
cd /opt/apps/Reserva-Pistas-UTP
git switch main
git pull
docker compose up -d --build
```

### Estado

```bash
docker compose ps
```

### Logs

```bash
docker logs reserva-pistas-app --tail 50
docker logs reserva-pistas-nginx --tail 50
```

### Reinicio

```bash
docker compose restart
```

### Parada completa

```bash
docker compose down
```

Los contenedores usan `restart: unless-stopped`; tras un reinicio del host, Docker recupera automáticamente ambos servicios sin necesidad de ejecutar Compose manualmente.

## Validaciones realizadas

- Imagen Python construida correctamente.
- Backend ejecutado dentro de Docker con UID/GID `1000:1000`.
- Comunicación `nginx -> app` mediante red privada de Compose.
- `GET /` responde HTTP `200` en `http://192.168.18.220:8083/`.
- Interfaz cargada correctamente desde Replicant.
- Bind mount `/opt/data/reserva-pistas:/app/data` validado.
- Persistencia conservada después de recrear contenedores.
- `restart: unless-stopped` validado.
- Reinicio completo de Nexus validado: la aplicación vuelve a quedar operativa automáticamente.

## Diferencias Nexus / producción

| Aspecto | Nexus / Lab | DigitalOcean / Producción |
|---|---|---|
| Objetivo | Desarrollo, prueba, staging y ejecución controlada | Servicio público 24x7 |
| Backend | Contenedor `reserva-pistas-app` | Python gestionado por `systemd` |
| Proxy | Contenedor `reserva-pistas-nginx` | Nginx del host |
| Entrada | `192.168.18.220:8083` | `https://app.raulatienza.com/padel/` |
| Acceso | LAN | Internet + HTTPS + Basic Auth |
| Persistencia | `/opt/data/reserva-pistas` | Ficheros locales privados en `/opt/reserva-pistas/` |
| Git | Misma base de código | Misma base de código tras promoción controlada |
| Disponibilidad | Depende de Replicant/Nexus | 24x7 |

Nexus puede ejecutar reservas reales porque usa el mismo código y puede disponer de credenciales válidas, pero no debe competir simultáneamente con producción sobre las mismas tareas.

## Estado de `tasks.local.json`

La aplicación no utiliza una base SQL: el histórico, programaciones y estado operativo se conservan principalmente en `tasks.local.json`.

Antes de considerar Nexus plenamente sincronizado con producción, debe copiarse de forma controlada el `tasks.local.json` vigente de DigitalOcean.

Regla obligatoria:

1. DigitalOcean es la fuente del estado vivo actual hasta la sincronización.
2. Obtener el `tasks.local.json` más reciente de producción.
3. Validar integridad y conservar el histórico completo.
4. Revisar tareas con estado `queued` o `running`.
5. Si existen, neutralizarlas únicamente en la copia de Nexus antes de activar la ejecución allí.
6. No modificar producción durante esta operación.

## Regla operativa crítica

No ejecutar simultáneamente tareas reales equivalentes en Nexus y DigitalOcean. Ambas instancias podrían intentar reservar la misma pista.

La promoción a producción y la sincronización autónoma del estado quedan dentro del encargo específico de Codex para esta aplicación.
