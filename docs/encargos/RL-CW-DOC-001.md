# RL-CW-DOC-001 · Documentación de CryptoWallet V1.0

## Estado

`in_progress` · fuentes actualizadas, validación y publicación documental en curso.

## Repositorios

- Infraestructura canónica: `ratienza/infra-replicant-lab` (público).
- Producto/funcionalidad: `ratienza/cryptowallet` (privado).
- Base de infraestructura: `cc6a33cd7fbab6669ed5c633ccf3468a21670550`.
- Base de producto: `2dd0eab5d820fa3ea98cd7054bc87885738c4e56`.
- Ramas: `docs/cryptowallet-v1-documentation` y `docs/v1-documentation`.

## Objetivo y alcance

Petición de Raúl tras aceptar V1.0: documentación completa del artefacto y de The Replicant Lab, respetando esquemas/formato existentes. Manual, arquitectura/datos, operación/recuperación, Cloudflare, inventarios, catálogo documental, decisiones, pendientes y Change Log. HTML/PDF globales y fichas individuales desde MkDocs canónico.

## Autorización y límites

Raúl indica «adelante» después de comprobar accesos y acordar actualización de repositorios y publicación documental en Nexus. Alcance técnico: ramas, PRs/checks, integración y reconstrucción exclusiva del sitio documental. No modifica datos financieros, imagen funcional, Access, Tunnel, secretos ni runtimes de aplicaciones. El tag funcional V1.0 no se desplaza.

## Evidencia inicial

- CryptoWallet productiva y previa saludables; imagen aprobada y binds localhost 8516/8517.
- Tag V1.0, PR funcional #3 fusionado y documentación de cierre.
- 339 pruebas e integridad verificadas durante promoción.
- Docs Nginx 8082 responde HTTP 200; checkout Nexus limpio en SHA base.
- Cloudflared activo/habilitado; URLs CryptoWallet redirigen a Access sin sesión.
- Apps_Lauch #15 fusionado y catálogo servido con enlaces protegidos.
- No hay acceso administrativo al panel Cloudflare comprobado en este encargo; no se infieren políticas actuales desde HTTP 302.

## Criterios y verificación

- Documentación vigente coherente con código/runtime, historial sin reabrir CW-004.
- Sin información financiera ni secretos en el repositorio público.
- Importación V2 y demás límites diferenciados de funciones aceptadas.
- Pipeline oficial generate/check, panel ErasmusHomes check sin actualizar su roadmap, enlaces y Mermaid.
- Revisión visual del PDF y ficha, git diff --check, CI y construcción de imagen documental.
- Tras integración, sitio y descargas servidas comparados con Git; CryptoWallet permanece sin recreación.

## Recuperación

Revertir el cambio documental mediante Git y reconstruir únicamente la imagen Nginx de documentación. No afecta a las bases ni revierte la release financiera.

## Resultado

Se registra al concluir validación y publicación. Las referencias PR/CI y SHA de entrega se mantienen también en el cierre Git; el contenido generado usa huella de fuentes para evitar autorreferencias variables.
