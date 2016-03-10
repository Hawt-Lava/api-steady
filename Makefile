start: sync
	python2.7 manage.py runserver

migration:
	python2.7 manage.py makemigrations

sync: migration
	python2.7 manage.py syncdb
