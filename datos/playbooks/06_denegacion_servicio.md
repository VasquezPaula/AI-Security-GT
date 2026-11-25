# Playbook: Denegación de servicio

Categoría de alerta: **denegacion_servicio**. Documento sintético de la Organización Ejemplo.

## Descripción
Tráfico o peticiones en cantidad suficiente para degradar o interrumpir un servicio, ya sea de red (inundación de paquetes) o de aplicación (muchas peticiones costosas).

## Indicadores típicos
- Aumento súbito de peticiones por segundo hacia un mismo servicio.
- Muchas conexiones a medio abrir (inundación SYN).
- Latencia alta y errores 503 en el balanceador.
- Peticiones repetidas a un mismo endpoint de búsqueda o de inicio de sesión.

## Severidad
Alta si afecta a un servicio de cara al cliente. Media si afecta a un entorno interno o de pruebas.

## Pasos de triage
1. Distinguir un ataque de un pico legítimo, como una campaña de marketing.
2. Identificar las IP o rangos de origen principales.
3. Activar limitación de tasa o la protección del proveedor de red.
4. Informar al equipo del servicio afectado.

## Escalamiento
Escalar al equipo de redes y al proveedor de acceso a internet si la mitigación local no basta.
