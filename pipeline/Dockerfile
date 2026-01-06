FROM python:3.13.1-slim

RUN pip install pyarrow pandas

COPY --from=ghcr.io/astral-sh/uv:latest /uv/ /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock pipeline.py ./

RUN  uv sync --locked

ENTRYPOINT ["uv", "run", "python", "pipeline.py"]