# Fase 03 · Nexus

## Objetivo

Crear un servidor Linux local, estable y mínimo.

## VM

- Hyper-V Gen2.
- Ubuntu Server 24.04.4 LTS.
- Aproximadamente 4 vCPU.
- Aproximadamente 6 GB de RAM dinámica.
- VHDX dinámico de 150 GB.

## Red

- Interfaz: `eth0`.
- MAC virtual: `00:15:5d:12:7b:00`.
- IP fija: `192.168.18.220/24`.
- Gateway: `192.168.18.1`.
- Netplan: `/etc/netplan/99-nexus-static.yaml` con permisos `600`.

## Acceso

SSH por clave desde Replicant mediante el alias `nexus`.

## Resultado

Nexus queda independiente del DHCP para su dirección y preparado para convertirse en host de servicios.
