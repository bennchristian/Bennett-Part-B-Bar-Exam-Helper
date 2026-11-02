# PRD Quality Review — Part B Bar Exam Helper

Reviewed 2 Nov 2026 against `prd-validation-checklist.md`. Inputs: `prd.md`, `addendum.md`,
plus spot checks of `SCHEMA.md`, `RULES.md`, `.memlog.md`, `study/` and the `3. PYP/` folder
listing. Calibrated for personal, solo stakes, with 29 days to the first exam and 28 build days
left (2 to 30 Nov).

## Overall verdict

The PRD has a clear, specific thesis. Written Papers are answered by retrieving and retyping
cited I-CRUPAC Pre-writes, and MCQ Papers by recognising the question and following a
Flowchart. The decisions behind it are crisp: cut order, source order, Templates for Written
Advocacy, and counter-metrics tied to Bennett's stated failure modes. The risk is execution.
The two "Cannot be cut" items have no denominator and no sizing against the remaining 28
days. The cut order would drop the practice papers that the primary metric SM-2 depends on.
The PRD also says nothing about the ~26k words already in `study/eth-w` and `study/clk-m`,
even though the `eth-w` block ends tomorrow. All five high findings are small text fixes.
Make them before the PRD is promoted to the root `PRD.md` and used to brief paper sessions.

## Decision-readiness — adequate

Most choices are stated as decisions and name what was given up. §7 ranks what gets cut.
FR-8 puts the module materials first and makes conflicts visible ("records the conflict").
§6 rules out essays with evidence. FR-5 replaces I-CRUPAC with Templates for Written Advocacy.
SM-C1 and SM-C2 say outright that volume and polish are not the goal. The Open Questions are
real questions, and each has an owner.

The PRD does not face its biggest tension: whether the uncuttable work fits the calendar. §7
marks items 1 and 2 "Cannot be cut", but nothing estimates how much work they are. The PRD
also redefines what counts as done on the day the first block nearly ends. It does not say
what happens to that block or to the work already done in it.

### Findings
- **high** Uncuttable work is not sized against the calendar (§7 items 1–2; FR-1; FR-3).
  "Flowcharts for every MCQ Topic. Cannot be cut." There are 19 MCQ Subjects (`SCHEMA.md`).
  The blocks in `AGENTS.md` give `pcp-m` 3 days for 5 Subjects and `ccp-1`, `ccp-2` and
  `clk-m` 3 days for 4 Subjects each. The same days also hold the practice paper that SM-2
  needs. Nothing says what happens when a block's uncuttable work does not fit. It could
  borrow days from the next block, move into exam week (which §5 forbids), or drop below
  "every Topic". *Fix:* make the first step of each block a count of Topics and Sub-points
  (see the Done-ness finding on inventory). Add a `[NOTE FOR PM]` in §7 that says what
  gives when the count exceeds the block: the order of borrowing, or a floor such as every
  Topic tested in the past-year papers.
- **high** The PRD does not say how existing work and the current block carry over (§4.7
  FR-11 "no Subject counts as reviewed"; §5 Time; addendum B). `study/eth-w/` (~9.3k words)
  and `study/clk-m/` (~17k words) already hold outlines, drills and weak spots in the old
  format. The `eth-w` outline header reads "Built 2 Nov 2026". Addendum B says that file set
  is to be "replaced". The PRD does not say whether those outlines become the source for
  Pre-writes and Flowcharts, are kept alongside them, or are retired. Block 1 (`eth-w`, 29
  Oct–3 Nov) ends tomorrow, and the new definition of done applies to it. *Fix:* add one
  paragraph, in §7 or §5, that says what happens to the existing outlines (for example:
  inputs to the Sub-point inventory, then archived). Also say whether `eth-w` gets more days
  or rolls into its exam-week review.
- **medium** No fallback if the reference-device rules restrict the Reference Pack (§5
  "Reference device contents"; Open Question 1). Every feature ends in a searchable PDF on a
  second device. If the 2026 Examinations Rules limit what that device may hold or how it is
  used, Features 4.1–4.4 all lose their delivery channel. The open question has an owner but
  no date or fallback. *Fix:* add the expected issue date, if known, and a one-line fallback
  (for example, printed packs with the contents page and index kept).

