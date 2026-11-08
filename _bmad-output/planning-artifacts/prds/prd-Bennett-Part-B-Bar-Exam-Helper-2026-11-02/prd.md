---
title: Part B Bar Exam Helper
status: final
created: 2026-11-02
updated: 2026-11-08
---

# PRD: Part B Bar Exam Helper

## 0. Document Purpose

This is the scope contract for Bennett's Part B study system: what the Claude sessions in
this repo produce, in what priority, and how success is judged. Bennett is the only user
and decides scope. The Main Session and Paper Sessions build to it. It builds on the
verified facts in `SCHEMA.md` (papers, subjects, tracker), `AGENTS.md` (who does what,
block schedule) and `RULES.md` (exam integrity, sourcing), and does not repeat them.
Detail that supports the PRD but does not belong in it (exam-format evidence, changes to
other docs) is in `addendum.md`. Terms are defined in §3 and used exactly. Inferred
points were tagged `[ASSUMPTION]`; all are now confirmed (§10).

## 1. Vision

Part B is eight two-hour Papers in eleven days (1–11 Dec 2026), and they test two
different skills. The exams are open book: Bennett may bring a second device for
reference materials, but cannot paste text into the exam software, and he is planning
for no internet access.

For the **Written Papers** (`drp-w`, `eth-w`, `pcp-w`), the system makes sure no
hypothetical comes as a surprise. It predicts the questions likely to be set and builds
a stack of **Pre-writes** in I-CRUPAC form, each citing real cases and statutes. In the
exam Bennett finds the right Pre-write, then adapts and retypes it, rather than writing
from nothing.

For the **MCQ Papers** (`drp-m`, `pcp-m`, `ccp-1`, `ccp-2`, `clk-m`), the system turns
the notes into **Cheatsheets**. On reading a question, Bennett recognises the Subject and
the issue at once and follows the Cheatsheet to the answer.

Everything is packaged per Paper as a **Reference Pack**: a PDF he can search, with a
contents page and a keyword index, ready on the reference device. Beside it sits the
Paper's **Model Q&A**, which shows by Topic the kinds of question that come up. Cyril's notes from last
year's sitting are the main secondary source, Nic's package is a fallback, and the Course
Materials win on any point of law.

## 2. Target User

Bennett, sitting 2026 Part B Session 2. He is the only user. User Journeys are omitted
because there is one person working the system and the jobs below cover it.

### 2.1 Jobs To Be Done

- When a written hypothetical raises an issue, find a ready, accurate, cited Pre-write in
  seconds and adapt it to the facts.
- When an MCQ question appears, recognise its Subject and issue at once and reach the
  answer through a Cheatsheet.
- When studying a Topic, learn it from the Cheatsheet and Model Q&A alongside Cyril's
  notes, so the files he will use in the exam are the files he studied from.
- When practising, learn what kinds of question each Topic produces, so in the exam he
  recognises the kind at once and goes straight to the matching model question.
- Know each day which Paper and Subject to work on, and what is still missing before
  exam week.
- Walk into each exam trusting the Reference Pack: it is accurate, he can find things in
  it, and it covers the ground.

### 2.2 How Bennett studies a Paper

Recorded from Bennett on 8 Nov 2026. Each feature in §4 serves a step here.

1. **Syllabus and learning plan.** He reads the Subject's syllabus and learning plans to
   see what the Module requires. The Coverage List is drawn from the same documents
   (RULES: Coverage List first), so it is his checklist of what the Paper can test.
2. **Cyril's notes.** He reads Cyril's notes for depth. They are the main secondary
   source (FR-8), and the Course Materials still win on any point of law.
3. **Reference Pack and Model Q&A.** He builds both with the Paper Session, studies
   alongside them, and uses them in practice and then in the exam. His lookup in the
   Reference Pack is:
   1. Work out which Topic the question is about.
   2. Ctrl-F a keyword from the question (contents page if no keyword comes to mind).
   3. Land on the Topic's Cheatsheet, which he calls the framework, and follow it down to
      the Sub-point.
   4. MCQ: follow the link to the end point, which gives the answer. Written: follow the
      link to the right Pre-write paragraph or paragraphs, then adapt and retype them.
