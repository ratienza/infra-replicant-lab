# Aplicación · CiclosBTC

Observatorio privado de ciclos de Bitcoin de The Replicant Lab. La edición **1.1.0** procede del [commit 892cb01 de ciclosbtc](https://github.com/ratienza/ciclosbtc/tree/892cb01c0ee8d53c3e8102ac9e4c1a89f911dbb5). Incluye los logos corporativos, el favicon y la tipografía Inter versionados en el repositorio.

## Accesos

- [CiclosBTC por Cloudflare Access](https://launch.thereplicantlab.com/btc-cycle-lab/).
- [CiclosBTC en Nexus](http://192.168.18.220/btc-cycle-lab/).
- Ficha descargable en [HTML](/downloads/apps/btc-cycle-lab.html) y [PDF](/downloads/apps/btc-cycle-lab.pdf).

## Ficha de documentación

| Campo | Detalle |
|---|---|
| Runtime | Node.js en Docker en Nexus, detrás del proxy de Launch |
| Datos | Histórico incorporado hasta el 7 de noviembre de 2026. Kraken y Coinbase aportan las observaciones recientes |
| Navegación | Tarjeta «CiclosBTC» con enlace «Documentación» en Launch Nexus |
| Persistencia | Volumen `ciclosbtc-data`, estado y cierres observados |
| Claude | Activación de la API pendiente. La app permite preparar y copiar preguntas con el contexto del modelo |

## Guía de uso

Usa el reloj para consultar una fecha y comparar ciclos. Cada vuelta representa el intervalo de un halving al siguiente. En Hitos y Proyección puedes seguir los escenarios y distinguir los datos observados de las hipótesis. En Simulador puedes cambiar los supuestos sin modificar el modelo de referencia. Superpuestos, Patrones y Estacionalidad muestran las comparaciones históricas. El precio intradía se distingue de los cierres que usa el modelo. Si faltan cierres recientes, la interfaz indica el hueco y puede pausar la proyección.

- [Metodología y escenarios](https://github.com/ratienza/ciclosbtc/blob/892cb01c0ee8d53c3e8102ac9e4c1a89f911dbb5/docs/MODELO.md).
- [Documentación de la API de Claude](https://github.com/ratienza/ciclosbtc/blob/892cb01c0ee8d53c3e8102ac9e4c1a89f911dbb5/docs/API-ANTHROPIC.md).

## Operación

La ruta reutiliza el [Cloudflare Tunnel de Launch](../red/cloudflare-tunnel.md). El contenedor escucha en la red privada de Docker. Launch sirve la interfaz, la consulta de estado y el endpoint de preguntas bajo `/btc-cycle-lab/`. Comprueba la edición y la cobertura de mercado con [el estado del servicio](https://launch.thereplicantlab.com/btc-cycle-lab/healthz). El código de Claude está incluido y su configuración de credenciales queda pendiente.
