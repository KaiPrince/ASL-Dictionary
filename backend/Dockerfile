FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN python -m pip install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-cache
COPY . /code/

RUN apt-get update && apt-get install -y \
	ffmpeg \
	&& rm -rf /var/lib/apt/lists/*
