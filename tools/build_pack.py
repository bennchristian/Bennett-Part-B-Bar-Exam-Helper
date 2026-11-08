"""Build study/<paper-id>/reference-pack.pdf from coverage.md and the Paper's content files.

Usage: python3 tools/build_pack.py <paper-id> [--questions | --check]

With --check it runs every coverage/format check and prints the coverage report, but renders
nothing and writes no PDF (the default until Bennett approves PDFs — CLAUDE.md, 9 Nov 2026).

With --questions it instead builds study/<paper-id>/model-questions.pdf from model-questions.md:
questions by Subject and Topic, each with a Keywords line (Topic, Sub-point from coverage.md, and
the Keywords of the end-point blocks it names) and its answer boxed directly below, plus a
contents page linking every Topic with its page.

The one Reference Pack builder (ARCHITECTURE.md AD-6). It reads coverage.md plus whichever
of prewrites.md, templates.md and cheatsheets.md exist, checks them against AD-2/AD-4/AD-5,
prints the pack with headless Chrome in two passes (pypdf reads each block's page from the PDF's named
destinations), and prints the coverage report.

Exit 0: built. Exit 1: build failed, the old PDF is kept. Exit 2: bad paper ID or a
missing tool. Writes only study/<paper-id>/ and the system temp directory.
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent.parent
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CONTENT_FILES = ("prewrites.md", "templates.md", "cheatsheets.md")

# SCHEMA.md "Paper IDs": name (the running header), exam day, Subjects in index order.
PAPERS = {
    "drp-w": ("DRP written", "Tue 1 Dec 2026", ["Civil Litigation", "Written Advocacy"]),
    "drp-m": ("DRP MCQ", "Wed 2 Dec 2026", ["Arbitration", "Mediation Advocacy"]),
    "eth-w": ("ETH written", "Thu 3 Dec 2026", ["Ethics & Professional Responsibility"]),
    "pcp-w": ("PCP written", "Mon 7 Dec 2026", ["Criminal Litigation", "Family Law Practice"]),
    "pcp-m": ("PCP MCQ", "Tue 8 Dec 2026", ["Probate", "Real Estate (Conveyancing)",
                                            "Muslim Family & Succession", "Employment", "PIPD"]),
    "ccp-1": ("CCP MCQ 1", "Wed 9 Dec 2026", ["Banking & Fundraising", "Corporate Governance",
                                              "Insolvency", "Admiralty"]),
    "ccp-2": ("CCP MCQ 2", "Thu 10 Dec 2026", ["IP", "M&A", "Competition", "Taxation"]),
    "clk-m": ("CLK MCQ", "Fri 11 Dec 2026", ["Data Protection & Cyber", "Law & Tech",
                                            "Comparative Laws", "Conflict of Laws"]),
}

KEY = re.compile(r"(?:(\d+)\.)?([IVXLC]+)\.(\d+)")
ANY_ID = re.compile(r"\b(?:drp|eth|pcp|ccp|clk)-[wm12]-\d+-\d+\b")
QB_ID = re.compile(r"\bQB-\d+\b")
CASE = re.compile(r"(?<![\w*])\*([^*\n]+? v [^*\n]+?|Re [^*\n]+?)\*(?![\w*])")
STATES = ("ID", "item 4", "TODO", "none", "other")

ERRORS, WARNINGS = [], []


# ---- Markdown -> HTML (just what the study files use) ---------------------------------------

def inline(t):
    t = html.escape(t, quote=False)  # quotes stay straight and exactly as typed (AD-6 step 6)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])", r"<i>\1</i>", t)
    return re.sub(r"\[([^\]]+)\]\(#([\w-]+)\)", r"<a class='xref' href='#\2'>\1</a>", t)  # page no. added in build_html


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def md(text, where):
    out, para, lst = [], [], None
    lines = text.split("\n")

    def flush():
        nonlocal para, lst
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []
        if lst:
            out.append(f"<{lst}>" + "".join(lst_items) + f"</{lst}>")
            lst = None

    lst_items, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            flush()
            lang = (ln[3:].split() or [""])[0]
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            src = "\n".join(lines[i + 1:j])
            if lang == "mermaid":  # AD-5: no diagrams; a Topic's framework is its Cheatsheet
                ERRORS.append(f"{where}: has a mermaid diagram; write it as a Cheatsheet list instead (AD-5)")
            out.append(f"<pre>{html.escape(src)}</pre>")
            i = j + 1
            continue
        if ln.startswith(">"):  # a run of '>' lines is a rule box; its inside is Markdown too
            flush()
            j = i
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            inner = [re.sub(r"^> ?", "", t) for t in lines[i:j]]
            out.append(f"<div class='box'>{md(chr(10).join(inner), where)}</div>")
            i = j
            continue
        h = re.match(r"(#{1,6}) +(.*)", ln)
        if h:
            flush()
            n = min(max(len(h.group(1)), 2), 4)
            out.append(f"<h{n}>{inline(h.group(2))}</h{n}>")
        elif ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.fullmatch(r"[\s|:-]+", lines[i]):
                    rows.append(cells(lines[i]))
                i += 1
            out.append("<table>" + "".join(
                "<tr>" + "".join(f"<{t}>{inline(c)}</{t}>" for c in row) + "</tr>"
                for r, row in enumerate(rows) for t in ["th" if r == 0 else "td"]) + "</table>")
            continue
        elif re.fullmatch(r"\s*(-{3,}|\*{3,})\s*", ln) or not ln.strip():
            flush()
        elif m := re.match(r"(\s*)([-*+]|\d+\.) (.*)", ln):
            if para:
                out.append("<p>" + inline(" ".join(para)) + "</p>")
                para = []
            kind = "ol" if m.group(2)[0].isdigit() else "ul"
            if lst != kind:
                flush()
                lst, lst_items = kind, []
            item = m.group(3)
            while i + 1 < len(lines) and lines[i + 1].startswith("  ") and lines[i + 1].strip() \
                    and not re.match(r"\s*([-*+]|\d+\.) ", lines[i + 1]):
                i += 1
                item += " " + lines[i].strip()
            lst_items.append(f"<li class='d{len(m.group(1)) // 2}'>{inline(item)}</li>")
        else:
            if lst:
                flush()
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)


# ---- Parsing ------------------------------------------------------------------------------

def parse_coverage(text, paper, nsubj):
    """Return the Sub-point rows of coverage.md, in file order."""
    rows, keys, topic, in_table = [], set(), None, False
    for n, line in enumerate(text.splitlines(), 1):
        where = f"coverage.md:{n}"
        h = re.match(r"#{2,6} +(.*)", line)
        if h:
            topic, in_table = h.group(1).strip(), False
            if nsubj > 1 and re.match(r"\d+(?![\d.])", topic):
                topic = None  # a Subject heading; the Key prefix names the Subject
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        if re.fullmatch(r"[\s|:-]+", line):
            continue
        c = cells(line)
        if c[0] in ("Key", "#"):
            in_table = True
            continue
        m = KEY.fullmatch(c[0])
        if not m:
            if in_table:
                ERRORS.append(f"{where}: Key '{c[0]}' is not <Topic roman>.<n>"
                              + (" with a <subject#>. prefix" if nsubj > 1 else ""))
            continue
        if len(c) != 4:
            ERRORS.append(f"{where}: row {c[0]} has {len(c)} columns; AD-2 needs Key | Sub-point | Tested | Covered by")
            continue
        if nsubj > 1 and m.group(1) is None:
            ERRORS.append(f"{where}: Key {c[0]} needs its <subject#>. prefix on a multi-Subject Paper (<subject#>.{c[0]}, e.g. 0.{c[0]})")
            continue
        subj = int(m.group(1) or 0)
        if subj >= nsubj:
            ERRORS.append(f"{where}: Key {c[0]} names Subject {subj}; {paper} has Subjects 0–{nsubj - 1}")
            continue
        if c[0] in keys:
            ERRORS.append(f"{where}: Key {c[0]} is duplicated")
        keys.add(c[0])
        covered = c[3]
        ids = ANY_ID.findall(covered)
        for i in ids:
            if not i.startswith(paper + "-"):
                ERRORS.append(f"{where}: Covered by names {i}, which is not a {paper} ID")
        low = covered.lower()
        state = ("ID" if ids else "item 4" if low.startswith("item 4") else "TODO" if covered.startswith("TODO")
                 else "none" if low.startswith("none") else "other")
        if state == "other":
            WARNINGS.append(f"{where}: Covered by '{covered}' for {c[0]} is not an ID, item 4, TODO or none: <reason>")
        rows.append(dict(key=c[0], subj=subj, topic=topic, sub=c[1], tested=c[2], covered=covered,
                         ids=ids, state=state, qb=bool(QB_ID.search(c[2])), line=n))
    return rows


def split_sections(fname, text):
    """Return (preamble, [section]) where a section holds its intro lines and raw blocks."""
    lines = text.split("\n")
    preamble, sections, fence = [], [], False
    for n, line in enumerate(lines, 1):
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith("## "):
            sections.append(dict(title=line[3:].strip(), intro=[], blocks=[], line=n))
        elif not fence and line.startswith("### "):
            if not sections:
                ERRORS.append(f"{fname}:{n}: block before the first '## ' heading")
                continue
            sections[-1]["blocks"].append(dict(head=line.rstrip(), lines=[], line=n))
        elif not sections:
            preamble.append(line)
        elif sections[-1]["blocks"]:
            sections[-1]["blocks"][-1]["lines"].append(line)
        else:
            sections[-1]["intro"].append(line)
    if fence:
        ERRORS.append(f"{fname}: a ``` fence is never closed")
    return "\n".join(preamble), sections


def parse_block(fname, raw, paper, nsubj):
    """Parse one AD-4 block, or record why it can't be parsed and return None."""
    where = f"{fname}:{raw['line']}"
    m = re.fullmatch(r"### (\S+) — (.+)", raw["head"])
    idm = m and re.fullmatch(rf"{re.escape(paper)}-(\d+)-(\d+)", m.group(1))
    if not idm:
        ERRORS.append(f"{where}: heading must be '### {paper}-<subject#>-<n> — <title>', got '{raw['head']}'")
        return None
    bid, title = m.groups()
    subj = int(idm.group(1))
    if subj >= nsubj:
        ERRORS.append(f"{where}: {bid} names Subject {subj}; {paper} has Subjects 0–{nsubj - 1}")
        return None
    lines = raw["lines"]
    kw = re.fullmatch(r"\*Keywords: (.+)\*", lines[0].strip()) if lines else None
    if not kw:
        ERRORS.append(f"{where}: {bid} needs '*Keywords: a, b, c*' on the line after its heading")
        return None
    rest = "\n".join(lines[1:])
    notes = list(re.finditer(r"^\*Source note: ?", rest, re.M))
    if not notes:
        ERRORS.append(f"{where}: {bid} has no '*Source note: …*' paragraph")
        return None
    body = rest[:notes[-1].start()].strip()
    tail = rest[notes[-1].end():].split("\n")
    end = next((k for k, t in enumerate(tail) if t.rstrip().endswith("*")), None)
    if end is None:
        ERRORS.append(f"{where}: {bid}'s Source note is not closed with '*'")
        return None
    note = " ".join(t.strip() for t in tail[:end + 1])[:-1].strip()
    trailing = "\n".join(t for t in tail[end + 1:] if not re.fullmatch(r"\s*(-{3,})?\s*", t))
    if not body:
        ERRORS.append(f"{where}: {bid} has no body between Keywords and Source note")
        return None
    if fname == "cheatsheets.md" and not body.startswith("**End point:**"):
        ERRORS.append(f"{where}: {bid}'s body must start with '**End point:**' (AD-4)")
        return None
    text = "\n".join([raw["head"]] + lines)
    return dict(id=bid, subj=subj, short=f"{subj}-{idm.group(2)}", title=title, kw_raw=kw.group(1),
                kws=[k.strip() for k in kw.group(1).split(",") if k.strip()], body=body, note=note,
                trailing=trailing, file=fname, line=raw["line"],
                verify=sum("TODO: verify" in t for t in text.splitlines()),
                cases=sorted(set(CASE.findall(" ".join(body.split())))))


