# Aplicación · Cartera Estratégica

## Estado

Aplicación Python/Streamlit operativa como MVP local en Windows, con versión documental `v1.2.0` y SQLite privada fuera del repositorio. El repositorio de la aplicación registra las fases 0–7B integradas y mantiene pendientes el endurecimiento y una eventual publicación privada.

## Entorno comprobado

El entorno vigente es Replicant/Windows con ejecución local de Streamlit. No existe en la documentación actual de la aplicación una decisión aprobada que convierta Nexus o Docker/Linux en su siguiente destino.

## Consideraciones

- La base privada no debe entrar en Git.
- Tokens como EODHD deben inyectarse como secreto/entorno.
- Los datos de inversión pueden permanecer solo en local.
- Cualquier soporte Docker/Linux o despliegue remoto deberá decidirse e implementarse en el repositorio de la aplicación mediante rama y PR.

!!! note "Pendiente"
    No está desplegada ni validada en Nexus. Tampoco debe presentarse Nexus como objetivo acordado hasta que exista una decisión versionada en el repositorio de la aplicación.
