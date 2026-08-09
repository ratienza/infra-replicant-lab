# Pendientes Codex

Esta página conserva encargos reales y discrepancias comprobadas. Los estados distinguen Git, prueba local, Nexus y producción; una validación no se extrapola a otro entorno.

## Reglas de trabajo

- Leer `AGENTS.md`, comprobar `origin/main`, el working tree y la documentación vigente antes de actuar.
- Trabajar en el repositorio propio de cada aplicación sin mezclar código ni contexto entre proyectos.
- Separar código/configuración reproducible de secretos, datos e históricos vivos.
- Registrar como hechos solo lo implementado o validado con evidencia; identificar expresamente el entorno.
- Promover o modificar producción únicamente por encargo explícito.
- Actualizar la fuente MkDocs del lab cuando cambie su arquitectura u operación.
- Tratar HTML/PDF como artefactos derivados. Su generación obligatoria empezará cuando exista un proceso versionado y reproducible.

## Encargos

| Nº | Encargo | Estado | Criterio de cierre |
|---:|---|---|---|
| 1 | Contrato operativo raíz | ✅ Completado | `AGENTS.md` integrado en `main` mediante PR #7. |
| 2 | Reserva-Pistas-UTP · promoción controlada a producción | ⏳ Nexus validado; producción pendiente | Encargo explícito, sincronización segura de estado vivo, promoción de lo validado y verificación final en DigitalOcean. |
| 3 | Portables reproducibles de Replicant Lab | ⏳ Pendiente | Generador versionado desde MkDocs, HTML offline limpio y PDF completo, rutas canónicas únicas, validación automática y documentación del proceso. |
| 4 | Reconciliar el bind de Salones AV | ⏳ Pendiente en repo de la app | El bind LAN observado en Nexus queda versionado o se revierte de forma deliberada; checkout de Nexus limpio y acorde con `main`. |
| 5 | Alinear runtime y comprobación CI de Replicant Lab | ⏳ Pendiente de decisión | Se documenta y valida si deben coexistir `compose.yml` con MkDocs en vivo y el `Dockerfile` Nginx estático, sin confundir sus funciones. |
| 6 | Activar y validar el renderizado Mermaid | ⏳ Pendiente | Elegir un runtime reproducible, incorporarlo al proyecto MkDocs y verificar visualmente los cinco diagramas; hoy se generan bloques `mermaid` sin librería de renderizado. |

## Encargo 2 · Reserva-Pistas-UTP

Estado comprobado en Nexus:

- `reserva-pistas-app` y `reserva-pistas-nginx` operativos mediante Docker Compose;
- solo Nginx publica `192.168.18.220:8083` y el backend permanece en `app:8765`;
- persistencia en `/opt/data/reserva-pistas:/app/data` y backend con UID/GID `1000:1000`;
- checkout de Nexus limpio y coincidente con `main` del repositorio de la aplicación el 09/08/2026;
- DigitalOcean siguió siendo la fuente del estado vivo y no fue inspeccionado durante la reconciliación documental.

Antes de cualquier activación o promoción real:

1. obtener de DigitalOcean el `tasks.local.json` más reciente sin modificar producción;
2. validar el JSON, conservar el histórico y revisar tareas `queued` y `running`;
3. neutralizar riesgos de duplicación solo en la copia de Nexus si fuera necesario;
4. preservar credenciales, notificaciones y estado Telegram fuera de Git;
5. impedir ejecución real simultánea equivalente en Nexus y producción;
6. promover únicamente código/configuración ya validado;
7. verificar servicio, logs, acceso y salud en el entorno final.

## Encargo 3 · Portables reproducibles

Hechos que debe resolver un encargo separado:

- `docs/downloads/Replicant-Lab.html` y `standalone/Replicant-Lab.html` son copias del mismo resumen autónomo;
- el PDF existente está solo en `docs/downloads/Replicant-Lab.pdf` y resume una página;
- no existe un generador versionado ni `standalone/Replicant-Lab.pdf`;
- el HTML obtenido desde Nexus incorpora el cliente `livereload` de `mkdocs serve`;
- la configuración Git de Windows aplica un filtro de texto al PDF, circunstancia que debe investigarse sin modificar el binario en este encargo;
- la navegación y los botones deben validarse sobre las rutas finales generadas.

Este encargo definirá una única convención de rutas y un pipeline reproducible antes de volver a exigir la regeneración de portables en cada cierre documental.
