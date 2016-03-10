start: sync
	python2.7 manage.py runserver

migrate:
	python2.7 manage.py makemigrations

sync: migrate
	python2.7 manage.py syncdb

activate:
	source env/bin/activate
