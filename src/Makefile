# Definujte proměnné
PYTHON=python3
PIP=pip3
VENV_DIR=venv

# all (přeloží projekt – včetně programu pro profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
all:
	echo Hello World!

# pack (zabalí projekt tak, aby mohl být odevzdán)
pack:

# doc (spustí generování dokumentace)
doc:

# Vytvoření virtuálního prostředí
venv:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/activate

# run (spustí program)
run:
	$(PYTHON) main.py

# test (spustí testy matematické knihovny)
test:
	$(PYTHON) -m unittest mathLibTests

# Spuštění linters pro kontrolu kódu
lint:
	flake8

# stddev (spustí překlad programu pro výpočet směrodatné odchylky na profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
stddev:

# clean (smaže všechny soubory, co nemají být odevzdány)
clean:
	rm -rf __pycache__
	rm -rf $(VENV_DIR)
