"""Site configuration for personal website."""

# Profile Information
AUTHOR_NAME = "Mike Hilton"
AUTHOR_EMAIL = "hilton.mike.c@gmail.com"
SITE_TITLE = "Mike Hilton | Personal Website & Portfolio"
SITE_TAGLINE = "Software Engineer & Builder"
SITE_DESCRIPTION = (
    "Personal website, portfolio, and technical writing by Mike Hilton."
)
AUTHOR_BIO = (
    "Hi, I'm Mike! I'm a software engineer passionate about building high-quality "
    "developer tools, data pipelines, and web applications. Welcome to my personal site."
)

# Domain Configuration
# Replace with your actual custom domain (e.g., "mikehilton.com" or "mhilton.dev")
SITE_DOMAIN = "yourdomain.com"
SITE_URL = f"https://{SITE_DOMAIN}"

# Social and Contact Links
SOCIAL_LINKS = [
    {
        "name": "GitHub",
        "url": "https://github.com/renzokuken",
        "icon": "github",
    },
    {
        "name": "LinkedIn",
        "url": "https://www.linkedin.com/in/YOUR_LINKEDIN_HANDLE",
        "icon": "linkedin",
    },
    {
        "name": "Email",
        "url": "mailto:hilton.mike.c@gmail.com",
        "icon": "email",
    },
    {
        "name": "RSS",
        "url": "/feed.xml",
        "icon": "rss",
    },
]

# Navigation Items
NAV_ITEMS = [
    {"title": "Home", "endpoint": "index"},
    {"title": "Projects", "endpoint": "projects"},
    {"title": "Blog", "endpoint": "blog"},
]
