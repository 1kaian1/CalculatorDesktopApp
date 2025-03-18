# Definujte proměnné
PYTHON=python3
PIP=pip3
VENV_DIR=venv

# Instalace závislostí
install:
	$(PIP) install -r requirements.txt

# Vytvoření virtuálního prostředí
venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/activate

# Spuštění aplikace
run:
	$(PYTHON) main.py

# Spuštění testů
test:
	$(PYTHON) -m unittest discover

# Spuštění linters pro kontrolu kódu
lint:
	flake8

# Vyčištění souborů
clean:
	rm -rf __pycache__
	rm -rf $(VENV_DIR)
