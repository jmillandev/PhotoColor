dev:
	@if [ -z "$(command)" ]; then \
		echo "No <command> specified. Defaulting to bash."; \
		echo "To specify a <command?, run 'make dev command=<command>'"; \
		command="bash"; \
	fi;
	echo "Running command: $(command)"
	./init.sh run --rm photo_api $(command)

up:
	make migrate
	uvicorn apps.server:app --reload --workers 1 --host 0.0.0.0 --port 8080	

migrate:
	./migrate.py

test:
	make lint
	pytest -v

generate/migration:
	alembic revision -m "$(message)"

format:
	black .
	isort .

lint:
	flake8 .
	black --check .
	isort --check-only .
	mypy .
