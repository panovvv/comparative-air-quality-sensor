invocation_params = -b 1

help:
	@echo "Prerequisites:"
	@echo "  * Open ./sbc.sh and define user and IP for your single-board computer."
	@echo "  * Copy your public key to SBC for passwordless login."
	@echo "  * Install Python 3.7 on your SBC. Adding it to \$PATH is not necessary."
	@echo "  * Customize invocation_params above as needed. Take a look at main.py to see how to invoke it."
	@echo "Basic commands you'll need:"
	@echo "  clean - remove local virtual environment and the whole remote project folder on SBC."
	@echo "  dev - install venv with all requirements on local PC. Useful for development."
	@echo "  format - reformat code + sort imports."
	@echo "  lint - run flake8 to highlight code design problems."
	@echo "  run - run project remotely on SBC."

default: help

clean: local-clean rem-clean

local-clean:
	rm -rf venv/

rem-clean:
	./sbc.sh rm-clean

venv:
	@if [ ! -e "./venv/bin/activate" ] ; then \
		python3 -m venv ./venv ; \
		. ./venv/bin/activate && \
		pip3 install --upgrade pip && \
		pip3 install -r requirements.txt ; \
	else \
		echo "Virtual environment had already been created." ; \
	fi

dev: venv
	@if [ ! -e "./venv/bin/black" ] ; then \
		. ./venv/bin/activate && \
		pip3 install -r requirements_dev.txt ; \
	else \
		echo "Dev dependencies had already been installed." ; \
	fi


format: dev
	. ./venv/bin/activate && \
	black communications/ gui/ sensors/ main.py && \
	isort -rc communications/ gui/ sensors/ main.py

lint: dev
	. ./venv/bin/activate && \
	flake8

sync:
	./sbc.sh sync

rem-venv: sync
	./sbc.sh venv

run: sync rem-venv
	./sbc.sh run $(invocation_params)
