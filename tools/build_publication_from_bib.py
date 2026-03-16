#!/usr/bin/env python3
from pathlib import Path
import re
import datetime

# ---- SETTINGS ----
BIB_PATH = Path("static/pubs.bib")            # where your BibTeX lives
OUT_PATH = Path("content/publications/_index.md")
YOUR_NAME_REGEX = re.compile(r"\bJericho\b\s+\bCain\b", re.I)  # bold your name
# ------------------

def load_bibtex(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def split_entries(bib_text: str):
    # Very lightweight BibTeX splitter (avoids extra deps). Works for typical .bib.
    # If you have very complex entries, we can switch to bibtexparser later.
    entries = []
    buf, depth = [], 0
    for line in bib_text.splitlines():
        if line.strip().startswith("@") and depth == 0:
            if buf:
                entries.append("\n".join(buf).strip())
                buf = []
        buf.append(line)
        depth += line.count("{") - line.count("}")
    if buf:
        entries.append("\n".join(buf).strip())
    return [e for e in entries if e.startswith("@")]

def parse_fields(entry: str) -> dict:
    # crude field extractor; good enough for typical CSL/BibTeX exports
    mtype = entry[1:entry.find("{")].strip().lower()  # article, inproceedings, etc.
    fields = {"_type": mtype}
    # remove first line "@type{key,"
    body = entry[entry.find("{")+1:]
    body = body[body.find(",")+1:]  # drop key prefix
    # collect key-value pairs until final "}"
    for line in body.splitlines():
        if line.strip().startswith("}"):
            break
        if "=" in line:
            k, v = line.split("=", 1)
            k = k.strip().lower()
            v = v.strip().rstrip(",")
            # strip braces/quotes
            if v.startswith("{") and v.endswith("}"):
                v = v[1:-1]
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            fields[k] = v.strip()
    return fields

def clean_tex(s: str) -> str:
    if not s:
        return ""
    # decode common LaTeX escapes minimally
    s = s.replace(r"\&", "&")
    s = s.replace(r"---", "—").replace(r"--", "–")
    s = re.sub(r"\{\\\'\s*([A-Za-z])\}", r"´\1", s)  # very rough acute handling
    s = re.sub(r"[{}]", "", s)
    return s

def fmt_authors(s: str) -> str:
    # Authors usually "Last, First and Last, First ..."
    parts = [p.strip() for p in re.split(r"\s+and\s+", s)]
    def flip(name):
        if "," in name:
            last, first = [t.strip() for t in name.split(",", 1)]
            disp = f"{first} {last}".strip()
        else:
            disp = name.strip()
        # bold your name
        if YOUR_NAME_REGEX.search(disp):
            disp = f"**{disp}**"
        return disp
    return ", ".join(flip(p) for p in parts if p)

def link_from(fields: dict) -> str:
    doi = clean_tex(fields.get("doi"))
    eprint = clean_tex(fields.get("eprint"))
    url = clean_tex(fields.get("url"))
    if doi:
        return f"https://doi.org/{doi}"
    if fields.get("archiveprefix", "").lower() == "arxiv" and eprint:
        return f"https://arxiv.org/abs/{eprint}"
    if url:
        return url
    return ""

def get_year(fields: dict) -> int:
    y = fields.get("year")
    try:
        return int(re.findall(r"\d{4}", y or "")[0])
    except Exception:
        return 0

def title_md(fields: dict) -> str:
    t = clean_tex(fields.get("title", "")).strip()
    url = link_from(fields)
    return f"[{t}]({url})" if url else t

def html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
         .replace("<", "&lt;")
         .replace(">", "&gt;")
         .replace('"', "&quot;")
    )

def title_html(fields: dict) -> str:
    t = html_escape(clean_tex(fields.get("title", "")).strip())
    url = link_from(fields)
    if url:
        return f'<a href="{html_escape(url)}">{t}</a>'
    return t

def simple_md_to_html(s: str) -> str:
    s = html_escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def venue_string(f: dict) -> str:
    t = f.get("_type", "")
    if t == "article":
        j = clean_tex(f.get("journal"))
        vol = clean_tex(f.get("volume"))
        num = clean_tex(f.get("number"))
        pages = clean_tex(f.get("pages"))
        bits = [b for b in [j, vol and f"**{vol}**", num and f"({num})", pages] if b]
        return ", ".join(bits)
    elif t in ("inproceedings", "conference", "proceedings"):
        book = clean_tex(f.get("booktitle"))
        pages = clean_tex(f.get("pages"))
        return ", ".join([b for b in [book, pages] if b])
    elif t in ("techreport", "report"):
        inst = clean_tex(f.get("institution"))
        num = clean_tex(f.get("number"))
        return ", ".join([b for b in [inst, num] if b])
    else:
        # fallback: try journal/booktitle/venue-like fields
        for k in ("journal","booktitle","howpublished","publisher","institution","note"):
            if f.get(k):
                return clean_tex(f.get(k))
        return ""

