# PCP-M audit — syllabus coverage and Model Q&A (read-only, 18 Nov 2026)

Paper `pcp-m` (PCP MCQ): Subject 0 Probate & Succession Planning, 1 Real Estate (Conveyancing),
2 Muslim Family & Succession Law, 3 Employment Law, 4 PIPD. Checked against
`study/pcp-m/coverage.md`, `cheatsheets.md` and `model-questions.md` (no `drills.md` exists).
Nothing under `study/`, `tools/` or `Bar Exam/` was edited.

## How the items were counted

The sources differ by Subject, so the unit of "item" differs. State this before reading the
counts.

| Subject | Source of the item list | Core / non-core marking | Items |
|---|---|---|---|
| 0 Probate | Detailed Syllabus (B26S1): 24 numbered headings + 91 lettered entries, with the 28 named cases and the PAA / Probate Rules / MCA provisions inside them checked by grep | Blue font, read from the PDF colour operators (core = black). Blue = non-core for the Wills Act "types of wills", "who can make a will", executors, insurance nominations, construction (a)–(b), rectification, CLA provisions, IFPA, contentious probate, and parts of the MCA procedure | 115 |
| 1 Real Estate | Learning Plan Schedule 1 key competencies (16) + Schedule 2 reference materials (5) + 25 lecture topic bullets + 5 cases on the slides | Learning Plan marks (vi) progressive payments and (vii) defects liability as blue / "non-examinable"; slides mark HDB flats "FYI only" | 51 |
| 2 Muslim | Learning Plan topic bullets (21, including the contact-session lists) + 49 cases / authorities on the three decks + the "children's judicial interview" proposition | None: the plan is not colour-coded. Slides say shares calculations and school differences are "NOT required" | 71 |
| 3 Employment | Learning Plan: 10 statutes + 4 optional further reading (blue) + 11 topic bullets + 8 cases on the two decks | Further Reading list is blue (non-core): EFMA 1990, CPF Act 1953, MOM, Ravi Chandran | 33 |
| 4 PIPD | Learning Plan reading list (22) + 20 lecture topic bullets + 1 case on the slides | Colour read from the PDF **and** confirmed on page images: non-core = Intro lecture, "At Lawyer's Office", pre-writ considerations heading, post-judgment, Workmen Injury Compensation, MAG / Damages Guidelines / Practitioners Library / Actuarial Tables, *Ng Kong Choon*, the pre-action protocols (PD 2014 and 2021), MIB, multi-vehicle collisions, limitation, *Salmizan* (SGHC), MVA post-judgment, PT Circular, intervening for insurers | 43 |

Case and statute names were extracted from the slides with pdftotext and a regex, then grepped
against `cheatsheets.md`; names the regex missed or garbled were checked by hand. Topic bullets
were checked against `coverage.md` and block titles. *Covered* = a block states a usable rule or
holding. *Thin* = named but no holding or rule. *Missing* = not in the pack. This was a presence
and substance check, not a re-verification of points of law. Blue-font attribution for Probate
relies on colour operators that can bleed across paragraphs, so a few non-core labels may be
off by one paragraph.

**Do not re-report** (writer sessions are on them): clk-m, drp-w-cl, pcp-w Family non-core, ccp-2
merger control. None of those is a `pcp-m` item.

## Summary

| Subject | Items checked | Covered | Thin | Missing | Topics with no Model Q&A |
|---|---|---|---|---|---|
| 0 Probate & Succession Planning | 115 | 106 | 9 | 0 | 0 of 9 |
| 1 Real Estate (Conveyancing) | 51 | 51 | 0 | 0 | 0 of 9 |
| 2 Muslim Family & Succession Law | 71 | 66 | 0 | 5 | 0 of 9 |
| 3 Employment Law | 33 | 33 | 0 | 0 | 0 of 8 |
| 4 PIPD | 43 | 40 | 2 | 1 | 0 of 9 |
| **Total** | **313** | **296** | **11** | **6** | **0 of 44** |

