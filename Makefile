.PHONY: install test

default: test

install:
		python3 -m pip install pipenv
		python3 -m pipenv install --dev

test:
		python -m pipenv run pytest -v
