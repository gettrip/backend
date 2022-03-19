FROM python:3.10.2-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /webapp

RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /webapp/
RUN poetry install --no-dev

COPY backend /webapp/backend

CMD ["python", "-m", "backend"]