4. **Model Q&A for practice.** He practises on it to learn the kinds of question each
   Topic produces. This lets him recognise a question's kind quickly and turn to the matching model
   question in the exam.

What follows for the outputs: Ctrl-F is the way in, so Cheatsheet cue lines and Keywords
use the words a question uses (FR-7). Each Cheatsheet answering line leads to one end point
or Pre-write, and the Model Q&A can be read Topic by Topic (FR-12).

## 3. Glossary

- **Module**: one of the five examined course modules (DRP, ETH, PCP, CCP, CLK). It has
  one or two Papers. The pass score is set per Module.
- **Paper**: one of the eight exams, identified by Paper ID (`drp-w`, `drp-m`, `eth-w`,
  `pcp-w`, `pcp-m`, `ccp-1`, `ccp-2`, `clk-m`). It has one or more Subjects. See
  `SCHEMA.md`.
- **Written Paper**: `drp-w`, `eth-w`, `pcp-w`. Hypotheticals and sub-questions, with no
  MCQ section (Opening Brief slide 45; `Bar Exam/Bar Dump.docx`).
- **MCQ Paper**: `drp-m`, `pcp-m`, `ccp-1`, `ccp-2`, `clk-m`. 60 questions, 4 options,
  2 hours.
- **Subject**: an examinable subject within a Paper, as listed in `SCHEMA.md`.
- **Course Materials**: the module materials under `Bar Exam/Modules/`.
- **Topic**: a heading within a Subject (e.g. service out of jurisdiction). It has one
  or more Sub-points.
- **Sub-point**: the smallest issue a question can turn on. It is the unit for judging
  coverage.
- **Coverage List**: the list of a Subject's Topics and Sub-points, drawn from its
  syllabus, learning plan and Course Materials. It is the baseline that "every Topic" and
  "every Sub-point" are counted against.
- **Question Bank**: the list of likely questions for a Written Paper, each tagged with
  its Source Tier and the Sub-points it raises.
- **Source Tier**: where a likely question came from, in priority order: (1) past-year
  papers, (2) course contact sessions, (3) Bennett's own questions, starting from Topics
  the past papers under-test.
- **Pre-write**: a ready-made answer paragraph for one Sub-point, in I-CRUPAC form,
  written as prose.
- **I-CRUPAC**: Issue, Conclusion, Rule, Proof/Precedent, Application & analysis, restated
  Conclusion.
- **Template**: an annotated skeleton of a document Written Advocacy may ask Bennett to
  draft (e.g. letter of demand, reply, written submissions).
- **Cheatsheet**: a Q&A cue list ("framework") for one Topic of any Paper, written as nested
  text lines. It runs from broad question cues to the Sub-point, and each answering line links
  to the end point (MCQ) or Pre-write (Written) that holds the rule. On MCQ Papers it replaced
  Mermaid flowcharts on 4 Nov 2026; Written Papers have them from 8 Nov 2026.
- **Reference Pack**: one PDF per Paper that collects its Cheatsheets, with its Pre-writes
  and Templates (Written) or its end points (MCQ). It has text he can search, a contents page and a keyword index.
- **Model Q&A**: the second exam-day PDF per Paper (`model-questions.pdf`): practice
  questions grouped by Topic, each with its Keywords and its model answer directly under it.
  It is how Bennett learns the kinds of question a Topic produces (§2.2, FR-12).
- **Drill**: a set of questions for Bennett on one or more Subjects, then marked.
- **Practice Paper**: a full Paper sat timed, with its Reference Pack, then marked. It is
  a past-year paper, or a mock where none exists.
- **Weak Spot**: a Sub-point where a Drill or Practice Paper showed a gap, or where a
  lookup in the Reference Pack failed.
- **Main Session / Paper Session / Tracker / Block**: as defined in `AGENTS.md` and
  `SCHEMA.md`.
