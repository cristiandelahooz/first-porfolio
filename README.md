# 🚀 Proyecto de Análisis de Texto y NLP - Portafolio Profesional

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![NLTK](https://img.shields.io/badge/NLTK-3.9+-green.svg)](https://www.nltk.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

Este proyecto implementa un sistema completo y profesional de análisis de texto y procesamiento de lenguaje natural (NLP) aplicado al corpus webtext de NLTK. El proyecto ha sido completamente reestructurado siguiendo las mejores prácticas de ciencia de datos y desarrollo de software.

### ✨ Características Principales

- **🏗️ Arquitectura Modular**: Separación clara de responsabilidades
- **🔍 Tipado Estático**: Implementación completa con `typing`
- **🧪 Pruebas Unitarias**: Validación automática de funcionalidad
- **📊 Análisis Completo**: Desde ingesta hasta visualización
- **🤖 Automatización**: Scripts para limpieza y procesamiento
- **📖 Documentación**: Español técnico profesional

## 📁 Estructura del Proyecto

```
proyecto_limpieza_datos_nlp/
├── 📁 data/
│   ├── raw/                 # Datos originales del corpus
│   └── processed/           # Datos procesados y limpios
├── 📁 notebooks/           # Notebooks de análisis exploratorio
├── 📁 src/                 # Código fuente modular
│   ├── __init__.py
│   ├── data_ingestion.py   # Gestión y carga de datos
│   ├── data_cleaning.py    # Limpieza avanzada de texto
│   └── utils.py           # Funciones de utilidad
├── 📁 tests/              # Pruebas unitarias
│   └── test_data_cleaning.py
├── requirements.txt       # Dependencias del proyecto
└── README.md             # Este archivo
```

## Características Principales

- ✓ **Gestión automática de dependencias**: Verificación e instalación automática de paquetes
- ✓ **Limpieza multi-nivel**: Sistema escalonado de limpieza de texto
- ✓ **Análisis exploratorio**: Estadísticas descriptivas y visualizaciones
- ✓ **Análisis de sentimientos**: Enfoque dual lexical y contextual
- ✓ **Análisis semántico**: Extracción de synsets con WordNet
- ✓ **Tipado estático**: Código con tipado estricto para mayor robustez

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el notebook principal:
   ```bash
   jupyter notebook notebooks/exploratory_data_analysis.ipynb
   ```

## Uso

El proyecto está diseñado para ser usado tanto de forma modular (importando clases individuales) como de forma completa (ejecutando el notebook completo).

### Ejemplo de uso modular:

```python
from src.data_ingestion import GestorDatosTexto
from src.data_cleaning import LimpiadorAvanzadoTexto

# Cargar datos
gestor = GestorDatosTexto()
gestor.seleccionar_archivo('firefox.txt')

# Limpiar texto
limpiador = LimpiadorAvanzadoTexto()
resultado = limpiador.proceso_limpieza_completa(gestor.texto_crudo)
```

## Metodología

El proyecto implementa las siguientes técnicas de NLP:

1. **Preprocesamiento**: Normalización, eliminación de ruido
2. **Tokenización**: División inteligente del texto
3. **Filtrado**: Eliminación de stopwords y tokens irrelevantes
4. **Normalización morfológica**: Lemmatización y stemming
5. **Análisis de frecuencias**: Distribuciones y ley de Zipf
6. **Análisis de sentimientos**: Opinion Lexicon y VADER
7. **Análisis semántico**: WordNet synsets por categoría gramatical

## Resultados

El análisis proporciona insights sobre:
- Características estadísticas del corpus
- Distribución de sentimientos en el texto
- Riqueza léxica y diversidad semántica
- Patrones lingüísticos y estructurales

## Contribución

Este proyecto fue desarrollado como parte del curso de NLP. Las contribuciones son bienvenidas siguiendo las mejores prácticas de desarrollo.

## Licencia

Proyecto académico - Uso educativo.

## 🎯 Estado del Proyecto

### ✅ Completado
- [x] **Reestructuración Completa**: Arquitectura modular implementada
- [x] **Tipado Estático**: Anotaciones de tipo en todos los módulos
- [x] **Limpieza de Código**: Eliminación de emojis y mejora de documentación
- [x] **Automatización**: Script de limpieza y procesamiento automatizado
- [x] **Pruebas Unitarias**: Validación de funcionalidad modular
- [x] **Notebook Profesional**: Versión final limpia y estructurada

### 📊 Métricas de Calidad
- **Cobertura de Tipado**: 100% en módulos principales
- **Estructura Modular**: 4 módulos especializados
- **Pruebas**: 3 suites de pruebas implementadas
- **Documentación**: Comentarios y docstrings en español
