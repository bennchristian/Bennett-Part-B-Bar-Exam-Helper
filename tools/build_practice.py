"""Build a Practice Pack PDF for one Paper from its Model Q&A Markdown — nothing is rewritten.

Usage: python3 tools/build_practice.py <paper-id> [--md]

Rearranges the questions already in the Paper's model-questions file(s) so they can be sat like a
real paper:

  1. Contents (with page numbers)
  2. Past papers — the 2026 Sample Questions, then each past year newest first, questions in their
     original paper order, each with its fact pattern; question text only
  3. Drills — every other question (own, drill and course questions), in timed sets by Topic
  4. Answer key with explanations — every answer, in the same order, with its tag line

A question is a past-paper question when its tag line's source starts with "PYP <year>", "<year> "
or names the Sample Questions ("SQ", "Sample Questions", "Official sample"). Everything else is a
Drill question. Writes study/<folder>/<paper-id>-practice.pdf (with --md, also the Markdown it
printed, to the system temp directory, for checking). Reads only study/; writes only that PDF.
"""
import html
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_pack as bp  # noqa: E402  (md, inline, chrome printing, CSS, PAPERS)

ROOT = bp.ROOT
SOURCES = {  # Paper → (output folder, model-questions files in paper order)
    "eth-w": ("eth-w", ["eth-w/model-questions.md"]),
    "clk-m": ("clk-m", ["clk-m/model-questions.md"]),
    "drp-w": ("drp-w-cl", ["drp-w-cl/cl-model-questions.md", "drp-w-wa/wa-model-questions.md"]),
    "drp-m": ("drp-m", ["drp-m/model-questions.md"]),
    "pcp-w": ("pcp-w", ["pcp-w/model-questions.md"]),
    "pcp-m": ("pcp-m", ["pcp-m/model-questions.md"]),
    "ccp-1": ("ccp-1", ["ccp-1/model-questions.md"]),
    "ccp-2": ("ccp-2", ["ccp-2/model-questions.md"]),
}

QTAG = re.compile(r"\*\*(Q[\w-]+)\*\* · (.+)")
CODE = re.compile(r"(\d+)\.([IVXLC]+)(?:\.(\d+))?\b")
FACTS_BOLD = re.compile(r"^\*\*([^*]*\b[Ff]acts\b[^*]*?)[.:]?\*\*")
FACTS_REF = re.compile(r"^\*Facts: (.+?)(?:, under [^*]*?)?,? above\.\*\s*")
SQ = re.compile(r"^(SQ\b|Sample Questions|Official sample)")
YEAR = re.compile(r"^(?:PYP )?(20\d\d)\b")
WARN = []


def nat(s):
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", s)]


def facts_key(label):
    """'PYP 2025 Crim Q1 facts (= SQ22)' → 'PYP 2025 Crim Q1'; 'Facts A — …' → 'Facts A'."""
    m = re.match(r"Facts ([A-D]) —", label)
    if m:
        return f"Facts {m.group(1)}"
    if "`" in label:  # 'Real case facts used by the `Q1-25F` questions …'
        return label
    return re.split(r"\s+facts\b", label, 1, re.I)[0].strip()


def pointer(text):
    """A fact paragraph that only points elsewhere ('See Q2025-4-1 under 0.XII.2 (…).')."""
    body = re.sub(r"^\*\*[^*]+\*\*\s*", "", text.strip())
    return bool(re.match(r"(See|As for) ", body)) and not strip_pointer(body).strip()


def strip_pointer(text):
    """Drop a leading 'See Q… under 0.II.4 (…).' sentence; the facts it points to are printed above."""
    return re.sub(r"^((?:\*\*[^*]+\*\*\s*)?)(?:See|As for) (?:[^()]|\([^)]*\))*?\.(?:\s+|$)(?=[A-Z\[*]|$)", r"\1", text.strip(), 1)