def lint_cheatsheet(fname, sec):
    """AD-5: every Topic in cheatsheets.md / prewrites.md opens with a cue list (warns, not fails)."""
    cheatsheet = any(re.match(r"\s*[-*+] ", ln) for ln in sec["intro"])
    if fname in ("cheatsheets.md", "prewrites.md") and not cheatsheet:
        WARNINGS.append(f"{fname}:{sec['line']}: Topic '{sec['title']}' has no Cheatsheet directly under it "
                        "(fine only if its coverage rows say none: <reason>)")


# ---- Rendering ----------------------------------------------------------------------------

def chrome(tmp, *args):
    """Headless Chrome with no network and every file it writes kept in tmp.

    --user-data-dir alone still leaves Crashpad files in ~/Library, so CFFIXED_USER_HOME
    points Chrome's home there too."""
    (tmp / "home").mkdir(exist_ok=True)
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
           "--disable-extensions", "--disable-breakpad", "--use-mock-keychain",
           "--host-resolver-rules=MAP * ~NOTFOUND", "--proxy-server=127.0.0.1:9",  # no network at all
           f"--user-data-dir={tmp / 'chrome'}", f"--disk-cache-dir={tmp / 'chrome-cache'}", *args]
    env = dict(os.environ, CFFIXED_USER_HOME=str(tmp / "home"))
    return subprocess.run(cmd, capture_output=True, text=True, timeout=600, env=env)


