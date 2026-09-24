#!/usr/bin/env python3
"""Freeze the Flask website into static HTML/CSS/JS files inside build/."""

import sys
import shutil
from pathlib import Path
from flask_frozen import Freezer
from app import app, get_all_posts, get_all_projects

freezer = Freezer(app)


@freezer.register_generator
def post_detail():
    """Ensure Frozen-Flask freezes all blog posts."""
    for post in get_all_posts(include_drafts=False):
        yield {"slug": post["slug"]}


def main():
    print("Freezing website into static files...")
    
    # Clean old build
    build_dir = Path(app.config["FREEZER_DESTINATION"])
    if build_dir.exists():
        shutil.rmtree(build_dir)
        
    freezer.freeze()
    
    print(f"Site successfully frozen to: {build_dir}")
    print(f"Total files generated: {sum(1 for _ in build_dir.rglob('*') if _.is_file())}")
    
    if "--serve" in sys.argv:
        freezer.serve(port=8000)


if __name__ == "__main__":
    main()
