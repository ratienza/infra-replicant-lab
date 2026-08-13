# Operación · SSH

## Desde Replicant

```powershell
ssh raul@nexus
ssh docean
```

`ssh raul@nexus` es la referencia operativa principal. El alias corto puede depender de la configuración SSH local y no debe darse por supuesto.

## Configuración conceptual

```text
Host nexus
    HostName 192.168.18.220
    User raul
    IdentityFile C:\Users\raul\.ssh\nexus_local
    IdentitiesOnly yes

Host docean
    HostName app.raulatienza.com
    User root
    IdentityFile C:\Users\raul\.ssh\reserva_pistas_do
    IdentitiesOnly yes
```

## Claves

- `nexus_local`: Replicant → Nexus.
- `reserva_pistas_do`: Replicant → DigitalOcean.
- `~/.ssh/id_ed25519` en Nexus: Nexus → GitHub.

!!! danger "Nunca documentar"
    No almacenar en este repo claves privadas, tokens, contraseñas ni el contenido de secretos.
