.PHONY: lint mypy tests check

lint:
	poetry run black .

mypy:
	poetry run mypy src
	poetry run mypy tests

# tests:
# 	poetry run pytest

check: lint mypy tests
	@echo "✅ Проверки пройдены"