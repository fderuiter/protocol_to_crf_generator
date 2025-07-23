# Staging Environment Setup

A staging environment mirrors production and allows testing new builds before promoting them live.

## Prerequisites

- Docker and Docker Compose installed
- TLS certificates generated as described in [TLS Configuration](tls-setup.md)

## Starting the Stack

Run the following from the repository root:

```bash
docker compose -f deploy/docker-compose.staging.yml up -d --build
```

This command launches the API listening on `https://localhost:8443` using the certificates in `deploy/certs`.

## Updating the Environment

Rebuild the image or pull a new version and restart:

```bash
docker compose -f deploy/docker-compose.staging.yml pull
docker compose -f deploy/docker-compose.staging.yml up -d
```

Stopping the stack is just as simple:

```bash
docker compose -f deploy/docker-compose.staging.yml down
```
