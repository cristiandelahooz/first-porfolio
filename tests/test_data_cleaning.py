"""
Pruebas unitarias para el módulo de limpieza de datos.
"""

import unittest
from typing import List
from src.data_cleaning import LimpiadorAvanzadoTexto


class TestLimpiadorAvanzadoTexto(unittest.TestCase):
    """
    Clase de pruebas para el limpiador avanzado de texto.
    """

    def setUp(self) -> None:
        """Configuración inicial para las pruebas."""
        self.limpiador = LimpiadorAvanzadoTexto()
        self.texto_prueba = "Hello! This is a TEST text with URLs http://example.com and emails test@example.com"

    def test_limpiar_nivel_basico(self) -> None:
        """Prueba la limpieza básica de texto."""
        resultado = self.limpiador.limpiar_nivel_basico(self.texto_prueba)
        self.assertIsInstance(resultado, str)
        self.assertNotIn("http://", resultado)
        self.assertNotIn("@", resultado)

    def test_tokenizar_y_filtrar(self) -> None:
        """Prueba la tokenización y filtrado."""
        texto_limpio = "this is a test text with some words"
        tokens = self.limpiador.tokenizar_y_filtrar(texto_limpio)
        self.assertIsInstance(tokens, list)
        self.assertTrue(all(isinstance(token, str) for token in tokens))
        self.assertTrue(all(len(token) > 2 for token in tokens))

    def test_proceso_completo(self) -> None:
        """Prueba el proceso completo de limpieza."""
        resultado = self.limpiador.proceso_limpieza_completa(self.texto_prueba)
        self.assertIn("original", resultado)
        self.assertIn("limpieza_basica", resultado)
        self.assertIn("tokenizacion_filtrado", resultado)


if __name__ == "__main__":
    unittest.main()
