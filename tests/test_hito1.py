import json
import tempfile
import unittest
from pathlib import Path

from src.asistente import Asistente
from src.ingesta import cargar_fragmentos
from src.recuperador import Recuperador


class PruebasHito1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.recuperador = Recuperador()

    def test_corpus_cargado(self):
        fragmentos = cargar_fragmentos()
        documentos = {f.documento for f in fragmentos}
        self.assertEqual(len(documentos), 9)

    def test_recupera_documento_correcto(self):
        casos = {
            "correo con enlace que pide iniciar sesión y suplanta al banco": "01_phishing.md",
            "archivos cifrados y extensión desconocida en un equipo": "02_malware.md",
            "muchos inicios de sesión fallidos contra una cuenta": "03_fuerza_bruta.md",
            "subida masiva de archivos a la nube personal": "04_exfiltracion.md",
            "tiempo de primera revisión para severidad alta": "09_politica_severidad.md",
        }
        for consulta, esperado in casos.items():
            with self.subTest(consulta=consulta):
                mejor, _ = self.recuperador.buscar(consulta, k=1)[0]
                self.assertEqual(mejor.documento, esperado)

    def test_registro_de_eventos(self):
        with tempfile.TemporaryDirectory() as tmp:
            archivo = Path(tmp) / "eventos.jsonl"
            asistente = Asistente(self.recuperador, usar_llm=False, archivo_registro=archivo)
            asistente.responder("¿Cómo triagear un phishing?")
            lineas = archivo.read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(lineas), 1)
            evento = json.loads(lineas[0])
            for campo in ("consulta", "documentos_recuperados", "herramientas_invocadas", "respuesta"):
                self.assertIn(campo, evento)

    def test_pregunta_fuera_de_tema(self):
        with tempfile.TemporaryDirectory() as tmp:
            asistente = Asistente(self.recuperador, usar_llm=False, archivo_registro=Path(tmp) / "e.jsonl")
            resultado = asistente.responder("receta de ceviche con camote")
            self.assertEqual(resultado["modo"], "sin_contexto")


if __name__ == "__main__":
    unittest.main()
