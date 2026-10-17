# Host · Nexus

| Campo | Valor |
|---|---|
| Hostname | `nexus` |
| SO | Ubuntu Server 24.04.4 LTS |
| IP | `192.168.18.220/24` |
| Gateway | `192.168.18.1` |
| Interfaz | `eth0` |
| MAC | `00:15:5d:12:7b:00` |
| Plataforma | VM Hyper-V Gen2 |
| Acceso | `ssh raul@nexus` |
| Función | Laboratorio Linux, Docker, servicios internos y copias de consulta |

## Software base

- OpenSSH Server.
- Docker Engine CE.
- Docker Compose.
- Git.
- UFW.
- Nano.
- unattended-upgrades.

## Estructura

```text
/opt/apps      repositorios y aplicaciones
/opt/data      datos persistentes
/opt/backups   copias
/opt/compose   composiciones separadas si hacen falta
/opt/secrets   secretos y .env fuera de Git
```

## Seguridad

!!! success "Estado"
    SSH por clave, UFW activo y actualizaciones automáticas de seguridad habilitadas.

## Puertos conocidos

| Puerto | Uso | Ámbito |
|---|---|---|
| `22/tcp` | SSH | LAN |
| `80/tcp` | App Launch | LAN |
| `8080/tcp` | Libre | Sin listener |
| `8081/tcp` | Salones AV | LAN |
| `8082/tcp` | Replicant Lab · Nginx estático | LAN |
| `8083/tcp` | Reserva-Pistas-UTP · Nginx | LAN |
| `8084/tcp` | Control Red · demo Docker read-only | LAN |
| `8085/tcp` | Cartera Estratégica · Streamlit | LAN |
| `8516/tcp` | CryptoWallet V1.6.11 · producción privada | localhost; Tunnel |
| `8517/tcp` | CryptoWallet · previa independiente | localhost; Tunnel |
| `53` | systemd-resolved | localhost |

## Estado observado el 13/08/2026

- Docker y `unattended-upgrades` activos.
- Replicant Lab ejecutándose como sitio estático en Nginx, construido desde el `Dockerfile` y publicado en `192.168.18.220:8082 → 80`, sin bind mounts ni servidor de desarrollo.
- Salones AV accesible mediante Nginx en `192.168.18.220:8081`; checkout limpio e idéntico a GitHub `main` en `8c0bc08` después de la Fase 2A.
- Reserva-Pistas-UTP ejecutándose como backend privado y proxy Nginx en `192.168.18.220:8083`, con autenticación, datos persistentes separados y canal saliente SSH restringido hacia DigitalOcean.
- App Launch ejecutándose en el puerto `80` mediante Nginx `1.27-alpine`, con sitio y configuración montados en solo lectura.
- `8080` sin listener.
- En esta observación del 13/08, CV y Control de Red estaban presentes solo como checkouts; el cambio posterior de Control Red queda registrado en la actualización del 30/08.
- Consumos Cupra y Cartera Estratégica sin checkout servido ni puerto Nexus.
- La tarjeta PULA de App Launch apunta a la publicación pública externa y fue validada en el catálogo Nexus `2d265ee`; no implica ejecución de PULA en Nexus.

Esta observación confirma el estado del laboratorio privado en esa fecha. DigitalOcean se validó por separado y de forma acotada para el cierre de Reserva-Pistas-UTP; cada repositorio conserva sus definiciones operativas.

## Actualización del 30/08/2026

Control Red incorpora un demo Docker separado del panel operativo. `control-red-demo` publica exclusivamente `192.168.18.220:8084:8084`, monta `/proc/net/arp` en solo lectura y no persiste inventarios ni resultados. El checkout de Nexus quedó limpio en `control-red@d3a05ac`; se verificaron `/` y `/health` con HTTP `200` desde la LAN. Esta actualización sustituye únicamente la observación histórica del 13/08/2026 que describía Control Red como checkout sin servicio.

## Runtime documental validado en Nexus

