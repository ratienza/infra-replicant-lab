# Pendientes

Visión mantenible del estado de los repositorios GitHub vinculados a Raul Lab. Corte comprobado: **09/08/2026**. GitHub aporta commits y PR; las afirmaciones de ejecución proceden de la documentación versionada o de validaciones de entorno indicadas expresamente.

## Leyenda

- ✅ **Terminado:** alcance documentado cerrado.
- 🟢 **Operativo:** existe una forma de uso o despliegue documentada; no implica validación viva de producción.
- 🧪 **En desarrollo:** producto utilizable con fases abiertas.
- ⏳ **Pendiente:** existe trabajo real documentado.
- ⛔ **Bloqueado:** no puede avanzar sin una decisión o dependencia externa.

## Estado conjunto

| Repositorio y finalidad | Estado actual | Último hito y trabajo terminado | Pendientes reales y siguiente acción | PR |
|---|---|---|---|---|
| [`infra-replicant-lab`](https://github.com/ratienza/infra-replicant-lab)<br>Gestor canónico de infraestructura y operación de Raul Lab. | ✅ **Terminado y operativo en Nexus** | Pipeline reproducible, MkDocs canónico, Nginx estático, HTML/PDF completos y validación real en Nexus. | Sin pendientes documentales tras esta corrección final. DNS local y backups generales continúan como pendientes de infraestructura, fuera de este cierre. | Abiertos: ninguno al iniciar la corrección.<br>Último fusionado: [#10](https://github.com/ratienza/infra-replicant-lab/pull/10), registro de validación de Nexus. |
| [`Reserva-Pistas-UTP`](https://github.com/ratienza/Reserva-Pistas-UTP)<br>Automatización de reservas de pádel. | 🟢 **Operativo en Nexus**; producción descrita, no revalidada aquí. | [PR #3](https://github.com/ratienza/Reserva-Pistas-UTP/pull/3): despliegue Docker Compose reproducible para Nexus. | Promoción controlada y sincronización segura del estado vivo desde DigitalOcean, solo mediante encargo explícito. Decidir el destino del PR borrador #1. | Abierto: [#1 borrador](https://github.com/ratienza/Reserva-Pistas-UTP/pull/1), acceso y disponibilidad por Telegram.<br>Último fusionado: #3. |
| [`salones-av-valencia-palace`](https://github.com/ratienza/salones-av-valencia-palace)<br>Documentación operativa AV del SH Valencia Palace. | 🟢 **Operativo en Nexus** con una deriva conocida. | [PR #1](https://github.com/ratienza/salones-av-valencia-palace/pull/1): Compose con Nginx; HTML y recursos operativos versionados. | Reconciliar en su repositorio el bind LAN observado en Nexus y completar la revisión final de escritorio, móvil e impresión A4 indicada en su contexto. | Abiertos: ninguno.<br>Último fusionado: #1. |
| [`cartera-estrategica`](https://github.com/ratienza/cartera-estrategica)<br>MVP privado de control y análisis de cartera. | 🧪 **Operativo local y en desarrollo**, versión documentada `v1.2.0`. | [PR #17](https://github.com/ratienza/cartera-estrategica/pull/17): estabilización del arranque privado. Fases 0–7B y libro de cash integrados. | Fase 8, pruebas y endurecimiento; Fase 9, publicación privada. La Fase 7C permanece fuera del MVP vigente. | Abiertos: ninguno.<br>Último fusionado: #17. |
| [`CV-Raul-IA-Estudio-Google-`](https://github.com/ratienza/CV-Raul-IA-Estudio-Google-)<br>CV web generado desde Google AI Studio. | 🧪 **En desarrollo/desplegable**; no hay validación viva registrada aquí. | Último cambio: Dockerfile y configuración Nginx; incluye aplicación Vite y PDF generado. | No hay un pendiente ni siguiente encargo versionado en README. | Abiertos: ninguno.<br>Sin PR fusionados; último cambio directo `38c9fe7`. |
| [`Apps_Lauch`](https://github.com/ratienza/Apps_Lauch)<br>Launchpad público de aplicaciones. | 🟢 **Operativo según README**; producción no revalidada aquí. | Último cambio: la tarjeta del CV apunta a Cloud Run; despliegue y verificación están documentados. | No hay pendiente versionado. La siguiente acción dependerá de incorporar o cambiar una aplicación enlazada. | Abiertos: ninguno.<br>Sin PR fusionados; último cambio directo `98149fa`. |
| [`Consumos_Cupra`](https://github.com/ratienza/Consumos_Cupra)<br>Aplicación de control de consumos de combustible. | 🧪 **En desarrollo/desplegable**; no hay validación viva registrada aquí. | Último cambio: soporte para despliegue bajo la ruta `consumos`; incluye PWA, servidor y Docker Compose. | No hay pendiente ni siguiente encargo versionado en README. | Abiertos: ninguno.<br>Sin PR fusionados; último cambio directo `050535f`. |
| [`control-red`](https://github.com/ratienza/control-red)<br>Panel local de inventario y escaneo de red. | 🟢 **Operativo local según README**. | Primera versión del panel PowerShell, lanzador local e inventario persistente. | No hay pendiente ni siguiente encargo versionado. Cualquier cambio debe proteger el inventario y snapshots existentes. | Abiertos: ninguno.<br>Sin PR fusionados; último cambio directo `0e285d2`. |

## Exclusión expresa

[`ratienza/python`](https://github.com/ratienza/python) no forma parte de Raul Lab y se excluye de esta visión.

## Reglas de mantenimiento

1. Consultar GitHub antes de cambiar estados, PR o hitos.
2. No convertir documentación de despliegue en validación viva.
3. No presentar como pendiente lo ya cerrado.
4. Registrar “sin pendiente documentado” cuando GitHub y el repositorio no definan una siguiente acción.
5. Mantener separados código, secretos, bases, históricos y datos vivos de cada aplicación.
