# Replicant Lab

Documentación viva de la infraestructura local y cloud del laboratorio.

!!! info "Objetivo"
    Mantener una visión única, entendible y versionada de **concepto, hosts, red, seguridad, Git, Docker y operación**. La documentación funcional de cada aplicación vive en su propio repositorio.

> Las versiones portables se descargan desde el icono **⬇ Descargas** de la cabecera, junto al selector claro/oscuro.

## Arquitectura de un vistazo

<div class="replicant-architecture" style="overflow-x:auto; margin:1rem 0;">
<svg viewBox="0 0 1100 470" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Arquitectura Replicant Lab" style="width:100%; min-width:760px; height:auto;">
  <defs>
    <marker id="arrow-index" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#667085"/>
    </marker>
  </defs>
  <style>
    .rb{fill:#fff;stroke:#52728d;stroke-width:2}.rt{font:700 20px sans-serif;fill:#173f65}.rs{font:14px sans-serif;fill:#475467}.rl{stroke:#667085;stroke-width:2;marker-end:url(#arrow-index)}
  </style>
  <rect x="35" y="35" width="210" height="90" rx="14" class="rb"/>
  <text x="140" y="70" text-anchor="middle" class="rt">Router O2</text>
  <text x="140" y="98" text-anchor="middle" class="rs">192.168.18.1 · GW / DHCP</text>
  <rect x="330" y="35" width="210" height="90" rx="14" class="rb"/>
  <text x="435" y="70" text-anchor="middle" class="rt">Linksys Mesh</text>
  <text x="435" y="98" text-anchor="middle" class="rs">Bridge · Wi-Fi / capa 2</text>
  <rect x="35" y="205" width="240" height="110" rx="14" class="rb"/>
  <text x="155" y="242" text-anchor="middle" class="rt">Replicant</text>
  <text x="155" y="270" text-anchor="middle" class="rs">Windows 11 Pro · 192.168.18.200</text>
  <text x="155" y="294" text-anchor="middle" class="rs">Hyper-V · puesto de trabajo</text>
  <rect x="360" y="205" width="240" height="110" rx="14" class="rb"/>
  <text x="480" y="242" text-anchor="middle" class="rt">Nexus</text>
  <text x="480" y="270" text-anchor="middle" class="rs">Ubuntu 24.04 · 192.168.18.220</text>
  <text x="480" y="294" text-anchor="middle" class="rs">Docker · Git · UFW</text>
  <rect x="790" y="35" width="245" height="90" rx="14" class="rb"/>
  <text x="912" y="70" text-anchor="middle" class="rt">GitHub</text>
  <text x="912" y="98" text-anchor="middle" class="rs">Código + configuración versionable</text>
  <rect x="790" y="205" width="245" height="110" rx="14" class="rb"/>
  <text x="912" y="242" text-anchor="middle" class="rt">DigitalOcean</text>
  <text x="912" y="270" text-anchor="middle" class="rs">app.raulatienza.com</text>
  <text x="912" y="294" text-anchor="middle" class="rs">Servicios públicos / 24×7</text>
  <rect x="360" y="380" width="240" height="70" rx="14" class="rb"/>
  <text x="480" y="410" text-anchor="middle" class="rt">Docker Apps</text>
  <text x="480" y="435" text-anchor="middle" class="rs">Salones AV · Reserva Pistas · futuras apps</text>
  <line x1="245" y1="80" x2="330" y2="80" class="rl"/>
  <line x1="140" y1="125" x2="150" y2="205" class="rl"/>
  <line x1="275" y1="260" x2="360" y2="260" class="rl"/>
  <line x1="790" y1="105" x2="600" y2="225" class="rl"/>
  <line x1="912" y1="125" x2="912" y2="205" class="rl"/>
  <line x1="600" y1="260" x2="790" y2="260" class="rl"/>
  <line x1="480" y1="315" x2="480" y2="380" class="rl"/>
</svg>
</div>

> La portada usa **SVG nativo**, no Mermaid. Así evitamos que una incompatibilidad del parser pueda romper la vista principal.

## Principios

- **Minimalismo:** pocas piezas y cada una con una función clara.
- **Git como fuente de verdad:** código y configuración versionable viven en GitHub.
- **Separación:** Windows para trabajo interactivo; Ubuntu para servicios; cloud para disponibilidad pública/24x7.
- **Persistencia fuera de Git:** datos, secretos y backups no se mezclan con repositorios.
- **Seguridad práctica:** SSH por clave, UFW y puertos publicados de forma explícita.
- **Reproducibilidad:** un host debe poder reconstruirse sin depender de cambios manuales no documentados.

## Estado actual

| Componente | Estado |
|---|---|
| Replicant | ✅ Operativo |
| Nexus | ✅ Operativo |
| SSH por clave | ✅ Operativo |
| UFW | ✅ Activo |
| Docker / Compose | ✅ Operativo |
| GitHub desde Nexus | ✅ Operativo |
| Salones AV | ✅ Observada en Nexus · `8081` |
| Replicant Lab en Nexus | ✅ Runtime Nginx estático validado · `8082` |
| Reserva-Pistas-UTP | ✅ Validada y observada en Nexus · `8083` |
| Cartera Estratégica | ✅ MVP local en Replicant · no desplegada en Nexus |
| Reserva-Pistas histórico en Nexus | ⏳ Pendiente de sincronizar desde DigitalOcean |
| Producción DigitalOcean | ⚠️ Documentada desde Git; no validada en esta reconciliación |
| Backups | ⏳ Pendiente |
| DNS local | ⏳ Pendiente |

## Cómo usar esta documentación

- **Arquitectura** explica cómo encajan las piezas.
- **Fases** conserva el recorrido y las decisiones que llevaron al estado actual.
- **Hosts** describe cada máquina.
- **Red** documenta direccionamiento e inventario.
- **Despliegue** fija los patrones Git/Docker.
- **Aplicaciones** contiene solo la ficha de infraestructura de cada app.
- **Operación** concentra comandos y procedimientos cortos.
- **Pendientes** conserva el estado y los encargos que deben retomarse sin depender de memoria de chat.
- **Decisiones** registra criterios que no conviene redescubrir cada vez.

Los estados distinguen entre contenido **implementado en Git**, **probado localmente**, **validado u observado en Nexus** y **validado en producción**. Una evidencia de un entorno no se extrapola a otro.
