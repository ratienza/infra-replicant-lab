# Aplicación · Cartera Estratégica

## Estado

Aplicación Python/Streamlit operativa como MVP local en Windows, con versión documental `v1.2.0` y SQLite privada fuera del repositorio. GitHub `main` estaba en `f2b319dea862469b90eb65fa20f8ae2d8c96875d`; el checkout de trabajo observado en Replicant estaba atrasado en `3be6254` y no se modificó.

## Entorno comprobado

El entorno vigente es Replicant/Windows con ejecución local de Streamlit. No existe en la documentación actual de la aplicación una decisión aprobada que convierta Nexus o Docker/Linux en su siguiente destino.

## Consideraciones

- La base privada no debe entrar en Git.
- Tokens como EODHD deben inyectarse como secreto/entorno.
- Los datos de inversión pueden permanecer solo en local.
- Cualquier soporte Docker/Linux o despliegue remoto deberá decidirse e implementarse en el repositorio de la aplicación mediante rama y PR.

## Arquitectura y funciones verificadas

El núcleo usa Python, SQLite y migraciones versionadas; Streamlit es la presentación. El repositorio incluye importación y conciliación, transacciones, FIFO, cash, backups, exportaciones, datos de mercado EODHD, estrategia 7A e inteligencia SMC 7B. Las credenciales se inyectan por entorno y la base, los backups, XLSX y exportaciones reales quedan fuera de Git.

La actualización debe hacerse únicamente sobre una copia y con backup SQLite verificado antes de migrar. El rollback usa el servicio de restauración y una copia probada; nunca se sustituye la base privada por un fichero del repositorio.

## Pruebas del 13/08/2026

- `pytest --collect-only`: 369 pruebas recogidas.
- La suite aislada avanzó aproximadamente hasta el 58 % sin fallos antes del límite de cinco minutos.
- No se declara la suite completa como validada.
- No se abrió, copió, migró ni modificó la SQLite privada.

!!! note "Pendiente"
    No está desplegada ni validada en Nexus. Tampoco debe presentarse Nexus como objetivo acordado hasta que exista una decisión versionada en el repositorio de la aplicación.
