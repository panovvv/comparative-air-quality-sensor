invocation_params = --bus 1

help:
	@echo "Prerequisites:"
	@echo "  * Define username and IP for your single-board computer in environment"
	@echo "    variables SBC_NAME and SBC_IP."
	@echo "    Find a slightly automated solution in \"vars\" rule below:"
	@echo "    'make vars' scans the network and saves the found IP address +"
	@echo "    hardcoded username to ./sbc_vars.sh,"
	@echo "    which is then sourced in sbc.sh script."
	@echo "  * Copy your public key to SBC for passwordless login."
	@echo "  * Install Python 3.7 on your SBC. Adding it to \$PATH is not necessary."
	@echo "  * Customize invocation_params above as needed. Take a look at main.py to see how to invoke it."
	@echo "Basic commands you'll need:"
	@echo "  clean - remove local virtual environment and the whole remote project folder on SBC."
	@echo "  dev - install venv with all requirements on local PC. Useful for development."
	@echo "  format - reformat code + sort imports."
	@echo "  test - run flake8 to highlight code design problems and run tests"
	@echo "  run - run project remotely on SBC."

default: help

clean: local-clean rem-clean

local-clean:
	rm -rf venv/

rem-clean:
	./sbc.sh rm-clean

vars:
	echo -n "export SBC_IP=" > sbc_vars.sh
	echo `sudo nmap -sP -PS22 192.168.1.1/24 | grep raspberrypi | grep -oP "([0-9]{1,3}[\.]){3}[0-9]{1,3}"` >> sbc_vars.sh
	echo "export SBC_USER=pi" >> sbc_vars.sh

venv:
	@if [ ! -e "./venv/bin/activate" ] ; then \
		python3 -m venv ./venv ; \
		. ./venv/bin/activate && \
		pip install --upgrade pip && \
		pip install -r requirements.txt ; \
	else \
		echo "Virtual environment had already been created." ; \
	fi

dev: venv
	@if [ ! -e "./venv/bin/black" ] ; then \
		. ./venv/bin/activate && \
		pip install -r requirements_dev.txt ; \
	else \
		echo "Dev dependencies had already been installed." ; \
	fi

format: dev
	. ./venv/bin/activate && \
	black . && \
	isort -rc .

test: dev
	. ./venv/bin/activate && \
	tox

sync:
	./sbc.sh sync

rem-venv: sync
	./sbc.sh venv

run: sync rem-venv
	./sbc.sh run $(invocation_params)

shutdown:
	./sbc.sh shutdown
