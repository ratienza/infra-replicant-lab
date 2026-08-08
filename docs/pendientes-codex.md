# Pendientes Codex

Esta página es el backlog operativo de encargos que deben retomarse con Codex. Su objetivo es que los trabajos pendientes no dependan de la memoria de una sesión o de una conversación.

## Regla de trabajo

- Los encargos se numeran de forma correlativa.
- Cada aplicación modificada y validada en Nexus tendrá su propio encargo independiente para Codex cuando proceda llevar el cambio a producción.
- Los cambios de producción no se improvisan: Codex debe partir de lo ya probado y documentado.
- El estado de cada encargo debe actualizarse aquí al iniciar, completar o descartar el trabajo.
- Antes de actuar sobre una aplicación, Codex debe leer su ficha en `docs/aplicaciones/`, el repositorio propio de la app y el estado de despliegue vigente.
- No debe asumir que una app se despliega igual que otra: cada ficha debe indicar explícitamente host, puertos, Compose/systemd, persistencia, secretos, proxy, datos y diferencias entre Nexus y producción.

## Contrato operativo obligatorio por aplicación

Para **cada app** que Codex toque dentro de Replicant Lab, debe aplicar este ciclo:

1. **Leer la verdad actual**: ficha de `docs/aplicaciones/<app>.md`, `main` del repositorio de la app y documentación de despliegue del lab.
2. **Identificar entornos**: qué corre en Nexus, qué corre en DigitalOcean u otro host y qué instancia es la fuente viva de datos/estado.
3. **Separar código de datos**: código y configuración reproducible en Git; datos, secretos, históricos y credenciales fuera de Git.
4. **Trabajar primero en el entorno acordado**: si el encargo indica Nexus/staging, no modificar producción durante la adaptación.
5. **Validar antes de formalizar**: arranque, red, puertos, persistencia, permisos, reinicio/autoarranque y acceso real de la aplicación.
6. **Cerrar la verdad en Git**: rama lógica → commit → push → PR → merge → `main`.
7. **Actualizar la ficha de la app** con la arquitectura realmente validada, no con una previsión o staging ya descartado.
8. **Actualizar Replicant Lab**: índice de aplicaciones, mapa de puertos, cambios, pendientes Codex y cualquier decisión operativa afectada.
9. **Actualizar y publicar siempre las salidas portables** del lab: `standalone/Replicant-Lab.html` y `standalone/Replicant-Lab.pdf`.
10. **Promover a producción solo por encargo explícito**, preservando datos privados y comprobando servicio, logs y salud al finalizar.

### Regla obligatoria de descargas HTML/PDF

Cada cierre documental debe dejar disponibles **dos descargas reales y vigentes** desde la documentación web:

- **Índice HTML autónomo**: `standalone/Replicant-Lab.html`, autocontenido y utilizable sin servidor una vez descargado.
- **PDF Pro**: `standalone/Replicant-Lab.pdf`, generado con formato profesional y coherente con la documentación vigente.

Requisitos para Codex:

- La portada web (`docs/index.md`) debe mantener botones visibles para descargar ambos artefactos.
- El propio HTML autónomo debe incluir también controles visibles para **descargar/guardar el índice HTML autónomo** y **descargar el PDF Pro**.
- No basta con dejar enlaces: Codex debe comprobar que ambos ficheros existen realmente en `main` y que los enlaces no devuelven 404.
- Cada vez que cambie de forma material la documentación de arquitectura, una ficha de aplicación, el mapa de puertos, operación o pendientes, Codex debe regenerar **HTML + PDF** antes de cerrar el PR.
- El HTML autónomo y el PDF deben reflejar la misma versión/fecha de la documentación.
- Si el PDF todavía no existe o está desactualizado, el trabajo documental **no está cerrado**.

### Regla específica de la documentación de Replicant Lab

La documentación en Nexus (`192.168.18.220:8082`) se sirve ahora con **MkDocs Material en modo `serve` y bind mounts**:

```text
./mkdocs.yml  → /docs/mkdocs.yml
./docs        → /docs/docs
```

Consecuencias para Codex:

- Tras cambios normales en Markdown o `mkdocs.yml`, un `git pull` en `/opt/apps/infra-replicant-lab` es suficiente; MkDocs detecta los cambios y regenera automáticamente.
- **No** debe ejecutar `docker compose up --build` ni reiniciar Docker solo por un cambio documental.
- El contenedor solo debe recrearse si cambia `compose.yml`, la imagen, los mounts o los parámetros de ejecución del propio servicio de documentación.
- Si el contenido Markdown aparece actualizado pero el menú/navigation no, comprobar primero que el contenedor está leyendo el `mkdocs.yml` del host mediante el bind mount antes de tocar más piezas.

