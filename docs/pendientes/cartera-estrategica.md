# Pendientes · Cartera Estratégica

## Estado

La publicación privada está completada y validada: Cartera se mantiene operativa en Nexus, responde por LAN y su hostname público está protegido por Cloudflare Access, Google OIDC interno y PIN de seis cifras. SQLite, migraciones y datos financieros permanecen íntegros y privados.

No existe un pendiente bloqueante específico de publicación, OIDC o PIN de Cartera.

## Límites permanentes

- La URL LAN y la URL pública son rutas distintas; Cloudflare protege únicamente el hostname externo.
- La SQLite no se expone por ninguna ruta y no se almacena en Git.
- App Launch y los servicios `8081–8084` no cambiaron durante esta publicación.
- La configuración sensible y las rutas privadas no se documentan.

## Pendientes posteriores a v2.0.0

- La privacidad visual ya tiene control y máscaras en la aplicación v2.0.0; el antiguo texto que la calificaba como no implementada queda superado. Cualquier ampliación de cobertura requiere un encargo propio.
- No existe tarea autónoma diaria de refresco Indexa con la aplicación cerrada. Solo se intenta al abrir/recargar sesión o con el botón. Añadir un programador sería una mejora futura.
- Vigilar cambios en el esquema de la API oficial de Indexa sin permitir fallback silencioso a proveedores externos. Ver [contrato vigente](../aplicaciones/cartera-estrategica.md).
