# Ficha del sistema

## Para qué sirve y a quién
**SOC Triage Assistant** apoya a analistas de un centro de operaciones de seguridad (SOC) en el triage de alertas. A partir de la descripción de una alerta, el producto la clasifica por tipo (phishing, malware, fuerza bruta, exfiltración, escalada de privilegios, denegación de servicio, reconocimiento o benigna) y consulta los playbooks de la organización para indicar severidad y pasos de atención.

Es un prototipo académico: corre en local o en Colab, no se despliega en internet y no se conecta a ningún SIEM real.

## Componentes

| Componente | Descripción | Sesión del curso | Estado |
|------------|-------------|------------------|--------|
| Asistente con modelo de lenguaje (obligatorio) | Responde preguntas sobre los playbooks recuperando fragmentos del corpus y generando la respuesta con Gemini | 3 y 4 | **Hito 1: funciona** |
| Clasificador de *machine learning* | Asigna una categoría a la descripción de una alerta | 2 | Hito 2 |
| Agente con herramientas | Abre tickets según la clasificación | 5 | Por decidir (el curso exige tres de cuatro componentes) |
| Memoria o varios agentes | Fuera del alcance previsto | 6 | No previsto |

## Datos y su origen
- **Corpus de playbooks** (`datos/playbooks/`): 9 documentos escritos para este proyecto, para una «Organización Ejemplo» ficticia. No provienen de ninguna empresa real.
- **Alertas** (hito 2): se generarán de forma sintética con descripciones inventadas.
- **No hay** datos personales, nombres de clientes ni arquitecturas internas reales.

## Quién lo usa y con qué permisos

| Rol | Qué puede hacer | Qué no puede hacer |
|-----|-----------------|--------------------|
| Analista SOC | Enviar preguntas y leer respuestas | Modificar el corpus ni el registro |
| Autor de playbooks | Agregar o editar los `.md` del corpus | — |
| Producto (proceso local) | Leer el corpus, escribir el registro, llamar a la API de Gemini | Ejecutar acciones sobre otros sistemas (en el hito 1 no hay herramientas) |

## Registro de eventos
Cada consulta queda en `registros/eventos.jsonl` con la pregunta, los documentos recuperados y su puntaje, las herramientas invocadas y la respuesta. Una muestra está en `registros/muestra_hito1.jsonl`.
