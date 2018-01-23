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
1. *mythril_webapi*: Django module
1. *myth_rest*: Django REST Framework app

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
celery -A tasks worker --loglevel=info
celery -A tasks worker -c 2 --loglevel=info # To run wit 2 workers
```

## Production Build and Installation
How to build the application for upload to a server
```bash
Note: assume it is a dedicated server not AWS or Heroku.
```

## Running Tests

## Notes


## What would have been done with more time :)
1. More tests
1. Heroku packaging
1. Somehow I cannot get myth to display security issues for contracts that apparently do have some, would need some additional time to investigate this.
