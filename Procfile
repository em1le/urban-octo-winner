release: python manage.py migrate
release: python manage.py collecstatic
web: gunicorn core.wsgi:application
