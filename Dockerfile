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

ENV PATH="/root/.local/bin:$PATH"

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "protocol_to_crf_generator.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
