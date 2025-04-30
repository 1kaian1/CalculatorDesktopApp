# Makefile for Calculator_app
#
# This Makefile provides a set of shortcuts for developing, testing, documenting, and running
# the Calculator_app project. It simplifies common operations using Python's venv and tools.
#
# Targets:
#
# help               Show all available targets and their descriptions.
# all                Set up the full environment
# venv               Create a new virtual environment in the .venv directory.
# install            Install required Python packages into the virtual environment.
# run                Run the GUI application.
# test               Run unit tests using unittest.
# clean              Remove all Python cache files and compiled bytecode.
# doc              Generate HTML documentation using pydoc for project modules.
# open-doc           Open the generated documentation file in the default browser.
# remove-doc         Remove generated documentation files.

# Show help for available commands
help:
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Default setup
all: venv install stddev ## Set up the full environment (venv, install, stddev)

# Create a new virtual environment
venv: ## Create a new virtual environment in .venv/
	python3 -m venv .venv

# Install dependencies
install: ## Install Python dependencies from requirements.txt
	.venv/bin/pip install -r requirements.txt

# Run the application
run: ## Launch the calculator GUI
	.venv/bin/python3 main.py

# Run tests
test: ## Execute unit tests using unittest
	.venv/bin/python3 -m unittest discover

# Clean up compiled files
clean: ## Delete __pycache__ folders and .pyc files
	find . -type d -name "__pycache__" -exec rm -r {} +; find . -name "*.pyc" -delete

# Generate documentation
doc: ## Generate HTML documentation using pydoc
	.venv/bin/python -m pydoc -w mathLib
	.venv/bin/python -m pydoc -w gui
	.venv/bin/python -m pydoc -w mathLibTests
	.venv/bin/python -m pydoc -w stddev

# Open documentation in browser
open-doc: ## Open the mathLib.html documentation file in default browser
	xdg-open mathLib.html || open mathLib.html

# Remove generated documentation
remove-doc: ## Delete generated .html documentation files
	rm -f *.html

# Make stddev.py executable as ./stddev
stddev: ## Make stddev.py executable and create symlink ./stddev
	chmod +x stddev.py
	ln -sf stddev.py stddev