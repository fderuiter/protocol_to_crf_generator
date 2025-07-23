# syntax=docker/dockerfile:1

FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
COPY requirements.txt ./
RUN pip install --user --no-cache-dir -r requirements.txt

COPY . .
RUN pip install --user --no-cache-dir .

FROM python:3.11-slim

WORKDIR /app

ENV PATH="/home/app/.local/bin:$PATH"

RUN addgroup --system app && adduser --system --ingroup app --uid 1000 app

COPY --from=builder /root/.local /home/app/.local
COPY --from=builder /app /app

RUN chown -R app:app /app /home/app/.local

USER app

EXPOSE 8443

CMD ["uvicorn", "protocol_to_crf_generator.api.main:app", "--host", "0.0.0.0", "--port", "8443", "--ssl-keyfile", "/certs/server.key", "--ssl-certfile", "/certs/server.crt"]
