# Aplicaciones

Catálogo operativo del laboratorio. Cada ficha técnica se abre como documento HTML independiente y autocontenido.

<style>
.app-catalog { display:grid; grid-template-columns:repeat(auto-fit,minmax(270px,1fr)); gap:1rem; margin:1.2rem 0; }
.app-card { display:flex; flex-direction:column; gap:.55rem; padding:1.05rem; border:1px solid var(--md-default-fg-color--lightest); border-radius:.7rem; background:var(--md-code-bg-color); }
.app-card h2 { margin:0; font-size:1.2rem; }
.app-card p { margin:0; }
.app-card dl { display:grid; grid-template-columns:max-content 1fr; gap:.22rem .65rem; margin:.25rem 0; font-size:.82rem; }
.app-card dt { font-weight:700; }
.app-card dd { margin:0; }
.app-card .tech-link { margin-top:auto; padding-top:.45rem; font-weight:700; }
</style>

<div class="app-catalog" markdown>

<article class="app-card" markdown>
## App Launch
Catálogo de acceso a aplicaciones públicas e internas.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>HTML, CSS, JavaScript</dd><dt>Repositorio</dt><dd><code>ratienza/Apps_Lauch</code></dd><dt>Deploy</dt><dd>Scripts por destino</dd><dt>Runtime</dt><dd>Nginx · Nexus y DigitalOcean</dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/app-launch.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Salones AV
Guía operativa audiovisual para los salones del Valencia Palace.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>HTML, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/salones-av-valencia-palace</code></dd><dt>Deploy</dt><dd>Docker Compose</dd><dt>Runtime</dt><dd>Nexus · <code>8081</code></dd><dt>Estado</dt><dd>Cerrado / operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220:8081/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/salones-av.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Reserva-Pistas-UTP
Gestión y programación de reservas de pistas de pádel.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>Python, Flask, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/Reserva-Pistas-UTP</code></dd><dt>Deploy</dt><dd>Compose + systemd/Nginx</dd><dt>Runtime</dt><dd>Nexus y DigitalOcean</dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="https://app.raulatienza.com/padel/">Producción</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/reserva-pistas-utp.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Consumos Cupra
Registro y análisis de consumos de combustible.

<dl><dt>Herramienta</dt><dd>AI Studio + Codex</dd><dt>Stack</dt><dd>React, Vite, Express</dd><dt>Repositorio</dt><dd><code>ratienza/Consumos_Cupra</code></dd><dt>Deploy</dt><dd>Cloud Build</dd><dt>Runtime</dt><dd>Google Cloud Run</dd><dt>Estado</dt><dd>Cerrado / operativo</dd></dl>

<p class="tech-link"><a href="../downloads/apps/consumos-cupra.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## CV de Raúl
Currículum y portfolio profesional público.

<dl><dt>Herramienta</dt><dd>AI Studio</dd><dt>Stack</dt><dd>Vite, Tailwind, PDFKit</dd><dt>Repositorio</dt><dd><code>ratienza/CV-Raul-IA-Estudio-Google-</code></dd><dt>Deploy</dt><dd>Firebase Hosting</dd><dt>Runtime</dt><dd>Firebase</dd><dt>Estado</dt><dd>Operativo / POST-CARTERA</dd><dt>URL</dt><dd><a href="https://cv.raulatienza.com">Producción</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/cv-raul.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Control de Red
Inventario y revisión de dispositivos de la red local.

<dl><dt>Herramienta</dt><dd>PowerShell + Codex</dd><dt>Stack</dt><dd>PowerShell</dd><dt>Repositorio</dt><dd><code>ratienza/control-red</code></dd><dt>Deploy</dt><dd>Ejecución local</dd><dt>Runtime</dt><dd>Replicant</dd><dt>Estado</dt><dd>Operativo local / POST-CARTERA</dd></dl>

<p class="tech-link"><a href="../downloads/apps/control-red.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Cartera Estratégica
Gestión y análisis de una cartera personal de inversión.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>Python, Streamlit, SQLite</dd><dt>Repositorio</dt><dd><code>ratienza/cartera-estrategica</code></dd><dt>Deploy</dt><dd>Ejecución local</dd><dt>Runtime</dt><dd>Replicant</dd><dt>Estado</dt><dd>MVP operativo</dd></dl>

<p class="tech-link"><a href="../downloads/apps/cartera-estrategica.html">Ver ficha técnica</a></p>
</article>

<article class="app-card" markdown>
## Replicant Lab
Manual vivo de infraestructura, despliegue y operación del laboratorio.

<dl><dt>Herramienta</dt><dd>Codex</dd><dt>Stack</dt><dd>MkDocs, Mermaid, Nginx</dd><dt>Repositorio</dt><dd><code>ratienza/infra-replicant-lab</code></dd><dt>Deploy</dt><dd>Docker Compose</dd><dt>Runtime</dt><dd>Nexus · <code>8082</code></dd><dt>Estado</dt><dd>Operativo</dd><dt>URL</dt><dd><a href="http://192.168.18.220:8082/">Nexus</a></dd></dl>

<p class="tech-link"><a href="../downloads/apps/replicant-lab.html">Ver ficha técnica</a></p>
</article>

</div>

`Checkout ≠ Runtime` y `Tarjeta App Launch ≠ Runtime local`.
