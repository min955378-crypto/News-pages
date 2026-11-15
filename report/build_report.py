#!/usr/bin/env python3
"""Build the Breaking-News Top-35 Formats research report (styled HTML + PDF).

Design rule: NO green (incl. light green) anywhere — palette is navy/red/white/black/grey/gold.
"""
import pathlib
import re

from markdown import markdown

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

PARTS = [
    "part-1-cover-methodology.md",
    "part-2-landscape.md",
    "part-3-design-system.md",
    "part-4a-formats-F01-F12.md",
    "part-4b-formats-F13-F24.md",
    "part-4c-formats-F29-F35.md",
    "part-5-headlines.md",
    "part-6-implementation.md",
    "part-7-appendices.md",
]

TITLE = "Breaking News on Facebook & Instagram — Top 35 Post Formats"

md_text = "\n\n".join((ROOT / p).read_text(encoding="utf-8") for p in PARTS)
body_html = markdown(md_text, extensions=["tables", "sane_lists"])

# First h1 should not force a page break.
body_html = body_html.replace("<h1>", '<h1 class="first-h1">', 1)

# ---- fonts: copy DejaVu into the workspace (xhtml2pdf cannot read outside it) ----
import shutil  # noqa: E402

FONTS = ROOT / "fonts"
FONTS.mkdir(exist_ok=True)
SYSTEM_FONT_DIR = pathlib.Path("/usr/share/fonts/truetype/dejavu")
for fn in ["DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSansMono.ttf", "DejaVuSansMono-Bold.ttf"]:
    dst = FONTS / fn
    if not dst.exists() and (SYSTEM_FONT_DIR / fn).exists():
        shutil.copy(SYSTEM_FONT_DIR / fn, dst)

FONT_FACE = ""
if (FONTS / "DejaVuSans.ttf").exists():
    FONT_FACE = f"""
@font-face {{ font-family: dejavu; src: url('{FONTS / "DejaVuSans.ttf"}'); }}
@font-face {{ font-family: dejavu; src: url('{FONTS / "DejaVuSans-Bold.ttf"}'); font-weight: bold; }}
@font-face {{ font-family: dejavumono; src: url('{FONTS / "DejaVuSansMono.ttf"}'); }}
@font-face {{ font-family: dejavumono; src: url('{FONTS / "DejaVuSansMono-Bold.ttf"}'); font-weight: bold; }}
"""
    SANS = "dejavu, Helvetica, Arial, sans-serif"
    MONO = "dejavumono, monospace"
else:
    SANS = "Helvetica, Arial, sans-serif"
    MONO = "monospace"

CSS = FONT_FACE + """
@page {
    size: A4;
    margin: 1.9cm 1.7cm 2.1cm 1.7cm;
    @bottom-center {
        content: "Page " counter(page);
        font-family: dejavu, Helvetica, sans-serif;
        font-size: 8pt;
        color: #666666;
    }
}
body {
    font-family: dejavu, Helvetica, Arial, sans-serif;
    font-size: 9.6pt;
    line-height: 1.45;
    color: #111111;
}
h1 {
    background-color: #0B1F3A;
    color: #FFFFFF;
    font-size: 16pt;
    padding: 10px 14px;
    margin: 0 0 14px 0;
    page-break-before: always;
    page-break-inside: avoid;
}
h1.first-h1 { page-break-before: avoid; font-size: 20pt; }
h2 {
    color: #0B1F3A;
    font-size: 12.5pt;
    border-bottom: 2px solid #C9A227;
    padding-bottom: 3px;
    margin: 18px 0 8px 0;
    page-break-after: avoid;
}
h3 {
    color: #C8102E;
    font-size: 10.8pt;
    margin: 14px 0 5px 0;
    page-break-after: avoid;
}
h4 { color: #0B1F3A; font-size: 10pt; margin: 10px 0 4px 0; }
p { margin: 5px 0; }
strong { color: #0B1F3A; }
hr { border: none; border-top: 1px solid #C9A227; margin: 12px 0; }
table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0 12px 0;
    font-size: 8.2pt;
    page-break-inside: avoid;
}
th {
    background-color: #0B1F3A;
    color: #FFFFFF;
    text-align: left;
    padding: 5px 6px;
    border: 1px solid #0B1F3A;
}
td {
    padding: 4px 6px;
    border: 1px solid #C9CDD4;
    vertical-align: top;
}
tr:nth-child(even) td { background-color: #F2F2F2; }
code, pre {
    font-family: dejavumono, monospace;
    font-size: 7.8pt;
}
code { background-color: #F2F2F2; padding: 1px 3px; }
pre {
    background-color: #F2F2F2;
    border-left: 4px solid #C8102E;
    padding: 8px 10px;
    margin: 8px 0;
    page-break-inside: avoid;
}
pre code { background-color: transparent; padding: 0; }
blockquote {
    border-left: 4px solid #C8102E;
    margin: 8px 0 8px 2px;
    padding: 2px 12px;
    color: #333333;
    background-color: #F2F2F2;
}
ul, ol { margin: 5px 0 8px 18px; padding-left: 8px; }
li { margin: 2px 0; }
a { color: #0B1F3A; text-decoration: none; }
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>{TITLE}</title>
<style>{CSS}</style>
</head>
<body>
{body_html}
</body>
</html>"""

out_html = OUT / "Breaking-News-Top-35-Formats-Research-Report.html"
out_html.write_text(html, encoding="utf-8")
print(f"HTML written: {out_html} ({out_html.stat().st_size:,} bytes)")

# ---- PDF via xhtml2pdf ----
from xhtml2pdf import pisa  # noqa: E402

out_pdf = OUT / "Breaking-News-Top-35-Formats-Research-Report.pdf"
with open(out_pdf, "wb") as fh:
    status = pisa.CreatePDF(src=html, dest=fh, encoding="utf-8")

print(f"PDF written: {out_pdf} ({out_pdf.stat().st_size:,} bytes), err={status.err}")