CSS = """
@page{size:A4;margin:16mm 14mm 15mm;
 @top-left{content:"PAPER_NAME";font:8pt Helvetica,Arial,sans-serif;color:#555}
 @top-right{content:"p " counter(page) " of " counter(pages);font:8pt Helvetica,Arial,sans-serif;color:#555}}
body{font:10.5pt/1.45 Georgia,serif;margin:0;font-variant-ligatures:none}
h1{font-size:18pt;margin:0 0 4px} h2{font-size:13pt;border-bottom:1px solid #999;margin:16px 0 6px}
h3{font-size:11.5pt;margin:12px 0 2px} h4{font-size:10.5pt;margin:8px 0 2px}
p{margin:0 0 6px} .kw{font-size:8.5pt;color:#555;margin:0 0 4px} .note{font-size:8pt;color:#666;margin:4px 0 0}
.stamp{font:9pt Helvetica,Arial,sans-serif;background:#f1f1f1;padding:4px 6px}
.block{break-inside:avoid;margin-bottom:10px} .part{break-before:page}
.part-cheatsheets section{break-before:page} .part-cheatsheets section:first-of-type{break-before:auto}
h2,h3,h4{break-after:avoid}
table{border-collapse:collapse;width:100%;font-size:8.5pt;margin:4px 0} td,th{border:1px solid #ccc;padding:2px 4px;vertical-align:top}
tr.subj td{background:#e4e4e4;font-weight:bold;font-size:9.5pt} tr.topic td{background:#f4f4f4;font-weight:bold}
td.pg{white-space:nowrap;width:4em} a{color:#003b8e;text-decoration:none}
.secs p{margin:0 0 3px;font-size:9pt} .idx{column-count:2;column-gap:16px;font-size:8.5pt}
.idx p{margin:0 0 2px;break-inside:avoid} .idx h4{margin:6px 0 2px}
pre{font-size:8.5pt;white-space:pre-wrap} li.d1{margin-left:14px} li.d2{margin-left:28px}
.box{border:1px solid #888;background:#f6f6f6;padding:4px 8px;margin:4px 0 8px;font-size:9.5pt;break-inside:auto}
.block:has(.box){break-inside:auto}
.kw,.box > p:first-child{break-after:avoid} .kw{break-inside:avoid} .box p,.box li{orphans:3;widows:2}
.box p{margin:0 0 3px} .box ul,.box ol{list-style:none;padding-left:0;margin:0 0 3px}
.box li.d0{margin-left:0} .box li.d1{margin-left:16px} .box li.d2{margin-left:32px} .box li.d3{margin-left:48px}
"""


