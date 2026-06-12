# Blog App

Simple Flask blog application.

## Files & Symbols
- Application entry: [app.py](app.py) — imports [`blog.blog_bp`](blog/__init__.py)
- Docker compose: [docker-compose.yml](docker-compose.yml)
- Dockerfile: [Dockerfile](Dockerfile)
- Python requirements: [requirements.txt](requirements.txt)
- Database models: [models.py](models.py) and [blog/models.py](blog/models.py)
- Blueprint and routes: [blog/__init__.py](blog/__init__.py) (exports `blog_bp`) and [blog/routes.py](blog/routes.py)
- Templates: [templates/posts.html](templates/posts.html), [templates/comments.html](templates/comments.html)

## Quick start (Docker)
1. Build and run:
```sh
docker-compose up --build
```
2. Open http://localhost:5000

## Run locally
1. Create virtualenv and install:
```sh
python -m venv .venv
.venv/Scripts/activate   # or `source .venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
```
2. Export env vars from [.env](.env) or set them in your environment.
3. Run:
```sh
python app.py
```

## Notes
- The Flask app registers the blueprint from [`blog.blog_bp`](blog/__init__.py) in [app.py](app.py).
- Database is configured via environment variables in [.env](.env) and [docker-compose.yml](docker-compose.yml).
