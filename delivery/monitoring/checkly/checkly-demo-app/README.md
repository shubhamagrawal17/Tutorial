# Checkly demo app

A small Node.js demo application and Playwright browser check used to demonstrate uptime and browser-based monitoring with Checkly.

## Run locally

```bash
docker build -t checkly-demo .
docker run --rm -p 3000:3000 checkly-demo
```

Open `http://localhost:3000` and inspect the browser test under `tests/`.

## Checkly agent

Configure the Checkly agent using a newly created API key supplied through your deployment platform's secret store. Do not paste API keys into shell history, command-line arguments, Docker Compose files committed to Git, or README documentation.

**Credential hygiene:** the previous version of this README contained a value formatted like a Checkly API key and a sample admin/password pair. The key has been removed from this file, but it may remain in Git history or other copies. Treat it as exposed: revoke/rotate it in Checkly, review access logs, and replace the demo login with a unique test credential before using this app.
