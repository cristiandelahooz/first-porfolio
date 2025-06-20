# Makefile para Proyecto de Análisis de Texto y NLP
# Autor: Cristian de la Hoz
# Descripción: Automatización de tareas para análisis de texto y procesamiento de lenguaje natural

# Variables de configuración
PYTHON := python3
PIP := pip3
VENV_NAME := venv
NOTEBOOK_PORT := 8888
PROJECT_NAME := first-portfolio
SRC_DIR := src
TEST_DIR := tests
NOTEBOOK_DIR := notebooks
DATA_DIR := data

# Colores para output
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[0;33m
BLUE := \033[0;34m
NC := \033[0m # No Color

# Targets por defecto
.PHONY: help setup install clean test lint format notebook run-analysis check-env download-data all

# Target por defecto - muestra ayuda
help:
	@echo "$(BLUE)🚀 Makefile para Proyecto de Análisis de Texto y NLP$(NC)"
	@echo "$(YELLOW)Comandos disponibles:$(NC)"
	@echo "  $(GREEN)setup$(NC)           - Configuración inicial completa del proyecto"
	@echo "  $(GREEN)install$(NC)         - Instala dependencias del proyecto"
	@echo "  $(GREEN)clean$(NC)           - Limpia archivos temporales y cache"
	@echo "  $(GREEN)test$(NC)            - Ejecuta todas las pruebas unitarias"
	@echo "  $(GREEN)lint$(NC)            - Verifica estilo de código con flake8"
	@echo "  $(GREEN)format$(NC)          - Formatea código con black"
	@echo "  $(GREEN)notebook$(NC)        - Inicia Jupyter Notebook"
	@echo "  $(GREEN)run-analysis$(NC)    - Ejecuta el análisis completo (notebook)"
	@echo "  $(GREEN)check-env$(NC)       - Verifica el entorno de desarrollo"
	@echo "  $(GREEN)download-data$(NC)   - Descarga datos NLTK necesarios"
	@echo "  $(GREEN)all$(NC)             - Ejecuta setup, test y verifica todo"
	@echo ""
	@echo "$(YELLOW)Ejemplos de uso:$(NC)"
	@echo "  make setup           # Configurar proyecto desde cero"
	@echo "  make test            # Ejecutar pruebas"
	@echo "  make notebook        # Iniciar Jupyter"
	@echo "  make run-analysis    # Ejecutar análisis completo"

# Configuración inicial completa del proyecto
setup: check-env install download-data
	@echo "$(GREEN)✅ Configuración inicial completada$(NC)"
	@echo "$(YELLOW)📋 Siguiente paso: make notebook o make run-analysis$(NC)"

# Instalar dependencias
install:
	@echo "$(BLUE)📦 Instalando dependencias...$(NC)"
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)✅ Dependencias instaladas$(NC)"

# Limpiar archivos temporales y cache
clean:
	@echo "$(BLUE)🧹 Limpiando archivos temporales...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	rm -rf .pytest_cache 2>/dev/null || true
	rm -rf .coverage 2>/dev/null || true
	rm -rf htmlcov 2>/dev/null || true
	@echo "$(GREEN)✅ Limpieza completada$(NC)"

# Ejecutar pruebas unitarias
test:
	@echo "$(BLUE)🧪 Ejecutando pruebas unitarias...$(NC)"
	@if [ -d "$(TEST_DIR)" ]; then \
		$(PYTHON) -m pytest $(TEST_DIR)/ -v --tb=short; \
	else \
		$(PYTHON) -m unittest discover -s $(TEST_DIR) -p "test_*.py" -v; \
	fi
	@echo "$(GREEN)✅ Pruebas completadas$(NC)"

# Verificar estilo de código
lint:
	@echo "$(BLUE)🔍 Verificando estilo de código...$(NC)"
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 $(SRC_DIR)/ $(TEST_DIR)/ --max-line-length=88 --extend-ignore=E203,W503; \
	else \
		echo "$(YELLOW)⚠️  flake8 no instalado. Instalando...$(NC)"; \
		$(PIP) install flake8; \
		flake8 $(SRC_DIR)/ $(TEST_DIR)/ --max-line-length=88 --extend-ignore=E203,W503; \
	fi
	@echo "$(GREEN)✅ Verificación de estilo completada$(NC)"

# Formatear código
format:
	@echo "$(BLUE)🎨 Formateando código...$(NC)"
	@if command -v black >/dev/null 2>&1; then \
		black $(SRC_DIR)/ $(TEST_DIR)/ --line-length=88; \
	else \
		echo "$(YELLOW)⚠️  black no instalado. Instalando...$(NC)"; \
		$(PIP) install black; \
		black $(SRC_DIR)/ $(TEST_DIR)/ --line-length=88; \
	fi
	@echo "$(GREEN)✅ Formateo completado$(NC)"

# Iniciar Jupyter Notebook
notebook:
	@echo "$(BLUE)📓 Iniciando Jupyter Notebook...$(NC)"
	@echo "$(YELLOW)💡 El notebook se abrirá en: http://localhost:$(NOTEBOOK_PORT)$(NC)"
	@echo "$(YELLOW)💡 Para detener: Ctrl+C$(NC)"
	jupyter notebook --port=$(NOTEBOOK_PORT) --no-browser --ip=127.0.0.1

# Ejecutar análisis completo usando nbconvert
run-analysis:
	@echo "$(BLUE)🔬 Ejecutando análisis completo...$(NC)"
	@if [ -f "$(NOTEBOOK_DIR)/analisis_limpio_tipado.ipynb" ]; then \
		echo "$(YELLOW)📊 Ejecutando notebook principal...$(NC)"; \
		jupyter nbconvert --to notebook --execute $(NOTEBOOK_DIR)/analisis_limpio_tipado.ipynb --output=analisis_ejecutado.ipynb; \
		echo "$(GREEN)✅ Análisis completado. Revisa: $(NOTEBOOK_DIR)/analisis_ejecutado.ipynb$(NC)"; \
	else \
		echo "$(RED)❌ No se encontró el notebook principal$(NC)"; \
		exit 1; \
	fi

# Verificar entorno de desarrollo
check-env:
	@echo "$(BLUE)🔧 Verificando entorno de desarrollo...$(NC)"
	@echo "$(YELLOW)Python version:$(NC)"
	@$(PYTHON) --version
	@echo "$(YELLOW)Pip version:$(NC)"
	@$(PIP) --version
	@echo "$(YELLOW)Estructura del proyecto:$(NC)"
	@if [ -d "$(SRC_DIR)" ]; then echo "✅ Directorio src/ encontrado"; else echo "❌ Directorio src/ no encontrado"; fi
	@if [ -d "$(TEST_DIR)" ]; then echo "✅ Directorio tests/ encontrado"; else echo "❌ Directorio tests/ no encontrado"; fi
	@if [ -d "$(NOTEBOOK_DIR)" ]; then echo "✅ Directorio notebooks/ encontrado"; else echo "❌ Directorio notebooks/ no encontrado"; fi
	@if [ -d "$(DATA_DIR)" ]; then echo "✅ Directorio data/ encontrado"; else echo "❌ Directorio data/ no encontrado"; fi
	@if [ -f "requirements.txt" ]; then echo "✅ requirements.txt encontrado"; else echo "❌ requirements.txt no encontrado"; fi
	@echo "$(GREEN)✅ Verificación de entorno completada$(NC)"

# Descargar datos NLTK necesarios
download-data:
	@echo "$(BLUE)📥 Descargando datos NLTK necesarios...$(NC)"
	$(PYTHON) -c "import nltk; nltk.download('webtext', quiet=True); nltk.download('stopwords', quiet=True); nltk.download('punkt', quiet=True); nltk.download('wordnet', quiet=True); nltk.download('averaged_perceptron_tagger', quiet=True); nltk.download('vader_lexicon', quiet=True); print('✅ Datos NLTK descargados')"
	@echo "$(GREEN)✅ Descarga de datos completada$(NC)"

# Crear directorios necesarios
create-dirs:
	@echo "$(BLUE)📁 Creando directorios necesarios...$(NC)"
	@mkdir -p $(DATA_DIR)/raw $(DATA_DIR)/processed
	@echo "$(GREEN)✅ Directorios creados$(NC)"

# Ejecutar análisis modular (usando scripts de Python)
run-modular:
	@echo "$(BLUE)🔬 Ejecutando análisis modular...$(NC)"
	@echo "$(YELLOW)1. Probando ingesta de datos...$(NC)"
	$(PYTHON) -c "from $(SRC_DIR).data_ingestion import GestorDatosTexto; g = GestorDatosTexto(); print('✅ Módulo de ingesta OK')"
	@echo "$(YELLOW)2. Probando limpieza de datos...$(NC)"
	$(PYTHON) -c "from $(SRC_DIR).data_cleaning import LimpiadorAvanzadoTexto; l = LimpiadorAvanzadoTexto(); print('✅ Módulo de limpieza OK')"
	@echo "$(GREEN)✅ Análisis modular completado$(NC)"

# Generar reporte de cobertura de pruebas
coverage:
	@echo "$(BLUE)📊 Generando reporte de cobertura...$(NC)"
	@if command -v coverage >/dev/null 2>&1; then \
		coverage run -m pytest $(TEST_DIR)/; \
		coverage report -m; \
		coverage html; \
		echo "$(GREEN)✅ Reporte generado en htmlcov/index.html$(NC)"; \
	else \
		echo "$(YELLOW)⚠️  coverage no instalado. Instalando...$(NC)"; \
		$(PIP) install coverage pytest; \
		coverage run -m pytest $(TEST_DIR)/; \
		coverage report -m; \
		coverage html; \
		echo "$(GREEN)✅ Reporte generado en htmlcov/index.html$(NC)"; \
	fi

# Ejecutar todo: setup, test, lint
all: setup test lint
	@echo "$(GREEN)🎉 Todos los procesos completados exitosamente$(NC)"
	@echo "$(YELLOW)📋 Proyecto listo para usar:$(NC)"
	@echo "  - make notebook     # Para análisis interactivo"
	@echo "  - make run-analysis # Para ejecutar análisis completo"

# Target para desarrollo: watch de archivos y ejecución automática de tests
dev-watch:
	@echo "$(BLUE)👁️  Modo desarrollo: observando cambios...$(NC)"
	@echo "$(YELLOW)💡 Los tests se ejecutarán automáticamente al detectar cambios$(NC)"
	@echo "$(YELLOW)💡 Para detener: Ctrl+C$(NC)"
	@if command -v fswatch >/dev/null 2>&1; then \
		fswatch -o $(SRC_DIR)/ $(TEST_DIR)/ | xargs -n1 -I{} make test; \
	else \
		echo "$(RED)❌ fswatch no instalado. Instala con: brew install fswatch$(NC)"; \
	fi

# Instalar dependencias de desarrollo
install-dev:
	@echo "$(BLUE)🛠️  Instalando dependencias de desarrollo...$(NC)"
	$(PIP) install black flake8 pytest coverage jupyter nbconvert
	@echo "$(GREEN)✅ Dependencias de desarrollo instaladas$(NC)"

# Mostrar estadísticas del proyecto
stats:
	@echo "$(BLUE)📈 Estadísticas del proyecto:$(NC)"
	@echo "$(YELLOW)Líneas de código:$(NC)"
	@find $(SRC_DIR)/ -name "*.py" -exec wc -l {} + | tail -1
	@echo "$(YELLOW)Archivos de prueba:$(NC)"
	@find $(TEST_DIR)/ -name "*.py" | wc -l
	@echo "$(YELLOW)Notebooks:$(NC)"
	@find $(NOTEBOOK_DIR)/ -name "*.ipynb" | wc -l
	@echo "$(YELLOW)Tamaño del proyecto:$(NC)"
	@du -sh . 2>/dev/null || echo "No disponible"
