"""
Módulo de utilidades y funciones auxiliares para el proyecto de análisis de texto.
"""

from typing import Dict, List, Any, Tuple
import subprocess
import sys
import importlib


def verificar_e_instalar_dependencias() -> Dict[str, bool]:
    """
    Verifica e instala las dependencias necesarias para el proyecto de NLP.

    Returns:
        Dict[str, bool]: Diccionario con el estado de instalación de cada paquete
    """
    paquetes_requeridos: List[str] = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "nltk",
        "wordcloud",
        "textblob",
        "spacy",
        "scikit-learn",
    ]

    estado_instalacion: Dict[str, bool] = {}
    paquetes_faltantes: List[str] = []

    print("Verificando dependencias...")
    print("-" * 50)

    for paquete in paquetes_requeridos:
        try:
            importlib.import_module(paquete)
            print(f"✓ {paquete}: Instalado")
            estado_instalacion[paquete] = True
        except ImportError:
            print(f"✗ {paquete}: No encontrado")
            estado_instalacion[paquete] = False
            paquetes_faltantes.append(paquete)

    if paquetes_faltantes:
        print(f"\nInstalando paquetes faltantes: {', '.join(paquetes_faltantes)}")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", *paquetes_faltantes, "--quiet"]
            )
            print("✓ Instalación completada exitosamente")

            # Verificar nuevamente después de la instalación
            for paquete in paquetes_faltantes:
                try:
                    importlib.import_module(paquete)
                    estado_instalacion[paquete] = True
                    print(f"✓ {paquete}: Ahora disponible")
                except ImportError:
                    estado_instalacion[paquete] = False
                    print(f"✗ {paquete}: Error en la instalación")

        except subprocess.CalledProcessError as e:
            print(f"✗ Error durante la instalación: {e}")

    print("\n" + "=" * 50)
    return estado_instalacion


def descargar_recursos_nltk() -> Dict[str, bool]:
    """
    Descarga todos los recursos necesarios de NLTK para el análisis de texto.

    Returns:
        Dict[str, bool]: Estado de descarga de cada recurso
    """
    import nltk

    recursos_nltk: List[str] = [
        "names",
        "wordnet",
        "webtext",
        "stopwords",
        "averaged_perceptron_tagger",
        "punkt",
        "opinion_lexicon",
        "vader_lexicon",
        "averaged_perceptron_tagger_eng",
    ]

    estado_descarga: Dict[str, bool] = {}
    print("Descargando recursos de NLTK...")
    print("-" * 40)

    for recurso in recursos_nltk:
        try:
            nltk.download(recurso, quiet=True)
            print(f"✓ {recurso}: Descargado")
            estado_descarga[recurso] = True
        except Exception as e:
            print(f"✗ {recurso}: Error - {str(e)}")
            estado_descarga[recurso] = False

    print("\n* Descarga de recursos NLTK completada")
    return estado_descarga


def mostrar_progreso(mensaje: str, progreso: int, total: int) -> None:
    """
    Muestra una barra de progreso simple.

    Args:
        mensaje (str): Mensaje a mostrar
        progreso (int): Progreso actual
        total (int): Total de elementos
    """
    porcentaje: float = (progreso / total) * 100
    barra: str = "█" * int(porcentaje // 5) + "░" * (20 - int(porcentaje // 5))
    print(f"\r{mensaje}: [{barra}] {porcentaje:.1f}%", end="", flush=True)

    if progreso == total:
        print()  # Nueva línea al completar


def calcular_metricas_texto(tokens: List[str]) -> Dict[str, Any]:
    """
    Calcula métricas básicas de un conjunto de tokens.

    Args:
        tokens (List[str]): Lista de tokens

    Returns:
        Dict[str, Any]: Diccionario con métricas calculadas
    """
    if not tokens:
        return {
            "total_tokens": 0,
            "tokens_unicos": 0,
            "riqueza_lexica": 0.0,
            "longitud_promedio": 0.0,
        }

    total_tokens: int = len(tokens)
    tokens_unicos: int = len(set(tokens))
    riqueza_lexica: float = tokens_unicos / total_tokens
    longitud_promedio: float = sum(len(token) for token in tokens) / total_tokens

    return {
        "total_tokens": total_tokens,
        "tokens_unicos": tokens_unicos,
        "riqueza_lexica": riqueza_lexica,
        "longitud_promedio": longitud_promedio,
    }


def formatear_numero(numero: int) -> str:
    """
    Formatea un número con separadores de miles.

    Args:
        numero (int): Número a formatear

    Returns:
        str: Número formateado
    """
    return f"{numero:,}"


def validar_entrada_texto(texto: str, longitud_minima: int = 10) -> Tuple[bool, str]:
    """
    Valida que un texto cumple con los criterios mínimos.

    Args:
        texto (str): Texto a validar
        longitud_minima (int): Longitud mínima requerida

    Returns:
        Tuple[bool, str]: (Es válido, mensaje de error si aplica)
    """
    if not texto:
        return False, "El texto no puede estar vacío"

    if len(texto.strip()) < longitud_minima:
        return False, f"El texto debe tener al menos {longitud_minima} caracteres"

    return True, ""
