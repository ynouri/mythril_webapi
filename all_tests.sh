#!/usr/bin/env bash

# Django tests
./manage.py test test/

# Command line tests
./test/test_command_line.sh