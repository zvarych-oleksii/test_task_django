# Test task on Django REST API
## Install service
```bash
git clone https://github.com/zvarych-oleksii/test_task_django
cd test_task_django
```

## To run service:
### With docker
```bash
docker-compose build
docker-compose up
```

In browser 0.0.0.0:8000

### or without docker
#### Create and activate virtual env
```bash
python -m venv vevn
source  venv/bin/activate
```
#### Install requirements 
```bash
pip install -r requirements.txt 
```

#### Make migrations and run the service 
```bash
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```

In browser 127.0.0.1:8000