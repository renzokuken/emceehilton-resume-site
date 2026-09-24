.PHONY: dev build preview clean help

VENV ?= .venv
PYTHON ?= $(VENV)/bin/python

help:
	@echo "Available commands:"
	@echo "  make dev      - Start local Flask development server with auto-reloading"
	@echo "  make build    - Freeze website to static files inside build/"
	@echo "  make preview  - Freeze and serve static files locally at http://localhost:8000"
	@echo "  make clean    - Remove build artifacts and temporary files"

dev:
	$(PYTHON) app.py

build:
	$(PYTHON) freeze.py

preview:
	$(PYTHON) freeze.py --serve

clean:
	rm -rf build __pycache__ content/*/__pycache__
