# mythril_webapi
Web API for [Mythril](https://github.com/ConsenSys/mythril/) - a Smart Contract Security Analysis Tool.

## Prerequisites
1. Python 3.6
1. Mythril
1. Django
1. Django Rest Framework
1. Celery
1. RabbitMQ

## File structure
1. *mythril_webapi*: Django project
1. *analysis*: Django REST Framework app

## Deployment on Heroku

```bash
git clone https://github.com/ynouri/mythril_webapi.git
heroku login
heroku create
git push heroku master
heroku logs --tail
# Following collectstatic line is apparently run automatically by Heroku during the push
#heroku run python manage.py collectstatic
heroku run python manage.py migrate
heroku addons:create rabbitmq-bigwig:pipkin
heroku open

```

## Local Deployment on OS X

### Pip installs
```bash
pip install mythril
pip install Django
pin install djangorestframework
pip install celery
```

### Django + Django REST framework
```bash
```


### RabbitMQ (Celery broker)
```bash
brew install rabbitmq
sudo mkdir /usr/local/sbin
sudo chown -R `whoami`:admin /usr/local/sbin
export PATH="/usr/local/sbin:$PATH" # or add this line in ./bash_profile and restart a shell
rabbitmq-server # Runs the rabbitmq server.
rabbitmqctl status # To check that the server is running
```

### Celery
```bash
# Runs a single worker. To run in root folder (mythril_webapi), not project folder (mythril_webap/myhtril_webapi)
celery worker -A mythril_webapi.celery_app --loglevel=info --concurrency=1
```

## Production Build and Installation
How to build the application for upload to a server
```bash
Note: assume it is a dedicated server not AWS or Heroku.
```

## Running Tests
The following shell script will run:
1. Unit tests on Django Rest serializers
1. Unit tests on the Celery task
1. Curl command line tests on the running Web API
```bash
./all_tests.sh
```

## Notes


## To do :)
1. Expand and enhance existing unit tests:
11. Django model
11. Django serializers
11. Django views
11. Celery task
11. Django REST API
1. Heroku packaging
1. Cover remaining requirements: handle multiple contract bytecodes POST
1. Mythril seems to display no found security issues for contracts that apparently do have some --> need to investigate
1. Integrate advanced Mythril settings such as the depth
1. Handle all limit cases, error messages
1. Review and enhance exception handling
1. Refine the status and report deserializers so that json response only display the relevant fields.
1. Review security around default settings and login/passwords: Django, Celery, RabbitMQ, SQLite
1. Review production settings vs test
1. Adapt the Celery workers number settings to the deployment environment target (Heroku dynos?)
1. Enhance the diplay of issues returned by myth - return them in a dictionnary
1. Review the integration of Celery data model within Django's. Better model would be to have an Analysis model which would have a one-to-one (or one-to-many) relationship with CeleryTask model
