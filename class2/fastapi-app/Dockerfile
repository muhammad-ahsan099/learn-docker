FROM python:3.12 AS builder

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

COPY main.py ./

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /app /app

EXPOSE 8000

# Run the application.
CMD ["/app/.venv/bin/fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]