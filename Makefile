-include .env
export

db.run:
	docker-compose up -d db

stop:
	docker-compose stop -t 1

lint:
	@mypy backend
	@flake8 backend
