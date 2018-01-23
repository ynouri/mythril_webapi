# mythril_webapi
Web API for [Mythril](https://github.com/ConsenSys/mythril/) - a Smart Contract Security Analysis Tool.

## Prerequisites
1. Python 3.6
1. Mythril
1. Django
1. Django Rest Framework
1. Celeri

## Local Deployment on OS X
```bash
pip install mythril
pip install Django
pin install djangorestframework
pip install -U Celery
```

## RabbitMQ
```bash
brew install rabbitmq
sudo mkdir /usr/local/sbin
sudo chown -R `whoami`:admin /usr/local/sbin
# export PATH="/usr/local/sbin:$PATH" in ./bash_profile
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
