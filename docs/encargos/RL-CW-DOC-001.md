# RL-CW-DOC-001 · Documentación de CryptoWallet V1.0

## Estado

`done` · documentación implementada, probada, integrada y primera publicación verificada el 08/10/2026. Este registro final incorpora esa evidencia y se publica mediante el mismo flujo Git.

## Repositorios y coordinación

| Repositorio | Rama inicial / PR | Integración inicial | Validación |
|---|---|---|---|
| infra-replicant-lab · público | docs/cryptowallet-v1-documentation · [#49](https://github.com/ratienza/infra-replicant-lab/pull/49) | c0757ed634530e5eb666ffc0cbbe2d48a2815c29 | [CI 37756509480](https://github.com/ratienza/infra-replicant-lab/actions/runs/37756509480) correcto; Nexus verificado |
| cryptowallet · privado | docs/v1-documentation · [#4](https://github.com/ratienza/cryptowallet/pull/4) | 10cca54272685fe7da099f192afc0399ad2611a9 | Enlaces/exclusiones/diff correctos; sin workflow activado para este cambio documental |

Bases iniciales: infraestructura `cc6a33cd7fbab6669ed5c633ccf3468a21670550`; producto `2dd0eab5d820fa3ea98cd7054bc87885738c4e56`. Rama de cierre `docs/cryptowallet-v1-documentation-close`: registra publicación real y mantiene derivados sincronizados; las referencias definitivas de esta integración están en su PR.

## Objetivo y alcance

Petición de Raúl tras aceptar V1.0: documentación completa del artefacto y de The Replicant Lab, respetando esquemas/formato existentes. Manual, arquitectura/datos, operación/recuperación, Cloudflare, inventarios, catálogo documental, decisiones, pendientes y Change Log. HTML/PDF globales y fichas individuales desde MkDocs canónico.

## Autorización y límites

Raúl indica «adelante» después de comprobar accesos y acordar actualización de repositorios y publicación documental en Nexus. Ramas, PRs/checks, integración y reconstrucción exclusiva del sitio documental. No modifica datos financieros, imagen funcional, Access, Tunnel, secretos ni runtimes de aplicaciones. El tag funcional V1.0 no se desplaza.

La regla de entornos se aclara en AGENTS: Nexus puede alojar producción privada expresamente aprobada por aplicación. No autoriza trasladar otras producciones ni desplegar nuevas apps. Las futuras sesiones deben cargar las instrucciones vigentes.

## Resultado documental

- Nueva petición posterior de Raúl: pantalla de revisión de operaciones más informativa, siguiendo Cartera Estratégica, con antes/después. Solo anotada en ambos repositorios, sin implementación. CryptoWallet [PR #5](https://github.com/ratienza/cryptowallet/pull/5) conserva esa nota y el cierre de HANDOFF.
- Guías V1.0 en el repositorio privado; README vigente e historia subordinada sin reabrir CW-004.
- Ficha pública sin bases, importes, originales, capturas, credenciales ni ubicaciones privadas de copias.
- Importación funcional CSV/Excel y reconciliación V2 separadas de operaciones/cosmética ya aceptadas.
- Once fichas más dossier global: doce parejas HTML/PDF; primera generación de 120 páginas globales y ficha CryptoWallet de tres.
- Enlaces cruzados portables apuntan al sitio canónico, no a rutas de la máquina.
- Se corrige el pendiente antiguo Apps_Lauch #15: fusionado y enlaces protegidos observados. Metadatos de su tarjeta CryptoWallet quedan como ajuste separado.

## Verificación registrada

Panel ErasmusHomes `check` correcto, sin refrescar su roadmap. Pipeline oficial `generate --screenshots` y `check` correctos: 42 rutas de navegador, 17 Mermaid, navegación móvil y descargas. Revisión visual de PDFs y comprobación de límites de texto sin desbordamientos; `git diff --check` limpio. CI reproduce dependencias fijadas, construcción Docker y Nginx/descargas.

Primera publicación desde `main@c0757ed`: **58 rutas de navegación con HTTP 200 y 25 descargas idénticas byte a byte a Git** (las doce parejas y el roadmap PDF existente). Reconstrucción/recreación exclusiva de documentación. Identidad, imagen y arranque de los demás contenedores intactos; huellas de las SQLite productivas de CryptoWallet sin cambios, producción y previa saludables.

Ambos hostnames CryptoWallet redirigen a Access sin sesión; cloudflared activo/habilitado. No se inspeccionó el panel administrativo de políticas ni se certifica una nueva prueba móvil autenticada. Esos controles operativos permanecen abiertos.

## Recuperación y continuidad

La imagen documental anterior se conserva para recuperación controlada. Reversión permanente por Git/PR y reconstrucción exclusiva de Nginx; jamás recuperar o sobrescribir bases financieras para revertir documentación.

El cierre incorpora los resultados anteriores, regenera los derivados y vuelve a comprobar CI/publicación. La huella de fuentes visible en HTML/PDF identifica el contenido final, sin autorreferencias al SHA que contiene ese mismo documento. V1.0 funcional permanece cerrada; futuros desarrollos requieren encargo de Raúl.
