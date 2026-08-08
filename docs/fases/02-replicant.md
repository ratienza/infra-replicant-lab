# Fase 02 · Replicant

## Objetivo

Preparar el host Windows que aloja Hyper-V y sirve de estación de trabajo principal.

## Configuración consolidada

- Windows 11 Pro.
- 16 GB RAM.
- Intel N100, 4 cores.
- Hyper-V habilitado.
- Switch externo: `Replicant Ethernet`.
- IP fija: `192.168.18.200`.
- Gateway: `192.168.18.1`.

## Rol

Replicant concentra las herramientas interactivas y administra los servidores, pero evita asumir cargas de servidor que encajan mejor en Nexus.
