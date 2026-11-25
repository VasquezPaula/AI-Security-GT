# Playbook: Escalada de privilegios

Categoría de alerta: **escalada_privilegios**. Documento sintético de la Organización Ejemplo.

## Descripción
Una cuenta o proceso obtiene permisos superiores a los asignados, mediante errores de configuración, vulnerabilidades o abuso de credenciales.

## Indicadores típicos
- Una cuenta de usuario estándar se agrega a un grupo de administradores.
- Ejecución de herramientas de volcado de credenciales.
- Creación de nuevas cuentas con privilegios fuera de un cambio aprobado.
- Servicios nuevos instalados con permisos de sistema.

## Severidad
Alta por defecto, porque suele indicar un intruso ya dentro de la red.

## Pasos de triage
1. Comprobar si existe un cambio aprobado que explique el aumento de permisos.
2. Revisar qué hizo la cuenta después de obtener los permisos.
3. Revertir los permisos y deshabilitar la cuenta si no hay justificación.
4. Revisar otras cuentas modificadas en el mismo intervalo.

## Escalamiento
Escalar de inmediato a respuesta a incidentes.
