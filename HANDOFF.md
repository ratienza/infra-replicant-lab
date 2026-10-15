# HANDOFF · CryptoWallet V1.6.5 / documentación Replicant Lab

15/10/2026. `ratienza/cryptowallet` fusionó el PR funcional #29 en `36d50affe9afac059f399e75e80fabe0cf8aca56`, tag `v1.6.5`; los PR #31 y #32 corrigieron y documentaron la composición de las tarjetas. Nexus ejecuta `cryptowallet:1.6.5-69f121ac86eb` healthy en localhost `8516`, con datos, copias y seguridad en montajes privados separados.

V1.6.5 añade pesos coherentes sobre patrimonio total completo en Dashboard y Cartera, separa Estables/FIAT y mantiene P&G como rentabilidad sobre coste. La corrección presenta `Peso` como una fila completa con el mismo formato que `Invertido` y `Valor actual`, y conserva `Peso por red` y `Activos por red`. No muestra peso en Invertido FIFO ni porcentajes derivados de subtotales. La cabecera identifica v1.6.5 y retira `Cartera privada`. 405 pruebas superadas en la imagen aislada. Copia previa restaurada en aislamiento; 33 componentes, 2 operaciones y huella financiera idéntica antes/después.

La ficha, índices, Nexus, fases, pendientes, cambio del 15/10 y derivados HTML/PDF se regeneran mediante el pipeline canónico. Publicar solo `infra-replicant-docs` en Nexus `:8082`, conservando su imagen anterior para rollback. No reiniciar CryptoWallet ni cambiar datos, copias, OAuth, Access, Tunnel o seguridad.

---

# Histórico · CryptoWallet V1.6.4 / documentación Replicant Lab

14/10/2026. `ratienza/cryptowallet` fusionó el PR funcional #27 en `0111397b51ca8b9119fdc08593eca4bd59d9b2e5`, tag `v1.6.4`; el PR #28 registró la promoción. Nexus ejecuta `cryptowallet:1.6.4-0111397b51ca` healthy en localhost `8516`, con datos, copias y seguridad en montajes privados separados.

V1.6.4 cierra visualmente el Logbook: distintivos para estados reales, filtro Estado combinable y paginación coherente, siete filtros en una línea de escritorio y distribución móvil, importe del listado a dos decimales sin perder precisión interna, Activo alineado a la derecha y colores compartidos entre Añadir y Revisar operación. 397 pruebas y 68 subpruebas superadas. Copia previa restaurada en aislamiento; 33 componentes, 2 operaciones y huella financiera idéntica antes/después.

La ficha, índices, Nexus, fases, pendientes, cambio del 14/10 y derivados HTML/PDF se regeneran mediante el pipeline canónico. Publicar solo `infra-replicant-docs` en Nexus `:8082`, conservando su imagen anterior para rollback. No reiniciar CryptoWallet ni cambiar datos, copias, OAuth, Access, Tunnel o seguridad.

---

# Histórico · CryptoWallet V1.6.2 / documentación Replicant Lab

14/10/2026. `ratienza/cryptowallet` fusionó el PR funcional #23 en `43d04a2e8d3681e9cb8631ba6c7f16582327b813`, tag `v1.6.2`. Nexus ejecuta `cryptowallet:1.6.2-43d04a2e8d36` healthy en localhost `8516`, con datos, copias y seguridad en montajes privados separados.

V1.6.2 conserva íntegro el Logbook V1.6.1 y completa la identidad visual: favicon BTC SVG versionado, marca oficial de The Replicant Lab a la derecha de la cabecera, título y navegación centrados, y lockup corporativo centrado en el pie. La referencia aprobada procede de Cartera Estratégica y usa el bitmap corporativo exacto sin transformación. 395 pruebas superadas; revisión visual sintética 1280/390 en claro/oscuro y comprobación autenticada de producción. Copia previa restaurada en aislamiento; 33 componentes, 1 operación y árbol del borrador BTC permanecieron idénticos antes/después.

La ficha, índices, Nexus, operación, fases, pendientes, cambio del 14/10 y derivados HTML/PDF se regeneran mediante el pipeline canónico. Publicar solo `infra-replicant-docs` en Nexus `:8082`, conservando su imagen/composición anterior para rollback. No reiniciar CryptoWallet ni cambiar datos, copias, OAuth, Access, Tunnel o seguridad.

---

# Histórico · CryptoWallet V1.6.1 / documentación Replicant Lab

