# syntax=docker/dockerfile:1

FROM python:3-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ../requirements.txt /code/

RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

COPY . /code/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8090" ]