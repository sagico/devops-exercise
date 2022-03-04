FROM python:3.10.2 AS builder

ENV JSON_LOGGING=1

WORKDIR /coin-master
RUN pip install -U pip poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev
COPY . .

EXPOSE 8000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--factory", "coin_master.api:create_app", "--no-access-log", "--log-level", "critical"]
