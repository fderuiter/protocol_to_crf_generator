# Performance Load Test

This directory contains a Locust configuration for exercising the ingestion API.

## Usage

Install Locust and run the test against a running instance of the service:

```bash
pip install locust
locust -f locustfile.py --headless -u 500 -r 50 -t 5m --host http://localhost:8000
```

The run simulates 500 concurrent users posting a small DOCX file to `/ingest`.
Locust reports the median and 95th percentile latencies which should stay within
five and seven minutes respectively on the reference node.
