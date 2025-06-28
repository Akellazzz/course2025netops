.PHONY: lint init-dev

init:
	pip install poetry
	poetry install --without dev

init-dev: init
	poetry install --with dev

build: init
	poetry build

lint:
	poetry run black --check .
	poetry run ruff check .

mypy:
	mypy --strict .

check: lint mypy
	@echo "✅ Проверки пройдены"