- **Notes level / Practice level**: the Tracker's per-Subject scales (0 not yet,
  1 done, 2 reviewed). Notes now means Pre-writes and Templates (Written) or Cheatsheets
  (MCQ). See FR-11.

## 4. Features

Features are listed in priority order (see §7).

### 4.1 Cheatsheets (every Paper)

**Description:** For each Paper, MCQ and Written, the Paper Session builds one Cheatsheet per Topic. A
Cheatsheet starts from the cues a question gives (the words, facts and parties that signal
the Topic). It branches to the specific Sub-point and ends at the rule or answer, with a
source for each end point. On a Written Paper the Cheatsheet heads the Topic's Pre-writes and
its lines link to them. The Cheatsheets are compiled into the Paper's Reference Pack. This
is the minimum Bennett will not go into any Paper without.

#### FR-1: One Cheatsheet per Topic

A Paper Session produces a Cheatsheet for every Topic of every Subject in every Paper
(Written Advocacy excepted: its Templates serve instead).

**Consequences (testable):**
- The Subject's Coverage List is written before its Cheatsheets.
- Every Topic on the Coverage List has a Cheatsheet, or an explicit reason why it does
  not.
- Every end point names the rule or answer and cites its source (file path under
  `Bar Exam/` and page or slide).
- Each Cheatsheet has a recognition layer: broad question cues that narrow to the
  Sub-point.
- Each answering line links to its end point, and the Reference Pack prints that
  end point's page beside the link.

#### FR-2: Cheatsheets on screen and as a PDF

Bennett can open each Cheatsheet on his laptop and download the Paper's Cheatsheets as a
single PDF.

**Consequences (testable):**
- The compiled PDF opens offline in a standard PDF viewer.
- Cheatsheet cues are text, not images, so Ctrl-F finds them.

### 4.2 Pre-write Stack (Written Papers)

**Description:** For each Written Paper Subject other than Written Advocacy, the Paper
Session writes Pre-writes until every Sub-point has at least one. Each Pre-write
follows I-CRUPAC. It cites cases by name in brackets with the paragraph relied on
(Opening Brief slide 50), plus the statute section. It is written as prose, because the
exam does not allow bullet points. Its Rule part is short enough to retype, with the
rule's full text in a box beside it for reference, since pasting is not allowed.

#### FR-3: Pre-write coverage

A Paper Session produces at least one Pre-write for every Sub-point of every Written
Paper Subject, Written Advocacy excepted.

**Consequences (testable):**
- The Subject's Coverage List shows each Sub-point and the ID of its Pre-write, with no
  gaps left unexplained.

#### FR-4: Pre-write form

Every Pre-write follows I-CRUPAC, is written as prose, gives its rule in full in a box,
and cites its law.

**Consequences (testable):**
- All six I-CRUPAC parts are present. Part labels are there for lookup only and are not
  retyped.
- The Application part holds a pattern, not an answer: the facts that trigger the rule,
  and how to apply it to them.
- **In the Pre-write text** (what Bennett retypes): cases by name in brackets, with the
  paragraph number where the sources give one; statutes by section.
- **In a source note under the Pre-write** (not retyped): the file path under
  `Bar Exam/` and page or slide for every proposition. A proposition without a source
  note is marked `TODO: verify`. A case whose paragraph number the sources don't give is
  not a TODO.
- No Pre-write cites lecture notes or slides as authority (Opening Brief slide 50).
- **Rule part:** a short statement of the rule that Bennett can retype.
- **Rule in full box:** straight after the Rule part, a box gives the full text of the
  main rule, with any criteria, exceptions, powers or case factors it relies on (for
  example, the PD 9.1.1 powers and how to check a power is real; the *Harsha* factors).
  Each limb is on its own line and sub-limbs are indented one step. The box is for
  reference and is not retyped; Bennett takes from it what fits the facts.
- Proof, Application and the restated Conclusion are written in full, phrased as "the
  lawyer did / did not breach r X, which states …" or "here, r X applies, which states
  that …". Model answers set out, in the rule's own words, only the rule and the limbs they rely on, keeping the limb letters (e.g. "r 44(2) … (c) …; or (d) …").
