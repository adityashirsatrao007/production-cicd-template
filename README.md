# 04 · Live Demo + CI/CD Template

> **Target role: All (AI / ML / Data Engineer)**
> **Resume-ready label:** *"Deployed production project with CI/CD — live URL, GitHub Actions (lint + test + build), /health endpoint, uptime 99.9%"*

The single most effective change to your resume: a **live, deployed URL** next to each project. Accepted interns always show deployed demos with user/performance numbers. This repo is a drop-in template — copy the CI/CD, Dockerfile, and health endpoint into any of your projects.

## What this adds to any repo

- **GitHub Actions CI** — runs lint + tests + build + image publish on every push/PR
- **Multi-stage Dockerfile** + `.dockerignore`
- **`/health` endpoint** with uptime/UptimeRobot badge support
- **Render / Railway / Fly.io** deploy configs
- **README badges** (build status, uptime, test coverage) — this is what makes resumes pop

## Resume bullet (copy/adapt)

> **Production Deployment & CI/CD** · *GitHub Actions, Docker, Render*
> - Deployed [Project] with **CI/CD: auto lint + tests + build on every PR**, cutting regression risk
> - Live demo at [URL] serving [N] requests/day at **99.9% uptime** (uptime-monitored)
> - Added `/health` + metrics endpoint; test coverage **85%+**

## How to use with your projects

```bash
# Copy the template files into your project repo
cp -r .github Dockerfile .dockerignore render.yaml app/health.py <your-project>/

# 1. Add a /health route (FastAPI example included)
# 2. Push to GitHub — CI runs automatically
# 3. Deploy: Render "New +" → "Blueprint" (uses render.yaml)
# 4. Add live URL to your resume top
```

## GitHub Actions CI

Runs on push + PR (`.github/workflows/ci.yml`): `ruff` lint, `pytest` with
coverage, multi-arch Docker build, and optional `docker push` on main.

## Deploy targets

| Provider | File | Notes |
|----------|------|-------|
| Render | `render.yaml` | Blueprint deploy, free tier, auto HTTPS |
| Railway | — | `railway up` after `railway init` |
| Fly.io | — | `fly launch` with the Dockerfile |

## Role fit

| Role | Fit |
|------|-----|
| All roles | Primary — live URLs are the #1 missing signal on fresher resumes |
