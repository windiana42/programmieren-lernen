#!/usr/bin/env python3
"""Convert all Markdown files to HTML in docs/html/, with correct inter-linking."""

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent
DOCS = ROOT / "docs"
HTML_DIR = DOCS / "html"
IMAGES_SRC = DOCS / "images"
IMAGES_DST = HTML_DIR / "images"

PANDOC_ARGS = [
    "pandoc",
    "--standalone",
    "--metadata", "lang=de",
    "--css", "style.css",
    "-f", "markdown",
    "-t", "html5",
]

MD_LINK = re.compile(r'\[([^\]]+)\]\(([^)]+\.md)\)')

CSS = """\
body {
  max-width: 800px;
  margin: 2rem auto;
  padding: 0 1rem;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  line-height: 1.6;
  color: #1a1a1a;
}
h1, h2, h3 { margin-top: 2rem; }
h1 { border-bottom: 2px solid #eee; padding-bottom: 0.3rem; }
hr { border: none; border-top: 1px solid #ddd; margin: 2rem 0; }
a { color: #0366d6; text-decoration: none; }
a:hover { text-decoration: underline; }
img { max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; margin: 0.5rem 0; }
code { background: #f6f8fa; padding: 0.15em 0.4em; border-radius: 3px; font-size: 0.9em; }
pre { background: #f6f8fa; padding: 1rem; border-radius: 6px; overflow-x: auto; }
pre code { background: none; padding: 0; }
ul, ol { padding-left: 1.5rem; }
"""


def rewrite_links(md_text: str, source_file: Path) -> str:
    """Rewrite .md links to .html, adjusting paths for flat output in docs/html/."""
    def replace(m):
        text, href = m.group(1), m.group(2)
        name = Path(href).stem + ".html"
        if source_file == ROOT / "README.md":
            # README links like docs/Foo.md -> Foo.html
            name = Path(href).stem + ".html"
        return f"[{text}]({name})"
    return MD_LINK.sub(replace, md_text)


def rewrite_image_paths(md_text: str, source_file: Path) -> str:
    """Rewrite image paths so they point to images/ relative to docs/html/."""
    if source_file.parent == DOCS:
        # docs/*.md references images/foo.png — stays the same
        return md_text
    # README.md references docs/images/... — strip docs/ prefix
    return md_text.replace("docs/images/", "images/")


def convert(source: Path, output_name: str):
    md_text = source.read_text(encoding="utf-8")
    md_text = rewrite_links(md_text, source)
    md_text = rewrite_image_paths(md_text, source)

    title = output_name.replace("_", " ").removesuffix(".html")
    out = HTML_DIR / output_name

    result = subprocess.run(
        PANDOC_ARGS + ["--metadata", f"title={title}", "-o", str(out)],
        input=md_text, text=True, capture_output=True,
    )
    if result.returncode != 0:
        print(f"ERROR converting {source}: {result.stderr}")
    else:
        print(f"  {source} -> {out}")


def main():
    HTML_DIR.mkdir(parents=True, exist_ok=True)

    # Copy images
    if IMAGES_SRC.exists():
        if IMAGES_DST.exists():
            shutil.rmtree(IMAGES_DST)
        shutil.copytree(IMAGES_SRC, IMAGES_DST)
        print(f"  Copied images -> {IMAGES_DST}")

    # Write CSS
    (HTML_DIR / "style.css").write_text(CSS, encoding="utf-8")
    print("  Wrote style.css")

    # Convert README
    convert(ROOT / "README.md", "index.html")

    # Convert all docs/*.md
    for md in sorted(DOCS.glob("*.md")):
        convert(md, md.stem + ".html")

    print("\nDone.")


if __name__ == "__main__":
    main()
