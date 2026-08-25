# Evidencias GOV-001

Evidencias generadas desde la rama `agent/gov-001-work-codex-git`, sin despliegue:

- [Página completa en móvil, viewport 390 × 844](gobierno-mobile.png).
- [Página completa, viewport 800 × 900](gobierno-800.png).
- [Página completa, viewport 1024 × 900](gobierno-1024.png).
- [Página completa en escritorio, viewport 1440 × 1000](gobierno-desktop.png).
- [Informe automatizado de navegación, Mermaid, consola y overflow](validacion.json).

El informe registra por viewport el ancho, `clientWidth`, `scrollWidth`, overflow horizontal, límites de cada contenedor y SVG, `viewBox`, límites gráficos, clipping, errores de consola y peticiones/respuestas fallidas. Valida 390, 800, 1024 y 1440 px, exactamente tres Mermaid en GOV-001 y diez en el sitio. Los tres diagramas quedan completos, sin clipping y sin ocultar contenido mediante `overflow: hidden`.
