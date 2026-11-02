---
review: reconcile
target: ../ARCHITECTURE-SPINE.md
inputs: [PRD.md, prds/.../addendum.md, SCHEMA.md, AGENTS.md, RULES.md, .memlog.md, study/eth-w/ (current state)]
date: 2 Nov 2026
verdict: sound substrate, not yet buildable against — fix R1–R4 before promoting to ARCHITECTURE.md
---

# Reconcile review — Architecture Spine vs PRD, addendum, SCHEMA, AGENTS, RULES

**Verdict.** The pipeline (Markdown master → generated PDF), the one-file-per-Subject layout
and the Sub-point ID key are sound and cover most of the PRD. Four gaps would bite in the next
week: the existing `eth-w` files do not fit the new layout and their IDs collide with AD-3;
the build has no owner or date although an uncuttable item depends on it; the PRD's "no new
tools" non-goal is contradicted without a recorded amendment; and the build cannot check the
two uncuttable coverage items (§7 items 1–2). The rest are smaller slot or wording gaps.

Severity: **High** = blocks or contradicts a binding requirement; **Med** = a requirement has
no home in the spine; **Low** = wording or a dropped memlog decision.

## 1. Findings

### R1 (High) — The `eth-w` migration is missing, and AD-3 collides with existing IDs

- **Evidence.** `study/eth-w/` already holds `coverage.md` (76 Sub-points keyed `I.1`, `II.8`…),
  `prewrites.md` (34 Pre-writes `### eth-w-0-1 — …`), `question-bank.md` (QB rows citing
  `II.8, II.12`…), `weak-spots.md` (keyed to `coverage.md` numbers) and a built
  `reference-pack.pdf`. In those files, `eth-w-0-1` is a *Pre-write* ID that covers two
  Sub-points (II.1 and II.2).
