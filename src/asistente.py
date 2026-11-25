"""Asistente SOC (hito 1): responde preguntas sobre los playbooks y registra cada consulta.

Uso:
    python -m src.asistente "¿Qué hago ante un correo con un enlace a un formulario de inicio de sesión?"
    python -m src.asistente            # modo interactivo
"""
import sys

from . import llm
from .config import TOP_K, UMBRAL_RELEVANCIA
from .recuperador import Recuperador
from .registro import registrar_evento

MENSAJE_SIN_CONTEXTO = (
    "No encontré documentos del corpus que respondan esa pregunta. "
    "Reformúlala con términos de alertas de seguridad (phishing, malware, fuerza bruta, etc.)."
)


class Asistente:
    def __init__(self, recuperador=None, usar_llm=True, archivo_registro=None):
        self.recuperador = recuperador or Recuperador()
        self.usar_llm = usar_llm and llm.disponible()
        self.archivo_registro = archivo_registro

    def responder(self, consulta: str) -> dict:
        recuperados = self.recuperador.buscar(consulta, k=TOP_K)
        relevantes = [(f, p) for f, p in recuperados if p >= UMBRAL_RELEVANCIA]

        if not relevantes:
            modo, respuesta = "sin_contexto", MENSAJE_SIN_CONTEXTO
        elif self.usar_llm:
            try:
                respuesta, modo = llm.generar(consulta, relevantes), "gemini"
            except RuntimeError as error:
                respuesta, modo = self._extractiva(relevantes), "extractivo"
                respuesta += f"\n\n(Nota: {error}; se muestra el texto recuperado sin generación.)"
        else:
            modo, respuesta = "extractivo", self._extractiva(relevantes)

        evento = registrar_evento(
            consulta, recuperados, herramientas=[], respuesta=respuesta, modo=modo,
            archivo=self.archivo_registro,
        )
        return {"respuesta": respuesta, "modo": modo, "recuperados": recuperados, "evento": evento}

    @staticmethod
    def _extractiva(relevantes) -> str:
        """Sin LLM: devuelve los fragmentos recuperados con su fuente."""
        return "\n\n".join(f"[{f.documento}] {f.seccion}:\n{f.texto}" for f, _ in relevantes)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    asistente = Asistente()
    print(f"Modo: {'Gemini' if asistente.usar_llm else 'extractivo (sin GEMINI_API_KEY)'}\n")
    if argv:
        print(asistente.responder(" ".join(argv))["respuesta"])
        return
    print("Escribe tu pregunta (línea vacía para salir).")
    while True:
        consulta = input("\n> ").strip()
        if not consulta:
            break
        print("\n" + asistente.responder(consulta)["respuesta"])


if __name__ == "__main__":
    main()
