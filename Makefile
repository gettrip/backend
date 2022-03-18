-include .env
export

db.run:
	@docker-compose up -d db

stop:
	@docker-compose stop -t 1

clean:
	@docker-compose down

lint:
	@mypy backend
	@flake8 backend

dev.install:
	@poetry install

db.create:
	@python -m backend.models

run:
	@python -m backend
