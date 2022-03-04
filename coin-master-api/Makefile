.SILENT: clean

.PHONY: start
start:
	LOG_LEVEL=DEBUG poetry run uvicorn --no-access-log --log-level critical --reload --factory coin_master.api:create_app --host 0.0.0.0 --port 8000

.PHONY: start-json
start-json:
	JSON_LOGGING=1 poetry run uvicorn --no-access-log --log-level critical --reload --factory coin_master.api:create_app --host 0.0.0.0 --port 8000

.PHONY: deps
deps:
	poetry install

.PHONY: deps-update
deps-update:
	poetry update

.PHONY: deps-no-dev
deps-no-dev:
	poetry install --no-dev

.PHONY: docker-build
docker-build:
	docker build -t coin-master-api:latest .

.PHONY: docker-run
docker-run:
	docker run -it --rm --env-file .env -p 8000:8000 coin-master-api:latest

.PHONY: docker-debug
docker-debug:
	docker run -it --rm --env-file .env -p 8000:8000 --entrypoint /bin/bash coin-master-api:latest

.PHONY: docker
docker: docker-build docker-run

.PHONY: clean
clean:
	rm -rf build/ dist/ *.egg-info/ .eggs/ .pytest_cache/ .mypy_cache .coverage *.spec test-result.html htmlcov/
	find . -type d -name __pycache__ -exec rm -rf '{}' +
