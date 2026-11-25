"""Registro de eventos: una línea JSON por consulta.

Guarda la consulta, los documentos recuperados (con su puntaje), las herramientas invocadas
y la respuesta. Es la fuente de la columna «señal en el registro» del modelo de amenazas.
"""
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .config import ARCHIVO_REGISTRO


def registrar_evento(consulta, recuperados, herramientas, respuesta, modo, archivo: Path = None):
    evento = {
        "id": uuid.uuid4().hex[:12],
        "marca_de_tiempo": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "consulta": consulta,
        "documentos_recuperados": [
            {"id": f.id, "documento": f.documento, "seccion": f.seccion, "puntaje": round(p, 4)}
            for f, p in recuperados
        ],
        "herramientas_invocadas": herramientas,  # vacío en el hito 1: aún no hay agente
        "modo_respuesta": modo,  # "gemini", "extractivo" o "sin_contexto"
        "respuesta": respuesta,
    }
    destino = Path(archivo or ARCHIVO_REGISTRO)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("a", encoding="utf-8") as f:
        f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    return evento