Core gaps: 4 thin (Probate) + 1 thin and 1 missing (PIPD) + 5 missing (Muslim, unclassified, all
case citations) = 11. Non-core gaps: 5 thin (Probate) + 1 thin (PIPD) = 6. This is a strong pack:
the syllabus coverage is close to complete, and the gaps are single cases and procedural cites.
The larger weakness is Model Q&A depth (below).

---

## Part A — Syllabus gaps (core first)

### A1. Core gaps

| # | Subject | Item | Learning Plan / Syllabus reference | Status | Pack location and what is missing |
|---|---|---|---|---|---|
| 1 | PIPD | State Courts Practice Directions **2014 edition, Appendix C and Appendix E** | PIPD LP reading list, "At the Scene" (bold = core) | **Missing** | The pack cites only the 2021 PD (App B protocol, App C CDR write-up, App D benchmark rates, App A1 forms). Nothing on 2014 App C or E (0 hits). TODO: find what they contain and whether the 2021 PD superseded them; the pack should say so |
| 2 | PIPD | *Lee Song Yam v Hafizah bte Abdul Rahman* [2019] SGMC 24 (SJE) | PIPD LP timetable (State Courts – SJE) and reading list, core | Thin | `pcp-m-4-28` (line 3333) calls it "optional reading" and gives no holding. The LP lists it in bold core. State what it held on the single joint expert |
| 3 | Probate | *Chan Yuen Lan v See Fong Mun* [2014] 3 SLR 1048 (CA) | PR-SYL 6(a)(iii), joint tenancies, core | Thin | `pcp-m-0-3` (line 58): "no holding is relied on". The block has s 66A(3) CLPA and s 53(5) LTA but not the case |
| 4 | Probate | *Ong Chai Soon v Ong Chai Koon* [2022] 2 SLR 457 (CA) | PR-SYL 6(a)(iv), core | Thin | Same note, no holding |
| 5 | Probate | *WWI v WWJ* [2024] SGFC 22 (testamentary capacity) | PR-SYL 4(a)(iii), core | Thin | `pcp-m-0-11`: name in keywords and the Source note only; the block gives *ULV*, *XBO* and *Chee Mu Lin* propositions but not *WWI* |
| 6 | Probate | *WKR v WKQ* [2023] SGHC(A) 35 (principles in resealing a foreign grant) | PR-SYL 3(a)(v), core | Thin | Keyword line only in `pcp-m-0-67` (line 903); the s 47(4) rule is stated, the case holding is not |
| 7 | Muslim | *Mohamed Salleh v Habibah* (1997) 1 SSAR 84 and *AM v AN* [2012] 6 SSAR 202 | MU2, talak: SYC hears the evidence of the parties and witnesses | **Missing** (cases) | The talak block (`pcp-m-2-16`) states the procedure and cites *BQ v BR* only. Add the two authorities if Bennett wants the cases for the disputed-pronouncement point |
| 8 | Muslim | *DR v DS* [2021] 8 SSAR (SYC applies *TNL v TNK* single-income and broad-brush) | MU2, matrimonial assets | **Missing** (case) | Not cited; check 2.V block for whether the proposition is stated |
| 9 | Muslim | *AZB v AZC* [2016] SGHCF 1, and the proposition that SYC judges do not interview children while civil courts may | MU2 slide, custody | **Missing** | No judicial-interview / child's-wishes point in the Muslim custody block (0 hits for "interview") |

The 5 Muslim items counted in the summary are: *Mohamed Salleh*, *AM v AN*, *DR v DS*, *AZB v AZC*, and
the "SYC does not interview children" proposition.

### A2. Non-core gaps