El PR #9 fusionado sustituye `mkdocs serve` y los bind mounts por una imagen construida desde el `Dockerfile`: MkDocs estricto en la etapa builder y Nginx estático en runtime, manteniendo `192.168.18.220:8082`. El 09/08/2026 se reconstruyó y recreó exclusivamente este servicio en Nexus y se validaron HTTP, navegación, recursos, cinco diagramas Mermaid y descargas HTML/PDF idénticas byte a byte a los artefactos versionados. El HTML funciona offline sin dependencias esenciales externas y el PDF conserva la documentación completa.

## Cartera Estratégica · estado histórico 12/09/2026

Cartera Estratégica v1.0.0 se ejecuta en Nexus mediante el proyecto Docker Compose `cartera-estrategica`, con `restart: unless-stopped` y bind LAN `192.168.18.220:8085`. La aplicación responde HTTP `200` y se publica mediante el Tunnel y Cloudflare Access; después exige Google OIDC interno y PIN de seis cifras. App Launch conserva su tarjeta LAN sin cambios. La SQLite real fue copiada de forma consistente, validada en staging y promovida con backup recuperable; datos, secretos y backups permanecen fuera de Git.

CE-SEC-001 está desplegado: PIN independiente y Google OIDC preparado. Durante la etapa LAN Google continúa desactivado y sin URL, callback ni secretos OAuth; el PIN solo puede configurarlo el usuario desde `Configuración → Seguridad → PIN`.

Esta actualización sustituyó exclusivamente la observación histórica del 13/08/2026 que indicaba que Cartera no tenía checkout servido ni puerto Nexus. La mención anterior a Google desactivado describe solo aquella etapa, no el estado actual.

## Cartera Estratégica · v2.0.0, comprobación 04/10/2026

`main`, tag y release `v2.0.0` del repositorio de Cartera señalan `c672eb1cadfcb191aaff6db8aeb1ed783321b692`. El checkout productivo y la etiqueta OCI del contenedor saludable en `:8085` mostraron ese SHA; HTTP respondió `200`. Google OAuth interno y PIN están activos. La base SQLite privada real está montada mediante `CARTERA_DB_PATH`: `cartera-demo.db` es un nombre heredado, no una base demo. Este cierre documental no recrea el contenedor de Cartera ni toca su base. [Ficha vigente](../aplicaciones/cartera-estrategica.md).

## Cloudflare Tunnel y Access · actualización 06/09/2026

`cloudflared` está instalado, activo y habilitado en Nexus. El Tunnel único `replicant-launch` publica seis servicios mediante hostnames separados: Launch (`:80`), Salones (`:8081`), documentación (`:8082`), Pádel (`:8083`) y Control de Red (`:8084`) y Cartera (`:8085`).

Google está configurado como IdP de Cloudflare Access. Cada hostname tiene una aplicación y una política Access independientes; el Tunnel transporta tráfico y Access aplica la autorización. El router no expone puertos entrantes para esta arquitectura.

El acceso LAN a `80`, `8081`, `8082`, `8083`, `8084` y `8085` no cambia y no pasa por Cloudflare. Tokens, secretos OAuth y configuración sensible permanecen fuera de Git.

## CryptoWallet · actualización 08/10/2026

V1.0 aceptada y promovida: `cryptowallet-app`, imagen `cryptowallet:1.0.0-5e7c3d79`, origen `127.0.0.1:8516 → 8501`, producción privada de esta aplicación. `cryptowallet-preview-app` sigue saludable en localhost `8517`, con copia real y demo ficticia separadas. Producción monta solo su conjunto real; ningún movimiento sintético se promueve. Copia consistente puntual verificada en Nexus y segunda ubicación privada.

Ambos hostnames externos redirigen a Access sin sesión; cloudflared activo/habilitado. No se inspeccionó el panel administrativo de políticas. El mantenimiento documental no reinicia estos contenedores ni toca las bases. [Ficha y recuperación compatible](../aplicaciones/cryptowallet.md).


## CryptoWallet · V1.5, promoción registrada 09/10/2026

