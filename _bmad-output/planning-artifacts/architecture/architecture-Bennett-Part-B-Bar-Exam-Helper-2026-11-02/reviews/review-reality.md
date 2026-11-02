---
review: reality-check
target: ARCHITECTURE-SPINE.md (2026-11-02 draft)
reviewer_lens: every committed technical decision was tested on this machine, not asserted from training data
date: 2 Nov 2026
scratch: /private/tmp/claude-501/-Users-bennettchristian-Downloads-Bennett-Part-B-Bar-Exam-Helper/46991d04-55fd-4e61-b4c8-a1657a69b8ef/scratchpad/verify/
verdict: SOUND WITH FIXES. The toolchain does what the spine says, but AD-5's chart-size rule is wrong, and AD-6 needs three concrete build flags or checks before build_pack.py is written.
---

# Reality-check review — Architecture Spine

Every claim below was tested with the installed tools on 2 Nov 2026. The scratch files are
`t1.md` (anchors, links, TOC), `t2.md` (a broken chart and smart quotes), `t3*.md` / `fan*.md`
(chart readability), `big40.md` / `big80lr.md` (scale), `pass2.py` (two-pass index) and
`inspect.py` (named destinations, outline, links).

## 1. Claims confirmed

| Spine claim | Test | Result |
|---|---|---|
| Mermaid labels are searchable text (AD-5) | Quoted labels `"s 15(1) SCJA & O 8 r 1"`, `"§ 16 leave & Ann's case"`, `"Defendant's address abroad?"` → `pdftotext` | **Confirmed.** `§`, `&`, `'` and `(1)` all extract verbatim. Chart labels keep the straight `'` (no smartypants inside SVG). |
| `{#id}` is not supported (AD-6 step 2) | `### Heading {#clk-m-0-13}` | **Confirmed**, with a correction: it is not *ignored*, it is **printed literally** in the body, the contents and the bookmarks. The build must strip it. |
| Raw `<a id>` anchor in a heading works (AD-6 step 2) | `### <a id="clk-m-0-12"></a>Deemed consent by conduct` | **Confirmed.** The contents entry and bookmark read "Deemed consent by conduct" with no stray HTML. make-pdf assigns its own `toc-N` id to the `<h3>` and keeps the inner `<a id>`. |
| Internal links produce working annotations (AD-6 step 3) | `<a href="#clk-m-0-12">` in body and in an Index H1 | **Confirmed.** These are `/Link` annotations with `/Dest /clk-m-0-12`. pypdf `named_destinations` holds `/clk-m-0-12`, and `get_destination_page_number` returns the right page. |
| `--toc` gives a clickable contents page and PDF bookmarks | t1, big40 | **Confirmed.** H1, H2 and H3 all appear in the contents and as a three-level bookmark outline. |
| Contents has no printed page numbers | t1.html: `.toc-page` spans are empty | **Confirmed.** It is links only. The Paged.js `target-counter` never fills. |
| Two-pass "p N" index is stable (AD-6 step 4) | `pass2.py` rewrote 280 index links with `p N` from pass-1 dests, then rebuilt | **Confirmed.** All 605 named destinations sit on the same pages in both passes, and the page count is unchanged (220). The footer "N of M" equals the pypdf page index + 1, including on landscape pages, so a printed "p N" matches what the viewer shows. |
| Offline (Deployment table) | `.gstack/browse-network.log` after about 10 builds | **Confirmed.** All 282 requests went to `127.0.0.1`, none elsewhere. Mermaid is vendored in `lib/diagram-render/dist/diagram-render.html` (7.9 MB). Remote images are blocked unless `--allow-network` is passed. |
| Column-0 fences only | source `diagram-prepass.ts` "Extract column-0 fences" | Confirmed from source; the memlog spike had already tested it. |
| Build time is reasonable | big40: 280 Sub-points, 40 charts (10 nodes each), `--toc` | **11.4 s per pass**, so about 23 s for the two-pass build (220 pages, 2.8 MB). 80 charts with 240 Sub-points took **19.9 s per pass** (343 pages). make-pdf runs mermaid in batches of 40 calls per browser script under a 120 s cap, so 80+ charts take two scripts but are still fine. |
| Two Paper Sessions building at once | par1 and par2 run concurrently | **Confirmed.** Both exit 0 with 0 diagram failures after 14 s wall time. The gstack browse daemon is shared safely. |

