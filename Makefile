.PHONY: test coverage init lint

init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

test:
	pipenv run py.test tests

lint:
	pipenv run pylint monzopy

coverage:
	pipenv run py.test --verbose --cov-report term --cov-report xml --cov=monzopy tests