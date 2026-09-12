# Red · Visión general

## Topología

```mermaid
flowchart LR
    WAN[Internet] --> O2[Router O2\n192.168.18.1]
    O2 --> LM[Linksys Mesh\nbridge]
    O2 --> R[Replicant\n.200]
    R --> N[Nexus VM\n.220]
    LM --> WIFI[Clientes Wi-Fi / IoT]
```

## Convención provisional

| Rango | Uso previsto |
|---|---|
| `.1` | Router / gateway |
| `.2-.19` | Infraestructura de red / mesh |
| `.20-.179` | Clientes, IoT y DHCP general |
| `.180-.199` | Equipos fijos, NAS, impresoras |
| `.200-.219` | Servidores físicos |
| `.220-.239` | VMs / laboratorio |
| `.240-.254` | Reserva futura |

## DNS

No existe servidor DNS local. Replicant mantiene dos aliases puntuales en el archivo `hosts` de Windows:

| Nombre | IP | Uso |
|---|---|---|
| `replicant` | `192.168.18.200` | Escritorio remoto y herramientas del host |
| `nexus` | `192.168.18.220` | SSH y `http://nexus/` |

El alias solo resuelve el nombre. El protocolo, puerto, usuario y credenciales siguen perteneciendo a cada servicio.

## Acceso externo mediante Tunnel

La LAN conserva sus direcciones y puertos actuales. La publicación externa no usa NAT ni port forwarding: `cloudflared` en Nexus mantiene una conexión saliente hacia Cloudflare mediante el Tunnel `replicant-launch`.

Cinco hostnames publican servicios seleccionados de Nexus: Launch, Salones, Docs, Pádel y Control de Red. **Cloudflare Access + Google IdP están implantados** y cada hostname dispone de una aplicación y política Access independientes.

El acceso por IP privada sigue siendo independiente: Cloudflare protege la ruta externa, no la LAN.

Cartera Estratégica se incorpora al inventario LAN en `192.168.18.220:8085`, pero no forma parte todavía de esos hostnames ni del Tunnel. App Launch la enlaza localmente desde `http://192.168.18.220/`.
