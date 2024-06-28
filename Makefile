docker-createsuperuser:
	docker-compose exec zebrands_web python ./src/manage.py createsuperuser --settings=config.settings.local
docker-migrate:
	docker-compose exec zebrands_web python ./src/manage.py migrate --settings=config.settings.local
docker-migrations:
	docker-compose exec zebrands_web python ./src/manage.py makemigrations --settings=config.settings.local
docker-pytest:
	docker-compose run --rm zebrands_web pytest ./src/ ${PARAMS} -vv
docker-coverage:
	docker-compose run --rm zebrands_web pytest --cov-report term-missing --cov-config=.coveragerc --cov=./src/apps ./src/tests/
docker-run:
	docker-compose up
docker-build:
	docker-compose build
docker-down:
	docker-compose down