## 2. Findings that change the spine

### F1 — AD-5's "about 12 nodes" cap does not stop shrunk charts; chart width does (HIGH)

make-pdf scales every chart to the column width. Labels shrink with the number of nodes **side by side**, not with the total node count. Label glyph-box height measured with `pdftotext -bbox` (body text is 12 pt):

| Chart | Label box height |
|---|---|
| TD, 1 cue → 3 children | 9.2 pt |
| TD, 1 cue → 4 children | 6.8 pt |
| TD, 1 cue → 6 children | 6.2 pt |
| TD, 10-node tree, 6 leaves wide (realistic) | **5.0 pt**, hard to read |
| Same tree as LR | 6.8 pt |
| TD, 1 cue → 10 children (11 nodes, within the cap) | **auto-promoted to a landscape page; labels are illegible** (`td-017.png`) |
| LR, 1 cue → 10 children | readable, but **the chart is split across two pages**: the 10th node lands on the next page (`lr-017.png`, `big80lr.pdf` p 17–18) |

**Fix:** replace "about 12 nodes" with a breadth rule, for example "at most 4 nodes in any one rank, prefer `flowchart LR`, labels of 6 words or fewer". Then add a build check: either flag any `[make-pdf] warning: promoting diagram to a landscape page`, or read each SVG `viewBox` width from `--to html` output and flag charts above a set width. The "split into several fences" escape hatch is right, but it must trigger on width.

### F2 — A failed chart does not fail make-pdf, and `--quiet` hides the failure (HIGH for AD-6 step 6)

A broken mermaid fence still gives **exit 0**, including with `--strict`, which covers images only. The only signals are:

- the stderr line `[make-pdf] warning: diagram N (mermaid) failed to render: …`, which **disappears under `--quiet`**;
- the text "Diagram failed to render (mermaid)" in the PDF, or `class="diagram-error"` in `--to html` output.

AD-6 promises "exits non-zero if any diagram failed to render", so build_pack.py has to detect the failure itself. Run without `--quiet` and grep stderr, or grep `pdftotext` output for "Diagram failed to render". The spine should name that mechanism; otherwise the obvious `subprocess.run(...).returncode` check passes on a broken pack.

### F3 — Smartypants rewrites body text but not chart labels; Ctrl-F with a straight `'` may miss (MEDIUM, unverified in a viewer)

make-pdf always runs smartypants on body text, and no flag turns it off. Measured with `t2.md`:

- `defendant's` → `defendant’s` (U+2019)
- `"deemed"` → `“deemed”`
- `--` → `—`
- `...` → `…`

`Keywords:` lines and the generated index are affected too. Chart labels, and anything in backticks, keep ASCII. Whether Bennett's reference-device viewer matches `'` against `’` was **not tested**, because no viewer was driven. **Fix:** test Ctrl-F for `Ann's` on the actual device's viewer before the first Practice Paper. If it does not normalise apostrophes, either write keywords without apostrophes, or have build_pack.py emit both forms in the index.

### F4 — Default make-pdf output needs three flags in AD-6 (LOW to MEDIUM)

