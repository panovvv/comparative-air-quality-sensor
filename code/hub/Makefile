help:
	@echo "clean - remove Python artifacts, virtual environment and IDE project files"
	@echo "venv - install venv with all requirements for Airflow"
	@echo "cp - copy the project over to single board computer"
	@echo "rem-venv - update remote venv"
	@echo "run - run project on SBC"

all: help

default: help

clean: clean-venv clean-pyc

clean-venv:
	rm -rf venv/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

venv:
	@if [ ! -e "./venv/bin/activate" ] ; then \
		python3 -m venv ./venv ; \
		source ./venv/bin/activate && \
		pip install -r requirements.txt ; \
	else \
		echo "Virtual environment had already been created." ; \
	fi

cp:
	./sbc.sh cp

rem-venv: cp
	./sbc.sh venv

rem-clean:
	./sbc.sh clean

run:
	./sbc.sh run
