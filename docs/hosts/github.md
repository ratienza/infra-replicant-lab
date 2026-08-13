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
| `ratienza/Apps_Lauch` | Catálogo público e interno de aplicaciones |
| `ratienza/Consumos_Cupra` | Aplicación de consumos desplegada en Cloud Run |
| `ratienza/CV-Raul-IA-Estudio-Google-` | Fuente del CV publicado en Firebase Hosting |
| `ratienza/control-red` | Herramienta local de inventario de red |

Cada aplicación conserva en su propio repositorio su código, configuración reproducible y documentación funcional. Este repositorio solo mantiene la visión de infraestructura y las diferencias comprobadas entre entornos.

Un checkout no prueba que exista un runtime, y un trigger conectado a GitHub no se considera producción si la cadena real no está demostrada.
