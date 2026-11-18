@AGENTS.md

# Part B Bar Exam Helper — project guide

Keep this file current and short: after every change, remove anything stale and fold new
facts into the sections below. It is the handover; nothing else is.

**Read these first — they are the contract, this file is the running commentary:**
`PRD.md` (scope, features, cut order, tracker levels — final 2 Nov) · `ARCHITECTURE.md`
(`study/` file formats, builder, write ownership, tracker writes — final 2 Nov) · `SCHEMA.md` (paper IDs, tracker doc, `study/` layout) ·
`DESIGN.md` (TODO, `bmad-ux`) · `RULES.md` (exam integrity, source order, I-CRUPAC,
Cheatsheet rules) · `AGENTS.md` (main session vs paper sessions, block schedule) ·
`SKILLS.md` (which skill wins which job). Anything below that contradicts them is stale and
should be fixed here, not there.

## 1. What this is

Bennett is sitting the 2026 Part B (Session 2) Singapore Bar Examinations: eight two-hour
papers, Tue 1 – Fri 11 Dec 2026, all 2:30–4:30pm, open book with a second reference
device. This repo is the workspace: one **main session** coordinates, and one **paper
session** per paper builds a searchable Reference Pack in `study/<paper-id>/` from the
course library in `Bar Exam/` — a Q&A Cheatsheet per Topic for every paper, then I-CRUPAC Pre-writes
(written papers) or end points (MCQ papers), plus a Model Q&A PDF. Bennett's workflow, which
these outputs serve (PRD §2.2): he reads the syllabus and learning plan, then Cyril's notes, and studies
alongside the pack and Model Q&A. To look something up he finds the Topic, Ctrl-Fs a keyword, and follows the
Cheatsheet ("framework") to the end point or Pre-write paragraph(s). He uses the Model Q&A to learn
the kinds of question each Topic produces. Progress lives in the **Part B
tracker** artifact (<https://claude.ai/artifact/QKBF5HvcsMUjirCfmZAMzK>), which shows the
33-day study plan, per-subject progress, admin tasks and the exam timetable.

## 2. How to work on it

- **Start of a main-session turn:** read the tracker doc (`ArtifactData` get,
  `data/users/me` / `tracker`), work out today's block from `order` + `days` starting
  29 Oct, and say what that paper still needs.
- **Starting a paper session:** brief it per `AGENTS.md`; name it by paper ID.
- **Phases (`PRD.md` §7):** Phase 1 (Markdown packs) and Phase 2 (PDFs, Model Q&A,
  Practice Packs) are both done for all 8 papers (Bennett, 18 Nov). Bennett practises from
  the PDFs, so any Markdown fix now means: run `build_pack.py <paper-id> --check`, rebuild
  the affected PDF, and save it as the next version beside the old one
  (e.g. `drpm-reference-pack-v2.pdf` → `-v3.pdf`; the builder writes `reference-pack.pdf`,
  so rename it). For `drp-w` use the pack folder, `drp-w-cl` or `drp-w-wa`.
- **Building a Reference Pack (Phase 2):** `python3 tools/build_pack.py <paper-id>` — the only
  builder; paper sessions run it, never edit it. The PDF is generated and git-ignored. `--questions` builds `model-questions.pdf` from
  `model-questions.md` the same way. Every paper gets both PDFs (Bennett, 5 Nov). For `eth-w`, `model-questions.md` is generated:
  run `python3 tools/assemble_eth_questions.py` after changing `model-answers.md`,
  `drills.md` or `pyp-facts.md`, never edit it by hand.
- **Practice Pack (Bennett, 17 Nov):** `python3 tools/build_practice.py <paper-id>` writes
  `study/<folder>/<paper-id>-practice.pdf` (drp-w → `study/drp-w-cl/`, CL + WA merged): contents,
  past papers (2026 SQ, then years newest first, paper order, facts boxed), Drills (every other
  question, timed by Topic), then the answer key. It only rearranges the Model Q&A Markdown — fix
  content there and rebuild. A question counts as past-paper if its tag-line source starts
  `PYP <year>`, `<year> ` or names the Sample Questions.
- **Recording progress:** only on Bennett's word; read the doc, update the `subj` / `full` /
  `tasks` fields, set `updated`, pin `if_version`.
- **Finding sources** (in `RULES.md` source order): `Bar Exam/Modules/<module>/<n.
  subject>/` for course materials; Cyril's `Bar Exam/Seniors Notes/Cyril - Part B/` —
  `For exam/finalised muggers/<module>` and `For exam/Exam files/` (his 2025 exam-day
  file per paper, the nearest model of a Reference Pack); then Nic's
  `.../Nic_s Part B Package/3. PYP/` (2018–2025 past papers, no 2024 — read `PYP index.md` there first for gaps and format changes) and `4. Nic Exam Go Pack/`;
  `Bar Exam/Sample Questions/` for this session's samples. Use `pdftotext -layout` to
  search PDFs.

## 3. Gotchas that cost real time

None recorded yet.

Only observed mistakes belong here — something that actually went wrong, not something that
looks like it might.

## 4. Working with Bennett

- Exams 1–11 Dec 2026; the ETH06 closing session is Tue 10 Nov, 2:30pm.
- Suggest a skill or subagent in one line before non-trivial work; propose, don't
  auto-delegate.
- Mark unknowns as `TODO:` rather than guessing — especially points of law.
