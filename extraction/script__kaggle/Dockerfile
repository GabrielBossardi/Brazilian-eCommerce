FROM python:3.10.8 AS base
ADD .kaggle ./root/.kaggle

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip install poetry==1.2.2
RUN poetry config virtualenvs.create false --local
RUN poetry install --only main

COPY kaggle_connector.py main.py ./

LABEL image.version=latest
LABEL image.name=extractor/kaggle