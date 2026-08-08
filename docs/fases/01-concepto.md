# Fase 01 · Concepto

## Objetivo

Construir un laboratorio doméstico sencillo para desarrollar y ejecutar aplicaciones sin mezclar estación de trabajo, servidor y cloud.

## Decisiones

- **Replicant** permanece como equipo Windows de trabajo.
- Se crea una VM Linux dedicada: **Nexus**.
- GitHub será la fuente de verdad para código/configuración.
- Docker será la capa de ejecución estándar en Linux.
- DigitalOcean se reserva para servicios públicos/24x7.
- Los datos sensibles pueden permanecer solo en local.

## Resultado

Se define una arquitectura híbrida con separación clara entre **desarrollo**, **ejecución local**, **control de versiones** y **cloud**.