## Substance over theater — strong

Very little is furniture. The Vision could only describe this product: it names the
open-book-offline, no-paste setting and the split between Written and MCQ papers that shapes
every feature. Each Job To Be Done maps to a feature. The counter-metrics come from
Bennett's ranked failure modes (`.memlog.md`: inaccuracy, then navigation, then coverage),
not from a template. There is no persona or NFR padding.

### Findings
- **low** SM-1 is lagging and cannot steer the work (§8 SM-1, "Validates everything"). Results
  arrive after the exams, so SM-1 cannot influence any decision in this PRD's window. That
  is fine for the ultimate goal, but SM-2 to SM-5 are the metrics that actually steer. *Fix:*
  label SM-1 as the outcome and SM-2 as the main steering metric, or drop "Validates
  everything".

## Strategic coherence — adequate

The thesis is clear and the features follow from it. The first two cut-order items are the
core of each half of the thesis (Flowcharts for MCQ, Pre-writes for tier-1 Sub-points), and
the Question Bank exists to feed Pre-write coverage. Counter-metrics are named against
SM-3 and FR-2. The MVP is clearly problem-solving in kind.

Three things weaken it. The cut order works against the primary metric. The top-ranked
failure mode, inaccuracy, is checked only by self-flagging. The retype-under-time-pressure
idea at the centre of the written strategy is never checked against the exam's time.

### Findings
- **high** The cut order removes what the primary metric needs (§7 item 6 "Drills and Weak
  Spot logging" vs SM-2, SM-4, FR-11). SM-2 needs every Subject at Practice level 2,
  "meaning Bennett has sat a practice paper using its Reference Pack". §3 defines a Drill as
  including "a practice paper he sits". SM-4 is measured "in practice papers". Cutting item
  6, which §7 treats as the first thing to cut, makes SM-2 impossible to meet and SM-4
  impossible to measure. It also means nothing tests whether the uncuttable items work in
  practice. *Fix:* split item 6. Put "sit one practice paper per Paper using its Reference
  Pack" at item 3 or higher, and keep extra Drills and MCQ distractor explanations last.
- **medium** Accuracy, the top failure mode, is checked only by the author's own flags (§4.5;
  FR-4; SM-5). SM-5 counts open `TODO: verify` markers. A wrong proposition that was never
  flagged still scores perfectly. Nothing in the PRD checks Pre-writes or Flowchart end
  points against their sources, and `AGENTS.md` handover only has the main session "check
  the files exist". *Fix:* add a consequence to FR-4 and FR-1, or a line to SM-5. For
  example, before a pack is final, a second pass checks a sample of citations per Subject
  against the cited file and page, and records the result.
