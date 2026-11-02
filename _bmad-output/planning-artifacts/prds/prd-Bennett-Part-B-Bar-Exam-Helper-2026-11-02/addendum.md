# Addendum: Part B Bar Exam Helper PRD

Supporting detail for downstream documents (`ARCHITECTURE.md`, `SCHEMA.md`, `RULES.md`).

## A. Exam format evidence (checked 2 Nov 2026)

Sources: `Bar Exam/Admin/2026_Part_B_Session_2_Opening_Brief.pdf` (slides 43–50),
`Bar Exam/Admin/2026_Part_B_Course_Handbook_(B26S2).pdf` §7.4,
`Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf`.

| Paper | Format seen in 2026 materials |
|---|---|
| `eth-w` | A hypothetical; sub-questions read "Discuss and evaluate…" (12–15 marks each) |
| `drp-w` Civil Litigation | A hypothetical; sub-questions read "Please advise Z…" |
| `drp-w` Written Advocacy | Drafting task; the sample is a letter of demand |
| `pcp-w` Criminal / Family | Hypotheticals; "Advise Mr Loh…", "discuss and explain…" |
| MCQ papers | 60 questions × 4 options, 2 hours; the cover page gives the per-subject breakdown |

- Handbook §7.4: formats may be MCQ, hypotheticals and/or short-answer questions.
- Slide 43: two devices are allowed, one for the exam and one for reference materials.
  Wireless peripherals and external displays are not allowed.
- Slide 48: every Subject in a written paper has at least one question; the two
  components are of similar depth.
- Slide 50: cite a case by name in brackets (italics if possible) with the paragraph
  number; full citations are only needed to tell apart similarly named cases. Do not
  cite lecture notes or slides. Write in prose, no bullet points. No spell-check.
- Slide 51: no external copy-paste into the exam software; avoid cut-and-paste within it.
- Slide 52: graded Distinction / Pass / Fail, not on a curve. The pass score is
  confidential and is set on the combined score of all papers in a module (e.g. CCP
  Papers 1 + 2). Do not assume it is 50%.

## B. Changes the PRD implies for other root docs (owner: Main Session)

- `RULES.md` "Answer to the paper's format" says IRAC; it should say I-CRUPAC, and add
  Templates for Written Advocacy and the citation and prose rules from slide 50.
- `RULES.md` / `CLAUDE.md` §2 / `AGENTS.md` brief format: source order should become
  module materials, then Cyril's notes, then Nic's package.
- `SCHEMA.md` `study/` file set: replace outline / drills / weak-spots with the outputs
  in PRD §4 (Question Bank, Pre-writes, Templates, Flowcharts, Reference Pack PDF,
  Drills, Weak Spots).
- Tracker (`SCHEMA.md`): record the level meanings from PRD FR-11, and that a Practice
  Paper writes `full[paperId]`. All Subjects are reset to not-reviewed as of 2 Nov. No
  field change is needed; only what the values mean changes.
- `AGENTS.md` phase gating: add the Block-overrun rule (PRD §5), the uncuttable items
  (PRD §7 items 1–3), and that the existing `study/eth-w` and `study/clk-m` files are raw
  material for Pre-writes and Flowcharts (PRD §7).
