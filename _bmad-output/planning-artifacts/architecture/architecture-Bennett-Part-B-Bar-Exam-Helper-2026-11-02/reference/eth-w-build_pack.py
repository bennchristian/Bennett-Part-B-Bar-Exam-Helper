"""Build study/eth-w/reference-pack.pdf from prewrites.md and coverage.md.

Usage: python3 -I build_pack.py <study/eth-w dir>
Two passes: print once, read each Pre-write's page with pypdf, print again with page refs.
"""
import html, json, re, subprocess, sys, tempfile
from pathlib import Path
from pypdf import PdfReader

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D = Path(sys.argv[1])
PW = (D / "prewrites.md").read_text()
COV = (D / "coverage.md").read_text()


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return t


def parse_prewrites():
    """Return (intro_md, [(section, id, title, keywords, body, note)])."""
    head, _, rest = PW.partition("\n## ")
    items, section = [], None
    for block in re.split(r"\n(?=## |### )", "## " + rest):
        if block.startswith("## "):
            section = block[3:].splitlines()[0].strip()
            continue
        m = re.match(r"### (eth-w-0-\d+) — (.+?)\n\*Keywords: (.+?)\*\n\n(.*)", block, re.S)
        if not m:
            continue
        pid, title, kw, rest2 = m.groups()
        body, _, note = rest2.partition("*Source note:")
        note = note.strip().rstrip("-").strip().rstrip("*").strip()
        items.append((section, pid, title, [k.strip() for k in kw.split(",")], body.strip(), note))
    return head, items


def parse_coverage():
    """Return [(topic, num, subpoint, prewrite_cell)]."""
    rows, topic = [], None
    for line in COV.splitlines():
        if line.startswith("## "):
            topic = line[3:].strip()
        m = re.match(r"\| ([IVX]+\.\d+) \| (.+?) \| (.+?) \| (.+?) \|$", line)
        if m:
            rows.append((topic, m.group(1), m.group(2), m.group(4)))
    return rows


def cases_in(text):
    return sorted(set(c for c in re.findall(r"\*([^*]+? v [^*]+?)\*", text)))


def build_html(items, cov, pages):
    pg = lambda pid: pages.get(pid, "00")
    out = ["<html><head><meta charset='utf-8'><title>ETH-W Reference Pack</title><style>",
           "body{font:10.5pt/1.45 Georgia,serif;margin:0} h1{font-size:18pt} h2{font-size:13pt;border-bottom:1px solid #999;margin-top:18px}",
           "h3{font-size:11.5pt;margin:14px 0 2px} .kw{font-size:8.5pt;color:#555;margin:0 0 4px} .note{font-size:8pt;color:#666;margin:4px 0 0}",
           ".pw{page-break-inside:avoid;margin-bottom:10px} table{border-collapse:collapse;width:100%;font-size:8.5pt} td,th{border:1px solid #ccc;padding:2px 4px;vertical-align:top}",
           ".pb{page-break-before:always} a{color:#003b8e;text-decoration:none} .idx{column-count:2;font-size:8.5pt} .idx p{margin:0 0 2px}",
           "@page{size:A4;margin:14mm 14mm 16mm 14mm}</style></head><body>"]
    out.append("<h1>ETH-W Reference Pack — Ethics &amp; Professional Responsibility</h1>")
    out.append("<p>Exam Thu 3 Dec 2026, 2:30–4:30pm. Find it by Ctrl-F (keyword, case name or rule number), "
               "the contents below (Topic → Sub-point → Pre-write), or the keyword index at the end. "
               "Bold letters I C R P A C are place-markers — don't type them. Grey source notes are not retyped. "
               "Built 2 Nov 2026 from study/eth-w/prewrites.md.</p>")
    out.append("<p><b>Answer shape (INTRO2 p25):</b> issue → rule, PD/GN → cases → competing considerations and exceptions → "
               "apply to facts → conclude whether there is a breach (and for conflicts, whether the lawyer may act and with what safeguards).</p>")
    out.append("<p><b>Which conflict rule?</b> 2+ clients in one matter → r 20 (0-7, 0-8). Former client + confidential info → r 21 (0-11). "
               "Own/family/firm interest → r 22 (0-13, 0-14). Lawyer will be a witness → r 11(3) (0-22, 0-23). "
               "Firm drafted the disputed document for both sides → r 20(8) (0-9). Opponent demands withdrawal → court's power (0-12).</p>")
    out.append("<h2>Contents</h2><table><tr><th>Sub-point</th><th>Pre-write</th><th>Page</th></tr>")
    topic = None
    for t, num, sp, cell in cov:
        if t != topic:
            topic = t
            out.append(f"<tr><td colspan=3><b>{inline(t)}</b></td></tr>")
        ids = re.findall(r"eth-w-0-\d+", cell)
        if ids:
            links = ", ".join(f"<a href='#{i}'>{i}</a>" for i in ids)
            pages_ = ", ".join(f"<a href='#{i}'>{pg(i)}</a>" for i in ids)
        else:
            links, pages_ = "<i>not written (untested)</i>", ""
        out.append(f"<tr><td>{num} {inline(sp)}</td><td>{links}</td><td>{pages_}</td></tr>")
    out.append("</table>")
    out.append("<h2 class='pb'>Pre-writes</h2>")
    section = None
    for sec, pid, title, kw, body, note in items:
        if sec != section:
            section = sec
            out.append(f"<h2>{inline(sec)}</h2>")
        paras = "".join(f"<p>{inline(p.replace(chr(10), ' '))}</p>" for p in body.split("\n\n"))
        out.append(f"<div class='pw' id='{pid}'><h3>{pid} — {inline(title)}</h3>"
                   f"<p class='kw'>Keywords: {inline(', '.join(kw))}</p>{paras}"
                   f"<p class='note'>Source note: {inline(note.replace(chr(10), ' '))}</p></div>")
    # keyword index: keywords + case names, each -> pre-write ids with pages
    idx = {}
    for _, pid, _, kw, body, _ in items:
        for k in kw + cases_in(body):
            idx.setdefault(k.strip(), set()).add(pid)
    out.append("<h2 class='pb'>Keyword index</h2><div class='idx'>")
    for k in sorted(idx, key=lambda s: s.lower().lstrip("“\"'")):
        refs = ", ".join(f"<a href='#{i}'>{i[6:]} (p {pg(i)})</a>"
                         for i in sorted(idx[k], key=lambda x: int(x.split('-')[-1])))
        out.append(f"<p>{inline(k)} — {refs}</p>")
    out.append("</div></body></html>")
    return "\n".join(out)


def render(html_text, pdf):
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / "pack.html"
        src.write_text(html_text)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", src.as_uri()], check=True, capture_output=True)


def find_pages(pdf, ids):
    pages = {}
    for n, page in enumerate(PdfReader(pdf).pages, 1):
        text = page.extract_text() or ""
        for i in ids:
            if i not in pages and re.search(re.escape(i) + r" —", text):
                pages[i] = str(n)
    return pages


if __name__ == "__main__":
    _, items = parse_prewrites()
    cov = parse_coverage()
    out = D / "reference-pack.pdf"
    render(build_html(items, cov, {}), out)
    pages = find_pages(out, [i[1] for i in items])
    render(build_html(items, cov, pages), out)
    check = find_pages(out, [i[1] for i in items])
    print(json.dumps({"prewrites": len(items), "subpoints": len(cov),
                      "pages": len(PdfReader(out).pages), "page_refs_stable": check == pages,
                      "missing": [i[1] for i in items if i[1] not in pages]}))
