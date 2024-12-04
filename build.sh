#!/usr/bin/env bash

set -o errexit

pip installl -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate