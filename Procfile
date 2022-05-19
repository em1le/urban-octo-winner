release: python manage.py migrate
web: python manage.py collectstatic --no-input; gunicorn myapp.wsgi --log-file - --log-level debug