Comprobación útil:

```bash
docker inspect infra-replicant-docs --format '{{range .Mounts}}{{println .Source "->" .Destination}}{{end}}'
docker exec infra-replicant-docs sh -c 'grep -A6 "Aplicaciones:" /docs/mkdocs.yml'
```

## Encargos abiertos

| Nº | Encargo | Estado | Criterio de cierre |
|---:|---|---|---|
| 1 | Marco operativo genérico de Replicant Lab | Pendiente | Codex entiende la arquitectura, roles, repositorios, Nexus/DigitalOcean, flujo Git, datos/secretos y dispone de un contrato operativo tipo `AGENTS.md` para trabajar desde cualquier máquina sin depender del contexto de chat. |
| 2 | Reserva-Pistas-UTP · promover a producción lo validado en Nexus | Nexus validado · pendiente promoción/sincronización | Codex sincroniza de forma segura el estado vivo necesario, lleva a DigitalOcean únicamente lo validado en Nexus sin alterar datos privados ni provocar doble ejecución y verifica servicio, logs y salud antes de cerrar. |

## Encargo 1 · Marco operativo genérico

Objetivo: establecer las reglas maestras que cualquier agente de desarrollo/sistemas debe leer antes de modificar infraestructura o aplicaciones.

Debe cubrir como mínimo:

- Product Owner: Raúl.
- Project Manager: Work.
- Desarrollo y sistemas: Codex.
- GitHub como fuente de verdad de código y configuración versionable.
- Nexus como entorno Linux local de desarrollo, pruebas y staging cuando aplique.
- DigitalOcean como entorno de producción para los servicios públicos/24×7 que correspondan.
- Flujo obligatorio: entender contexto → actualizar `main` → rama lógica → cambio → validación → commit/push → PR → revisión → merge → despliegue en host destino.
- No subir secretos, bases privadas ni datos sensibles a Git.
- No asumir que Nexus y DigitalOcean comparten datos o configuración privada.
- Preferir Docker cuando sea razonable y evitar instalar software en el host sin necesidad.
- Actualizar la documentación de Replicant Lab cuando cambie la arquitectura o la operación.
- Mantener una ficha por aplicación con su arquitectura, operación, datos, red, seguridad, despliegue y diferencias por entorno.
- Aplicar la regla de documentación live de Replicant Lab descrita arriba.
- Regenerar y publicar siempre el HTML autónomo y el PDF Pro, verificando sus botones de descarga.

## Encargo 2 · Reserva-Pistas-UTP

Contexto validado actual:

- Repositorio: `ratienza/Reserva-Pistas-UTP`.
- Producción actual: DigitalOcean, publicada en `https://app.raulatienza.com/padel/`.
- Nexus: despliegue Docker Compose validado y operativo en `http://192.168.18.220:8083`.
- Nexus usa dos servicios: `reserva-pistas-app` + `reserva-pistas-nginx` sobre red privada de Compose.
- Solo Nginx publica `192.168.18.220:8083`; el backend queda privado en `app:8765`.
- Persistencia Nexus: `/opt/data/reserva-pistas:/app/data`.
- Backend Nexus ejecutado como UID/GID `1000:1000`.
- Ambos servicios usan `restart: unless-stopped` y el reinicio completo de Nexus ya fue validado.
- Producción no se modificó durante la adaptación.
- No deben ejecutarse simultáneamente tareas reales equivalentes en Nexus y DigitalOcean para evitar reservas duplicadas.

### Sincronización autónoma obligatoria antes de activar Nexus con estado real

Codex debe resolver esta parte de forma autónoma inmediatamente antes de una activación/promoción real:

1. Obtener de DigitalOcean el `tasks.local.json` **más reciente**.
2. Validar que el JSON sea íntegro y conservar el histórico completo.
3. Revisar expresamente tareas en estados `queued` y `running`.
4. Si existen tareas que puedan duplicarse, neutralizarlas **solo en la copia de Nexus** cuando sea necesario para hacerla segura.
5. No modificar el estado de producción para facilitar la sincronización.
6. Mantener DigitalOcean como fuente del estado vivo durante el handover.
7. No arrancar ejecución real en Nexus mientras exista riesgo de doble reserva o doble ejecución.
8. Preservar también credenciales, notificaciones y estado Telegram según corresponda, sin subirlos a Git.
9. Promover a DigitalOcean únicamente los cambios de código/configuración ya validados en Nexus.
10. Verificar al final servicio, logs, acceso y salud antes de considerar cerrado el encargo.

## Próximos encargos

Las aplicaciones que se modifiquen antes de retomar Codex se añadirán aquí como encargos `3`, `4`, `5`... cada una por separado y deberán heredar el **Contrato operativo obligatorio por aplicación** de esta página.