13/10/2026. `ratienza/cryptowallet` fusionó el PR funcional #21 en `2cc792dea0509881c1beeddebce9a006065e8010`, tag `v1.6.1`, y el PR documental #22 en `de75bba00755331a1187196bc90f337e30038936`. Nexus ejecuta `cryptowallet:1.6.1-2cc792dea050` healthy en localhost `8516`, con datos, copias y seguridad en montajes privados separados.

V1.6.1 conserva origen Tarjeta/Liquidez/Otros, comisión Externa/Cartera y favicon BTC, y estabiliza alta, borradores anteriores y correcciones contabilizadas mediante reproducción cronológica. Las seis clases manuales admiten edición completa y eliminación reversible con CAS, idempotencia, eventos append-only y tombstones; `finance.sqlite3` permanece inmutable y la revisión usa solo tres bloques. 391 pruebas + 68 subpruebas superadas en aislamiento antes de promover. Copia previa, restauración aislada, rollback, seguridad separada, imagen, versión y salud verificados. Producción conservó exactamente 32 componentes, 1 operación y su huella; el único borrador BTC activo conservó su árbol y prepara como Tarjeta sin contabilizarse.

La ficha, índices, Nexus, operación, fases, pendientes, cambio del 13/10 y derivados HTML/PDF se regeneraron mediante el pipeline canónico. La nota histórica sobre logos quedó resuelta por V1.6.2 con la identidad corporativa aprobada.

# HANDOFF · v1.1.2 ACEPTADA POR RAÚL / CIERRE DEFINITIVO

