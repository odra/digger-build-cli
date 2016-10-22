all: dependencies test build

clear:
	rm -rf dist build *egg-info 

dependencies:
	pip install -U -r requirements.txt

build:
	python setup.py build

install:
	python setup.py install

test:
	py.test -s

doc:
	(cd ./docs; make html;)

install-cordova:
	./scripts/install-cordova

download-android-sdk:
	./scripts/install-android-sdk

install-android-packages:
	./scripts/install-android-packages

install-sdks: install-android-packages install-cordova
