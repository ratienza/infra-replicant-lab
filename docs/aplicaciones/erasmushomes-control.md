# ErasmusHomes · Control del MVP

<!-- GENERATED: edit ratienza/ErasmusHomes Docs/board/roadmap.yaml, never this file -->

## Accesos

- **Panel de control:** [Control MVP autónomo](/control/erasmushomes/)
- **Ficha técnica:** [HTML autocontenido](/downloads/apps/erasmushomes-control.html)
- **Aplicación / producción:** no hay una URL de producto ErasmusHomes desplegada.

<div class="eh-dashboard">
<section class="eh-hero"><p class="eh-kicker">Objetivo diciembre</p><h2>Piloto público durante la semana del 30-11-2026</h2><div class="eh-sync eh-sync--synchronized">Sincronizado</div><dl><dt>SHA ErasmusHomes main</dt><dd><code>d5cabad5a769e8b9bbac8482d8a85910934f6c4c</code></dd><dt>Última sincronización</dt><dd>30-08-2026 14:16</dd></dl><div class="eh-agreed-document"><a href="/downloads/erasmushomes/Roadmap_ErasmusHomes_MVP_Diciembre_2026.pdf" target="_blank" rel="noopener noreferrer">Abrir roadmap acordado (PDF)</a><span><b>Archivo:</b> Roadmap_ErasmusHomes_MVP_Diciembre_2026.pdf</span><span><b>Git:</b> <code>d5cabad5</code> · <a href="https://github.com/ratienza/ErasmusHomes/blob/d5cabad5a769e8b9bbac8482d8a85910934f6c4c/Docs/source/Roadmap_ErasmusHomes_MVP_Diciembre_2026.pdf" target="_blank" rel="noopener noreferrer">ver fuente versionada</a></span><span><b>SHA-256:</b> <code>077afbd06f30723663dfcbf93c966dc8a39005e49865d34542ce0976c91e3c2c</code></span><span><b>Fecha:</b> 23-08-2026</span></div></section>
<section class="eh-metrics">
<article><strong>21%</strong><span>completado</span></article>
<article class="eh-metric eh-status--done"><strong>4</strong><span>Completado</span></article>
<article class="eh-metric eh-status--in_progress"><strong>0</strong><span>En ejecución</span></article>
<article class="eh-metric eh-status--pending"><strong>14</strong><span>Pendiente</span></article>
<article class="eh-metric eh-status--blocked"><strong>1</strong><span>Bloqueado</span></article>
</section>
<section class="eh-gate"><h2>Próximo gate</h2>
<p><strong>WK-01 · Supply y validación</strong><br>Mantener Pula como referencia y no confundir portal enlazable con permiso de ingesta o matching.</p>
</section>
<section><h2>Esta semana</h2><div class="eh-priorities">
<p>No hay tareas en ejecución.</p>
</div></section>
<section><h2>Kanban</h2><div class="eh-kanban">
<div class="eh-column eh-status--done"><h3>Completado · 4</h3>
<article class="eh-task"><span>EH-001</span><h4>Consolidar la fuente de verdad</h4><p><b>Objetivo:</b> Consolidar fuentes, decisiones y alcance en Git y sincronizar Nexus.</p><p><b>Terminado:</b> PR fusionado en main y GitHub, local y Nexus en el mismo SHA.</p><p><b>Riesgos:</b> Divergencia histórica de PDFs ya documentada</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/1">Evidencia</a></p></article>
<article class="eh-task"><span>EH-002</span><h4>Roadmap canónico y panel Replicant Lab</h4><p><b>Objetivo:</b> Publicar roadmap estructurado y panel interno generado sin duplicar el estado.</p><p><b>Terminado:</b> PRs validados, panel derivado y sincronización documentada sin nuevo servicio.</p><p><b>Riesgos:</b> Integración coordinada entre tres repositorios</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/2">Evidencia</a></p></article>
<article class="eh-task"><span>EH-002R-C</span><h4>Cierre definitivo de documentación y Control Scrum-lite</h4><p><b>Objetivo:</b> Cerrar documentación, contrato de datos, Control autónomo, PDF e inventario de Apps Launch.</p><p><b>Terminado:</b> Tres PR aceptados visualmente, fusionados y publicados en Nexus con trazabilidad completa.</p><p><b>Riesgos:</b> Deuda menor de presentación de fechas trasladada al próximo encargo</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/5">Evidencia</a></p></article>
<article class="eh-task"><span>EH-003</span><h4>Contrato funcional del piloto mobile-first</h4><p><b>Objetivo:</b> Definir el contrato funcional y los flujos móviles del piloto antes de desarrollar producto.</p><p><b>Terminado:</b> Contrato funcional priorizado y criterios de aceptación mobile-first aprobados.</p><p><b>Riesgos:</b> Ambigüedad funcional, Crecimiento de alcance</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/7">Evidencia</a></p></article>
</div>
<div class="eh-column eh-status--in_progress"><h3>En ejecución · 0</h3>
</div>
<div class="eh-column eh-status--pending"><h3>Pendiente · 14</h3>
<article class="eh-task"><span>WK-02</span><h4>Arquitectura y confianza</h4><p><b>Objetivo:</b> Definir datos, estados, eventos, permisos, privacidad, retención y Gmail fallback.</p><p><b>Terminado:</b> ADR técnico, modelo de datos y threat checklist aceptados.</p><p><b>Riesgos:</b> OAuth restringido, Sobrearquitectura</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-03</span><h4>UX móvil y prototipo</h4><p><b>Objetivo:</b> Diseñar onboarding, hoy, resultados, detalle, shortlist, contacto y seguimiento a 360-430 px.</p><p><b>Terminado:</b> Prototipo navegable probado con 3-5 personas.</p><p><b>Riesgos:</b> Flujos contemplativos sin acción</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-04</span><h4>Base PWA</h4><p><b>Objetivo:</b> Preparar CI, entornos, auth, perfil, PWA instalable, diseño y observabilidad mínima.</p><p><b>Terminado:</b> La app abre en móvil y persiste el perfil de un usuario.</p><p><b>Riesgos:</b> Incompatibilidad móvil o persistencia</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-05</span><h4>Ingesta y listings</h4><p><b>Objetivo:</b> Integrar primeras fuentes permitidas con normalización, deduplicación y origen.</p><p><b>Terminado:</b> Listings reales o dataset trazable disponible en una ciudad.</p><p><b>Riesgos:</b> Fuente bloqueada, Datos duplicados</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-06</span><h4>Búsqueda y selección</h4><p><b>Objetivo:</b> Implementar filtros, matching explicable, shortlist y estados.</p><p><b>Terminado:</b> Un usuario obtiene una shortlist útil en menos de cinco minutos.</p><p><b>Riesgos:</b> Matching opaco o sin evidencia</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-07</span><h4>Contacto seguro</h4><p><b>Objetivo:</b> Crear plantillas multilingües editables, consentimiento y derivación controlada.</p><p><b>Terminado:</b> Mensaje contextual listo y acción auditada.</p><p><b>Riesgos:</b> Spam, Mensaje incorrecto</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-08</span><h4>Seguimiento</h4><p><b>Objetivo:</b> Añadir estados, recordatorios, forwarding o vinculación de hilos y pendientes.</p><p><b>Terminado:</b> Dashboard de qué hacer hoy operativo.</p><p><b>Riesgos:</b> Auditoría OAuth retrasa el piloto</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-09</span><h4>Conversación y alertas</h4><p><b>Objetivo:</b> Resumir hilos, extraer peticiones y sugerir alertas y siguiente acción.</p><p><b>Terminado:</b> Tres conversaciones de prueba interpretadas correctamente.</p><p><b>Riesgos:</b> Interpretación errónea de IA</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-10</span><h4>Vertical slice</h4><p><b>Objetivo:</b> Completar buscar, seleccionar, contactar y seguir con datos reales.</p><p><b>Terminado:</b> Demo móvil reproducible de punta a punta.</p><p><b>Riesgos:</b> Bloqueantes P0/P1</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-11</span><h4>Calidad y cumplimiento</h4><p><b>Objetivo:</b> QA móvil, accesibilidad, seguridad, privacidad, logs, errores y recuperación.</p><p><b>Terminado:</b> Checklist de release y registro de riesgos aceptados.</p><p><b>Riesgos:</b> Privacidad, Accesibilidad, Recuperación incompleta</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-12</span><h4>Piloto cerrado</h4><p><b>Objetivo:</b> Incorporar primeros usuarios, prestar soporte ligero y medir activación/contacto.</p><p><b>Terminado:</b> Primeros usuarios reales y panel de métricas.</p><p><b>Riesgos:</b> Soporte fragmentado, Muestra insuficiente</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-13</span><h4>Corrección por evidencia</h4><p><b>Objetivo:</b> Resolver los tres mayores frenos observados y validar fuentes y mensajes.</p><p><b>Terminado:</b> Release candidate pública basada en evidencia.</p><p><b>Riesgos:</b> Cambios sin evidencia, Scope creep</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-14</span><h4>Lanzamiento piloto</h4><p><b>Objetivo:</b> Publicar PWA, monitorizar, soportar y comunicar cobertura honestamente.</p><p><b>Terminado:</b> Piloto comercial público estable y observable.</p><p><b>Riesgos:</b> Inestabilidad, Cobertura mal comunicada</p><p>Evidencia pendiente</p></article>
<article class="eh-task"><span>WK-15</span><h4>Estabilización y decisión de enero</h4><p><b>Objetivo:</b> Corregir incidencias, medir embudo, entrevistar y decidir el backlog de enero.</p><p><b>Terminado:</b> Informe de piloto y backlog 2027 priorizado.</p><p><b>Riesgos:</b> Escalado prematuro</p><p>Evidencia pendiente</p></article>
</div>
<div class="eh-column eh-status--blocked"><h3>Bloqueado · 1</h3>
<article class="eh-task"><span>WK-01</span><h4>Supply y validación</h4><p><b>Objetivo:</b> Seleccionar tres ciudades para un piloto de agregador inteligente y validar demanda, alojamiento, fuentes trazables, permisos y cinco entrevistas.</p><p><b>Terminado:</b> Ranking reproducible, fuentes clasificadas por uso, decisión condicionada y cinco entrevistas reales completadas.</p><p><b>Riesgos:</b> Cinco entrevistas pendientes, Matching sin permiso o flujo oficial, Volumen visible no equivale a cobertura autorizada</p><p><b>Bloqueo:</b> La shortlist condicionada es Pula, Barcelona y Lisboa, pero faltan cinco entrevistas reales y una ruta permitida y verificable de matching por ciudad antes de cerrar WK-01 o iniciar producto.</p><p><a href="https://github.com/ratienza/ErasmusHomes/pull/9">Evidencia</a></p></article>
</div>
</div></section>
<section><h2>Línea temporal hasta el 20 de diciembre</h2><ol class="eh-timeline">
<li class="eh-status--done"><time>22-08-2026 - 30-08-2026</time><strong>Consolidar la fuente de verdad</strong><span>Completado</span></li>
<li class="eh-status--done"><time>22-08-2026 - 30-08-2026</time><strong>Roadmap canónico y panel Replicant Lab</strong><span>Completado</span></li>
<li class="eh-status--done"><time>24-08-2026 - 30-08-2026</time><strong>Cierre definitivo de documentación y Control Scrum-lite</strong><span>Completado</span></li>
<li class="eh-status--done"><time>31-08-2026 - 06-09-2026</time><strong>Contrato funcional del piloto mobile-first</strong><span>Completado</span></li>
<li class="eh-status--blocked"><time>31-08-2026 - 06-09-2026</time><strong>Supply y validación</strong><span>Bloqueado</span></li>
<li class="eh-status--pending"><time>07-09-2026 - 13-09-2026</time><strong>Arquitectura y confianza</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>14-09-2026 - 20-09-2026</time><strong>UX móvil y prototipo</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>21-09-2026 - 27-09-2026</time><strong>Base PWA</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>28-09-2026 - 04-10-2026</time><strong>Ingesta y listings</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>05-10-2026 - 11-10-2026</time><strong>Búsqueda y selección</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>12-10-2026 - 18-10-2026</time><strong>Contacto seguro</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>19-10-2026 - 25-10-2026</time><strong>Seguimiento</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>26-10-2026 - 01-11-2026</time><strong>Conversación y alertas</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>02-11-2026 - 08-11-2026</time><strong>Vertical slice</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>09-11-2026 - 15-11-2026</time><strong>Calidad y cumplimiento</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>16-11-2026 - 22-11-2026</time><strong>Piloto cerrado</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>23-11-2026 - 29-11-2026</time><strong>Corrección por evidencia</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>30-11-2026 - 06-12-2026</time><strong>Lanzamiento piloto</strong><span>Pendiente</span></li>
<li class="eh-status--pending"><time>07-12-2026 - 20-12-2026</time><strong>Estabilización y decisión de enero</strong><span>Pendiente</span></li>
</ol></section>
</div>

La fuente canónica es `ratienza/ErasmusHomes/Docs/board/roadmap.yaml`. Consolidación `Docs/` terminada en `main` con CI verde. Esta página es un artefacto derivado.
