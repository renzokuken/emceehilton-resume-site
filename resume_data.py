"""Structured resume and career data for Michael Hilton."""

PROFILE = {
    "name": "Michael Hilton",
    "title": "Senior Data & Cloud Infrastructure Engineer",
    "tagline": "15+ Years in Data Engineering, Enterprise Cloud Architecture & Streaming ETL",
    "location": "Oakland, CA",
    "email": "hilton.mike.c@gmail.com",
    "phone": "(415) 816-5982",
    "show_phone": False,  # Kept false by default to prevent web crawlers/spam, toggleable
    "github": "https://github.com/renzokuken",
    "linkedin": "https://www.linkedin.com/in/YOUR_LINKEDIN_HANDLE",
    "resume_pdf_url": "static/Mike_Hilton_Resume.pdf",
}

SUMMARY = (
    "Senior Data and Cloud Infrastructure Engineer with over 15 years of experience across "
    "data engineering, streaming ETL, cloud migration, and enterprise solutions architecture. "
    "Deep expertise in Google Cloud Platform (GCP), Python, distributed pipelines, and DevOps automation. "
    "Extensive history architecting and delivering high-availability cloud infrastructure and mission-critical "
    "data solutions for Fortune 500 enterprises within Google Professional Services (PSO) and Alooma."
)

SKILL_GROUPS = [
    {
        "category": "Cloud & Infrastructure",
        "skills": [
            "Google Cloud Platform (GCP)",
            "BigQuery",
            "Cloud Dataflow",
            "Cloud Storage",
            "GKE / Kubernetes",
            "Terraform",
            "Docker",
        ],
    },
    {
        "category": "Data Engineering & Warehousing",
        "skills": [
            "Real-time Streaming ETL",
            "Data Pipeline Architecture",
            "BigQuery",
            "Snowflake",
            "Redshift",
            "PostgreSQL",
            "Data Modeling & Schema Design",
            "Query Optimization",
        ],
    },
    {
        "category": "Software & Languages",
        "skills": [
            "Python",
            "SQL",
            "Bash / Shell",
            "Java",
            "R",
            "Jinja2 / Flask",
        ],
    },
    {
        "category": "DevOps, SRE & Methodologies",
        "skills": [
            "CI/CD Automation",
            "Git Workflow",
            "Test Automation",
            "Site Reliability Engineering (SRE)",
            "Data Quality Auditing",
            "Technical Consulting & Mentorship",
        ],
    },
]

EXPERIENCE = [
    {
        "company": "Google",
        "location": "Sunnyvale, CA",
        "role": "Cloud Solutions Architect / Senior Data Engineer (PSO)",
        "period": "2019 – Present",
        "badge": "Current Role",
        "context": "Alooma was acquired by Google in early 2019; absorbed into Google's Professional Services Organization (PSO).",
        "bullets": [
            "Architected and delivered end-to-end cloud infrastructure, migration strategies, and enterprise data pipelines for Fortune 500 customers, ensuring high availability, fault tolerance, and multi-region scalability.",
            "Led complex cloud migrations and modernization initiatives, dramatically reducing infrastructure costs and improving system throughput via GCP services.",
            "Partnered closely with customer stakeholders and executive leadership to align technical architectures with strategic business objectives, accelerating time-to-market for mission-critical applications.",
            "Collaborated directly with Google Product and Engineering teams to provide customer feedback, driving product improvements and directly influencing roadmaps for core GCP data services.",
            "Mentored and upskilled customer engineering organizations on modern cloud best practices, DevOps methodologies, and Site Reliability Engineering (SRE) principles.",
        ],
    },
    {
        "company": "Alooma",
        "location": "Redwood City, CA",
        "role": "Technical Solutions Engineer & SME",
        "period": "2016 – 2019",
        "badge": "Acquired by Google",
        "context": "Real-time streaming ETL platform moving transactional data into cloud warehouses (acquired by Google in 2019).",
        "bullets": [
            "Designed and implemented scalable real-time data integration pipelines, enabling enterprise clients to seamlessly ingest, transform, and load massive streaming datasets into Redshift, Snowflake, and BigQuery.",
            "Served as the technical subject matter expert during onboarding and enterprise implementation phases, troubleshooting complex data infrastructure bottlenecks and optimizing query performance.",
            "Developed custom integrations and connector plugins in Python and Java to expand platform capabilities and support diverse customer data sources and destinations.",
            "Partnered with Sales and Product teams to deliver technical demonstrations, scope engineering requirements, and translate enterprise pain points into actionable platform features.",
        ],
    },
    {
        "company": "Schoolzilla",
        "location": "Oakland, CA",
        "role": "Data Systems Engineer",
        "period": "2013 – 2016",
        "badge": None,
        "context": "Enterprise data warehouse platform providing analytics and visualization solutions for K-12 education.",
        "bullets": [
            "Formulated and implemented audit strategies to guarantee enterprise-grade data quality and consistency.",
            "Provided architectural guidance on data storage solutions and schema optimizations for high-volume records.",
            "Developed software solutions in R, SQL, and Python to ingest, clean, validate, and visualize incoming multidimensional data.",
            "Managed technical working relationships with in-house developers and external vendors.",
        ],
    },
    {
        "company": "KIPP Foundation",
        "location": "San Francisco, CA",
        "role": "Data Systems Analyst & Collection Specialist",
        "period": "2011 – 2016",
        "badge": None,
        "context": "National charter school network providing college-preparatory education to underserved communities.",
        "bullets": [
            "Designed and executed automated audit routines and ETL pipelines to validate, store, and report on educational data across a nationwide network of schools.",
            "Engineered complex SQL queries and ETL processes for executive analytics and operational reporting.",
            "Managed and improved web-input collection systems to maximize data accuracy and intake efficiency.",
            "Constructed validated data models and exhibits that directly supported multi-million-dollar grant applications.",
        ],
    },
    {
        "company": "Net Impact",
        "location": "San Francisco, CA",
        "role": "Program Intern / Data Analyst",
        "period": "2010 – 2011",
        "badge": None,
        "context": "Global professional network focused on corporate social responsibility.",
        "bullets": [
            "Manipulated, cross-referenced, and audited datasets across multiple relational database platforms.",
            "Calculated chapter distributions and metrics in Excel using pivot tables and advanced formulas.",
            "Supported technical operations and managed regular communications reaching 3,000+ member organizations.",
        ],
    },
]

EDUCATION = {
    "institution": "University of Michigan",
    "location": "Ann Arbor, MI",
    "degree": "Bachelor of Arts in Political Science and History",
    "period": "Graduated April 2010",
    "coursework": [
        "Statistics",
        "Economics",
        "Political Modeling (Complex Systems)",
        "Game Theory",
    ],
}

MISC = {
    "languages": ["English (Native)", "Japanese (Conversational)", "French (Conversational)"],
    "interests": ["3D Printing", "Crafting", "Open Source Tooling", "Video Games", "Dogs"],
}
