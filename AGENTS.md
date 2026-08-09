# Contrato operativo de Replicant Lab

## Alcance y precedencia

Estas reglas se aplican a todo el repositorio. Las instrucciones explícitas del encargo actual y las reglas superiores de la plataforma prevalecen sobre este archivo. Si aparece un `AGENTS.md` más específico en un subdirectorio, también se aplica dentro de su alcance.

## Fuentes de verdad

- El contenido técnico versionado del repositorio es la fuente de verdad técnica reproducible.
- La documentación MkDocs del proyecto —incluidos `mkdocs.yml`, `docs/` y sus recursos— es la referencia canónica de contenido, estructura y presentación documental.
- La instancia publicada en Nexus debe reflejar fielmente esa documentación MkDocs.
- Los HTML/PDF descargables, las exportaciones y los archivos adjuntos son artefactos derivados, no fuentes de verdad ni referencias prioritarias.
- Ningún `index.html` exportado, externo o antiguo debe emplearse como plantilla ni prevalecer sobre la documentación MkDocs del proyecto.
- Los artefactos derivados deben mantenerse sincronizados con la documentación MkDocs mediante un proceso reproducible cuando exista o sea implementado.
- Antes de actuar, comprueba el remoto correcto, actualiza `origin/main`, revisa rama, divergencia y working tree, y lee la documentación e instrucciones aplicables.
- Contrasta Git con el estado desplegado cuando el encargo lo autorice. Si difieren, registra estado esperado, estado observado e impacto; no elijas silenciosamente una versión.

## Entornos y aplicaciones

- Replicant/Hyper-V es el host físico y puesto de administración; Nexus es el laboratorio privado; DigitalOcean es producción.
- Cada aplicación tiene su propio repositorio, instrucciones, arquitectura, datos y ciclo de despliegue. No mezcles ni extrapoles contexto, código, secretos o procedimientos entre aplicaciones.
- Identifica siempre el entorno objetivo y diferencia expresamente entre `implementado`, `probado localmente`, `validado en Nexus` y `validado en producción`.

## Flujo de cambios

- Respeta el working tree existente. Conserva los cambios del usuario y nunca los descartes, sobrescribas o mezcles sin identificarlos y obtener dirección cuando sea necesario.
- El flujo normal es: `origin/main` actualizado, rama de alcance único, cambio, pruebas, revisión del diff, commit, push, Pull Request, revisión y merge.
- No hagas commit, push, PR, merge, despliegue ni otras escrituras externas salvo que el encargo lo autorice.
- No despliegues, modifiques producción, ejecutes migraciones ni realices acciones destructivas o irreversibles sin autorización expresa y comprobación previa del objetivo, backup y rollback cuando proceda.

## Seguridad y datos

- Nunca muestres ni versiones contraseñas, tokens, claves, cookies, credenciales o valores sensibles.
- Mantén fuera de Git bases de datos, `.env`, backups, datos vivos, estado de integraciones, archivos locales y cualquier material privado excluido por el repositorio.
- Verifica solo existencia, nombre, permisos o ubicación esperada de secretos cuando sea suficiente; no leas ni expongas su contenido.
- Protege los cambios ajenos y aplica mínimo privilegio. No cambies accesos, firewall, DNS, certificados, usuarios o visibilidad del repositorio sin autorización explícita.

## Contradicciones y cierre

- Resuelve dudas mediante evidencia del repositorio, historial, CI y estado observado autorizado. Si una contradicción requiere una decisión funcional o de riesgo, detente y solicita dirección.
- No declares validado lo que solo esté implementado o inspeccionado. Conserva los pendientes reales hasta que exista evidencia de cierre.
- Cada entrega debe indicar: estado encontrado, cambios realizados, pruebas y resultados, riesgos o contradicciones, pendientes, siguiente paso y acciones no realizadas por falta de autorización.
- Confirma expresamente repositorio, rama/SHA cuando aplique y que no se modificaron entornos, datos o sistemas fuera del alcance autorizado.
