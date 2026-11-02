---
reviews: ../ARCHITECTURE-SPINE.md
type: rubric-review
date: 2026-11-02
verdict: revise
---

# Rubric review — Architecture Spine, Part B Bar Exam Helper

**Verdict: REVISE before promotion.** The shape is right for the seven papers not yet
started (pipes-and-filters, Markdown master, one pack file per Subject, generated index,
single Tracker writer) and it is mostly proportionate to a 29-day personal system. But it
contradicts the one paper that already has a working Reference Pack (`eth-w`), models
Sub-point and Pre-write as one-to-one when reality is many-to-one, leaves the build
script without an owner or deadline although `clk-m` needs a pack by Fri 6 Nov, and
defers backups although Markdown is now the only master copy.

Evidence read: the spine, `.memlog.md`, `PRD.md`, `SCHEMA.md`, `.gitignore`, all files in
`study/eth-w/` and `study/clk-m/`, the eth-w PDF (pypdf, pdftotext), the make-pdf skill and
binary, and the scratchpad builder that made the eth-w PDF.

## Findings by severity

### F1 — CRITICAL — Contradicts eth-w reality; Sub-point ≠ Pre-write (checklist 1, 5)

**Reality, as of 17:02 today:**
- `study/eth-w/` holds `coverage.md` (76 Sub-points, Roman-numbered `I.1` … `VII.6`),
  `prewrites.md` (34 Pre-writes, IDs `eth-w-0-1` … `eth-w-0-34`) and a working
  `reference-pack.pdf`. The PDF has 24 pages, a contents table Sub-point → Pre-write →
  page, a keyword index, and named destinations per Pre-write.
- That PDF was built by
  `/private/tmp/claude-501/-Users-bennettchristian-Downloads-Bennett-Part-B-Bar-Exam-Helper/28965415-eee3-43b8-bd84-1c9efe8f44c5/scratchpad/build_pack.py`.
  It reads `prewrites.md` + `coverage.md`, prints with headless Chrome directly (no
  make-pdf), and does two passes for page numbers.
- In eth-w, one Pre-write covers several Sub-points. `eth-w-0-1` covers II.1 and II.2;
  `eth-w-0-28` covers V.5 and VI.6; I.4 and III.1 both point to `eth-w-0-17`.
- `question-bank.md` and `weak-spots.md` refer to Sub-points by Roman number (`II.12`),
  not by `eth-w-0-n`.
- The eth-w conventions are `*Keywords: a, b, c*` (italic, comma-separated) and
  `*Source note: …*`, with aliases defined in `outline.md`.

**The spine says the opposite on every point:**
- "There is no `coverage.md`" (AD-2).
- One H3 is one Sub-point, and its ID is the one key (AD-3).
- `Keywords:` is `;`-separated and the source line is `Sources:` (AD-4).
- Aliases are defined in `sources.md`.
- The raw-material row grandfathers only `outline.md`.
- The memlog claims AD-3 "ratifies SCHEMA interim Pre-write/Flowchart ID". It does not:
  in SCHEMA and in eth-w, `<paper>-<subject#>-<n>` is a *Pre-write* ID. Reusing it as a
  *Sub-point* ID either renumbers eth-w, which AD-3 forbids, or collides with it.

**Divergence this lets through:**
- AD-2 allows an H3 to hold only content, `TODO:` or `None:`. It has no way to say
  "covered by another Sub-point's Pre-write". Sessions will variously duplicate the
  Pre-write, write a misleading `None:`, or leave a `TODO:` that inflates the build's gap
  count and blocks Notes 1.
- No migration is stated for eth-w, whose block ends tomorrow (3 Nov), so whoever touches
  it next must improvise one.

**Fix (KISS):**
1. Grandfather eth-w explicitly. Its `prewrites.md` + `coverage.md` + builder stay as they
   are. Copy the scratchpad builder into the repo now as `tools/build_pack_ethw.py`;
   `/private/tmp` will be lost.
2. Add a fourth allowed H3 body to AD-2/AD-4: `Covered by: <sub-point-id>`. The build
   counts it as covered and links to it in the index.
3. Change the memlog/AD-3 claim from "ratifies" to "supersedes, for papers started after
   2 Nov".