| # | Subject | Item | Reference | Status | Pack location |
|---|---|---|---|---|---|
| 10 | Probate | *VTL v VTM* [2021] SGHCF 30 (mutual wills) | PR-SYL 1 (blue) | Thin | `pcp-m-0-9` Source note: "not summarised in the Course Materials"; test is taken from *Hiroto Watanabe* |
| 11 | Probate | *TWD v UQE* [2019] 3 SLR 662 at [56]–[84] (third-party intervention in deputyship) | PR-SYL 5(a)(iii) (blue) | Thin | Line 1170: named, no holding |
| 12 | Probate | Administration pending trial (s 20 PAA; P 7 r 21 Probate Rules) | PR-SYL 5(d) (blue) | Thin | Keyword and a one-line list item in `pcp-m-0-68`; no rule |
| 13 | Probate | Costs in probate actions (P 16 r 3(5) Probate Rules) and costs of deputyship (P 22 r 4, r 10 General Rules) | PR-SYL 5(e), 5(a)(iii) (blue) | Thin | Cited by number only |
| 14 | Probate | Litigation representative for P (P 6 r 4, r 10 General Rules; FJC PD paras 64, 67) | PR-SYL MCA 5(a)(iii) (blue) | Thin | One mention in the deputyship block |
| 15 | PIPD | Pre-action protocol under **PD 2014** (the LP lists "PD 2014 and PD 2021" for NIMA / PIMA) | PIPD LP reading list (blue) | Thin | The pack covers the 2021 protocol (App B) only; no statement of what changed from 2014 |

### A3. Covered strongly (spot-checked, no gap)

- **Probate:** all named cases not listed above have a stated proposition (*Low Ah Cheow*, *Cheo
  Yeoh*, *Chee Mu Lin*, *Lim Chen Yeow*, *Yang Chun*, *Chye Seng Kait*, *Foo Jee Seng*, *Zhao Hui
  Fang*, *Lau Tyng Tyng*, *Loke Soh Lui*, *Low Gim Har*, *Mahidon*, *Kuek Siang Wei*, *Lee Suet
  Fern*, *Lim Weipin*, *Chng Heng Tee*, *Low Guang Hong*, *AAG*, *AOS*, *Toh Seok Kheng*, *Teo Gim
  Tiong*, *Lee Han Tiong*, *Wong Moy*, *Mustaq*, *Tacplas*, *Re BKR*, *BUV v BUU*, *Sum Chong Mun*).
  Probate Rules, PAA, MCA, ISA, IFPA and PD paragraph cites were found for every procedural step
  checked (grant, caveat, citation, schedule of assets, bond, resealing, foreign domicile, 6-month
  delay).
- **Real Estate:** all 16 Schedule 1 competencies and all 5 Schedule 2 references map to blocks
  (the Safeguarding Conveyancing Money Guidebook Part D is covered under "Conveyancing Money
  Guidebook (2012)" in `pcp-m-1-47`). Both non-examinable items (progress payments, defects
  liability) are in `pcp-m-1-36`, labelled. Caveat: I could not check the Conditions of Sale 2020
  clause by clause because the Conditions are not in the module folder.
- **Employment:** every Act on the Learning Plan is in the pack, and all eight lecture cases.
  *Uday Mehra*, *Phosagro* and *RDC Concrete* appear as authorities for the four summary-dismissal
  situations in `pcp-m-3-31`.

---

## Part B — Model Q&A audit

