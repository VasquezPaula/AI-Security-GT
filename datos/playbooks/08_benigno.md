# Playbook: Alerta benigna o falso positivo

Categoría de alerta: **benigno**. Documento sintético de la Organización Ejemplo.

## Descripción
Alerta generada por una actividad legítima: pruebas autorizadas, mantenimiento, errores de usuario o reglas demasiado sensibles.

## Indicadores típicos
- La actividad coincide con una ventana de mantenimiento o un cambio aprobado.
- Un usuario olvidó su contraseña y generó varios fallos seguidos, sin acceso exitoso posterior.
- Herramientas de administración conocidas ejecutadas por el equipo de TI.
- La misma alerta se repite a diario sin ningún impacto observado.

## Severidad
Informativa.

## Pasos de triage
1. Cotejar la alerta con el calendario de cambios y mantenimientos.
2. Confirmar con el responsable del equipo o del usuario.
3. Cerrar la alerta indicando el motivo.
4. Si la regla genera ruido repetido, proponer su ajuste al equipo de detección.

## Escalamiento
No requiere escalamiento. Registrar el cierre y la justificación.
