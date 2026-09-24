import os
from datetime import datetime
from pathlib import Path
import frontmatter
import markdown
from flask import Flask, render_template, abort, make_response, send_from_directory, url_for
import config

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
POSTS_DIR = CONTENT_DIR / "posts"
PROJECTS_DIR = CONTENT_DIR / "projects"

app = Flask(__name__)
app.config["FREEZER_DESTINATION"] = BASE_DIR / "build"
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = False
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True

# Markdown parser configured with GitHub Flavored Markdown extensions
MD_EXTENSIONS = [
    "fenced_code",
    "codehilite",
    "tables",
    "toc",
    "attr_list",
    "def_list",
    "abbr",
]
MD_EXTENSION_CONFIGS = {
    "codehilite": {
        "css_class": "highlight",
        "guess_lang": False,
        "use_pygments": True,
    }
}


def render_markdown(text: str) -> str:
    """Convert Markdown text to HTML."""
    return markdown.markdown(
        text,
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
    )


def calculate_reading_time(text: str) -> int:
    """Rough reading time calculation (approx 200 words per minute)."""
    words = len(text.split())
    return max(1, round(words / 200))


def load_post(filepath: Path) -> dict:
    """Parse a single markdown post file with YAML frontmatter."""
    post_data = frontmatter.load(filepath)
    metadata = post_data.metadata
    content_html = render_markdown(post_data.content)

    # Derive slug from filename: e.g., '2026-01-15-my-post.md' -> 'my-post'
    stem = filepath.stem
    parts = stem.split("-", 3)
    if len(parts) == 4 and parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():
        slug = parts[3]
        default_date_str = f"{parts[0]}-{parts[1]}-{parts[2]}"
    else:
        slug = stem
        default_date_str = None

    date_val = metadata.get("date")
    if isinstance(date_val, datetime):
        post_date = date_val.date()
    elif isinstance(date_val, str):
        try:
            post_date = datetime.strptime(date_val, "%Y-%m-%d").date()
        except ValueError:
            post_date = datetime.now().date()
    elif default_date_str:
        post_date = datetime.strptime(default_date_str, "%Y-%m-%d").date()
    else:
        post_date = datetime.now().date()

    return {
        "slug": metadata.get("slug", slug),
        "title": metadata.get("title", stem.replace("-", " ").title()),
        "date": post_date,
        "date_formatted": post_date.strftime("%B %d, %Y"),
        "date_iso": post_date.isoformat(),
        "summary": metadata.get("summary", ""),
        "tags": metadata.get("tags", []),
        "reading_time": calculate_reading_time(post_data.content),
        "content": content_html,
        "published": metadata.get("published", True),
    }


def get_all_posts(include_drafts: bool = False) -> list[dict]:
    """Retrieve and sort all markdown posts by date descending."""
    if not POSTS_DIR.exists():
        return []

    posts = []
    for f in POSTS_DIR.glob("*.md"):
        post = load_post(f)
        if include_drafts or post["published"]:
            posts.append(post)

    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def load_project(filepath: Path) -> dict:
    """Parse a single project markdown file with frontmatter."""
    project_data = frontmatter.load(filepath)
    metadata = project_data.metadata
    content_html = render_markdown(project_data.content)

    return {
        "slug": filepath.stem,
        "title": metadata.get("title", filepath.stem.replace("-", " ").title()),
        "description": metadata.get("description", ""),
        "tags": metadata.get("tags", []),
        "featured": metadata.get("featured", False),
        "order": metadata.get("order", 100),
        "github_url": metadata.get("github_url"),
        "live_url": metadata.get("live_url"),
        "content": content_html,
    }


def get_all_projects() -> list[dict]:
    """Retrieve and sort all project entries."""
    if not PROJECTS_DIR.exists():
        return []

    projects = [load_project(f) for f in PROJECTS_DIR.glob("*.md")]
    projects.sort(key=lambda p: (not p["featured"], p["order"], p["title"]))
    return projects


@app.context_processor
def inject_global_context():
    """Make config variables accessible in every Jinja2 template."""
    return {
        "config": config,
        "current_year": datetime.now().year,
    }


@app.route("/")
def index():
    posts = get_all_posts()[:3]
    projects = [p for p in get_all_projects() if p["featured"]][:4]
    return render_template("index.html", posts=posts, projects=projects)


@app.route("/projects/")
def projects():
    all_projects = get_all_projects()
    return render_template("projects.html", projects=all_projects)


@app.route("/blog/")
def blog():
    posts = get_all_posts()
    return render_template("blog.html", posts=posts)


@app.route("/blog/<slug>/")
def post_detail(slug):
    for post in get_all_posts(include_drafts=True):
        if post["slug"] == slug:
            return render_template("post.html", post=post)
    abort(404)


@app.route("/feed.xml")
def feed():
    posts = get_all_posts()[:15]
    xml = render_template("feed.xml", posts=posts, build_date=datetime.now())
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml; charset=utf-8"
    return response


@app.route("/CNAME")
def cname():
    """Output CNAME record for GitHub Pages custom domain routing."""
    return config.SITE_DOMAIN, 200, {"Content-Type": "text/plain"}


@app.route("/robots.txt")
def robots():
    """Standard robots.txt pointing to the sitemap/feed."""
    content = f"User-agent: *\nAllow: /\n\nSitemap: {config.SITE_URL}/feed.xml\n"
    return content, 200, {"Content-Type": "text/plain"}


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
