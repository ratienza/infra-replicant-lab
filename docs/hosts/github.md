# Host lógico · GitHub

GitHub no es un host de ejecución del lab, pero sí una pieza de infraestructura crítica porque actúa como **fuente de verdad**.

## Reglas

- Código y configuración versionable viven aquí.
- Cambios relevantes se realizan en rama.
- Se revisan mediante Pull Request.
- `main` representa el estado estable aprobado.
- Datos, bases de datos, `.env`, tokens y claves privadas no se versionan.

## Repos relevantes

| Repo | Función |
|---|---|
| `ratienza/infra-replicant-lab` | Documentación viva de infraestructura |
| `ratienza/salones-av-valencia-palace` | Aplicación AV / PoC Docker |
| `ratienza/cartera-estrategica` | Aplicación de cartera |
| `ratienza/Reserva-Pistas-UTP` | Aplicación de reservas de pádel |

Cada aplicación conserva en su propio repositorio su código, configuración reproducible y documentación funcional. Este repositorio solo mantiene la visión de infraestructura y las diferencias comprobadas entre entornos.
