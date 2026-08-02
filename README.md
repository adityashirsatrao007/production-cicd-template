<div align="center">

# Production CI/CD Template

**Drop-in deployment + CI/CD starter — lint, test, build, publish, and `/health` on every push.**

GitHub Actions · Docker · FastAPI · Render / Railway / Fly.io

[![CI](https://github.com/adityashirsatrao007/production-cicd-template/actions/workflows/ci.yml/badge.svg)](https://github.com/adityashirsatrao007/production-cicd-template/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Coverage](https://img.shields.io/badge/coverage-%E2%89%A570%25-brightgreen)](https://github.com/adityashirsatrao007/production-cicd-template/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

A copy-ready template for taking a project to production with **CI/CD built in**: a GitHub Actions pipeline (lint → test with coverage gate → multi-arch Docker build), a multi-stage `Dockerfile`, a `/health` endpoint for uptime monitoring, and deploy configs for Render, Railway, and Fly.io.

Copy the files into any project repo and push — the pipeline runs automatically.

## What's included

- **GitHub Actions CI** — `ruff` lint, `pytest` with a 70% coverage gate, multi-arch Docker build, optional image publish on `main`
- **Multi-stage Dockerfile** + `.dockerignore` for small, cached images
- **`/health` endpoint** — ready for UptimeRobot / uptime badges
- **Deploy configs** — `render.yaml` blueprint, Railway, Fly.io
- **Coverage upload** — Codecov action wired in

## Quick start

```bash
# Copy the template into your project
cp -r .github Dockerfile .dockerignore render.yaml app/health.py <your-project>/

# Push — CI runs automatically (lint → tests → build)
git push origin main

# Deploy on Render
# "New +" → "Blueprint" (uses render.yaml) → auto HTTPS
```

## CI pipeline

| Stage | What runs |
|-------|-----------|
| `lint` | `ruff check app tests` |
| `test` | `pytest --cov=app --cov-fail-under=70` + Codecov upload |
| `docker` | multi-arch Docker build (`app:ci-${{ github.sha }}`) |

## Deploy targets

| Provider | File | Notes |
|----------|------|-------|
| Render | `render.yaml` | Blueprint deploy, free tier, auto HTTPS |
| Railway | — | `railway up` after `railway init` |
| Fly.io | — | `fly launch` with the Dockerfile |

## Project layout

```
.github/workflows/ci.yml   lint + test + docker build
Dockerfile                 multi-stage production image
.dockerignore              keeps images lean
app/health.py              /health endpoint
render.yaml                Render blueprint deploy config
tests/                     health endpoint tests
```

## License

[MIT](LICENSE)
