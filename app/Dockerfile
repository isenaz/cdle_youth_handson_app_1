FROM python:3.8
ENV PYTHONBURRERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt update && apt install -y sqlite3 vim less
RUN pip install --upgrate pip
RUN pip install -r requirements.txt