def kind_of(label_or_source):
    s = label_or_source
    if SQ.match(s) or re.match(r"Facts [AB] — SQ", s):
        return ("real", "SQ")
    if m := YEAR.match(s):
        return ("real", m.group(1))
    return ("own", None)


# ---- Parsing -------------------------------------------------------------------------------

def parse(files):
    """Every question with its section, Subject, Topic, stem, answer and nearby fact paragraphs."""
    qs, facts = [], {}
    order = 0
    for fi, rel in enumerate(files):
        lines = (ROOT / "study" / rel).read_text().splitlines()
        subj = topic = section = None
        sec_paras, q, para = [], None, []

        def end_para():
            nonlocal para
            if para:
                text = "\n".join(para)
                if (m := FACTS_BOLD.match(para[0])) and (q is None or q["answer_started"]):
                    label = m.group(1).strip()
                    key = facts_key(label)
                    if not pointer(text) and len(text) > len(facts.get(key, "")):
                        facts[key] = text
                    sec_paras.append(("facts", key, text))
                elif q is None:
                    sec_paras.append(("text", None, text))
                para = []

        for line in lines + ["# END"]:
            if line.startswith("#"):
                end_para()
                q = None
                h = re.match(r"(#+) +(.*)", line)
                level, title = len(h.group(1)), h.group(2).strip()
                if level <= 2:
                    m = re.match(r"(?:Part \d+ · )?(\d+) · (.*)", title) if level == 2 else None
                    subj = (int(m.group(1)), re.split(r" — ", m.group(2))[0]) if m else None
                    section, sec_paras, topic = None, [], None
                elif level == 3:
                    c = CODE.match(title)
                    if c and not c.group(3):
                        topic = title
                    section = dict(title=title, coded=bool(c), file=fi, paras=[])
                    sec_paras = section["paras"]
                continue
            m = QTAG.match(line)
            if m and subj is not None:
                end_para()
                fields = [p.strip() for p in m.group(2).split(" · ")]
                plain = [p for p in fields if "`" not in p]
                q = dict(id=m.group(1), tag=m.group(2), source=plain[0] if plain else "",
                         extra=plain[1:], subj=subj, topic=topic, section=section, file=fi,
                         order=order, stem=[], answer=[], answer_started=False,
                         before=list(sec_paras))
                order += 1
                qs.append(q)
                continue
            if q is not None and q["answer_started"] and FACTS_BOLD.match(line):
                q = None  # a fact paragraph after an answer belongs to the questions that follow
            if q is not None:
                if line.startswith("**Answer"):
                    q["answer_started"] = True
                if line.strip() != "---":
                    (q["answer"] if q["answer_started"] else q["stem"]).append(line)
                continue
            if line.strip() == "---":
                end_para()
                continue
            if not line.strip():
                end_para()
            else:
                para.append(line)
    return qs, facts


def attach_facts(q, facts):
    """The fact paragraph(s) a question needs, by: explicit 'Facts:' reference, 'Facts A'-style
    mention, backticked ID prefix, nearest fact paragraph above it in its section, source prefix."""
    stem = "\n".join(q["stem"]).strip()
    kind, year = kind_of(q["source"])
    keys = []
    if m := FACTS_REF.search(stem):
        name = m.group(1).strip()
        k = name if name in facts else next((k for k in facts if k.startswith(name)), None)
        if k:
            keys.append((k, facts[k]))
        else:
            WARN.append(f"{q['id']}: facts '{name}' not found")
        stem = FACTS_REF.sub("", stem, 1)
    if not keys and (m := re.match(r"Facts ([A-D])\b", stem)):
        keys.append((f"Facts {m.group(1)}", facts.get(f"Facts {m.group(1)}", "")))
    if not keys:
        for k in facts:
            if (b := re.search(r"`(Q[\w-]+)`", k)) and q["id"].startswith(b.group(1)):
                keys.append((k, facts[k]))
    if not keys:
        for typ, k, text in reversed(q["before"]):
            if typ == "facts" and k is not None:
                fk, fy = kind_of(k)
                if fk == kind and (kind == "own" or fy == year or (fy == "SQ") == (year == "SQ")):
                    if pointer(text) and k in facts:
                        keys.append((k, facts[k]))
                    elif not pointer(text):
                        if k in facts and facts[k] != text:
                            keys.append((k, facts[k]))  # the full facts first, then this addition
                        keys.append((k, text))
                break
    if not keys and kind == "real":
        hits = [k for k in facts if re.match(re.escape(k) + r"(?!\d)", q["source"])]
        if hits:
            k = max(hits, key=len)
            keys.append((k, facts[k]))
    q["facts"] = keys
    # each MCQ option on its own line: a blank line before 'A. ', 'b) ', 'IV. ' lines
    q["stem_text"] = re.sub(r"\n(?=(?:[A-Ha-h]|[IVX]{1,4})[.)] )", "\n\n", stem)
    return q