def render_entry(fields: dict) -> str:
    authors = simple_md_to_html(fmt_authors(clean_tex(fields.get("author",""))))
    title = title_html(fields)
    venue = simple_md_to_html(venue_string(fields)) if venue_string(fields) else ""
    ydisp = year_display(fields)     # <-- use display string
    tail = []
    doi = clean_tex(fields.get("doi"))
    if doi:
        tail.append(f'<a href="{html_escape(f"https://doi.org/{doi}")}">DOI</a>')
    elif fields.get("archiveprefix","").lower() == "arxiv" and fields.get("eprint"):
        tail.append(f'<a href="{html_escape(f"https://arxiv.org/abs/{clean_tex(fields["eprint"])}")}">arXiv</a>')
    elif fields.get("url"):
        tail.append(f'<a href="{html_escape(clean_tex(fields["url"]))}">Link</a>')
    links = " · ".join(tail)

    lines = ['<article class="pub-card">']
    lines.append(f'  <h3>{title}</h3>')
    lines.append(f'  <p class="pub-authors">{authors}</p>')

    meta_bits = []
    if venue:
        meta_bits.append(f"<span>{venue}</span>")
    meta_bits.append(f'<span class="pub-year">{ydisp}</span>')
    meta_html = '<span class="pub-sep">•</span>'.join(meta_bits)
    lines.append(f'  <p class="pub-meta">{meta_html}</p>')

    if links:
        lines.append(f'  <p class="pub-links">{links}</p>')

    lines.append("</article>")
    return "\n".join(lines)


def group_by_year(parsed):
    by = {}
    for f in parsed:
        y = get_year(f)
        by.setdefault(y, []).append(f)
    return dict(sorted(by.items(), key=lambda kv: kv[0], reverse=True))

import re

def year_display(fields: dict) -> str:
    y = (fields.get("year") or "").strip()
    if not y:
        return "n.d."
    # handle BibTeX ranges: "2008 --2011", "2008--2011", "2008–2011"
    m = re.search(r'(\d{4})\s*[-–—]{1,2}\s*(\d{4})', y)
    if m:
        return f"{m.group(1)}–{m.group(2)}"  # en dash
    m = re.search(r'(\d{4})', y)
    if m:
        return m.group(1)
    return "n.d."

def clean_tex(s: str) -> str:
    if not s:
        return ""
    s = s.replace(r"\&", "&")
    s = s.replace(r"---", "—").replace(r"--", "–")
    # strip \url{...} and \url https://... wrappers
    s = re.sub(r"\\url\{([^}]+)\}", r"\1", s)
    s = re.sub(r"\\url\s*([^\s]+)", r"\1", s)
    s = re.sub(r"[{}]", "", s)
    return s




def main():
    bib = load_bibtex(BIB_PATH)
    entries = split_entries(bib)
    parsed = [parse_fields(e) for e in entries]
    # sort inside each year by title (or add custom ordering)
    for f in parsed:
        f["_title_sort"] = clean_tex(f.get("title","")).lower()
    grouped = group_by_year(parsed)

    dated_years = [get_year(f) for f in parsed if get_year(f)]
    pub_count = len(parsed)
    start_year = min(dated_years) if dated_years else None
    end_year = max(dated_years) if dated_years else None

    lines = []
    lines.append('+++\ntitle = "Publications"\ndraft = false\n+++\n')
    lines.append('<div class="publications">\n')
    lines.append('<section class="pub-hero">')
    lines.append('  <div>')
    lines.append('    <p class="pub-kicker">Research output</p>')
    lines.append('    <p class="pub-lede">A chronological record of journal articles, conference papers, preprints, and related work.</p>')
    lines.append('    <p class="pub-note">This list is generated from <code>static/pubs.bib</code>.</p>')
    lines.append('  </div>')
    lines.append('  <div class="pub-summary">')
    lines.append(f'    <div class="pub-stat"><strong>{pub_count}</strong><span>publications</span></div>')
    if start_year and end_year:
        lines.append(f'    <div class="pub-stat"><strong>{start_year}-{end_year}</strong><span>coverage</span></div>')
    lines.append('  </div>')
    lines.append('</section>\n')

    for year, items in grouped.items():
        if year == 0 and not items:
            continue
        items.sort(key=lambda f: f.get("_title_sort",""))
        ydisp = year if year else "No date"
        lines.append(f'<section class="pub-year-block">')
        lines.append(f'  <div class="pub-year-heading">{ydisp}</div>')
        lines.append('  <div class="pub-year-list">')
        for it in items:
            lines.append(render_entry(it))
        lines.append('  </div>')
        lines.append('</section>\n')

    lines.append('<div class="publications-footer">')
    lines.append('  <a href="/research/">← Back to Research</a>')
    lines.append('</div>')
    lines.append('</div>')

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} with {sum(len(v) for v in grouped.values())} entries.")

if __name__ == "__main__":
    main()