- **medium** The retype idea is not checked against the time in the exam (§1 "adapts and
  retypes it"; FR-4 "about 5 minutes"). Addendum A gives ETH sub-questions of 12–15 marks.
  `study/eth-w/outline.md` gives past splits of 50+50 and 40+30+30 within "2 hours inclusive
  of reading time". There is no spell-check (slide 50). If a sub-question raises three
  Sub-points, retyping Pre-writes alone takes about 15 minutes before any fact-specific
  analysis. The PRD never checks this budget, and FR-4's 150–300 word cap follows from it.
  *Fix:* add a timed retype trial early in the first Written block, and let the result set
  FR-4's length cap. Alternatively, state that only Rule and Precedent are retyped verbatim
  and the rest is written fresh.

## Done-ness clarity — thin

Several FRs are well bounded. FR-5's "document types seen in the 2026 Sample Questions and
the past-year papers" is checkable. FR-7's "searchable (not scanned images)" and "entries
link to the pages" are checkable, and so is FR-10's link from each Weak Spot to the fix.

The two uncuttable FRs are the weak point. Their denominators, "every Topic" and "every
Sub-point", rest on definitions that need judgment, and nothing produces the list they
count against. FR-4's citation rules can conflict with the sources available offline.

### Findings
- **high** No list of Topics and Sub-points to measure coverage against (§3 "Topic: a
  heading within a Subject"; "Sub-point: the smallest issue a question can turn on"; FR-1;
  FR-3; SM-3). The PRD does not say whose headings count: the syllabus, the lecture slides
  or Cyril's notes. "Smallest issue a question can turn on" is a judgment call. FR-3 asks
  for a coverage list for Written Papers, but no FR produces one for MCQ Papers. Without a
  fixed list, "every Topic", "every Sub-point" and SM-3 cannot be checked, and §7's
  uncuttable items have no defined size. *Fix:* add an FR, or a first consequence under
  FR-1 and FR-3. Each Paper Session first writes a Topic → Sub-point list per Subject from
  a named source (for ETH, the syllabus file the outline already cites as `SYL`). That list
  is the denominator for FR-1, FR-3 and SM-3, and the main session approves it.
- **high** The citation rules may be impossible to meet from the sources, and FR-4 mixes two
  kinds of citation (FR-4; SM-5). "Every case gives a name and paragraph number" and "every
  proposition traces to a source under `Bar Exam/`" sit next to "No Pre-write cites lecture
  notes or slides as authority". Most of `Bar Exam/` is course slides and notes. Those
  slides give the source a Pre-write traces to (file path and page). They are not the
  citation used in the exam (case and paragraph). Course materials often name a case
  without a paragraph number. Unless a case's paragraph can be found offline, every such
  case becomes a `TODO: verify`, and SM-5 (zero open TODOs at exam time) cannot be met.
  *Fix:* in FR-4, separate the exam citation (case name and paragraph, statute and section,
  which is what gets retyped) from the source note (`Bar Exam/` path and page, never
  retyped). Say what to do when a paragraph number cannot be found. For example, use a
  distinct `para?` marker that SM-5 does not count, so SM-5 measures accuracy rather than
  whether every paragraph number was found.
- **medium** FR-11 leaves parts of the Tracker scale undefined (FR-11; §3 "Notes level /
  Practice level"; addendum B "No field change is needed"). FR-11 defines Notes 1 and
  Practice 2. It does not define Practice 1 or Notes 2. A practice paper is sat per Paper,
  but `p` is per Subject. The Tracker's `full` field, which records the practice papers
  sat, is not mentioned. *Fix:* define all four values (`n`=1, `n`=2, `p`=1, `p`=2). State
  whether sitting a practice paper writes `full[paperId]`, every Subject's `p`, or both.
- **medium** FR-2 "viewable on screen" has no test, and Flowcharts may fail the searchable-text
  rule (FR-2; FR-7). The only consequence under FR-2 covers the PDF. A Flowchart rendered as
  an image would pass "opens offline" but fail FR-7's searchable-text requirement for the
  very content Ctrl-F is meant to find. *Fix:* add a consequence that node and cue text in
  each Flowchart is real text in the PDF, not a picture. Either define "viewable on screen"
  (where, in what viewer) or drop it.
- **medium** FR-4 requires a pre-written Application and labels, which clash with the prose
  rule (FR-4 "All six I-CRUPAC parts are present and labelled"). Application and analysis
  depend on the facts, so a Pre-write can only hold a pattern for them. Labelled parts also
  sit awkwardly with "written as prose" and the exam's no-bullets rule. *Fix:* say what the
  A part of a Pre-write holds (for example, the facts that trigger the rule and how to apply
  it). State that labels are for lookup only and are not retyped.
- **low** The keyword index test is subjective (FR-7 "terms … a question is likely to use").
  FR-10 corrects the index after failed lookups, which limits the damage. *Fix:* make it
  checkable: every Flowchart cue, every case name, every statute section and every Question
  Bank keyword appears in the index.

## Scope honesty — adequate

§6 does real work: it excludes non-examinable Subjects, new tools, quizzes and essays, with
evidence. All four drafting assumptions were confirmed (§10). The Open Questions are real,
which is proportionate for personal stakes. The unstated gaps all concern what material
exists and how the existing setup changes.

### Findings
- **medium** The PRD assumes a practice paper exists for every Subject (SM-2; FR-9; FR-11).
  SM-2 needs a practice paper for every Subject by 30 Nov. Going by file names in
  `3. PYP/`, MCQ coverage is thin. 2023 has CCP Paper 2, DRP Paper 2 and PCP Paper 2, and
  CCP Paper 1 "missing questions 42, 44, 53". CLK has only an instruction sheet. 2021 and
  2022 are mostly written papers. CLK, and possibly other MCQ Subjects, may have no past
  paper to sit. The Go Pack and Cyril's folders were not opened for this check. *Fix:* in
  FR-9, say that where no past paper exists, the Paper Session builds a mock from a named
  source and that a mock counts for Practice level 2. Otherwise, narrow SM-2 for those
  Subjects.
- **low** A paper that mixes written and MCQ questions is not covered (§3 "Written Paper:
  `drp-w`, `eth-w`, `pcp-w`"). `study/eth-w/outline.md` records a 20-question MCQ Section
  A in ETH 2022, and a TODO to confirm at the End of Course Lecture (~10 Nov) whether any
  MCQ part remains. *Fix:* add this to §9 as Open Question 4, owned by the `eth-w` Paper
  Session.
- **low** It is unclear whether exam week allows any building (§5 Time: "no new building" vs
  FR-10 "Weak Spots … lead to a fix in the Reference Pack"). Exam-week Weak Spot review will
  produce fixes. *Fix:* state that index, contents and Pre-write fixes from Weak Spots are
  allowed in exam week, and new Topics are not.

## Downstream usability — adequate

The PRD feeds `ARCHITECTURE.md` and `SCHEMA.md` (addendum B, Open Question 3), not story
creation, so traceability needs are modest. The Glossary is good and mostly followed. FR and
SM IDs are contiguous, and addendum B is a clean list of changes for the main session to make
to the root docs. FR-3's "the ID of its Pre-write" assumes an ID scheme that does not
exist yet. That is properly deferred to Open Question 3, but architecture should know it
must define one. Terms drift slightly (see Mechanical notes).

## Shape fit — strong

The PRD is shaped as a capability spec for one operator, with Jobs To Be Done in place of
User Journeys, and §2 says why. That is the right shape. At ~2.5k words it is longer than
the "lean ~2 page" target in the memlog, but it does not repeat the root docs (§0) and
nothing in it is filler. No enterprise sections are missing that would matter here.

## Mechanical notes

- **IDs:** FR-1 to FR-11, SM-1 to SM-5 and SM-C1 to SM-C2 are contiguous and unique.
  References to §3, §5, §7 and §10 resolve.
- **Assumptions Index:** "None open. The four drafting assumptions were confirmed". The PRD
  does not list the four, so you cannot trace them from the PRD alone (they are in
  `.memlog.md`). List them in one line each, marked confirmed 2 Nov.
- **Paper naming drift:** §1 and §2.1 use "DRP-W, ETH, PCP-W" and "CCP-1". §3 uses `eth-w`,
  `ccp-1`. "ETH" has no `-W`. Use the Paper IDs from §3 throughout.
- **"Module" is undefined.** SM-1's "five modules" means DRP, PCP, CCP, CLK and ETH, but FR-8
  and §1 use "course module materials" for the `Bar Exam/Modules/` library. Add a Glossary
  entry or reword one of them.
- **Notes definition drift:** §3 says "Notes now means Pre-writes (Written) or Flowcharts
  (MCQ)". FR-11 says "Pre-writes and Templates (Written)". Make them match.
- **"practice paper"** is used in FR-9, FR-11, SM-2 and SM-4 but is not in the Glossary. It is
  folded into "Drill". Give it its own entry or use "Drill" consistently.
- **Offline is stated as fact and as open:** §1 says the exam is "open book but offline",
  while Open Question 1 asks "whether it must be offline". Soften §1 or close the question.
- **Front matter** still says `status: draft` although every assumption is confirmed. Update
  it when the PRD is promoted.
