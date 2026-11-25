# Playbook: Phishing

Categoría de alerta: **phishing**. Documento sintético de la Organización Ejemplo.

## Descripción
Correo, mensaje o enlace que suplanta a una entidad legítima para obtener credenciales, pagos o que el usuario ejecute un adjunto.

## Indicadores típicos
- Remitente con dominio parecido al corporativo (typosquatting).
- Enlace acortado o que redirige a un formulario de inicio de sesión externo.
- Asunto con urgencia: "su cuenta será suspendida", "factura pendiente".
- Adjuntos con macros o archivos comprimidos protegidos con clave.

## Severidad
Media por defecto. Alta si el usuario hizo clic y ingresó credenciales, o si el destinatario es personal directivo o de finanzas.

## Pasos de triage
1. Verificar cabeceras del correo y reputación del dominio remitente.
2. Confirmar cuántos usuarios recibieron el mismo mensaje.
3. Revisar si hubo clics en el enlace o apertura del adjunto.
4. Si hubo ingreso de credenciales, forzar cambio de contraseña y cerrar sesiones activas.

## Escalamiento
Escalar al analista de nivel 2 si hubo clic con credenciales. Notificar a Comunicaciones si el correo suplanta a la organización.
