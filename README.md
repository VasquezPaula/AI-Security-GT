# AI-Security-GT · SOC Triage Assistant

Prototipo experimental, con fines educativos, de IA generativa que apoya la clasificación y el triage de alertas de un SOC a partir de su descripción. Trabajo integrador del curso **Ciberseguridad de Inteligencia Artificial** (Maestría en Ciencia de Datos, UNI).

> **Solo datos sintéticos.** El repositorio no contiene datos reales, información confidencial ni llaves.

📄 **Página del proyecto:** https://vasquezpaula.github.io/AI-Security-GT/

## Estado: hito 1

| Entregable | Archivo | Estado |
|------------|---------|--------|
| Ficha del sistema | `docs/ficha.md` | Listo |
| Arquitectura (Mermaid) | `docs/arquitectura.md` | Listo |
| Estructura del repositorio y página | `mkdocs.yml`, `.github/workflows/docs.yml` | Listo |
| Asistente que responde sobre sus documentos | `src/` | Listo |
| Modelo de amenazas, priorización, controles, evaluación, regulatorio | `docs/` | Pendiente (hito 2 y final) |

## Instalación

```bash
git clone https://github.com/VasquezPaula/AI-Security-GT.git
cd AI-Security-GT
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

```bash
python -m src.asistente "Un usuario recibió un correo con un enlace que pide iniciar sesión, ¿qué hago?"
python -m src.asistente        # modo interactivo
```

**Sin llave de API** el asistente funciona en modo *extractivo*: devuelve los fragmentos del playbook más relevantes con su fuente. **Con llave** de la API de Gemini (nivel gratuito) genera una respuesta a partir de esos fragmentos:

```bash
cp .env.example .env     # luego escribe tu llave en GEMINI_API_KEY (el archivo .env no se sube a git)
```

Cada consulta se guarda en `registros/eventos.jsonl`. Una muestra de una corrida está en `registros/muestra_hito1.jsonl`.

## Pruebas

```bash
python -m unittest -v tests.test_hito1
```

## Documentación local

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## Estructura

```
docs/            documentación y fuente de la página
src/             asistente, ingesta, recuperador, cliente LLM, registro
datos/playbooks/ corpus sintético de playbooks
controles/       controles implementados (hito final)
evaluacion/      catálogo, código y resultados de la evaluación adversarial
registros/       muestra del registro de eventos
tests/           pruebas
```