# ---- Ordering ------------------------------------------------------------------------------

def mins(q, written):
    for e in q["extra"]:
        if m := re.match(r"(\d+) minutes?", e):
            return int(m.group(1))
    for e in q["extra"]:
        if m := re.match(r"(\d+) marks", e):
            return math.ceil(int(m.group(1)) * 1.2)
    return None if written else 2


def marks(q):
    for e in q["extra"]:
        if m := re.match(r"(\d+) marks", e):
            return int(m.group(1))
    return None


def past_groups(qs):
    """[(title, [questions])]: Sample Questions first, then years newest first, paper order."""
    real = [q for q in qs if kind_of(q["source"])[0] == "real"]
    first_seen = {}
    for q in real:
        label = re.sub(r"\s*(\([^)]*\)|\[[^\]]*\])", "", re.split(r"\bQ\d", q["source"])[0]).strip()
        q["label"] = label
        first_seen.setdefault(label, q["order"])

    # Sample Questions: by Subject (the ID minus its number, placed by its first page), then number
    sq_page, sq_seen = {}, {}
    for q in real:
        if kind_of(q["source"])[1] == "SQ":
            g = re.sub(r"\d+[a-z]?$", "", q["id"])
            page = re.search(r"\bpp?(\d+)", q["source"])
            sq_page[g] = min(sq_page.get(g, 10 ** 6), int(page.group(1)) if page else 10 ** 6)
            sq_seen.setdefault(g, q["order"])

    def key(q):
        if kind_of(q["source"])[1] == "SQ":
            g = re.sub(r"\d+[a-z]?$", "", q["id"])
            n = re.search(r"\bQ(\d+)", q["source"])
            return (sq_page[g], sq_seen[g], int(n.group(1)) if n else 0, nat(q["id"]), q["order"])
        ref = re.split(r"[(;,\[]", q["source"])[0]
        return (0, first_seen[q["label"]], nat(ref), nat(q["id"]), q["order"])

    groups = []
    sq = sorted([q for q in real if kind_of(q["source"])[1] == "SQ"], key=key)
    if sq:
        groups.append(("2026 Sample Questions", sq))
    years = sorted({kind_of(q["source"])[1] for q in real} - {"SQ"}, reverse=True)
    for y in years:
        groups.append((f"{y} past paper", sorted([q for q in real if kind_of(q["source"])[1] == y], key=key)))
    return groups