La evidencia privada de CW-V15 sustituye únicamente la identidad productiva histórica anterior: tag `v1.5.0`, ejecutable `d7aac669b5f905933558c3a7ffa7b42cdae9741e`, imagen `cryptowallet:1.5.0-d7aac669b5f9`, usuario `1000:1000`, contenedor healthy y origen localhost `8516`. Previa `8517` independiente, sin promoción de datos sintéticos.

En la promoción inicial, PIN activo y persistente 24 horas, privacidad inicial ON y Google interno OFF. Este estado es histórico. Datos, copias multibase y seguridad persisten en montajes privados separados; retención efectiva 7 diarias / 10 manuales / 10 previas y protegidas conservadas. Restauración comprobada en aislamiento y 27 componentes financieros idénticos antes/después. Access/Tunnel se mantienen; 302 exterior no acredita sesión autenticada. [Ficha y fuentes](../aplicaciones/cryptowallet.md).

Esta actualización documental consulta la aceptación versionada, sin nueva inspección remota de Nexus. La publicación de la documentación tiene su propio gate en [RL-CW-DOC-002](../encargos/RL-CW-DOC-002.md). Esta observación era histórica: [Backups Lab v1.1.3](../aplicaciones/backups-lab.md) es ahora el servicio de nueve alcances Drive en8087.

## CryptoWallet · cierre OAuth confirmado 09/10/2026 22:33

Google interno quedó activo y Raúl confirmó manualmente en incógnito Google → PIN → cartera. La documentación atribuye la prueba al propietario; no afirma una nueva inspección independiente. Se conservan PIN 24 horas, privacidad inicial ON y copias locales. Cuenta no autorizada, cancelación/error OIDC y recorrido móvil exterior no constan probados y son límites aceptados. [RL-CW-DOC-003](../encargos/RL-CW-DOC-003.md) registra la publicación documental posterior sin reiniciar CryptoWallet.

## CryptoWallet · V1.6, promoción verificada 13/10/2026

Producción ejecuta `cryptowallet:1.6.0-256cff7f490f`, SHA `256cff7f490ff67601a514848555c19d38bde48e`, usuario `1000:1000`, healthy y origen localhost `8516`. Los montajes privados de datos, copias y seguridad permanecen separados. Se verificaron copia previa protegida, rollback de composición, respaldo de seguridad, 387 pruebas dentro de la imagen sin red y salud loopback.

La migración añadió `purchase-payment.sqlite3` al conjunto multibase: dos borradores BTC quedaron como Tarjeta y alcanzaron preparación sin contabilizarse; su huella de archivos no cambió. La segunda ejecución migró 0 filas y la SQLite devolvió integridad correcta. No existía base de confirmaciones, por lo que no procede regularización histórica de liquidez. La sesión exterior existente se comprobó con privacidad activa; no se desactivó ni se expusieron importes.

## CryptoWallet · V1.6.4, cierre visual del Logbook verificado 14/10/2026

Producción ejecuta `cryptowallet:1.6.4-0111397b51ca`, SHA `0111397b51ca8b9119fdc08593eca4bd59d9b2e5`, healthy y origen localhost `8516`. Los montajes privados permanecen separados. La entrega superó 397 pruebas + 68 subpruebas. Copia previa, restauración aislada, rollback de composición y seguridad separada quedaron verificados. El estado productivo conservó 33 componentes, 2 operaciones y su huella financiera antes/después.

## CryptoWallet · V1.6.5, pesos coherentes verificados 15/10/2026

Producción ejecuta `cryptowallet:1.6.5-36d50affe9af`, SHA `36d50affe9afac059f399e75e80fabe0cf8aca56`, healthy y origen localhost `8516`. Los montajes privados permanecen separados. La entrega superó 404 pruebas localmente y dentro de la imagen aislada. Copia previa, restauración aislada, rollback de composición y seguridad separada quedaron verificados. El estado productivo conservó 33 componentes, 2 operaciones y la misma huella financiera antes/después. La ruta exterior alcanzó la puerta PIN sin leer secretos; no se declara una nueva aceptación autenticada.

## CryptoWallet · V1.6.6, revisión fiel verificada 16/10/2026

