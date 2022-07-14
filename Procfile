web: gunicorn dm_backend.wsgi
release: python manage.py migrate && python manage.py loaddata api/fixtures/*.json
