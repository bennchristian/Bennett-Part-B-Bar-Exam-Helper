# SCHEMA — Part B Bar Exam Helper

No database in this repo. The one structured store is the **Part B tracker** artifact's
per-user document, plus files on disk. Both are described below as they exist on 2 Nov 2026.

## Entity overview

```
Paper (8, fixed) ──< Subject (by index)          ← defined in the tracker's page code
  │
  └── tracker doc: order, days, subj progress, full practice papers, notes
Admin task (6, fixed)  ── tracker doc: tasks{id: done}
Paper ──> study/<paper-id>/  (notes the sessions write)
Paper ──> Bar Exam/ sources  (read-only course library)
```

## Paper IDs

The key for everything. Defined in the tracker page (`PAPERS`); every exam is 2:30–4:30pm.

| ID | Paper | Exam | Subjects (index order — `subj` keys depend on it) |
|---|---|---|---|
| `drp-w` | DRP written | Tue 1 Dec | 0 Civil Litigation · 1 Written Advocacy |
| `drp-m` | DRP MCQ | Wed 2 Dec | 0 Arbitration · 1 Mediation Advocacy |
| `eth-w` | ETH written | Thu 3 Dec | 0 Ethics & Professional Responsibility |
| `pcp-w` | PCP written | Mon 7 Dec | 0 Criminal Litigation · 1 Family Law Practice |
| `pcp-m` | PCP MCQ | Tue 8 Dec | 0 Probate · 1 Real Estate (Conveyancing) · 2 Muslim Family & Succession · 3 Employment · 4 PIPD |
| `ccp-1` | CCP MCQ 1 | Wed 9 Dec | 0 Banking & Fundraising · 1 Corporate Governance · 2 Insolvency · 3 Admiralty |
| `ccp-2` | CCP MCQ 2 | Thu 10 Dec | 0 IP · 1 M&A · 2 Competition · 3 Taxation |
| `clk-m` | CLK MCQ | Fri 11 Dec | 0 Data Protection & Cyber · 1 Law & Tech · 2 Comparative Laws · 3 Conflict of Laws |

Non-examinable (Course Handbook §3.1, quiz only): Litigation Technology, Law & Society, all
of Professional Skills. They are deliberately absent above.

## Tracker document

Artifact: <https://claude.ai/artifact/QKBF5HvcsMUjirCfmZAMzK> (capabilities `db`, `user`).
Path: collection `data/users/me`, doc `tracker` — private to Bennett's account. Read/write
from a session with the `ArtifactData` tool.

| Field | Type | Meaning |
|---|---|---|
| `v` | `1` | Schema version |
| `order` | `PaperID[]` | Study order. Blocks run back-to-back from Thu 29 Oct |
| `days` | `{PaperID: 1–14}` | Days per block. Total should be 33 (29 Oct–30 Nov) |
| `subj` | `{"<PaperID>\|<i>": {n: 0–2, p: 0–2}}` | Per subject: notes / practice, 0 not yet · 1 done · 2 reviewed — what each level requires is PRD FR-11 |
| `full` | `{PaperID: [{id, name, s: 0–2}]}` | Practice Papers: `{id: pyp-<year>\|mock-<n>, name: "<id> · covers <subject#s>", s}`. `s: 1` = sat and marked, `s: 2` = Weak Spots fixed; entries with other IDs are legacy and set no levels (ARCHITECTURE AD-8) |
| `notes` | `{PaperID: string}` | "Notes to self" free text |
| `tasks` | `{taskId: bool}` | Admin checklist: `docs`, `eth1`–`eth3`, `ethclose`, `quizzes` |
| `updated` | epoch ms | Last-write timestamp; the page keeps whichever of local/account copy is newer |

Progress per paper = sum of all `n`, `p` and `s` values ÷ max (4 per subject + 2 per full paper).

## Study outputs (`study/`)

Written by Paper Sessions, one folder per paper ID. **`ARCHITECTURE.md` is the authority**
on this file set and its formats (AD-1 to AD-5, Consistency Conventions); this table is a
summary only. Terms are as defined in PRD §3.

| File | Papers | Holds | Format |
|---|---|---|---|
| `coverage.md` | all | Coverage List, written first | AD-2 table: `Key` · `Sub-point` · `Tested` · `Covered by` |
| `question-bank.md` | written | Likely questions by Source Tier | `QB-<n>` rows (Conventions) |
| `prewrites.md` | written | I-CRUPAC Pre-writes | AD-4 blocks, IDs per AD-3 |
| `templates.md` | `drp-w` | Written Advocacy Templates | AD-4 blocks |
| `flowcharts.md` | MCQ | Q&A Cheatsheet per Topic plus end-point blocks (file name predates Cheatsheets) | AD-5 + AD-4 |
| `drills.md` | all | Drills and Practice Papers (`pyp-<year>` / `mock-<n>`, `Covers:` line), answers, marks | AD-8 |
| `weak-spots.md` | all | `WS-<n>` rows linked to the content ID fixed | Conventions |
| `model-questions.md` | all | Practice questions by Subject → Topic (Written: by paper, facts then parts; ARCHITECTURE AD-6), tag line `**Q…** · `Key` · source · `end-point ID``, answer and cite under each | as is |
| `model-questions.pdf` | all | Generated second exam-day file: contents linked to Topics, Keywords per question, answer under it | `python3 tools/build_pack.py <paper-id> --questions` |
| `reference-pack.pdf` | all | Generated — never hand-edited | `python3 tools/build_pack.py <paper-id>` (AD-6) |
| `outline.md` | `eth-w`, `clk-m` | Pre-PRD outlines, kept as raw material | as is |

## Off-store state

- **Browser `localStorage`** key `partb-tracker-v1` — a copy of the tracker doc per browser.
  The page reconciles it with the account copy by `updated`, so a stale browser can
  overwrite a newer session write if its clock is ahead. Write `updated: Date.now()`.
- **`Bar Exam/`** (git-ignored, ~1.6 GB, 911 PDFs, 134 DOCX, 7 MP4) — the source library:
  `Admin/` (handbook, code of conduct, opening brief), `Modules/<module>/<subject>/`,
  `Sample Questions/`, `Seniors Notes/` (Cyril's notes: `Stuff/` per-module materials,
  `For exam/finalised muggers/` per module, `For exam/Exam files/` his 2025 exam-day
  files per paper; Nic's package: 2018–2025 past papers (no 2024; index in `3. PYP/PYP index.md`) and an exam go-pack),
  `Bar Dump.docx`, `BENNETT_S BAR PROGRESS.xlsx`.
- **Hard-coded in the tracker page**: paper list, subject lists, exam dates, admin tasks,
  start date. Changing any of these means republishing the artifact, not writing the doc.

## Access control

The `data/users/<uid>` subtree is private to that user by the artifact runtime. The artifact
itself is private. No other access rules exist.

## Migrations

None. If `PAPERS` subject order ever changes, `subj` keys (`<id>|<index>`) silently point at
the wrong subject — remap them in the same change.
