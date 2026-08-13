# Aplicaciones

Inventario auditado el **13/08/2026** desde GitHub, checkouts, código y servicios observados. “Checkout en Nexus” no significa “aplicación servida por Nexus”.

## Estado conjunto

<div class="status-panel"><table>
<thead><tr><th>Aplicación</th><th>Estado real</th><th>Entorno validado</th><th>Referencia</th></tr></thead>
<tbody>
<tr><td><a href="app-launch/"><strong>App Launch</strong></a></td><td>🟢 Operativo multientorno</td><td>DigitalOcean + Nexus</td><td><code>ced6e14</code></td></tr>
<tr><td><a href="salones-av/"><strong>Salones AV</strong></a></td><td>🟢 Operativo · Git y Nexus reconciliados</td><td>Nexus + DigitalOcean</td><td><code>8c0bc08</code></td></tr>
<tr><td><a href="reserva-pistas-utp/"><strong>Reserva-Pistas-UTP</strong></a></td><td>🟢 Operativo</td><td>Nexus + DigitalOcean</td><td><code>6df1698</code></td></tr>
<tr><td><a href="consumos-cupra/"><strong>Consumos Cupra</strong></a></td><td>🟡 Operativo; despliegue no trazado por SHA</td><td>DigitalOcean</td><td><code>050535f</code></td></tr>
<tr><td><a href="cv-raul/"><strong>CV de Raúl</strong></a></td><td>🟡 Producción Cloud con configuración divergente</td><td>Build local + URL Cloud</td><td><code>0da08cf</code></td></tr>
<tr><td><a href="control-red/"><strong>Control de Red</strong></a></td><td>🟡 Herramienta local con datos versionados</td><td>Sintaxis local</td><td><code>0e285d2</code></td></tr>
<tr><td><a href="cartera-estrategica/"><strong>Cartera Estratégica</strong></a></td><td>🟡 MVP local; no desplegado</td><td>Replicant / pruebas parciales</td><td><code>f2b319d</code></td></tr>
<tr><td><a href="replicant-lab/"><strong>Replicant Lab</strong></a></td><td>🟢 Documentación canónica</td><td>Nexus</td><td><code>91e0495</code> antes de este cierre</td></tr>
</tbody>
</table></div>

## Servicios publicados en Nexus

| Puerto | Servicio | Estado observado |
|---:|---|---|
| `80` | App Launch | `200` |
| `8080` | Libre | Sin listener |
| `8081` | Salones AV | `200` |
| `8082` | Replicant Lab | `200` |
| `8083` | Reserva-Pistas-UTP | `200` |

CV y Control de Red tienen checkout en Nexus, pero no contenedor, servicio ni puerto. Consumos no tiene checkout ni servicio Nexus. Cartera Estratégica permanece en Replicant.

## Criterio de lectura

- **Implementado:** existe en el código versionado.
- **Validado localmente:** superó una prueba sobre una copia o entorno local.
- **Validado en Nexus:** se observó el servicio real de Nexus.
- **Validado en producción:** se comprobó el servicio público correspondiente.

Ninguno de esos estados se extrapola automáticamente a los demás.
