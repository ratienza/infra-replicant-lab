# Aplicación · Cartera Estratégica

## Estado

Aplicación Python/Streamlit actualmente orientada al entorno local Windows, con SQLite privada fuera del repositorio.

## Objetivo de infraestructura

Adaptarla oficialmente a Linux/Docker **desde el propio repositorio**, evitando parchear Nexus de forma manual.

## Consideraciones

- La base privada no debe entrar en Git.
- Tokens como EODHD deben inyectarse como secreto/entorno.
- Los datos de inversión pueden permanecer solo en local.
- El soporte Docker/Linux debe llegar mediante rama + PR.

!!! note "Pendiente"
    No se considera desplegada en Nexus todavía.
