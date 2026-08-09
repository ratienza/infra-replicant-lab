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
| 3 | Portables reproducibles de Replicant Lab | 🧪 Implementado en 2B.1; pendiente merge/Nexus | HTML y PDF completos generados y validados desde MkDocs; cierre de entorno tras despliegue y prueba en Nexus. |
| 4 | Reconciliar el bind de Salones AV | ⏳ Pendiente en repo de la app | El bind LAN queda versionado o se revierte deliberadamente; checkout de Nexus limpio y acorde con `main`. |
| 5 | Alinear runtime y CI de Replicant Lab | 🧪 Implementado en 2B.1; pendiente merge/Nexus | Dockerfile, Compose y CI usan build MkDocs estricto y Nginx estático; validar servicio desplegado. |
| 6 | Activar y validar Mermaid | 🧪 Implementado en 2B.1; pendiente merge/Nexus | Mermaid fijado y local, cinco SVG verificados en web/HTML/PDF; repetir validación visual tras despliegue. |
| 7 | Desplegar y validar el sistema documental 2B.1 | ⏳ Encargo 2B.2 | Merge aprobado, reconstrucción controlada en Nexus, HTTP/descargas/diagramas verificados y rollback disponible. |

## Encargo 2 · Reserva-Pistas-UTP

Antes de cualquier activación o promoción real:

1. obtener de DigitalOcean el `tasks.local.json` más reciente sin modificar producción;
2. validar el JSON, conservar el histórico y revisar tareas `queued` y `running`;
3. neutralizar riesgos de duplicación solo en la copia de Nexus si fuera necesario;
4. preservar credenciales, notificaciones y estado Telegram fuera de Git;
5. impedir ejecución real simultánea equivalente en Nexus y producción;
6. promover únicamente código/configuración ya validado;
7. verificar servicio, logs, acceso y salud en el entorno final.

## Encargo 7 · Paso a 2B.2

El siguiente encargo debe operar exclusivamente sobre el PR 2B.1 aprobado y su commit fusionado:

1. verificar SHA, checks y artefactos;
2. conservar evidencia y rollback del contenedor actual;
3. actualizar el checkout de Nexus sin leer secretos ni datos;
4. ejecutar `docker compose up -d --build`;
5. comprobar Nginx en `192.168.18.220:8082`;
6. verificar las páginas principales, los cinco Mermaid y ambas descargas;
7. comprobar que los ficheros servidos son idénticos a Git y no contienen inyección;
8. actualizar estados documentales únicamente con evidencia de Nexus.
