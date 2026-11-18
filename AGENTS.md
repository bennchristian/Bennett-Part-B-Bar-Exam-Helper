# AGENTS — who does what

## Roles

| Role | Model | Does | Never does |
|---|---|---|---|
| **Bennett** | — | Decides the study order and block lengths, sits practice papers, says what is done | — |
| **Main session** (coordinator) | Opus | Reads the tracker each day, says what today's block needs, starts and briefs paper sessions, checks their output, records progress in the tracker on Bennett's word. Sole owner of the tracker, `tools/` and git commits (ARCHITECTURE AD-7, AD-8) — may delegate `tools/` work to a session it briefs | Writes long study notes itself; starts a paper session Bennett didn't ask for; pushes without Bennett saying so |
| **Paper session** (one per paper ID) | Opus; Sonnet for pure extraction | Builds the Paper's `study/<paper-id>/` set per `PRD.md` §4 and §7 — **Phase 1 (done):** Coverage List, then a Cheatsheet per Topic with its end points (MCQ) or Pre-writes (+ Templates) (written), as Markdown only, checked with `build_pack.py <paper-id> --check`, built to serve Bennett's workflow in `PRD.md` §2.2. **Phase 2 (done 18 Nov; now maintenance — every Markdown fix gets a rebuilt, versioned PDF):** PDFs, Model Q&A, PYP coverage/Question Bank, Drills, Practice Paper, Weak Spots | Makes a PDF, Model Q&A, Drill or PYP coverage check in Phase 1; touches another paper's folder; writes to the tracker; edits `Bar Exam/` |
| **Extraction subagent** | Sonnet / Haiku | Bulk-reads PDFs/DOCX for a paper session and returns condensed, cited excerpts | Writes files; gives legal conclusions |

Paper sessions are named by paper ID (`eth-w`, `clk-m`, …) so the main session and the
tracker share one vocabulary. At most one paper session per paper.

## Brief format for a paper session

Every brief is self-contained and includes: the paper ID and its subjects (from
`SCHEMA.md`), the study block dates and exam date, the reading order (`CLAUDE.md` →
`PRD.md` → `RULES.md` → `SCHEMA.md` → `ARCHITECTURE.md`), the source folders under `Bar Exam/` for that paper
in source order (module folder; then Cyril's `Stuff/<module>`, `For exam/finalised
muggers/<module>` and `For exam/Exam files/<paper>`; then Nic's `3. PYP` and
`4. Nic Exam Go Pack` for past papers and fallback), what already exists in
`study/<paper-id>/`, the tracker's current progress for that paper, which PRD §7 items
the block must reach, and the required final report (below).

A brief that assumes the session shares this conversation's context is the usual failure —
the session starts cold every time.

## Phase gating

Study blocks follow the tracker's `order` and `days` (as of 6 Nov 2026):

| Block | Dates | Paper |
|---|---|---|
| 1 | 29 Oct – 3 Nov | `eth-w` |
| 2 | 4 – 6 Nov | `clk-m` |
| 3 | 7 – 12 Nov | `drp-w` |
| 4 | 13 – 15 Nov | `drp-m` |
| 5 | 16 – 21 Nov | `pcp-w` |
| 6 | 22 – 24 Nov | `pcp-m` |
| 7 | 25 – 27 Nov | `ccp-2` |
| 8 | 28 – 30 Nov | `ccp-1` |

The tracker is the source of truth; if Bennett re-orders it there, this table is stale —
re-read the doc. A paper session for a block normally starts on the block's first day; the
next one can be prepared the day before. Both phases are done (18 Nov); a block's job is now practice and
pack fixes. A block that ends with its uncuttable Phase 1 items unfinished runs on, and the time comes out of the next block's
lower-priority items (PRD §5). Exam week (1–11 Dec) switches every session to timed
practice and weak-spot fixes only.

## Handover

A paper session ends each turn with: what it added or changed in `study/<paper-id>/`
(paths), Coverage List status per Subject (Sub-points covered / total), which PRD §7
items are done, the `--check` result, (Phase 2 only) Drill and Practice Paper results, Weak Spots and their fixes, any open
`TODO: verify`, and the tracker level each Subject now meets under PRD FR-11. The main
session checks the files exist, then asks Bennett before recording progress in the
tracker.

<!-- bmad:context -->
<!-- bmad-project-context manages this block. Run it once the repo has real code to scan;
     it path-checks every claim it writes, so running it against an empty repo produces
     guesses or nothing. Everything above these markers is preserved across its runs. -->
<!-- /bmad:context -->
