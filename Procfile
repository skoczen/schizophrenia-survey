web: manage.py collectstatic --noinput --settings=envs.live;python manage.py run_gunicorn -b "0.0.0.0:$PORT" --workers=4 --settings=envs.live

