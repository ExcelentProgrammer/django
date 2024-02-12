virtualenv venv
source ./.venv/bin/activate
pip install -r ./requirements/local.txt
python3 ./manage.py makemigrations
python3 ./manage.py migrate
# python3 manage.py runserver