def build_html(paper, parts, rows, blocks, index, built, pages):
    name, exam, subjects = PAPERS[paper]
    pg = lambda key: str(pages.get(key, "000"))
    link = lambda key, text: f"<a href='#{key}'>{text}</a>"
    out = [f"<!doctype html><html><head><meta charset='utf-8'><title>{name} Reference Pack</title>"
           f"<style>{CSS.replace('PAPER_NAME', name)}</style></head><body>",
           f"<h1>{html.escape(name)} Reference Pack</h1>",
           f"<p><b>{paper}</b> · {html.escape(' · '.join(f'{i} {s}' for i, s in enumerate(subjects)))} · "
           f"exam {exam}, 2:30–4:30pm</p>",
           f"<p class='stamp'>Built {built} from study/{paper}/ ({', '.join(['coverage.md'] + [p['file'] for p in parts])}). "
           "If you fixed anything since then, rebuild and copy this file again.</p>",
           "<p>Find things by Ctrl-F (keyword, case name, section or rule number), by the Contents below "
           "(Subject → Topic → Sub-point → block, with page numbers), or by the Keyword index at the end. "
           "Grey Source notes are for checking and are not retyped.</p>",
           "<h2>Contents</h2><div class='secs'>"]
    for part in parts:
        secs = " · ".join(f"{link(s['anchor'], inline(s['title']))} p {link(s['anchor'], pg(s['anchor']))}"
                          for s in part["sections"])
        out.append(f"<p><b>{part['file']}</b>: {secs}</p>")
    out.append(f"<p><b>{link('keyword-index', 'Keyword index')}</b> p {link('keyword-index', pg('keyword-index'))}</p></div>")
    out.append("<table><tr><th>Sub-point</th><th>Covered by</th><th>Page</th></tr>")
    subj = topic = None
    for r in rows:
        if len(subjects) > 1 and r["subj"] != subj:
            subj, topic = r["subj"], None
            out.append(f"<tr class='subj'><td colspan=3>{r['subj']} · {html.escape(subjects[r['subj']])}</td></tr>")
        if r["topic"] and r["topic"] != topic:
            topic = r["topic"]
            out.append(f"<tr class='topic'><td colspan=3>{inline(topic)}</td></tr>")
        cov = ANY_ID.sub(lambda m: link(m.group(0), m.group(0)), inline(r["covered"]))
        where = ", ".join(link(i, pg(i)) for i in dict.fromkeys(r["ids"]))
        out.append(f"<tr><td>{r['key']} {inline(r['sub'])}</td><td>{cov}</td><td class='pg'>{where}</td></tr>")
    out.append("</table>")
    for part in parts:
        out.append(f"<div class='part part-{part['file'][:-3]}'>{part['preamble']}")
        for s in part["sections"]:
            out.append(f"<section><h2 id='{s['anchor']}'>{inline(s['title'])}</h2>{s['intro']}")
            for b in s["blocks"]:
                out.append(f"<div class='block' id='{b['id']}'><h3>{b['id']} — {inline(b['title'])}</h3>"
                           f"<p class='kw'>Keywords: {inline(b['kw_raw'])}</p>{b['html']}"
                           f"<p class='note'>Source note: {inline(b['note'])}</p></div>{b['trail_html']}")
            out.append("</section>")
        out.append("</div>")
    out.append("<div class='part'><h2 id='keyword-index'>Keyword index</h2><div class='idx'>")
    letter = None
    for term in sorted(index, key=lambda t: (re.sub(r"^[^\w]+", "", t).lower(), t)):
        first = (re.sub(r"^[^\w]+", "", term)[:1] or "#").upper()
        first = "0–9" if first.isdigit() else first
        if first != letter:
            letter = first
            out.append(f"<h4>{html.escape(letter)}</h4>")
        refs = ", ".join(f"{link(i, blocks[i]['short'])} p {link(i, pg(i))}"
                         for i in sorted(index[term], key=lambda i: (blocks[i]["subj"], int(i.split("-")[-1]))))
        out.append(f"<p>{inline(term)} — {refs}</p>")
    out.append("</div></div></body></html>")

    def xref(m):  # in-text links to a block or section get its page number, like the contents page
        key, text = m.groups()
        if key not in blocks and key not in anchors:
            msg = f"link to #{key} ('{text}') has no matching block or section"
            if msg not in WARNINGS:
                WARNINGS.append(msg)
            return text
        return f"{link(key, text)} (p {pg(key)})"
    anchors = {s["anchor"] for part in parts for s in part["sections"]}
    return re.sub(r"<a class='xref' href='#([\w-]+)'>(.*?)</a>", xref, "\n".join(out))


