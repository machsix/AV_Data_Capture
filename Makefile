#.PHONY: help prepare-dev test lint run doc

#VENV_NAME?=venv
#VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
#PYTHON=${VENV_NAME}/bin/python3
SHELL = /bin/bash

.DEFAULT: make
make:
	#@echo "[+]make prepare-dev"
	#sudo apt-get -y install python3.7 python3-pip
	#pip3 install -r requirements.txt
	#pip3 install pyinstaller

	#@echo "[+]Set CLOUDSCRAPER_PATH variable"
	#export cloudscraper_path=$(python3 -c 'import cloudscraper as _; print(_.__path__[0])' | tail -n 1)

	@echo "[+]Pyinstaller make for x64"
	mkdir -p dist/amd64
	pyinstaller --onefile AV_Data_Capture.spec  --hidden-import ADC_function.py --hidden-import core.py --distpath "./dist/amd64"

	@echo "[+]Clean cache"
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -type d | xargs rm -fr
	@find . -name '.pytest_cache' -type d | xargs rm -fr
	rm -rf build/
