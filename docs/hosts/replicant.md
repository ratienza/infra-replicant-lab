# Host · Replicant

| Campo | Valor |
|---|---|
| Host | Replicant |
| Rol | Estación de trabajo + host Hyper-V |
| SO | Windows 11 Pro |
| IP | `192.168.18.200` |
| Gateway | `192.168.18.1` |
| Virtualización | Hyper-V |
| Switch | `Replicant Ethernet` |
| Acceso | Sesión local de Windows o Escritorio remoto: `mstsc /v:replicant` |

## Responsabilidades

- Herramientas interactivas: ChatGPT, Codex, Gemini y similares.
- Administración de Nexus.
- Hyper-V.
- Punto de entrada SSH hacia Nexus y DigitalOcean.

## Criterio

No convertir Replicant en servidor por comodidad si el servicio puede vivir limpiamente en Nexus.
