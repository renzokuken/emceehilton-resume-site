# Personal Website & Portfolio Template

A fast, minimalist personal website and blog built with **Flask**, **Jinja2**, and **Markdown**, frozen into static HTML via **Frozen-Flask** for free, zero-maintenance hosting on **GitHub Pages** or **Cloudflare Pages** with your custom domain.

---

## Architecture Overview

If you have experience with Flask and Hyde/Jekyll, this architecture gives you the best of both worlds:

- **Familiar Flask & Jinja2:** Write standard Python routes and clean Jinja templates with blocks and inheritance (`{% extends "base.html" %}`).
- **Hyde/Jekyll-style Flat Files:** Write articles and projects in Markdown with YAML frontmatter (`title`, `date`, `tags`, etc.).
- **Modern Syntax Highlighting:** Powered by Pygments in both Light and Dark themes.
- **Dark / Light Mode:** Built-in CSS custom properties with automatic system detection (`prefers-color-scheme`) and manual toggle persistence.
- **Automated Freezing:** Generates pure static files (`build/`) with clean relative URLs, custom `CNAME`, `robots.txt`, and RSS/Atom feed (`feed.xml`).
- **Free Custom Domain Hosting:** Continuous deployment via GitHub Actions with automated Let's Encrypt HTTPS.

---

## Directory Structure

```text
emceehilton-static-site/
├── config.py                  # Site metadata, author details, domain, social links
├── app.py                     # Flask dev server, markdown parser, route handlers
├── freeze.py                  # Frozen-Flask compiler to generate static HTML
├── requirements.txt           # Python dependencies
├── Makefile                   # Developer shortcuts (dev, build, preview)
├── content/
│   ├── posts/                 # Markdown blog articles with YAML frontmatter
│   │   ├── 2026-01-15-welcome-to-my-new-site.md
│   │   └── 2026-02-28-python-static-sites-frozen-flask.md
│   └── projects/              # Markdown project showcase items
│       ├── data-validator.md
│       └── personal-website.md
├── templates/
│   ├── base.html              # HTML shell, navigation, theme toggle, footer
│   ├── index.html             # Homepage: Hero bio, featured projects, recent posts
│   ├── projects.html          # Portfolio listing
│   ├── blog.html              # Article listing
│   ├── post.html              # Individual post layout with Pygments code highlighting
│   ├── feed.xml               # Atom / RSS 2.0 XML feed
│   └── 404.html               # 404 error page
├── static/
│   ├── css/
│   │   ├── style.css          # Design system & dark/light mode tokens
│   │   └── syntax.css         # Pygments syntax highlighting (Light & Dark)
│   ├── js/
│   │   └── main.js            # Theme toggle handler
│   └── images/
│       └── avatar.svg         # Profile avatar placeholder
└── .github/
    └── workflows/
        └── deploy.yml         # GitHub Actions CI/CD to auto-freeze and deploy
```

---

## Quickstart

### 1. Activate Environment

A Python virtual environment is already initialized in `.venv/`:

```bash
cd ~/renzokuken/emceehilton-static-site
source .venv/bin/activate
```

*(If you ever need to re-create it: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`)*

### 2. Run Local Development Server

Start Flask with live reload:

```bash
make dev
# or: python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Any edits to templates, CSS, or markdown files update instantly.

### 3. Freeze & Preview Static Site

To build the static HTML output into `build/`:

```bash
make build
# or: python freeze.py
```

To freeze and serve the static files locally at [http://127.0.0.1:8000](http://127.0.0.1:8000):

```bash
make preview
# or: python freeze.py --serve
```

---

## Adding & Editing Content

### Blog Posts (`content/posts/`)

Create a Markdown file inside `content/posts/`. Filenames can follow `YYYY-MM-DD-slug.md` or any name:

```markdown
---
title: My First Article
date: 2026-03-01
summary: A brief summary displayed in article cards and RSS feeds.
tags: [python, web, devops]
published: true
---

Your markdown text goes here...

```python
def hello_world():
    print("Code highlighting works out of the box!")
```
```

### Projects (`content/projects/`)

Create a Markdown file inside `content/projects/`:

```markdown
---
title: Project Name
description: Brief one-line pitch of what this project does.
featured: true
order: 1
tags: [Python, FastAPI, Docker]
github_url: https://github.com/renzokuken/your-repo
live_url: https://yourproject.com
---

Extended project documentation or notes...
```

---

## Deploying to Your Custom Domain

### Step 1: Update Domain in `config.py`

Open `config.py` and replace `yourdomain.com` with your domain:

```python
SITE_DOMAIN = "mikehilton.dev"   # Your domain or subdomain
SITE_URL = f"https://{SITE_DOMAIN}"
```

*(Frozen-Flask will automatically generate the `CNAME` file required by GitHub Pages).*

### Step 2: Push to GitHub

Initialize git and push to your GitHub repository:

```bash
cd ~/renzokuken/emceehilton-static-site
git init
git add .
git commit -m "Initial commit of personal website"
git branch -M main
git remote add origin git@github.com:renzokuken/emceehilton-static-site.git
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/renzokuken/emceehilton-static-site/settings/pages`.
2. Under **Build and deployment**:
   - **Source:** Select **GitHub Actions**.
3. Under **Custom domain**:
   - Enter your domain (e.g. `mikehilton.dev`).
   - Check **Enforce HTTPS** (once DNS records propagate, GitHub issues a free Let's Encrypt certificate).

### Step 4: Configure DNS at Your Registrar

At your DNS registrar (Namecheap, Cloudflare, Porkbun, Google Domains/Squarespace, etc.), create these records:

#### Apex Domain (`mikehilton.dev`):
Create four **A** records pointing `@` to GitHub's Anycast IP addresses:
- `185.199.108.153`
- `185.199.109.153`
- `185.199.110.153`
- `185.199.111.153`

#### Subdomain (`www.mikehilton.dev`):
Create a **CNAME** record:
- **Host / Name:** `www`
- **Value / Target:** `renzokuken.github.io.`

Whenever you push commits to `main`, GitHub Actions (`.github/workflows/deploy.yml`) will automatically freeze your Flask app and deploy the updated static site!