- No word cap (changed by Bennett on 3 Nov 2026; was 150–300 words).

#### FR-5: Written Advocacy Templates

A Paper Session produces annotated Templates for the documents Written Advocacy may ask
Bennett to draft.

**Consequences (testable):**
- At minimum, the document types seen in the 2026 Sample Questions and the past-year
  papers each have a Template.
- Every Template notes what each part must contain and the common mistakes to avoid.

### 4.3 Question Bank (Written Papers)

**Description:** For each Written Paper, the Paper Session lists likely questions by
Source Tier: past-year papers first, then course contact sessions, then its own
questions aimed at Topics the past papers under-test. Each question is mapped to the
Sub-points it raises, so the Question Bank both drives Pre-write coverage and serves as
Drill material.

#### FR-6: Likely questions by Source Tier

A Paper Session produces a Question Bank for each Written Paper, ordered by Source Tier.

**Consequences (testable):**
- Every entry gives its Source Tier, its source (paper and year, or contact session) and
  the Sub-points it raises.
- Tier 3 questions name the under-tested Topic they target.

### 4.4 Reference Packs and Model Q&A

**Description:** Each Paper's outputs are compiled into one Reference Pack for the
reference device. Bennett's lookup (§2.2 step 3) is: identify the Topic, Ctrl-F a keyword
from the question, land on the Cheatsheet and follow it to the end point or Pre-write. If
no keyword comes to mind he uses the contents page, and the keyword index is the backstop.
Beside the pack, each Paper's Model Q&A is the second exam-day PDF.

#### FR-7: Navigable Reference Pack

Bennett can find any Pre-write, Template or Cheatsheet in a Reference Pack by text
search, the contents page or the keyword index.

**Consequences (testable):**
- The PDF text is searchable (not scanned images).
- The contents page is organised Subject → Topic → Sub-point, and its entries link to
  the pages.
- The keyword index lists, for every Sub-point, its key terms, case names and statute
  sections, each with a page reference.
- Cheatsheet cue lines and Keywords use the words, facts and parties a question uses, so
  a Ctrl-F on a word from the question reaches the right Cheatsheet.
- The pack works fully offline.

#### FR-12: Model Q&A per Paper

Every Paper, MCQ and Written, has a Model Q&A PDF beside its Reference Pack (Bennett,
5 Nov 2026).

**Consequences (testable):**
- The kinds of question a Topic produces can be found together. MCQ questions sit under
  their Topic. Written questions run by past paper, and the contents page lists each one
  under every Topic it raises. Contents entries link to their pages.
- Each question has a Keywords line and its model answer directly under it.
- Each question's tag line names its coverage Key and the end points or Pre-writes it
  relies on, so practice leads back into the Reference Pack.
- The PDF text is searchable and works offline.

### 4.5 Sourcing and Accuracy

**Description:** Accuracy matters most: an answer that misses the point is a fail.
Sources follow a fixed order, and conflicts are shown openly rather than resolved
silently.

#### FR-8: Source priority

Paper Sessions draw on sources in this order: Course Materials (which win on any point
of law), then Cyril's notes (the most recent secondary source), then Nic's package, used
only when needed.

**Consequences (testable):**
- Where Cyril's notes or Nic's package conflict with Course Materials, the output follows
  the Course Materials and records the conflict.

### 4.6 Practice, Drills and Weak Spots

**Description:** Once a Paper's Cheatsheets or Pre-writes exist, Bennett sits at least one
Practice Paper for it with its Reference Pack. This is what makes a Subject "reviewed"
and what tests whether he can find things in the pack. Beyond that, the Paper Session
sets Drills: Question Bank items for Written Papers, single-best-answer questions for
MCQ Papers. It marks his answers. For MCQs it explains why each wrong option is wrong.
Gaps are logged as Weak Spots and fed back into the Reference Pack.

#### FR-9: Practice Paper and Drills, marked

A Paper Session provides at least one Practice Paper per Paper, can set Drills, and marks
Bennett's answers to the Paper's format.

