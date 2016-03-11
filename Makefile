start: migrate
	python2.7 manage.py runserver

makemigration:
	python2.7 manage.py makemigrations

migrate: makemigration
	python2.7 manage.py migrate

activate:
	source env/bin/activate

django:
	source manage.py shell

wipe:
	python manage.py sqlflush
lint:
	yapf ./api --recursive -i
	yapf ./test --recursive -i
