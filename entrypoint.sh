#!/bin/sh
set -e
docker compose exec web python3 manage.py migrate --noinput
docker compose exec web python3 manage.py collectstatic --noinput
docker compose exec web python3 manage.py seed

exec "$@"
