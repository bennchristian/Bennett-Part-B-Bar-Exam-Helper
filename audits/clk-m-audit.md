# clk-m audit — Contemporary Legal Knowledge (MCQ) (read-only, 18 Nov 2026)

Sources checked: the four 2026 Learning Plans in `Bar Exam/Modules/Contemporary Legal Knowledge & Practice/`
(DPCR, Law & Technology, Comparative Laws, Conflict of Laws, `pdftotext -layout`). I also used the lecture
slides and compiled lecture notes, the Comparative fact pattern, and the statutes in Nic's Go Pack
(`.../5. CLK/PDPA/2. PDPA Statutes/`). These were checked against `study/clk-m/` (`coverage.md`,
`cheatsheets.md`, `model-questions.md`, `drills.md`, `outline.md`, `weak-spots.md`).

**Core vs non-core (visual check).** Rendered every plan page with `pdftoppm` and tested for blue and
cyan text.
- **DPCR** is the only plan with a core/non-core split. Core is black. Non-core is light-blue text:
  timetable S/N 5 (AI), the whole "Non-core" legislation block, and all "Optional" readings (p4, p6–7).
  The synopsis and reading list also name the split in words.
- **Law & Tech**, **Comparative Laws** and **Conflict of Laws** have no colour tiers. The only
  blue is hyperlinks and headings.
- Conflict of Laws says its reading list "is for your information only. All examinable content will
  come solely from the lectures and the slides". Law & Tech says the same of its list via the CS1 and
  CS2 notes. Gaps against those lists matter less.
- The EU AI Act in the Law & Tech list is stated "will not be examined" (`Compiled_Lecture_Notes_CS_2`).
  It is not a gap.

**Excluded as already assigned:** DPCR 0.X AI regulation (S/N 5; Model AI Governance Framework),
Comparative/Conflict COCAA, and the other writer-session gaps you listed. I did not re-report them.

**Method.** Same as `eth-w`: grep by name and section in `cheatsheets.md`. The pack uses short names
("Burswood" for Liao Eng Kiat, "Desert Palace" for Poh Soon Kiat), so I matched on those too.
- **covered** = an end point holds the rule or ratio.
- **thin** = a statute, regulation or Schedule is only mentioned, or only part of what the plan
  names is covered.
- **missing** = no hit.

## Summary

| Subject | Items checked | Covered | Thin | Missing | Topics with no Model Q&A |
|---|---|---|---|---|---|
| 0 Data Protection & Cyber (excl. AI) | 71 (53 core · 18 non-core) | 51 | 6 | 14 | 0 of 10 (0.X AI has 2 of 3 Sub-points unquestioned: out of scope, being written) |
| 1 Law & Technology | 28 | 26 | 0 | 2 | 0 of 10 |
| 2 Comparative Laws | 17 | 15 | 1 | 1 | 0 of 8 |
| 3 Conflict of Laws | 47 | 43 | 3 | 1 | 0 of 10 |
| **Total** | **163** | **135** | **10** | **18** | **0 of 38** |

By tier (DPCR only): core 53 → 48 covered, 3 thin, 2 missing. Non-core 18 → 3 covered, 3 thin,
12 missing. Subjects 1–3 are all "core" (no tiers).

## Core gaps (DPCR, 5 items)

