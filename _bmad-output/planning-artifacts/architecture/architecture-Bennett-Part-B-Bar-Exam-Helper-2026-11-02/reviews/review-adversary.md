# Adversary review — Architecture Spine, Part B Bar Exam Helper

- **Spine:** `../ARCHITECTURE-SPINE.md` (draft, 2 Nov 2026)
- **Lens:** build pairs of units that each obey every AD to the letter and still produce
  things that don't fit together. Each pair is a hole to close with a new or tighter AD.
- **Units:** the 8 Paper Sessions, the Main Session (sole Tracker writer and `tools/`
  author), extraction subagents, the `build_pack.py` author, and Bennett in the tracker page.
- **Proportionality:** this is a 29-day personal system. Holes are ranked by how likely
  they are to cost a study day or an exam-time lookup. Theoretical holes are listed last
  and kept short.
- **Evidence read:** the spine, `SCHEMA.md`, `PRD.md` (FR-9 to FR-11, SM-2 to SM-5),
  `AGENTS.md` (brief format), and the existing `study/eth-w/` and `study/clk-m/` files.

## Verdict

**The spine is sound but not yet safe to brief from.** Its paradigm, the ownership rules
(AD-1, AD-7) and the build contract (AD-6) hold up. Five holes would realistically bite:

1. Paper Sessions are never told to read the spine.
2. eth-w's existing IDs collide with AD-3's ID format.
3. The `Keywords:` syntax is underspecified for a line parser.
4. Nothing records which Subjects a Practice Paper covers.
5. A Sub-point has no legal "covered elsewhere" state.

All five can be closed with short AD edits before the clk-m block starts on 4 Nov.

---

## H1 — Briefed sessions read `SCHEMA.md`, which still prescribes the old layout (critical)

**Pair.**
- **Paper Session A (`clk-m`, briefed 4 Nov per `AGENTS.md`)**
  - Its reading order is `CLAUDE.md` → `PRD.md` → `RULES.md` → `SCHEMA.md`
    (AGENTS.md l.18–19). The spine is not on that list.
  - `SCHEMA.md` "Study outputs" tells it to write `coverage.md`, `prewrites.md` and
    `flowcharts.md`, IDs `<paper>-<subject#>-<n>` per Flowchart.
  - It obeys every AD it was ever shown.
- **`build_pack.py` author (Main Session), obeying AD-6**
  - Joins only `study/<id>/[0-9]-*.md`.

**Result.** clk-m produces zero pack files. The build joins nothing. AD-6's report checks
counts, duplicates and diagram errors, but none of these fails on "no files", so the
build succeeds with an empty pack. Three days of the block are spent on files the build
never reads.

AD-2's "There is no `coverage.md`" contradicts `SCHEMA.md` outright. AD-7 gives no
precedence rule between the two.

**Tightened rule (new AD-0, or add to AD-7):**
> The spine (promoted to root `ARCHITECTURE.md`) supersedes `SCHEMA.md` §"Study outputs".
> Before the next Paper Session is briefed:
> - that section is replaced by a pointer to AD-2–AD-5;
> - `AGENTS.md`'s reading order becomes `CLAUDE.md → PRD.md → RULES.md → ARCHITECTURE.md → SCHEMA.md`.

**Tighten AD-6:**
> Exit non-zero, and do not write or overwrite `reference-pack.pdf`, when:
> - no `[0-9]-*.md` file exists; or
> - any H3 in a pack file lacks a `{#id}`.

## H2 — eth-w's existing IDs collide with AD-3's shape and mean something else (critical)

**State on disk (2 Nov).**
- `study/eth-w/prewrites.md` uses `eth-w-0-1` … `eth-w-0-34` as **Pre-write** IDs.
  - One Pre-write often covers several Sub-points: `eth-w-0-1` covers coverage rows
    II.1 and II.2.
- `coverage.md` has 76 Sub-points keyed `I.1`…`VII.n`.
- `question-bank.md`, `drills.md` and `weak-spots.md` refer to Sub-points by those row
  keys (`QB-2 → II.1, II.10 …`), not by ID.

**Pair.** Two sessions migrate eth-w, and both obey AD-3.

- **Migrator A** renumbers in coverage order: `II.1 → eth-w-0-5`, …
  - AD-3's "never renumbered" doesn't apply, because these were never Sub-point IDs.
- **Migrator B** keeps `eth-w-0-1…34` on the H3 that holds each Pre-write and gives
  untested rows `35+`.

**Result.** Under A, every existing reference to `eth-w-0-21` in coverage.md and
weak-spots.md silently points at a different Sub-point. Under B, the H3 granularity is
the Pre-write, not the Sub-point, so II.1 and II.2 share one ID.

