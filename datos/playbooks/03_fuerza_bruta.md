# Playbook: Fuerza bruta y acceso no autorizado

Categoría de alerta: **fuerza_bruta**. Documento sintético de la Organización Ejemplo.

## Descripción
Intentos repetidos de autenticación para adivinar credenciales, o inicio de sesión con credenciales válidas desde un contexto anómalo.

## Indicadores típicos
- Decenas de inicios de sesión fallidos en pocos minutos contra una misma cuenta o contra muchas cuentas con una misma contraseña (password spraying).
- Inicio de sesión exitoso inmediatamente después de una racha de fallos.
- Acceso desde un país o proveedor de VPN que el usuario nunca usó.
- Viaje imposible: dos inicios de sesión lejanos en un intervalo corto.

## Severidad
Media si todos los intentos fallaron. Alta si hubo un acceso exitoso tras la racha de fallos o si la cuenta es privilegiada.

## Pasos de triage
1. Revisar el origen de las IP y si coinciden con listas de reputación.
2. Confirmar con el usuario si reconoce el acceso.
3. Si hubo acceso exitoso, restablecer la contraseña y revocar tokens de sesión.
4. Verificar que la cuenta tenga autenticación multifactor.

## Escalamiento
Escalar a nivel 2 si la cuenta tiene privilegios de administración.