**Consequences (testable):**
- Where no past-year paper exists for a Paper or Subject, the Paper Session builds a mock
  from the 2026 Sample Questions and the Question Bank. The mock counts as a Practice
  Paper.
- Written answers are marked on I-CRUPAC structure, accuracy and coverage of Sub-points.
- MCQ answers are marked with the reason for the correct option and against each wrong
  option.
- Marking never happens during a live assessment (Handbook §7.11–7.13; see §5).

#### FR-10: Weak Spots fed back

Weak Spots from a Drill or Practice Paper lead to a fix in the Reference Pack.

**Consequences (testable):**
- Each Weak Spot links to the Pre-write, Cheatsheet or index entry that was added or
  changed.
- A failed lookup during a Practice Paper ("I couldn't find it") counts as a Weak Spot
  and leads to an index or contents fix.

### 4.7 Progress Tracking

**Description:** The Tracker remains the progress record (see `SCHEMA.md`). The Main
Session reads it daily to say what the current Block needs, and records progress only on
Bennett's word.

#### FR-11: What the Tracker levels mean

The Main Session records the Tracker levels as follows.

| Level | Meaning |
|---|---|
| Notes 1 (done) | Every Sub-point on the Subject's Coverage List has its Cheatsheet end point, or its Pre-write (and Templates, for Written Advocacy) |
| Notes 2 (reviewed) | Notes 1, used in a Practice Paper, and its Weak Spots fixed |
| Practice 1 (done) | At least one Drill on the Subject marked |
| Practice 2 (reviewed) | Bennett has sat a Practice Paper covering the Subject with its Reference Pack |

**Consequences (testable):**
- A Practice Paper is recorded in the Tracker's `full[paperId]` and sets Practice 2 for
  every Subject it covers.
- As of 2 Nov 2026 no Subject counts as reviewed, whatever the Tracker currently shows.
- No Tracker write happens without Bennett confirming.

## 5. Constraints and Guardrails

- **Exam integrity:** no AI help during any exam, quiz, Mock Exam or other assessment
  under exam conditions (Handbook §7.11–7.13). Sessions stop if a request looks like a
  live assessment. Practice Papers Bennett sits on his own and brings for marking are
  fine.
- **Reference device contents:** the exam allows a second device for reference
  materials (Opening Brief slide 43). TODO: verify against the 2026 Examinations Rules,
  once issued, what that device may hold.
- **Licensed material:** `Bar Exam/` is read-only and stays out of git. Outputs condense
  it and do not copy it out wholesale.
- **Time:** the Blocks end 30 Nov. Exam week (1–11 Dec) is for timed practice and Weak
  Spot review. Fixes to existing Pre-writes, Cheatsheets, contents and index are allowed;
  new Topics are not.
- **Block overrun:** if a Block ends before its uncuttable items (§7 items 1–3) are done,
  it runs on only until they are done, then hands over. The time comes out of the next
  Block's lower-priority items, not by pushing every later Block back, because the order
  runs last exam first and a general slip would eat into Papers sat earlier.

## 6. Non-Goals

- No study time on non-examinable Subjects (Litigation Technology, Law & Society,
  Professional Skills) unless Bennett asks.
- Not building new apps or tools. The existing Tracker and PDFs are the only interfaces.
- Not answering, or helping with, the compulsory online quizzes or any live assessment.
- Not standalone essay preparation. No 2026 material sets one (see `addendum.md`).

## 7. MVP Scope and Cut Order

If a Block runs short, work is cut in this order, last item first:

1. **Cheatsheets for every Topic** (MCQ and Written). Cannot be cut.
2. **Pre-writes for every Sub-point the past-year papers have tested.** Cannot be cut.
   This is the Written Paper equivalent of item 1, and needs Question Bank tier 1 (the
   past-year papers) to identify those Sub-points.
3. **One Practice Paper per Paper, sat with its Reference Pack.** Cannot be cut. It is
   what makes a Subject "reviewed" (SM-2) and what tests lookup (SM-4).
