# Moon Capital · Preventas y nodos

## Acceso vigente · 26/11/2026

Moon Capital adopta la tarjeta de acceso común de Moon Capital, con el infinito oficial
en relieve en escritorio (más de 600 px) y plano en móvil. Se mantienen la
versión funcional 1.1.0 y las credenciales y datos existentes.
Imagen de Nexus: `moon-capital:access-20261126`.

La puerta de seguridad sigue validando las credenciales en el servidor.
Se verificaron las interfaces en claro/oscuro y tres anchos, y el desbloqueo
con estados sintéticos aislados. [Publicación, pruebas y rollback](../cambios/2026-11-26.md).

## Registro anterior

Las versiones, imágenes y comprobaciones anteriores se conservan como historial.


Aplicación privada de Raúl para seguir y conciliar preventas (CHIRP, LayerZero y Bitfinity) y nodos (0G y Lumoz). Conserva la fuente y la calidad de la evidencia de cada cifra. Las consultas a las redes son de solo lectura.

| Campo | Valor |
|---|---|
| Responsable | Raúl |
| Versión | 1.1.0 · 11/11/2026 |
| Estado | Activa en Nexus, con acceso privado |
| Acceso | [Moon Capital](https://mooncapital.thereplicantlab.com/) |
| Aplicación | FastAPI, SQLite, React y Vite |
| Fuentes | Repositorio local privado, sin remoto |
| Datos en Nexus | `/opt/data/moon-capital/moon.db` y ficheros asociados |
| Copia local verificada | `/opt/backups/moon-capital/activa-20261111T132020Z.db` |
| Salud | `/api/health` en el origen local de Nexus |

## Accesos

- **Aplicación:** [Moon Capital](https://mooncapital.thereplicantlab.com/).
- **Ficha técnica:** [HTML autocontenido](/downloads/apps/moon-capital.html) · [PDF](/downloads/apps/moon-capital.pdf).
- **Navegación:** [App Launch](https://launch.thereplicantlab.com/).

## Arranque y acceso

Abre Moon Capital desde el Launch privado o desde su URL HTTPS. Cloudflare Access solicita el inicio de sesión con Google. En la pantalla de Moon Capital, activa **Código largo o contraseña** y usa la credencial individual.

En Nexus, desde `/opt/apps/moon-capital`, se gestiona con `docker compose -f deploy/compose.yaml`. El backend escucha en `127.0.0.1:8765` y Nginx en `127.0.0.1:8766`. Cloudflare Tunnel conecta con el proxy. En el equipo local, `python start.py` conserva el arranque en `http://127.0.0.1:8765`.

## Datos y copias

Nexus conserva una copia SQLite coherente de la base actual del titular, con sus ajustes manuales. Se comprobó que los datos de negocio coinciden con los de la copia inicial y que la copia operativa se restaura en aislamiento. Los ficheros asociados existentes se guardan en el mismo directorio privado que la base. El registro del proxy está en `/opt/data/moon-capital/proxy-logs`.

Para nuevas capturas coherentes usa `sqlite3.Connection.backup` y verifica `PRAGMA integrity_check`. El alta gestionada en Backups Lab requiere un contrato específico y su prueba de recuperación. Las copias verificadas en este despliegue están en Nexus.

## Operación y seguridad

El refresco consulta Arbitrum y su proveedor alternativo, Bitfinity, 0G y Sui, además de CoinGecko y GeckoTerminal para precios. Los RPC configurables están en `.env.example`. La revisión mensual existente continúa fuera de la app.

El bloqueo propio admite códigos largos o contraseñas y conserva las seis casillas. Aplica pausas crecientes por IP, cierre tras 15 minutos de inactividad, cookie Secure en HTTPS y `noindex`. Nginx añade un límite por IP en `/api/auth/unlock`.

Se verificaron 72 pruebas en Windows y en la imagen de Nexus, semilla al día, redirección HTTP a HTTPS, desafío de Cloudflare Access sin sesión y API con HTTP 401 sin desbloqueo. Se comprobó en el proxy de Nexus que la nueva credencial abre sesión, que la API responde y que al cerrar se revoca la cookie. El recorrido exterior con la cuenta de Google del titular queda por comprobar en su sesión.
