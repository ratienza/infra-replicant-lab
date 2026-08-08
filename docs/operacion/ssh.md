# Operación · SSH

## Desde Replicant

```powershell
ssh nexus
ssh docean
```

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
