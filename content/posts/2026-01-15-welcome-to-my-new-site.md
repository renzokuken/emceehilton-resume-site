---
title: Welcome to My New Website
date: 2026-01-15
summary: Migrating from traditional static generators to a modern Python-powered Frozen-Flask architecture.
tags: [web, python, flask]
published: true
---

Welcome to my new personal corner on the web!

After using systems like Hyde and Jekyll for years, I wanted a modern setup that combined the **developer happiness of Flask** with the **zero-maintenance resilience of static HTML hosting**.

## Why this architecture?

If you enjoy Python and Flask, traditional static generators often feel like an unnecessary abstraction:

1. **Native Flask routes and Jinja2:** No idiosyncratic templating engines or complex configuration files.
2. **Instant live reload:** Running `python app.py` starts Flask's development server with instant preview.
3. **Static deployment:** Running `python freeze.py` generates pure HTML, CSS, and JS that can be hosted anywhere for free—GitHub Pages, Cloudflare Pages, or AWS S3.
4. **Custom Domain with SSL:** Zero server management, zero database vulnerabilities, and free automatic SSL certificates.

## Code Highlighting Example

Here is how simple it is to freeze a Flask application:

```python
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    freezer.freeze()
```

Stay tuned for more updates on software engineering, open source projects, and technical experiments!
