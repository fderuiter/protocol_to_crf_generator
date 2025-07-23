# TLS Configuration

To enforce HTTPS, the application expects a certificate bundle mounted at `/certs`.
Use OpenSSL to generate a self-signed certificate for testing:

```bash
mkdir -p deploy/certs
openssl req -x509 -nodes -newkey rsa:4096 -keyout deploy/certs/server.key \
  -out deploy/certs/server.crt -days 365 -subj "/CN=localhost"
```

Run the container with the `docker-compose.yml` in the `deploy` directory:

```bash
cd deploy
docker-compose up --build
```

The service is then available at `https://localhost:8443`.