- **Footer:** "CONFIDENTIAL" is printed on every page by default. Pass `--no-confidential`.
- **Running header:** it is the first H1 on **every** page. In big40 every page of Subjects 1–3 and of the Index is headed "Subject 0 — Synthetic", which misleads during an open-book lookup. Pass `--title "<paper-id> Reference Pack"`. That `--title` changes the header was not checked on a multi-page build.
- **Contents length:** with every H3 in the contents, 280 Sub-points produce **15 pages of contents** (pp 1–15) before the first Subject, with no page numbers. Also, `.toc li.level-2` is used for both H2 and H3, so Topics and Sub-points are indented the same and cannot be told apart. This is acceptable because the bookmarks give a proper three-level tree, but the spine or `DESIGN.md` should decide it consciously. One option is to put the generated keyword index first in reading guidance, since it has page numbers.

### F5 — The "writes nothing outside `study/<paper-id>/`" claim is slightly false (LOW)

Each make-pdf run creates or updates a `.gstack/` folder in the **current working directory**. It holds browse-daemon state and logs (about 180 KB), plus its own `.gitignore`. The repo root already has one from earlier runs. It also leaves a background browse daemon running. This is harmless to git but contradicts AD-6's last line. Either run make-pdf with `cwd` set to a temp dir, or reword the claim.

### F6 — H3 text is uppercased in the PDF text layer (INFO)

The print CSS sets `h3 { text-transform: uppercase }`. The bookmarks and the extracted text read "DEEMED CONSENT BY CONDUCT". Case-insensitive viewer search is unaffected. The contents entries keep their original case.

## 3. Stack table

| Row | Claimed | Found | Status |
|---|---|---|---|
| make-pdf | 1.0.0 (gstack 1.81.0.0) | `1.0.0` is only the `version:` in `make-pdf/SKILL.md` frontmatter. `dist/pdf version` prints **"make-pdf (version unknown)"**, because the compiled binary cannot resolve `../../VERSION` from argv. gstack `VERSION` = `1.81.0.0`, commit `0530392` dated 2026-09-06. | Confirmed with a caveat. The pin is "gstack 1.81.0.0 @ 0530392"; 1.0.0 is not machine-checkable. |
| Python | 3.12.5 | `python3 --version` → 3.12.5 | Confirmed |
| pypdf | 6.16.2 | `pypdf.__version__` → 6.16.2 | Confirmed |
| poppler pdftotext | 26.09.0 | `pdftotext -v` → 26.09.0 | Confirmed |
| *(missing)* mermaid | — | **11.16.1**, exact-pinned in `lib/diagram-render/package.json` and present in the bundle | Add it. Chart parsing and layout (F1, F2) depend on it. |
| *(missing)* marked | memlog says ^18 | 18.0.11 in gstack `node_modules` | Optional |
| *(missing)* renderer | — | the gstack browse fallback (`browse/dist/browse`); `pdf setup` passes 5/5; Aside is not running | Name it. It is the PDF engine. |

## 4. Not tested

- Ctrl-F apostrophe matching and internal-link behaviour in the **reference-device viewer**. That device is unknown until PRD Q1 is answered.
- Whether `--title` changes the running header on every page.
- Phrase search across a **wrapped** chart label. For example, "Defendant's address abroad?" wraps in the label and extracts as two lines. AD-5 already notes this risk.

## 5. Suggested spine edits (for the author)

1. **AD-5 Size:** replace "about 12 nodes at most" with a breadth limit, for example "at most 4 nodes per rank, prefer LR, short labels". Add a build check on landscape promotion or chart width.
2. **AD-6 step 4:** name the flags `--toc --no-confidential --title "<paper-id> Reference Pack"`, and say "do not use `--quiet`".
3. **AD-6 step 6:** detect diagram failures by stderr warning or by "Diagram failed to render" in the PDF text, because make-pdf exits 0 on them.
4. **AD-6 last line:** run make-pdf with a temp `cwd`, or allow `.gstack/`.
5. **AD-6 step 2 wording:** "make-pdf prints `{#id}` literally", not "ignores".
6. **Stack:** add mermaid 11.16.1 and the gstack browse renderer; pin make-pdf as gstack 1.81.0.0 @ 0530392.
7. **Open TODO:** test apostrophe search on the reference-device viewer (F3).
