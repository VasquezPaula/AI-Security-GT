"""Carga el corpus de playbooks y lo divide en fragmentos por sección (encabezados '##')."""
from dataclasses import dataclass
from pathlib import Path

from .config import DIR_CORPUS


@dataclass(frozen=True)
class Fragmento:
    id: str  # archivo#n
    documento: str  # nombre del archivo
    titulo: str  # título del documento
    seccion: str  # encabezado de la sección
    texto: str


def _dividir(texto: str):
    """Devuelve (titulo, [(seccion, cuerpo), ...]) a partir de un markdown simple."""
    titulo = ""
    secciones = []
    seccion_actual, lineas = "Introducción", []
    for linea in texto.splitlines():
        if linea.startswith("# ") and not titulo:
            titulo = linea[2:].strip()
        elif linea.startswith("## "):
            if "".join(lineas).strip():
                secciones.append((seccion_actual, "\n".join(lineas).strip()))
            seccion_actual, lineas = linea[3:].strip(), []
        else:
            lineas.append(linea)
    if "".join(lineas).strip():
        secciones.append((seccion_actual, "\n".join(lineas).strip()))
    return titulo, secciones


def cargar_fragmentos(directorio: Path = DIR_CORPUS):
    fragmentos = []
    for ruta in sorted(Path(directorio).glob("*.md")):
        titulo, secciones = _dividir(ruta.read_text(encoding="utf-8"))
        for n, (seccion, cuerpo) in enumerate(secciones):
            fragmentos.append(
                Fragmento(
                    id=f"{ruta.name}#{n}",
                    documento=ruta.name,
                    titulo=titulo,
                    seccion=seccion,
                    texto=cuerpo,
                )
            )
    if not fragmentos:
        raise FileNotFoundError(f"No se encontraron documentos .md en {directorio}")
    return fragmentos
