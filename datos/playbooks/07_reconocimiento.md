# Playbook: Reconocimiento y escaneo

Categoría de alerta: **reconocimiento**. Documento sintético de la Organización Ejemplo.

## Descripción
Exploración de la red o de las aplicaciones para descubrir equipos, puertos, servicios y vulnerabilidades, normalmente previa a un ataque.

## Indicadores típicos
- Un mismo origen consulta muchos puertos o muchas direcciones en poco tiempo.
- Peticiones web a rutas típicas de administración o a archivos de configuración.
- Resolución DNS masiva de subdominios.
- Huellas de herramientas de escaneo en el campo de agente de usuario.

## Severidad
Baja si el origen es externo y no obtuvo respuesta. Media si el escaneo proviene de un equipo interno, porque puede haber un equipo comprometido.

## Pasos de triage
1. Verificar si existe un escaneo de vulnerabilidades programado por la organización.
2. Revisar la reputación del origen.
3. Si el origen es interno, identificar el equipo y su responsable.
4. Bloquear el origen externo si el escaneo es persistente.

## Escalamiento
Escalar a nivel 2 si el origen es un equipo interno sin escaneo autorizado.
