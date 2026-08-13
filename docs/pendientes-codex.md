# Pendientes

No hay incidencias críticas abiertas en Salones AV, Consumos Cupra o CV. Las fases 2A, 2B y 2C están cerradas.

## Activos

- Continuar Cartera Estratégica como siguiente bloque de producto.

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
