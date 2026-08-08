# Red · Inventario provisional

!!! warning "Estado"
    Inventario de trabajo obtenido del escaneo de agosto de 2026. No se considera una CMDB definitiva y algunos nombres/fabricantes pueden requerir validación posterior.

## Infraestructura y equipos conocidos

| IP | Nombre / función | MAC / fabricante / nota |
|---|---|---|
| `.1` | Router Fibra O2 | `2C-96-82-69-25-F2` · gateway |
| `.3` | RAN-CASA | HP |
| `.4` | Sonos 5 | `5C-AA-FD-0D-54-36` · no visto |
| `.5` | Enchufe Emma | `4C-11-AE-14-10-6E` · IoT |
| `.6` | Keres.local | `14-91-82-8D-8C-6A` · Linksys |
| `.7` | SONOS Cocina | `B8-E9-37-E7-51-2E` |
| `.8` | Enchufe ordenador RAN-CASA | `D4-A6-51-E5-0F-24` · Tuya |
| `.9` | Termostato Nest | `18-B4-30-C4-52-48` |
| `.10` | Sonos Habitación | `B8-E9-37-E1-8E-AE` |
| `.11` | Echo Darío | `F4-03-2A-7B-1B-1B` |
| `.12` | Alexa Comedor | `DC-91-BF-D1-35-B3` |
| `.13` | Linksys13497.local | `14-91-82-8D-8C-B2` · Linksys |
| `.14` | Alexa Despacho | `20-A1-71-00-43-44` |
| `.18` | Play Darío | `0C-FE-45-37-AA-4F` · Sony |
| `.19` | Alexa Cocina | `1C-FE-2B-4F-5A-1B` |
| `.20` | Fire Stick | `34-AF-B3-DE-58-06` |
| `.25` | IoT desconocido | `28-6D-CD-49-AF-28` · no visto |
| `.27` | Lamparita Darío | `28-6D-CD-56-C8-41` |
| `.35` | Lamparita comedor | `28-6D-CD-5D-BD-81` |
| `.42` | Chromecast antiguo | `8A-05-36-D5-F8-2D` · no visto |
| `.44` | Escalera | `40-F5-20-C1-C7-FB` · luces · no visto |
| `.45` | Lamparita comedor escalera | `28-6D-CD-49-AB-D1` |
| `.52` | Enchufe Raúl | `D4-A6-51-E6-94-8B` |
| `.53` | Sebastian - CECOTEC | `44-87-63-97-02-EA` |
| `.54` | Impresora Darío | `28-C5-C8-AB-D7-BE` · HP |
| `.71` | Luz despacho | `CE-CC-5A-B6-E9-BC` · no visto |
| `.74` | Móvil Emma | `76-9D-67-FE-0D-CA` · Samsung · no visto |
| `.82` | Chromecast | `F6-45-CE-C2-7C-F6` |
| `.83` | Móvil Darío | `BA-D8-D1-F2-04-44` · no visto |
| `.94` | Portátil SH | `28-92-00-45-01-CD` · HP · no visto |
| `.101` | Móvil Emma antiguo | `58-02-05-B8-4E-BA` · no visto |
| `.106` | Móvil Raúl | `52-1E-45-1D-FB-AA` |
| `.123` | Antigua IP DHCP de Replicant | `00-E0-4C-4B-35-AD` · migrado a `.200` |
| `.124` | No identificado | `A4-E8-8D-08-12-44` · no visto |
| `.125` | Antigua IP DHCP de Nexus | `00-15-5D-12-7B-00` · migrado a `.220` |
| `.200` | **Replicant** | host físico Windows / Hyper-V · IP fija |
| `.220` | **Nexus** | VM Ubuntu / Docker · IP fija |

## Nota operativa

El inventario sirve para orientación y futuras decisiones de direccionamiento. No se reubicarán dispositivos por estética ni se convertirán en IP fija salvo necesidad concreta.
