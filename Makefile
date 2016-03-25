.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

start: migrate ## Starts The App
	python2.7 manage.py runserver

makemigration:
	python2.7 manage.py makemigrations

migrate: makemigration ## Makes Migrations and Executes them
	python2.7 manage.py migrate

django: ## Starts a Django Env for testing code
	source manage.py shell

wipe:  ## Wipe the database clean
	python manage.py sqlflush

lint: ## Cleans the Code
	yapf ./api --recursive -i

tests:  ## Runs Tests
	coverage run manage.py test
