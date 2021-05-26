## Florestario

A basic news provider API. You can see the usage docs for the application in the [wiki](https://github.com/MarlonCorreia/florestario/wiki) =]

## Requirements 

- Python3.9+
- Django
- Django Rest Freamework
- Docker
- Docker-compose

## How to run 

### Development Mode

First, change the postgres information in the `.env` file to match the service running on your machine. Next, you can change de debug mode in the same file to true.

- Install the requirements `pip install -r requirements.txt`
- Run databse migrations `python manage.py migrate`
- Run sever `python manage.py runserver`

Access the service at `127.0.0.1:8000`

obs: I encourage the usage of a [virtualenv](https://pypi.org/project/virtualenv/) to install the packages in a project basis.

### Production Mode

For production mode, you can leave the `.env` file as is. 

- Initiate docker containers `docker-compose up`

Access the service at `127.0.0.1:8000`