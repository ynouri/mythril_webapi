# mythril_webapi
Web API for [Mythril](https://github.com/ConsenSys/mythril/) - a Smart Contract Security Analysis Tool.

## Pre-requisites
1. Python 3.6
1. Mythril
1. Django
1. Django Rest Framework
1. Celery
1. RabbitMQ

Detailed dependencies and versions are available in the requirements.txt file.

## File structure
1. *mythril_webapi*: Django project
1. *analysis*: Django REST Framework app

## Deployment on Heroku

*Important note:* I had very little time to test the Heroku deployment, and it's very likely to not be working in its current state. If possible, please see next part focusing on MacOS deployment.

```bash
# Clone the git repo
git clone https://github.com/ynouri/mythril_webapi.git

# Login to Heroku, create app and push repo
heroku login
heroku create
git push heroku master
heroku logs --tail

# Following line is apparently run automatically by Heroku during the push. Not needed
#heroku run python manage.py collectstatic

# Migrate the model, only first push
heroku run python manage.py migrate

# Start the CloudAMPQ service
heroku addons:create cloudamqp

# Start the Celery worker within a one-off dyno
heroku run celery worker -A mythril_webapi.celery_app --loglevel=info --concurrency=1

# Open the app
heroku open

```

## Local Deployment on MacOS


### Terminal 1 - web app
```bash
# Clone the git repo
git clone https://github.com/ynouri/mythril_webapi.git deploy_test

# Deploy a virtual environment and install the dependencies
virtualenv deploy_env
source deploy_env/bin/activate
pip install -r requirements.txt

# Deploy static assets
python manage.py collectstatic --no-input

# Migrate the models
python manage.py migrate

# Run Django server
python manage.py runserver

```

### Terminal 2 - RabbitMQ
```bash
# Make sure to have the correct rights on /usr/local/sbin, and add it to $PATH
sudo chown -R `whoami`:admin /usr/local/sbin
export PATH="/usr/local/sbin:$PATH" # or add this line in ./bash_profile and restart a shell

# Install RabbitMQ
brew install rabbitmq

# Run RabbitMQ server
rabbitmq-server

# Check if it is running correctly
rabbitmqctl status
```

### Terminal 3 - Celery
```bash
# Go to deploy folder and switch to deploy environment
cd deploy_test
source deploy_env/bin/activate

# Run Celery worker
celery worker -A mythril_webapi.celery_app --loglevel=info --concurrency=1
```

### Terminal 4 - Run tests
```bash
# Go to deploy folder and switch to deploy environment
cd deploy_test
source deploy_env/bin/activate

# Run the tests
./all_tests.sh
```

### Web browser
Open http://127.0.0.1:8000/mythril/v1/analysis/. Django REST framework provides a browsable API which can be used to play with the API.

## Tests
```bash
./all_tests.sh
```
This script will run:
1. Unit tests on Django Rest serializers
1. Unit tests on the Celery task
1. Unit tests on the Web API
1. Curl command line tests on the running Web API

Most of the tests are using smart contract bytecode source from Mythril samples or Ethernaut.

## To do :)
1. Expand and enhance existing unit tests:
11. Django model
11. Django serializers
11. Django views
11. Celery task
11. Django REST API
1. Validate fully Heroku packaging
1. Cover remaining requirements: handle multiple contract bytecodes POST
1. Mythril seems to display no found security issues for contracts that apparently do have some. Might not have taken the right bytecode in Remix.
1. Integrate advanced Mythril settings such as the depth
1. Handle all limit cases, error messages
1. Review and enhance exception handling
1. Refine the status and report deserializers so that json response only display the relevant fields.
1. Review security around default settings and login/passwords: Django, Celery, RabbitMQ, SQLite
1. Review production settings vs test
1. Adapt the Celery workers number settings to the deployment environment target (Heroku dynos?)
1. Enhance the diplay of issues returned by myth - return them in a dictionnary
1. Review the integration of Celery data model within Django's. Better model would be to have an Analysis model which would have a one-to-one (or one-to-many) relationship with CeleryTask model
