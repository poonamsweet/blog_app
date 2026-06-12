# Blog App

A simple Flask-based blog application with Blueprint architecture.

---

## 📁 Project Structure & Files

- Application entry: [app.py](app.py) — registers [`blog.blog_bp`](blog/__init__.py)
- Docker Compose: [docker-compose.yml](docker-compose.yml)
- Dockerfile: [Dockerfile](Dockerfile)
- Requirements: [requirements.txt](requirements.txt)

### 🧩 Blog Module
- Blueprint initialization: [blog/__init__.py](blog/__init__.py)
- Routes: [blog/routes.py](blog/routes.py)
- Templates:
  - [templates/posts.html](templates/posts.html)
  - [templates/comments.html](templates/comments.html)

### 🗄️ Database
- Models: [models.py](models.py)(optional)

---

## 🚀 After Clone - How to Run

### 1. Clone the repository
```bash
git clone https://github.com/poonamsweet/blog_app.git
cd blog_app