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

El inventario actual añade a los seis hostnames históricos los dos entornos CryptoWallet: producción y previa. Sus orígenes escuchan solo en localhost `8516/8517`; no ofrecen acceso directo por IP LAN. **Cloudflare Access + Google IdP están implantados** y cada hostname dispone de una aplicación y política Access independientes.

El acceso por IP privada sigue siendo independiente: Cloudflare protege la ruta externa, no la LAN.

Cartera Estratégica conserva su acceso LAN en `http://192.168.18.220:8085` y además se publica en `https://cartera.thereplicantlab.com` mediante el mismo Tunnel. La ruta pública atraviesa Cloudflare Access y, dentro de Cartera, Google OIDC y PIN; App Launch enlaza ahora el hostname protegido y su ficha; la ruta LAN sigue disponible por separado.
