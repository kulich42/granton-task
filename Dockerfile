FROM python:3.9
COPY api ./api
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install
ENV OPENAI_API_KEY=$OPENAI_API_KEY
EXPOSE 8000
ENTRYPOINT ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "api.main:app", "--reload", "--port", "8000"]