| Item | Status | Plan ref | Note |
|---|---|---|---|
| **PDPA Part 10 General — s 53 (employer liable for employee's acts), ss 51–52 (offences, offences by corporations), s 56 (general penalties)** | missing | Reading List "Core — PDPA Parts 1–6, 6A, 9B, 9C, 9D and 10" (p5) | 0 hits for ss 51, 52, 53, 56. A likely MCQ ("is the employer liable for…"). It should sit next to 0-38 or 0-4. |
| **PDPA Eleventh Schedule** (specified purposes for the s 48F(4) re-identification defence) | missing | Reading List p5 | 0-38 gives s 48F but not the defence's Schedule. |
| **PDPA Part 2** (PDPC functions, delegation, cooperation, ss 5–10) | thin | Reading List p5 | Appears only as "s 5 / s 6" in other contexts. No Part 2 end point. |
| **CYSA Part 4 ss 21–23** (s 21 ID card, s 22 technical experts, s 23 emergency cybersecurity measures) | thin | Reading List p5 ("Parts 1, 3 and 4") | 0-54 covers ss 19–20 only. s 23 emergency measures is a plausible MCQ. |
| **CYSA First Schedule** (the essential-service sectors) | thin | Reading List p5 | 0-46 cites "First Schedule" but never lists the sectors. 0 hits for the sector names. |

Minor core notes. The plan lists PDPA Parts 9B, 9C and 9D; these are covered (0-35 to 0-38, 0-33).
- **ss 48K and 48M** (procedure for directions; enforcing directions in the District Court) have no hit.
- PDP Regulations 2021 Parts 2–4 and the NDB Regulations 2021 are covered.

## Non-core gaps (DPCR, 18 items: 3 covered, 3 thin, 12 missing)

Non-core in `coverage.md` is mostly "none" or one-liners. These are the actual gaps:

| Item | Status | Plan ref |
|---|---|---|
| POFMA Act 2019 ss 7–16, 20–28, 32–34, 40–43, 48 | thin | Non-core legislation, p6. One end point (0-68): "POFMA works through ministerial directions…". The section groups are not mapped. |
| POFMA Regulations 2019 regs 3–8 | thin | p6. Not cited. |
| POHA (Exempt Class of Persons) Order 2014 | thin | p6. One hit, no rule. |
| POHA (Prescribed Internet Intermediaries) Regulations 2020 | missing | p6 |
| Online Safety (Relief and Accountability) Bill 2025 | missing | p6 |
| POFMA Office Code of Practice (Prominence to Credible Online Sources) | missing | p6 |
| PDPC Guide on Active Enforcement | missing | Optional, p6 |
| PDPC Guide on Managing and Notifying Data Breaches | missing | Optional, p6 |
| CSA Singapore Cybersecurity Strategy 2021 | missing | Optional, p6 |
| CSA Singapore Cyber Landscape 2021 | missing | Optional, p6 |
| [2019] SGPDPC 22 Spize Concepts | missing | Optional, p6 |
| PDPC Case DP-2102-B7878 Singtel (no breach) | missing | Optional, p7 |
| [2023] SGPDPC 1 RedMart | missing | Optional, p7 |
| [2020] SGHC 95 Lai Kwok Kin v Teo Zien Jackson | missing | Optional, p7 |
| [2025] SGPDPC 6 Marina Bay Sands | missing | Optional, p7 |

The library holds only SingHealth and Reed v Bellingham (both covered). These case decisions are
not in the library, so any fix needs them fetched.

Covered non-core: PDPC Advisory Guidelines on Key Concepts, SingHealth/IHiS [2019] SGPDPC 3, Reed.
PDPA Part 9 (Do Not Call) and Part 9A are covered (0-27, "non-core") even though neither the core nor the
non-core lists name them. That is harmless.

## Law & Technology (2 missing, 0 thin)

| Item | Status | Plan ref | Note |
|---|---|---|---|
| Soh, *Towards a Control-Centric Account of Tort Liability for Automated Vehicles* (2021) | missing | Articles, p5 | 0 hits. The automobiles end points (1-13 to 1-16) come from the slides and don't use it. Optional. |
| Dow Jones v Gutnick (via Gary Chan, SJLS 2003) | missing | Reading List folder (not in the plan's list) | Platform defamation (1.VIII). 0 hits. Low priority. |

Covered: all seven lectures, ETA, UN MLETR, Platform Workers Act, Model AI GF, six cases, Lessig,
Easterbrook, Bennett Moses, Soh (dispositionism), Ooi, Yeong, ByBit. The CS1 and CS2 notes carry
longer starred reading lists. I read their narrative only. Check the asterisked items if time allows.

## Comparative Laws (1 thin, 1 missing)

| Item | Status | Note |
|---|---|---|
| Fact Pattern (both contact sessions) | thin | `outline.md` §3.5 lists the issues, but the cheatsheets have no end points for several. These are: (1)(b) grounds to invalidate (mistake, fraud, non-disclosure); Q4(a) the wrong-party exception; Q4(b) a court refusing fees; and costs (Q4(d)). Cl 15 entire-agreement and non-reliance vs good faith is only partly covered. The lecture slides contain no vitiating-factors material, so this may be a course gap, not a pack gap. |
| ALA, *Introduction to Indonesian contract law* pp 146–155 (optional) | missing | Not cited. |

Covered: every lecture topic and bullet (the civil-law introduction and codification, contract and
good faith, discharge, delict in Indonesia and Thailand, competence, ex aequo et bono, discovery,
privilege). Also covered: Pongsapan and the HSF privilege guide.

## Conflict of Laws (3 thin, 1 missing)

All reading-list cases are covered under short names. The list is "for your information only".

| Item | Status | Note |
|---|---|---|
| *Raffles Education v Shantanu Prakash* [2020] SGHC 83 [49]–[51], [58]–[67] | missing | Conspiracy tort. The pack uses EFT Holdings (3-9) from the slides. |
| Rules of Court 2021 O 7 r 1–3 and SCJA s 16(2) (service within jurisdiction) | thin | 3-16 and 3-17 cite s 16(1)(a)(i) and the Companies Act only. |
| Rules of Court O 2 r 5(4) (irregularity, submission) | thin | 3-31 to 3-33 cite O 6 only. |
| PD 63(1) and 63(2) (general) | thin | PD 63(3)(d), (e), (f), (p) are covered. 63(3)(r) is cited in 3-29. |

## Model Q&A audit

`model-questions.md` has 266 questions (118 existing: 40 official samples, drills and mock-1; 148
new). I counted by the Sub-point Key in each question's tag line.
- **Topics with no question:** none. All 38 Topics have at least 3.
- **Sub-points with no question: 2 of 227, both in 0.X (AI)**: 0.X.1 Model AI Governance Framework
  and 0.X.3 AI ethics. Not re-reported (writer session active).
- **Sub-points with exactly one question: 193 of 227** (85%). The thinnest Topics are
  `2.VII` ex aequo et bono (3 questions), `3.VII` submission (3), `3.IX` foreign judgments:
  recognition (3), and `1.III` Automobiles, `2.III` good faith, `2.VI` competence and `3.III` limits
  (4 each). I did not find weaker spots with more than one question each.
- **Past papers.** Nothing held for CLK: Nic's PYP folder has only the 2023 *instruction sheet*
  (`outline.md`, `PYP-CLK`), and Cyril's 2025 file is exam-day notes. The only exam-style
  questions are the 40 official sample questions (10 per subject). Each maps to a Sub-point that
  has questions. No "past-paper Sub-point" lacks a question.
- The Q&A table counts Existing 118 / New 148. The 148 "New" questions are the project's own
  and were not checked against an official key.

## Limits of this audit
- I checked mention and rule only. I did not re-verify pinpoints, or whether the end-point wording
  matches each statute (the pack records its own statutory-currency checks, `weak-spots.md`).
- The DPCR Contact Session II slides (2 Nov) are not in the library (`weak-spots.md` source gap 1).
  The plan's lecture-bullet items are therefore checked against the Act and the Go Pack only.
- The Law & Tech CS2 deck (15 Oct) is also missing (`weak-spots.md` source gap 2).