def print_pdf(text, pdf, tmp):
    src = tmp / "pack.html"
    src.write_text(text)
    if pdf.exists():
        pdf.unlink()
    res = chrome(tmp, "--no-pdf-header-footer", "--generate-pdf-document-outline", f"--print-to-pdf={pdf}", src.as_uri())
    if not pdf.exists() or pdf.stat().st_size == 0:
        raise RuntimeError(f"Chrome printed nothing: {res.stderr.strip()[-500:]}")


def find_pages(pdf):
    """Page of every link target, from the named destinations Chrome writes for them."""
    r = PdfReader(pdf)
    return {str(k).lstrip("/"): r.get_destination_page_number(d) + 1 for k, d in r.named_destinations.items()}, r


# ---- Model Questions PDF (--questions) ------------------------------------------------------

QTAG = re.compile(r"\*\*(Q[\w-]+)\*\* · (.+)")
OPTION = re.compile(r"(?:[A-H]|[IVX]+)\. ")
QCSS = """
.q{break-inside:avoid;border-top:1px solid #ccc;padding-top:4px;margin:0 0 10px} .q.long{break-inside:auto}
.q h4{margin:0 0 2px} .q p{margin:0 0 3px} .q h4,.q .kw{break-after:avoid}
.facts{margin:0 0 8px} table.qtoc td:first-child{width:46%} .ql{white-space:nowrap}
.ans{border-left:3px solid #888;background:#f6f6f6;padding:3px 8px;margin:4px 0 0}
.toc{margin:0 0 2px 14px;font-size:9pt}
"""


def parse_questions(text):
    """'## <n> · Subject' → '### Topic' → '**Q…** · tags' questions; other '##' sections are skipped."""
    subjects, subj, topic, q, n_topics = [], None, None, None, 0
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            subj = dict(title=line[3:].strip(), topics=[]) if re.match(r"## \d+ ·", line) else None
            if subj:
                subjects.append(subj)
            topic = q = None
        elif subj is None:
            continue
        elif line.startswith("### "):
            n_topics += 1
            topic, q = dict(title=line[4:].strip(), anchor=f"topic-{n_topics}", qs=[], intro=[]), None
            subj["topics"].append(topic)
        elif m := QTAG.match(line):
            if topic is None:
                ERRORS.append(f"model-questions.md:{n}: {m.group(1)} sits under no '### Topic' heading")
                continue
            ticks = re.findall(r"`([^`]+)`", m.group(2))
            q = dict(id=m.group(1), line=n, lines=[],
                     keys=[t for t in ticks if KEY.fullmatch(t)],
                     ids=[i for t in ticks for i in ANY_ID.findall(t)],
                     source=" · ".join(p.strip() for p in m.group(2).split(" · ") if "`" not in p))
            topic["qs"].append(q)
        elif q is not None:
            q["lines"].append(line)
        elif topic is not None:
            topic["intro"].append(line)  # a written paper's hypothetical facts
    return subjects


def question_html(q, topic, subs, kws, written=False):
    """One question: tag line, Keywords, the question, then its answer boxed directly below.

    MCQ: the Keywords are the file's Topic, the Sub-points and the end-point blocks' Keywords.
    Written: the coverage Topics and Sub-points of its Keys and the titles of its Pre-writes, since a
    written answer cites many Pre-writes and their full Keywords would swamp the line."""
    body = "\n".join(q["lines"]).strip()
    cut = body.find("**Answer")
    ask, ans = (body, "") if cut < 0 else (body[:cut], body[cut:])
    if not ans:
        WARNINGS.append(f"model-questions.md:{q['line']}: {q['id']} has no '**Answer' line")
    ask = "\n".join("\n" + ln if OPTION.match(ln) else ln for ln in ask.splitlines())  # one option per line
    terms = ([] if written else [topic["title"]]) + list(dict.fromkeys(subs[k][0] for k in q["keys"] if k in subs and written))
    terms += [f"{k} {subs[k][1]}" for k in q["keys"] if k in subs]
    for k in q["keys"]:
        if k not in subs:
            WARNINGS.append(f"model-questions.md:{q['line']}: {q['id']} names Key {k}, which is not in coverage.md")
    for i in q["ids"]:
        if i not in kws:
            WARNINGS.append(f"model-questions.md:{q['line']}: {q['id']} points at {i}, which has no block")
        title, words = kws.get(i, ("", []))
        terms += [t for t in ([title] if written and title else [] if written else words) if t not in terms]
    ends = ", ".join(re.sub(r"^\w+-\w+-", "", i) for i in q["ids"])
    return (f"<div class='q{' long' if written else ''}' id='q-{q['id']}'><h4>{q['id']} · {inline(q['source'])}"
            + (f" · end point {ends}" if ends else "") + "</h4>"
            f"<p class='kw'>Keywords: {inline(', '.join(terms))}</p>{md(ask, q['id'])}"
            + (f"<div class='ans'>{md(ans, q['id'])}</div>" if ans else "") + "</div>")


