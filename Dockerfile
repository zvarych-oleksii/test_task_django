FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE test_django_project.settings

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


RUN python manage.py makemigrations
RUN python manage.py migrate



EXPOSE 8000


CMD ["python", "manage.py", "migrate"]
