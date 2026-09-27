#!/usr/bin/env python3
"""Render LaTeX resume from resume_data.py and compile to PDF using pdflatex."""

import os
import re
import shutil
import subprocess
from pathlib import Path
import jinja2

import resume_data

BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
TEX_TEMPLATE_FILE = TEMPLATES_DIR / "resume.tex.j2"
TEX_OUTPUT_FILE = STATIC_DIR / "resume.tex"
PDF_TARGET_FILE = STATIC_DIR / "Mike_Hilton_Resume.pdf"


def tex_escape(text: str) -> str:
    """Escape LaTeX special characters in string values."""
    if not isinstance(text, str):
        text = str(text)
    
    conv = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "•": r"$\bullet$",
        "–": r"--",
        "—": r"---",
    }
    regex = re.compile("|".join(re.escape(k) for k in conv.keys()))
    return regex.sub(lambda m: conv[m.group(0)], text)


def get_pdflatex_path() -> str | None:
    """Find pdflatex binary in PATH or standard TeX locations."""
    # Check standard PATH
    path = shutil.which("pdflatex")
    if path:
        return path
    
    # Check macOS TeXLive / BasicTeX paths
    mac_paths = [
        "/Library/TeX/texbin/pdflatex",
        "/usr/local/texlive/2026/bin/universal-darwin/pdflatex",
        "/usr/local/texlive/2025/bin/universal-darwin/pdflatex",
        "/usr/local/texlive/2024/bin/universal-darwin/pdflatex",
    ]
    for p in mac_paths:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    return None


def render_latex_source() -> Path:
    """Render resume_data.py into static/resume.tex using Jinja2."""
    latex_jinja_env = jinja2.Environment(
        block_start_string=r"\BLOCK{",
        block_end_string=r"}",
        variable_start_string=r"\VAR{",
        variable_end_string=r"}",
        comment_start_string=r"\#{",
        comment_end_string=r"}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(str(TEMPLATES_DIR)),
    )
    latex_jinja_env.filters["tex_escape"] = tex_escape

    template = latex_jinja_env.get_template("resume.tex.j2")
    rendered_tex = template.render(
        profile=resume_data.PROFILE,
        summary=resume_data.SUMMARY,
        skill_groups=resume_data.SKILL_GROUPS,
        experience=resume_data.EXPERIENCE,
        education=resume_data.EDUCATION,
        misc=resume_data.MISC,
    )

    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    with open(TEX_OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(rendered_tex)

    return TEX_OUTPUT_FILE


def generate_resume_pdf() -> bool:
    """Render LaTeX and compile to static/Mike_Hilton_Resume.pdf."""
    tex_path = render_latex_source()
    print(f"Generated LaTeX source at: {tex_path}")

    pdflatex_bin = get_pdflatex_path()
    if not pdflatex_bin:
        print("[Notice] pdflatex not found in PATH or standard macOS TeX directories.")
        print("         The LaTeX source was generated at static/resume.tex.")
        print("         To compile locally, run: brew install --cask basictex")
        print("         In GitHub Actions, the PDF will compile automatically on deploy.")
        return False

    print(f"Compiling LaTeX to PDF using {pdflatex_bin}...")
    try:
        # Run pdflatex into static/
        result = subprocess.run(
            [
                pdflatex_bin,
                "-interaction=nonstopmode",
                f"-output-directory={STATIC_DIR}",
                f"-jobname=Mike_Hilton_Resume",
                str(tex_path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        # Cleanup auxiliary LaTeX build files (.aux, .log, .out)
        for ext in [".aux", ".log", ".out"]:
            aux_file = STATIC_DIR / f"Mike_Hilton_Resume{ext}"
            if aux_file.exists():
                aux_file.unlink()

        print(f"[Success] Successfully compiled: {PDF_TARGET_FILE}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Error] pdflatex compilation failed:\n{e.stdout}\n{e.stderr}")
        return False


if __name__ == "__main__":
    generate_resume_pdf()