def contents_table(names, subjects, rows, written, pg):
    """The Reference Pack's contents table, with questions in the right column: one row per coverage
    Sub-point (MCQ) or per coverage Topic (written), listing every question whose Keys fall in it."""
    if not rows:
        return []
    qs = [q for s in subjects for t in s["topics"] for q in t["qs"]]
    unit = (lambda r: (r["subj"], r["topic"])) if written else (lambda r: r["key"])
    hits = {}
    for q in qs:
        for u in dict.fromkeys(unit(r) for r in rows if r["key"] in q["keys"]):
            hits.setdefault(u, []).append(q)
    links = lambda found: ", ".join(
        f"<span class='ql'><a href='#q-{q['id']}'>{q['id']}</a> p <a href='#q-{q['id']}'>{pg('q-' + q['id'])}</a></span>"
        for q in found) or "—"
    out = [f"<table class='qtoc'><tr><th>{'Topic' if written else 'Sub-point'}</th><th>Questions</th></tr>"]
    subj = topic = last = None
    for r in rows:
        if len(names) > 1 and r["subj"] != subj:
            subj, topic = r["subj"], None
            out.append(f"<tr class='subj'><td colspan=2>{r['subj']} · {html.escape(names[r['subj']])}</td></tr>")
        if written:
            if unit(r) != last:
                last = unit(r)
                out.append(f"<tr><td><b>{inline(r['topic'] or names[r['subj']])}</b></td><td>{links(hits.get(last, []))}</td></tr>")
            continue
        if r["topic"] and r["topic"] != topic:
            topic = r["topic"]
            out.append(f"<tr class='topic'><td colspan=2>{inline(topic)}</td></tr>")
        out.append(f"<tr><td>{r['key']} {inline(r['sub'])}</td><td>{links(hits.get(r['key'], []))}</td></tr>")
    loose = [q for q in qs if not any(r["key"] in q["keys"] for r in rows)]
    if loose:
        out.append(f"<tr><td><i>Not tagged to a coverage Key</i></td><td>{links(loose)}</td></tr>")
    out.append("</table>")
    return out


def questions_html(paper, subjects, rendered, built, pages, facts, rows, written):
    name = PAPERS[paper][0]
    pg = lambda key: str(pages.get(key, "000"))
    total = sum(len(t["qs"]) for s in subjects for t in s["topics"])
    out = [f"<!doctype html><html><head><meta charset='utf-8'><title>{name} Model Questions</title>"
           f"<style>{CSS.replace('PAPER_NAME', name + ' model questions')}{QCSS}</style></head><body>",
           f"<h1>{html.escape(name)} Model Questions</h1>",
           f"<p class='stamp'>Built {built} from study/{paper}/model-questions.md: {total} questions by "
           f"{'paper (contents by Topic)' if written else 'Subject and Topic'}, each answer directly below its question. If you fixed anything since then, "
           "rebuild and copy this file again.</p>",
           "<p>Find a question by Ctrl-F on its Keywords (Topic, Sub-point, terms, sections, cases), or by the "
           "Contents below. \"End point\" names the block in the Reference Pack that holds the rule.</p>",
           "<h2>Contents</h2>"]
    out += contents_table(PAPERS[paper][2], subjects, rows, written, pg)
    if written:  # the body runs by paper
        out.append("<div class='secs'><p><b>By paper</b></p>")
        out += [f"<p class='toc'><a href='#{t['anchor']}'>{inline(t['title'])}</a> · {len(t['qs'])} question{'s' * (len(t['qs']) != 1)}"
                f" · p <a href='#{t['anchor']}'>{pg(t['anchor'])}</a></p>" for s in subjects for t in s["topics"]]
        out.append("</div>")
    else:
        out.append("<div class='secs'><p><b>By section</b></p>")
        out += [f"<p><b>{inline(s['title'])}</b>: " + " · ".join(
                f"<a href='#{t['anchor']}'>{inline(t['title'])}</a> p <a href='#{t['anchor']}'>{pg(t['anchor'])}</a>"
                for t in s["topics"]) + "</p>" for s in subjects]
        out.append("</div>")
    for s in subjects:
        out.append(f"<div class='part'><h2>{inline(s['title'])}</h2>")
        for t in s["topics"]:
            intro = f"<div class='facts'>{facts[t['anchor']]}</div>" if facts[t["anchor"]].strip() else ""
            out.append(f"<section><h3 id='{t['anchor']}'>{inline(t['title'])}</h3>{intro}{''.join(rendered[t['anchor']])}</section>")
        out.append("</div>")
    out.append("</body></html>")
    return "\n".join(out)