Either way, the `II.24`-style keys in QB, drills and weak-spots stay unmapped. AD-3 says
working files use IDs only, but nothing tells anyone to rewrite them.

A third, likely failure: the Main Session rebuilds eth-w before migration. AD-6 then
overwrites the existing `reference-pack.pdf` with an empty one, unless H1's guard is added.

eth-w's block ends 3 Nov, so this happens tomorrow.

**Tightened rule (add "Migration" to AD-3):**
> - Existing `eth-w-0-<n>` IDs are kept, each on the H3 that receives that Pre-write's
>   text.
> - Coverage rows with no Pre-write get the next free `n` in coverage order.
> - In the same change, rewrite every row key (`II.24`) in `question-bank.md`,
>   `drills.md` and `weak-spots.md` to the new ID. Leave a one-time key→ID table at the
>   top of `weak-spots.md`.
> - `coverage.md` and `prewrites.md` are then frozen as raw material, like `outline.md`.
> - Aliases defined in `outline.md` move to `sources.md`, as the conventions require.
>
> clk-m has drills and weak spots but no IDs, so it starts clean.

## H3 — `Keywords:` is defined as a "line", but sessions hard-wrap and bold labels (high)

**Pair.**
- **Paper Session**
  - The repo's prose is hard-wrapped at about 90 columns (every existing study file
    is), and AD-4 says Pre-writes use bold part labels.
  - So the session writes `**Keywords:** duty to court; r 4; Re Shankar …`, wrapped
    onto two physical lines.
- **Script author**
  - Reads AD-6 step 3 ("from the `Keywords:` lines") literally and matches
    `^Keywords:` per physical line.

**Result.** Either the whole block is reported as "missing Keywords", or only the first
line's keywords reach the index. The second line's terms, often the case names, are
dropped silently.

Index entries go missing with no error. That produces exactly the "couldn't find it"
failed lookups SM-4 is meant to drive to zero.

`Sources:` has the same problem, but only its presence is counted, so the damage is
just a false warning.

**Tightened rule (AD-4):**
> - `Keywords:` and `Sources:` are plain labels (not bold, not a list item) at column 0.
> - Each is one paragraph: the value runs to the next blank line, and soft line breaks
>   are joined.
> - Terms are split on `;` only, so a term may not contain `;`.
> - The parser accepts an optional `**…**` around the label and reports any H3 whose
>   label it cannot find.
> - `None:` and `TODO:` Sub-points are exempt from both lines and from the "missing" count.

## H4 — Practice Paper "covers" is decided in one place and recorded nowhere (high)

**Pair.**
- **Paper Session (`pcp-m`)**
  - With no past paper per Subject, it builds `mock-1` from the 2026 Sample Questions
    (FR-9).
  - It has 14 Probate and Conveyancing questions, 1 Employment question, and nothing
    on PIPD or Muslim Family.
  - Its hand-over says "Subjects covered: 0, 1, 3".
- **Main Session, next day, starting cold**
  - Per AD-8 it sets `p: 2` for 0, 1, 3 and writes `full["pcp-m"] = {id, name, s: 1}`.
  - The Tracker entry has no field for covered Subjects.
  - When the `s: 2` write comes days later, it must re-derive "covered" to set `n: 2`.
    That information exists only in a hand-over report that is no longer in context,
    or in `drills.md`, which AD-8 doesn't require to hold it.

**Result.**
- One Employment question earns Employment "Practice reviewed". That inflates SM-2.
- PIPD silently never reaches `p: 2`.
- `s: 2` may bump a different set of Subjects than `s: 1` did.

**Related gaps.**
- **Join key:** nothing says the Tracker entry's `id` equals the PP ID (`pyp-2023`).
- **Legacy entry:** eth-w already has a `full` entry at "done" for an unknown paper
  (`drills.md`). AD-8 gives its `s` a new meaning ("sat with a freshly built pack"), and
  FR-11 says nothing counts as reviewed as of 2 Nov. A Main Session could read the legacy
  entry as `s: 1` and set `p: 2`.

**Tightened rule (AD-8):**
> - A PP's record in `drills.md` has a `Covers:` line listing Subject indexes.
> - A Subject is covered only if the PP gives it at least one full written question
>   (Written), or at least 20% of the questions and at least 5 questions (MCQ).
> - The Tracker entry is `{id: <PP ID>, name: "<PP ID> · covers 0,1,3", s}`.
> - Both Tracker writes use that `Covers:` list.
> - Entries whose `id` is not `pyp-*` or `mock-*` are legacy and drive no `p`/`n` value.
>   The Main Session asks Bennett once what to do with them.

## H5 — No legal "covered elsewhere" state; Notes 1 has no mechanical test (medium-high)

