SHELL := /bin/bash

bootstrap:
	pip install virtualenv
	pip install --upgrade virtualenv
	virtualenv env
	source env/bin/activate
	pip install -r requirement.txt

dev-up:
	docker-compose -f dev.yaml up -d

dev-down:
	docker-compose -f dev.yaml down