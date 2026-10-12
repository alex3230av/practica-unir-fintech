.PHONY: all $(MAKECMDGOALS)

FILE ?= palabras.txt
DUP ?= yes
ORDER ?= asc

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py $(FILE) $(DUP) $(ORDER)

run-local:
	python3 main.py $(FILE) $(DUP) $(ORDER)