Counts use the Sub-point Keys in each question's tag line (a question testing two Sub-points
counts under both). **"Real" = a 2026 Sample Question, a Probate practice paper, or a held
past-paper part.** No Muslim, Employment or PIPD past paper exists and the 2023 and 2025 MCQ
papers are held only as case facts, so for those Subjects the real questions are the 10 Sample
Questions (and the pack's own questions are the rest).

| Topic | Questions touching it | of which real (SQ / past paper / practice paper) | Sub-points | Sub-points with no real question |
|---|---|---|---|---|
| 0.I Succession planning tools and assets outside the will | 7 | 0 | 7 | 7 |
| 0.II Wills: who can make one, formalities, witnesses, capacity | 10 | 2 | 9 | 8 |
| 0.III Construction of wills, failure of gifts, revocation and alteration | 17 | 4 | 15 | 11 |
| 0.IV Taking instructions, will clauses, executors and ethics | 8 | 2 | 6 | 5 |
| 0.V Intestate Succession Act | 10 | 2 | 9 | 6 |
| 0.VI Dying testate v dying intestate | 2 | 1 | 1 | 0 |
| 0.VII Inheritance (Family Provision) Act and maintenance of parents | 7 | 0 | 7 | 7 |
| 0.VIII Grants of representation: probate, administration, resealing, contentious matters | 24 | 10 | 17 | 7 |
| 0.IX Mental Capacity Act: principles, LPAs, deputies, Public Guardian | 21 | 8 | 16 | 11 |
| 1.I Introduction: parties, property types, regulations and formalities | 6 | 0 | 6 | 6 |
| 1.II Searches, title and legal requisitions | 8 | 2 | 6 | 5 |
| 1.III Option to purchase, contract terms, stakeholding and caveats | 12 | 5 | 8 | 3 |
| 1.IV Stamp duties: BSD, ABSD, SSD, remissions and penalties | 11 | 3 | 8 | 2 |
| 1.V Foreign ownership: Residential Property Act | 3 | 1 | 3 | 2 |
| 1.VI Sale of a residential property: vendor's side, bank and CPF | 5 | 0 | 5 | 5 |
| 1.VII Mortgages and CPF | 7 | 2 | 5 | 2 |
| 1.VIII Completion accounts and conveyancing money | 6 | 0 | 6 | 6 |
| 1.IX Completion process and late completion | 6 | 2 | 5 | 2 |
| 2.I Applicability of Muslim law and AMLA | 3 | 0 | 3 | 3 |
| 2.II Jurisdiction of the Syariah Court | 8 | 4 | 6 | 2 |
| 2.III Concurrent and residual jurisdiction with the civil courts; finality | 4 | 0 | 4 | 4 |
| 2.IV Divorce at the Syariah Court: types, grounds, process | 9 | 3 | 8 | 5 |
| 2.V Ancillary orders: nafkah iddah, mutaah, children and matrimonial assets | 8 | 3 | 7 | 4 |
| 2.VI Enforcement of SYC orders | 3 | 2 | 2 | 0 |
| 2.VII Muslim law of inheritance (faraid) | 5 | 0 | 5 | 5 |
| 2.VIII Muslim wills | 4 | 0 | 4 | 4 |
| 2.IX Civil courts and Muslim inheritance disputes | 6 | 0 | 6 | 6 |
| 3.I Legislative framework and classes of employees | 5 | 1 | 5 | 4 |
| 3.II Statutory rights and obligations: pay, hours, leave, retirement, safety | 10 | 3 | 8 | 5 |
| 3.III The employment contract: express terms, implied terms, variation | 3 | 0 | 3 | 3 |
| 3.IV Industrial relations | 3 | 0 | 3 | 3 |
| 3.V Harassment, bullying and discrimination | 5 | 0 | 5 | 5 |
| 3.VI Performance management and misconduct | 5 | 1 | 4 | 1 |
| 3.VII Termination of employment | 7 | 5 | 5 | 1 |
| 3.VIII Wrongful dismissal and remedies | 4 | 2 | 4 | 2 |
| 4.I Legal framework and references | 4 | 0 | 4 | 4 |
| 4.II At the scene: immediate steps and the GIA Motor Claims Framework | 4 | 3 | 4 | 1 |
| 4.III At the lawyer's office: claimant's and defendant's options; repudiation; MIB | 4 | 1 | 4 | 3 |
| 4.IV Pre-action protocol for PI and NIMA claims (State Courts PD Appendix B) | 8 | 5 | 6 | 1 |
| 4.V FIDReC Non-Injury Motor Accident scheme | 3 | 0 | 3 | 3 |
| 4.VI Other pre-writ issues: multiple collisions, limitation, one action | 3 | 1 | 3 | 2 |
| 4.VII Where to sue and how the courts manage PIPD cases | 5 | 1 | 4 | 3 |
| 4.VIII Trials and assessment of damages | 2 | 0 | 2 | 2 |
| 4.IX Post-judgment and other matters: Public Trustee, insurers, work injury | 3 | 0 | 3 | 3 |

### Findings

1. **No Topic is without a question and no Sub-point is without a dedicated one.** All 254
   Sub-points have at least one question filed under them. 287 questions in all: 50 Sample
   Questions, 7 Probate practice-paper questions (PR-PP1 and PR-PP2), a handful of 2021 REP
   parts, and 210 own questions.
2. **Depth is thin.** 193 of the 254 Sub-points have exactly one question (Probate 64 of 87,
   Real Estate 34 of 52, Muslim 37 of 45, Employment 29 of 37, PIPD 29 of 33).
3. **Sub-points with no real question:** 174 of 254 (Probate 62, Real Estate 33, Muslim 33,
   Employment 24, PIPD 22). That is expected where no past paper exists, but it means most of the
   pack is practised only on the pack's own questions.
4. **Topics with no real question at all (17):** 0.I, 0.VII, 1.I, 1.VI, 1.VIII, 2.I, 2.III, 2.VII,
   2.VIII, 2.IX, 3.III, 3.IV, 3.V, 4.I, 4.V, 4.VIII, 4.IX. Of these, the heaviest-weight Topics
   are **2.VII faraid / 2.VIII Muslim wills / 2.IX civil courts and Muslim inheritance** (the
   whole of the Muslim inheritance lecture has no real question), **0.VII IFPA** (non-core by the syllabus's blue
   font, but it names five cases) and **1.VI sale of a residential property, 1.VIII completion accounts**
   (both are worked-calculation Topics).
5. **Topics with only two or three questions in all:** 0.VI (2), 1.V (3), 2.I (3), 2.VI (3), 3.III
   (3), 3.IV (3), 4.V (3), 4.VI (3), 4.VIII (2), 4.IX (3). Probably under-served: **4.VIII Trials
   and assessment of damages** (two questions) and **3.III the employment contract** (three).
6. **Real questions the pack left unanswered.** PR-PP2 Q3 (what an LPA donee may do: gifts to
   herself, settling assets on trust) and 2021 REP Q2.3 (ABSD count for a flat under contract to
   be sold) are named in "Left out" as unanswerable. The Probate half is now answerable from
   `pcp-m-0-80` (line 1090: no cash gifts unless expressly authorised, s 14(3)
   MCA); that statement in `model-questions.md` looks stale.
7. **Past-paper evidence.** The pack's `coverage.md` records no PYP mapping for `pcp-m` ("Tested
   is —", PYP mapping deferred to Phase 2); I did not find a Sub-point whose real-source tag
   claims a paper that has no question. The only real PCP Paper 2 sources held are in
   `Nic_s Part B Package/3. PYP/PYP index.md`, and they match what is in the Q&A.

---

## Five most important gaps (pcp-m)

1. **PIPD: State Courts PD 2014 Appendix C and E (core reading list) are not in the pack**
   (it knows only the 2021 PD). Needs a TODO or a "superseded" note.
2. **Muslim inheritance has no real question and the case coverage has three gaps**
   (talak-proof cases, the SYC's use of *TNL v TNK*, the child-interview point). Add the three
   cases and a judicial-interview line to the custody block.
3. **Probate core cases cited with no holding:** *Chan Yuen Lan*, *Ong Chai Soon*, *WWI v WWJ*,
   *WKR v WKQ*. A MCQ on a joint-tenancy case or a resealing principle would hit these.
4. **Model Q&A is one question per Sub-point** for 193 of 254 Sub-points, and 174 have no real
   question; the thinnest Topics are 4.VIII, 0.VI, 3.III, 3.IV and the Muslim inheritance Topics.
5. **PIPD *Lee Song Yam*** is core, one line, "optional reading" in the pack: reconcile with the
   Learning Plan.