4. State on promotion that `SCHEMA.md` §Study outputs (`coverage.md`, `prewrites.md`,
   `templates.md`, `flowcharts.md`) is replaced by AD-2.

### F2 — HIGH — The build script has no owner, deadline or home; the only builder that works is ephemeral (checklist 7)

- `tools/` does not exist.
- AD-7 makes the Main Session the only writer of `tools/`. AD-6 says Paper Sessions run
  the script.
- The memlog's open question ("Who writes `tools/build_pack.py` and when? Must exist
  before first Practice Paper, clk-m sample paper ~6 Nov") was not carried into the spine,
  which has no Open Questions section at all.
- `study/clk-m/drills.md` schedules the 40 official sample questions, timed, for Fri 6 Nov.
  The clk-m block starts Wed 4 Nov.

**Fix:**
- Add an Open Questions section.
- Decide that the Main Session writes `tools/build_pack.py` on 3 Nov, before the clk-m
  brief, starting from the existing scratchpad builder, which already solves the two-pass
  page numbers with Chrome + pypdf.
- Name the fallback for a missing or broken build (text-only PDF, per PRD §7 item 5).

### F3 — HIGH — Backups and versioning wrongly deferred (checklist 3, 7)

AD-1 makes the Markdown the only master copy. `study/` is untracked: `git status` shows
`?? study/` and the only commit is the initial one. It sits on one Mac 29 days before the
exams.

Deferred item 5 says "nothing here depends on it". That is wrong: losing or overwriting a
pack file is a real path, a Paper Session can rewrite its own files wholesale, and nothing
lets anyone restore them.

**Fix:**
- Decide it rather than defer it. The Main Session commits `study/` (PDFs excluded) after
  each Paper Session hand-over, or Bennett confirms Time Machine/iCloud covers the repo
  folder.
- Add `study/*/reference-pack.pdf` to `.gitignore`. AD-1 says the PDF is git-ignored, but
  today it is not.

### F4 — MEDIUM — Rules that are not literal enough to enforce (checklist 2)

- **AD-4 line syntax.** The rule shows `Keywords:` / `Sources:` but not their literal
  form. eth-w already writes `*Keywords: …*` with commas. Fix: give the exact
  line-start forms the parser accepts, for example `^Keywords: ` and `^Sources: `, plain
  text with `;` separators. Make AD-6 report any H3 whose block does not match.
- **AD-4 has no `[ADOPTED]` tag**, unlike AD-1–3 and AD-5–8. Confirm or mark it proposed.
- **AD-3 ID retirement.** "Never reused; dropped IDs retired" leaves no record, so the
  build can catch duplicates but not reuse. Fix: keep a retired H3 as
  `None: retired`, which costs nothing and lets the duplicate check cover it.
- **AD-5 "about 12 nodes".** This cannot be enforced. Fix: make AD-6 warn above 12
  nodes, but not fail.
- **AD-8 covers only `p:2`, `s:1/2` and `n:2`.** FR-11's Notes 1 and Practice 1 have no
  write rule. Fix: `n:1` when the AD-6 report shows zero `TODO:` (excluding
  `TODO: verify`) for the Subject; `p:1` when a `D-n` on the Subject is marked. Both on
  Bennett's word.
- **The rebuild trigger is missing.** The memlog decided "rebuild at end of any turn
  that changed pack files"; the spine only shows rebuilds inside the Practice Paper
  sequence. Fix: add it to AD-1 or AD-6.
- **AD-6 overwrites the PDF before it knows the build succeeded.** A failed exam-week
  build could clobber the last good pack. Fix: render to a temp file and move it into
  place only on exit 0.

### F5 — MEDIUM — Operational envelope: getting PDFs to the device in exam week (checklist 7)

Deferring the reference-device rules to PRD Q1 is fine. But the spine adds no guard
against a stale pack on the device: in exam week Bennett copies "again after each fix",
and nothing shows which build he holds.

**Fix:**
- AD-6 stamps the build date-time (and git short hash once F3 lands) on page 1.
- Bennett checks the stamp before each exam.
- Carry the memlog assumption into the spine: links and Ctrl-F must be tested on the
  device's own viewer, with printed page numbers as the fallback. `make-pdf --toc` prints
  none in the contents, so F2's two-pass builder should add them as eth-w's already does.