**Pair (one Pre-write answers two Sub-points, as eth-w-0-1 already does).**
- **Session A** copies the Pre-write under both H3s.
  - The pack doubles in size (SM-C1).
  - A later Weak Spot fix lands in one copy only, which is the two-masters drift that
    AD-1 forbids within a single file.
- **Session B** writes `None: covered by eth-w-0-1` under the second H3.
  - AD-2 allows `None: <reason>`.
  - But `None` means "nothing to write", and FR-11 Notes 1 requires every Sub-point to
    have its Pre-write. The Main Session can't tell whether B's Subject is at Notes 1.

**Skeleton drift after Notes 1.**
- AD-2 has the skeleton written first, and FR-10 fixes add Sub-points (a failed lookup
  for a topic nobody listed).
- A session adds an H3 with `TODO:` to a Subject already at `n: 1`. The Tracker now
  overstates progress.
- No rule says whether the level falls back or whether the addition must arrive complete.

**Tightened rule (AD-2 + AD-3):**
> - An H3 is in exactly one of four states:
>   1. content;
>   2. `See: {#<id>}` (covered by another Sub-point; the build checks that the target
>      exists);
>   3. `None: <reason>` (deliberately not covered);
>   4. `TODO: <what>`.
> - **Notes 1** for a Subject is true when the build reports 0 `TODO:` lines (excluding
>   `TODO: verify`) for it. The Main Session uses that count, not judgement.
> - Once a Subject is at `n ≥ 1`, a new H3 arrives with content in the same edit, never
>   as a `TODO`.

## H6 — Flowchart leaves link to H3s only by title text, and IDs may be invisible in the PDF (medium)

**Pair.**
- **MCQ Session.** Per AD-5, its chart leaves are Sub-point *titles*. AD-3 then lets it
  reword an H3 title, because "the ID is the key".
- **Script author.** AD-6 step 2 says to anchor `{#id}` but doesn't say whether to strip
  it from the visible heading. The author strips it to keep the TOC tidy.

**Result.**
- In the exam, Bennett follows a chart to a leaf label that no longer matches any
  heading, and a phrase search fails.
- Weak Spots and Question Bank entries cite IDs that appear nowhere in the PDF.
- Mermaid output usually loses links, so the chart can't carry the link either.

**Tightened rule (AD-5 + AD-6):**
> - Each chart leaf label ends with the ID tail in parentheses, e.g.
>   `"Deemed consent (0-12)"`.
> - The build:
>   - renders the ID tail visibly in each H3 (e.g. `Deemed consent · 0-12`);
>   - checks that every leaf tail exists under that H2.
> - Searching for `0-12` then always finds the block.

---

## Lower-risk holes (one line each)

- **Split Sub-points.** AD-3 covers drop and retire, but not split. Rule: the original
  ID stays with the part that keeps the original title. The other part gets the next `n`.
- **Retired-ID reuse.** "Next `n`" is invisible once a dropped H3 is deleted. Rule: leave
  `<!-- retired: clk-m-0-12 -->` in place. The build counts it for duplicate and
  next-`n` checks.
- **Dangling references.** Nothing checks that IDs cited in `weak-spots.md` or
  `question-bank.md` exist. Rule: the build warns on unknown or retired IDs found in
  working files.
- **`TODO:` vs `TODO: verify` counts.** AD-6 doesn't say whether the first count
  includes the second. Rule: the counts are disjoint.
- **Parallel builds.** A block can be prepared the day before, so two sessions may build
  at once. Rule: the script uses `mkdtemp`, never fixed temp names.
- **A second Tracker writer.** Bennett can edit the tracker page, and a stale browser can
  win on `updated` (SCHEMA "Off-store state"). AD-7 calls the Main Session the "only
  writer". Rule: the page is a sanctioned second writer (it is Bennett's word). The Main
  Session never writes from remembered state, always reads fresh, and pins `if_version`.
  It already does most of this; say so in AD-7.
- **drp-w mixes block bodies.** Subject 0 uses I-CRUPAC; Subject 1 uses Template
  guidance. AD-4 picks the body by Subject, not Paper. State "by Subject" explicitly.
  The build should not expect a mermaid fence in drp-w.

## Not holes (checked and fine)

- **Single-digit glob `[0-9]-*.md`.** The maximum Subject index is 4 (pcp-m), so this is
  safe.
- **Cross-paper ID collisions.** These are impossible because of the paper prefix.
- **Ownership of `tools/` vs Paper Sessions.** This is clean. A session that hits a
  parser bug hands it to the Main Session and doesn't patch the script.
- **AD-1's single master.** It holds, once H5's `See:` state removes the reason to copy
  Pre-writes.
