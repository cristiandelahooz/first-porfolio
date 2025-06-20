"""
Módulo para gestión e ingesta de datos de texto.
Contiene clases y funciones para cargar y manipular corpus de texto.
"""

from typing import Dict, List, Optional
import pandas as pd
from nltk.corpus import webtext


class GestorDatosTexto:
    """
    Clase para gestionar la carga, exploración y manipulación de datos de texto.
    """
    
    def __init__(self) -> None:
        self.corpus_webtext = webtext
        self.archivo_seleccionado: Optional[str] = None
        self.texto_crudo: Optional[str] = None
        self.dataframe_texto: Optional[pd.DataFrame] = None
    
    def explorar_archivos_disponibles(self) -> List[str]:
        """
        Obtiene la lista de archivos disponibles en el corpus webtext.
        
        Returns:
            List[str]: Lista de nombres de archivos
        """
        archivos: List[str] = self.corpus_webtext.fileids()
        print("Archivos disponibles en el corpus webtext:")
        print("=" * 45)
        
        for i, archivo in enumerate(archivos, 1):
            tamaño_palabras: int = len(self.corpus_webtext.words(archivo))
            print(f"{i}. {archivo} ({tamaño_palabras:,} palabras)")
        
        return archivos
    
    def seleccionar_archivo(self, nombre_archivo: str) -> bool:
        """
        Selecciona un archivo específico del corpus para análisis.
        
        Args:
            nombre_archivo (str): Nombre del archivo a seleccionar
            
        Returns:
            bool: True si la selección fue exitosa
        """
        try:
            if nombre_archivo in self.corpus_webtext.fileids():
                self.archivo_seleccionado = nombre_archivo
                self.texto_crudo = self.corpus_webtext.raw(nombre_archivo)
                print(f"Archivo '{nombre_archivo}' seleccionado exitosamente")
                return True
            else:
                print(f"Archivo '{nombre_archivo}' no encontrado")
                return False
        except Exception as e:
            print(f"Error al seleccionar archivo: {e}")
            return False
    
    def crear_dataframe_texto(self) -> Optional[pd.DataFrame]:
        """
        Convierte el texto crudo en un DataFrame de pandas para análisis.
        
        Returns:
            Optional[pd.DataFrame]: DataFrame con el texto dividido en líneas
        """
        if self.texto_crudo is None:
            print("Primero debe seleccionar un archivo")
            return None
        
        lineas: List[str] = self.texto_crudo.split('\n')
        # Filtrar líneas vacías y muy cortas
        lineas_filtradas: List[str] = [
            linea.strip() for linea in lineas 
            if linea.strip() and len(linea.strip()) > 3
        ]
        
        self.dataframe_texto = pd.DataFrame({
            'texto': lineas_filtradas,
            'longitud': [len(linea) for linea in lineas_filtradas],
            'num_palabras': [len(linea.split()) for linea in lineas_filtradas]
        })
        
        return self.dataframe_texto
