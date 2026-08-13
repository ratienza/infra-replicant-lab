# Decisiones arquitectónicas

Registro corto de decisiones que no conviene redescubrir.

| Decisión | Motivo |
|---|---|
| Nexus usa IP fija `.220` | Identidad estable del servidor local |
| Replicant usa `.200` | Identidad estable del host físico |
| Aliases locales sin servidor DNS | Replicant resuelve `nexus → 192.168.18.220` y `replicant → 192.168.18.200` mediante `hosts`; no se añade infraestructura DNS |
| Docker como estándar | Mantener limpio el host Ubuntu |
| GitHub como source of truth | Reproducibilidad e histórico |
| Datos y secretos fuera de Git | Seguridad y separación de responsabilidades |
| UFW restringe SSH a LAN | Reducir superficie de exposición |
| No usar Portainer/Webmin/Cockpit por defecto | Evitar complejidad innecesaria |
| Ramas por cambio lógico | Facilitar revisión y mantener `main` estable |
| MkDocs es la fuente documental canónica | `mkdocs.yml`, `docs/` y sus recursos definen contenido, estructura y presentación |
| HTML/PDF son artefactos derivados | Deben sincronizarse mediante un proceso reproducible; nunca prevalecen sobre MkDocs |
| Nexus sirve una imagen estática Nginx | `Dockerfile`, Compose y CI comparten build MkDocs estricto; el despliegue requiere reconstrucción |
| Validación por entorno | Git, prueba local, Nexus y producción son estados distintos y no se extrapolan |
| Dependencias documentales fijadas | Python/Node, MkDocs, Mermaid y Playwright se resuelven desde lockfiles versionados |
| Huella SHA-256 para portables | Evita timestamps variables y permite demostrar sincronía inequívoca con las fuentes |
| PDF tratado como binario | `.gitattributes` anula `diff=astextplain` y conversiones CRLF de Git para Windows |
| Rutas portables únicas | HTML y PDF viven exclusivamente en `docs/downloads/` |
| App Launch usa puerto `80` en Nexus | Permite `http://nexus/` sin puerto explícito; `8080` queda libre |
| App Launch selecciona catálogo al desplegar | Una presentación común y un único `apps.json` activo por host evitan filtrar enlaces internos |
| Checkouts no equivalen a servicios | CV y Control de Red pueden existir en disco de Nexus sin declararse desplegados |
| Fichas técnicas derivadas por aplicación | Cada aplicación tiene HTML/PDF generado desde su Markdown canónico |
| Salones AV liga `8081` a la IP LAN | `192.168.18.220:8081:80` evita publicar el servicio en todas las interfaces y queda versionado desde `8c0bc08` |
| App Launch es navegación, no runtime | Una tarjeta puede apuntar a servicios locales o remotos sin trasladar su ejecución al host del launchpad |
| Consumos Cupra usa Cloud Run | La cadena canónica es GitHub → Cloud Build → Artifact Registry → Cloud Run; DigitalOcean y Nexus no son su producción |
| CV usa Firebase Hosting | La producción observada pertenece al proyecto `replicant-lab`; el Cloud Run placeholder no es producción |
