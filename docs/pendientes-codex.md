# Pendientes

Panel compacto del estado de los repositorios GitHub vinculados a Raul Lab. Corte comprobado: **10/08/2026**. Los detalles permanecen plegados para facilitar una lectura rápida y conservan los hitos, pendientes, siguientes acciones y PR ya documentados.

## Leyenda

- 🟢 **Terminado u operativo**
- 🟡 **En desarrollo o con pendientes**
- 🔴 **Bloqueado o con incidencia real**
- ⚪ **Sin iniciar**

El texto acompaña siempre al indicador visual; el color no es la única señal de estado.

## Estado conjunto

<div class="status-panel"><table>
<thead><tr><th>Repositorio</th><th>Finalidad</th><th>Estado</th><th>PR abiertos</th><th>Detalle</th></tr></thead>
<tbody>
<tr><td><a href="https://github.com/ratienza/infra-replicant-lab"><code>infra-replicant-lab</code></a></td><td>Gestor de infraestructura y operación de Raul Lab.</td><td>🟢 <strong>Terminado y operativo en Nexus</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> pipeline reproducible, MkDocs canónico, Nginx estático y portables completos.</p><p><strong>Terminado:</strong> validación real en Nexus y cierre documental mediante <a href="https://github.com/ratienza/infra-replicant-lab/pull/11">PR #11</a>.</p><p><strong>Pendientes:</strong> ninguno del gestor documental; DNS local y backups generales pertenecen a infraestructura.</p><p><strong>Siguiente acción:</strong> mantenimiento normal cuando cambie la fuente canónica.</p><p><strong>PR:</strong> último fusionado #11.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/Reserva-Pistas-UTP"><code>Reserva-Pistas-UTP</code></a></td><td>Automatización de reservas de pádel.</td><td>🟢 <strong>Operativo y sincronizado bajo demanda</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> sincronización segura DigitalOcean ↔ Nexus integrada mediante los <a href="https://github.com/ratienza/Reserva-Pistas-UTP/pull/4">PR #4</a>, <a href="https://github.com/ratienza/Reserva-Pistas-UTP/pull/5">#5</a> y <a href="https://github.com/ratienza/Reserva-Pistas-UTP/pull/6">#6</a>.</p><p><strong>Terminado:</strong> servicios validados en ambos entornos, 18 registros reconciliados sin conflictos ni secretos y canal SSH restringido operativo.</p><p><strong>Pendientes:</strong> ninguno del encargo; la sincronización futura se ejecuta solo bajo demanda y con confirmación.</p><p><strong>Siguiente acción:</strong> operación normal y revisión de conflictos si una vista previa futura los detecta.</p><p><strong>PR:</strong> ninguno abierto; últimos fusionados #4, #5 y #6. El borrador #1 quedó cerrado por quedar sustituido.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/salones-av-valencia-palace"><code>salones-av-valencia-palace</code></a></td><td>Documentación operativa audiovisual.</td><td>🟡 <strong>Operativo con incidencia conocida</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> <a href="https://github.com/ratienza/salones-av-valencia-palace/pull/1">PR #1</a>, Compose con Nginx.</p><p><strong>Terminado:</strong> HTML y recursos operativos versionados y servicio observado en Nexus.</p><p><strong>Pendientes:</strong> reconciliar en su repositorio el bind LAN observado y completar la revisión final indicada en su contexto.</p><p><strong>Siguiente acción:</strong> corregir la deriva en el repositorio de la aplicación.</p><p><strong>PR:</strong> ninguno abierto; último fusionado #1.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/cartera-estrategica"><code>cartera-estrategica</code></a></td><td>MVP privado de análisis de cartera.</td><td>🟡 <strong>En desarrollo</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> <a href="https://github.com/ratienza/cartera-estrategica/pull/17">PR #17</a>, estabilización del arranque privado.</p><p><strong>Terminado:</strong> fases 0–7B y libro de cash integrados; versión documentada <code>v1.2.0</code>.</p><p><strong>Pendientes:</strong> Fase 8, pruebas y endurecimiento; Fase 9, publicación privada. La Fase 7C permanece fuera del MVP.</p><p><strong>Siguiente acción:</strong> continuar con la Fase 8.</p><p><strong>PR:</strong> ninguno abierto; último fusionado #17.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/CV-Raul-IA-Estudio-Google-"><code>CV-Raul-IA-Estudio-Google-</code></a></td><td>CV web generado desde Google AI Studio.</td><td>🟡 <strong>En desarrollo</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> Dockerfile y configuración Nginx; aplicación Vite y PDF generado.</p><p><strong>Terminado:</strong> aplicación desplegable versionada.</p><p><strong>Pendientes:</strong> ninguno documentado en README.</p><p><strong>Siguiente acción:</strong> no definida.</p><p><strong>PR:</strong> ninguno abierto; último cambio directo <code>38c9fe7</code>.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/Apps_Lauch"><code>Apps_Lauch</code></a></td><td>Launchpad público de aplicaciones.</td><td>🟢 <strong>Operativo según README</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> la tarjeta del CV apunta a Cloud Run.</p><p><strong>Terminado:</strong> despliegue y verificación documentados.</p><p><strong>Pendientes:</strong> ninguno versionado.</p><p><strong>Siguiente acción:</strong> incorporar o cambiar una aplicación cuando exista un encargo.</p><p><strong>PR:</strong> ninguno abierto; último cambio directo <code>98149fa</code>.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/Consumos_Cupra"><code>Consumos_Cupra</code></a></td><td>Control de consumos de combustible.</td><td>🟡 <strong>En desarrollo</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> soporte para despliegue bajo la ruta <code>consumos</code>.</p><p><strong>Terminado:</strong> PWA, servidor y Docker Compose versionados.</p><p><strong>Pendientes:</strong> ninguno documentado en README.</p><p><strong>Siguiente acción:</strong> no definida.</p><p><strong>PR:</strong> ninguno abierto; último cambio directo <code>050535f</code>.</p></details></td></tr>
<tr><td><a href="https://github.com/ratienza/control-red"><code>control-red</code></a></td><td>Panel local de inventario y escaneo de red.</td><td>🟢 <strong>Operativo local según README</strong></td><td>0</td><td><details><summary>Ver</summary><p><strong>Último hito:</strong> primera versión del panel PowerShell.</p><p><strong>Terminado:</strong> lanzador local e inventario persistente.</p><p><strong>Pendientes:</strong> ninguno documentado.</p><p><strong>Siguiente acción:</strong> proteger inventario y snapshots ante cualquier cambio.</p><p><strong>PR:</strong> ninguno abierto; último cambio directo <code>0e285d2</code>.</p></details></td></tr>
</tbody>
</table></div>

## Exclusión expresa

[`ratienza/python`](https://github.com/ratienza/python) no forma parte de Raul Lab y se excluye de esta visión.

## Reglas de mantenimiento

1. Consultar GitHub antes de cambiar estados, PR o hitos.
2. No convertir documentación de despliegue en validación viva.
3. No presentar como pendiente lo ya cerrado.
4. Registrar “sin pendiente documentado” cuando GitHub y el repositorio no definan una siguiente acción.
5. Mantener separados código, secretos, bases, históricos y datos vivos de cada aplicación.
