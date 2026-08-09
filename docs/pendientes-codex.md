# Pendientes Codex

Esta página conserva encargos reales y discrepancias comprobadas. Los estados distinguen Git, prueba local, Nexus y producción; una validación no se extrapola a otro entorno.

## Reglas de trabajo

- Leer `AGENTS.md`, comprobar `origin/main`, el working tree y la documentación vigente antes de actuar.
- Trabajar en el repositorio propio de cada aplicación sin mezclar código ni contexto entre proyectos.
- Separar código/configuración reproducible de secretos, datos e históricos vivos.
- Registrar como hechos solo lo implementado o validado con evidencia; identificar expresamente el entorno.
- Promover o modificar producción únicamente por encargo explícito.
- Regenerar HTML/PDF mediante el pipeline versionado cuando cambie materialmente la fuente MkDocs.

## Encargos

| Nº | Encargo | Estado | Criterio de cierre |
|---:|---|---|---|
| 1 | Contrato operativo raíz | ✅ Completado | `AGENTS.md` integrado mediante PR #7. |
| 2 | Reserva-Pistas-UTP · promoción controlada a producción | ⏳ Nexus validado; producción pendiente | Encargo explícito, sincronización segura de estado vivo, promoción y verificación final en DigitalOcean. |
| 3 | Portables reproducibles de Replicant Lab | ✅ Completado y validado en Nexus | HTML y PDF completos generados desde MkDocs, descargados del servicio y comparados byte a byte con Git. |
| 4 | Reconciliar el bind de Salones AV | ⏳ Pendiente en repo de la app | El bind LAN queda versionado o se revierte deliberadamente; checkout de Nexus limpio y acorde con `main`. |
| 5 | Alinear runtime y CI de Replicant Lab | ✅ Completado y validado en Nexus | Dockerfile, Compose y CI usan build MkDocs estricto y Nginx estático; servicio desplegado y estable. |
| 6 | Activar y validar Mermaid | ✅ Completado y validado en Nexus | Mermaid fijado y local; cinco diagramas verificados en web, HTML y PDF. |
| 7 | Desplegar y validar el sistema documental 2B.1 | ✅ Completado | PR #9 fusionado, reconstrucción controlada en Nexus y validación integral realizada el 09/08/2026. |

## Encargo 2 · Reserva-Pistas-UTP

Antes de cualquier activación o promoción real:

1. obtener de DigitalOcean el `tasks.local.json` más reciente sin modificar producción;
2. validar el JSON, conservar el histórico y revisar tareas `queued` y `running`;
3. neutralizar riesgos de duplicación solo en la copia de Nexus si fuera necesario;
4. preservar credenciales, notificaciones y estado Telegram fuera de Git;
5. impedir ejecución real simultánea equivalente en Nexus y producción;
6. promover únicamente código/configuración ya validado;
7. verificar servicio, logs, acceso y salud en el entorno final.

## Encargo 7 · Cierre del gestor documental

El 09/08/2026 se completó el ciclo aprobado:

1. se verificaron el head aprobado, los checks y la ausencia de revisiones pendientes del PR #9;
2. se fusionó mediante squash y se sincronizaron los checkouts local y de Nexus;
3. se reconstruyó y recreó exclusivamente `infra-replicant-lab` con `docker compose up -d --build`;
4. se comprobó Nginx en `192.168.18.220:8082`, su estabilidad y sus logs;
5. se verificaron navegación, recursos, cinco Mermaid y ambas descargas;
6. se compararon byte a byte los artefactos servidos con Git;
7. se validaron el HTML offline y el PDF completo, sin clientes de desarrollo ni dependencias esenciales externas.

DigitalOcean y los repositorios, contenedores y datos de las aplicaciones quedan fuera de esta validación.
