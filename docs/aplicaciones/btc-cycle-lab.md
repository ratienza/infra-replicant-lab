# Aplicación · BTC Cycle Lab

Laboratorio de análisis de los ciclos de Bitcoin con un reloj concéntrico, comparación histórica y escenarios mensuales. La edición inicial usa cierres hasta el **6 de noviembre de 2026 UTC**.

## Accesos

- [BTC Cycle Lab por Cloudflare Access](https://launch.thereplicantlab.com/btc-cycle-lab/).
- [BTC Cycle Lab en la red de Nexus](http://192.168.18.220/btc-cycle-lab/).
- Ficha descargable en [HTML](/downloads/apps/btc-cycle-lab.html) y [PDF](/downloads/apps/btc-cycle-lab.pdf).

## Ficha de documentación

| Campo | Detalle |
|---|---|
| Entorno | Nexus, sitio estático servido por el Nginx de Launch |
| Acceso remoto | Cloudflare Access de Launch |
| Acceso LAN | Nginx de Nexus, puerto 80 |
| Navegación | Tarjeta «BTC Cycle Lab» y enlace «Documentación» en Launch Nexus |
| Persistencia | HTML con datos incluidos y archivos estáticos de consulta |
| Cobertura | Cierres desde julio de 2010 y escenario condicional hasta octubre de 2030 |
| Series | Coin Metrics para cierres y Bitstamp para el contraste intradía |

## Guía de uso

1. Abre el reloj y arrastra un anillo o selecciona un ciclo. Cada vuelta comprime el intervalo entre dos halvings en 24 horas. El centro muestra la fecha elegida y la cuenta atrás al siguiente halving. La tabla compara cada anillo a la misma fracción de su ciclo.
2. Selecciona un día, semana, mes, trimestre, año o hito. Usa los botones para avanzar, retroceder o reproducir en la dirección y velocidad elegidas.
3. Consulta el gráfico mensual y los hitos. Los tramos proyectados aparecen discontinuos y los precios entre puntos mensuales se identifican como interpolados.
4. En Superpuestos, alinea las series por hora del reloj o por días desde el halving, techo o suelo. En Preguntas, consulta el modelo incluido desde el momento seleccionado.

## Auditoría y datos

- [Auditoría completa y fuentes](https://launch.thereplicantlab.com/btc-cycle-lab/auditoria.html).
- [Proyección mensual en USD](https://launch.thereplicantlab.com/btc-cycle-lab/proyeccion-mensual-btc.csv).
- [Hitos y ventanas de escenarios](https://launch.thereplicantlab.com/btc-cycle-lab/hitos-y-escenarios.csv).
- [Prompt para reproducir la auditoría](https://launch.thereplicantlab.com/btc-cycle-lab/prompt.html).

El modelo principal y los tres escenarios alternativos se presentan por separado. Los resultados futuros son condicionales y los datos permanecen en el corte indicado hasta reconstruir una edición. La consulta usa respuestas locales sobre los datos incluidos. Las fechas de halving futuras son teóricas y la muestra histórica es pequeña.

## Operación

La ruta externa reutiliza el [Cloudflare Tunnel de Launch](../red/cloudflare-tunnel.md). El directorio de publicación en Nexus es `/home/raul/app-launch/site/btc-cycle-lab/`. Para actualizar la edición, genera y valida el HTML autónomo, la auditoría y sus datos, comprueba sus sumas y activa la nueva versión como conjunto. Conserva la versión previa fuera del directorio web para poder recuperarla.
