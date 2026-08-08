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

## Convención de puertos en Nexus

Los servicios web locales se asignan de forma secuencial para que el mapa sea fácil de recordar y mantener.

| Puerto | Servicio | Estado |
|---:|---|---|
| `8080` | Launch-pad de Nexus | Reservado |
| `8081` | Salones AV | Operativo |
| `8082` | Replicant Lab · documentación | Operativo |
| `8083` | Reserva-Pistas-UTP · staging | Operativo |
| `8084+` | Próximos servicios | Asignación secuencial |

Reglas:

- `8080` queda reservado como puerta de entrada del laboratorio y futuro launch-pad.
- A partir de `8081`, los servicios se numeran consecutivamente salvo necesidad técnica justificada.
- Cada nuevo servicio debe quedar documentado aquí al asignar su puerto.
- Siempre que sea posible, publicar el servicio ligado a `192.168.18.220` y no a `0.0.0.0`.

## Reserva-Pistas-UTP · staging actual

La aplicación Python sigue escuchando sin cambios en `127.0.0.1:8765`. Para las pruebas en Nexus se utiliza un Nginx temporal en Docker con `--network host`, que publica `192.168.18.220:8083` y reenvía al backend local.

UFW permite `8083/tcp` solo desde `192.168.18.0/24`.

Este montaje es deliberadamente de staging: permite validar la app en Linux sin modificar producción ni el código de negocio antes de formalizar el despliegue definitivo.

## Operación estándar

```bash
cd /opt/apps/<proyecto>
git switch main
git pull
docker compose up -d
```
