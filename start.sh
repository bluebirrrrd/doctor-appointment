#! /bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Run with root!"
    exit 1
fi

export DEBIAN_FRONTEND=noninteractive

# TODO: set up nginx+wsgi and normal db
apt-get install -y python3 npm

npm install
virtualenv -p python3 .env
source ./.env/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput

gunicorn doctor_appointment.wsgi:application -D -b :80 -P gunicorn.pid
echo "The app is listening to port 80!"