4. Pre-writes for the remaining Sub-points, and Written Advocacy Templates.
5. Reference Pack contents page and keyword index. Text search alone is the fallback.
   TODO: Bennett to place the Model Q&A (FR-12) in this order.
6. Question Bank tiers 2–3.
7. Further Drills beyond the Practice Paper.

**Work already done.** Before this PRD, the `eth-w` and `clk-m` Paper Sessions wrote
outlines, drills and weak-spot logs in `study/eth-w/` and `study/clk-m/`. These are kept
as raw material that Pre-writes and Cheatsheets are built from, not discarded. `eth-w`
Pre-writes are finished from its outline in time left over during Block 2.

## 8. Success Metrics

**Primary**
- **SM-1:** Bennett passes all five Modules. The pass score is set per Module on its
  combined Papers (e.g. `ccp-1` + `ccp-2`; Opening Brief slide 52), so a weak Paper can
  be offset by its partner Paper. This is the outcome; SM-2 to SM-5 are the measures that
  can steer the work before it.
- **SM-2:** By 30 Nov, every examinable Subject is at Notes level ≥1 and Practice level 2
  in the Tracker. Validates FR-1–FR-7, FR-9 and FR-11.

**Secondary**
- **SM-3, Coverage:** every Sub-point on every Coverage List has a Pre-write or a
  Cheatsheet end point (FR-1, FR-3).
- **SM-4, Navigation:** in Practice Papers Bennett finds what he needs in the Reference
  Pack. Target: zero unresolved failed lookups per Paper by 30 Nov (FR-7, FR-10).
- **SM-5, Accuracy:** no open `TODO: verify` left in a Reference Pack at exam time
  (FR-4, FR-8).

**Counter-metrics (do not optimise)**
- **SM-C1, Volume:** number of Pre-writes or pages. More is not better if it slows
  lookup or retyping. Counterbalances SM-3.
- **SM-C2, Polish:** how the Cheatsheets look. A clear, correct Cheatsheet beats a pretty one.
  Counterbalances FR-2.

## 9. Open Questions

1. What may the reference device hold, and must it be offline? Until the 2026
   Examinations Rules are issued, plan for a PDF on an offline device. Owner: Bennett.
   Revisit when the Rules are issued.
2. Do the 2021–2023 past-year papers include any essay-style question? Only the 2026
   Opening Brief and Sample Questions were checked. Owner: each Written Paper Session.
3. How is accuracy checked beyond the author's own `TODO: verify` flags? Revisit if a
   Practice Paper turns up a wrong Pre-write or Cheatsheet. Owner: Main Session.
4. Can a full written answer be retyped from Pre-writes within the 2 hours? Measure in
   the first written Practice Paper; if not, Bennett decides what to retype less of. Owner: Written
   Paper Sessions.
5. Exactly where should outputs live, and in what file format, under `study/<paper-id>/`?
   Owner: `bmad-architecture` / `SCHEMA.md`.

## 10. Assumptions Index

None open. Recorded from Bennett on 8 Nov 2026: his study workflow (§2.2), the lookup path
it implies (§4.4, FR-7) and the Model Q&A as FR-12 (§3). Changed by Bennett on 8 Nov 2026: every Reference Pack, Written included, has a
Cheatsheet per Topic (§3, §4.1, FR-1, §7 item 1). Added by Bennett on 5 Nov 2026: every Paper, MCQ and Written, has two exam-day
PDFs, its Reference Pack and a model Q&A PDF (questions by Topic, each answer directly
under its question, Keywords per question, contents linked to Topics). Changed by Bennett on 4 Nov 2026: MCQ Papers use Q&A Cheatsheets instead
of Mermaid flowcharts (§3, FR-1, FR-2). Changed by Bennett on 3 Nov 2026: Pre-writes keep a short Rule part, add a
Rule in full box, and have no word cap (FR-4). Confirmed by Bennett on 2 Nov 2026: a failed lookup counts as a Weak Spot (FR-10); Pre-writes on Sub-points the past papers
have tested cannot be cut (§7); target of zero unresolved failed lookups (SM-4); the
Tracker level meanings and the `full[paperId]` write (FR-11).
