# Pendientes

Panel vivo de remediación de la **Fase 2**, iniciado el **13/08/2026** desde la evidencia cerrada en la Fase 1. Ningún elemento se elimina: cada bloque conserva su problema inicial, acción y estado final demostrado.

## Leyenda

- 🟢 **Operativo o cerrado**
- 🟡 **Operativo con pendiente**
- 🔴 **Bloqueado**
- ⚪ **No desplegado / no aplicable**

## Matriz de Fase 2

| Área | Problema | Estado inicial | Acción | PR | Validación | Estado final |
|---|---|---|---|---|---|---|
| 2A · Salones AV | Bind LAN correcto solo en Nexus | ⏳ Pendiente | Versionar el cambio, reconciliar y desplegar desde `main` | `salones-av-valencia-palace#2` | Blob idéntico, Compose válido, checkout limpio y 7 rutas `200` | ✅ Resuelto |
| 2B · Consumos Cupra | Despliegue sin SHA/rollback inequívoco | ⏳ Pendiente | No iniciado | — | — | ⏳ Pendiente |
| 2C · CV | Flujo Firebase/Cloud Run divergente | ⏳ Pendiente | No iniciado | — | — | ⏳ Pendiente |
| 2D · Control de Red | Datos vivos versionados | ⏳ Pendiente | No iniciado | — | — | ⏳ Pendiente |
| 2E · Cartera Estratégica | Suite completa no finalizada | ⏳ Pendiente | No iniciado | — | — | ⏳ Pendiente |
| 2F · Backups Nexus | Política y restauración pendientes | ⏳ Pendiente | No iniciado | — | — | ⏳ Pendiente |

## Estado conjunto

<div class="status-panel"><table>
<thead><tr><th>Aplicación</th><th>Estado</th><th>Detalle</th></tr></thead>
<tbody>
<tr><td><code>infra-replicant-lab</code></td><td>🟢 Cierre documental</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> inventario real, fichas individuales, portables globales e individuales y validación en Nexus.</p><p><strong>Pendiente:</strong> mantenimiento normal cuando cambie una aplicación o su despliegue.</p></details></td></tr>
<tr><td><code>Apps_Lauch</code></td><td>🟢 Operativo</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> catálogos público/Nexus aislados y validados.</p><p><strong>Pendiente menor:</strong> decidir en un cambio propio si se eliminan assets PWA históricos del VPS que no forman parte del despliegue actual.</p></details></td></tr>
<tr><td><code>Reserva-Pistas-UTP</code></td><td>🟢 Operativo</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> Nexus y DigitalOcean observados; 21 pruebas correctas; código principal desplegado coincidente con GitHub.</p><p><strong>Pendiente:</strong> operación normal y sincronización solo bajo demanda.</p></details></td></tr>
<tr><td><code>salones-av-valencia-palace</code></td><td>🟢 Resuelto</td><td><details><summary>Ver</summary><p><strong>Incidencia inicial:</strong> Nexus restringía correctamente el bind a <code>192.168.18.220:8081</code>, pero el cambio era local.</p><p><strong>Cierre:</strong> PR <code>#2</code>, SHA <code>8c0bc08</code>, Compose válido, GitHub/Nexus iguales, checkout limpio y siete rutas con <code>200</code>.</p></details></td></tr>
<tr><td><code>Consumos_Cupra</code></td><td>🟡 Trazabilidad</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> servicio DigitalOcean activo; lint y build correctos.</p><p><strong>Pendiente:</strong> despliegue reproducible desde un SHA, persistencia documentada y rollback probado.</p></details></td></tr>
<tr><td><code>CV-Raul-IA-Estudio-Google-</code></td><td>🟡 Configuración Cloud</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> build y PDF correctos; URL Cloud responde.</p><p><strong>Pendiente:</strong> reconciliar Firebase, Cloud Build, región y nombre real del servicio. El checkout Nexus sigue siendo solo lectura.</p></details></td></tr>
<tr><td><code>control-red</code></td><td>🟡 Datos en Git</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> sintaxis PowerShell válida; no se ejecutó escaneo.</p><p><strong>Pendiente:</strong> separar inventario/snapshots reales del código con backup previo y ejemplos anonimizados.</p></details></td></tr>
<tr><td><code>cartera-estrategica</code></td><td>🟡 MVP local</td><td><details><summary>Ver</summary><p><strong>Hito:</strong> 369 pruebas recogidas; ejecución parcial sin fallos hasta el límite temporal.</p><p><strong>Pendiente:</strong> completar la suite en su entorno de proyecto y continuar el plan propio. No desplegar en Nexus sin decisión aprobada.</p></details></td></tr>
</tbody>
</table></div>

## Infraestructura transversal

- Definir política y prueba de restauración para backups generales de Nexus.
- Mantener los aliases `nexus` y `replicant` como configuración local; no requieren servidor DNS.
- No cerrar ninguna deriva copiando el estado de un servidor hacia GitHub.

## Reglas de mantenimiento

1. Consultar GitHub y el servicio real antes de cambiar estados.
2. Distinguir siempre implementación, validación local, Nexus y producción.
3. No convertir un checkout en evidencia de despliegue.
4. Mantener secretos, datos vivos y backups fuera de Git.
