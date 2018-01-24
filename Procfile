web: gunicorn mythril_webapi.wsgi --log-file -
main_worker: celery worker -A mythril_webapi.celery_app --loglevel=info --concurrency=1 # Runs with a single worker
