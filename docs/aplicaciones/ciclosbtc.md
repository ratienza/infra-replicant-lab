# CiclosBTC

Observatorio privado de ciclos de Bitcoin. Incluye reloj, histórico, hitos y un simulador de escenarios. Consulta los [supuestos del modelo](https://github.com/ratienza/ciclosbtc/blob/main/docs/MODELO.md).

| Elemento | Estado |
| --- | --- |
| Código | [ratienza/ciclosbtc](https://github.com/ratienza/ciclosbtc), versión 1.1.0 y commit de referencia `892cb01` |
| Destino | Nexus mediante Docker Compose |
| Origen | Puerto local pendiente de comprobar en Nexus |
| Acceso externo previsto | `ciclos.thereplicantlab.com`, Tunnel `replicant-launch` y política Access independiente |
| Launch | Tarjeta preparada para el catálogo interno. Publicación después de verificar el acceso |
| API de Claude | Pendiente. La interfaz permite preparar y copiar preguntas |

## Despliegue y verificación

1. En Nexus, comprobar el estado de Docker y el túnel, elegir un puerto libre y verificar la ruta del checkout antes de crear el servicio. Si ya existe una instancia, guardar el estado y registrar el commit y la imagen anteriores.
2. Construir desde el commit aprobado con la [variante Compose de la aplicación](https://github.com/ratienza/ciclosbtc/blob/main/docker-compose.app-only.yml). Mantener el bind en loopback para el conector local y ajustar el puerto si está ocupado. Mantener los datos y la configuración fuera de Git. Dejar `ANTHROPIC_API_KEY` sin valor, `AI_REVIEWS=off` y el modo de precios simulados desactivado.
3. Verificar HTTP 200 en el origen y consultar `/healthz`. Distinguir `ok` de `ready`, revisar `closesReady`, `spotReady`, `gaps` y confirmar `ai: false`. Registrar los resultados observados antes de publicar.
4. Crear la aplicación Access con Google y autorización del propietario, sin bypass. Una vez aplicada la política, asociar al origen la ruta del túnel existente. Comprobar desde fuera que una sesión anónima exige autenticación y que una sesión autorizada abre CiclosBTC.
5. Publicar la ficha en App Launch de Nexus y comprobar desde el catálogo los enlaces a la aplicación y a esta documentación. Actualizar esta ficha con el puerto, SHA y resultados observados.

## Operación

Los cierres UTC y el precio intradía se consultan a Kraken y Coinbase. Si falta el último cierre, la aplicación marca la proyección en pausa. El estado se guarda en `data/state.json`.

Si falla la publicación, desactivar la ruta nueva del túnel y revertir solo el servicio y la ficha de CiclosBTC. Conservar los datos y la configuración para poder diagnosticar el fallo.
