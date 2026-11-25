"""Configuración central. Las llaves se leen de variables de entorno (.env), nunca del código."""
import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:  # python-dotenv es opcional
    pass

RAIZ = Path(__file__).resolve().parent.parent
DIR_CORPUS = RAIZ / "datos" / "playbooks"
ARCHIVO_REGISTRO = Path(os.getenv("REGISTRO_EVENTOS", RAIZ / "registros" / "eventos.jsonl"))

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

TOP_K = int(os.getenv("TOP_K", "3"))
# Debajo de este puntaje de similitud el asistente declara que no tiene documentos relevantes.
UMBRAL_RELEVANCIA = float(os.getenv("UMBRAL_RELEVANCIA", "0.08"))
