FROM python:3.10

# Install ffmpeg for video processing
RUN apt-get update && apt-get install -y \
	ffmpeg \
	&& rm -rf /var/lib/apt/lists/*

# Set up app
RUN mkdir /code
WORKDIR /code
RUN python -m pip install poetry
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-interaction --no-cache
COPY . /code/

# Run server
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
