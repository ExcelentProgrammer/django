#!/bin/bash

cp .env.example .env
virtualenv venv
. ./venv/bin/activate
pip install -r ./requirements/local.txt
python3 ./manage.py makemigrations
python3 ./manage.py migrate

echo "DJANGO SECRET KEY: "
python3 ./manage.py generate_secret_key