# Despliegue · Git

## Flujo normal

```mermaid
flowchart LR
    M[main estable] --> B[Nueva rama]
    B --> C[Commits]
    C --> P[Push]
    P --> PR[Pull Request]
    PR --> MR[Merge]
    MR --> M2[main actualizado]
    M2 --> H[git pull en host]
```

## Convención de ramas para esta documentación

Las ramas representan **cambios lógicos**, no archivos individuales.

Ejemplos:

- `docs/bootstrap-infra`
- `docs/app-salones`
- `docs/app-cartera`
- `docs/network`
- `docs/backups`

## Regla

!!! important "Main"
    `main` debe representar siempre la documentación aprobada y coherente con el estado real.
