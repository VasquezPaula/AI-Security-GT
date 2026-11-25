# Playbook: Exfiltración de datos

Categoría de alerta: **exfiltracion**. Documento sintético de la Organización Ejemplo.

## Descripción
Salida no autorizada de información de la organización hacia destinos externos, por red, correo, almacenamiento en la nube o medios extraíbles.

## Indicadores típicos
- Volumen de subida muy superior al habitual para un usuario o servidor.
- Transferencias hacia servicios de almacenamiento personal en la nube.
- Archivos comprimidos y protegidos con clave enviados fuera de horario.
- Consultas masivas a una base de datos seguidas de una conexión externa.

## Severidad
Alta cuando los datos son clasificados como confidenciales. Media si el destino es un servicio permitido por política pero con volumen anómalo.

## Pasos de triage
1. Determinar qué datos se movieron y su clasificación.
2. Identificar usuario, equipo y destino de la transferencia.
3. Bloquear el destino en el proxy si no está autorizado.
4. Conservar los registros de red y del proxy de las últimas 72 horas.

## Escalamiento
Escalar a respuesta a incidentes y al área legal si los datos son confidenciales.