def build_questions(paper, d):
    """study/<paper>/model-questions.md → model-questions.pdf, with linked contents and page numbers."""
    src, dst = d / "model-questions.md", d / "model-questions.pdf"
    if not src.exists():
        print(f"BUILD FAILED: {src.relative_to(ROOT)} does not exist", file=sys.stderr)
        return 1
    subs, rows = {}, []
    if (d / "coverage.md").exists():
        rows = parse_coverage((d / "coverage.md").read_text(), paper, len(PAPERS[paper][2]))
        subs = {r["key"]: (r["topic"] or "", r["sub"]) for r in rows}
    kws = {}
    for f in CONTENT_FILES:
        if (d / f).exists():
            for m in re.finditer(r"^### (\S+) — (.*)\n\*Keywords: (.+)\*$", (d / f).read_text(), re.M):
                kws[m.group(1)] = (m.group(2).strip(), [k.strip() for k in m.group(3).split(",") if k.strip()])
    subjects = parse_questions(src.read_text())
    if not subjects:
        ERRORS.append("model-questions.md: no '## <n> · Subject' sections found")
    written = paper.endswith("-w")
    rendered = {t["anchor"]: [question_html(q, t, subs, kws, written) for q in t["qs"]]
                for s in subjects for t in s["topics"]}
    facts = {t["anchor"]: md("\n".join(t["intro"]), t["title"]) for s in subjects for t in s["topics"]}
    tmp = Path(tempfile.mkdtemp(prefix=f"build_pack-{paper}-questions-"))
    try:
        built, pdf, pages, stable = datetime.now().strftime("%-d %b %Y %H:%M"), tmp / "pack.pdf", {}, False
        targets = set(rendered) | {f"q-{q['id']}" for s in subjects for t in s["topics"] for q in t["qs"]}
        for _ in range(3 if not ERRORS else 0):
            try:
                print_pdf(questions_html(paper, subjects, rendered, built, pages, facts, rows, written), pdf, tmp)
            except (RuntimeError, subprocess.TimeoutExpired) as e:
                ERRORS.append(f"Chrome could not print the questions: {e}")
                break
            found, reader = find_pages(pdf)
            found = {k: v for k, v in found.items() if k in targets}
            if found == pages:
                stable = True
                break
            pages = found
        missing = sorted(targets - set(pages))
        if stable and missing:
            ERRORS.append(f"page lookup found no page for: {', '.join(missing[:20])}")
        elif not stable and not ERRORS:
            ERRORS.append("page numbers did not settle after 3 passes")
        total = sum(len(t["qs"]) for s in subjects for t in s["topics"])
        print(f"{paper} — model questions: {len(subjects)} Subjects, {len(rendered)} Topics, {total} questions")
        for w in WARNINGS:
            print(f"warning: {w}")
        if ERRORS:
            print(f"\nBUILD FAILED — {dst.relative_to(ROOT)} left unchanged:", file=sys.stderr)
            for e in ERRORS:
                print(f"  {e}", file=sys.stderr)
            return 1
        part_file = d / ".model-questions.pdf.part"
        shutil.copyfile(pdf, part_file)
        os.replace(part_file, dst)
        print(f"Built {dst.relative_to(ROOT)}: {len(reader.pages)} pages, {built}, page numbers stable")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ---- Report -------------------------------------------------------------------------------

def report(paper, rows, blocks, parts, wide_verify, cov_verify):
    _, _, subjects = PAPERS[paper]
    print("Coverage rows by state (AD-6 step 4)")
    print(f"  {'Subject':<40} {'rows':>4} " + " ".join(f"{s:>6}" for s in STATES) + "  TODO: verify")
    for i, s in enumerate(subjects):
        mine = [r for r in rows if r["subj"] == i]
        counts = [sum(r["state"] == st for r in mine) for st in STATES]
        verify = sum(b["verify"] for b in blocks.values() if b["subj"] == i) + cov_verify.get(i, 0)
        print(f"  {f'{i} {s}':<40} {len(mine):>4} " + " ".join(f"{c:>6}" for c in counts) + f"  {verify:>12}")
    if wide_verify:
        print(f"  {'(preambles and Topic intros)':<40} {'':>4} " + " " * 34 + f"  {wide_verify:>12}")
    gaps = [r for r in rows if r["qb"] and not r["ids"]]
    print(f"Tested rows with no ID (uncuttable item 2 gaps): {len(gaps) or 'none'}")
    for r in gaps:
        print(f"  {r['key']:<10} {r['sub'][:60]}  (Tested: {r['tested']}; Covered by: {r['covered']})")
    per_file = " · ".join(f"{p['file']} {sum(len(s['blocks']) for s in p['sections'])}" for p in parts)
    print(f"Blocks: {per_file}")


# ---- Main ---------------------------------------------------------------------------------

