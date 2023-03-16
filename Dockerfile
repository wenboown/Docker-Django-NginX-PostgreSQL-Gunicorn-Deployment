FROM python:3.11.2-slim-bullseye

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/djangoapp/src

# install psycopg2 dependencies
RUN apt update \
    && apt -y install libpq-dev python-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /opt/services/djangoapp/src/requirements.txt
WORKDIR /opt/services/djangoapp/src
RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp/src
# https://stackoverflow.com/questions/59719175/where-to-run-collectstatic-when-deploying-django-app-to-heroku-using-docker
RUN cd hello && python manage.py collectstatic --no-input 


EXPOSE 80
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "hello", "hello.wsgi:application"]

