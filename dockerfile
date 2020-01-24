FROM python:3.6

ADD . /my-django-app

WORKDIR /my-django-app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "/my-django-app/manage.py", "runserver", "0.0.0.0:8000" ]
