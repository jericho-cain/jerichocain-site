#!/usr/bin/env python3
from pathlib import Path
import re
import datetime

# ---- SETTINGS ----
BIB_PATH = Path("static/pubs.bib")            # where your BibTeX lives
OUT_PATH = Path("content/research/publications/_index.md")
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
    authors = fmt_authors(clean_tex(fields.get("author","")))
    title = title_md(fields)
    venue = venue_string(fields)
    year = get_year(fields) or "n.d."
    tail = []
    doi = clean_tex(fields.get("doi"))
    if doi:
        tail.append(f"[DOI](https://doi.org/{doi})")
    elif fields.get("archiveprefix","").lower() == "arxiv" and fields.get("eprint"):
        tail.append(f"[arXiv](https://arxiv.org/abs/{clean_tex(fields['eprint'])})")
    elif fields.get("url"):
        tail.append(f"[Link]({clean_tex(fields['url'])})")
    tail_str = f" · {' · '.join(tail)}" if tail else ""
    line = f"- {authors}. **{title}**"
    if venue:
        line += f". *{venue}*"
    line += f", {year}{tail_str}"
    return line

def group_by_year(parsed):
    by = {}
    for f in parsed:
        y = get_year(f)
        by.setdefault(y, []).append(f)
    return dict(sorted(by.items(), key=lambda kv: kv[0], reverse=True))

def main():
    bib = load_bibtex(BIB_PATH)
    entries = split_entries(bib)
    parsed = [parse_fields(e) for e in entries]
    # sort inside each year by title (or add custom ordering)
    for f in parsed:
        f["_title_sort"] = clean_tex(f.get("title","")).lower()
    grouped = group_by_year(parsed)

    lines = []
    lines.append('+++\ntitle = "Publications"\ndraft = false\n+++\n')
    lines.append("_This list is generated from `data/pubs.bib`._\n")

    for year, items in grouped.items():
        if year == 0 and not items:
            continue
        items.sort(key=lambda f: f.get("_title_sort",""))
        ydisp = year if year else "No date"
        lines.append(f"\n## {ydisp}\n")
        for it in items:
            lines.append(render_entry(it))

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_PATH} with {sum(len(v) for v in grouped.values())} entries.")

if __name__ == "__main__":
    main()
