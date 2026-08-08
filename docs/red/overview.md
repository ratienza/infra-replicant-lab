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

Se deja pendiente. Para dos equipos de trabajo, la operación por IP es aceptable y evita añadir una dependencia innecesaria por ahora.
