"""Site configuration for personal resume and splash website."""

import resume_data

# Author & Profile Metadata
AUTHOR_NAME = resume_data.PROFILE["name"]
SITE_TITLE = f"{AUTHOR_NAME} | Senior Data & Cloud Infrastructure Engineer"
SITE_TAGLINE = resume_data.PROFILE["tagline"]
SITE_DESCRIPTION = (
    "Personal website, resume, and portfolio of Michael Hilton. "
    "15+ years of data engineering, cloud architecture, and streaming ETL."
)

# Custom Domain Configuration
SITE_DOMAIN = "yourdomain.com"
SITE_URL = f"https://{SITE_DOMAIN}"

# Navigation Items (Jump links on the single-page splash layout)
NAV_ITEMS = [
    {"title": "Summary", "url": "#summary"},
    {"title": "Experience", "url": "#experience"},
    {"title": "Skills", "url": "#skills"},
    {"title": "Projects", "url": "#projects"},
    {"title": "Education", "url": "#education"},
]

# Social and Contact Links
SOCIAL_LINKS = [
    {
        "name": "Email",
        "url": f"mailto:{resume_data.PROFILE['email']}",
        "icon": "email",
    },
    {
        "name": "GitHub",
        "url": resume_data.PROFILE["github"],
        "icon": "github",
    },
    {
        "name": "LinkedIn",
        "url": resume_data.PROFILE["linkedin"],
        "icon": "linkedin",
    },
    {
        "name": "Download PDF",
        "url": resume_data.PROFILE["resume_pdf_url"],
        "icon": "pdf",
        "is_primary": True,
    },
]
