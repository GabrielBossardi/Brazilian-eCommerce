FROM python:3.10.1

WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==1.1.11 && \
    poetry config virtualenvs.create false --local && \
    poetry install --no-dev

COPY ./ /usr/src/app/

RUN dbt deps
