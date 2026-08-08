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
| `8083+` | Próximos servicios | Asignación secuencial |

Reglas:

- `8080` queda reservado como puerta de entrada del laboratorio y futuro launch-pad.
- A partir de `8081`, los servicios se numeran consecutivamente salvo necesidad técnica justificada.
- Cada nuevo servicio debe quedar documentado aquí al asignar su puerto.
- Siempre que sea posible, publicar el servicio ligado a `192.168.18.220` y no a `0.0.0.0`.

## Operación estándar

```bash
cd /opt/apps/<proyecto>
git switch main
git pull
docker compose up -d
```