12/10/2026. Raúl acepta definitivamente Backups Lab v1.1.2. Código funcional `8f703237619e0501c78a202524c05149abdd0339` (PR #28); evidencia, release y runtime construido `69c2957a99137bfe48bb9e97859c1e161a243e1d` (PR #29). La documentación Replicant Lab previa a este sello está en `6666f70023e8a628035fe8b09746c95e2b92b013` (PR #60); el merge del PR documental de cierre es su SHA final publicado. La corrección conserva fichas compactas, muestra solo candidatas independientes con distintivo propio y mueve siete orígenes vinculados al final, plegados por defecto y fuera de contadores/copias. Ignorar/ocultar/revertir es persistente, solicita autorización en contexto y nunca borra directorios.

Observación 12/10/2026 22:53 CEST: 55 registros y cero trabajos activos; programación global ON, seis horarios ON/tres OFF, retención ON 7/4/12/3, Facility detenida, previews fuera, BL-002 verificada y Restore V2. La publicación de Backups Lab se comprobó con 24 capturas de solo lectura, sin trabajos ni mutaciones. La redirección anónima 302 solo acredita la puerta de Cloudflare Access, no una sesión autenticada. Este sello obliga a regenerar y publicar únicamente `infra-replicant-docs` en Nexus `:8082`; no reconstruir ni reiniciar Backups Lab, no modificar otros runtimes, Cloudflare, OAuth ni datos privados. Rollbacks, snapshots y checkouts se conservan.

# HANDOFF · Cartera Estratégica v2.1.0

12/10/2026. Raúl aprobó y autorizó el cierre. `ratienza/cartera-estrategica` publica la release `v2.1.0` en `f520216889d7c1f78551125b66a068fb54df6b99`; PR funcional #30 y PR de release #31 fusionados. Nexus `:8085` ejecuta una imagen con ese SHA y versión, conserva la fuente de datos, montajes, OAuth, PIN y evidencia Indexa, y no incorpora bases de Windows.

Backup SQLite consistente, imagen v2.0.0 y checkout anterior disponibles para rollback. Integridad, huella y conteos coinciden antes y después. Salud HTTP, P&G por conceptos/activos, filtros, visual móvil/escritorio, temas, privacidad, cabecera, pie y favicon verificados. La documentación canónica, ficha HTML/PDF e índice se regeneran mediante el pipeline; App Launch actualiza solo la descripción de la tarjeta Nexus. No queda bloqueante de esta release; el refresco autónomo de Indexa cerrado sigue fuera de alcance.

# HANDOFF · Documentación Backups Lab v1.1.1

12/10/2026. `ratienza/backups-lab` publica v1.1.1 en `50a65d1f708cae7ecd5c3f6402c589da79fa0529`, PR #27. Descubrimiento persistente clasifica seis candidatas solicitadas y cinco checkouts adicionales sin duplicar aplicaciones: 11 carpetas, 0 pendientes. Backups Lab es la única nueva incorporada; su primera copia/Drive/descarga/integridad/recuperación aislada quedó `verified` antes de activar 05:00 Europe/Madrid.

Se preservan 55 copias, BL-002, seis horarios ON/tres OFF, retención ON 7/4/12/3, Facility detenida, preview y Cartera Windows fuera y Restore V2. La ficha, índices, Nexus, fases, cambios, pendientes y derivados HTML/PDF se regeneran con el pipeline canónico. Publicar solo `infra-replicant-docs` en Nexus `:8082`, con rollback propio; no modificar Backups Lab, otros runtimes, Cloudflare, OAuth ni datos privados.

# HANDOFF · Documentación Backups Lab v1.1.0

12/10/2026. Raúl aprobó y autorizó cierre, fusión y publicación. `ratienza/backups-lab` sirve la release `v1.1.0` y SHA `75c0e452b040c1bfca474fbed444b3d12c6c8f98` en Nexus. PR funcional #25 fusionado; copia seleccionada 1/1 y copia de todas 8/8 verificadas y recuperadas, sin previews. Dashboard ON/OFF, retención editable 7/4/12/3 y grupos activo/inactivo comprobados. Guardar parámetros y reiniciar la API preservó política, horarios y el estado de retención ya ON; no hubo limpieza, cambio de ON/OFF, borrado ni restauración.

La ficha, índices, Nexus, fases, cambio del 12/10, pendientes y derivados HTML/PDF se actualizan al estado aprobado. El pipeline canónico regenera trece parejas contando el dossier global. Publicar solo `infra-replicant-docs` en Nexus `:8082`, con imagen anterior etiquetada para rollback; no modificar Backups Lab, otros runtimes, Cloudflare, OAuth ni datos privados. La aplicación conserva su rollback v1.0.1 y snapshot SQLite privado preparados.

# HANDOFF · Documentación Backups Lab V1.0.1

## Corrección vigente v1.0.1 ·12/10/2026

Mismo cierre. Ficha/manual, índice, catálogo, fases, Nexus y cambio del12/10 recogen descubrimiento persistente, candidatas NEW pendientes, fuentes/volúmenes propios y controles globales de programación/retención. v1.0.0/tag no se mueve; release v1.0.1. Horarios, Control Red OFF, exclusiones y Facility detenida preservados; automática de retención OFF y Restore V2. Documentos/derivados sincronizados mediante pipeline existente; CI/recibo/PR/release referencian SHAs servidos. No se leen ni exportan claves privadas o contenido de copias; la pista raemda es solo recordatorio autorizado.

# Histórico · Documentación Backups Lab V1.0.0

12/10/2026. Encargo explícito de cierreV1.0 autoriza documentación/pipeline/publicación. Base infra main6bc3ab8; Backups base main4c63ac1/PR22 (d2c7e1c/PR21 históricos). Sin PR pendientes al empezar, árboles limpios. Nueva rama documental agent/backups-v1-documentation; release funcional en ratienza/backups-lab.

MkDocs canónico: ficha docs/aplicaciones/backups-lab.md, índice, estado/Nexus, cambios, manual/incidente y backlogV2. Fuentes y portables derivan del pipeline existente, doce fichas+dossier global/trece parejas. No se usa un HTML exportado como fuente. Release/tag de Backups v1.0.0, SHA servido en API/labels y recibo de despliegue publicado como comentario en PR; la ficha no inventa un SHA futuro.

Ocho aptas, siete ON a las 05:00 Europe/Madrid y Control Red OFF posterior preservado. Facility detenida/parcial, previews/secretos/Windows excluidos. RetenciónOFF; documentadas dos eliminaciones automáticas11/10 22:20:01Madrid y ocho de manual ya running12/10 00:02:21Madrid, sin atribuir autoría. No purgas/copias nuevas de ensayo. Sesión HTTPS, preview/cancelación y recarga autorizadas verificadas, sin valores de claves.

Sustitución/rollback originales expresamente V2; código/evidencias/snapshots preservados. No implementar V2. Respaldo integral, cifrado adicional, correo/log y agentes/nuevosadaptadores son propuestas anteriores pendientes de decisiones/contratos. Las observaciones históricas no sustituyen el estado actual. Aceptación humana independiente del cierre técnico.

Publicación: construirMkDocs estricto, validar derivados, enlaces y bytes servidos en Nexus, puerto 8082; imágenes anteriores y rollback privado preparados. Solo recrear infra-replicant-docs y Backups Lab autorizados. No modificar otros servicios financieros, DNS/Cloudflare, OAuth ni datos privados.
