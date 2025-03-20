FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y make && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

RUN uv pip install --system --no-cache-dir ".[dev]"

ENV PYTHONPATH=/app
