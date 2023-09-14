#!/usr/bin/env bash
# exit on error
set -o errexit


python3.10 manage.py collectstatic --no-input
python3.10 manage.py migrate
python3.10 manage.py makemessages --all
python3.10 manage.py compilemessages