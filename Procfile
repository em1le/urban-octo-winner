release: python manage.py migrate
release: python manage.py collecstatic --no-input
web: gunicorn core.wsgi:application
