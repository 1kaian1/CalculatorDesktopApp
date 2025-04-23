# This file is part of Calculator_app.
#
# Calculator_app is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Calculator_app is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (c) 2025 Jan Kai Marek, xmarekj00
# Copyright (c) 2025 Jan Frantisek Levicek, xlevic02

# Definujte proměnné
PYTHON=python3
PIP=pip3
PACKAGE_NAME=but-fit-ivs25
PACKAGE_VERSION=1.0
BUILD_DIR=../build

# all (přeloží projekt – včetně programu pro profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
all:
	echo Hello World!

# pack (zabalí projekt tak, aby mohl být odevzdán)
pack:
	mkdir -p ../build  # Vytvoří složku pro balíček

	cp -r ../src ../build  # Zkopíruje hlavní složku projektu

	# Přejdeme do build adresáře a vytvoříme balíček
	cd ../build && dpkg-buildpackage -us -uc


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
	rm -rf $(BUILD_DIR)