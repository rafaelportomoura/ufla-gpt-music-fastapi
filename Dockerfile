FROM python:3.11.4-alpine3.18


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm /usr/src/app/requirements.txt

COPY ./app/* /usr/src/app/
