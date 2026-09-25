from pathlib import Path
from datetime import datetime
import frontmatter
import markdown
from flask import Flask, render_template
import config
import resume_data

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
PROJECTS_DIR = CONTENT_DIR / "projects"

app = Flask(__name__)
app.config["FREEZER_DESTINATION"] = BASE_DIR / "build"
app.config["FREEZER_RELATIVE_URLS"] = True
app.config["FREEZER_REMOVE_EXTRA_FILES"] = False
app.config["FREEZER_IGNORE_MIMETYPE_WARNINGS"] = True

MD_EXTENSIONS = ["fenced_code", "tables", "attr_list"]


def render_markdown(text: str) -> str:
    """Convert Markdown to HTML."""
    return markdown.markdown(text, extensions=MD_EXTENSIONS)


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
    """Make config and resume variables accessible across templates."""
    return {
        "config": config,
        "resume": resume_data,
        "current_year": datetime.now().year,
    }


@app.route("/")
def index():
    projects = get_all_projects()
    return render_template("index.html", projects=projects)


@app.route("/CNAME")
def cname():
    """Output CNAME record for GitHub Pages custom domain routing."""
    return config.SITE_DOMAIN, 200, {"Content-Type": "text/plain"}


@app.route("/robots.txt")
def robots():
    """Standard robots.txt."""
    content = "User-agent: *\nAllow: /\n"
    return content, 200, {"Content-Type": "text/plain"}


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
