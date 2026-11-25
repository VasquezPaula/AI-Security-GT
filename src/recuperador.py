"""Recuperación léxica con TF-IDF y similitud coseno. No requiere red ni llaves."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .ingesta import Fragmento, cargar_fragmentos


# sklearn no trae palabras vacías en español; sin ellas «de», «con» o «un» inflan la similitud.
PALABRAS_VACIAS = [
    "a", "al", "algo", "ante", "como", "con", "cual", "cuando", "de", "del", "desde", "donde", "el",
    "ella", "en", "entre", "era", "es", "esa", "ese", "eso", "esta", "este", "esto", "fue", "ha",
    "hace", "hago", "hay", "la", "las", "le", "les", "lo", "los", "mas", "me", "mi", "mis", "muy",
    "no", "nos", "o", "para", "pero", "por", "que", "quien", "se", "ser", "si", "sin", "sobre",
    "su", "sus", "te", "tiene", "tu", "tus", "un", "una", "uno", "unos", "unas", "y", "ya", "yo",
    "cual", "cuales", "cuanto", "debo", "puedo", "hacer", "hacen",
]


class Recuperador:
    def __init__(self, fragmentos=None):
        self.fragmentos = fragmentos or cargar_fragmentos()
        self._vectorizador = TfidfVectorizer(
            strip_accents="unicode", lowercase=True, sublinear_tf=True, ngram_range=(1, 2),
            stop_words=PALABRAS_VACIAS,
        )
        # El título y la sección ayudan a ubicar el fragmento correcto.
        textos = [f"{f.titulo}. {f.seccion}. {f.texto}" for f in self.fragmentos]
        self._matriz = self._vectorizador.fit_transform(textos)

    def buscar(self, consulta: str, k: int = 3):
        """Devuelve [(Fragmento, puntaje)] ordenado de mayor a menor similitud."""
        vector = self._vectorizador.transform([consulta])
        puntajes = cosine_similarity(vector, self._matriz).ravel()
        orden = puntajes.argsort()[::-1][:k]
        return [(self.fragmentos[i], float(puntajes[i])) for i in orden]
