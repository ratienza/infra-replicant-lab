# Aplicaciones

Catálogo operativo del laboratorio. Cada ficha técnica se abre como documento HTML independiente y autocontenido.

<style>
.app-catalog { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1rem; margin:1.2rem 0; }
.app-card { --card-accent:#2878a8; display:flex; flex-direction:column; gap:.55rem; padding:1.05rem; border:1px solid color-mix(in srgb,var(--card-accent) 35%,var(--md-default-fg-color--lightest)); border-top:3px solid var(--card-accent); border-radius:.7rem; background:var(--md-code-bg-color); }
.app-card:nth-child(4n+2) { --card-accent:#2d8067; }
.app-card:nth-child(4n+3) { --card-accent:#a66528; }
.app-card:nth-child(4n+4) { --card-accent:#6f6aa8; }
.app-card h2 { margin:0; color:var(--card-accent); font-size:1.2rem; }
.app-card p { margin:0; }
.app-card .app-type { color:var(--card-accent); font-size:.72rem; font-weight:800; letter-spacing:.06em; text-transform:uppercase; }
.app-card dl { display:grid; grid-template-columns:max-content 1fr; gap:.22rem .65rem; margin:.25rem 0; font-size:.82rem; }
.app-card dt { font-weight:700; }
.app-card dd { margin:0; }
.app-card .tech-link { margin-top:auto; padding-top:.45rem; font-weight:700; }
</style>

<div class="app-catalog" markdown>

<article class="app-card" markdown>
## App Launch
<p class="app-type">Portal multientorno</p>
Catálogo de acceso a aplicaciones públicas e internas. Se publica en Nexus y DigitalOcean con catálogos distintos por entorno; las tarjetas navegan hacia servicios, pero no constituyen su runtime.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>HTML, CSS, JavaScript</dd><dt>Repositorio</dt><dd><code>ratienza/Apps_Lauch</code></dd><dt>Deploy</dt><dd>Scripts por destino</dd><dt>Runtime</dt><dd>Nginx · Nexus y DigitalOcean</dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/app-launch.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Salones AV
<p class="app-type">Guía operativa</p>
Guía audiovisual para los salones del Valencia Palace. Reúne procedimientos, conexiones, sonido y mapas de apoyo para la operación diaria.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>HTML, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/salones-av-valencia-palace</code></dd><dt>Deploy</dt><dd>Docker Compose</dd><dt>Runtime</dt><dd>Nexus · <code>8081</code></dd><dt>Estado</dt><dd>Cerrado / operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220:8081/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/salones-av.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Reserva-Pistas-UTP
<p class="app-type">Reservas y automatización</p>
Gestiona reservas de pistas de pádel y su programación. Ofrece interfaz web y bot de Telegram para consultar, crear o cancelar operaciones autorizadas.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>Python, Flask, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/Reserva-Pistas-UTP</code></dd><dt>Deploy</dt><dd>Compose + systemd/Nginx</dd><dt>Runtime</dt><dd>Nexus y DigitalOcean</dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="https://app.raulatienza.com/padel/">Producción</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/reserva-pistas-utp.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Consumos Cupra
<p class="app-type">Registro y análisis</p>
Registra y analiza consumos del vehículo, histórico, pendientes y estadísticas. Mantiene la información operativa desde una interfaz web conectada con servicios Google.

<dl><dt>Herramienta</dt><dd>AI Studio + Codex</dd><dt>Stack</dt><dd>React, Vite, Express</dd><dt>Repositorio</dt><dd><code>ratienza/Consumos_Cupra</code></dd><dt>Deploy</dt><dd>Cloud Build</dd><dt>Runtime</dt><dd>Google Cloud Run</dd><dt>Estado</dt><dd>Cerrado / operativo</dd></dl>

<p class="tech-link"><a href="../downloads/apps/consumos-cupra.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## CV de Raúl
<p class="app-type">Perfil profesional</p>
Presenta el currículum y portfolio profesional público. Organiza experiencia, formación y contacto, con una versión descargable en PDF.

<dl><dt>Herramienta</dt><dd>AI Studio</dd><dt>Stack</dt><dd>Vite, Tailwind, PDFKit</dd><dt>Repositorio</dt><dd><code>ratienza/CV-Raul-IA-Estudio-Google-</code></dd><dt>Deploy</dt><dd>Firebase Hosting</dd><dt>Runtime</dt><dd>Firebase</dd><dt>Estado</dt><dd>Operativo / POST-CARTERA</dd><dt>URL</dt><dd><a href="https://cv.raulatienza.com">Producción</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/cv-raul.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Control de Red
<p class="app-type">Inventario local</p>
Descubre e inventaría dispositivos de la red local. Ayuda a revisar direccionamiento, nombres y estado observable desde Replicant.

<dl><dt>Herramienta</dt><dd>PowerShell + Codex</dd><dt>Stack</dt><dd>PowerShell</dd><dt>Repositorio</dt><dd><code>ratienza/control-red</code></dd><dt>Deploy</dt><dd>Ejecución local</dd><dt>Runtime</dt><dd>Replicant</dd><dt>Estado</dt><dd>Operativo local / POST-CARTERA</dd></dl>

<p class="tech-link"><a href="../downloads/apps/control-red.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Cartera Estratégica
<p class="app-type">Análisis financiero</p>
Gestiona y analiza una cartera personal de inversión. Centraliza posiciones, histórico y métricas de seguimiento en una interfaz local.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>Python, Streamlit, SQLite</dd><dt>Repositorio</dt><dd><code>ratienza/cartera-estrategica</code></dd><dt>Deploy</dt><dd>Ejecución local</dd><dt>Runtime</dt><dd>Replicant</dd><dt>Estado</dt><dd>MVP operativo</dd></dl>

<p class="tech-link"><a href="../downloads/apps/cartera-estrategica.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Replicant Lab
<p class="app-type">Documentación operativa</p>
Documenta infraestructura, despliegue y operación del laboratorio. Genera un sitio navegable y versiones portables HTML/PDF desde fuentes Markdown canónicas.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>MkDocs, Mermaid, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/infra-replicant-lab</code></dd><dt>Deploy</dt><dd>Docker Compose</dd><dt>Runtime</dt><dd>Nexus · <code>8082</code></dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220:8082/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/replicant-lab.html">Ver ficha técnica</a></p>
</article>

</div>

`Checkout ≠ Runtime` y `Tarjeta App Launch ≠ Runtime local`.
