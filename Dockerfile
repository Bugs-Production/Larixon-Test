FROM python:3.11

WORKDIR /app

COPY  . .

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=larixon.settings

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:80"]