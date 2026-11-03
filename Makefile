run:
	uvicorn quotelab.main:app --reload

# Garante que o make use o pytest do ambiente virtual
VENV = .venv
PYTHON = $(VENV)/bin/python
PYTEST = $(VENV)/bin/bin/pytest # ou apenas $(VENV)/bin/pytest

test:
	$(VENV)/bin/pytest