def main():
    args = sys.argv[1:]
    questions = "--questions" in args
    check = "--check" in args
    args = [a for a in args if a not in ("--questions", "--check")]
    if len(args) != 1 or args[0] not in PAPERS or (questions and check):
        print(f"usage: python3 tools/build_pack.py <paper-id> [--questions | --check]   (one of: {', '.join(PAPERS)})",
              file=sys.stderr)
        return 2
    paper = args[0]
    if questions:
        if not Path(CHROME).exists():
            print(f"missing: {CHROME}", file=sys.stderr)
            return 2
        return build_questions(paper, ROOT / "study" / paper)
    if not check and not Path(CHROME).exists():
        print(f"missing: {CHROME}", file=sys.stderr)
        return 2
    d = ROOT / "study" / paper
    dst = d / "reference-pack.pdf"
    nsubj = len(PAPERS[paper][2])
    if not (d / "coverage.md").exists():
        print(f"BUILD FAILED: {d / 'coverage.md'} does not exist; {dst} left unchanged", file=sys.stderr)
        return 1

    cov_text = (d / "coverage.md").read_text()
    rows = parse_coverage(cov_text, paper, nsubj)
    if not rows:
        ERRORS.append("coverage.md: no Sub-point rows found (a table with a 'Key' or '#' first column and "
                      "Keys like II.12, or 1.II.12 on a multi-Subject Paper)")
    cov_verify = {}
    for r in rows:
        cov_verify[r["subj"]] = cov_verify.get(r["subj"], 0) + ("TODO: verify" in r["sub"] + r["covered"])

    parts, blocks, wide_verify = [], {}, 0
    files = [f for f in CONTENT_FILES if (d / f).exists()]
    if not files:
        ERRORS.append(f"study/{paper}/ has none of {', '.join(CONTENT_FILES)}")
    for f in files:
        text = (d / f).read_text()
        preamble, sections = split_sections(f, text)
        wide_verify += sum("TODO: verify" in t for t in preamble.splitlines())
        part = dict(file=f, preamble=md(preamble, f"{f} preamble"), sections=[])
        for n, sec in enumerate(sections, 1):
            wide_verify += sum("TODO: verify" in t for t in sec["intro"])
            where = f"{f}:{sec['line']}"
            out = dict(title=sec["title"], anchor=f"{f[:-3]}-{n}", intro=md("\n".join(sec["intro"]), where),
                       blocks=[], line=sec["line"])
            for raw in sec["blocks"]:
                b = parse_block(f, raw, paper, nsubj)
                if not b:
                    continue
                if b["id"] in blocks:
                    ERRORS.append(f"{f}:{b['line']}: {b['id']} is duplicated (also {blocks[b['id']]['file']}:"
                                  f"{blocks[b['id']]['line']})")
                    continue
                b["html"] = md(b["body"], f"{f}:{b['line']}")
                b["trail_html"] = md(b["trailing"], f"{f}:{b['line']}")
                blocks[b["id"]] = b
                out["blocks"].append(b)
            part["sections"].append(out)
        parts.append(part)
        for sec in sections:
            lint_cheatsheet(f, sec)

    # AD-2: every Covered-by ID has a block, every block is in a row, no ID twice.
    named = {i for r in rows for i in r["ids"]}
    for r in rows:
        for i in r["ids"]:
            if i.startswith(paper + "-") and i not in blocks:
                ERRORS.append(f"coverage.md:{r['line']}: {r['key']} is covered by {i}, which has no block")
    for i, b in blocks.items():
        if i not in named:
            ERRORS.append(f"{b['file']}:{b['line']}: block {i} appears in no coverage.md row")

    index = {}
    for i, b in blocks.items():
        for term in b["kws"] + b["cases"]:
            index.setdefault(term, set()).add(i)

    if check:
        print(f"{paper} — {PAPERS[paper][0]} (check only, no PDF)")
        report(paper, rows, blocks, parts, wide_verify, cov_verify)
        print(f"Index terms: {len(index)}")
        for w in WARNINGS:
            print(f"warning: {w}")
        if ERRORS:
            sys.stdout.flush()
            print(f"\nCHECK FAILED — {len(ERRORS)} problem(s):", file=sys.stderr)
            for e in ERRORS:
                print(f"  {e}", file=sys.stderr)
            return 1
        print("Check passed")
        return 0

    tmp = Path(tempfile.mkdtemp(prefix=f"build_pack-{paper}-"))
    try:
        if not ERRORS:
            built = datetime.now().strftime("%-d %b %Y %H:%M")
            targets = set(blocks) | {s["anchor"] for p in parts for s in p["sections"]} | {"keyword-index"}
            pdf, pages, stable = tmp / "pack.pdf", {}, False
            for _ in range(3):  # pass 1 finds pages; pass 2 prints them; pass 3 only if they moved
                try:
                    print_pdf(build_html(paper, parts, rows, blocks, index, built, pages), pdf, tmp)
                except (RuntimeError, subprocess.TimeoutExpired) as e:
                    ERRORS.append(f"Chrome could not print the pack: {e}")
                    break
                found, reader = find_pages(pdf)
                found = {k: v for k, v in found.items() if k in targets}
                if found == pages:
                    stable = True
                    break
                pages = found
            missing = sorted(targets - set(pages))
            if stable and missing:
                ERRORS.append(f"page lookup found no page for: {', '.join(missing[:20])}")
            elif not stable and not ERRORS:
                ERRORS.append("page numbers did not settle after 3 passes")
            elif stable:
                text = "\n".join(p.extract_text() or "" for p in reader.pages)
                if "CONFIDENTIAL" in text and not any("CONFIDENTIAL" in (d / f).read_text() for f in files):
                    ERRORS.append("the printed PDF contains a CONFIDENTIAL footer")

        print(f"{paper} — {PAPERS[paper][0]}")
        report(paper, rows, blocks, parts, wide_verify, cov_verify)
        print(f"Index terms: {len(index)}")
        for w in WARNINGS:
            print(f"warning: {w}")
        if ERRORS:
            sys.stdout.flush()
            print(f"\nBUILD FAILED — {dst.relative_to(ROOT)} left unchanged. {len(ERRORS)} problem(s):", file=sys.stderr)
            for e in ERRORS:
                print(f"  {e}", file=sys.stderr)
            return 1
        part_file = d / ".reference-pack.pdf.part"
        shutil.copyfile(pdf, part_file)
        os.replace(part_file, dst)  # replace only on success (AD-1)
        print(f"Built {dst.relative_to(ROOT)}: {len(reader.pages)} pages, {built}, page numbers stable")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
