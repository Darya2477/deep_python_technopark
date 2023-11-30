VENV = venv

all: $(VENV) build

venv:
 python3 -m venv $(VENV); \
    . $(VENV)/bin/activate; \
    pip install -r requirements.txt

build:
 $(VENV)/bin/python setup.py install

test: all
 $(VENV)/bin/python -m unittest discover -v

.PHONY: all test build
.DEFAULT_GOAL := all