### F6 — LOW — Working-file conventions vs clk-m and eth-w reality (checklist 5)

The working files already use their own formats:
- **clk-m:** `weak-spots.md` columns `Date | Set/Q | What I got wrong | Rule | Re-tested`;
  drills keyed `D1`, `D2-A`; inline `[DP-1 p16]` citations.
- **eth-w:** drills keyed `1`, `PP-1`.

None of these match the spine's `WS-n` / `D-n` / `pyp-<year>`.

**Fix:** one line in Consistency Conventions: existing working-file entries stay; new
entries from the paper's block start use the new keys.

### F7 — LOW — FR gaps (checklist 6)

All 11 FRs are mapped. Small holes:
- **FR-1** "or an explicit reason why not": AD-5 requires a fence under every MCQ H2,
  with no `None:` option for a Topic.
- **FR-8** "records the conflict": there is no convention for where. clk-m uses an
  outline section. Fix: an optional `Conflict:` line in the AD-4 block.
- **FR-4** 150–300 words: AD-6 could warn on Pre-writes outside 120–350 words. Optional.
- **§7 item 2** "tested Sub-points first": AD-6 could flag `TODO:` Sub-points that a
  tier-1 QB entry references. This is what eth-w's coverage table shows today.

### F8 — LOW — Tech pinning (checklist 4)

Versions are verified in the memlog and confirmed on disk: gstack 1.81.0.0 at commit
`0530392`, `~/.claude/skills/gstack/make-pdf/dist/pdf` present.

But:
- AD-6 writes `make-pdf --toc`, and no `make-pdf` exists on PATH. The real invocation is
  `$P generate --toc in.md out.pdf` with
  `P=~/.claude/skills/gstack/make-pdf/dist/pdf` (or `$MAKE_PDF_BIN`).
- gstack is a self-upgrading suite (`gstack-upgrade`), so the pin is not enforced.

**Fix:**
- Correct the invocation in AD-6.
- Either freeze gstack upgrades until 11 Dec, or drop make-pdf for headless Chrome
  directly as the eth-w builder does. That builder has fewer moving parts and is already
  proven here.

## Checklist summary

| # | Criterion | Result |
|---|---|---|
| 1 | Fixes the real divergence points, misses none | Partial. Misses many-to-one Pre-write coverage (F1), paper-level front matter (eth-w's opening/closing lines and "which conflict rule?" selector have no home in digit-prefixed Subject files), and literal line syntax (F4) |
| 2 | Each AD Rule enforceable and prevents its divergence | Mostly. AD-4 syntax, AD-3 retirement, AD-5 size and AD-8 levels 1 need tightening (F4) |
| 3 | Nothing Deferred lets two Paper Sessions diverge | Partial. "Committing `study/`" is wrongly deferred (F3). The build-script internals are fine as long as AD-4 line syntax is literal |
| 4 | Tech verified-current | Yes, in the memlog. Invocation wrong and pin unenforced (F8) |
| 5 | Ratifies existing reality | **No.** eth-w contradicted; clk-m working files not addressed (F1, F6) |
| 6 | Covers the PRD FRs | Yes, with small holes (F7) |
| 7 | Every owned dimension decided, deferred or open | Partial. No Open Questions section; build owner/deadline missing (F2); backups (F3); device staleness (F5); where it runs is decided |

## Over-engineering check

Mostly proportionate. Watch three things:
- **Migrating eth-w into the AD-2 layout** would be the biggest waste of the 29 days:
  34 Pre-writes, 76 Sub-points and Roman-numeral cross-references across three files, for
  a pack that already works. Grandfather it (F1).
- **The make-pdf dependency** is a 64 MB binary from an auto-updating skill suite, used
  for one rendering step that headless Chrome already does here (F8).
- **AD-3's permanent-ID discipline and Sub-point-ID-only references** are fine if cheap.
  Do not add tooling to police them beyond the duplicate check.

The two-pass page-number render, generated index and per-Topic Mermaid are justified by
FR-7, FR-2 and SM-4, and are already proven on eth-w. Keep them.
