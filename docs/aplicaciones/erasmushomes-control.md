# ErasmusHomes · Control del MVP

<!-- GENERATED: edit ratienza/ErasmusHomes docs/board/roadmap.yaml, never this file -->

<div class="eh-dashboard">
<section class="eh-hero"><p class="eh-kicker">Objetivo diciembre</p><h2>Piloto comercial público antes del 20 de diciembre de 2026</h2><div class="eh-sync eh-sync--synchronized">Sincronizado</div><dl><dt>SHA ErasmusHomes main</dt><dd><code>fe867b64f53febfe7d203718b03c2e5dff31169c</code></dd><dt>Última sincronización</dt><dd>2026-08-23T09:00:09+02:00</dd></dl><div class="eh-agreed-document"><a href="/downloads/erasmushomes/Roadmap_ErasmusHomes_MVP_Diciembre_2026.docx" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (DOCX)</a><span><b>Archivo:</b> Roadmap_ErasmusHomes_MVP_Diciembre_2026.docx</span><span><b>Git:</b> <code>fe867b64</code> · <a href="https://github.com/ratienza/ErasmusHomes/blob/fe867b64f53febfe7d203718b03c2e5dff31169c/docs/source/Roadmap_ErasmusHomes_MVP_Diciembre_2026.docx" target="_blank" rel="noopener noreferrer">ver fuente versionada</a></span><span><b>SHA-256:</b> <code>f4e6be71905f7ed234ebd88a84d9b482b6b464b7fdd7bc4ec7241c29d5cbf36b</code></span><span><b>Fecha:</b> 2026-08-22</span></div></section>
<section class="eh-metrics">
<article><strong>12%</strong><span>completado</span></article>
<article class="eh-metric eh-status--done"><strong>2</strong><span>Completado</span></article>
<article class="eh-metric eh-status--in_progress"><strong>0</strong><span>En ejecución</span></article>
<article class="eh-metric eh-status--pending"><strong>15</strong><span>Pendiente</span></article>
<article class="eh-metric eh-status--blocked"><strong>0</strong><span>Bloqueado</span></article>
</section>
<section class="eh-gate"><h2>Próximo gate</h2>
<p><strong>W-2026-08-31 · Supply y validación</strong><br>Retirar toda ciudad sin tres fuentes viables; no forzar scraper.</p>
</section>
<section><h2>Esta semana</h2><div class="eh-priorities">
<p>No hay tareas en ejecución.</p>
</div></section>
<section><h2>Kanban</h2><div class="eh-kanban">
<div class="eh-column eh-status--done"><h3>Completado · 2</h3>
<article class="eh-task"><span>EH-001</span><h4>Consolidar la fuente de verdad</h4><p><b>Objetivo:</b> Consolidar fuentes, decisiones y alcance en Git y sincronizar Nexus.</p><p><b>Terminado:</b> PR fusionado en main y GitHub, local y Nexus en el mismo SHA.</p><p><b>Riesgos:</b> Divergencia histórica de PDFs ya documentada</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/1">Evidencia</a></p></article>
<article class="eh-task"><span>EH-002</span><h4>Roadmap canónico y panel Replicant Lab</h4><p><b>Objetivo:</b> Publicar roadmap estructurado y panel interno generado sin duplicar el estado.</p><p><b>Terminado:</b> PRs validados, panel derivado y sincronización documentada sin nuevo servicio.</p><p><b>Riesgos:</b> Integración coordinada entre tres repositorios</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/2">Evidencia</a></p></article>
</div>
<div class="eh-column eh-status--in_progress"><h3>En ejecución · 0</h3>
</div>
<div class="eh-column eh-status--pending"><h3>Pendiente · 15</h3>
<article class="eh-task"><span>W-2026-08-31</span><h4>Supply y validación</h4><p><b>Objetivo:</b> Evaluar hasta tres ciudades, fuentes, permisos, calidad, volumen y cinco entrevistas.</p><p><b>Terminado:</b> Ficha por ciudad y decisión de piloto con tres fuentes viables por ciudad elegida.</p><p><b>Riesgos:</b> Fuentes insuficientes o no permitidas</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-09-07</span><h4>Arquitectura y confianza</h4><p><b>Objetivo:</b> Definir datos, estados, eventos, permisos, privacidad, retención y Gmail fallback.</p><p><b>Terminado:</b> ADR técnico, modelo de datos y threat checklist aceptados.</p><p><b>Riesgos:</b> OAuth restringido, Sobrearquitectura</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-09-14</span><h4>UX móvil y prototipo</h4><p><b>Objetivo:</b> Diseñar onboarding, hoy, resultados, detalle, shortlist, contacto y seguimiento a 360-430 px.</p><p><b>Terminado:</b> Prototipo navegable probado con 3-5 personas.</p><p><b>Riesgos:</b> Flujos contemplativos sin acción</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-09-21</span><h4>Base PWA</h4><p><b>Objetivo:</b> Preparar CI, entornos, auth, perfil, PWA instalable, diseño y observabilidad mínima.</p><p><b>Terminado:</b> La app abre en móvil y persiste el perfil de un usuario.</p><p><b>Riesgos:</b> Incompatibilidad móvil o persistencia</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-09-28</span><h4>Ingesta y listings</h4><p><b>Objetivo:</b> Integrar primeras fuentes permitidas con normalización, deduplicación y origen.</p><p><b>Terminado:</b> Listings reales o dataset trazable disponible en una ciudad.</p><p><b>Riesgos:</b> Fuente bloqueada, Datos duplicados</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-10-05</span><h4>Búsqueda y selección</h4><p><b>Objetivo:</b> Implementar filtros, matching explicable, shortlist y estados.</p><p><b>Terminado:</b> Un usuario obtiene una shortlist útil en menos de cinco minutos.</p><p><b>Riesgos:</b> Matching opaco o sin evidencia</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-10-12</span><h4>Contacto seguro</h4><p><b>Objetivo:</b> Crear plantillas multilingües editables, consentimiento y derivación controlada.</p><p><b>Terminado:</b> Mensaje contextual listo y acción auditada.</p><p><b>Riesgos:</b> Spam, Mensaje incorrecto</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-10-19</span><h4>Seguimiento</h4><p><b>Objetivo:</b> Añadir estados, recordatorios, forwarding o vinculación de hilos y pendientes.</p><p><b>Terminado:</b> Dashboard de qué hacer hoy operativo.</p><p><b>Riesgos:</b> Auditoría OAuth retrasa el piloto</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-10-26</span><h4>Conversación y alertas</h4><p><b>Objetivo:</b> Resumir hilos, extraer peticiones y sugerir alertas y siguiente acción.</p><p><b>Terminado:</b> Tres conversaciones de prueba interpretadas correctamente.</p><p><b>Riesgos:</b> Interpretación errónea de IA</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-11-02</span><h4>Vertical slice</h4><p><b>Objetivo:</b> Completar buscar, seleccionar, contactar y seguir con datos reales.</p><p><b>Terminado:</b> Demo móvil reproducible de punta a punta.</p><p><b>Riesgos:</b> Bloqueantes P0/P1</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-11-09</span><h4>Calidad y cumplimiento</h4><p><b>Objetivo:</b> QA móvil, accesibilidad, seguridad, privacidad, logs, errores y recuperación.</p><p><b>Terminado:</b> Checklist de release y registro de riesgos aceptados.</p><p><b>Riesgos:</b> Privacidad, Accesibilidad, Recuperación incompleta</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-11-16</span><h4>Piloto cerrado</h4><p><b>Objetivo:</b> Incorporar primeros usuarios, prestar soporte ligero y medir activación/contacto.</p><p><b>Terminado:</b> Primeros usuarios reales y panel de métricas.</p><p><b>Riesgos:</b> Soporte fragmentado, Muestra insuficiente</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-11-23</span><h4>Corrección por evidencia</h4><p><b>Objetivo:</b> Resolver los tres mayores frenos observados y validar fuentes y mensajes.</p><p><b>Terminado:</b> Release candidate pública basada en evidencia.</p><p><b>Riesgos:</b> Cambios sin evidencia, Scope creep</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-11-30</span><h4>Lanzamiento piloto</h4><p><b>Objetivo:</b> Publicar PWA, monitorizar, soportar y comunicar cobertura honestamente.</p><p><b>Terminado:</b> Piloto comercial público estable y observable.</p><p><b>Riesgos:</b> Inestabilidad, Cobertura mal comunicada</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>W-2026-12-07</span><h4>Estabilización y decisión de enero</h4><p><b>Objetivo:</b> Corregir incidencias, medir embudo, entrevistar y decidir el backlog de enero.</p><p><b>Terminado:</b> Informe de piloto y backlog 2027 priorizado.</p><p><b>Riesgos:</b> Escalado prematuro</p><p>Evidencia pendiente</p></article>
</div>
<div class="eh-column eh-status--blocked"><h3>Bloqueado · 0</h3>
</div>
</div></section>
<section><h2>Línea temporal hasta el 20 de diciembre</h2><ol class="eh-timeline">
<li class="eh-status--done"><time>2026-08-22 - 2026-08-30</time><strong>Consolidar la fuente de verdad</strong><span>Completado</span></li>
<li class="eh-status--done"><time>2026-08-22 - 2026-08-30</time><strong>Roadmap canónico y panel Replicant Lab</strong><span>Completado</span></li>
<li class="eh-status--pending"><time>2026-08-31 - 2026-09-06</time><strong>Supply y validación</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-09-07 - 2026-09-13</time><strong>Arquitectura y confianza</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-09-14 - 2026-09-20</time><strong>UX móvil y prototipo</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-09-21 - 2026-09-27</time><strong>Base PWA</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-09-28 - 2026-10-04</time><strong>Ingesta y listings</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-10-05 - 2026-10-11</time><strong>Búsqueda y selección</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-10-12 - 2026-10-18</time><strong>Contacto seguro</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-10-19 - 2026-10-25</time><strong>Seguimiento</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-10-26 - 2026-11-01</time><strong>Conversación y alertas</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-11-02 - 2026-11-08</time><strong>Vertical slice</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-11-09 - 2026-11-15</time><strong>Calidad y cumplimiento</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-11-16 - 2026-11-22</time><strong>Piloto cerrado</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-11-23 - 2026-11-29</time><strong>Corrección por evidencia</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-11-30 - 2026-12-06</time><strong>Lanzamiento piloto</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>2026-12-07 - 2026-12-20</time><strong>Estabilización y decisión de enero</strong><span>Pendiente</span></li>
</ol></section>
</div>

La fuente canónica es `ratienza/ErasmusHomes/docs/board/roadmap.yaml`. Esta página es un artefacto derivado.
