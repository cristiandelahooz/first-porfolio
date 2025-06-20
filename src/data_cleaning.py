"""
Módulo para limpieza avanzada y sistemática de datos de texto.
Implementa múltiples niveles de limpieza con seguimiento de transformaciones.
"""

from typing import Dict, List, Any
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize


class DataCleaner:
    """
    Clase especializada para limpieza avanzada y sistemática de datos de texto.
    Implementa múltiples niveles de limpieza con seguimiento de transformaciones.
    """

    def __init__(self, idioma: str = "english") -> None:
        self.idioma: str = idioma
        self.lemmatizador: WordNetLemmatizer = WordNetLemmatizer()
        self.stemmer: PorterStemmer = PorterStemmer()
        self.palabras_vacias: set[str] = set(stopwords.words(idioma))  # type: ignore
        self.historial_limpieza: Dict[str, Any] = {}

        # Patrones de expresiones regulares para limpieza
        self.patrones_limpieza: Dict[str, str] = {
            "urls": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "menciones": r"@\w+",
            "hashtags": r"#\w+",
            "numeros": r"\b\d+\b",
            "puntuacion_multiple": r"[^\w\s]{2,}",
            "espacios_multiples": r"\s{2,}",
            "caracteres_especiales": r"[^\w\s\-\'.,!?;:]",
        }

    def limpiar_nivel_basico(self, texto: str) -> str:
        """
        Nivel 1: Limpieza básica de formato y caracteres especiales.

        Args:
            texto (str): Texto original

        Returns:
            str: Texto con limpieza básica aplicada
        """
        # Convertir a minúsculas
        texto_limpio: str = texto.lower()

        # Eliminar URLs, emails, menciones
        for patron_nombre, patron in self.patrones_limpieza.items():
            if patron_nombre in ["urls", "emails", "menciones", "hashtags"]:
                texto_limpio = re.sub(patron, "", texto_limpio)

        # Normalizar espacios en blanco
        texto_limpio = re.sub(
            self.patrones_limpieza["espacios_multiples"], " ", texto_limpio
        )

        return texto_limpio.strip()

    def limpiar_nivel_intermedio(self, texto: str) -> str:
        """
        Nivel 2: Limpieza de puntuación y caracteres especiales.

        Args:
            texto (str): Texto con limpieza básica

        Returns:
            str: Texto con limpieza intermedia aplicada
        """
        texto_limpio: str = texto

        # Manejar contracciones comunes en inglés
        contracciones: Dict[str, str] = {
            "can't": "cannot",
            "won't": "will not",
            "n't": " not",
            "'re": " are",
            "'ve": " have",
            "'ll": " will",
            "'d": " would",
            "'m": " am",
            "it's": "it is",
            "that's": "that is",
            "what's": "what is",
        }

        for contraccion, expansion in contracciones.items():
            texto_limpio = texto_limpio.replace(contraccion, expansion)

        # Eliminar puntuación múltiple pero preservar puntos y comas importantes
        texto_limpio = re.sub(
            self.patrones_limpieza["puntuacion_multiple"], "", texto_limpio
        )

        # Eliminar caracteres especiales pero mantener apóstrofes y guiones
        texto_limpio = re.sub(
            self.patrones_limpieza["caracteres_especiales"], " ", texto_limpio
        )

        # Normalizar espacios nuevamente
        texto_limpio = re.sub(
            self.patrones_limpieza["espacios_multiples"], " ", texto_limpio
        )

        return texto_limpio.strip()

    def tokenizar_y_filtrar(self, texto: str) -> List[str]:
        """
        Nivel 3: Tokenización y filtrado avanzado.

        Args:
            texto (str): Texto limpio

        Returns:
            List[str]: Lista de tokens filtrados
        """
        # Tokenizar usando NLTK
        tokens: List[str] = word_tokenize(texto)

        # Filtros aplicados secuencialmente
        tokens_filtrados: List[str] = []

        for token in tokens:
            # Solo palabras alfabéticas de más de 2 caracteres
            if (
                token.isalpha()
                and len(token) > 2
                and token not in self.palabras_vacias
                and not token.isdigit()
            ):
                tokens_filtrados.append(token)

        return tokens_filtrados

    def aplicar_normalizacion_morfologica(
        self, tokens: List[str], metodo: str = "lemmatization"
    ) -> List[str]:
        """
        Nivel 4: Normalización morfológica (lemmatización o stemming).

        Args:
            tokens (List[str]): Lista de tokens filtrados
            metodo (str): 'lemmatization' o 'stemming'

        Returns:
            List[str]: Tokens normalizados morfológicamente
        """
        if metodo == "lemmatization":
            return [self.lemmatizador.lemmatize(token) for token in tokens]
        elif metodo == "stemming":
            return [self.stemmer.stem(token) for token in tokens] # type: ignore
        else:
            raise ValueError("Método debe ser 'lemmatization' o 'stemming'")

    def proceso_limpieza_completa(
        self,
        texto: str,
        incluir_normalizacion: bool = True,
        metodo_normalizacion: str = "lemmatization",
    ) -> Dict[str, Any]:
        """
        Ejecuta el proceso completo de limpieza con seguimiento de cada paso.

        Args:
            texto (str): Texto original
            incluir_normalizacion (bool): Si aplicar normalización morfológica
            metodo_normalizacion (str): Método de normalización a usar

        Returns:
            Dict[str, Any]: Resultados de cada nivel de limpieza con estadísticas
        """
        resultados: Dict[str, Any] = {}

        # Texto original
        resultados["original"] = {
            "texto": texto,
            "longitud": len(texto),
            "palabras": len(texto.split()),
        }

        # Nivel 1: Limpieza básica
        texto_basico: str = self.limpiar_nivel_basico(texto)
        resultados["limpieza_basica"] = {
            "texto": texto_basico,
            "longitud": len(texto_basico),
            "palabras": len(texto_basico.split()),
        }

        # Nivel 2: Limpieza intermedia
        texto_intermedio: str = self.limpiar_nivel_intermedio(texto_basico)
        resultados["limpieza_intermedia"] = {
            "texto": texto_intermedio,
            "longitud": len(texto_intermedio),
            "palabras": len(texto_intermedio.split()),
        }

        # Nivel 3: Tokenización y filtrado
        tokens_filtrados: List[str] = self.tokenizar_y_filtrar(texto_intermedio)
        resultados["tokenizacion_filtrado"] = {
            "tokens": tokens_filtrados,
            "cantidad_tokens": len(tokens_filtrados),
            "tokens_unicos": len(set(tokens_filtrados)),
        }

        # Nivel 4: Normalización morfológica (opcional)
        if incluir_normalizacion:
            tokens_normalizados: List[str] = self.aplicar_normalizacion_morfologica(
                tokens_filtrados, metodo_normalizacion
            )
            resultados["normalizacion_morfologica"] = {
                "tokens": tokens_normalizados,
                "cantidad_tokens": len(tokens_normalizados),
                "tokens_unicos": len(set(tokens_normalizados)),
                "metodo": metodo_normalizacion,
            }

        return resultados

    def mostrar_resumen_limpieza(self, resultados: Dict[str, Any]) -> None:
        """
        Muestra un resumen detallado de los resultados del proceso de limpieza.
        
        Args:
            resultados (Dict[str, Any]): Diccionario con los resultados del proceso_limpieza_completa
        """
        print("RESUMEN DEL PROCESO DE LIMPIEZA")
        print("=" * 50)
        
        # Texto original
        if "original" in resultados:
            original = resultados["original"]
            print("TEXTO ORIGINAL:")
            print(f"   • Longitud: {original['longitud']:,} caracteres")
            print(f"   • Palabras: {original['palabras']:,}")
            
        # Limpieza básica
        if "limpieza_basica" in resultados:
            basica = resultados["limpieza_basica"]
            print("\nLIMPIEZA BÁSICA:")
            print(f"   • Longitud: {basica['longitud']:,} caracteres")
            print(f"   • Palabras: {basica['palabras']:,}")
            if "original" in resultados:
                reduccion_chars = ((resultados["original"]["longitud"] - basica["longitud"]) / resultados["original"]["longitud"]) * 100
                reduccion_palabras = ((resultados["original"]["palabras"] - basica["palabras"]) / resultados["original"]["palabras"]) * 100
                print(f"   • Reducción: {reduccion_chars:.1f}% caracteres, {reduccion_palabras:.1f}% palabras")
        
        # Limpieza intermedia
        if "limpieza_intermedia" in resultados:
            intermedia = resultados["limpieza_intermedia"]
            print("\nLIMPIEZA INTERMEDIA:")
            print(f"   • Longitud: {intermedia['longitud']:,} caracteres")
            print(f"   • Palabras: {intermedia['palabras']:,}")
            if "limpieza_basica" in resultados:
                reduccion = ((resultados["limpieza_basica"]["palabras"] - intermedia["palabras"]) / resultados["limpieza_basica"]["palabras"]) * 100
                print(f"   • Reducción adicional: {reduccion:.1f}% palabras")
        
        # Tokenización y filtrado
        if "tokenizacion_filtrado" in resultados:
            tokens = resultados["tokenizacion_filtrado"]
            print("\nTOKENIZACIÓN Y FILTRADO:")
            print(f"   • Total tokens: {tokens['cantidad_tokens']:,}")
            print(f"   • Tokens únicos: {tokens['tokens_unicos']:,}")
            diversidad = (tokens['tokens_unicos'] / tokens['cantidad_tokens']) * 100 if tokens['cantidad_tokens'] > 0 else 0
            print(f"   • Diversidad léxica: {diversidad:.1f}%")
            
        # Normalización morfológica
        if "normalizacion_morfologica" in resultados:
            norm = resultados["normalizacion_morfologica"]
            print(f"\nNORMALIZACIÓN MORFOLÓGICA ({norm['metodo'].upper()}):")
            print(f"   • Total tokens: {norm['cantidad_tokens']:,}")
            print(f"   • Tokens únicos: {norm['tokens_unicos']:,}")
            diversidad_norm = (norm['tokens_unicos'] / norm['cantidad_tokens']) * 100 if norm['cantidad_tokens'] > 0 else 0
            print(f"   • Diversidad léxica: {diversidad_norm:.1f}%")
            
            if "tokenizacion_filtrado" in resultados:
                reduccion_total = ((tokens['tokens_unicos'] - norm['tokens_unicos']) / tokens['tokens_unicos']) * 100
                print(f"   • Reducción de vocabulario: {reduccion_total:.1f}%")
        
        print("\n" + "=" * 50)
        
        # Mostrar muestra del texto final
        if "normalizacion_morfologica" in resultados:
            tokens_finales = resultados["normalizacion_morfologica"]["tokens"]
            print("MUESTRA DEL TEXTO PROCESADO:")
            muestra = " ".join(tokens_finales[:20])  # Primeras 20 palabras
            print(f"   {muestra}{'...' if len(tokens_finales) > 20 else ''}")
        elif "tokenizacion_filtrado" in resultados:
            tokens_finales = resultados["tokenizacion_filtrado"]["tokens"]
            print("MUESTRA DEL TEXTO PROCESADO:")
            muestra = " ".join(tokens_finales[:20])  # Primeras 20 palabras
            print(f"   {muestra}{'...' if len(tokens_finales) > 20 else ''}")
        
        print("Resumen de limpieza completado\n")