Producción ejecuta `cryptowallet:1.6.6-fe6620f00b3e`, SHA `fe6620f00b3ec7aa5425b17c40b5b5ce1844fbf0`, healthy y origen localhost `8516`. Los montajes privados permanecen separados. La entrega superó 411 pruebas dentro de la imagen final, revisión sintética claro/oscuro/móvil/confidencialidad y comprobación productiva autenticada sin confirmar una operación. Copia previa, restauración aislada, rollback de composición y seguridad separada quedaron verificados. El estado productivo conservó 33 componentes, 2 operaciones y la misma huella financiera antes/después.

## CryptoWallet · V1.6.7, justificantes reales verificados 16/10/2026

Producción ejecuta `cryptowallet:1.6.7-592a325be9ea`, SHA `592a325be9ea94cdc8780c7dfbda630b462434a1`, healthy y origen localhost `8516`. Los montajes privados permanecen separados. La entrega superó 417 pruebas y 68 subpruebas localmente, más 417 pruebas dentro de la imagen final sin red; se revisaron la compra sintética `60 EUR → 64.65556087 USDC`, claro/oscuro, formulario compacto y estado recuperable sin referencia. La sesión productiva autenticada mostró V1.6.7, privacidad activa y los cuatro gráficos, sin guardar ni confirmar una operación. Copia previa, restauración aislada, rollback de composición y seguridad separada quedaron verificados. El estado productivo conservó 33 componentes, 2 operaciones y la misma huella financiera antes/después.

## CryptoWallet · V1.6.8, borradores de valoración completables 16/10/2026

Producción ejecuta `cryptowallet:1.6.8-24895424be4d`, SHA `24895424be4d80763e9f69e8c9334641a8e683cd`, healthy y origen localhost `8516`. La entrega superó 419 pruebas y 68 subpruebas localmente, más 419 pruebas dentro de la imagen final sin red. El recorrido sintético guardó, recuperó, editó, recargó y confirmó una compra pendiente una sola vez; no se usaron datos productivos ni se confirmó una operación real. Copia previa, restauración aislada, rollback de composición y seguridad separada quedaron verificados. El estado productivo conservó 34 componentes, 2 operaciones y la misma huella financiera antes/después.

## CryptoWallet · V1.6.11, regularización estable ante compras retroactivas 17/10/2026

Producción ejecuta `cryptowallet:1.6.11-45d83c7ffc7d`, SHA `45d83c7ffc7d6267df0f8926968826de948b4b94`, healthy y origen localhost `8516`. Usuario `1000:1000`, raíz de solo lectura y montajes separados siguen activos. La entrega superó 430 pruebas locales y 430 dentro de la imagen final sin red. Dos restauraciones del estado productivo, sin red y sin montar producción, confirmaron la compra retroactiva exacta, el reintento idempotente y la recuperación del borrador existente. La regularización conserva su delta fijo, evidencia, autorización, cadena y coste desconocido; la compra real continúa pendiente. La copia previa protegida conservó 35 componentes, 5 operaciones y la misma huella financiera antes/después. Access respondió 302 anónimo; no se atribuye una nueva aceptación humana.

## Backups Lab v1.1.3 ·15/10/2026

Repositorio `/opt/apps/backups-lab`, API/web en Compose y ayudante fijo en socket Unix 0600; datos, estado, OAuth y clave privados fuera de Git. [HTTPS](https://backups.thereplicantlab.com/) y [LAN 8087](http://192.168.18.220:8087/). Runtime v1.1.3 en `1e7acbef8235faeb43ac8f7eeb07a70b24927abd`, API healthy y contratos esquema 2. Nueve aptas; CryptoWallet/Control Red con copia Drive y recuperación nuevas; previews excluidas y Facility original detenida. Retención 7/4/12/3 ON, seis horarios ON/tres OFF e historial preservados. [Ficha/manual](../aplicaciones/backups-lab.md). No equivale a respaldo integral de Nexus.

Rollback de publicación v1.1.0 y snapshot SQLite privado consistente preparados. BL-002, seis horarios ON/tres OFF y operaciones históricas de retención intactos; no se ejecutaron borrados, sustituciones ni restauraciones productivas en el cierre v1.1.1.
