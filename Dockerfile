FROM python:3.10.7

RUN python -m pip install --upgrade pip

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt    