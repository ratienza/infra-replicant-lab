# Reserva-Pistas-UTP

Ficha de infraestructura de la aplicación de reservas de pádel de Torre de Porta-Coeli.

La documentación funcional y de operación específica permanece en el repositorio de la aplicación: `ratienza/Reserva-Pistas-UTP`.

## Estado

| Elemento | Valor |
|---|---|
| Repositorio | `ratienza/Reserva-Pistas-UTP` |
| Nexus | ✅ Staging operativo |
| Ruta Nexus | `/opt/apps/Reserva-Pistas-UTP` |
| URL LAN | `http://192.168.18.220:8083` |
| Backend local | `127.0.0.1:8765` |
| Producción | DigitalOcean |
| URL producción | `https://app.raulatienza.com/padel/` |
| Producción modificada durante la prueba | No |

## Arquitectura actual de staging

La aplicación se ejecuta en Nexus con Python 3.12 dentro de un entorno virtual local. El código original permanece sin modificar y escucha en `127.0.0.1:8765`.

Un Nginx temporal en Docker expone la aplicación en la LAN por `192.168.18.220:8083` usando red de host:

```text
Replicant / LAN
      ↓
192.168.18.220:8083
      ↓
Nginx (Docker, --network host)
      ↓
127.0.0.1:8765
      ↓
Reserva-Pistas-UTP (Python)
```

Esta solución permite validar la aplicación en Nexus sin modificar `app.py` ni tocar la instancia de producción.

## Preparación realizada en Nexus

Se instaló soporte de entornos virtuales Python:

```bash
sudo apt install -y python3.12-venv
```

Dentro del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

La única dependencia directa declarada por la aplicación es `requests`.

## Arranque actual

### 1. Backend Python

```bash
cd /opt/apps/Reserva-Pistas-UTP
source .venv/bin/activate
python app.py
```

El backend queda escuchando en:

```text
http://127.0.0.1:8765
```

### 2. Proxy de staging

El fichero local `nginx-staging.conf` se usa únicamente para las pruebas de Nexus.

El contenedor se arranca con:

```bash
docker run --rm \
  --name reserva-pistas-staging-proxy \
  --network host \
  -v "$PWD/nginx-staging.conf:/etc/nginx/nginx.conf:ro" \
  nginx:alpine
```

El proxy escucha en `192.168.18.220:8083` y reenvía al backend `127.0.0.1:8765`.

## Firewall

UFW permite `8083/tcp` exclusivamente desde la LAN:

```text
8083/tcp    ALLOW    192.168.18.0/24
```

Regla aplicada:

```bash
sudo ufw allow from 192.168.18.0/24 to any port 8083 proto tcp
```

## Validaciones realizadas

- La aplicación arranca en Ubuntu/Nexus sin modificar el código.
- `GET /` responde `HTTP 200` desde `127.0.0.1:8765`.
- Nginx responde `HTTP 200` desde `192.168.18.220:8083`.
- La interfaz web carga correctamente desde Replicant.
- DigitalOcean no se modificó durante estas pruebas.

## Datos y estado

La aplicación no utiliza una base de datos SQL. El histórico, programaciones y estado se almacenan principalmente en:

```text
tasks.local.json
```

Los ficheros privados de credenciales y notificaciones permanecen separados:

```text
credentials.local.json
notifications.local.json
```

### Pendiente Nexus

Existe una tarea específica en el repositorio de la aplicación para copiar a Nexus el `tasks.local.json` actual de DigitalOcean y disponer del mismo histórico/estado.

Antes de arrancar Nexus con esa copia se debe comprobar que no haya tareas `queued` o `running`; si las hubiera, se neutralizarán únicamente en la copia de Nexus para evitar reservas duplicadas. Producción no debe modificarse.

## Producción y Codex

DigitalOcean continúa siendo la instancia definitiva de producción.

La promoción de los cambios validados en Nexus será el **Encargo Codex nº 2**. Codex deberá llevar a producción únicamente lo ya probado, preservando datos privados y verificando servicio, logs y salud antes de cerrar el encargo.

## Regla operativa

No ejecutar simultáneamente tareas reales equivalentes en Nexus y DigitalOcean. Ambas instancias podrían intentar reservar la misma pista.
