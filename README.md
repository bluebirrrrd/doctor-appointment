# Doctor appoinment Django app (v1)


## Getting Started

First of all, clone the repo:

```bash
git clone https://github.com/bluebirrrrd/doctor-appointment.git
cd doctor-appointment
```

## Dependencies
* `npm` and `python3` for dev mode (will be installed automatically if you run `start.sh`)

## Installing & running

### Prod mode
`sudo ./start.sh` starts the script to install all dependencies and run the app

### Dev mode
```
npm install
python3 -m virtualenv -p python3 .env
source ./.env/bin/activate
pip install -r dev.txt
pre-commit install

python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

## Important note
To use app properly you need to create some doctors in admin panel. To access it, you need to create a superuser.
If you run `start.sh`, you'll be asked for superuser credentials during setup. If you're running in dev mode,
just type `python manage.py createsuperuser` and provide the data.

## Other commands

### kill the process in prod mode
```bash
sudo kill `cat gunicorn.pid`
```
