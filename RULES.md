# RULES — Part B Bar Exam Helper

Most of this repo is study content, not code. Where code does appear (the tracker page,
helper scripts), the principles apply; the study rules apply to everything.

## Principles

1. **SOLID.** One responsibility per file and per function. Depend on small named helpers,
   not on incidental structure that can shift underneath you.
2. **DRY at 4.** Extract a shared helper only when the same logic appears 4 or more times.
   Below that, repetition is acceptable and clearer — the wrong abstraction couples callers
   that had no reason to be coupled, and costs more to unwind than the duplication cost to
   tolerate. For study notes this means: repeat a rule in two outlines rather than building
   a cross-reference web.
3. **KISS.** Ship the simplest thing that helps Bennett pass. No tooling "for later".

## Exam integrity (non-negotiable)

- Course Handbook §7.11–7.13: no AI assistance during any examination, quiz, mock exam or
  other assessment under exam conditions. If a request looks like a live assessment (a
  timed quiz open now, the Mock Exam, a compulsory online quiz), stop and say so. Practice
  papers Bennett sits for self-study and then brings for marking are fine.
- Do not complete or answer the compulsory online quizzes.

## Study-content rules

What to build, in what priority, and what counts as done is in `PRD.md` (§4 features,
§7 cut order, FR-11 tracker levels). These rules govern how it is written.

- **Source order (PRD FR-8):** Course Materials (`Bar Exam/Modules/`) win on any point of
  law → Cyril's notes (`Bar Exam/Seniors Notes/Cyril - Part B/`, last year's sitting) →
  Nic's package, only when needed. A conflict with the Course Materials is followed
  their way and recorded, never resolved silently.
- **Cite the source** for every legal proposition: file path under `Bar Exam/` and page
  or slide. Unsourced law is worse than a gap — mark it `TODO: verify`.
- **Pre-writes (Written Papers `drp-w`, `eth-w`, `pcp-w`):** I-CRUPAC — Issue,
  Conclusion, Rule, Proof/Precedent, Application & analysis, restated Conclusion. Prose
  only, no bullets (the exam does not allow them); about 150–300 words, so it can be
  retyped in ~5 minutes (pasting is not allowed). In the text: cases by name in brackets
  with the paragraph number where the sources give one, statutes by section. Never cite
  lecture notes or slides as authority. The `Bar Exam/` path and page go in a source
  note under the Pre-write, which is not retyped. Application is a pattern (trigger facts
  and how to apply), not a worked answer.
- **Flowcharts (MCQ Papers):** one per Topic. Start from question cues, branch to the
  Sub-point, end at the rule or answer with its source. Labels are text, not images, so
  Ctrl-F finds them. Correct and clear beats pretty.
- **Coverage List first:** a Subject's Topics and Sub-points are listed from its
  syllabus, learning plan and Course Materials before any Pre-write or Flowchart.
- **Marking:** written answers on I-CRUPAC structure, accuracy and Sub-point coverage;
  MCQs with why the right option is right and each wrong one is wrong. Pass marks are not
  50% (Handbook §7.5).
- **Examinable scope only** — the subjects in `SCHEMA.md`. Litigation Technology, Law &
  Society and Professional Skills get no study time unless Bennett asks.
- **Exam week (1–11 Dec):** fixes to existing Pre-writes, Flowcharts and index only; no
  new Topics.
- Don't reproduce course materials wholesale into `study/`; condense.

## Data rules

- `Bar Exam/` is read-only. Never edit, move or rename files there.
- The tracker doc is Bennett's record. Write to it only to record something Bennett has
  confirmed, at the level meanings in PRD FR-11; always pin `if_version` from a fresh
  read and set `updated`.
- Field contracts in `SCHEMA.md` are fixed; add fields at the end and update `SCHEMA.md`
  in the same change.

## Process rules

- Before any implementation, the eight context files exist and are current: CLAUDE, AGENTS,
  ARCHITECTURE, DESIGN, PRD, RULES, SCHEMA, SKILLS.
- `PRD.md` is the scope contract. Work outside it stops and asks rather than widening.
- Check command: `python3 tools/build_pack.py <paper-id>` (ARCHITECTURE AD-6). Exit 0 =
  built; 1 = a coverage/format check failed and the old PDF was kept; 2 = bad paper ID or
  missing tool. Run it at the end of any turn that changed `coverage.md` or a content file,
  and before every Practice Paper.
- Keep an explicit resolved/unresolved list when auditing; never imply a pass fixed more
  than it did.
- `Bar Exam/` stays out of git (`.gitignore`): it is licensed course material and far past
  GitHub's file-size limits.

## Prefer enforcement over prose

A rule a linter, formatter, type checker, or CI check can enforce belongs there instead of
here. When a rule above becomes mechanically enforced, delete it from this file.