def drill_sets(qs, written):
    """Non-past-paper questions in file order, cut into timed sets at Topic (or question) boundaries."""
    own = [q for q in qs if kind_of(q["source"])[0] == "own"]
    units = []  # (title, [qs]) — a Topic, or one question-level section
    for q in own:
        sec = q["section"]
        if sec and not sec["coded"]:
            title = re.sub(r"^Drill \d+ (\(H\d+\) )?— ", "", re.split(r" · ", sec["title"])[0])
        else:
            title = f"{q['subj'][1]}: {re.sub(r'^\d+\.', '', q['topic'] or (sec['title'] if sec else ''))}".rstrip(": ")
            title = re.sub(r"^([^:]+): ([IVXLC]+) ", r"\1 — \2. ", title)
        if units and units[-1][0] == title and units[-1][2] == (q["file"], q["subj"]):
            units[-1][1].append(q)
        else:
            units.append((title, [q], (q["file"], q["subj"])))
    target = 50 if written else 40  # minutes
    sets, cur = [], None
    for title, items, grp in units:
        coded = not any(q["section"] and not q["section"]["coded"] for q in items)
        t = sum(mins(q, written) or 0 for q in items)
        if not coded:  # an eth-style drill or practice-session question stands alone
            sets.append(dict(titles=[title], qs=items))
            cur = None
            continue
        if cur and cur["grp"] == grp and cur["t"] + t <= target * 1.3 and cur["t"] < target:
            cur["titles"].append(title)
            cur["qs"] += items
            cur["t"] += t
        else:
            cur = dict(titles=[title], qs=list(items), t=t, grp=grp)
            sets.append(cur)
    out = []
    for s in sets:  # split anything far over the target
        n = len(s["qs"])
        per = 30 if not written else n
        chunks = [s["qs"][i:i + per] for i in range(0, n, per)] if n > per * 1.3 else [s["qs"]]
        for i, c in enumerate(chunks):
            out.append(dict(titles=s["titles"], qs=c, part=(i + 1, len(chunks)) if len(chunks) > 1 else None))
    return out


def set_title(s):
    t = s["titles"]
    if len(t) > 1:
        subj = t[0].split(" — ")[0]
        same = all(x.split(" — ")[0] == subj for x in t)
        title = subj + " — " + "; ".join(x.split(" — ", 1)[-1] for x in t) if same else "; ".join(t)
    else:
        title = t[0]
    if s.get("part"):
        title += f" (part {s['part'][0]} of {s['part'][1]})"
    return title


def timing(items, written):
    m = [mins(q, written) for q in items]
    total = sum(x for x in m if x)
    mk = [marks(q) for q in items]
    if written and all(mk) and not any(re.match(r"\d+ minutes?", e) for q in items for e in q["extra"]):
        total = math.ceil(sum(mk) * 1.2)
    mk_txt = f" · {sum(x for x in mk if x)} marks" if written and any(mk) else ""
    t_txt = f" · {5 * math.ceil(total / 5)} minutes" if total else ""
    return f"{len(items)} question{'s' * (len(items) != 1)}{mk_txt}{t_txt}"


# ---- Rendering -----------------------------------------------------------------------------

