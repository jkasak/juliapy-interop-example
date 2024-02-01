PYTHON ?=python3

.PHONY: clean dist run

venv: requirements.txt
	$(PYTHON) -m venv venv --clear
	./venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv build dist

dist: venv
	./venv/bin/python -m build
	
run: venv
	./venv/bin/python demo_script.py