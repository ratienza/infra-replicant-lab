# Pendientes

No hay incidencias críticas abiertas en Salones AV, Consumos Cupra o CV. Las fases 2A, 2B y 2C están cerradas.

## Activos

- Continuar Cartera Estratégica como siguiente bloque de producto.

### PULA

- **Crítico antes de cualquier exposición adicional:** autenticar y autorizar la API, bloquear SSRF y sacar contactos y estado vivo de Git.
- **Importante antes de trasladar a DigitalOcean:** definir persistencia, imagen y despliegue reproducibles, secretos, healthcheck, backup/restore y rollback.
- **Calidad:** corregir el falso estado `sent`, añadir tests aislados y CI, fijar runtime y gestor de dependencias y reconciliar `AGENTS.md` con las funciones ya presentes.
- **Mejora:** normalizar extracción, traducción y capacidad de los anuncios SCPU y añadir observabilidad sin datos personales.

PULA está documentada, pero estos puntos son deuda de la aplicación: no están implementados ni validados en Nexus o producción.

## Deuda POST-CARTERA

### CV / Firebase

- Reconciliar Firebase y Cloud Build.
- Retirar o corregir el trigger y la configuración obsoletos.
- Demostrar trazabilidad entre SHA Git y versión Firebase.
- Incorporar lockfile y build reproducible, CI, tests y typecheck.
- Revisar restos React, metadata Gemini y artefactos residuales.
- Revisar cabeceras de seguridad, caché, protección de `main` y UX de revelado de contacto.

### Control de Red

- Hacer backup antes de intervenir.
- Separar inventarios, snapshots y datos operativos reales del código Git.
- Mantener únicamente ejemplos anonimizados en el repositorio.

### Nexus

- Definir una política global de backups y ejecutar una prueba de restauración.
- Inventariar y gestionar los checkouts que son solo copias de consulta.
- Mantener explícito `Checkout ≠ Runtime`; el CV en Nexus no es un despliegue.

## Mejoras opcionales

- Limpiar assets PWA históricos no utilizados de App Launch mediante un cambio versionado y verificable.

La deuda aceptada no debe presentarse como fallo de producción ni reabrir las fases ya cerradas.
