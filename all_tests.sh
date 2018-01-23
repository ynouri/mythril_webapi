#!/usr/bin/env bash

# Django tests
python manage.py test test/ --verbosity=1

# Command line tests
./test/test_command_line.sh