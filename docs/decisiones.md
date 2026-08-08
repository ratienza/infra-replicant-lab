# Decisiones arquitectónicas

Registro corto de decisiones que no conviene redescubrir.

| Decisión | Motivo |
|---|---|
| Nexus usa IP fija `.220` | Identidad estable del servidor local |
| Replicant usa `.200` | Identidad estable del host físico |
| DNS local se pospone | Con dos equipos de trabajo, las IP son suficientes |
| Docker como estándar | Mantener limpio el host Ubuntu |
| GitHub como source of truth | Reproducibilidad e histórico |
| Datos y secretos fuera de Git | Seguridad y separación de responsabilidades |
| UFW restringe SSH a LAN | Reducir superficie de exposición |
| No usar Portainer/Webmin/Cockpit por defecto | Evitar complejidad innecesaria |
| Ramas por cambio lógico | Facilitar revisión y mantener `main` estable |
