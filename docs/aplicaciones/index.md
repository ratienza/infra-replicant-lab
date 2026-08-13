# Aplicaciones

Vista operativa compacta. Cada nombre abre su ficha técnica completa.

| Aplicación | Objetivo | Stack / herramienta | Repositorio | Deploy / runtime | Estado |
|---|---|---|---|---|---|
| [App Launch](app-launch.md) | Catálogo de acceso | HTML/CSS/JS · Codex | `ratienza/Apps_Lauch` | Scripts · Nginx en Nexus y DigitalOcean | Operativo |
| [Salones AV](salones-av.md) | Guía audiovisual | HTML · Codex | `ratienza/salones-av-valencia-palace` | Compose · Nexus `8081` | Cerrado / operativo |
| [Reserva-Pistas-UTP](reserva-pistas-utp.md) | Reservas de pádel | Python/Flask · Codex | `ratienza/Reserva-Pistas-UTP` | Compose + systemd/Nginx · Nexus y DigitalOcean | Operativo |
| [Consumos Cupra](consumos-cupra.md) | Registro y análisis de consumos | React/Vite/Express · AI Studio + Codex | `ratienza/Consumos_Cupra` | Cloud Build · Cloud Run | Cerrado / operativo |
| [CV de Raúl](cv-raul.md) | CV y portfolio público | Vite/Tailwind · AI Studio | `ratienza/CV-Raul-IA-Estudio-Google-` | Firebase Hosting | Operativo / POST-CARTERA |
| [Control de Red](control-red.md) | Inventario de LAN | PowerShell · Codex | `ratienza/control-red` | Local · Replicant | Operativo local / POST-CARTERA |
| [Cartera Estratégica](cartera-estrategica.md) | Gestión de inversión | Python/Streamlit · Codex | `ratienza/cartera-estrategica` | Local · Replicant | MVP operativo |
| [Replicant Lab](replicant-lab.md) | Manual vivo del laboratorio | MkDocs/Mermaid · Codex | `ratienza/infra-replicant-lab` | Compose · Nexus `8082` | Operativo |

## Lectura correcta

- Un checkout en Nexus puede ser solo una copia de consulta.
- App Launch enlaza aplicaciones; una tarjeta no acredita runtime local.
- Los detalles de build, persistencia, seguridad, pruebas, rollback y deuda viven en cada ficha.
