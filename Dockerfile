FROM python:3.11-slim-buster AS base-image

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get install gcc python3-dev -y

USER root

RUN pip install --no-input --upgrade pip

# Create an application user
RUN groupadd -g 1000 app && \
    useradd -M \
            -d /app \
            -c 'Application user' \
            -u 1000 \
            -g 1000 \
            --system \
            -s /sbin/nologin \
            app

USER app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

COPY requirements.txt .
RUN pip install --no-input --no-cache-dir -r requirements.txt

COPY --chown=app:app . src/

FROM base-image AS service

WORKDIR /app/src

ENTRYPOINT ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8080"]

FROM base-image AS unittest

ENTRYPOINT ["pytest", "tests/unit"]

FROM base-image AS ittest

ENTRYPOINT ["pytest", "tests/it"]