def anchor(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def q_head(q, written):
    mk = marks(q)
    return f"<p class='qid' id='q-{anchor(q['id'])}'><b>{html.escape(q['id'])}</b>" + \
        (f" · {mk} marks" if written and mk else "") + "</p>"


def render(paper, qs, facts, built, pages, written):
    name = bp.PAPERS[paper][0]
    pg = lambda k: str(pages.get(k, "000"))
    groups = past_groups(qs)
    drills = drill_sets(qs, written)
    toc, body, key = [], [], []
    seen_ids = set()

    def facts_html(keys, shown):
        out = []
        for k, text in keys:
            if text and text not in shown:
                shown.add(text)
                out.append(f"<div class='facts'>{bp.md(strip_pointer(text), k)}</div>")
        return "".join(out)

    def section_context(q, shown):
        sec = q["section"]
        if not sec or sec["coded"] or id(sec) in shown:
            return ""
        shown.add(id(sec))
        paras = [t for typ, k, t in sec["paras"] if not (typ == "facts" and pointer(t))]
        shown |= {t for typ, k, t in sec["paras"]}
        intro = bp.md("\n\n".join(paras), sec["title"]) if paras else ""
        return f"<h4>{bp.inline(sec['title'])}</h4><div class='facts'>{intro}</div>"

    def questions(items, shown):
        out = []
        for q in items:
            out.append(section_context(q, shown) + facts_html(q["facts"], shown))
            out.append(f"<div class='q{' long' if written else ''}'>{q_head(q, written)}{bp.md(q['stem_text'], q['id'])}</div>")
        return "".join(out)

    def answers(items):
        out = []
        for q in items:
            ans = "\n".join(q["answer"]).strip() or "_No answer in the Model Q&A._"
            tag = re.sub(r"`([^`]+)`", r"\1", q["tag"])
            out.append(f"<div class='a'><p class='qid'><b>{html.escape(q['id'])}</b></p>"
                       f"<p class='kw'>{bp.inline(tag)}</p>{bp.md(ans, q['id'])}</div>")
        return "".join(out)

    # Past papers
    body.append("<div class='part'><h2 id='past'>Part 1 — Past papers</h2>"
                "<p>Newest first. Each paper keeps its original question order; questions held in more "
                "than one part of the Model Q&A appear once. Sit a paper unseen, timed, with the Reference "
                "Pack only, then mark it against Part 3.</p>")
    toc.append(f"<p class='t1'><a href='#past'>Part 1 — Past papers</a> <span>{pg('past')}</span></p>")
    for title, items in groups:
        a = anchor(title)
        body.append(f"<section class='paper'><h3 id='{a}'>{html.escape(title)}</h3>"
                    f"<p class='kw'>{timing(items, written)}</p>{questions(items, set())}</section>")
        toc.append(f"<p class='t2'><a href='#{a}'>{html.escape(title)}</a> · {timing(items, written)} <span>{pg(a)}</span></p>")
        seen_ids |= {q["id"] for q in items}
    body.append("</div>")

    # Drills
    body.append("<div class='part'><h2 id='drills'>Part 2 — Drills</h2>"
                "<p>Every other question in the Model Q&A (own, drill and course questions), in timed sets by "
                f"Topic. Time: {'1.2 minutes a mark, or the minutes the question gives' if written else '2 minutes a question, as in the exam'}"
                ", rounded up to 5 minutes.</p>")
    toc.append(f"<p class='t1'><a href='#drills'>Part 2 — Drills</a> <span>{pg('drills')}</span></p>")
    for i, s in enumerate(drills, 1):
        a = f"drill-{i}"
        t = f"Drill {i} — {set_title(s)}"
        body.append(f"<section class='paper'><h3 id='{a}'>{bp.inline(t)}</h3>"
                    f"<p class='kw'>{timing(s['qs'], written)}</p>{questions(s['qs'], set())}</section>")
        toc.append(f"<p class='t2'><a href='#{a}'>{bp.inline(t)}</a> · {timing(s['qs'], written)} <span>{pg(a)}</span></p>")
    body.append("</div>")

    # Answer key
    body.append("<div class='part'><h2 id='key'>Part 3 — Answer key with explanations</h2>"
                "<p>Same order as Parts 1 and 2. Under each ID: its tag line (Sub-point Keys · source · "
                "Reference Pack blocks), then the answer and why.</p>")
    toc.append(f"<p class='t1'><a href='#key'>Part 3 — Answer key with explanations</a> <span>{pg('key')}</span></p>")
    for title, items in groups:
        a = "key-" + anchor(title)
        body.append(f"<section><h3 id='{a}'>Answers — {html.escape(title)}</h3>{answers(items)}</section>")
        toc.append(f"<p class='t2'><a href='#{a}'>Answers — {html.escape(title)}</a> <span>{pg(a)}</span></p>")
    for i, s in enumerate(drills, 1):
        a = f"key-drill-{i}"
        body.append(f"<section><h3 id='{a}'>Answers — Drill {i}</h3>{answers(s['qs'])}</section>")
    toc.append(f"<p class='t2'><a href='#key-drill-1'>Answers — Drills 1–{len(drills)}</a> <span>{pg('key-drill-1')}</span></p>")
    body.append("</div>")

    files = ", ".join(f"study/{f}" for f in SOURCES[paper][1])
    n_past = sum(len(i) for _, i in groups)
    n_drill = sum(len(s["qs"]) for s in drills)
    head = [f"<!doctype html><html><head><meta charset='utf-8'><title>{name} Practice Pack</title>"
            f"<style>{bp.CSS.replace('PAPER_NAME', name + ' practice pack')}{PCSS}</style></head><body>",
            f"<h1>{html.escape(name)} Practice Pack</h1>",
            f"<p><b>{paper}</b> · exam {bp.PAPERS[paper][1]}, 2:30–4:30pm · {n_past} past-paper questions, "
            f"{n_drill} drill questions</p>",
            f"<p class='stamp'>Built {built} from {files}. The questions and answers are the Model Q&A's, "
            "rearranged; nothing is rewritten. If the Model Q&A changes, rebuild.</p>",
            "<p>Self-study only — never use this with a live quiz, the Mock Exam or another assessment "
            "(Handbook §7.11).</p>",
            "<h2>Contents</h2><div class='toc'>", *toc, "</div>"]
    return "\n".join(head + body + ["</body></html>"]), groups, drills


PCSS = """
.toc p{margin:0 0 2px;display:flex;gap:6px} .toc span{margin-left:auto} .toc .t1{font-weight:bold;margin-top:6px}
.toc .t2{margin-left:14px;font-size:9.5pt}
.paper{break-before:page} .part > .paper:first-of-type{break-before:auto}
.qid{margin:10px 0 2px;font-family:Helvetica,Arial,sans-serif;font-size:10pt;break-after:avoid}
.q{break-inside:avoid;margin:0 0 8px} .q.long{break-inside:auto}
.facts{border-left:3px solid #888;background:#f6f6f6;padding:4px 8px;margin:6px 0 8px}
.a{border-top:1px solid #ccc;margin:0 0 6px} .a .qid{margin-top:6px}
"""


def main():
    args = [a for a in sys.argv[1:] if a != "--md"]
    if len(args) != 1 or args[0] not in SOURCES:
        print(f"usage: python3 tools/build_practice.py <paper-id> [--md]   (one of: {', '.join(SOURCES)})", file=sys.stderr)
        return 2
    paper = args[0]
    folder, files = SOURCES[paper]
    written = paper.endswith("-w")
    qs, facts = parse(files)
    ids = [q["id"] for q in qs]
    dups = sorted({i for i in ids if ids.count(i) > 1})
    if dups:
        WARN.append(f"IDs used twice: {', '.join(dups)}")
    for q in qs:
        attach_facts(q, facts)
        if not q["answer"]:
            WARN.append(f"{q['id']}: no '**Answer' line")
    bp.FOLDER = folder
    dst = ROOT / "study" / folder / f"{paper}-practice.pdf"
    tmp = Path(tempfile.mkdtemp(prefix=f"build_practice-{paper}-"))
    try:
        built, pdf, pages = datetime.now().strftime("%-d %b %Y %H:%M"), tmp / "pack.pdf", {}
        for _ in range(3):
            text, groups, drills = render(paper, qs, facts, built, pages, written)
            bp.print_pdf(text, pdf, tmp)
            found, reader = bp.find_pages(pdf)
            if found == pages:
                break
            pages = found
        else:
            WARN.append("page numbers did not settle after 3 passes")
        if "--md" in sys.argv:
            (Path(tempfile.gettempdir()) / f"{paper}-practice.html").write_text(text)
        part = dst.with_name(f".{dst.name}.part")
        shutil.copyfile(pdf, part)
        os.replace(part, dst)
        print(f"{paper}: {len(qs)} questions — past papers: "
              + "; ".join(f"{t} ({len(i)})" for t, i in groups)
              + f"; {len(drills)} drills ({sum(len(s['qs']) for s in drills)} Qs)")
        for q in qs:
            if kind_of(q["source"])[0] == "real" and written and not q["facts"] and not (q["section"] and not q["section"]["coded"]):
                WARN.append(f"{q['id']}: past-paper question with no fact paragraph found ({q['source']})")
        for w in WARN:
            print(f"warning: {w}")
        print(f"Built {dst.relative_to(ROOT)}: {len(reader.pages)} pages")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
