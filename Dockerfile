FROM python:3.8.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
        libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \    
    && rm -rf /root/.cache/pip

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt



RUN mkdir -p /src
COPY src/ /src/
RUN pip install -e /src
COPY tests/ /tests

WORKDIR /src