- **Contradiction.** AD-3 makes `<paper>-<subject#>-<n>` the *Sub-point* ID, "never renumbered
  or reused", and says working files refer to Sub-points only by that ID. Adopting AD-3 in
  `eth-w` means either reusing `eth-w-0-1` with a new meaning (breaking AD-3's own rule) or
  renumbering. AD-2 says "there is no `coverage.md`", but one exists. The Raw material row
  only covers `outline.md`.
- **Format drift.** The existing files use `*Keywords: …*` and `*Source note: …*` (italic);
  AD-4 and the AD-6 parser expect `Keywords:` and `Sources:`. The existing "Opening line /
  Closing line for any answer" are Subject-level Pre-writes with no H3, and `coverage.md`
  counts Sub-point I.2 as covered by the closing line. AD-2 has no slot for them.
- **Fix.** Add an AD (or a Structural Seed note) "Migrating pre-spine files": `eth-w` is
  converted to `0-ethics.md` with Sub-point IDs allocated fresh from the `coverage.md` order.
  Old Pre-write IDs are recorded once as aliases in a migration table (or retired), and QB and
  Weak Spot rows are rewritten to the new IDs. `coverage.md` and `prewrites.md` become raw
  material like `outline.md`. Either allow one optional Subject-level block under H1
  ("Stock lines"), or make the opening and closing lines a Sub-point. State when this happens:
  Block 1 ends 3 Nov, and PRD §7 says `eth-w` Pre-writes are finished during Block 2.

### R2 (High) — `tools/build_pack.py` has no owner or date, but uncuttable item 3 depends on it

- **Evidence.** PRD §7 item 3 (uncuttable) is a Practice Paper "sat with its Reference Pack",
  and AD-1/AD-6 make the pack exist *only* through `tools/build_pack.py`. `tools/` does not
  exist yet. The memlog's open question ("must exist before first Practice Paper, clk-m
  ~6 Nov; owner: main session decides") was dropped from the spine. Deferred lists only the
  script's internals.
- **Fix.** Add to Deferred or AD-6: the owner (the Main Session, or a session it starts), a
  deadline (before the first Practice Paper, around 5 Nov), and a fallback if it is late
  (plain `make-pdf --toc` over the concatenated pack files, with no index). PRD cut item 5
  already makes that degraded pack acceptable.

### R3 (High) — PRD §6 says "Not building new apps or tools"; the spine builds a tool

- **Evidence.** PRD §6 is explicit: "Not building new apps **or tools**. The existing Tracker
  and PDFs are the only interfaces." AD-6 creates `tools/build_pack.py`. The memlog records
  Bennett adopting it and reasons that it is "a build step not an app", but the spine itself
  carries no ruling. The PRD is the scope contract (RULES.md Process rules), so a downstream
  session reading the PRD sees a violation.
- **Fix.** Ask Bennett to amend PRD §6, for example: "No new apps or user-facing interfaces;
  a local build/check script for the Reference Pack is in scope." Or cite his 2 Nov ruling
  in AD-6 and add `PRD §6` to its Binds. RULES.md KISS ("No tooling 'for later'") needs the
  same carve-out (see §3).

### R4 (High) — The build cannot measure the two uncuttable coverage items

- **FR-1 / §7 item 1.** "Every Topic … has a Flowchart, **or an explicit reason why it does
  not**." AD-5 puts a fence under each MCQ H2, but there is no Topic-level `None: <reason>`
  (AD-2's `None:` is per H3 only). AD-6 step 6 does not count H2s that have neither a fence
  nor a reason.
- **§7 item 2.** "Pre-writes for every Sub-point the past-year papers have tested" needs a
  join of Question Bank tier 1 against Sub-points that still read `TODO:`. Nothing produces
  it. The `eth-w` `coverage.md` "Tested" column did this job by hand, and AD-2 deletes it.
- **Fix.** (a) Allow `None: <reason>` directly under an H2 in place of the fence, and have
  AD-6 step 6 report "Topics without Flowchart or None" for MCQ Papers. (b) Have AD-6 step 6
  read `question-bank.md` (if present), take tier-1 Sub-point IDs, and report those whose H3
  still holds only `TODO:`. That is item 2's checklist. Both are counts, so they stay
  within the "check command" role.

### R5 (Med) — FR-10 "index or contents fix" cannot exist under AD-1

- **Evidence.** The Weak Spot convention lets `fix` be `index` or `contents`. Under AD-1 and
  AD-6, both are generated. An index fix can only be a change to some Sub-point's `Keywords:`
  line, and a contents fix only a heading change. FR-10 also says each Weak Spot *links to*
  the entry changed; a bare word `index` links to nothing.
- **Fix.** `fix` is always a Sub-point ID plus what changed: `keywords`, `heading`, `body`,
  `chart` (for the H2 fence, use the Topic's first Sub-point ID or add Topic IDs), or `new`.
  Drop bare `index` / `contents`.

### R6 (Med) — FR-7 contents depth and the no-link fallback are not pinned down

- **Evidence.** FR-7 requires contents "organised Subject → Topic → Sub-point", linking to
  pages. AD-6 step 4 says only "`make-pdf --toc`". It does not say the TOC must go to H3
  depth, or that the `{#id}` suffix and the index section are handled in it. The memlog
  records that the TOC shows **no printed page numbers** and assumes the reference-device
  viewer supports internal links. The index gets a printed "p N" fallback; the contents page
  gets none.
- **Fix.** In AD-6, state: TOC depth = H1–H3, with the `{#id}` stripped from TOC text.
  Either print "p N" in the contents on the second pass (the same mechanism as the index), or
  record the link-only contents as an accepted risk tied to PRD Q1 (reference device).

### R7 (Med) — Smaller requirements with no slot

- **FR-5 common mistakes and whole-document skeleton.** AD-4's Written Advocacy body is
  "guidance for that part". FR-5 also needs the document's annotated skeleton and its common
  mistakes, and there is no H2-level slot for either. Fix: a WA H2 may carry the skeleton (and
  a `Common mistakes:` block) before its H3s.
- **FR-8 recorded conflict.** "records the conflict" has no place in AD-4. Fix: an optional
  `Conflict:` line inside or after `Sources:`.
- **FR-2 cue searchability.** AD-5 gives "phrase search failing on wrapped chart labels" as
  the reason to move answers out of charts, but the cues stay *only* in chart nodes, so a
  wrapped cue label can still fail Ctrl-F. Fix: each Sub-point's `Keywords:` also carries its
  question cues, or cue labels are kept short enough not to wrap.
- **FR-11 Notes 1 / Practice 1.** AD-8 covers the two Practice Paper writes only. Fix: one
  line stating Notes 1 = the build reports zero `TODO: <what>` for that Subject (and saying
  whether `None:` counts as covered), and Practice 1 = a `D-<n>` covering the Subject is
  marked in `drills.md`.
- **FR-11 reset.** "As of 2 Nov 2026 no Subject counts as reviewed" is a one-off Tracker write
  (any `n: 2` / `p: 2` → 1) that nothing schedules. Fix: note it under AD-8 as a migration
  that needs Bennett's word.
- **AD-8 edge.** A Subject whose `n` reaches 1 *after* its paper's `s: 2` write never gets
  `n: 2`. Fix: also set `n: 2` when Notes 1 is recorded for a Subject already covered by an
  `s: 2` paper. Also state what `full` `id` holds (the `pyp-<year>` / `mock-<n>` ID) and
  what `s: 0` means (planned, not sat), or that it is unused.

### R8 (Low) — Dropped memlog decisions and wording

- **Rebuild triggers** (memlog: rebuild at the end of any turn that changed pack files, and
  before a Practice Paper). Only the second survives, in the AD-8 diagram. Add both to AD-6
  or AD-1.
- **"Never run against another paper by a paper session"** (memlog). AD-7 implies it but
  does not say it; add it to AD-7 for paper sessions.
- **Aliases vs FR-1/FR-4.** FR-1/FR-4 say "file path under `Bar Exam/`"; the spine allows
  aliases resolved in `sources.md`, which is outside the pack. That is fine (sources are not
  used in the exam), but say so in the conventions row so it is not read as an FR-4 breach.
- **Per-proposition sources.** FR-4 requires a source for *every proposition*; AD-6 checks
  only that a `Sources:` line exists. Acceptable, but note it so nobody treats the build
  report as SM-5 proof.
- **AD-4 has no `[ADOPTED]` tag** while every other AD does. Confirm with Bennett or tag it.
- **`.gitignore`**: AD-1 says "The PDF is git-ignored", but `.gitignore` lists only
  `Bar Exam/` and `.DS_Store`.

## 2. Checked and not a gap

- **FR-4 source note not retyped / prose only / labels not retyped.** AD-4 puts `Keywords:`
  before and `Sources:` after the body, so both stay outside the retyped prose. The prose,
  length and citation form stay in RULES.md (Deferred, correctly).
- **"Coverage List before charts" (FR-1, RULES).** AD-2's skeleton-first rule covers it.
- **Block overrun, exam-week "fixes only, no new Topics".** These are process rules that
  belong in AGENTS.md / RULES.md, and they are already there. The spine's Deployment row
  covers the exam-week rebuild and re-copy. Optional: the build could warn about new H2s
  after 30 Nov, but this does not need an AD.
- **Licensed material / condense.** `Bar Exam/` is read-only (AD-7) and the PDF stays local.
  Condensing is a content rule (RULES.md). Committing `study/` is correctly left to Bennett.
- **Exam integrity, marking rules, source order.** These are content and process rules;
  RULES.md owns them.
- **FR-6 Question Bank format, SM-5 `TODO: verify` count, offline pack (FR-2/FR-7)** are all
  covered.

## 3. Implied edits to other docs (the spine does not make these)

### SCHEMA.md

1. "Study outputs" table: drop "**Interim layout**" and the PRD Q5 hedge, and point to the
   spine/ARCHITECTURE.md.
2. Replace rows `coverage.md`, `prewrites.md`, `templates.md`, `flowcharts.md` with
   `<subject#>-<slug>.md` (all Papers; H1 Subject / H2 Topic / H3 Sub-point; Pre-writes,
   Templates or Flowchart + end points; the Coverage List *is* the heading skeleton). Delete
   the `flowcharts.md` "TODO: confirm format" line.
3. Add `sources.md` (optional alias key, outside the pack) and note `outline.md` plus the
   pre-spine `coverage.md` / `prewrites.md` (`eth-w`) as raw material.
4. `reference-pack.pdf`: generated by `tools/build_pack.py <paper-id>`, never hand-edited,
   git-ignored. Add `tools/build_pack.py` to the Entity overview.
5. ID section: the Sub-point ID `<paper>-<subject#>-<n>` is written as an H3 suffix `{#id}`,
   is never renumbered or reused, and is the only key in working files. It is no longer a
   "Pre-write / Flowchart ID".
6. Entry formats for `question-bank.md` (QB-n…), `weak-spots.md` (WS-n…, with the R5 `fix`
   form) and `drills.md` (D-n / `pyp-<year>` / `mock-<n>`).
7. Tracker `full` row: `id` = `pyp-<year>` / `mock-<n>`; `s: 1` = sat and marked (covered
   Subjects `p: 2`); `s: 2` = Weak Spots fixed and pack rebuilt (covered Subjects with
   `n ≥ 1` → `n: 2`); define or retire `s: 0`. `subj` row: Notes 1 = zero `TODO:` in the
   build report for that Subject.
8. Migrations: add the one-off 2 Nov "nothing reviewed" reset (FR-11) and the `eth-w`
   ID migration (R1).

### RULES.md

1. Flowcharts bullet: the chart runs cue → Sub-point title only; the rule/answer and its
   source live in the H3 `End point:` / `Sources:` (it currently says "end at the rule or
   answer with its source"). Add: about 12 nodes at most, split under a bold label; labels
   double-quoted; fence at column 0; `None: <reason>` under an H2 that gets no chart.
2. Coverage List first: "= the H2/H3 skeleton of the pack file, written before content; no
   separate `coverage.md`."
3. Cite the source: a `Sources:` line per Sub-point; a full `Bar Exam/` path *or* an alias
   defined in `study/<paper-id>/sources.md`; an optional `Conflict:` line for FR-8.
4. New: the Markdown is the master copy; never edit the PDF; every fix (Weak Spots included)
   is a Markdown edit then a rebuild. Rebuild at the end of any turn that changed pack files,
   and before any Practice Paper.
5. Process rules: replace "No check command exists yet … TODO" with
   `python3 tools/build_pack.py <paper-id>` as the check command (non-zero exit on a diagram
   render failure or a duplicate ID).
6. Principles / KISS: carve out the build script ("No tooling 'for later'" except the
   Reference Pack build, which PRD §6 now allows; see R3).
7. Exam week: add "rebuild and re-copy the PDF to the reference device after each fix".
8. Data rules: Sub-point IDs are never renumbered or reused (or point to SCHEMA.md).

### AGENTS.md

1. Roles, Paper Session "Does": writes pack files `study/<id>/<subject#>-<slug>.md` per the
   spine, runs `tools/build_pack.py <its id>`; "Never does": edit `tools/`, run the build for
   another paper.
2. Roles, Main Session "Does": owns and maintains `tools/build_pack.py` (with the R2
   owner/date); makes the two AD-8 Tracker writes and the FR-11 reset on Bennett's word.
3. Brief format: add `ARCHITECTURE.md` (the promoted spine) to the reading order
   (`CLAUDE.md` → `PRD.md` → `RULES.md` → `SCHEMA.md` → `ARCHITECTURE.md`), and for `eth-w` /
   `clk-m` name the migration step (R1).
4. Handover: Coverage status = the build report's per-Subject counts (Sub-points, `TODO:`,
   `TODO: verify`, missing Keywords/Sources, Topics without a chart, tier-1 Sub-points still
   `TODO`); Practice Paper ID (`pyp-<year>` / `mock-<n>`) and the Tracker write it asks for
   (`s: 1` or `s: 2`); Weak Spot IDs with their `fix` Sub-point IDs.
5. Extraction subagent: "condensed, cited excerpts" is already correct; no change.

### Outside the three docs (for completeness)

- `.gitignore`: add `study/*/reference-pack.pdf` (AD-1).
- `PRD.md` §6: the amendment in R3 (Bennett's call). §9 Q5 can be marked resolved by the spine.
- `CLAUDE.md` header: `ARCHITECTURE.md` stops being TODO once the spine is promoted.
