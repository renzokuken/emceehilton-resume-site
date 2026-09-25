# Michael Hilton — Personal Website & Resume Splash Page

A fast, minimalist personal resume and splash website built with **Flask**, **Jinja2**, and **Frozen-Flask**, deployed as pure static HTML to **GitHub Pages** (or Cloudflare Pages) with custom domain support.

---

## Architecture Overview

- **Static Generation with Python & Flask:** Standard Flask routing and Jinja2 templating, frozen into pure static files inside `build/`. Zero JavaScript framework overhead, sub-50ms page load times, 100/100 Lighthouse performance.
- **Structured Resume Data (`resume_data.py`):** Career history, technical skills matrix, education, and links are separated into a clean Python data structure. Update your resume anytime without writing HTML.
- **Official Resume PDF Included:** Bundled in `static/Mike_Hilton_Resume.pdf` with direct download buttons in the header and hero section.
- **Print / PDF Optimized:** Includes a custom `@media print` stylesheet. Pressing `Cmd + P` (or clicking the **Print / PDF** button) formats the page cleanly for printing or saving to PDF without navigation bars or shadows.
- **Dark & Light Mode:** System-aware theme toggle that remembers user preferences via `localStorage`.
- **Zero Maintenance:** Free static hosting via GitHub Pages with automated HTTPS and custom domain configuration.

---

## Directory Structure

```text
emceehilton-static-site/
├── resume_data.py             # Complete resume data (profile, skills, work history)
├── config.py                  # Domain, site title, navigation, and social links
├── app.py                     # Flask dev server & project loader
├── freeze.py                  # Frozen-Flask compiler to generate static HTML
├── requirements.txt           # Python dependencies
├── Makefile                   # Developer shortcuts (make dev, make build, make preview)
├── content/
│   └── projects/              # Markdown project showcase items
│       ├── data-validator.md
│       └── personal-website.md
├── templates/
│   ├── base.html              # HTML shell, header nav, theme switch, footer
│   ├── index.html             # Executive splash page, skills matrix, experience timeline
│   └── 404.html               # 404 error page
├── static/
│   ├── Mike_Hilton_Resume.pdf # Downloadable resume PDF
│   ├── css/
│   │   ├── style.css          # Design system & dark/light mode tokens
│   │   └── syntax.css         # Pygments code styling
│   ├── js/
│   │   └── main.js            # Theme toggle handler
│   └── images/
│       └── avatar.svg         # Profile monogram placeholder
└── .github/
    └── workflows/
        └── deploy.yml         # GitHub Actions workflow for automatic deployment
```

---

## Quickstart

### 1. Activate Environment

```bash
cd ~/renzokuken/emceehilton-static-site
source .venv/bin/activate
```

### 2. Live Development

```bash
make dev
# or: python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000). Any changes to `resume_data.py`, templates, or styles update live.

### 3. Build & Preview Static Output

```bash
make preview
# or: python freeze.py --serve
```
This builds static HTML inside `build/` and starts a local web server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Updating Your Resume Data

Open `resume_data.py` to update:
- **`PROFILE`**: Name, title, location, email, LinkedIn, and GitHub links.
- **`SUMMARY`**: Executive summary and professional abstract.
- **`SKILL_GROUPS`**: Technical skills grouped by category.
- **`EXPERIENCE`**: Roles, companies, dates, and bullet points.
- **`EDUCATION` & `MISC`**: Degrees, coursework, languages, and interests.

---

## Deploying to Your Custom Domain

1. In [`config.py`](config.py), set your domain:
   ```python
   SITE_DOMAIN = "yourdomain.com"
   ```
2. Push your repository to GitHub:
   ```bash
   git add .
   git commit -m "Update resume splash page"
   git push origin main
   ```
3. In GitHub: **Settings** → **Pages** → under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Configure your custom domain DNS records (A records to GitHub Pages IPs, CNAME for `www`).
