run:
	python backend/manage.py runserver

superuser:
	python backend/manage.py createsuperuser


migrate:
	python backend/manage.py migrate

migrations:
	python backend/manage.py makemigrations
