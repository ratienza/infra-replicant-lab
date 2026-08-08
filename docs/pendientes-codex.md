# Pendientes Codex

Esta página es el backlog operativo de encargos que deben retomarse con Codex. Su objetivo es que los trabajos pendientes no dependan de la memoria de una sesión o de una conversación.

## Regla de trabajo

- Los encargos se numeran de forma correlativa.
- Cada aplicación modificada y validada en Nexus tendrá su propio encargo independiente para Codex cuando proceda llevar el cambio a producción.
- Los cambios de producción no se improvisan: Codex debe partir de lo ya probado y documentado.
- El estado de cada encargo debe actualizarse aquí al iniciar, completar o descartar el trabajo.

## Encargos abiertos

| Nº | Encargo | Estado | Criterio de cierre |
|---:|---|---|---|
| 1 | Marco operativo genérico de Replicant Lab | Pendiente | Codex entiende la arquitectura, roles, repositorios, Nexus/DigitalOcean, flujo Git, datos/secretos y dispone de un contrato operativo tipo `AGENTS.md` para trabajar desde cualquier máquina sin depender del contexto de chat. |
| 2 | Reserva-Pistas-UTP · promover a producción lo validado en Nexus | Pendiente de validar staging | La versión probada en Nexus se formaliza en Git y Codex la lleva a DigitalOcean sin alterar datos privados ni tareas de producción; se verifican servicio, logs y salud antes de cerrar. |

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

## Encargo 2 · Reserva-Pistas-UTP

Contexto actual:

- Repositorio: `ratienza/Reserva-Pistas-UTP`.
- Producción actual: DigitalOcean, publicada en `https://app.raulatienza.com/padel/`.
- Nexus se utilizará como instancia de staging/pruebas.
- Puerto previsto en Nexus: `8083`.
- Producción no se toca durante las pruebas locales.
- No deben ejecutarse simultáneamente tareas reales equivalentes en Nexus y DigitalOcean para evitar reservas duplicadas.

Secuencia prevista:

1. Adaptar y probar la aplicación exclusivamente en Nexus.
2. Confirmar que la versión staging funciona correctamente.
3. Formalizar en Git exactamente lo validado.
4. Actualizar ficha de aplicación, documentación oficial, HTML offline e informe PDF de Replicant Lab.
5. Entregar a Codex el encargo de promoción a DigitalOcean.
6. Codex despliega únicamente los cambios validados y verifica producción.

## Próximos encargos

Las aplicaciones que se modifiquen antes de retomar Codex se añadirán aquí como encargos `3`, `4`, `5`... cada una por separado.
