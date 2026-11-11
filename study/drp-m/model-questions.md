# DRP-M — Model Questions and Answers

Paper `drp-m`, DRP Paper 2 (MCQ), Wed 2 Dec 2026, 2:30–4:30pm. Subjects: 0 Arbitration · 1 Mediation Advocacy. Written 11 Nov 2026 as Markdown only, on Bennett's instruction of that day; no PDF is built until Phase 2 (`python3 tools/build_pack.py drp-m --questions`).

**How the file runs.** Four parts: Arbitration past-paper questions, Mediation Advocacy past-paper questions, then Arbitration Drills and Mediation Advocacy Drills. Within each part the order is Topic → Sub-point, as in `coverage.md`. Each past-paper question sits under the Sub-point it mainly tests; any other Sub-point it tests carries a "See …" line pointing to it. The Drills cover every Sub-point no past paper has tested, so every Topic has at least one answered question, plus 12 extra drills on the seven elements of negotiation (MED-4). Each Topic opens with a line listing which Sub-points were tested and which drills cover the rest.

**How to read a question.** The tag line gives the question ID · the Sub-point Keys (`coverage.md`) · the source · the end-point block(s) in `cheatsheets.md` that hold the rule. The answer follows the options: why it is right, why each other option is wrong, then the cite. Cites use the source key in `outline.md`. Cover the answer, answer it, then check; log every miss in `weak-spots.md` under its Key.

**Question IDs.** `Q2023-<n>` = 2023 DRP Paper 2, question n. `QSQ-A<n>` / `QSQ-M<n>` = 2026 Sample Questions, Arbitration / Mediation question n. `Q2021A-…` / `Q2021M-…` = 2021 ARB / MED papers (written). `Qdrill-<n>` = drill n.

**Sources.** Question text is transcribed from the papers in `Bar Exam/Seniors Notes/Nic_s Part B Package/3. PYP/` and from `Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf` ("SampleQs"). Words in [square brackets] are not in the paper. The papers held (see `PYP index.md` there) are:

- **PYP 2023** — `2023 PYP/DRP Paper 2.pdf`: "Part B Bar Examinations 2023 (Main)", DRP Paper 2, Wednesday 6 December 2023, 60 MCQs on Examplify (Arbitration Qs 1–36, Mediation Advocacy Qs 37–60). The PDF is 60 screenshots taken by a former candidate (PDF page = Q − 7 for Qs 8–60; pp 54–60 = Qs 1–7). Q1's screenshot is cropped, so its number is inferred; Q2 survives only as the candidate's typed note. The "Currently Selected" answers on the screenshots are the candidate's, not an answer key, and are wrong in several places (Q19, Q23, Q25, Q30, noted at each). **There is no official key**: every 2023 answer here is this project's own, from `cheatsheets.md` and the primary texts.
- **SampleQs** — Arbitration Qs 1–10 (p56–59) and Mediation Advocacy Qs 1–10 (p60–63), with the **official key** at p122. Qs 1–5 of each are labelled "[Part B 2023-S]" (a 2023 sitting not otherwise held) and Qs 6–10 "[Part B 2024]" (no 2024 paper is held). Each answer below matches the official key.
- **PYP 2021 ARB** — `2021 PYP/ARB 2021 Exam.pdf`: "The Law and Practice of Arbitration Practice", Part B 2021 (Main), Tuesday 14 December 2021. Two written questions, each with parts (a)–(b).
- **PYP 2021 MED** — `2021 PYP/MED 2021 Paper.pdf`: Mediation Advocacy, Part B 2021 (Main). Written: Q1 (ten short questions, 70 marks) and Q2 (one problem, 30 marks).

No 2018–2020, 2022, 2024 or 2025 Arbitration or Mediation paper is held. The 2021 papers are written; their answers are given as short model answers in the same Sub-point places, because 2026 is MCQ only and they show the issues each Topic raises.

**The law.** Every answer follows `cheatsheets.md`, which states statutes and rules as in force on 9 Nov 2026 (IAA and AA as at 9 Mar 2025; ROC 2021 as at 1 Apr 2026; SIAC Rules 2025; Mediation Act 2017; PCR 2015; Practice Directions as last updated in 2026). Where a past paper assumed older law, the answer gives the current law and a "What changed" line says what the paper assumed. Points that go beyond a Cheatsheet block were checked against the primary texts in `study/drp-m/authorities/`. An "open point, no authority" states both views where the law is unsettled.

Self-study only: never use this file with a live quiz, the Mock Exam or another assessment (Handbook §7.11). The 2023 paper is the candidate Practice Paper (`drills.md`): if Bennett means to sit it unseen, he should skip the questions tagged `PYP 2023` until he has.

| Subject | Past-paper questions | Drills | Total |
|---|---|---|---|
| 0 Arbitration | 36 (2023) + 10 (SampleQs) + 5 (2021 parts) = 51 | 107 | 158 |
| 1 Mediation Advocacy | 24 (2023) + 10 (SampleQs) + 20 (2021 parts) = 54 | 32 | 86 |
| **Total** | **105** | **139** | **244** |

## 0 · Arbitration — past-paper questions

### 0.I Applicable laws and the IAA framework

Sub-points 0.I.1–0.I.12. Tested: 0.I.1, 0.I.2, 0.I.3, 0.I.5, 0.I.6, 0.I.8, 0.I.11. Drills 1–5 cover 0.I.4, 0.I.7, 0.I.9, 0.I.10 and 0.I.12.

### 0.I.1 — The laws that apply in an arbitration

**Q2023-3** · `0.I.1` · PYP 2023 Q3 · `drp-m-0-1`

In an ad hoc arbitration between an English party and an Indian party that is seated in Singapore, the lex arbitri (or the procedural law governing the conduct of the arbitration) is

A. English law.
B. Indian law.
C. Singapore law.
D. All of the options are accurate.

**Answer: C.** The lex arbitri is the law of the seat, so a Singapore seat means Singapore law: here the IAA, since the parties have their places of business outside Singapore (IAA s 5(2)(a)). A and B: the parties' nationalities do not fix the procedural law; English or Indian law might govern the contract or a party's capacity, not the conduct of the arbitration. D: only one lex arbitri applies.
*Cite: ARB-SN p6 paras 13–14; IAA s 5(2)(a)*

### 0.I.2 — When the IAA applies: "international" arbitration or opt-in

**QSQ-A1** · `0.I.2` · Sample Questions (Part B 2023-S) Arbitration Q1 · `drp-m-0-2`

What is the primary legislation governing international arbitration in Singapore?

A. Singapore Arbitration Act.
B. Singapore International Arbitration Act.
C. Singapore Commercial Arbitration Act.
D. New York Convention.

**Answer: B.** Part 2 of the International Arbitration Act 1994 and the Model Law apply to an "international" arbitration (s 5(2)), or to any arbitration whose parties agree in writing (s 5(1)). A: the Arbitration Act 2001 governs domestic Singapore-seated arbitrations (AA s 3). C: no such Act exists. D: the NYC is a treaty on enforcing foreign awards, given effect by IAA Part 3; it is not the governing legislation. Official key: B.
*Cite: IAA s 5(1)–(2); AA s 3; SampleQs p56 Q1, key p122*

See also Q2021A-2b under 0.II.5 (two Singapore companies: the AA, not the IAA, applies).

### 0.I.3 — Model Law has the force of law, except Chapter VIII; 2006 amendments not enacted

**Q2023-1** · `0.I.3` · PYP 2023 Q1 · `drp-m-0-3`

The UNCITRAL Model Law on International Commercial Arbitration ("Model Law") is incorporated into Singapore law by way of

A. The Supreme Court of Judicature Act.
B. The International Arbitration Act.
C. The International Arbitration Act and the Arbitration Act.
D. All of the options are accurate.

**Answer: B.** The Model Law, except Chapter VIII, has the force of law in Singapore under IAA s 3(1); it is set out in the IAA's First Schedule. C: the AA borrows many Model Law provisions in its own words but does not give the Model Law the force of law. A: the SCJA confers court jurisdiction; it does not enact the Model Law. D fails with A and C.
*Cite: IAA s 3(1); [2013] SGCA 57 at [86]*

### 0.I.5 — Institutional v ad hoc arbitration; UNCITRAL Rules v Model Law

See Q2023-9 under 0.XIII.1 (party autonomy includes choosing institutional or ad hoc arbitration).

### 0.I.6 — Institutional rules v the lex arbitri: which prevails (IAA ss 15, 15A)

**Q2023-10** · `0.I.6` · PYP 2023 Q10 · `drp-m-0-6`

Parties to an international arbitration seated in Singapore may agree to adopt institutional arbitration rules. Once institutional arbitration rules are adopted by the parties

A. Every provision of the institutional rules shall be given effect.
B. Every provision of the institutional rules shall be given effect unless the provision is inconsistent with the International Arbitration Act.
C. Every provision of the institutional rules shall be given effect unless the provision is inconsistent with the International Arbitration Act and the Model Law.
D. Every provision of the institutional rules shall be given effect unless the provision is inconsistent with a non-derogable provision of the Model Law or the International Arbitration Act.

**Answer: D.** IAA s 15A(1): the rules apply to the extent they are not inconsistent with a provision of the Model Law or Part 2 from which the parties cannot derogate. A rule that departs from a *default* ("unless otherwise agreed") provision is not inconsistent (s 15A(5)). A: mandatory provisions still prevail (SIAC25 r 1.6 says the same). B and C: a clash with a non-mandatory provision does not displace the rule.
*Cite: IAA s 15A(1), (3)–(5); [2009] SGCA 24 at [41]–[43]; SIAC25 r 1.6*

### 0.I.8 — Seat v venue; seat is not fixed by the institution; choosing a seat

**Q2023-12** · `0.I.8` · PYP 2023 Q12 · `drp-m-0-8`

Assuming that an arbitration is seated in Singapore

A. Parties must conduct all hearings in Singapore.
B. Parties must conduct at least one hearing in Singapore.
C. Parties can conduct hearings in any location.
D. Parties are prohibited from conducting virtual hearings.

**Answer: C.** The seat is a juridical concept; hearings may be held anywhere, including virtually, without changing the seat (Model Law Art 20(2); *PT Garuda Indonesia v Birgen Air* [2002] SGCA 12). A and B: no rule requires any hearing at the seat. D: virtual hearings are allowed; the Expedited Procedure even makes remote hearings the default (Sch 3).
*Cite: MAL Art 20(1)–(2); [2002] SGCA 12*

**Q2023-5** · `0.I.8` `0.III.7` · PYP 2023 Q5 · `drp-m-0-8` `drp-m-0-24`

Which of the following statements is true as a matter of Singapore law

A. Parties can choose a foreign arbitral institution to administer their arbitration seated in Singapore only if their dispute involves foreign elements.
B. Parties must choose Singapore International Arbitration Centre to administer their arbitration if the seat of arbitration is in Singapore.
C. Parties must choose an arbitral institution with offices in Singapore to administer their arbitration if the seat of arbitration is in Singapore.
D. Parties can choose Singapore International Arbitration Centre to administer their arbitration regardless of where the seat of arbitration is.

**Answer: D.** The institution does not fix the seat, and SIAC (like ICC, HKIAC, LCIA) can administer an arbitration seated anywhere. A, B and C: Singapore law imposes no requirement that a Singapore-seated arbitration use SIAC, a locally based institution, or a domestic institution for domestic disputes; party autonomy governs the choice.
*Cite: ARB-SN p5–6 paras 9–12 (see `drp-m-0-8`, `drp-m-0-24`)*

**Q2023-2** · `0.I.8` `0.XV.7` · PYP 2023 Q2 (text from a candidate's note; no screenshot) · `drp-m-0-8` `drp-m-0-118` `drp-m-0-46`

For an arbitration not seated in Singapore, which of the following apply?

A. The IAA
B. Certain parts of the IAA and the Model Law
C. The MAL
D. None of the above

**Answer: B.** The Model Law applies only where the seat is in Singapore, except Arts 8, 9, 35 and 36 (Art 1(2)): so a Singapore court still stays proceedings for a foreign-seated arbitration (Art 8; IAA s 6) and may grant interim relief (Art 9; IAA s 12A(1)(b), "irrespective of whether the place of arbitration is in the territory of Singapore"), and IAA Part 3 enforces foreign awards. A and C: neither the whole IAA nor the whole Model Law applies; setting aside, for example, is only at the seat. D: some provisions plainly do apply. The 2023 wording survives only in a candidate's note; read it with care.
*Cite: MAL Art 1(2); IAA ss 6, 12A(1)(b), 27–31*

### 0.I.11 — Law governing the arbitration agreement (BNA v BNB; Anupam Mittal)

**Q2023-26** · `0.I.11` · PYP 2023 Q26 · `drp-m-0-11`

In Singapore, in the absence of an express provision stipulating the law of the arbitration agreement, the law of the arbitration agreement is

A. Always the proper or applicable law of the main contract.
B. Presumed to be the proper or applicable law of the main contract.
C. The law having the closest connection to the arbitration agreement.
D. Singapore law.

**Answer: B.** Absent an express choice there is a rebuttable presumption that the law of the main contract governs the arbitration agreement; it is displaced if that law would negate a clear intention to arbitrate (*BNA v BNB* [2019] SGCA 84; *Anupam Mittal v Westbridge* [2023] SGCA 1 at [74]). A: "always" ignores the rebuttal. C: closest connection (usually the seat) is the third stage, used only where there is no express or implied choice. D: Singapore has no rule defaulting to Singapore law (contrast England's Arbitration Act 2025 s 6A, which defaults to the seat).
*Cite: [2019] SGCA 84 at [55]; [2023] SGCA 1 at [74]*

**Q2023-27** · `0.I.11` `0.VII.2` · PYP 2023 Q27 · `drp-m-0-11` `drp-m-0-47`

Which system of law will the Singapore courts apply to determine whether the arbitration agreement is "null and void" under section 6 of the International Arbitration Act?

A. The law of the place where the claimant is incorporated.
B. The law governing the main contract between the parties.
C. The law governing the arbitration agreement between the parties.
D. The law of the place where the respondent is incorporated.

**Answer: C.** Validity of the arbitration agreement, including whether it is "null and void" for a s 6(2) stay, is governed by the law of the arbitration agreement (*BNA v BNB* [2019] SGCA 84 at [55]). B: the main contract's law is only the presumptive starting point for identifying that law; by separability the clause has its own governing law. A and D: incorporation governs capacity, not validity.
*Cite: [2019] SGCA 84 at [55]; IAA s 6(2)*

### 0.II Domestic arbitration under the Arbitration Act 2001

Sub-points 0.II.1–0.II.5. Tested: 0.II.1 (inside Q2021A-2b), 0.II.4, 0.II.5. Drills 6–7 cover 0.II.2 and 0.II.3.

### 0.II.4 — Appeal on a question of law and exclusion agreements (ss 49–50 AA)

**QSQ-A6** · `0.II.4` · Sample Questions (Part B 2024) Arbitration Q6 · `drp-m-0-16`

Your client, XYZ Pte Ltd, is a company incorporated in Singapore and is a party to an arbitration seated in Singapore. The Chief Executive Officer of XYZ Pte Ltd, Mr Arby, is concerned that the arbitral tribunal may render an award against the company and wishes to be prepared for all possible outcomes, including the possibility of an appeal. Mr Arby seeks your advice on the Singapore Arbitration Act.

Which of the following statements is CORRECT?

I. Under the Singapore Arbitration Act, XYZ Pte Ltd cannot appeal against an arbitral award on a question of law.
II. Under the Singapore Arbitration Act, XYZ Pte Ltd may always appeal against an arbitral award on a question of law.
III. Under the Singapore Arbitration Act, XYZ Pte Ltd may appeal against an arbitral award on a question of law, but only with the agreement of all parties and the leave of the Court.

A. I only.
B. II only.
C. III only.
D. None of the above.

**Answer: D.** AA s 49(1) allows an appeal on a question of law arising out of an award, so I is wrong. It is not "always": the parties may exclude it (s 49(2)), and it needs the agreement of all other parties *or* the Court's permission (s 49(3)), so II is wrong. III is wrong because it demands both consent *and* permission; either suffices. Official key: D.
*Cite: AA s 49(1)–(3), (5); SampleQs p57 Q6, key p122*

**QSQ-A10** · `0.II.4` · Sample Questions (Part B 2024) Arbitration Q10 · `drp-m-0-16`

Parties to a domestic Singapore arbitration governed by the Arbitration Act have agreed in their arbitration agreement that "there shall be no right of appeal on any question of law arising from any award." Following an award against it, the losing party applies to the High Court under s 49 of the Arbitration Act for leave to appeal on a question of law. The winning party contends the contractual exclusion agreement bars the application entirely. Which of the following is most likely to be correct?

A. The exclusion agreement is void as contrary to public policy, because s 49 rights are mandatory provisions of the Arbitration Act that cannot be excluded.
B. The exclusion agreement is effective.
C. The exclusion agreement is effective only if it was entered into after the dispute had arisen; an exclusion clause in a pre-dispute arbitration agreement has no effect on s 49 rights.
D. The court retains a residual discretion to grant leave notwithstanding the exclusion agreement where the question of law is one of general public importance.

**Answer: B.** Section 49(1) operates "unless otherwise agreed by the parties", and s 49(2) treats an agreement to dispense with reasons as an exclusion, so an express exclusion in the arbitration agreement is effective whenever made. A: s 49 is not mandatory. C: the AA draws no pre-dispute/post-dispute distinction. D: "general public importance" is one of the s 49(5) conditions for permission where appeal is available; it cannot override an exclusion. Note: the SIAC Rules' waiver of recourse (SIAC25 r 51.6) has the same effect. Official key: B.
*Cite: AA s 49(1)–(2), (5); SIAC25 r 51.6; SampleQs p59 Q10, key p122*

### 0.II.5 — Other AA defaults: sole arbitrator, appointment, setting aside under s 48

**QSQ-A2** · `0.II.5` `0.IV.2` · Sample Questions (Part B 2023-S) Arbitration Q2 · `drp-m-0-17` `drp-m-0-26`

Under the Singapore Arbitration Act, an arbitration agreement must be:

A. In writing.
B. Made by way of a deed.
C. Approved by the Singapore International Arbitration Centre.
D. Witnessed by legal counsel or a notary public.

**Answer: A.** An arbitration agreement must be in writing (AA s 4(3); IAA s 2A(3) is the same), which is satisfied if its content is recorded in any form, including electronically (AA s 4(4)–(5)). B, C and D: no deed, institutional approval or witnessing is required. Official key: A.
*Cite: AA s 4(3)–(5); SampleQs p56 Q2, key p122*

**PYP 2021 ARB Q2 facts.** Parable Investments Pte Ltd and Star Movement Pte Ltd, both Singapore companies, agreed that Star would produce an animation series for Parable. The clause referred any dispute to "arbitration in Singapore by a sole arbitrator mutually agreed to or in the absence of such agreement, appointed by the President of the SIAC Court … in accordance with the SIAC Arbitration Rules, for the time being in force", and required the arbitrator to be "a person who has a Fine Arts degree from a reputable college as well as having the necessary qualifications in arbitration". The pandemic kept Star's two Malaysian film-makers out of Singapore; Star asked to extend delivery by 10 months, Parable refused, and Star missed the deadline. In July 2020 the SIAC President appointed Prof James Morgan (MFA and MBA from the Tisch School of the Arts, NYU; PhD from Exeter in partnership with the London Film School; FCIArb). The arbitration ran from September 2020 to June 2021. On 15 September 2021 the award found for Star on force majeure and held Parable's refusal to vary the timeline unreasonable. Parable's General Counsel proposes to set the award aside because (1) Prof Morgan's "MFA/MBA may be more of a business degree", so Parable did not get the arbitrator it agreed to; and (2) Prof Morgan refused to postpone the hearing until Parable's chosen counsel, Dr James Crick QC, could travel to Singapore, so the GC had to present the case himself, in breach of Parable's right to present its case and of natural justice. Star asks you: (a) What are the merits of the grounds? (b) Is the setting aside likely to succeed?

**Q2021A-2b** · `0.II.5` `0.II.1` `0.XVIII.2` · PYP 2021 ARB Q2(b) · `drp-m-0-17` `drp-m-0-13` `drp-m-0-139`

[Facts above.] Is Parable's application to set aside likely to succeed? (Answer under current law.)

**Answer.** No. First identify the regime. Both companies have their places of business in Singapore, the seat is Singapore and the work was to be done in Singapore, so the arbitration is not "international" under IAA s 5(2) and, absent a written opt-in (s 5(1)), it is a domestic arbitration under the AA (AA s 3). Adopting the SIAC Rules does not change that. So the application is under AA s 48, whose grounds mirror Model Law Art 34(2) and IAA s 24 in one section: composition not as agreed (s 48(1)(a)(v)), inability to present one's case (s 48(1)(a)(iii)), and breach of natural justice causing prejudice (s 48(1)(a)(vii)). It must be brought within 3 months of receiving the award, i.e. by 15 December 2021 (s 48(2)). Ground (1) fails on the facts (an MFA is a Fine Arts degree) and was waived by not challenging in time; ground (2) fails because refusing an adjournment was within the tribunal's procedural discretion, Parable was heard, and no prejudice is shown (see Q2021A-2a1 and Q2021A-2a2). An appeal on a question of law under AA s 49 is not available either: the SIAC Rules' waiver of recourse operates as an exclusion agreement (SIAC25 r 51.6). The court would dismiss the application, likely with costs.

*What changed:* the 2021 paper set the arbitration under the SIAC Rules 2016; under SIAC 2025 the finality and waiver provision is r 51.6 and the challenge provisions rr 26–28. The AA and IAA grounds are unchanged.
*Cite: IAA s 5(1)–(2); AA ss 3, 48(1)–(2), 49; SIAC25 r 51.6*

### 0.III Soft law instruments and arbitral institutions

Sub-points 0.III.1–0.III.7. Tested: 0.III.7 (Q2023-5 under 0.I.8). Drills 8–13 cover 0.III.1–0.III.6.

### 0.III.7 — Arbitral institutions and the SIAC Court

See Q2023-5 under 0.I.8 (SIAC can administer an arbitration wherever seated) and QSQ-A3 under 0.X.1 (the SIAC Court President, not the court, makes default appointments).

### 0.IV The arbitration agreement: form and parties

Sub-points 0.IV.1–0.IV.8. Tested: 0.IV.2 (QSQ-A2 under 0.II.5). Drills 14–20 cover 0.IV.1 and 0.IV.3–0.IV.8.

### 0.IV.2 — Writing requirement (s 2A(3)–(5) IAA; s 4 AA)

See QSQ-A2 under 0.II.5 (arbitration agreement must be in writing).

### 0.V Arbitrability

Sub-points 0.V.1–0.V.6. Tested: 0.V.1, 0.V.3, 0.V.4, 0.V.6. Drills 21–22 cover 0.V.2 and 0.V.5.

### 0.V.3 — Non-arbitrable subject matter; insolvency, oppression and IP disputes

**Q2023-22** · `0.V.3` · PYP 2023 Q22 · `drp-m-0-35`

In Singapore, any issue touching upon corporate insolvency which is governed by the Insolvency, Restructuring and Dissolution Act, 2018 is

A. Not arbitrable at all.
B. Arbitrable with the permission of the court.
C. Arbitrable depending on the substantive issue in dispute.
D. Arbitrable if all parties consent.

**Answer: C.** There is no blanket rule. Claims that are in essence insolvency claims, such as avoidance of transactions or a winding-up order, are not arbitrable (*Larsen Oil and Gas v Petroprod* [2011] SGCA 21 at [59]), but an ordinary contractual dispute involving a company in insolvency remains arbitrable; that a statute gives the court jurisdiction does not of itself make a dispute non-arbitrable (IAA s 11(2)). A: too wide. B: no court-permission mechanism exists. D: consent cannot make an objectively non-arbitrable matter arbitrable (s 11(1): "unless it is contrary to public policy").
*Cite: [2011] SGCA 21 at [59]; IAA s 11(1)–(2)*

**PYP 2021 ARB Q1 facts.** General Inc (Delaware) and Virus Technology Pte Ltd formed a Singapore joint venture company (65:35). The JVA's clause sent "any dispute whatsoever, arising out of or in connection with the agreement" to a sole arbitrator in Singapore under the SIAC Rules "for the time being in force", with Singapore law governing the arbitration agreement. Another JVA clause let either party give 6 months' notice to negotiate a buyout and provided that, if no buyout was achieved, "proceedings could be commenced" to wind up the JV company under s 254(1)(i) of the Companies Act on the just and equitable ground. The buyout failed; Virus Tech refused to have the JV company wound up; General referred the impasse to arbitration. Virus Tech did not take part. The SIAC-appointed sole arbitrator issued an award "declaring and directing that General may commence proceedings to wind up the JV Company in Singapore". Virus Tech applied under Art 34 to set aside, saying (1) a liquidation is for the courts under the Companies Act, so the dispute is not arbitrable and arbitrating it is contrary to public policy (Art 34(2)(b)); (2) winding up would involve the court deciding remedies such as orders protecting Virus Tech as minority shareholder; and (3) recognising the award would be contrary to public policy under IAA s 11. General asks: (a) Is the subject matter arbitrable? (b) How is public policy engaged, if at all?

**Q2021A-1a** · `0.V.3` `0.V.1` `0.V.6` · PYP 2021 ARB Q1(a) · `drp-m-0-35` `drp-m-0-33` `drp-m-0-38`

[Facts above.] Is the subject matter of the dispute arbitrable?

**Answer.** Yes, as the award frames it. Any dispute the parties agreed to arbitrate may be arbitrated unless it is contrary to public policy (IAA s 11(1)); that the Companies Act (now the IRDA) gives the court jurisdiction to wind up does not of itself make a dispute non-arbitrable (s 11(2)). Two questions arise (`drp-m-0-33`). *Subjective:* the clause covers "any dispute whatsoever … in connection with" the JVA and is read widely (*Larsen* [2011] SGCA 21 at [13], [19]); whether the buyout mechanism has run its course and General may start winding-up proceedings is a dispute about a JVA term. *Objective:* a winding-up order itself is not arbitrable, because it affects creditors and third parties and only a court can make it (*Aloe Vera of America v Asianic Food* [2006] SGHC 78 at [72]; *Larsen* at [59]). But the arbitrator made no winding-up order. The award only declares the shareholders' contractual position: that General is free to *commence* court proceedings. Whether the JV company should be wound up on the just and equitable ground, and on what terms, remains for the court. Virus Tech's point (2) does not change this: *Tomolugen Holdings v Silica Investors* [2015] SGCA 57 at [76], [84]–[91] held minority oppression claims arbitrable even though a tribunal cannot grant every remedy a court can; the remedies a tribunal cannot grant stay with the court. So the dispute decided was arbitrable, and the Art 34(2)(b)(i) ground (not capable of settlement by arbitration under Singapore law) fails. Virus Tech's absence does not stop it applying to set aside (*Rakna* [2019] SGCA 33), but it does mean the award stands on the evidence General put in (Art 25(c)). The application was made under Art 34, which assumes the IAA applies: it does, as General's place of business is in the US (s 5(2)(a)).

*What changed:* court winding up of companies moved from the Companies Act (s 254(1)(i) in the paper) to the Insolvency, Restructuring and Dissolution Act 2018 from 30 Jul 2020, and the 2021 paper's "President of the Court of Arbitration of the SIAC" is now the President of the SIAC Court (SIAC25). Neither changes the answer.
*Cite: IAA ss 5(2)(a), 11; [2011] SGCA 21 at [13], [19], [59]; [2006] SGHC 78 at [72]; [2015] SGCA 57 at [76], [84]–[91]; MAL Arts 25(c), 34(2)(b)(i)*

### 0.V.1 — Arbitrable unless contrary to public policy (s 11 IAA)

See Q2021A-1a under 0.V.3 and Q2021A-1b under 0.XVIII.3 (s 11(1)–(2) and public policy).

### 0.V.4 — Foreign public policy: the Anupam Mittal composite approach

**Q2023-13** · `0.V.4` · PYP 2023 Q13 · `drp-m-0-36`

Under Singapore law, whether the subject matter of a dispute is arbitrable at the pre-award stage depends on

A. Singapore law only.
B. The law of the arbitration agreement and the law of the seat.
C. The law with the closest connection to the dispute.
D. The agreement of the parties only.

**Answer: B.** Before an award, arbitrability is decided by the composite approach: if the dispute is non-arbitrable under the law governing the arbitration agreement, or under Singapore law as the law of the seat, the arbitration cannot proceed (*Anupam Mittal v Westbridge Ventures II* [2023] SGCA 1 at [55]). A: foreign public policy counts too ([48]–[52]). C: closest connection is a test for the law of the arbitration agreement, not for arbitrability. D: consent decides subjective arbitrability only; objective arbitrability is a matter of law.
*Cite: [2023] SGCA 1 at [48]–[52], [55]*

### 0.V.6 — Consequences of non-arbitrability

See Q2021A-1a under 0.V.3 (an award on a non-arbitrable matter is set aside under Art 34(2)(b)(i)).

### 0.VI Pathological clauses and drafting

Sub-points 0.VI.1–0.VI.7. Tested: 0.VI.1–0.VI.4 (all in Q2023-6). Drills 23–25 cover 0.VI.5–0.VI.7.

### 0.VI.1 — Pathological clauses: descriptive label, effective interpretation (Insigma)

**Q2023-6** · `0.VI.1` `0.VI.2` `0.VI.3` `0.VI.4` · PYP 2023 Q6 · `drp-m-0-39` `drp-m-0-40` `drp-m-0-41` `drp-m-0-42`

Which of the following statements is true as a matter of Singapore law

A. Any arbitration agreement which does not stipulate a seat can be enforceable.
B. Any arbitration agreement requiring the Singapore International Arbitration Centre to administer an arbitration using ICC Arbitration Rules can be enforceable.
C. An arbitration agreement which requires a non-existent arbitral institution to administer the arbitration is not necessarily unenforceable.
D. All of the statements are accurate.

**Answer: D.** Each is a pathology the courts cure by effective interpretation where an intention to arbitrate can be inferred (*Insigma Technology v Alstom Technology* [2009] SGCA 24 at [38]–[39]). A: a bare clause with no seat can still be enforced, and the SIAC President can appoint even where the seat is unclear (*KVC Rice Intertrade v Asian Mineral Resources* [2017] SGHC 32; IAA s 8(2)). B: SIAC administering the ICC Rules was upheld in *Insigma* at [34]–[35]. C: a non-existent institution does not nullify the clause (*Re Shanghai Xinan Screenwall* [2022] SGHC 58; *HKL Group v Rizq* [2013] SGHCR 5). Note "can be" and "not necessarily": each clause survives only if the defect is curable.
*Cite: [2009] SGCA 24 at [34]–[35], [38]–[39]; [2017] SGHC 32; [2022] SGHC 58; [2013] SGHCR 5*

### 0.VI.2 — Wrong or non-existent institution named

See Q2023-6 under 0.VI.1 (option C).

### 0.VI.3 — Bare clause: no seat, no appointment method (KVC Rice)

See Q2023-6 under 0.VI.1 (option A).

### 0.VI.4 — Hybrid clause: one institution administers another's rules

See Q2023-6 under 0.VI.1 (option B).

### 0.VII Stay of court proceedings under the IAA

Sub-points 0.VII.1–0.VII.6. Tested: 0.VII.2, 0.VII.3, 0.VII.5. Drills 26–28 cover 0.VII.1, 0.VII.4 and 0.VII.6.

### 0.VII.2 — Mandatory stay unless null and void, inoperative or incapable (s 6(2))

**Q2023-7** · `0.VII.2` `0.VII.5` · PYP 2023 Q7 · `drp-m-0-47` `drp-m-0-50`

Once all the requirements for a stay of court proceedings under section 6 of the International Arbitration Act are met

A. None of the statements is accurate.
B. The Singapore courts have discretion in certain cases when considering whether to grant the stay.
C. The Singapore courts have discretion in all cases when considering whether to grant the stay.
D. The Singapore courts does not have discretion in considering whether to grant the stay, but can impose such terms or conditions as they may think fit.

**Answer: D.** Under IAA s 6(2) the court "is to make an order, upon such terms or conditions as it may think fit, staying the proceedings" unless the agreement is null and void, inoperative or incapable of being performed. The stay itself is mandatory; the terms are discretionary (s 6(2)–(3), s 7). B and C describe the AA, where the court "may" stay (AA s 6(2); *CSY v CSZ* [2022] SGCA 43). A fails because D is accurate.
*Cite: IAA ss 6(2)–(3), 7; AA s 6(2); [2022] SGCA 43 at [23]–[26]*

See also Q2023-27 under 0.I.11 ("null and void" is judged by the law of the arbitration agreement).

### 0.VII.3 — Prima facie standard: the Tomolugen test

**Q2023-15** · `0.VII.3` · PYP 2023 Q15 · `drp-m-0-48`

In deciding whether to grant a stay of court proceedings in favour of arbitration, the Singapore courts will

A. Apply a balance of probabilities test to ascertain whether there is a valid and enforceable arbitration agreement.
B. Apply a prima facie test to ascertain whether there is a valid and enforceable arbitration agreement.
C. Apply a prima facie test to ascertain whether there is a valid and enforceable arbitration agreement, save for objections concerning the existence of an arbitration agreement where the court will apply a balance of probabilities test.
D. Apply a balance of probabilities test to ascertain whether there is a valid and enforceable arbitration agreement, save for objections concerning the existence of an arbitration agreement where the court will apply a prima facie test.

**Answer: B.** The court grants a stay if the applicant shows a prima facie case that there is a valid arbitration agreement between the parties, the dispute falls within it, and it is not null and void, inoperative or incapable of being performed (*Tomolugen* [2015] SGCA 57 at [63]). C: the prima facie standard applies even where the very existence of the agreement is disputed; *Malini Ventura v Knight Capital* [2015] SGHC 225 rejected the English balance-of-probabilities approach. A and D: balance of probabilities is the English approach, not Singapore's.
*Cite: [2015] SGCA 57 at [63]–[64]; [2015] SGHC 225*

### 0.VII.5 — Terms, interim orders and security (ss 6(2)–(3), 7)

See Q2023-7 under 0.VII.2 (the court may impose terms or conditions).

### 0.VIII Jurisdiction of the tribunal

Sub-points 0.VIII.1–0.VIII.11. Tested: 0.VIII.1, 0.VIII.5, 0.VIII.6 (inside Q2021A-2a1), 0.VIII.8, 0.VIII.9, 0.VIII.10. Drills 29–33 cover 0.VIII.2, 0.VIII.3, 0.VIII.4, 0.VIII.7 and 0.VIII.11.

### 0.VIII.1 — Competence-competence (Art 16(1))

**Q2023-8** · `0.VIII.1` · PYP 2023 Q8 · `drp-m-0-52`

Under Singapore law, the doctrine of kompetenz-kompetenz refers to

A. Arbitration clauses are separate and stand-alone agreements which will survive a failure of the contract in which they are found.
B. The court having the power to determine the arbitral tribunal's jurisdiction.
C. Arbitration laws are separate from, and superior to, any general laws.
D. The arbitral tribunal having the power to rule on its own jurisdiction.

**Answer: D.** Competence-competence is the tribunal's power to rule on its own jurisdiction, including objections to the existence or validity of the arbitration agreement (Model Law Art 16(1); SIAC25 r 31.1). A describes separability, the other half of Art 16(1). B: the court reviews jurisdiction afterwards (IAA s 10(3), setting aside, enforcement); that is not competence-competence. C is not a doctrine.
*Cite: MAL Art 16(1); SIAC25 r 31.1*

**QSQ-A5** · `0.VIII.1` · Sample Questions (Part B 2023-S) Arbitration Q5 · `drp-m-0-52`

The principle of kompetenz-kompetenz entails:

A. The jurisdiction of the arbitral tribunal is exclusively determined by the arbitral tribunal itself.
B. The arbitral tribunal can rule on its own jurisdiction.
C. The jurisdiction of the arbitral tribunal is determined by international law.
D. The jurisdiction of the arbitral tribunal is exclusively determined by the Courts.

**Answer: B.** The tribunal *may* rule on its own jurisdiction (Art 16(1)). A: not "exclusively", because its ruling is subject to court review (IAA s 10(3), Art 34, s 31) and the court decides afresh. D: nor exclusively by the courts; the tribunal rules first. C: jurisdiction rests on the parties' agreement and the applicable national law, not international law. Official key: B.
*Cite: MAL Art 16(1); IAA s 10(3); SampleQs p57 Q5, key p122*

### 0.VIII.5 — When to object (Art 16(2); SIAC r 31.2)

**Q2023-11** · `0.VIII.5` · PYP 2023 Q11 · `drp-m-0-56`

A plea that the arbitral tribunal has no jurisdiction needs to be raised

A. No later than the submission of the statement of defence in the arbitration.
B. Once the arbitration is commenced.
C. Once the arbitral tribunal is constituted.
D. Once any statement of claim in the arbitration is filed.

**Answer: A.** Art 16(2): a plea of no jurisdiction must be raised not later than the submission of the statement of defence (a plea that the tribunal is *exceeding* its authority, as soon as the matter arises). The tribunal may admit a later plea if the delay is justified, and appointing an arbitrator does not bar the plea. B, C and D name earlier triggers the Model Law does not impose. SIAC25 r 31.2 is to the same effect.
*Cite: MAL Art 16(2); SIAC25 r 31.2*

### 0.VIII.6 — Waiver by failing to object (Art 4; SIAC r 64)

See Q2021A-2a1 under 0.XI.1 (an objection to the arbitrator's qualifications not taken in time is waived).

### 0.VIII.8 — Court review under s 10(3) IAA: 30 days; positive or negative ruling

**Q2023-24** · `0.VIII.8` `0.VIII.9` · PYP 2023 Q24 · `drp-m-0-59` `drp-m-0-60`

Assume an arbitral tribunal in a Singapore-seated arbitration decides as a preliminary issue that it has no jurisdiction to proceed with the arbitration. Under the International Arbitration Act

A. The claimant cannot seek curial review against the negative ruling on jurisdiction by the tribunal.
B. None of the statements is accurate.
C. The claimant cannot seek curial review against the negative ruling on jurisdiction by the tribunal unless the respondent agrees.
D. The claimant cannot seek curial review against the negative ruling on jurisdiction by the tribunal unless the tribunal agrees.

**Answer: B.** IAA s 10(3)(b) lets any party apply to the General Division of the High Court within 30 days against a ruling "at any stage" that the tribunal has *no* jurisdiction, with no consent needed. So A, C and D are all wrong. A states the position under the unmodified Model Law, where Art 16(3) covers only positive rulings and a negative ruling is not an award that can be set aside (*PT Asuransi v Dexia* [2006] SGCA 41 at [66]); Singapore added review of negative rulings.
*Cite: IAA s 10(3); MAL Art 16(3); [2006] SGCA 41 at [66]*

### 0.VIII.9 — Model Law Art 16(3) compared; a jurisdiction ruling is not an award

See Q2023-24 under 0.VIII.8.

### 0.VIII.10 — Standard of court review: de novo; further evidence

**Q2023-21** · `0.VIII.10` · PYP 2023 Q21 · `drp-m-0-61`

Under Singapore law, when Singapore courts review the issue of whether an arbitral tribunal enjoys jurisdiction

A. The Singapore courts will grant deference to the tribunal's decision on its jurisdiction when the tribunal comprises eminent arbitrators.
B. The Singapore courts will grant deference to the tribunal's decision on its jurisdiction in all cases.
C. The Singapore courts will grant deference to the tribunal's decision on its jurisdiction when the dispute involves foreign elements.
D. None of the statements is accurate.

**Answer: D.** On jurisdiction the seat court decides afresh (de novo) and is not bound by, or deferential to, the tribunal's view, whether under s 10(3) or on setting aside (*Insigma v Alstom* [2008] SGHC 134 at [21]; *PT First Media v Astro* [2013] SGCA 57; *AQZ v ARA* [2015] SGHC 49 at [57]). So A, B and C are wrong: neither the tribunal's eminence nor foreign elements earn deference. Contrast procedural and case-management decisions, where the court does defer (Q2023-30 under 0.XVIII.5).
*Cite: [2008] SGHC 134 at [21]; [2015] SGHC 49 at [57]*

### 0.IX Resisting jurisdiction: the respondent's options

Sub-points 0.IX.1–0.IX.7. Tested: 0.IX.2. Drills 34–39 cover 0.IX.1 and 0.IX.3–0.IX.7.

### 0.IX.2 — Not using s 10(3): no later setting aside on the same ground

**Q2023-19** · `0.IX.2` · PYP 2023 Q19 · `drp-m-0-64`

Under Singapore law, if a respondent with objections to the jurisdiction of the arbitral tribunal does not invoke its recourse under section 10(3) of the International Arbitration Act when it can

A. It loses all rights of recourse against any ultimate award on those jurisdictional objections.
B. It likely loses the right to set aside any ultimate award, but does not lose the right to resist enforcement of the award, on those jurisdictional objections.
C. It loses the right to resist enforcement of the award, but does not lose the right to set aside any ultimate award, on those jurisdictional objections.
D. It does not lose any rights of recourse against any ultimate award on those jurisdictional objections.

**Answer: B.** *PT First Media v Astro* [2013] SGCA 57 at [130], [132] said, obiter and tentatively ("likely"), that a party who does not apply under s 10(3) after a preliminary positive ruling cannot later set aside the award on the same objection; but, subject to waiver, it keeps its right to resist enforcement wherever enforcement is sought (the "choice of remedies", [71]). A: overstated; passive remedies survive. C reverses the position. D ignores First Media. (The candidate whose screenshot this is chose A and flagged it; A is wrong.)
*Cite: [2013] SGCA 57 at [71], [130], [132]*

### 0.X Constitution of the tribunal

Sub-points 0.X.1–0.X.7. Tested: 0.X.1, 0.X.4. Drills 40–44 cover 0.X.2, 0.X.3 and 0.X.5–0.X.7.

### 0.X.1 — Number of arbitrators by default

**QSQ-A3** · `0.X.1` `0.X.4` · Sample Questions (Part B 2023-S) Arbitration Q3 · `drp-m-0-70` `drp-m-0-73`

Which of the following is TRUE about the appointment of arbitrators under the Singapore International Arbitration Act?

A. Parties are free to determine the number of arbitrators.
B. The default number of arbitrator(s) under the Act is three.
C. The Singapore Court plays a primary role in appointing arbitrators.
D. Parties are not allowed to select arbitrators with non-legal backgrounds.

**Answer: A.** The parties are free to determine the number of arbitrators (Model Law Art 10(1)). B: three is the *Model Law* default (Art 10(2)), but the IAA substitutes a single arbitrator (s 9). C: default appointments are made by the President of the SIAC Court as appointing authority (IAA s 8(2)); the court's role is supervisory (challenges, Art 13(3); s 8(1)). D: parties may choose anyone, lawyer or not (Art 11(1)). Official key: A.
*Cite: MAL Arts 10, 11(1); IAA ss 8(1)–(2), 9; SampleQs p56 Q3, key p122*

See also Q2023-9 under 0.XIII.1 (party autonomy includes the number of arbitrators).

### 0.X.4 — Appointing authority and competent court (s 8 IAA)

See QSQ-A3 under 0.X.1 (option C).

### 0.XI Challenging an arbitrator

Sub-points 0.XI.1–0.XI.12. Tested: 0.XI.1, 0.XI.9, 0.XI.12 (all in Q2021A-2a1). Drills 45–53 cover 0.XI.2–0.XI.8, 0.XI.10 and 0.XI.11.

### 0.XI.1 — Grounds for challenge (Art 12(2))

[PYP 2021 ARB Q2 facts: see under 0.II.5 above.]

**Q2021A-2a1** · `0.XI.1` `0.XI.9` `0.XI.12` `0.VIII.6` · PYP 2021 ARB Q2(a), ground (1) · `drp-m-0-77` `drp-m-0-85` `drp-m-0-88` `drp-m-0-57`

Advise Star on the merits of Parable's first ground: that Prof Morgan lacked the qualification the clause required ("a Fine Arts degree from a reputable college") because his MFA/MBA "may be more of a business degree", so Parable did not get the arbitrator it agreed to. (Answer under current law.)

**Answer.** The ground has no merit, for three reasons.

*Regime.* Both parties are Singapore companies and the arbitration is domestic, so the AA applies (see Q2021A-2b). Lack of an agreed qualification is a ground to challenge an arbitrator (AA s 14(3)(b), mirroring Model Law Art 12(2)), and a composition not in accordance with the parties' agreement is a ground to set aside the award (AA s 48(1)(a)(v), mirroring Art 34(2)(a)(iv)).

*Facts.* Prof Morgan holds a Master of *Fine Arts* from the Tisch School of the Arts at NYU, which Parable's own GC calls world-renowned. That is a Fine Arts degree from a reputable college; that he also holds an MBA does not take it away. He is also a Fellow of the CIArb, which meets "the necessary qualifications in arbitration". The composition was in accordance with the agreement.

*Waiver.* Even if there were doubt, Parable knew of the appointment and Prof Morgan's degrees in July 2020 and went through a hearing that ended in June 2021 without challenging him. A challenge had to be made within 15 days of becoming aware of the constitution or of the circumstances (AA s 15(2); under SIAC25, a notice of challenge to the Registrar within 15 days, r 27.1), and a party that proceeds without objecting in time is treated as having waived the objection (SIAC25 r 64.1; compare Model Law Art 4 for IAA arbitrations). It cannot hold the point back and raise it only after an adverse award (`drp-m-0-88`). "Party autonomy" adds nothing: the parties' agreement was honoured. The setting-aside ground under s 48(1)(a)(v) fails.

*What changed:* the arbitration ran under the SIAC Rules 2016; SIAC 2025 now governs challenges in rr 26–28 and waiver in r 64.
*Cite: AA ss 14(3)–(4), 15(2), 48(1)(a)(v); SIAC25 rr 26.1, 27.1, 64.1; MAL Arts 4, 12(2), 34(2)(a)(iv)*

### 0.XI.9 — Challenge procedure under the Model Law (Art 13)

See Q2021A-2a1 under 0.XI.1 (15 days to challenge; AA s 15 mirrors Art 13).

### 0.XI.12 — Arbitrator partiality after the award

See Q2021A-2a1 under 0.XI.1 (composition attacked only after the award; waiver).

### 0.XII Arb-Med, Arb-Med-Arb and multi-tier clauses

Sub-points 0.XII.1–0.XII.6. None has been tested. Drills 54–59 cover all six.

### 0.XIII Conduct of the proceedings and evidence

Sub-points 0.XIII.1–0.XIII.12. Tested: 0.XIII.1, 0.XIII.2, 0.XIII.6, 0.XIII.7. Drills 60–67 cover 0.XIII.3–0.XIII.5 and 0.XIII.8–0.XIII.12.

### 0.XIII.1 — Party autonomy over procedure; Evidence Act does not bind (Art 19)

**Q2023-14** · `0.XIII.1` · PYP 2023 Q14 · `drp-m-0-95`

The Evidence Act of Singapore

A. Applies automatically to all arbitrations seated in Singapore.
B. Does not apply to all arbitrations seated in Singapore unless parties agree.
C. Only does not apply to arbitrations with foreign elements that are seated in Singapore.
D. Applies automatically to arbitrations seated in Singapore where the proper law of the contract under dispute is governed by Singapore law.

**Answer: B.** Subject to the parties' agreement, the tribunal decides the admissibility, relevance, materiality and weight of evidence (Model Law Art 19(2)); domestic evidence statutes such as the Evidence Act 1893 do not bind a tribunal unless the parties agree. A and D: no automatic application, whatever law governs the contract. C: the position is the same for domestic arbitrations (the Evidence Act applies to judicial proceedings in court).
*Cite: MAL Art 19; IAA s 12(2)–(3); ARB-SN (see `drp-m-0-95`)*

**Q2023-9** · `0.XIII.1` `0.X.1` `0.I.5` · PYP 2023 Q9 · `drp-m-0-95` `drp-m-0-70` `drp-m-0-5`

Under Singapore law, the concept of party autonomy in arbitration means that

A. All of the statements are accurate.
B. Parties are free to determine the number of arbitrator(s).
C. Parties are free to choose between institutional and ad hoc arbitration.
D. Parties are free to determine the procedure of the arbitration.

**Answer: A.** Each is an aspect of party autonomy: the number of arbitrators (Art 10(1)); institutional or ad hoc arbitration (the parties choose whether to adopt an institution and its rules); and the procedure (Art 19(1)), subject only to the mandatory provisions such as equal treatment (Art 18).
*Cite: MAL Arts 10(1), 18, 19(1)*

### 0.XIII.2 — Equal treatment; hearings and notice (Arts 18, 24)

[PYP 2021 ARB Q2 facts: see under 0.II.5 above.]

**Q2021A-2a2** · `0.XIII.2` `0.XVIII.4` `0.XVIII.5` `0.XIII.7` · PYP 2021 ARB Q2(a), ground (2) · `drp-m-0-96` `drp-m-0-141` `drp-m-0-142` `drp-m-0-101`

Advise Star on the merits of Parable's second ground: that Prof Morgan unreasonably refused to postpone the hearing until Dr Crick QC could travel to Singapore, so Parable was not properly represented, could not properly present its case and suffered a breach of natural justice.

**Answer.** The ground is weak and is unlikely to succeed.

*The rules.* Each party must be treated with equality and given a full opportunity to present its case (Model Law Art 18; AA s 22 is the domestic counterpart). Under the AA an award may be set aside if a party was "otherwise unable to present [its] case" (s 48(1)(a)(iii)) or for a breach of natural justice in connection with the making of the award by which its rights were prejudiced (s 48(1)(a)(vii)), the equivalents of Art 34(2)(a)(ii) and IAA s 24(b). The applicant must show which rule was breached, how, how the breach was connected to the award, and how it prejudiced its rights (*John Holland v Toyo Engineering* [2001] SGHC 48; *BZW v BZV* [2022] SGCA 1 at [59]–[60]). The threshold is high: the court does not second-guess procedural decisions and remedies only meaningful breaches that caused actual prejudice (*Soh Beng Tee v Fairmount Development* [2007] SGCA 28 at [65(f)]; *DMZ v DNA* [2025] SGCA 52 at [46]).

*Application.* The right to be heard is a right to a fair opportunity to present one's case, not a right to a particular advocate. Parable was heard: its GC presented its case at the hearing. Foreign counsel may represent parties in Singapore-seated arbitrations (Legal Profession Act s 35), so Dr Crick could have been instructed, but the pandemic made his attendance in person impossible for an indefinite period; he could have advised behind the scenes or appeared remotely. Refusing an open-ended adjournment, after "several starts and stops", in a dispute about pandemic delay, was within the tribunal's discretion over procedure (Art 19(2)). Parable also cannot show prejudice: it does not identify any argument or evidence it was prevented from putting that could reasonably have changed the outcome. A complaint that the tribunal got force majeure or "unconscionable conduct" wrong is an attack on the merits, which is not reviewable (*PT Asuransi v Dexia* [2006] SGCA 41 at [57]).

*Cite: MAL Arts 18, 19(2); AA s 48(1)(a)(iii), (vii); IAA s 24(b); LPA s 35; [2001] SGHC 48; [2022] SGCA 1 at [59]–[60]; [2007] SGCA 28 at [65(f)]; [2025] SGCA 52 at [46]*

Note: the AA's equal-treatment provision is in Part 5 of the AA; the Model Law Art 18 wording is the one set out in `drp-m-0-96`.

### 0.XIII.6 — Confidentiality of arbitration and related court proceedings

**Q2023-20** · `0.XIII.6` · PYP 2023 Q20 · `drp-m-0-100`

In Singapore, arbitration proceedings are

A. Absolutely confidential.
B. Not confidential.
C. Subject to exceptions, confidential.
D. Confidential only if parties expressly agree.

**Answer: C.** An obligation of confidentiality applies by default, even without an express term (*AAY v AAZ* [2009] SGHC 142 at [55]), subject to exceptions such as disclosure reasonably necessary to protect a party's legal rights or to the authorities on reasonable suspicion of crime ([72]); SIAC25 r 59.3 lists permitted disclosures. A: not absolute. B: wrong in Singapore. D: no express agreement is needed (contrast the position in some other jurisdictions).
*Cite: [2009] SGHC 142 at [55], [72]; SIAC25 r 59.3; IAA ss 22–23*

### 0.XIII.7 — Foreign lawyers may act in Singapore-seated arbitrations

See Q2021A-2a2 under 0.XIII.2 (foreign counsel may appear; LPA s 35).

### 0.XIV Commencing the arbitration and SIAC procedures

Sub-points 0.XIV.1–0.XIV.5. None has been tested. Drills 68–72 cover all five.

### 0.XV Interim measures

Sub-points 0.XV.1–0.XV.10. Tested: 0.XV.6, 0.XV.7. Drills 73–80 cover 0.XV.1–0.XV.5 and 0.XV.8–0.XV.10.

### 0.XV.6 — Court's powers under s 12A: urgent and non-urgent cases

**Q2023-25** · `0.XV.6` `0.XV.7` · PYP 2023 Q25 · `drp-m-0-117` `drp-m-0-118`

Under the International Arbitration Act, an applicant

A. Can apply for interim relief from the Singapore courts in aid of arbitration seated elsewhere even if the facts of the dispute have no connection to Singapore.
B. All of the statements are accurate.
C. Can seek interim relief from the Singapore courts which shall lapse if the arbitral tribunal makes a subsequent order on the same subject matter.
D. Cannot obtain interim relief from the Singapore courts in aid of arbitration in all cases unless the arbitral tribunal is unable for the time being to act effectively.

**Answer: B.** Each of A, C and D paraphrases a limb of IAA s 12A. A: s 12A applies "irrespective of whether the place of arbitration is in the territory of Singapore" (s 12A(1)(b)); no connection to Singapore is required to *apply*, though the court may refuse where the foreign seat makes the order inappropriate (s 12A(3)). C: the court's order ceases to have effect, wholly or partly, if the tribunal (or institution) makes an order "which expressly relates to" it (s 12A(7)). D: "In every case" the court acts only if or to the extent that the tribunal (and any institution) has no power or is unable for the time being to act effectively (s 12A(6)). D was the 2023 candidate's choice; it is accurate, but not the only accurate statement. Not settled by any official key; the answer follows the statute's text.
*Cite: IAA s 12A(1)(b), (3), (6), (7)*

**Q2023-32** · `0.XV.6` · PYP 2023 Q32 · `drp-m-0-117`

A dispute arose between Party A and Party B. The contract between the parties provided for SIAC arbitration seated in Singapore. Party A intended to commence arbitration against Party B, but before doing so, discovered that Party B is planning to destroy certain pieces of key evidence. Which of the following is correct, as a matter of Singapore law

A. Party A can apply to the Singapore courts for interim relief as the situation is one of urgency, without any restriction.
B. Party A can apply to the Singapore courts for interim relief, but has to show that the arbitral tribunal is unable for the time being to act effectively.
C. Party A cannot obtain relief from the Singapore courts. Party A must apply for interim relief from the arbitral tribunal.
D. Party A cannot obtain relief from the Singapore courts. Party A must apply for interim relief from the courts in the jurisdiction where Party B is incorporated.

**Answer: B.** In urgency a party or *proposed* party may apply for orders necessary to preserve evidence or assets (s 12A(4)), so Party A need not commence first. But s 12A(6) applies "in every case": the court acts only if the tribunal and any institution have no power or are unable for the time being to act effectively. Under the SIAC Rules an Emergency Arbitrator can be appointed within 24 hours (SIAC25 Sch 1), so Party A must show why that route is not effective. A: urgency does not remove the s 12A(6) restriction. C: court relief is available, and seeking it is not a waiver (Art 9). D: no such rule.
*Cite: IAA s 12A(4), (6); MAL Art 9; SIAC25 Sch 1*

### 0.XV.7 — Foreign-seated arbitrations; non-parties (s 12A(1)(b), (3))

See Q2023-25 under 0.XV.6 (option A) and Q2023-2 under 0.I.8.

### 0.XVI Anti-suit injunctions

Sub-points 0.XVI.1–0.XVI.4. Tested: 0.XVI.1, 0.XVI.4. Drills 81–82 cover 0.XVI.2 and 0.XVI.3.

### 0.XVI.1 — When a Singapore court grants an ASI in aid of arbitration

**QSQ-A9** · `0.XVI.1` `0.XVI.4` · Sample Questions (Part B 2024) Arbitration Q9 · `drp-m-0-122` `drp-m-0-125`

A dispute arises between Party A and Party B. Their contract provides for SIAC arbitration seated in Singapore. Party A has not intended to commence arbitration but discovers that Party B has commenced court proceedings in Narnia in breach of the arbitration agreement. Assume that the laws of Narnia are substantially similar to those of Singapore. Which of the following statements is/are CORRECT?

I. Party A may apply for a stay of the court proceedings in Narnia.
II. Party A may apply to the Singapore courts for an anti-suit injunction.
III. Party A may commence arbitration and apply to the arbitral tribunal for an anti-suit injunction.

A. I only.
B. II only.
C. I and III.
D. I, II and III.

**Answer: D.** I: Narnian law mirrors Singapore's, so a stay is available there (as under IAA s 6 and Art 8, which apply whatever the seat). II: as the seat court, a Singapore court will generally restrain foreign proceedings brought in breach of a valid arbitration agreement absent strong cause (*Sun Travels & Tours v Hilton* [2019] SGCA 10 at [65]–[68]). III: a tribunal may itself order a party not to pursue foreign proceedings as an interim measure (IAA s 12(1)(i); *PT Pukuafu* [2012] SGHC 187), enforceable with permission under s 12(6). Official key: D.
*Cite: IAA ss 6, 12(1)(i), 12(6); [2019] SGCA 10 at [65]–[68]; [2012] SGHC 187 at [19]; SampleQs p59 Q9, key p122*

### 0.XVI.4 — Tribunal-ordered anti-suit relief

See QSQ-A9 under 0.XVI.1 (statement III).

### 0.XVII The award

Sub-points 0.XVII.1–0.XVII.12. Tested: 0.XVII.10, 0.XVII.12. Drills 83–92 cover 0.XVII.1–0.XVII.9 and 0.XVII.11.

### 0.XVII.10 — Correction of the award (Art 33(1)(a), (2))

**Q2023-23** · `0.XVII.10` `0.XVII.12` · PYP 2023 Q23 · `drp-m-0-135` `drp-m-0-137`

In a Singapore-seated arbitration under the International Arbitration Act, after the arbitral tribunal releases an award

A. None of the statements is accurate.
B. The tribunal has 30 days to make a correction of any nature without restriction to that award.
C. The tribunal cannot make any correction to that award on its own initiative.
D. The tribunal can release an additional award to correct its decision on a claim that was considered in that award.

**Answer: A.** B: the tribunal may correct on its own initiative within 30 days of the award, but only errors in computation, clerical or typographical errors or errors of a similar nature (Art 33(2), referring to Art 33(1)(a)); anything more is barred because the tribunal is functus officio (IAA s 19B(2)–(3)). C: Art 33(2) expressly allows own-initiative correction. D: an additional award covers claims presented but *omitted* from the award (Art 33(3)), not a change to a decision already made. So none is accurate. (The 2023 candidate chose B; B is wrong.)
*Cite: MAL Art 33(1)(a), (2), (3); IAA s 19B(2)–(3)*

### 0.XVII.12 — Additional award; extension of time (Art 33(3)–(4))

See Q2023-35 under 0.XVIII.7 (option B) and Q2023-23 under 0.XVII.10 (option D).

### 0.XVIII Setting aside the award

Sub-points 0.XVIII.1–0.XVIII.15. Tested: 0.XVIII.1–0.XVIII.8, 0.XVIII.12, 0.XVIII.14, and 0.XVIII.15 only in passing (Q2023-33 under 0.XIX.15). Drills 93–97 cover 0.XVIII.9–0.XVIII.11, 0.XVIII.13 and 0.XVIII.15.

### 0.XVIII.1 — No appeal; exhaustive grounds; only at the seat

**Q2023-4** · `0.XVIII.1` · PYP 2023 Q4 · `drp-m-0-138`

In an ad hoc arbitration between an English party and an Indian party that is seated in Singapore, the losing party can apply to set aside the award

A. All of the options are accurate.
B. In England.
C. In Singapore.
D. In India.

**Answer: C.** Setting aside is available only from the court of the seat (Model Law Arts 1(2), 34(1)), here the General Division of the High Court (IAA s 8(1)). B and D: the parties' home courts may be asked to refuse *enforcement* (NYC Art V), but they cannot annul a Singapore award. A fails with B and D.
*Cite: MAL Arts 1(2), 34(1); IAA s 8(1)*

**Q2023-18** · `0.XVIII.1` · PYP 2023 Q18 · `drp-m-0-138`

An award debtor is dissatisfied with the award rendered by a Singapore-seated arbitration tribunal under the International Arbitration Act. The award debtor

A. Can appeal against the award on points of law as of right.
B. Can appeal against the entire award as of right.
C. Can appeal against the award with the consent of the other party.
D. Cannot appeal against the award save for the grounds of setting aside under the International Arbitration Act.

**Answer: D.** There is no appeal on law or fact from an IAA award; errors are final and binding, and the only recourse is setting aside on the exhaustive grounds in Art 34(2) and IAA s 24 (*PT Asuransi v Dexia* [2006] SGCA 41 at [57]). A, B and C: an appeal on a question of law by consent or permission exists only for domestic awards under AA s 49. (Strictly, setting aside is not an appeal; D is the best answer.)
*Cite: [2006] SGCA 41 at [57]; IAA s 24; MAL Art 34(2); AA s 49*

### 0.XVIII.2 — Art 34(2)(a) grounds the applicant must prove

See Q2021A-2b under 0.II.5 and Q2021A-2a1 under 0.XI.1 (composition not as agreed; AA s 48(1)(a)(v), the domestic counterpart of Art 34(2)(a)(iv)).

### 0.XVIII.3 — Art 34(2)(b) grounds the court may raise itself

[PYP 2021 ARB Q1 facts: see under 0.V.3 above.]

**Q2021A-1b** · `0.XVIII.3` `0.V.1` `0.XIX.13` · PYP 2021 ARB Q1(b) · `drp-m-0-140` `drp-m-0-33` `drp-m-0-165`

How is public policy engaged in this case, if at all?

**Answer.** Public policy is engaged at two points, and Virus Tech fails at both.

*Before the award (arbitrability).* IAA s 11(1) uses public policy to define what may be arbitrated: a dispute may be arbitrated "unless it is contrary to public policy to do so". That is the arbitrability question answered in Q2021A-1a: a contractual dispute between shareholders about the buyout and exit mechanism is arbitrable, and the court keeps the winding-up decision itself. Virus Tech's point 3 misreads s 11: it concerns whether the dispute may be referred to arbitration, not whether an award may be "recognised".

*After the award (setting aside).* The court may set aside, whether or not the applicant proves it, if the subject matter is not capable of settlement by arbitration (Art 34(2)(b)(i)) or the award conflicts with Singapore public policy (Art 34(2)(b)(ii)). Public policy here is narrow: it is engaged only where upholding the award would "shock the conscience", be "clearly injurious to the public good" or "wholly offensive to the ordinary reasonable and fully informed member of the public", or violate the forum's most basic notions of morality and justice (*PT Asuransi v Dexia* [2006] SGCA 41 at [59]). An award that merely declares that one shareholder may *start* winding-up proceedings in the Singapore court, where the court will hear Virus Tech and decide whether winding up is just and equitable, does not come close: it sends the public-interest question to the very forum Virus Tech says should decide it. Public policy is not a back door to relitigate the merits (*Reliance Infrastructure* [2024] SGCA(I) 10 at [75]).

So Virus Tech's application should fail on both Art 34(2)(b) limbs. If General later enforces the award, the same narrow public policy test governs resistance (Art 36(1)(b)(ii) via s 19 IAA; *PT First Media* [2013] SGCA 57).
*Cite: IAA s 11; MAL Art 34(2)(b); [2006] SGCA 41 at [59]; [2024] SGCA(I) 10 at [75]*

### 0.XVIII.4 — IAA s 24: fraud or corruption; natural justice

**Q2023-28** · `0.XVIII.4` `0.XVIII.1` · PYP 2023 Q28 · `drp-m-0-141` `drp-m-0-138`

The grounds for setting aside an arbitral award under the International Arbitration Act are

A. Contained in the Model Law read together with the International Arbitration Act.
B. Contained in the New York Convention.
C. Exclusively contained in the Model Law.
D. Exactly the same as the grounds for resisting enforcement of an award in Singapore.

**Answer: A.** The grounds are Model Law Art 34(2) plus IAA s 24 (fraud or corruption; breach of natural justice causing prejudice), which applies "despite Article 34(1)". C: s 24 adds grounds, so the Model Law is not exclusive. B: the NYC deals with enforcement, not setting aside. D: the enforcement grounds (IAA s 31; Art 36 via s 19) overlap but differ: for example, enforcement can be refused because the award was set aside at the seat (s 31(2)(f)), and s 24 has no exact counterpart there.
*Cite: IAA ss 24, 31; MAL Art 34(2)*

See also Q2021A-2a2 under 0.XIII.2 (natural justice complaint about a refused adjournment).

### 0.XVIII.5 — Natural justice: elements and threshold

**QSQ-A7** · `0.XVIII.5` `0.XVIII.8` · Sample Questions (Part B 2024) Arbitration Q7 · `drp-m-0-142` `drp-m-0-145`

A Singapore-seated arbitral tribunal governed by the International Arbitration Act issues a final award. The losing party applies to set aside the award under s 24(b) of the IAA, alleging a breach of natural justice. Specifically, the tribunal had decided the dispute on a legal characterisation that neither party had pleaded or addressed in submissions, without inviting the parties to address it. Which of the following most accurately states what the applicant must establish to succeed?

A. The applicant need only demonstrate that the tribunal decided the case on a basis not argued by the parties; proof of prejudice is not a separate requirement once such a departure is shown.
B. The applicant must establish that the breach was deliberate or that the tribunal acted in bad faith, in addition to showing that its rights were prejudiced.
C. The applicant must show: (i) which rule of natural justice was breached; (ii) how it was breached; (iii) in what way the breach was connected to the making of the award; and (iv) how the breach prejudiced its rights, though it need not prove that the outcome would necessarily have been different.
D. The applicant must prove, on the balance of probabilities, that but for the breach the tribunal would have reached a different conclusion, such that the outcome was caused by the breach.

**Answer: C.** These are the four *John Holland* elements (*John Holland v Toyo Engineering* [2001] SGHC 48; *BZW v BZV* [2022] SGCA 1 at [59]–[60]). Prejudice is required, but it is enough that the point could reasonably have made a difference, not that it would have (compare *DFI v DFJ* [2024] SGHC(I) 4 at [73]: evidence that "would arguably have led to a different outcome"). A: s 24(b) itself requires prejudice to the party's rights. B: no bad faith is required. D: but-for causation sets the bar too high. Official key: C.
*Cite: IAA s 24(b); [2001] SGHC 48; [2022] SGCA 1 at [59]–[60]; [2024] SGHC(I) 4 at [73]; SampleQs p58 Q7, key p122*

**Q2023-30** · `0.XVIII.5` · PYP 2023 Q30 · `drp-m-0-142` `drp-m-0-148`

Under Singapore law, when an award debtor challenges an arbitral award on natural justice grounds

A. The courts will grant due deference to the tribunal's case management decisions.
B. The courts will grant due deference to the tribunal's case management decisions if the arbitral tribunal comprises eminent arbitrators.
C. None of the statements is accurate.
D. The courts will review de novo the tribunal's case management decisions.

**Answer: A.** On natural justice the court asks whether the process was fair; it does not second-guess the tribunal's procedural and case-management decisions, which the parties agreed to accept (*DMZ v DNA* [2025] SGCA 52 at [46]; *DBO v DBP* [2024] SGCA(I) 4, where an early-dismissal award survived). Awards are read generously and not microscopically, and only meaningful breaches causing actual prejudice are remedied (*Soh Beng Tee* [2007] SGCA 28 at [65(f)]). D confuses this with *jurisdiction*, which the court reviews de novo (Q2023-21 under 0.VIII.10). B: deference does not depend on the arbitrators' eminence. Not settled by an official key; the 2023 candidate chose D, which is wrong.
*Cite: [2025] SGCA 52 at [46]; [2024] SGCA(I) 4 at [29], [48]; [2007] SGCA 28 at [65(f)]*

### 0.XVIII.6 — Raise the breach at the time, do not reserve it (China Machine)

**QSQ-A8** · `0.XVIII.6` · Sample Questions (Part B 2024) Arbitration Q8 · `drp-m-0-143`

Under Singapore law, where an award debtor seeks to challenge an arbitral award on the ground of a breach of natural justice, which of the following statements is CORRECT?

I. The award debtor must have "reserved its position" during the arbitration proceedings and may wait until the award is rendered before deciding whether to pursue the objection.
II. The award debtor must give the arbitral tribunal fair notice of its intention to raise the objection at the appropriate time and should ordinarily seek a suspension of the proceedings to afford the tribunal an opportunity to address the alleged breach.
III. The award debtor must have commenced court proceedings immediately upon the alleged breach of natural justice occurring.

A. I only.
B. II only.
C. III only.
D. II and III.

**Answer: B.** A party that thinks the process has gone fatally wrong must give the tribunal fair intimation that it will take the point and at least seek a suspension until the breach is remedied; it cannot "reserve" its position and wait for the result (*China Machine New Energy v Jaguar Energy Guatemala* [2020] SGCA 12 at [170]; *DNO v DNP* [2025] SGHC(I) 24 at [115]). So I is wrong. III is wrong: there is no mid-arbitration court route for natural justice complaints, and the court will not intervene in matters governed by the Model Law except as it provides (Art 5; *DMZ v DNA* [2025] SGCA 52). Official key: B.
*Cite: [2020] SGCA 12 at [170]; [2025] SGHC(I) 24 at [115]; MAL Art 5; SampleQs p58 Q8, key p122*

**Q2023-31** · `0.XVIII.6` · PYP 2023 Q31 · `drp-m-0-143`

Under Singapore law, an award debtor can only challenge an award on natural justice grounds where

A. None of the statements is correct.
B. The award debtor had alerted the arbitral tribunal of the alleged breach of natural justice and sought to suspend the proceedings to give the tribunal an opportunity to consider and/or remedy the alleged breach.
C. The award debtor had "reserved its rights" during the arbitration proceedings.
D. The award debtor had brought a court application once the alleged breach of natural justice occurs during the arbitration proceedings.

**Answer: B.** Same rule as QSQ-A8: *China Machine* [2020] SGCA 12 at [170]. C: reserving rights is exactly what is not allowed. D: no such court application exists mid-arbitration (Art 5). "Only" is strong: the rule applies where the party knew of the breach during the proceedings; a breach first revealed in the award itself (e.g. a surprise chain of reasoning) cannot have been raised earlier. B is still the best answer.
*Cite: [2020] SGCA 12 at [170]; MAL Art 5*

### 0.XVIII.7 — Ultra petita v infra petita challenges

**Q2023-35** · `0.XVIII.7` `0.XVII.12` `0.XVIII.14` · PYP 2023 Q35 · `drp-m-0-144` `drp-m-0-137` `drp-m-0-151`

In a Singapore-seated arbitration, an arbitral tribunal releases an award without considering and addressing a key issue advanced by the claimant.

A. The Singapore courts may set aside relevant parts of the award for a breach of natural justice.
B. The claimant can request the tribunal to make an additional award to address that issue within the stipulated timeline.
C. All of the statements are accurate.
D. The Singapore courts can remit the award back to the tribunal to consider that issue.

**Answer: C.** A: failing to consider an essential point properly before the tribunal is an infra petita challenge under s 24(b) and Art 34(2)(a)(ii); all four conditions, including real prejudice, must be met (*DKT v DKU* [2025] SGCA 23 at [8]; *Palm Grove* [2025] SGCA 14 at [27]), and the court may set aside in part. B: within 30 days of receipt a party may ask for an additional award on claims presented but omitted (Art 33(3)); strictly this covers an omitted *claim*, so it fits where the "key issue" is one of the claimant's claims. D: on a party's request the court may suspend the setting-aside proceedings so the tribunal can resume and eliminate the ground (Art 34(4)), which Singapore calls remission (*Vietnam Oil and Gas* [2025] SGCA 50 at [111]–[130]). All three are possible routes.
*Cite: IAA s 24(b); MAL Arts 33(3), 34(2)(a)(ii), 34(4); [2025] SGCA 23 at [8]; [2025] SGCA 14 at [27]; [2025] SGCA 50 at [111]–[130]*

### 0.XVIII.8 — When prejudice must be shown

See QSQ-A7 under 0.XVIII.5 (prejudice required for natural justice, but not proof the outcome would have differed).

### 0.XVIII.12 — Time limit: 3 months, no extension

**Q2023-29** · `0.XVIII.12` · PYP 2023 Q29 · `drp-m-0-149`

Do the Singapore courts have the power to extend the time period for an award debtor to make a setting aside application?

A. Yes, provided the award debtor compensates the award creditor in costs.
B. Yes, provided the award debtor can show compelling reasons.
C. Yes, provided the award debtor has already made an application to resist enforcement of the same award in another jurisdiction.
D. None at all.

**Answer: D.** An application must be made within 3 months of receiving the award (or of the disposal of an Art 33 request) (Art 34(3); ROC O 48 r 2(3)), and the court has no power to extend it, even for fraud discovered later (*Bloomberry Resorts v Global Gaming Philippines* [2021] SGCA 9 at [11]–[13]). A, B and C invent conditions. The debtor can still resist enforcement after the time has passed (Q2023-34 under 0.XIX.1).
*Cite: MAL Art 34(3); ROC O 48 r 2(3); [2021] SGCA 9 at [11]–[13]*

### 0.XVIII.14 — Outcomes: set aside, sever, remit (Art 34(4))

See Q2023-35 under 0.XVIII.7 (partial setting aside; remission).

### 0.XIX Enforcement and resisting enforcement

Sub-points 0.XIX.1–0.XIX.16. Tested: 0.XIX.1, 0.XIX.2, 0.XIX.3, 0.XIX.9, 0.XIX.13, 0.XIX.15, and 0.XIX.8 only in passing (Q2023-17). Drills 98–107 cover 0.XIX.4–0.XIX.8, 0.XIX.10–0.XIX.12, 0.XIX.14 and 0.XIX.16.

### 0.XIX.1 — Choice of remedies: setting aside and resisting are cumulative

**Q2023-34** · `0.XIX.1` `0.XIX.2` · PYP 2023 Q34 · `drp-m-0-153` `drp-m-0-154`

A Singapore-seated arbitral tribunal issued an arbitral award under the International Arbitration Act. The time period for setting aside the award has elapsed. The award creditor then brings an application to enforce the award in Singapore.

A. The award debtor can no longer resist enforcement of the award in Singapore.
B. The award debtor can still resist enforcement of the award in Singapore under the International Arbitration Act.
C. The award debtor can apply to set aside the award before the Singapore courts now that the award is placed before the Singapore courts by the award creditor.
D. The award debtor can still resist enforcement of the award in Singapore under the New York Convention.

**Answer: B.** Setting aside and resisting enforcement are cumulative "active" and "passive" remedies; not applying to set aside does not stop the debtor resisting enforcement (*PT First Media v Astro* [2013] SGCA 57 at [71]). A Singapore-seated award is enforced under IAA s 19, and the Art 36(1) grounds are available to resist it ([84], [86]–[87]). A ignores the choice of remedies. C: the 3-month limit cannot be extended or revived (Art 34(3)). D: the NYC (IAA Part 3) applies only to *foreign* awards; a Singapore award is not one (s 27(1)).
*Cite: [2013] SGCA 57 at [71], [84], [86]–[87]; IAA ss 19, 27(1); MAL Art 34(3)*

### 0.XIX.2 — Enforcing a Singapore-seated award (s 19 IAA; First Media)

**Q2023-16** · `0.XIX.2` · PYP 2023 Q16 · `drp-m-0-154`

Under the International Arbitration Act, the grounds to refuse enforcement of an award arising out of an arbitration seated in Singapore

A. Are found in section 19 International Arbitration Act read with Article 36 of the Model Law.
B. Are found in Art V of the New York Convention.
C. Are found in Article 34 of the Model Law.
D. Are found in section 24 of the International Arbitration Act.

**Answer: A.** Section 19 lists no grounds, but the Art 36(1) grounds are available to resist enforcement of a Singapore-seated international award despite the exclusion of Chapter VIII from the force of law (*PT First Media* [2013] SGCA 57 at [84], [86]–[87]). B: NYC Art V (IAA s 31) governs *foreign* awards. C and D are *setting-aside* grounds.
*Cite: IAA s 19; MAL Art 36(1); [2013] SGCA 57 at [84], [86]–[87]*

### 0.XIX.3 — New York Convention scope and reservations

**QSQ-A4** · `0.XIX.3` · Sample Questions (Part B 2023-S) Arbitration Q4 · `drp-m-0-155`

Which statement on the New York Convention is TRUE?

A. The New York Convention sets out the grounds for setting aside awards.
B. The New York Convention sets out the grounds for resisting enforcement of foreign awards.
C. The New York Convention sets out the grounds for both setting aside awards and resisting enforcement of foreign awards.
D. The New York Convention sets out the grounds for enforcing arbitration agreements only.

**Answer: B.** The NYC governs recognition and enforcement of foreign awards, and Art V lists the grounds on which they may be refused (in Singapore, IAA s 31). A and C: setting aside is for the law of the seat (Model Law Art 34); the NYC only recognises its effect (Art V(1)(e)). D: Art II does require courts to refer parties to arbitration, but that is not the NYC's "only" subject. Official key: B.
*Cite: NYC Arts II, V; IAA s 31; SampleQs p56 Q4, key p122*

### 0.XIX.8 — Grounds the court may raise itself (s 31(4))

See Q2023-17 under 0.XIX.13 (public policy is a ground the court may raise of its own motion).

### 0.XIX.9 — Residual discretion to enforce despite a ground

**Q2023-36** · `0.XIX.9` · PYP 2023 Q36 · `drp-m-0-161`

Once a ground for resisting enforcement of an international arbitration award is made out by the award debtor, the Singapore courts

A. Must refuse enforcement of said award if the award is a foreign award.
B. May refuse enforcement of said award.
C. Must refuse enforcement of said award.
D. Must refuse enforcement of said award if the award was rendered in Singapore.

**Answer: B.** NYC Art V(1) and IAA s 31(2) say enforcement "may" be refused, so the court keeps a residual discretion to enforce, for example where an irregularity could not have affected the outcome (*Werner A Bock v N's Co*, HK CA). Art 36(1) is likewise permissive for Singapore awards. A, C and D turn "may" into "must", whatever the seat.
*Cite: NYC Art V(1); IAA s 31(1)–(2); MAL Art 36(1)*

### 0.XIX.13 — Public policy: narrow; illegality (AJU v AJT matrix)

**Q2023-17** · `0.XIX.13` `0.XIX.8` · PYP 2023 Q17 · `drp-m-0-165` `drp-m-0-160`

An international arbitration award may be refused enforcement in Singapore for breach of public policy

A. As long as the arbitral tribunal had made an error of fact.
B. As long as the arbitral tribunal had made an error of law.
C. As long as there is any kind of illegality involved in the underlying contract.
D. If the award violates the most basic notions of morality and justice.

**Answer: D.** Public policy (IAA s 31(4)(b); Art 36(1)(b)(ii)) is narrow: it applies where upholding the award would shock the conscience, be clearly injurious to the public good, or violate the forum's most basic notions of morality and justice (*PT Asuransi v Dexia* [2006] SGCA 41 at [59]). A and B: errors of fact or law are final and not reviewable ([57]). C: not every illegality reaches the threshold (*Gokul Patnaik v Nine Rivers* [2020] SGHC(I) 23 at [203], [206]; the *AJU v AJT* / *CBX v CBZ* matrix limits reopening a tribunal's illegality finding).
*Cite: IAA s 31(4)(b); [2006] SGCA 41 at [57], [59]; [2011] SGCA 41; [2020] SGHC(I) 17 at [67]; [2020] SGHC(I) 23 at [203], [206]*

See also Q2021A-1b under 0.XVIII.3.

### 0.XIX.15 — Adjourning enforcement pending a challenge at the seat (s 31(5))

**Q2023-33** · `0.XIX.15` `0.XVIII.15` · PYP 2023 Q33 · `drp-m-0-167` `drp-m-0-152`

A London-seated arbitral tribunal issued an arbitral award. The award creditor brings an application to enforce the award in Singapore. The award debtor then brings an application to set aside the award in London.

A. The Singapore courts must not enforce the award whilst there is a pending setting aside application in London.
B. The Singapore courts must adjourn the enforcement proceedings pending the setting aside decision by the English courts.
C. The award creditor must withdraw the enforcement proceedings in Singapore since there are ongoing setting aside proceedings in London.
D. The Singapore courts may adjourn the enforcement proceedings pending the setting aside decision by the English courts.

**Answer: D.** Where an application to set aside is pending at the seat, the Singapore court "may, if it considers it proper", adjourn and may order the debtor to give security (IAA s 31(5); NYC Art VI). The discretion is wide; the first question is whether the seat challenge is bona fide, then its merits on a sliding scale, the length and effect of delay and comity (*Man Diesel & Turbo v IM Skaugen* [2018] SGHC 132 at [45]–[46], [49], [54]; *Aastar Trading v Olam* [2025] SGHC 5 at [47]–[48], [59]–[61]). A, B and C make adjournment or withdrawal mandatory. Note also that the debtor could not set the London award aside in Singapore (`drp-m-0-152`).
*Cite: IAA s 31(5); NYC Art VI; [2018] SGHC 132; [2025] SGHC 5*

## 1 · Mediation Advocacy — past-paper questions

### 1.I Nature of mediation

Sub-points 1.I.1–1.I.6. Tested: 1.I.1–1.I.5. Drill 108 covers 1.I.6.

### 1.I.1 — Mediation compared with negotiation, arbitration and litigation

**QSQ-M2** · `1.I.1` · Sample Questions (Part B 2023-S) Mediation Q2 · `drp-m-1-1`

Which one of the following statements about mediation is TRUE?

A. Mediation is usually more costly and time-consuming than arbitration.
B. Mediation is confidential, rights-based and adversarial in nature.
C. Mediation involves a neutral and independent third party, who is the decision-maker.
D. Mediation is focussed on solutions and possible future relationship between parties.

**Answer: D.** Mediation looks forward to a solution and the parties' possible future relationship. A: it is usually cheaper and shorter. B: it is confidential but interest-based and non-adversarial; "rights-based and adversarial" describes arbitration and litigation. C: the mediator facilitates; the parties decide. Official key: D.
*Cite: MED-1 (see `drp-m-1-1`); SampleQs p60 Q2, key p122*

**Q2023-39** · `1.I.1` `1.I.2` · PYP 2023 Q39 · `drp-m-1-1` `drp-m-1-2`

Which of the following is accurate?

A. Mediation is an interest-based and confidential adjudication process.
B. Mediation should be considered alongside other forms of dispute resolution.
C. Mediation is a consensual process, focussing on the rights of the parties and past events.
D. Mediation should only be considered because of adverse cost order considerations.

**Answer: B.** The advocate considers mediation alongside negotiation, arbitration and litigation and advises the client which suits the dispute (ROC O 5 r 1(1); SCPD 53(2), (4)). A: mediation is interest-based and confidential but not *adjudication*; no one decides for the parties. C: it is consensual but focuses on interests and the future, not rights and past events. D: costs consequences (O 21 r 4(c)) are one reason, not the only one; the benefits to the client are the main ones.
*Cite: MED-1 (see `drp-m-1-1`, `drp-m-1-2`); ROC O 5 r 1(1); SCPD 53(2), (4)*

**Q2021M-1-9a** · `1.I.1` · PYP 2021 MED Q1.9(a) · `drp-m-1-1`

Mr Tan sells laptops from his shop; Mdm Ong, a friend of many years, bought two for $5,000 for her sons' home-based learning starting in a month. Problems began within a day; the distributor says the serial numbers do not match its official product numbers. Mr Tan refuses a refund, insisting nothing is wrong. Mdm Ong wants to sue. Explain to her the differences between mediation and litigation and which is more suitable in her case. (4 marks)

**Answer.** *Differences.* In mediation a neutral mediator helps the parties negotiate, but the parties decide; it is interest-based, consensual, confidential, relatively cheap and quick, and looks at solutions and the future relationship; it ends, if at all, in a settlement agreement. In litigation a judge decides on the parties' legal rights by an adversarial, public process focused on past events; it is slower and more expensive and ends in a binding judgment.

*Suitability.* Mediation suits Mdm Ong better. The sum is small ($5,000), so litigation costs would be disproportionate (counsel should advise settling paltry claims with minimum fuss and cost: *Lock Han Chng v Goh Jessiline* [2007] SGCA 56 at [45]); she needs working laptops within a month, which mediation can deliver faster; it can produce outcomes a court cannot order (replacement sets, an apology); and it can preserve a long friendship. Her alternative, if mediation fails, remains a claim in the Small Claims Tribunals or court; the distributor's evidence on the serial numbers strengthens her BATNA.
*Cite: MED-1 (see `drp-m-1-1`); [2007] SGCA 56 at [45]*

### 1.I.2 — What mediation is; possible outcomes

**QSQ-M3** · `1.I.2` · Sample Questions (Part B 2023-S) Mediation Q3 · `drp-m-1-2`

Which of the following statements about the possible outcomes of mediation is NOT TRUE?

A. In mediation, although each case is unique, most cases are settled and recorded in the form of a written settlement agreement.
B. In mediation, although each case is unique, it is possible for the parties to achieve a full settlement, or a partial settlement.
C. Where no settlement is reached at mediation, the parties will have to commit to litigating their case in court, without further opportunity to settle.
D. Where no settlement is reached at mediation, and the matter proceeds to trial, the mediation process would have narrowed down the issues in dispute between the parties.

**Answer: C.** Failing to settle at mediation does not end the chance to settle; the parties may settle at any later stage, and the duty to consider amicable resolution continues during the action (ROC O 5 r 1(1)). A, B and D are true outcomes: a written settlement, full or partial settlement, and narrowed issues. Official key: C.
*Cite: MED-1 (see `drp-m-1-2`); ROC O 5 r 1(1); SampleQs p60 Q3, key p122*

### 1.I.3 — Benefits for the client and for counsel

**Q2023-40** · `1.I.3` `1.I.4` · PYP 2023 Q40 · `drp-m-1-3` `drp-m-1-4`

Which one of the following is a benefit of mediation?

A. There is certainty of settlement.
B. There is no legal precedent due to confidentiality of the process.
C. There is formal discovery process to compel disclosure of information.
D. There is preservation or improvement of relationship between disputants.

**Answer: D.** Preserving or improving the relationship is one of the client benefits, with speed, control, more possible solutions, lower cost, confidentiality and choice of mediator. A, B and C are the three *disadvantages* turned round: there is no certainty of settlement, no precedent, and no formal discovery.
*Cite: MED-1 (see `drp-m-1-3`, `drp-m-1-4`)*

### 1.I.4 — Disadvantages of mediation

See Q2023-40 under 1.I.3 (options A–C are the disadvantages).

**Q2021M-1-3** · `1.I.4` `1.VIII.10` · PYP 2021 MED Q1.3 · `drp-m-1-4` `drp-m-1-61`

Anastasia Kumar, 28, has applied for a Personal Protection Order under s 65 of the Women's Charter against her husband Malcolm Yan, 42. Malcolm lost his job 9 months ago and has been verbally and physically abusing her; he has a violent temper, and Anastasia, who depends on him for her subsistence, is intensely afraid of him. Explain whether mediation is suitable for such a case. (4 marks)

**Answer.** Mediation is generally not suitable for the protection order application itself. Mediation assumes parties who can negotiate freely and "voluntarily reach an agreement" (MA s 3(1)(d)). Here there is serious ongoing violence, fear and economic dependence: a gross power imbalance in which Anastasia cannot negotiate safely or freely, and any "agreement" risks being coerced. Her safety, not a compromise, is the issue; a protection order is a matter for the court. Joint sessions could also expose her to further intimidation. The Family Justice Courts recognise this: the court may dispense with attendance at mediation or counselling where it is not in the parties' interest, for example where family violence has been committed (Women's Charter s 139I(3); FJCPD 82(7)). Mediation might later help on other matters (e.g. maintenance or children, if a divorce follows) only with safeguards: separate sessions, a support person, and Anastasia's free choice. Her lawyer should still inform her of the options available (PCR r 15A(2)(a)) but advise that mediation is not appropriate for the PPO.
*Cite: MA s 3(1)(d); Women's Charter s 139I(3); FJCPD 82(7); PCR r 15A(2)*

### 1.I.5 — Facilitative v evaluative mediation

**Q2021M-1-4** · `1.I.5` · PYP 2021 MED Q1.4 · `drp-m-1-5`

Paul (accountant, operations and finance) and Mary (fashion graduate, design and procurement) have been friends for 20 years and set up an online fashion business 5 years ago. For 6 months they have disagreed: Mary accuses Paul of mismanaging the accounts; Paul says she does not understand accounting, and is upset that her temper has caused high staff turnover. He wants to end the partnership. They agree to mediate at SMC and are asked what type of mediation and mediator they want. Advise Paul, with reference to the objectives, type and role of the mediator and the process. (4 marks)

**Answer.** Facilitative mediation suits this dispute. *Objectives:* the real issues are relational and interest-based (trust, respect, how to part or restructure fairly after a 20-year friendship), not a legal rights question; facilitative mediation avoids legal positions and works on underlying needs and interests. *Mediator:* an expert in the mediation process, not necessarily in the subject matter, who conducts the process, keeps the dialogue constructive and helps the parties negotiate, intervening less. *Process:* joint and private sessions where each can be heard (Mary on the accounts, Paul on staff and conduct), options generated together (buy-out, an independent accounts review, restructured roles, an orderly wind-down) and tested against objective criteria such as a valuation. *Why not evaluative:* an evaluative mediator, a subject-matter expert who advises on likely legal outcomes and persuades, intervenes more and gives the parties less control, which suits a rights-based money dispute better. If the accounts allegation becomes central, the parties could jointly bring in an accountant as an expert within the facilitative process.
*Cite: MED-1 p12 (see `drp-m-1-5`)*

### 1.II Mediation institutions and schemes

Sub-points 1.II.1–1.II.8. Tested: 1.II.1, 1.II.4, 1.II.5, 1.II.6, 1.II.7, 1.II.8. Drills 109–110 cover 1.II.2 and 1.II.3.

### 1.II.1 — Singapore Mediation Centre (SMC)

**QSQ-M5** · `1.II.1` · Sample Questions (Part B 2023-S) Mediation Q5 · `drp-m-1-7`

Which of the following statements is TRUE of the Singapore Mediation Centre?

I. It is a for-profit organisation.
II. It promotes the settlement of disputes by using alternative dispute resolution processes.
III. It is to provide mediator training and accreditation.
IV. It is to provide and administer mediation services.

A. I, III and IV.
B. II, III and IV.
C. II and III.
D. I, II, III and IV.

**Answer: B.** SMC is a *not-for-profit* body set up in 1997 (so I is false) that promotes ADR, trains and accredits mediators, and provides and administers mediation services. Official key: B.
*Cite: MED-2 p4, p9 (see `drp-m-1-7`); SampleQs p61 Q5, key p122*

**Q2023-43** · `1.II.1` · PYP 2023 Q43 · `drp-m-1-7`

Which of the following are functions of the Singapore Mediation Centre?

I. To provide mediator training
II. To provide mediator accreditation
III. To provide mediation services
IV. To provide mediation advocacy services

A. I, II, III and IV
B. I, II and III only
C. II, III and IV only
D. I, III and IV only

**Answer: B.** SMC's functions are mediator training and accreditation, providing and administering mediation, and other ADR services such as adjudication and neutral evaluation. It does not act as an advocate for parties: mediation advocacy is what the parties' lawyers do (IV). Note the 2023-S sample (QSQ-M5) treats training and accreditation as one function.
*Cite: MED-2 p4, p9 (see `drp-m-1-7`)*

### 1.II.4 — Community Mediation Centre (CMC)

**Q2023-42** · `1.II.4` `1.III.3` · PYP 2023 Q42 · `drp-m-1-10` `drp-m-1-17`

Under the Criminal Procedure Code, for a non-arrestable offence, a police officer may refer the case for mediation by a mediator from which of the following?

A. Community Mediation Centre
B. Tripartite Alliance for Dispute Management
C. Singapore International Mediation Centre
D. Singapore Mediation Centre

**Answer: A.** Where information relates to a non-arrestable offence, a police officer may refer the case to a mediator of a Community Mediation Centre (CPC 2010 s 16(1)(c)). B handles employment disputes; C international commercial disputes; D civil and family disputes generally, none of them under s 16.
*Cite: CPC 2010 s 16(1)(c) (see `drp-m-1-10`)*

### 1.II.5 — Court-based mediation

See Q2021M-1-5b under 1.IV.4 (mediation at the State Courts' dispute resolution centre).

### 1.II.6 — Industry schemes administered by SMC

**Q2023-44** · `1.II.6` · PYP 2023 Q44 · `drp-m-1-12`

The Committee for Private Education Mediation-Arbitration Scheme aims to help:

A. settle disputes between students and the Ministry of Education.
B. settle disputes between students and the tuition agencies.
C. settle disputes between students and their course leaders.
D. settle disputes between students and private education institutions.

**Answer: D.** The scheme resolves disputes between students and private education institutions (enrolment, fees, discipline). A, B and C name the wrong counterparty. *What changed:* the CPE was dissolved in Oct 2024 and its functions passed to SkillsFuture Singapore; the 2026 slides call it the SSG Private Education Institution Mediation-Arbitration Scheme.
*Cite: MED-2 p9–11 (see `drp-m-1-12`)*

**Q2023-45** · `1.II.6` · PYP 2023 Q45 · `drp-m-1-12`

Which of these is an industry specific mediation scheme?

A. Singapore Infrastructure Dispute Management Scheme
B. Council for Estate Agencies Mediation Sub-Scheme
C. Strata Titles Board Dispute Management Protocol
D. Committee for Private Education Arbitration Protocol

**Answer: B.** The Council for Estate Agencies Mediation Sub-Scheme (SMC-administered) mediates disputes between clients and estate agents. A: the real instrument is the Singapore Infrastructure Dispute-Management *Protocol*, a dispute board, not a mediation scheme. C: the Strata Titles Board runs its own mediation, but no "Dispute Management Protocol" of that name exists. D: the CPE scheme was a Mediation-Arbitration *Scheme*. The distractors misname real schemes.
*Cite: MED-2 p9–11 (see `drp-m-1-12`, `drp-m-1-13`)*

**Q2023-46** · `1.II.6` · PYP 2023 Q46 · `drp-m-1-12`

Which is true of the Singapore Infrastructure Dispute-Management Protocol?

A. It is an appointed Dispute Board that follows large construction projects to manage and resolve issues at the end of the project only.
B. It is an appointed Dispute Board that follows large infrastructure projects to manage and resolve issues at the middle point to the end of the project only.
C. It is an appointed Dispute Board that follows large construction or infrastructure projects to manage and resolve issues from start to finish.
D. It is an appointed Dispute Board that deals with large construction project disputes only at the start of the project.

**Answer: C.** The Protocol appoints a Dispute Board at the outset that follows a large project from start to finish, managing issues before they become disputes. A, B and D wrongly confine it to part of the project.
*Cite: MED-2 p11 (see `drp-m-1-12`)*

### 1.II.7 — Schemes not administered by SMC; private providers

**Q2021M-1-9b** · `1.II.7` `1.II.1` `1.II.4` · PYP 2021 MED Q1.9(b) · `drp-m-1-13` `drp-m-1-7` `drp-m-1-10`

[Facts: Q2021M-1-9a under 1.I.1.] Mr Lee, a mutual friend and senior lawyer with no mediation training or accreditation, offered to mediate, and the parties agreed. List two mediation service providers Mr Tan and Mdm Ong could have approached instead. (2 marks)

**Answer.** Any two of: the **Singapore Mediation Centre** (civil disputes of any amount; a designated mediation service provider under MA s 7, so a pre-action settlement it administers can be recorded as a court order under s 12(3)(a)); the **Community Mediation Centre** (social and community disputes between friends and neighbours); the **Consumers Association of Singapore (CASE)** (consumer disputes with retailers). Using SMC also gives the parties a trained, accredited mediator, unlike Mr Lee.
*Cite: MED-2 (see `drp-m-1-7`, `drp-m-1-10`, `drp-m-1-13`); MA ss 7, 12(3)(a)*

### 1.II.8 — Designated mediation service providers and certified mediators

**Q2023-49** · `1.II.8` · PYP 2023 Q49 · `drp-m-1-14`

Which of these organisations is a designated mediation service provider under section 12(3)(a) read with sections 7(1)(a) and 7(2) of the Mediation Act 2017?

A. Singapore Mediation Centre
B. Singapore International Dispute Resolution Academy
C. The Law Society of Singapore
D. Singapore International Mediation Institute

**Answer: A.** From 1 Nov 2017 the designated providers were SIMC, SMC, TADM and WIPO AMC. B: SIDRA is a research and training academy. D: SIMI runs the approved *certification scheme* (s 7(1)(b)), not a provider designation. C: the Law Society runs a mediation scheme but was not designated.
*Cite: MA ss 7, 12(3)(a); MinLaw press release, 1 Nov 2017 (see `drp-m-1-14`)*

### 1.III Legal sources and the basis of mediation

Sub-points 1.III.1–1.III.4. Tested: 1.III.3 (Q2023-42), 1.III.4 (Q2021M-1-5b). Drills 111–112 cover 1.III.1 and 1.III.2.

### 1.III.3 — Mediation under statute

See Q2023-42 under 1.II.4 (CPC s 16(1)(c)).

### 1.III.4 — Mediation by direction of a court or authority

See Q2021M-1-5b under 1.IV.4 (a District Judge urging mediation; the Court may order ADR under O 5 r 3).

### 1.IV Duty to consider amicable resolution; costs

Sub-points 1.IV.1–1.IV.9. Tested: 1.IV.1, 1.IV.4, 1.IV.6, 1.IV.7, 1.IV.9. Drills 113–116 cover 1.IV.2, 1.IV.3, 1.IV.5 and 1.IV.8.

### 1.IV.1 — Duty to consider amicable resolution; pre-action offer (O 5 r 1)

**Q2023-48** · `1.IV.1` · PYP 2023 Q48 · `drp-m-1-19`

Under Order 5 Rule 1(2) of the Rules of Court 2021, a party is:

A. To make an offer of amicable resolution before commencing the action even when the party has reasonable grounds not to do so.
B. To make an offer of amicable resolution only after commencing the action unless the party has reasonable grounds not do so.
C. To make an offer of amicable resolution before commencing the action unless the party has reasonable grounds not to do so.
D. To not make an offer of amicable resolution at any time whether before or after commencing the action.

**Answer: C.** O 5 r 1(2) is quoted in C. A drops the "reasonable grounds" exception; B moves the offer to after commencement; D contradicts the rule.
*Cite: ROC 2021 O 5 r 1(2)*

### 1.IV.4 — Costs consequences (O 21 rr 2(2)(a), 4(c))

**Q2021M-1-5b** · `1.IV.4` `1.IV.6` `1.III.4` `1.II.5` · PYP 2021 MED Q1.5(b) · `drp-m-1-22` `drp-m-1-24` `drp-m-1-18` `drp-m-1-11`

At the pre-trial conference of your client's case in the State Courts, the District Judge strongly urged the parties to attempt mediation at the State Courts' dispute resolution centre. Your client is reluctant: he thinks he has a very strong case and mediation would waste time, and is thinking of opting out. What would you advise? (4 marks; answer under current law)

**Answer.** Advise him not to opt out without a good reason. (1) *Duty:* every party has a duty to consider amicable resolution before and during an action (ROC O 5 r 1(1)), and the Court may order the parties to attempt it, and may require a party that refuses to give its reasons in a sealed document opened only on costs (O 5 r 3(1), (3)–(4)). (2) *Presumption of ADR:* all civil claims in the State Courts are presumed suitable for ADR, and if the Court considers ADR suitable and a party opts out for unsatisfactory reasons, that conduct may be taken into account in later costs orders (StCPD 34(5), (8); O 21 r 2(2)(a)). (3) *Costs even if he wins:* the Court may disallow or reduce a successful party's costs, or make it pay costs, if it has not discharged its O 5 duties (O 21 r 4(c)). Believing one's case strong is not, on its own, a good reason: in *Halsey* the merits are only one factor, and a party "sure to win" should have that belief reality-tested. (4) *Benefits:* court mediation is low-cost and confidential, can end the case sooner, and even without settlement can narrow the issues. A strong case simply strengthens his BATNA and his hand at the mediation. He should attend, and you should prepare him (interests, BATNA, settlement range).

*What changed:* in 2021 this was governed by ROC 2014 and the State Courts Practice Directions 2014 (presumption of ADR in para 35, with the "ADR Form"); ROC 2021 O 5 and O 21 and StCPD 2021 para 34 now apply. The result is the same.
*Cite: ROC 2021 O 5 rr 1, 3, O 21 rr 2(2)(a), 4(c); StCPD 34(5), (8); Halsey [2004] 1 WLR 3002 at [16]*

### 1.IV.6 — State Courts PD 34: presumption of ADR

**Q2021M-1-5a** · `1.IV.6` · PYP 2021 MED Q1.5(a) · `drp-m-1-24`

What is the "presumption of ADR" that applies to civil cases in the State Courts? (2 marks)

**Answer.** All civil claims filed in the State Courts are presumed suitable for alternative dispute resolution. At a case conference the Court may refer suitable matters to a Court ADR modality (mediation, conciliation or neutral evaluation); parties wanting Court ADR earlier file Form 2 of Appendix A1; and a party who opts out for unsatisfactory reasons, where the Court considers ADR suitable, risks that conduct being taken into account in later costs orders under O 21 r 2(2)(a) (StCPD 34(5), (6), (8)). (In 2021 the same presumption was in StCPD 2014 para 35.)
*Cite: StCPD 34(5), (6), (8); ROC O 21 r 2(2)(a)*

### 1.IV.7 — Family Justice Courts PD 81(2)

See Q2021M-1-6 under 1.VIII.10 (duty to advise on mediation in family proceedings).

### 1.IV.9 — Mediation costs are recoverable; settle small claims (Legis Point; Lock Han Chng)

**Q2023-47** · `1.IV.9` · PYP 2023 Q47 · `drp-m-1-27`

In the case of ____________________, the Singapore High Court held that the work undertaken by counsel during mediation was similar in nature to other negotiation work, which may be taken into account by the court when awarding party-and-party costs.

A. UJN v UJO [2018] SGFC 16
B. Legis Point LLC v Tay Choon Ai [2018] 3 SLR 1269
C. Lock Han Chng Jonathan v Goh Jessiline [2008] 2 SLR(R) 455
D. Sita Jaswant Kaur v Surinar Singh s/o Jaswant Singh [2013] 4 SLR 838

**Answer: B.** *Legis Point LLC v Tay Choon Ai* ([2017] SGHC 325, reported [2018] 3 SLR 1269). A is a Family Court case on settlement agreements in family proceedings; C is the Court of Appeal on settling paltry claims; D is on whether a post-mediation agreement binds (reversed on appeal, [2014] SGCA 37).
*Cite: [2017] SGHC 325 (see `drp-m-1-27`)*

**Q2023-50** · `1.IV.9` · PYP 2023 Q50 · `drp-m-1-27`

In the case of ____________________, the Court of Appeal made the observation that, 'the role of counsel in pursuing their clients' interests in a court of law, where paltry monetary claims were involved, is to exercise the degree of responsibility expected of an officer of the court and advise their clients to settle the dispute with minimum fuss and minimum cost'.

A. UJN v UJO [2018] SGFC 16
B. Legis Point LLC v Tay Choon Ai [2018] 3 SLR 1269
C. Lock Han Chng Jonathan v Goh Jessiline [2008] 2 SLR(R) 455
D. Sita Jaswant Kaur v Surinar Singh s/o Jaswant Singh [2013] 4 SLR 838

**Answer: C.** *Lock Han Chng Jonathan v Goh Jessiline* [2007] SGCA 56 at [45] (reported [2008] 2 SLR(R) 455). It is the only Court of Appeal decision listed. A and D are first-instance decisions on settlement agreements; B is the High Court on mediation costs.
*Cite: [2007] SGCA 56 at [45] (see `drp-m-1-27`)*

### 1.V Mediation Act 2017

Sub-points 1.V.1–1.V.11. Tested: 1.V.3, 1.V.5, 1.V.6, 1.V.10, 1.V.11. Drills 117–122 cover 1.V.1, 1.V.2, 1.V.4 and 1.V.7–1.V.9.

### 1.V.3 — Application of the Act (s 6)

See Q2021M-1-9g under 1.V.6 (does the Act apply to an informal mediation by a friend?).

### 1.V.5 — Confidentiality and "mediation communication" (ss 2(1), 9(1))

**Q2023-41** · `1.V.5` · PYP 2023 Q41 · `drp-m-1-32`

Under the Mediation Act 2017, "mediation communication" is defined as:

A. (a) anything said or done; (b) any document prepared; or (c) any information provided, for the purpose of or in the course of the mediation, and includes a mediation agreement or mediated settlement agreement.
B. (a) anything said or done; (b) any written document prepared; or (c) any written information provided only, for the purpose of or in the course of the mediation, and includes a mediation agreement only.
C. (a) anything said or done; (b) any document prepared; or (c) any information provided, for the purpose of the mediation, and includes a mediation agreement or mediated settlement agreement.
D. (a) anything done; (b) any document prepared; or (c) any information provided, for the purpose of or in the course of the mediation, and includes a mediated settlement agreement only.

**Answer: A.** A is the s 2(1) definition word for word. B adds "written" and drops the settlement agreement; C drops "or in the course of"; D drops "said" and the mediation agreement. The definition is in s 2(1), not s 1 as some notes say.
*Cite: MA s 2(1)*

### 1.V.6 — Disclosure allowed without permission (s 9(2))

**Q2021M-1-9g** · `1.V.6` `1.V.5` `1.V.3` · PYP 2021 MED Q1.9(g) · `drp-m-1-33` `drp-m-1-32` `drp-m-1-30`

[Facts: Q2021M-1-9a under 1.I.1.] At the mediation before Mr Lee (no lawyers present), Mr Tan admitted that the laptops were counterfeits he sourced online, and that he had sold laptops this way before to increase margins. They settled in a signed agreement written in Chinese: (i) Mr Tan's written apology; (ii) he pays 100% of the price within 3 months; (iii) Mdm Ong returns the laptops on full payment. Mdm Ong now wants to post Mr Tan's admissions on social media, with a copy of the settlement agreement as proof, to warn others. Advise. (2 marks)

**Answer.** Advise her not to post. *If the Mediation Act applies* (a mediation under a mediation agreement, in writing in any form, conducted in Singapore: MA ss 4, 6(1)), Mr Tan's admissions and the settlement agreement are "mediation communications" (s 2(1)), which she must not disclose to third parties (s 9(1)). Section 9(2)(j) does allow disclosure where the communication "relates to the commission of any offence under any written law", and selling counterfeit goods is likely an offence. So the admissions are not absolutely protected, and she may report them to the police or the relevant authority (s 9(2)(h)–(j)). But whether s 9(2)(j) licenses broadcasting them to the public on social media, rather than reporting them, is an open point with no authority: one view reads the exception literally (any disclosure of a communication relating to an offence); the other reads it, in context with paras (g)–(i), as permitting disclosure for the purpose of dealing with the offence. *If the Act does not apply,* the communications are still without prejudice and confidential at common law (*Mariwu* [2006] SGCA 37 at [24]). Either way, a public post risks a defamation claim and undermines the settlement she wants paid. The safe course: report to the authorities, and keep the agreement private unless needed to enforce it (with the court's permission under s 9(3)(a) if the Act applies).
*Cite: MA ss 2(1), 4, 6(1), 9(1)–(3); [2006] SGCA 37 at [24]*

### 1.V.10 — Recording a mediated settlement as an order of court (s 12(1)–(3))

**Q2021M-1-2** · `1.V.10` · PYP 2021 MED Q1.2 · `drp-m-1-37`

When a mediation is conducted before proceedings commence, what requirements must the mediated settlement agreement fulfil before it may be recorded as an order of court for enforcement under the Mediation Act 2017? (4 marks)

**Answer.** Under MA s 12, where no court proceedings have been commenced: (1) the application is made by a party *with the consent of all the other parties* (s 12(1)); (2) within 8 weeks of the agreement, or a longer period the court allows (s 12(2)); and the court may record it if (3) the mediation was administered by a designated mediation service provider or conducted by a certified mediator (s 12(3)(a)); (4) the agreement is in writing and signed by or on behalf of all parties (s 12(3)(b)); and (5) it contains the prescribed information (s 12(3)(c)): each party's name, each mediator's name, the provider's name if any, each certification scheme of each mediator if any, the date of the agreement, and the terms of settlement (Mediation Rules 2017 r 2). Even then the court may refuse on the s 12(4) grounds (vitiating factors, subject matter not capable of settlement, a term not enforceable as a court order, a child's best interests, public policy).
*Cite: MA s 12(1)–(4); Mediation Rules 2017 r 2*

**Q2021M-1-9h** · `1.V.10` `1.V.11` `1.VI.1` `1.VI.4` · PYP 2021 MED Q1.9(h) · `drp-m-1-37` `drp-m-1-38` `drp-m-1-39` `drp-m-1-42`

[Facts: Q2021M-1-9a and Q2021M-1-9g.] Mr Tan has not paid within 3 months. Mdm Ong has heard that the Mediation Act lets settlement agreements be enforced as court orders, and asks whether you can apply to enforce the payment term. Advise. (3 marks)

**Answer.** Not under the Mediation Act. Recording under s 12 is unavailable because: (1) the mediation was conducted by Mr Lee, who is neither a certified mediator nor acting for a designated provider (s 12(3)(a)); (2) the application needs all parties' consent (s 12(1)), which Mr Tan, now in default, is unlikely to give; and (3) it must be made within 8 weeks of the agreement unless the court extends time (s 12(2)), and more than 3 months have passed. Also, the agreement is in Chinese and must contain the prescribed information (Mediation Rules r 2), which an informal agreement may lack, and a translation would be needed. Instead, Mdm Ong can sue on the settlement agreement as a contract (it is binding if the usual elements and an intention to be bound are present: *Tiong Swee Eng v Yeo Khee Siang* [2015] SGHC 116 at [19]–[21]), most cheaply in the Small Claims Tribunals for the $5,000 refund, tendering return of the laptops as clause (iii) requires. If the Act applies, disclosing the agreement to enforce it needs the court's permission (s 9(3)(a)).
*Cite: MA ss 9(3)(a), 12(1)–(3); [2015] SGHC 116 at [19]–[21]*

### 1.V.11 — Refusal to record; enforcement (s 12(4)–(5))

See Q2021M-1-2 and Q2021M-1-9h under 1.V.10.

### 1.VI Mediated settlement agreements

Sub-points 1.VI.1–1.VI.6. Tested: 1.VI.1, 1.VI.2, 1.VI.4. Drills 123–125 cover 1.VI.3, 1.VI.5 and 1.VI.6.

### 1.VI.1 — A settlement agreement is a contract

See Q2021M-1-9h under 1.V.10 (sue on the settlement agreement as a contract).

### 1.VI.2 — Drafting checklist

See Q2021M-1-10 under 1.VII.4 (default, security and payment terms for an instalment settlement).

### 1.VI.4 — Ways to enforce a mediated settlement

See Q2021M-1-9h under 1.V.10.

### 1.VII The seven elements of effective negotiation

Sub-points 1.VII.1–1.VII.7. Tested: 1.VII.1–1.VII.4, 1.VII.6, and 1.VII.5 only in passing (QSQ-M9). Drills 126–127 cover 1.VII.5 and 1.VII.7; Drills 128–139 are extra drills on all seven elements (Bennett's 10 Nov quiz weak spot).

### 1.VII.1 — Interests, not positions

**Q2021M-1-1** · `1.VII.1` · PYP 2021 MED Q1.1 · `drp-m-1-45`

You have a brief where the client wants to sue for defamation over an online review by a disgruntled customer, who was unhappy with the quality of products bought from the client and accused it of selling counterfeit goods. (a) List one possible interest of your client. (1 mark) (b) Explain how you would uncover your client's interests. (2 marks)

**Answer.** (a) Any one of: protecting its reputation and goodwill (getting the review taken down or corrected); preserving its business and future sales; a public retraction or apology; keeping the customer; avoiding the cost and publicity of a court case. (Damages are a *position*, not an interest.) (b) Dig beneath the position ("we want to sue for defamation") by asking open questions, "why?" and "why not?": why does the review matter, what would a good outcome look like, what worries you most? Listen actively to understand rather than to debate, reflect back what is heard, and then clarify and prioritise the interests identified (e.g. reputation first, money second).
*Cite: MED-4 (see `drp-m-1-45`, `drp-m-1-49`)*

**Q2023-53** · `1.VII.1` `1.VII.2` `1.VII.3` `1.VII.6` · PYP 2023 Q53 · `drp-m-1-45` `drp-m-1-46` `drp-m-1-47` `drp-m-1-50`

During mediation, which of the following techniques may be employed by counsel?

I. Focus on interests, not positions - help the parties to move from being entrenched in their positions to exploring whether and how their interests can be better served.
II. Invent options for mutual gain - help the mediator to lead the process for parties to consider possibilities for settlement to better promote their interests.
III. Legitimacy - substantiate solutions with objective criteria, rather than subjective or emotional bases of the parties.
IV. Separate the people from the problem - encourage parties to suspend their personal animosities and instead focus on their common problem at hand.

A. I, II, III and IV
B. I, II and III only
C. I, III and IV only
D. I, II and IV only

**Answer: A.** Each statement is one of the seven elements used as a technique: interests (I), options (II), criteria or legitimacy (III), and relationship, "separate the people from the problem" (IV).
*Cite: MED-4 (see `drp-m-1-45`–`drp-m-1-50`)*

[PYP 2021 MED Q2 facts.] Mayu Tanaka runs "Japanese Booth", a popular eatery in the financial district (organic Japanese-style ramen, sushi, sashimi; her mother's recipes). Her former head chef Marcus Yeo, whom she hired as a new graduate and trusted with the concept, layout, décor, logo, menu and the recipes, resigned in November 2020; three cooks he had brought in followed. He then opened "Nippon Pot" in a suburban mall with a similar concept, décor and logo, near-identical menu items with similar names ("Tokyo Rhapsody" for her "Kyoto Rhapsody"), a door slogan claiming its food is "cheaper, tastier, healthier and more truly organic than those at the Japanese Booth's", and WhatsApp messages enticing her staff. Mayu estimates lost profits of about $250,000 (November 2020 – October 2021), much of it from the pandemic. Her firm is suing Marcus and Nippon Pot in the State Courts for passing off, copyright infringement, interference with contract and defamation; she wants to try mediation at the State Courts to save costs. She wants fair competition, differentiation of his eatery, no poaching, the slogan withdrawn, some payment ("at least to cover my legal costs"; "ask him for $50,000"), and remorse, but is "prepared to be reasonable". The defence denies copying and use of the recipes, says a suburban outlet does not compete, and pleads its own pandemic losses.

**Q2021M-2-1** · `1.VII.1` `1.VII.2` `1.VII.3` `1.VII.4` · PYP 2021 MED Q2.1 · `drp-m-1-45` `drp-m-1-46` `drp-m-1-47` `drp-m-1-48`

Identify the possible interests of both parties and their respective alternatives. Draw up a settlement proposal of options that might address these interests, and explain how it would resolve the dispute in a mutually acceptable way. (20 marks)

**Answer (outline).**

*Interests.* Mayu: business survival and focus on her eatery; protecting her concept, brand and her mother's recipes; fair competition and differentiation; keeping her staff; correcting the slogan's slur on her food's authenticity; recognition and remorse (an apology); some money, at least her legal costs; low cost and speed. Marcus/Nippon Pot: keeping a thriving business open; avoiding damages, costs and an injunction; reputation (a defamation finding or "copycat" label); keeping his staff; certainty; probably also not being seen to admit wrongdoing.

*Alternatives.* Mayu's BATNA: trial in the State Courts; WATNA: losing on copying (recipes are hard to protect without a restraint clause; "some dishes are just what they are"), large costs, and losses attributed to the pandemic; MLATNA: partial success (perhaps on the slogan and get-up), damages well below $250,000 after causation, and a long, costly process that distracts from her business. Marcus's BATNA: defeating most claims; WATNA: injunctions forcing a rebrand mid-recovery, damages and costs, defamation liability for a comparative slogan he cannot substantiate; MLATNA: some liability and costs, plus uncertainty. Both sides' alternatives are expensive and uncertain, which creates room to settle.

*Options (a package).* (1) Differentiation: Nippon Pot changes its logo, signage and décor features and renames the look-alike menu items within an agreed period. (2) The slogan is removed at once and replaced; a short written apology or acknowledgment to Mayu, privately or by a neutral notice. (3) Non-solicitation: no approaches to Japanese Booth's current staff for an agreed period. (4) Recipes: an undertaking not to use specified recipes or to market dishes as her mother's; a confidentiality undertaking. (5) Payment: a contribution to Mayu's legal costs, by instalments if cash is tight (anchored by her own "at least legal costs" and the $50,000 opening; criteria: costs actually incurred, the likely court range after allowing for the pandemic). (6) Each side's mutual non-disparagement; discontinuance of the suit with no admission of liability; confidentiality; default clause (e.g. consent judgment for a stated sum on breach); timeline and a monitoring step.

*Why it works.* It meets Mayu's real interests (fair competition, differentiation, staff, reputation, recognition, costs) without forcing Marcus to close, admit copying publicly or pay a sum that sinks him; it uses objective criteria (costs incurred, likely outcome, market practice on rebranding) so each side can justify it; both sides beat their MLATNA on cost, time and certainty; and the relationship issues (betrayal, remorse) are addressed directly by the apology. Commit only once interests, options, criteria and alternatives have been worked through, in a clear written agreement.
*Cite: MED-4 (see `drp-m-1-45`–`drp-m-1-51`)*

### 1.VII.2 — Options

**QSQ-M6** · `1.VII.2` · Sample Questions (Part B 2024) Mediation Q6 · `drp-m-1-46`

Which of the following techniques should be used during the option generation phase of a negotiation to encourage creativity?

A. Immediately evaluating each option as it is proposed.
B. Evaluating and eliminating impractical options.
C. Limiting discussion to legally viable options.
D. Separating inventing from deciding.

**Answer: D.** Generate options first and evaluate later: brainstorming rules are no commitment, no attribution, no criticism and no evaluation. A, B and C all evaluate or filter during invention, which stifles creativity. Official key: D.
*Cite: MED-4 (see `drp-m-1-46`); SampleQs p62 Q6, key p122*

### 1.VII.3 — Criteria (legitimacy)

**QSQ-M7** · `1.VII.3` · Sample Questions (Part B 2024) Mediation Q7 · `drp-m-1-47`

What role do objective criteria play in a negotiation?

A. To challenge or contradict the other party's position.
B. To assist in evaluating options based on subjective standards.
C. To help persuade the other party that they are being treated fairly.
D. To finalise the terms of the agreement.

**Answer: C.** Objective criteria (legitimacy) let each side see that an option is fair: a sword to persuade, a shield against unfairness, and a face-saving justification. A: their purpose is persuasion by fairness, not contradiction. B: the standards are *objective*. D: finalising terms is commitment. Official key: C.
*Cite: MED-4 p13–14 (see `drp-m-1-47`); SampleQs p62 Q7, key p122*

**Q2023-55** · `1.VII.3` · PYP 2023 Q55 · `drp-m-1-47`

Which of the following are NOT ways to determine "Objective Criteria"?

A. Look at past precedents.
B. Consider the position at Law.
C. Ask what the Market Value of the subject matter is.
D. Let one party decide on what is fair for both parties.

**Answer: D.** One party deciding is the opposite of an objective standard. Absent a standard, *fair procedures* are used: one cuts and the other chooses, taking turns, drawing lots, or letting a *neutral* decide. A, B and C are standard sources of criteria (precedent, the law, market value).
*Cite: MED-4 p13–14 (see `drp-m-1-47`)*

### 1.VII.4 — Alternatives: BATNA, WATNA, MLATNA

**QSQ-M8** · `1.VII.4` · Sample Questions (Part B 2024) Mediation Q8 · `drp-m-1-48`

What is the principal purpose of identifying one's alternatives (as well as those of the other party) during a negotiation?

I. To help dominate the conversation.
II. To expedite the negotiation process.
III. To understand the relative bargaining power of each party.
IV. To evaluate whether to accept the other party's offer or walk away from the negotiation.

A. I and II only.
B. II and III only.
C. III and IV only.
D. I, II, III and IV.

**Answer: C.** Alternatives show each side's bargaining power (III) and are the yardstick for accepting an offer or walking away (IV). I and II are not their purpose. Official key: C.
*Cite: MED-4 (see `drp-m-1-48`); SampleQs p62 Q8, key p122*

**Q2023-54** · `1.VII.4` · PYP 2023 Q54 · `drp-m-1-48`

Which statement is true about "Alternatives"?

A. An offer should only be accepted if your BATNA is better.
B. It is important to understand your BATNA alone and not the other side's.
C. They involve the other party.
D. They should be used to evaluate whether options should be accepted.

**Answer: D.** Alternatives are used to evaluate whether to accept an option. A reverses the rule: accept if the offer is at least as good as your BATNA; walk away if your BATNA is better. B: estimate the other side's BATNA too, to gauge its bargaining power. C: alternatives are unilateral; it is *options* that need the other party.
*Cite: MED-4 (see `drp-m-1-48`)*

**Q2021M-1-10** · `1.VII.4` `1.VI.2` · PYP 2021 MED Q1.10 · `drp-m-1-48` `drp-m-1-40`

Ocean Breeze supplied $130,000 of truffles to Luxury Palace, payment due 15 March 2021. It sued in the State Courts; Luxury Palace alleged defects and counterclaimed $85,000. At court mediation, Luxury Palace's solicitor said his clients owe about $800,000 to 5 creditors, can pay "no more than $50,000 in 10 monthly instalments of $5,000", as a "take-it-or-leave-it" goodwill offer, and would drop the counterclaim if accepted; otherwise they will go to trial to prove the defects, and may voluntarily wind up, even mid-trial, if things get worse. Advise Manson Lim, Ocean Breeze's sole director, on the options and their implications. (8 marks)

**Answer.** *Options.* (1) **Accept** $50,000 by instalments: certain, quick, cheap, the counterclaim goes; but Ocean Breeze writes off $80,000 and bears the risk of default over 10 months. (2) **Counter-offer** (the offer is called take-it-or-leave-it, but it is a negotiating position): more money or faster payment, plus protection such as a larger first payment, security (a guarantee from a director or parent, a charge), an acceleration clause and a default clause entitling Ocean Breeze to enter consent judgment for the full claim if any instalment is missed. Test the claim of insolvency using objective criteria: ask for management accounts or evidence of the $800,000 debts. (3) **Reject and go to trial**: Ocean Breeze may win $130,000 plus interest and costs, but faces the counterclaim, costs and delay, and (its WATNA) a judgment against a company that winds up, leaving it an unsecured creditor sharing pro rata with $800,000 of other debt, possibly recovering little. Its MLATNA is a paper judgment worth less than $50,000 in hand.

*Implications and advice.* Compare each offer with Ocean Breeze's BATNA, WATNA and MLATNA, not with the face value of its claim. If the insolvency claim is credible, a secured, front-loaded settlement with a default clause may beat trial; if not, the threat of winding up is a tactic to be reality-tested. Draft any settlement carefully: payment arrangements, default provisions, security, withdrawal of the counterclaim and discontinuance, confidentiality, and authority to settle. Note too the risk that payments made shortly before an insolvency are attacked as preferences; security and prompt payment help. The decision is Manson's (party autonomy).
*Cite: MED-4 (see `drp-m-1-48`); MED-3 p28 (see `drp-m-1-40`)*

### 1.VII.6 — Relationship

**QSQ-M9** · `1.VII.6` `1.VII.5` · Sample Questions (Part B 2024) Mediation Q9 · `drp-m-1-50` `drp-m-1-49`

Which of the following may assist in fostering a constructive working relationship between the parties during mediation?

I. Dealing with the issues objectively, without being influenced by negative feelings towards a party.
II. Building rapport through verbal and non-verbal communication.
III. Demonstrating empathy by putting oneself in the other party's shoes to appreciate their perspective.
IV. Allowing an appropriate degree of venting to enable the parties to express and identify their feelings.

A. I and II only.
B. III and IV only.
C. I, II and III only.
D. I, II, III and IV.

**Answer: D.** All four are the relationship toolkit: separate the people from the problem (I), communication and rapport (II), perception or empathy (III), and emotion, allowing venting (IV). Official key: D.
*Cite: MED-4 (see `drp-m-1-50`); SampleQs p63 Q9, key p122*

### 1.VIII Role and ethics of the mediation advocate

Sub-points 1.VIII.1–1.VIII.11. All tested.

### 1.VIII.1 — Role of the mediation advocate

**Q2023-37** · `1.VIII.1` · PYP 2023 Q37 · `drp-m-1-52`

As counsel acting for a party who will be engaged in mediation, which of the following most accurately describes the role of the mediation advocate?

A. Drafting of pleadings (in preparation for trial)
B. Litigation advocacy (to protect client's rights)
C. Drafting of any settlement agreement (with opposing counsel)
D. Verbatim note-taking (as documentary evidence)

**Answer: C.** The advocate ensures settlement terms are in the client's interest, reflect its intentions and are clearly prepared, and drafts the agreement with the other side. A and B are litigation roles. D: verbatim notes "as documentary evidence" defeat the confidentiality of the process (MA ss 9–10).
*Cite: MED-5 p4–5 (see `drp-m-1-52`)*

**Q2023-51** · `1.VIII.1` · PYP 2023 Q51 · `drp-m-1-52`

When representing the client during mediation, which of the following actions would be appropriate for counsel?

I. Assist the client in his/her opening statement, by adding in any important point the client may have missed out, at the end of the client's presentation.
II. Help explain to the other party and the mediator, the client's true interests and concerns.
III. Ask questions to 'test' and clarify the interests and concerns raised by the other party.
IV. Assist in the mediation process by helping to generate options and possible solutions, bearing in mind the goals, strategies and bottom lines of the client.

A. I, II and IV only
B. I, III and IV only
C. I, II and III only
D. I, II, III and IV

**Answer: D.** All four fit the advocate's role: supporting the client in presenting its account (I), assisting the mediator to understand the dispute (II), testing and clarifying the other side's interests (III) and helping generate options within the client's goals and bottom line (IV).
*Cite: MED-5 p4–5 (see `drp-m-1-52`)*

**Q2023-59** · `1.VIII.1` `1.VIII.2` · PYP 2023 Q59 · `drp-m-1-52` `drp-m-1-53`

During the mediation, the mediation advocate must:

I. approach the mediation like any other litigation matter, in an adversarial but professional manner.
II. assist the mediator in understanding the dispute.
III. ensure that any decision made by the client is a well-considered and an informed decision.
IV. ensure that the terms of settlement are in the client's best interests, and reflect the client's intentions.

A. II, III and IV only
B. I, II and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: A.** II, III and IV are on the MED-5 list. I is wrong: the approach is less adversarial or non-adversarial, focused on collaborative problem-solving, though no less zealous for the client.
*Cite: MED-5 p4–5 (see `drp-m-1-52`, `drp-m-1-53`)*

**Q2021M-1-9e** · `1.VIII.1` · PYP 2021 MED Q1.9(e) · `drp-m-1-52`

[Facts: Q2021M-1-9a.] If Mdm Ong had engaged you to represent her at the mediation, what would your role be in each stage? (6 marks)

**Answer.** *Before:* prepare her (the process, her interests and Mr Tan's, BATNA/WATNA, options, settlement range, her authority, the case statement and opening). *Opening:* support her in giving her own account, adding any key point she misses at the end; set a constructive tone. *Exploration (joint):* help the mediator understand the dispute (the serial-number evidence; the timing need for home-based learning); ask questions to clarify Mr Tan's concerns; manage her emotions. *Private sessions:* give candid advice, reality-test her expectations against her alternatives, and decide with her what may be disclosed (confidentiality, PCR r 6). *Negotiation:* help generate and evaluate options (refund, replacement genuine laptops, apology) against objective criteria; keep it constructive; act only within her authority. *Closure:* ensure the decision is informed and hers, and draft a clear settlement (payment date, return of laptops, default terms, confidentiality); follow up on performance.
*Cite: MED-5 p4–5 (see `drp-m-1-52`); PCR r 6*

### 1.VIII.2 — Approach: zealous but non-adversarial

**QSQ-M1** · `1.VIII.2` · Sample Questions (Part B 2023-S) Mediation Q1 · `drp-m-1-53`

Which of the following statements about the role of the mediation advocate is NOT TRUE?

A. The mediation advocate should help the client to assess whether or not their case is suitable for mediation.
B. The mediation advocate should advise the client to consider mediation, whenever it is appropriate.
C. The mediation advocate should preserve the client's rights, by remaining steadfast on the merits of their case.
D. The mediation advocate should assist in the drafting of any settlement agreement, together with the opposing counsel.

**Answer: C.** Remaining steadfast on the merits is a litigation stance; in mediation the advocate protects the client's interests by collaborative problem-solving. A, B and D are part of the role. Official key: C.
*Cite: MED-5 (see `drp-m-1-53`); SampleQs p60 Q1, key p122*

**QSQ-M4** · `1.VIII.2` · Sample Questions (Part B 2023-S) Mediation Q4 · `drp-m-1-53`

Mediation advocacy is about the advocate…

I. refraining from interrupting the mediator, the other party and counsel, when they are speaking during the mediation.
II. exploring the respective concerns of the parties, rather than focussing on the client's legal positions.
III. avoiding being antagonistic towards the mediator, the opposing party and counsel during the mediation.
IV. protecting the client's rights, remaining resolute on the merits of the client's case, and winning the legal argument.

Which of the above statements are CORRECT?

A. I and II.
B. III and IV.
C. I, II and III.
D. I, III and IV.

**Answer: C.** I, II and III describe non-adversarial advocacy; IV describes litigation. Official key: C.
*Cite: MED-5 (see `drp-m-1-53`); SampleQs p61 Q4, key p122*

**Q2023-52** · `1.VIII.2` · PYP 2023 Q52 · `drp-m-1-53`

Mediation advocacy is about the advocate...

I. not being antagonistic towards the mediator, the opposing party and counsel.
II. being persistent and steadfast - emphasising the strength and merits of the client's case throughout the mediation.
III. not constantly rebutting the other party's points and aggravating the mutual hostilities between the parties.
IV. focusing on the client's legal positions, and avoiding the broader conversation between the parties about their respective concerns.

Which of the above statements are CORRECT?

A. I and II only
B. I and III only
C. II and IV only
D. I, II and III only

**Answer: B.** I and III describe the constructive approach. II and IV are the adversarial stance of litigation (compare QSQ-M4).
*Cite: MED-5 (see `drp-m-1-53`)*

### 1.VIII.3 — Competence in advising (PCR r 5)

See Q2023-57 under 1.VIII.9 (statements II and III).

### 1.VIII.4 — Confidentiality (PCR r 6)

See Q2023-56 under 1.VIII.9 (statement I).

### 1.VIII.5 — Party autonomy and the advocate's authority

**Q2023-58** · `1.VIII.5` `1.VIII.8` · PYP 2023 Q58 · `drp-m-1-56` `drp-m-1-59`

The mediation advocate must:

I. respect the client's decision, even if it is not in accordance with the lawyer's opinion or advice. The decision to settle and the terms of settlement ultimately lie with the client.
II. advocate as persuasively and as fearlessly as possible. One can both disagree and be disagreeable.
III. endeavour to keep the negotiation constructive and collaborative with a view to resolving the dispute in a manner that is mutually acceptable to the parties.
IV. not enter into any agreement on behalf of the client when he or she does not have any mandate or authorisation to do so.

A. I, II and III only
B. I, III and IV only
C. II, III and IV only
D. I, II, III and IV

**Answer: B.** I and IV are party autonomy and authority; III is the honest, constructive approach. II's second sentence is the trap: one may disagree, but must not be disagreeable (courtesy, PCR rr 8, 8A(2)).
*Cite: MED-5 (see `drp-m-1-56`, `drp-m-1-59`); PCR r 8A(2)*

### 1.VIII.6 — Conflicts of interest (PCR r 22); acting after being the mediator

See Q2023-56 under 1.VIII.9 (statement IV) and Q2021M-1-6 under 1.VIII.10 (the partner's bonus).

### 1.VIII.7 — Conduct in ADR: respect, courtesy, good faith, not misleading (PCR r 8A)

**Q2021M-1-7** · `1.VIII.7` · PYP 2021 MED Q1.7 · `drp-m-1-58`

You act for a personal injury claimant; mediation is in a week. Over golf he tells you he will attend in a wheelchair, crutches and a neck brace to falsely substantiate a higher claim, because he needs money to rescue his business, and that your duty to act in his best interests means you must help him present this case to secure the highest possible settlement. What would you advise? (4 marks)

**Answer.** Advise him firmly that he must not do it and that you cannot assist. In any ADR process a lawyer must act in good faith, must not knowingly mislead or attempt to mislead the mediator, and must not knowingly assist or permit the client to mislead (PCR r 8A(3)–(5)); the lawyer must also be honest towards the other party and not act deceitfully (r 8(3)). The duty to advance the client's interests extends only to *legal* means (r 5(2)(j)), not deception. Explain the consequences: a settlement induced by misrepresentation is voidable and can be set aside (*Tiong Swee Eng* [2015] SGHC 116 at [19]–[21]); a mediation communication made "in furtherance of any illegal purpose" loses its confidentiality (MA s 9(2)(j)); he risks criminal liability for cheating. If he insists, you must decline to act further (and withdraw), without disclosing his confidence beyond what the rules allow.
*Cite: PCR rr 5(2)(j), 8(3), 8A(3)–(5); MA s 9(2)(j); [2015] SGHC 116 at [19]–[21]*

### 1.VIII.8 — Honesty in negotiation: no underhanded tactics

**QSQ-M10** · `1.VIII.8` `1.VIII.2` · Sample Questions (Part B 2024) Mediation Q10 · `drp-m-1-59` `drp-m-1-53`

Which of the following statements about the role of the mediation advocate during a mediation is untrue?

A. The mediation advocate should be constructive, and be focused on collaborative problem-solving.
B. The mediation advocate must uphold the client's interest no less robustly than in litigation.
C. The approach taken by the mediation advocate should be less contentious or non-adversarial.
D. The mediation advocate may resort to sharp negotiation tactics to advance the client's interests.

**Answer: D.** Any strategy serving the client is permitted, but not underhanded or misleading tactics (PCR r 8(3)). A, B and C are true: zealous but non-adversarial. Official key: D.
*Cite: MED-5 (see `drp-m-1-59`); PCR r 8(3); SampleQs p63 Q10, key p122*

**Q2021M-1-8** · `1.VIII.8` · PYP 2021 MED Q1.8 · `drp-m-1-59`

Brigitte Chan acts for Mary Khan, who sues Allen Wong for misappropriating money Mary asked him to invest. At court-referred mediation Allen appears unrepresented, saying he is ill and cannot afford a solicitor. Mary thinks he is acting for sympathy; Brigitte sees he looks pale, gaunt and tired, and feels sorry for him. How should Brigitte conduct herself towards Allen? (4 marks)

**Answer.** Brigitte acts only for Mary and must keep advancing Mary's interests, but must treat Allen honestly and courteously and must not take unfair advantage of him (PCR r 8(1), (3); r 8A(2)–(3) in ADR). With an unrepresented party she must give him no legal advice other than to obtain independent legal advice, and must ensure he does not mistake her for someone protecting his interests (r 8(2)). She should not exploit his illness or lack of a lawyer, make no misleading statements about the law or the facts, and be patient with process explanations best left to the mediator. Sympathy must not compromise her duty to Mary: if Allen's health or finances are genuine, they bear on Mary's interests (recoverability, a realistic instalment plan, security), and Brigitte can explore them through the mediator. Any agreement should be clear, and she might suggest he take advice before signing, which also protects the settlement against later challenge.
*Cite: PCR rr 8(1)–(3), 8A(2)–(3) (see `drp-m-1-59`)*

### 1.VIII.9 — Duties to the client; advising on ADR (PCR rr 5(2), 17(2))

**Q2023-56** · `1.VIII.9` `1.VIII.4` `1.VIII.6` · PYP 2023 Q56 · `drp-m-1-60` `drp-m-1-55` `drp-m-1-57`

Under the Legal Profession (Professional Conduct Rules) 2015, a lawyer must:

I. maintain the confidentiality of any information acquired by the lawyer in the course of his or her engagement.
II. act with reasonable diligence and competence in the provision of services to the client.
III. use all means to advance the client's interests, to the extent that the lawyer is reasonably expected to do so.
IV. not place himself or herself in a position of conflict between the duty to serve the best interests of the client and the interests of the lawyer, or his or her law practice.

Which of the above statements are CORRECT?

A. I, II and III only
B. II, III and IV only
C. I, III and IV only
D. I, II, III and IV

**Answer: D.** I: confidentiality (r 6). II: diligence and competence (r 5(2)). IV: avoid conflicts between the client's interests and one's own or the practice's (r 22). III paraphrases r 5(2)(j), which says "all *legal* means"; every option includes III, so the examiners treated it as correct, and the answer turns on I, II and IV, all true.
*Cite: PCR rr 5(2), 5(2)(j), 6, 22 (see `drp-m-1-60`)*

**Q2023-57** · `1.VIII.9` `1.VIII.3` · PYP 2023 Q57 · `drp-m-1-60` `drp-m-1-54`

Under the Legal Profession (Professional Conduct Rules) 2015, a lawyer must:

I. explain clearly and properly to the client a proposal of settlement, or any other offer or position taken by any other party, which affects the client.
II. when advising the client, only inform the client of such information that the client is reasonably prepared or willing to accept.
III. ensure that he or she has the relevant knowledge, skills and attributes required for each matter undertaken, and apply the knowledge, skills and attributes in a manner appropriate to that matter.
IV. conduct a cost-benefit or risk-benefit analysis with the client, and evaluate the use of alternative dispute resolution processes.

Which of the above statements are CORRECT?

A. II, III and IV only
B. I, II and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: C.** I: r 17(2)(c)–(d) (explain proposals and offers clearly). III: r 5(2)(d) (knowledge, skills, attributes). IV: r 17(2)(e) (evaluate whether pursuing the matter justifies the expense and risk, and evaluate ADR). II is wrong: the lawyer must inform the client of all information known that may reasonably affect its interests, subject to confidentiality (r 5(2)(b)), not only what the client wants to hear.
*Cite: PCR rr 5(2)(b), (d), 17(2)(c)–(e) (see `drp-m-1-54`, `drp-m-1-60`)*

### 1.VIII.10 — Family proceedings (PCR r 15A)

**Q2023-60** · `1.VIII.10` · PYP 2023 Q60 · `drp-m-1-61`

Under rule 15A of the Legal Profession (Professional Conduct Rules) 2015, a lawyer must:

I. inform the client of all available dispute resolution options, including mediation, so as to enable client to make an informed decision on how to resolve family proceedings.
II. advise the client to consider resolving family proceedings amicably, only from the time family proceedings are commenced in court.
III. advise the client to be constructive and reasonable when participating in family proceedings.
IV. advise the client that when the court makes any decision affecting a child, the welfare and bests interests of the child will take precedence over the wishes of either parent of the child, and the wishes of the child.

Which of the above statements are CORRECT?

A. I, III and IV only
B. I, II, III and IV
C. II, III and IV only
D. I, II and III only

**Answer: A.** I, III and IV track r 15A(2)(a), (2)(c) and (3). II is wrong: the duty runs from the time proceedings are *contemplated*, not only once commenced (r 15A(2)(b)).
*Cite: PCR r 15A(2)–(3)*

**Q2021M-1-6** · `1.VIII.10` `1.VIII.6` `1.IV.7` · PYP 2021 MED Q1.6 · `drp-m-1-61` `drp-m-1-57` `drp-m-1-25`

You are in the team acting for a husband in divorce proceedings in the Family Justice Courts; there are two children, 9 and 14. The wife's counsel proposes mediation at SMC with SMC appointing the mediator. Your senior partner tells you to advise the client to ignore the proposal and push for a court hearing, "or the firm will not have money to pay for your year-end bonus". What ethical considerations arise? (4 marks)

**Answer.** (1) *Duty to advise on ADR in family proceedings:* the lawyer must inform the client of all reasonably available dispute resolution options, including mediation, advise him to consider amicable resolution and to be constructive and reasonable (PCR r 15A(2)); it is the solicitor's professional duty to advise on mediation, which should be considered at the earliest stage (FJCPD 81(2)). (2) *Children:* the client must be advised that the children's welfare and best interests take precedence (r 15A(3)); both children are "children" (under 21), and mediation usually serves them better than adversarial litigation. (3) *Conflict of interest:* the partner's instruction puts the firm's fees and your bonus ahead of the client's interests, a conflict the lawyer must avoid (r 22(2)); advice must be given in the client's best interests (r 5). (4) *Duty to convey offers:* the wife's proposal must be explained to the client clearly (r 17(2)(c)–(d)); the decision is his. So you should not follow the instruction: raise it with the partner, and if pressed, escalate within the firm. The client should receive objective advice on the mediation proposal.
*Cite: PCR rr 5, 15A(2)–(3), 17(2)(c)–(d), 22(2); FJCPD 81(2)*

### 1.VIII.11 — Preparing the client for mediation

**Q2023-38** · `1.VIII.11` · PYP 2023 Q38 · `drp-m-1-62`

When counsel is preparing a client for mediation, which one of the following statements is UNTRUE?

A. Counsel should explain the mediation process to the client.
B. Counsel should discuss the possible outcomes.
C. Counsel should consider options which meets the client's interests only.
D. Counsel should identify the client's settlement range.

**Answer: C.** Options must be weighed against both sides' interests; an option meeting only the client's interests will not be accepted. A, B and D are part of preparation.
*Cite: MED-4, MED-5 (see `drp-m-1-62`)*

**Q2021M-1-9c** · `1.VIII.11` · PYP 2021 MED Q1.9(c) · `drp-m-1-62`

[Facts: Q2021M-1-9a.] Mr Lee asked both parties for mediation case statements. What information and/or documents would you advise Mdm Ong to include? (3 marks)

**Answer.** A short, non-inflammatory statement with: the parties and their relationship; the background facts (purchase date, price $5,000, the faults within a day, the distributor's reply on the serial numbers, Mr Tan's refusal); the issues; what she needs and why (working, genuine laptops before home-based learning starts in a month; a refund); her proposal for settlement and openness to options; and the key documents: the receipt or invoice, the distributor's email, records of the faults (photos, repair reports), and her correspondence with Mr Tan. Mark it confidential and for the purpose of the mediation.
*Cite: MED-5 (see `drp-m-1-62`); StCPD 42(2)–(4) (court mediation equivalent)*

**Q2021M-1-9d** · `1.VIII.11` `1.VIII.1` · PYP 2021 MED Q1.9(d) · `drp-m-1-62` `drp-m-1-52`

[Facts: Q2021M-1-9a.] Mdm Ong has never attended a mediation. Explain the different stages of a typical mediation and what happens in each. (6 marks)

**Answer.** The 2026 Course Materials do not set out the stages; this is the usual sequence of a facilitative mediation. (1) *Mediator's opening:* introductions, the mediator's role (neutral, not a judge), confidentiality, ground rules and the process. (2) *Parties' opening statements:* each side, then its lawyer, gives its account and concerns without interruption. (3) *Joint exploration:* the mediator summarises, identifies issues and interests, and encourages the parties to talk to each other. (4) *Private sessions (caucuses):* the mediator meets each side separately to explore interests, test alternatives and options in confidence; what is said stays private unless the party agrees. (5) *Negotiation and option generation:* jointly or by shuttle, the parties generate and evaluate options against objective criteria. (6) *Closure:* a written settlement agreement, signed by both, or a partial settlement or narrowed issues; if there is no settlement, the next steps.
*Cite: MED-1 (see `drp-m-1-2`); MED-5 (see `drp-m-1-52`, `drp-m-1-62`)*

**Q2021M-1-9f** · `1.VIII.11` `1.VIII.5` · PYP 2021 MED Q1.9(f) · `drp-m-1-62` `drp-m-1-56`

[Facts: Q2021M-1-9a.] Her teenage sons are livid that Mr Tan cheated their mother and want to confront him at the mediation. Whom would you recommend as appropriate attendees? Explain. (3 marks)

**Answer.** Mdm Ong herself, as the party with full authority to settle; her lawyer, if she engages one, to advise and support her; and Mr Tan with any adviser. The sons should not attend as participants: they are not parties, they want confrontation rather than resolution, and their anger would inflame emotions and harden positions. Their interest (working laptops for school) can be conveyed by Mdm Ong. If she needs emotional support, one calm support person may attend with the mediator's and the other side's agreement, bound by confidentiality.
*Cite: MED-5 (see `drp-m-1-56`, `drp-m-1-62`)*

**Q2021M-2-2** · `1.VIII.11` · PYP 2021 MED Q2.2 · `drp-m-1-62`

[PYP 2021 MED Q2 facts: see under 1.VII.1.] Draft the requisite Opening Statement (Form 9J, Appendix A, State Courts Practice Directions) for Japanese Booth. (10 marks)

**Answer (outline).** *What changed:* the 2021 form was Form 9J of the State Courts Practice Directions 2014. Under the State Courts Practice Directions 2021, each party submits to the Court Dispute Resolution Cluster, and serves, a written opening statement not less than 2 working days before the first mediation hearing, in Form 8 of Appendix A1, concise and not more than 10 pages (StCPD 42(2)–(4)); all parties attend in person (42(5)).

*Content (conciliatory, interest-based, no new allegations):* (1) parties and counsel; Mayu's authority to settle; (2) a short, neutral background: the founding of Japanese Booth, Marcus's role and trust placed in him, his resignation, the opening of Nippon Pot, the similarities, the slogan and the WhatsApp messages; (3) the issues: get-up and menu, recipes, staff, the slogan, losses and costs; (4) Mayu's key concerns and interests: fair competition and differentiation, protecting her mother's recipes and her brand, keeping her staff, withdrawal of the slogan, recognition of the hurt, costs, and getting back to running her business; (5) acknowledgment of the other side's position (its own pandemic difficulties; that some dishes are generic) and that much of her loss came from the pandemic; (6) what she hopes to achieve: a practical settlement including differentiation, removal of the slogan, non-solicitation, an apology, and a contribution to costs; (7) her willingness to listen and be reasonable and fair. Tone: firm on the core interests, respectful of Marcus, no inflammatory language.
*Cite: StCPD 42(2)–(5); MED-5 (see `drp-m-1-62`)*

## 0 · Arbitration — Drills

Part 3. One drill for each of the 105 Arbitration Sub-points no past paper has tested, plus 0.XVIII.15 and 0.XIX.8, which past papers raised only in passing, in `coverage.md` order (drills 1–107). Written 11 Nov 2026 from `cheatsheets.md`, checked against the primary texts where a drill goes beyond a block. Self-study only.

### 0.I Applicable laws and the IAA framework — drills

Drills 1–5 cover 0.I.4, 0.I.7, 0.I.9, 0.I.10 and 0.I.12.

### 0.I.4 — "Commercial" is read widely

**Qdrill-1** · `0.I.4` · drill-1 · `drp-m-0-4`

A Singapore bank and a Thai developer fall out over a loan facility and a related joint venture for a hotel. The developer argues that the Model Law cannot apply because a financing relationship is not "commercial" and part of the claim lies in tort, not contract. Which statement is CORRECT?

A. "Commercial" is limited to contracts for the sale of goods, so the Model Law does not apply.
B. The Model Law applies only to contractual claims, so the tort claim falls outside it.
C. "Commercial" is read widely to cover all relationships of a commercial nature, contractual or not, including banking, financing and joint ventures.
D. Whether a relationship is "commercial" is decided by the law of the debtor's place of incorporation.

**Answer: C.** The Model Law applies to international commercial arbitration (Art 1(1)), and the footnote reads "commercial" widely: relationships of a commercial nature, contractual or not, such as supply of goods or services, construction, banking, financing, carriage, joint ventures and investment. A: the examples go well beyond sale of goods. B: the relationship need not be contractual. D: there is no such choice-of-law test; the meaning comes from Art 1(1) and its footnote.
*Cite: Model Law Art 1(1) and footnote*

### 0.I.7 — Which version of the arbitration rules applies

**Qdrill-2** · `0.I.7` · drill-2 · `drp-m-0-7`

A contract signed in 2019 refers disputes to arbitration under the SIAC Rules. The claimant files its Notice of Arbitration in March 2025. The parties made no agreement on which edition of the rules applies. Which rules govern, and why?

A. The SIAC Rules 2025, because there is a presumption that the rules in force when the arbitration is commenced apply, and r 1.5 applies the 2025 Rules to arbitrations commenced on or after 1 Jan 2025 unless otherwise agreed.
B. The SIAC Rules 2016, because the rules in force at the date of the contract always apply.
C. The SIAC Rules 2016, because a party cannot be bound by rules it never saw when contracting.
D. Whichever edition the tribunal considers fairer, applying Art 28(2) of the Model Law.

**Answer: A.** *Black & Veatch v Jurong Engineering* sets a presumption that the rules in force at commencement apply, not those at the date of contract, and SIAC25 r 1.5 says the same for arbitrations commenced on or after 1 Jan 2025 unless otherwise agreed. B: reverses the presumption. C: the parties agreed to institutional rules, which can change; that is not a bar. D: Art 28 concerns the law governing the substance, not the procedural rules.
*Cite: Black & Veatch Singapore v Jurong Engineering [2004] SGCA 30 at [19]–[20]; SIAC25 r 1.5*

### 0.I.9 — New York Convention and Singapore's reciprocity reservation

**Qdrill-3** · `0.I.9` · drill-3 · `drp-m-0-9`

Which of the following statements about the New York Convention (NYC) in Singapore is TRUE?

A. Foreign awards are enforced in Singapore under Chapter VIII of the Model Law (Arts 35–36).
B. Singapore applies the NYC to an award made in any State, whether or not that State is a Contracting State.
C. The NYC governs the conduct of arbitrations seated in Singapore.
D. Singapore made the reciprocity reservation, so it applies the NYC only to awards made in another Contracting State; this is a reason to choose a seat in a NYC State.

**Answer: D.** Singapore made the reciprocity reservation under NYC Art I(3), applying the Convention only to awards made in another Contracting State. The NYC is part of Singapore law through IAA Part 3, which defines "foreign award" by reference to a "Convention country". A: Chapter VIII of the Model Law is excluded from the force of law in Singapore so that foreign awards go through the NYC alone. B: ignores the reservation. C: the NYC deals with recognition and enforcement of foreign awards, not the conduct of a Singapore-seated arbitration.
*Cite: NYC Art I(3); IAA s 27(1) ("foreign award", "Convention country")*

### 0.I.10 — Law governing the substance of the dispute (Art 28; SIAC r 35.1)

**Qdrill-4** · `0.I.10` · drill-4 · `drp-m-0-10`

Consider these statements about the law governing the substance of a dispute:

I. The parties may choose a law with no connection to them or the dispute.
II. Absent a choice, the Model Law lets the tribunal apply directly whatever law it considers appropriate.
III. Absent a choice, SIAC25 r 35.1 lets the tribunal apply the law or rules of law it determines to be appropriate.
IV. A tribunal may decide ex aequo et bono whenever it thinks that would be fair.

Which are CORRECT?

A. I and II only
B. I and III only
C. II and IV only
D. I, III and IV only

**Answer: B.** I is correct: parties may choose any law, with no connection needed (Art 28(1); *Quarella*). III is correct: r 35.1 is the voie directe. II is wrong: Art 28(2) requires the tribunal to apply the law found by the conflict of laws rules it considers applicable (voie indirecte), not to choose a law directly. IV is wrong: deciding as amiable compositeur or ex aequo et bono needs the parties' express authority (r 35.3). So A, C and D each include a wrong statement.
*Cite: Model Law Art 28(1)–(2); Quarella SpA v Scelta Marble [2012] SGHC 166 at [34]; SIAC25 r 35.1–35.3*

### 0.I.12 — Law governing a party's capacity

**Qdrill-5** · `0.I.12` · drill-5 · `drp-m-0-12`

X Co, incorporated in State P, signs a contract with a Singapore-seated SIAC clause. After an award against it, X Co says that under the law of State P it lacked capacity to agree to arbitrate. Which is CORRECT?

A. Capacity is generally governed by X Co's personal law (its place of incorporation or business), and incapacity is a ground to set aside under Art 34(2)(a)(i) or to resist enforcement under IAA s 31(2)(a) / NYC Art V(1)(a).
B. Capacity is always governed by the law of the seat, so State P's law is irrelevant.
C. Incapacity is a public policy ground and can be raised only under Art 34(2)(b)(ii).
D. Incapacity can only be raised after the award, never before or during the arbitration.

**Answer: A.** A party's capacity is generally governed by its personal law (nationality for individuals, place of incorporation or business for companies), or alternatively by the law of the contract. Incapacity is a ground to set aside (Art 34(2)(a)(i)) and to refuse enforcement (IAA s 31(2)(a); NYC Art V(1)(a)). B: the seat's law is not the general rule for capacity. C: incapacity has its own ground under Art 34(2)(a)(i). D: it can be raised before or during the arbitration as well.
*Cite: Model Law Art 34(2)(a)(i); IAA s 31(2)(a); NYC Art V(1)(a)*

### 0.II Domestic arbitration under the Arbitration Act 2001 — drills

Drills 6–7 cover 0.II.2 and 0.II.3.

### 0.II.2 — Stay under the AA is discretionary (s 6(2) AA; CSY v CSZ)

**Qdrill-6** · `0.II.2` · drill-6 · `drp-m-0-14`

A and B, both Singapore companies, agreed to arbitrate in Singapore; the IAA does not apply. A sues B and C in the High Court on overlapping facts; only A and B are bound by the clause. B applies for a stay. Which is CORRECT?

A. The court must stay the claim against B, because a stay is mandatory unless the agreement is null and void, inoperative or incapable of being performed.
B. The court must stay the whole action, including the claim against C.
C. The court has no power to stay because the dispute is domestic.
D. The court may stay if satisfied there is no sufficient reason not to refer the matter to arbitration and B was and remains ready and willing to arbitrate; related claims against non-parties and a risk of inconsistent findings are relevant factors.

**Answer: D.** Under AA s 6(2) the court *may* stay; the *CSY v CSZ* factors for "sufficient reason" include related actions not all governed by the clause, overlap of issues and the risk of inconsistent findings. Those factors must outweigh the strong consideration that the parties chose to arbitrate. A: that is the mandatory IAA test under IAA s 6(2), not the AA. B: there is no mandatory stay and C is not a party to the clause. C: AA s 6 gives the court a power to stay.
*Cite: AA s 6(2); CSY v CSZ [2022] SGCA 43 at [23]–[26]; Sim Chay Koon v NTUC Income [2015] SGCA 46 at [7], [9]–[10]*

### 0.II.3 — Court determination of a preliminary point of law (s 45 AA)

**Qdrill-7** · `0.II.3` · drill-7 · `drp-m-0-15`

In a domestic arbitration governed by the Arbitration Act 2001, the claimant wants the court to decide mid-arbitration whether an exclusion clause is valid. The respondent refuses to agree. The parties have not excluded the court's power. Which is CORRECT?

A. The claimant cannot apply without the respondent's agreement in every case.
B. The same application is available in an IAA arbitration.
C. The claimant may apply with the tribunal's permission, if the court is satisfied that determining the question is likely to produce substantial savings in costs and the application is made without delay; the tribunal may continue meanwhile.
D. Once the application is made, the arbitration is automatically stayed until the court decides.

**Answer: C.** AA s 45(1) lets the court determine a question of law that substantially affects a party's rights, unless otherwise agreed. Under s 45(2) the application needs all parties' agreement, or the tribunal's permission plus the court being satisfied on substantial costs savings and no delay. Under s 45(4) the tribunal may continue and make an award meanwhile. A: the tribunal-permission route is the alternative. B: the IAA has no equivalent. D: contradicts s 45(4).
*Cite: AA s 45(1), (2), (4)*

### 0.III Soft law instruments and arbitral institutions — drills

Drills 8–13 cover 0.III.1, 0.III.2, 0.III.3, 0.III.4, 0.III.5 and 0.III.6.

### 0.III.1 — Soft law binds only if adopted or applied

**Qdrill-8** · `0.III.1` · drill-8 · `drp-m-0-18`

In a SIAC arbitration, the arbitration agreement says nothing about evidence rules. The respondent argues that the IBA Rules on the Taking of Evidence automatically bind the tribunal because they reflect international practice. Which is CORRECT?

A. The IBA Rules bind every tribunal seated in Singapore by virtue of the IAA.
B. The IBA Rules apply only if the parties agree to adopt them (often in Procedural Order No 1) or the tribunal decides to apply them under its procedural discretion, and they yield to mandatory law.
C. The IBA Rules, once adopted, override mandatory provisions of the lex arbitri.
D. Soft law instruments cannot be referred to at all unless incorporated in the arbitration agreement.

**Answer: B.** Soft law is not law and binds only if the parties adopt it or the tribunal applies it. The IBA Rules apply where the parties agree or the tribunal determines to apply them (Art 1.1). Each instrument yields to mandatory law. A: no statute makes them binding. C: they give way to mandatory law. D: they are widely referred to as guidance by parties, arbitrators and courts even when not adopted.
*Cite: IBA Rules on Evidence Art 1.1; CIArb Protocol Art 2.2; Prague Rules Art 1.3*

### 0.III.2 — IBA Rules on the Taking of Evidence (2020)

**Qdrill-9** · `0.III.2` · drill-9 · `drp-m-0-19`

The IBA Rules on the Taking of Evidence (2020) apply. Which of the following is NOT TRUE?

A. A Request to Produce may describe a narrow and specific category of documents reasonably believed to exist.
B. The tribunal may exclude a document on the ground of compelling commercial or technical confidentiality.
C. It is improper for a party's counsel to interview a potential witness before the witness gives evidence.
D. If a party fails without satisfactory explanation to produce a document it was ordered to produce, the tribunal may infer that the document is adverse to that party.

**Answer: C.** Art 4.3 states that it is not improper for a party, its officers, employees, legal advisors or other representatives to interview its witnesses or potential witnesses. A is true: Art 3.3(a). B is true: Art 9.2(e). D is true: adverse inference under Art 9.6.
*Cite: IBA Rules on Evidence Arts 3.3(a), 4.3, 9.2(e), 9.6*

### 0.III.3 — IBA Guidelines on Conflicts of Interest (2024): structure

**Qdrill-10** · `0.III.3` · drill-10 · `drp-m-0-20`

Which statement about the structure of the IBA Guidelines on Conflicts of Interest (2024) is CORRECT?

A. Situations on the Orange List cannot be waived even if both parties expressly agree.
B. An arbitrator must disclose every situation on the Green List.
C. A failure to disclose a fact automatically makes the arbitrator partial.
D. Situations on the Waivable Red List are cured only if the parties, aware of the conflict, expressly agree; Non-Waivable Red List situations cannot be cured by acceptance.

**Answer: D.** The Non-Waivable Red List reflects the principle that no one may be their own judge, so acceptance cannot cure it; the Waivable Red List is cured only by express agreement with knowledge. A: Orange List situations must be disclosed, and the parties are deemed to accept if they make no timely objection. B: the Green List carries no duty to disclose. C: non-disclosure alone does not make an arbitrator partial; only the facts not disclosed can. The lists are non-exhaustive.
*Cite: IBA Guidelines on Conflicts of Interest 2024, Part II paras 2–7*

### 0.III.4 — IBA Guidelines on Party Representation (2013)

**Qdrill-11** · `0.III.4` · drill-11 · `drp-m-0-21`

A tribunal applying the IBA Guidelines on Party Representation finds, after notice and a hearing, that the claimant's counsel knowingly made false submissions of fact. Consider:

I. The tribunal may admonish counsel.
II. The tribunal may draw appropriate inferences in assessing the evidence.
III. The tribunal may reflect the misconduct in its costs decision.
IV. The Guidelines override counsel's professional and disciplinary rules.

Which are CORRECT?

A. I and II only
B. I, II and IV only
C. III and IV only
D. I, II and III only

**Answer: D.** Guideline 26 allows the tribunal to admonish the representative, draw appropriate inferences, consider the misconduct in allocating costs, and take any other measure to preserve fairness and integrity. IV is wrong: the Guidelines do not displace mandatory law, professional or disciplinary rules, or agreed rules (Guideline 3). A omits III; B and C include IV.
*Cite: IBA Guidelines on Party Representation, Guidelines 3, 26–27*

### 0.III.5 — CIArb Protocol on Party-Appointed Experts (2015)

**Qdrill-12** · `0.III.5` · drill-12 · `drp-m-0-22`

The CIArb Protocol on Party-Appointed Expert Witnesses applies. The respondent argues that the claimant's expert cannot be impartial because the claimant pays her fees. Which is CORRECT?

A. Payment of reasonable fees by the appointing party does not of itself vitiate the expert's impartiality; the expert's duty is to assist the tribunal, and the opinion must be impartial and objective.
B. A party-appointed expert's primary duty is to the party who pays her.
C. The expert need not disclose her instructions or the basis of her remuneration.
D. Each party decides for itself the issues its expert addresses and how many experts it calls, without any direction from the tribunal.

**Answer: A.** Art 4.1 requires an impartial and objective opinion; Art 4.2 says payment of reasonable fees does not of itself vitiate impartiality; Art 4.3 makes the duty one owed to assist the tribunal. B: contradicts Art 4.3. C: the opinion must disclose all instructions and the basis of remuneration (Art 4.4). D: the tribunal directs the issues, the number of experts and any tests (Art 3).
*Cite: CIArb Protocol Arts 3, 4.1–4.4*

### 0.III.6 — Prague Rules (2018)

**Qdrill-13** · `0.III.6` · drill-13 · `drp-m-0-23`

The parties adopt the Prague Rules. Which statement is NOT TRUE?

A. The tribunal and the parties are encouraged to avoid any form of document production, including e-discovery.
B. The tribunal may apply legal provisions not pleaded by the parties, after seeking their views.
C. Unless a party objects, the tribunal may assist the parties to reach an amicable settlement.
D. An arbitrator may act as mediator without the parties' consent, and continue as arbitrator automatically if mediation fails.

**Answer: D.** An arbitrator may act as mediator only with all parties' prior written consent, and may continue as arbitrator after a failed mediation only with written consent at that stage (Arts 9.2–9.3). A is true: Art 4.2. B is true: iura novit curia, Art 7.2. C is true: Art 9.1.
*Cite: Prague Rules Arts 4.2, 7.2, 9.1–9.3*

### 0.IV The arbitration agreement: form and parties — drills

Drills 14–20 cover 0.IV.1, 0.IV.3, 0.IV.4, 0.IV.5, 0.IV.6, 0.IV.7 and 0.IV.8.

### 0.IV.1 — Definition: clause or separate agreement

**Qdrill-14** · `0.IV.1` · drill-14 · `drp-m-0-25`

After a pipeline leak causes damage, two companies with no prior contract sign a short document agreeing to refer "the dispute concerning the leak" to arbitration. Under the IAA, which is CORRECT?

A. It is not an arbitration agreement, because an arbitration agreement must be a clause in a main contract.
B. It is not an arbitration agreement, because it covers a dispute that has already arisen.
C. It can be an arbitration agreement: it may cover disputes that have arisen or may arise in respect of a defined legal relationship, contractual or not, and may be a separate agreement.
D. It is an arbitration agreement only if the dispute is contractual.

**Answer: C.** IAA s 2A(1) defines an arbitration agreement as an agreement to submit all or certain disputes which have arisen or may arise in respect of a defined legal relationship, whether contractual or not. Under s 2A(2) it may be a clause or a separate agreement. A: a separate submission agreement is allowed. B: existing disputes are covered. D: the relationship need not be contractual; a tort claim qualifies.
*Cite: IAA s 2A(1)–(2); Model Law Art 7(1)*

### 0.IV.3 — Deemed agreement: assertion in a pleading not denied (s 2A(6))

**Qdrill-15** · `0.IV.3` · drill-15 · `drp-m-0-27`

In an IAA arbitration, the claimant's Statement of Claim asserts that R2, a non-signatory, is party to the arbitration agreement. R2 files a Statement of Defence on the merits that does not deny the assertion. Which is CORRECT?

A. R2 is not bound, because R2 never signed the agreement and the agreement must be in writing.
B. R2 is bound only if it expressly agrees in writing after the Statement of Claim.
C. R2's silence is irrelevant; only conduct before the arbitration counts.
D. There is deemed to be an effective arbitration agreement between the parties to the proceedings, because an assertion calling for a reply was not denied.

**Answer: D.** Under IAA s 2A(6), where a party asserts the existence of an arbitration agreement in a pleading, statement of case or other document in arbitral or legal proceedings, the assertion calls for a reply and it is not denied, there is deemed to be an effective arbitration agreement between the parties to those proceedings. A: the deeming provision answers the writing point. B: no further express agreement is needed. C: the conduct in the proceedings is what s 2A(6) looks at.
*Cite: IAA s 2A(6)*

### 0.IV.4 — Incorporation by reference (s 2A(7))

**Qdrill-16** · `0.IV.4` · drill-16 · `drp-m-0-28`

A purchase order states: "All other terms are as set out in the Supplier's General Conditions, which form part of this order." Clause 20 of the General Conditions is a SIAC arbitration clause. The purchase order does not mention clause 20. Which is CORRECT?

A. The arbitration clause cannot be incorporated unless the purchase order refers to it specifically.
B. Whether the clause is incorporated is a question of construction of the parties' intention; express reference to the arbitration clause is not necessary, and a reference adopting all the other document's terms can include it.
C. Incorporation by reference is not permitted under the IAA because the agreement must be signed.
D. The question is decided by the tribunal's discretion, without regard to the parties' intention.

**Answer: B.** A reference to a document containing an arbitration clause makes an arbitration agreement in writing if the reference makes the clause part of the contract (IAA s 2A(7)). The test is the parties' intention, a question of construction, and express reference to the clause itself is not necessary (*Lufthansa* at [33]–[34]). Where the reference clearly adopts all the terms of the other document, its arbitration clause is included (*Mancon*). A: states the stricter approach displaced by *Lufthansa*. C: s 2A(7) permits it. D: intention, not discretion, governs.
*Cite: IAA s 2A(7); International Research Corp v Lufthansa Systems [2013] SGCA 55 at [33]–[34]; Mancon v Heng Holdings [1999] SGHC 324 at [44]–[45]*

### 0.IV.5 — Non-signatories: implied consent, agency, assignment

**Qdrill-17** · `0.IV.5` · drill-17 · `drp-m-0-29`

Consider these possible routes for binding a non-signatory to an arbitration agreement:

I. The non-signatory negotiated and performed the contract in a way that shows an objective intention to be a party.
II. The contract was signed by the non-signatory's agent acting with apparent authority.
III. The non-signatory took an assignment of the contract.
IV. The non-signatory is a creditor of one of the parties.

Which routes may bind the non-signatory?

A. I and II only
B. II and III only
C. I, II and III only
D. I, II, III and IV

**Answer: C.** Arbitration rests on consent, but implied consent through negotiation or performance (I), agency with actual, apparent or ratified authority (II), and assignment (III) can each bind a non-signatory, applying the law of the arbitration agreement. IV is not a recognised route: being a creditor of a party does not show consent to the clause. A and B each omit a valid route; D wrongly adds IV.
*Cite: ARB-SN p15–16 para 49*

### 0.IV.6 — Non-signatories: group of companies and estoppel

**Qdrill-18** · `0.IV.6` · drill-18 · `drp-m-0-30`

The claimant in a Singapore-seated arbitration wants to add the respondent's parent company, a non-signatory, on the basis that the two companies form one economic group. Which is CORRECT?

A. The group of companies doctrine has been doubted as applying under Singapore law, and estoppel against a non-signatory has been applied only very narrowly.
B. The Court of Appeal has adopted the group of companies doctrine, so the parent is bound.
C. Singapore has adopted the wide US doctrine of equitable estoppel, which binds the parent.
D. A parent company is always bound by its subsidiary's arbitration agreement.

**Answer: A.** The High Court doubted that the group of companies doctrine (from the ICC *Dow Chemical* award) applies under Singapore law (*Manuchar Steel*). Estoppel was applied only to stop A insisting that B start a separate arbitration where B was a party on the agreement's proper construction (*Jiang Haiying* at [26]–[28]); the wider US equitable estoppel approach has not been adopted. B: no such Court of Appeal adoption. C: not adopted. D: corporate separateness and consent prevent any automatic rule.
*Cite: Manuchar Steel Hong Kong v Star Pacific Line [2014] SGHC 181; Jiang Haiying v Tan Lim Hui [2009] SGHC 42 at [26]–[28]*

### 0.IV.7 — Joinder of additional parties (SIAC r 18)

**Qdrill-19** · `0.IV.7` · drill-19 · `drp-m-0-31`

In a SIAC arbitration commenced in 2026, before the tribunal is constituted, X (not yet a party) applies to be joined. The respondent objects. Under SIAC25 r 18.1, which is CORRECT?

A. Only an existing party, never a non-party, may apply for joinder.
B. Joinder requires X to prove on a balance of probabilities that it is bound by the arbitration agreement.
C. The Model Law provides the joinder procedure, so the SIAC Rules are irrelevant.
D. X may be joined if all parties, including X, agree, or if X is prima facie bound by the arbitration agreement.

**Answer: D.** SIAC25 r 18.1 allows a party or a non-party to apply, at filing of the Notice or Response or before constitution, where (a) all parties including the additional party agree, or (b) the additional party is prima facie bound by the arbitration agreement. So the respondent's objection is not fatal under limb (b). A: non-parties may apply. B: the standard is prima facie. C: the Model Law and NYC are silent on joinder; institutional rules govern it.
*Cite: SIAC25 r 18.1*

### 0.IV.8 — Consolidation and coordinated proceedings (SIAC rr 15–17)

**Qdrill-20** · `0.IV.8` · drill-20 · `drp-m-0-32`

A supplier has a main supply contract and a separate guarantee with compatible SIAC clauses, and starts two SIAC arbitrations against the same buyer. No tribunal is yet constituted and the buyer does not agree to consolidation. Which is CORRECT?

A. Consolidation is impossible without all parties' agreement.
B. The arbitrations may be consolidated because the agreements are compatible and the disputes arise out of a principal contract and its ancillary contract.
C. Coordinated proceedings under r 17 merge the arbitrations into one with a single award.
D. Consolidation is governed by Model Law Art 10.

**Answer: B.** Under SIAC25 r 16.1, before any tribunal is constituted, arbitrations may be consolidated where (a) all parties agree, (b) all claims are under the same arbitration agreement, or (c) the agreements are compatible and the disputes arise out of the same legal relationship, a principal contract and its ancillary contract, or the same transaction or series. Limb (c)(ii) fits. A: agreement is only limb (a). C: coordinated arbitrations stay separate, with separate awards (r 17). D: the Model Law is silent on consolidation; Art 10 concerns the number of arbitrators.
*Cite: SIAC25 rr 15.1, 16.1, 17*

### 0.V Arbitrability — drills

Drills 21–22 cover 0.V.2 and 0.V.5.

### 0.V.2 — Scope of the clause: construed widely (Larsen; Premium Nafta)

**Qdrill-21** · `0.V.2` · drill-21 · `drp-m-0-34`

A clause refers "any dispute arising out of this Agreement" to arbitration. The claimant brings claims in contract and in tort for misrepresentation inducing the Agreement, and argues the tort claim must go to court. Which is CORRECT?

A. Tort claims are never within an arbitration clause unless expressly mentioned.
B. Only claims for breach of the Agreement's express terms are covered.
C. The clause is construed generously: all claims relating to the contract, in contract or tort, common law or statute, fall within it unless there is good reason to conclude otherwise.
D. The clause covers every claim between the parties, including insolvency avoidance claims brought by a liquidator.

**Answer: C.** *Larsen Oil v Petroprod*, applying *Premium Nafta*, starts from the assumption that rational businessmen want all disputes from their relationship decided by one tribunal, so claims in contract or tort fall within the clause unless there is good reason otherwise. A and B: too narrow. D: in *Larsen* the court found that the pre-insolvency management was unlikely to have meant to include insolvency avoidance claims, and those claims are in any case non-arbitrable.
*Cite: Larsen Oil and Gas v Petroprod [2011] SGCA 21 at [13], [19], [20]*

### 0.V.5 — Foreign exclusive jurisdiction and illegality are no bar (Medipas; DMF)

**Qdrill-22** · `0.V.5` · drill-22 · `drp-m-0-37`

Consider these statements about arbitrability under Singapore law:

I. A dispute over rights in immovable property abroad is non-arbitrable whenever the foreign State's courts have exclusive jurisdiction over it.
II. A dispute in which one party alleges the contract is illegal may be arbitrable, and the tribunal may decide the illegality issue first.
III. After the award, the court may consider under Art 34(2)(b) whether the subject matter was arbitrable and whether the award conflicts with public policy.

Which are CORRECT?

A. II and III only
B. I and II only
C. I and III only
D. I, II and III

**Answer: A.** I is wrong: that the subject matter falls within a foreign court's exclusive jurisdiction does not necessarily make it non-arbitrable; disputes over rights in Mongolian immovable property were held arbitrable (*Medipas*). II is correct: illegality is arbitrable and the tribunal may decide it first (*DMF v DMG*). III is correct: after the award the court considers arbitrability and public policy under Art 34(2)(b) (*DMF* at [192]). B, C and D each include I.
*Cite: Medipas v Erdenet Mining [2026] SGHC 97 at [75]; DMF v DMG [2025] SGHC(I) 12 at [192]*

### 0.VI Pathological clauses and drafting — drills

Drills 23–25 cover 0.VI.5, 0.VI.6 and 0.VI.7.

### 0.VI.5 — Essential elements of a clause; model clauses

**Qdrill-23** · `0.VI.5` · drill-23 · `drp-m-0-43`

A client asks you to draft an arbitration clause from scratch rather than use the SIAC model clause. Which of the following is NOT good drafting practice?

A. Stating that disputes "shall" be referred to arbitration.
B. Specifying the seat and the language of the arbitration.
C. Stating the law governing the arbitration agreement.
D. Providing for two arbitrators, one appointed by each party, so each side has an equal voice.

**Answer: D.** The essential elements include the number of arbitrators, and the advice is to avoid two, since an even-numbered tribunal can deadlock. A, B and C are all among the essential elements: an exclusive, mandatory reference ("shall"), the seat, the language, and the governing law of the arbitration agreement. The other elements are certainty of the parties' identity, the scope of disputes, the institution and rules, and whether expedited arbitration may apply. The SIAC model clause refers disputes to SIAC under its rules "for the time being in force".
*Cite: ARB-SN p22–23 para 72; SIAC Rules 2025 model clause*

### 0.VI.6 — "May" or "can" refer to arbitration

**Qdrill-24** · `0.VI.6` · drill-24 · `drp-m-0-44`

A clause says that disputes "may be referred to arbitration in Singapore". Which statement is CORRECT?

A. Under Singapore law, "may" always makes a clause void for uncertainty.
B. Whether "may" creates an obligation to arbitrate is arguable; some courts read it as binding the parties once one of them elects to arbitrate, and drafters should use "shall" to avoid the point.
C. "May" means the parties have agreed that court proceedings are mandatory.
D. A clause saying disputes "can" be submitted to arbitration has been held never to be an agreement to arbitrate.

**Answer: B.** Optional wording is to be avoided; "shall" is recommended. Whether "may" obliges is arguable, and in *China State Construction v Madiford* (HK, 1992) "may refer to arbitration" was read as binding once a party elects. A and C overstate it. D: in *Guangdong Agriculture v Conagra* (HK, 1993) a clause saying disputes "can" be submitted to arbitration after failed negotiations was upheld as an agreement to arbitrate.
*Cite: China State Construction v Madiford (HK, 1992); Guangdong Agriculture v Conagra (HK, 1993); ARB-SN p23 paras 73–75*

### 0.VI.7 — A later agreement must be explicit to displace arbitration (CNA v CNB)

**Qdrill-25** · `0.VI.7` · drill-25 · `drp-m-0-45`

A 2021 contract contains a SIAC arbitration clause. In 2023 the parties sign a settlement agreement with a clause submitting disputes "under this settlement agreement" to the Singapore courts. A dispute arises under the original 2021 contract. Which is CORRECT?

A. The later court clause automatically replaces the arbitration agreement for all disputes.
B. The later clause supersedes the arbitration agreement only if it is sufficiently explicit in its terms.
C. An arbitration agreement can never be displaced once made.
D. The latest dispute resolution clause in time always prevails, regardless of its wording.

**Answer: B.** A later dispute resolution provision supersedes an agreement to arbitrate only if it is sufficiently "explicit in its terms" (*CNA v CNB*). Here the court clause is limited to disputes under the settlement agreement, so it does not explicitly displace arbitration for disputes under the 2021 contract. A and D: there is no automatic replacement or "last in time" rule. C: parties can displace arbitration, but must do so explicitly.
*Cite: CNA v CNB [2024] SGCA(I) 2 at [48]*

### 0.VII Stay of court proceedings under the IAA — drills

Drills 26–28 cover 0.VII.1, 0.VII.4 and 0.VII.6.

### 0.VII.1 — Who may apply and when (s 6(1) IAA)

**Qdrill-26** · `0.VII.1` · drill-26 · `drp-m-0-46`

P sues D in the Singapore High Court on a matter within an IAA arbitration agreement. D files and serves a notice of intention to contest. Which step, if taken next, would bar D from obtaining a stay under IAA s 6(1)?

A. Filing a defence on the merits before applying for a stay.
B. Filing a pleading contesting the court's jurisdiction.
C. Filing a stay application immediately after the notice of intention to contest.
D. Having filed and served the notice of intention to contest.

**Answer: A.** Under IAA s 6(1) the stay application is made at any time after filing and serving a notice of intention to contest or not contest, and before delivering any pleading (other than one contesting jurisdiction) or taking any other step. A defence on the merits is a pleading and a step, so it bars a stay. B: a pleading contesting jurisdiction is expressly excepted. C: that is the correct timing. D: the notice is the starting point of the window, not a bar. Under the Model Law the limit is the first statement on the substance (Art 8(1)).
*Cite: IAA s 6(1); Model Law Art 8(1)*

### 0.VII.4 — Is there a "dispute"? A mere denial is enough

**Qdrill-27** · `0.VII.4` · drill-27 · `drp-m-0-49`

C sues D for unpaid invoices despite an IAA arbitration clause. D applies for a stay and asserts that the goods were defective and the sum is not owed. C shows that D's defence is very weak. Which is CORRECT?

A. No stay: the court must first be satisfied that D has a real prospect of defending the claim.
B. No stay: D's earlier silence after receiving the invoices means there is no dispute.
C. Stay: a dispute exists once D positively asserts that the claim is disputed, even if the assertion is easily shown to be wrong; there is no dispute only where liability and quantum were clearly and unequivocally admitted.
D. Stay only if D provides security for the full claim.

**Answer: C.** The court does not look at the merits. A dispute exists once the defendant positively asserts that the claim is disputed, even if it is easily shown to be wrong (*Dalian* at [75]–[76]; *Tjong Very Sumito* at [49], [51]); there is no dispute only on a clear and unequivocal admission of liability and quantum (*Tjong* at [36]). A: that is a summary judgment test, not the stay test. B: D's positive assertion now counts; mere silence or refusal to pay would not be enough on its own. D: there is no such condition.
*Cite: Dalian Hualiang v Louis Dreyfus [2005] SGHC 161 at [75]–[76]; Tjong Very Sumito v Antig Investments [2009] SGCA 41 at [36], [49], [51]; DKB v DKC [2025] SGHC(I) 11 at [67]*

### 0.VII.6 — Arbitration may run meanwhile; discontinuance after 2 years

**Qdrill-28** · `0.VII.6` · drill-28 · `drp-m-0-51`

Consider these statements about IAA stay proceedings:

I. While a stay application is pending, arbitral proceedings may be commenced or continued and an award made.
II. The arbitration cannot start until the court has decided the stay application.
III. After a stay, if no party takes a further step in the court proceedings for at least 2 years, the court may on its own motion discontinue them, without prejudice to reinstatement.
IV. After a stay, the court proceedings are automatically struck out after 1 year.

Which are CORRECT?

A. II and IV only
B. I and III only
C. I and IV only
D. II and III only

**Answer: B.** I is correct: Model Law Art 8(2). III is correct: IAA s 6(4), on the court's own motion, without prejudice to an application to reinstate. II contradicts Art 8(2). IV is wrong: the period is 2 years and discontinuance is discretionary, not automatic. A, C and D each include a wrong statement.
*Cite: Model Law Art 8(2); IAA s 6(4)*

### 0.VIII Jurisdiction of the tribunal — drills

Drills 29–33 cover 0.VIII.2, 0.VIII.3, 0.VIII.4, 0.VIII.7 and 0.VIII.11.

### 0.VIII.2 — Separability: attack the clause, not the contract

**Qdrill-29** · `0.VIII.2` · drill-29 · `drp-m-0-53`

The respondent in an IAA arbitration says the whole contract was procured by bribery and is void, so the arbitration clause falls with it and the tribunal has no jurisdiction. It makes no allegation directed at the arbitration clause itself. Which is CORRECT?

A. If the contract is void, the arbitration clause is automatically void too.
B. The tribunal must stay the arbitration until a court decides whether the contract is void.
C. The arbitration clause is treated as independent of the other terms, so a finding that the contract is void does not of itself invalidate it; the challenge must target the clause itself.
D. Separability applies only under the SIAC Rules, not the Model Law.

**Answer: C.** Under Art 16(1) and SIAC25 r 31.1 the arbitration clause is treated as an agreement independent of the contract, and a decision that the contract is void does not of itself invalidate the clause. The clause can be attacked only on grounds relating directly to it (*Premium Nafta* at [17]), as applied in Singapore (*Philippines v PIATCO*). The tribunal may hold the contract invalid and still decide the consequences. A: reverses separability. B: the tribunal decides its own jurisdiction. D: Art 16(1) itself provides for separability.
*Cite: Model Law Art 16(1); SIAC25 r 31.1; Premium Nafta v Fili Shipping [2007] UKHL 40 at [17]; Government of the Philippines v Philippine International Air Terminals [2006] SGHC 206*

### 0.VIII.3 — Separability does not apply to contract formation (COT v COU)

**Qdrill-30** · `0.VIII.3` · drill-30 · `drp-m-0-54`

Two parties exchange conflicting standard forms; one form contains a SIAC clause. The buyer says no contract was ever concluded. An award is made against it, and it applies to set aside on the ground that there was no binding contract. Which is CORRECT?

A. Separability applies to questions of validity, not formation, so the clause does not survive by separability if no contract was concluded, and the seat court decides whether the contract existed.
B. Separability saves the clause even if no contract was ever concluded.
C. The court must defer to the tribunal's finding that a contract was concluded.
D. Formation objections can only be raised at the enforcement stage.

**Answer: A.** In *COT v COU*, following *DHL v Gemini Ocean*, the Court of Appeal held that separability applies to contractual validity, not formation; where a party says no contract was ever concluded, the clause in the alleged contract does not survive by separability ([30]). On a setting-aside application based on the absence of a binding contract, the seat court decides whether the contract existed ([39]). B: contradicts *COT*. C: the court decides the point itself. D: it can be raised on setting aside.
*Cite: COT v COU [2023] SGCA 31 at [30], [39]*

### 0.VIII.4 — Jurisdiction v admissibility; pre-arbitration conditions

**Qdrill-31** · `0.VIII.4` · drill-31 · `drp-m-0-55`

A clause requires 60 days of senior management negotiation before arbitration. The claimant starts arbitration after 20 days. Under Singapore law, which statement is CORRECT?

A. The Court of Appeal has finally decided that non-compliance with a pre-arbitration step always goes to jurisdiction.
B. Whether non-compliance goes to jurisdiction or admissibility is unsettled: *Lufthansa* treated an unsatisfied condition precedent as defeating jurisdiction, while *DRO v DRP* and *DSQ v DSR* treat it generally as a matter of admissibility, and the Court of Appeal is yet to decide.
C. Non-compliance with a pre-arbitration step is irrelevant to both jurisdiction and admissibility.
D. The distinction does not matter, because admissibility rulings are reviewable by the court in the same way as jurisdictional ones.

**Answer: B.** Jurisdiction is the tribunal's power to hear a case; admissibility is whether it is appropriate to hear it (*DRO* at [63]). *Lufthansa* at [63] found no jurisdiction, but the distinction was not argued; *DRO* called that view obiter ([59]) and held non-compliance generally goes to admissibility ([63]); *DSQ* agreed as a displaceable general proposition ([87]). The Court of Appeal is yet to decide (*DRO* at [68]). A: not decided. C: overstated. D: wrong; the distinction matters because admissibility rulings are not open to court review as jurisdictional ones are.
*Cite: International Research v Lufthansa [2013] SGCA 55 at [63]; DRO v DRP [2025] SGHC 255 at [59], [63], [68]; DSQ v DSR [2026] SGHC 67 at [87]*

### 0.VIII.7 — Preliminary ruling or ruling with the merits; bifurcation

**Qdrill-32** · `0.VIII.7` · drill-32 · `drp-m-0-58`

In a SIAC arbitration seated in Singapore, the respondent objects to jurisdiction and asks for bifurcation. Which is CORRECT?

A. The tribunal must always decide jurisdiction as a preliminary question.
B. The tribunal must always decide jurisdiction together with the merits.
C. The tribunal must refer the objection to the High Court before ruling.
D. The tribunal may rule on jurisdiction either as a preliminary question or in its award on the merits; bifurcation suits a doubtful jurisdictional issue separable from the merits, and a frivolous objection weighs against it.

**Answer: D.** Model Law Art 16(3), IAA s 10(2) ("at any stage") and SIAC25 r 31.3 all let the tribunal rule either as a preliminary question or in an award on the merits. Bifurcation can avoid long merits proceedings where jurisdiction is doubtful and separable from the merits; frivolous objections, a common delaying tactic, weigh against it. A and B: the tribunal has a choice. C: the tribunal rules first under competence-competence; court review comes afterwards under s 10(3).
*Cite: Model Law Art 16(3); IAA s 10(2); SIAC25 r 31.3*

### 0.VIII.11 — SIAC Court's prima facie review (SIAC r 8)

**Qdrill-33** · `0.VIII.11` · drill-33 · `drp-m-0-62`

Before the tribunal is constituted, the respondent in a SIAC arbitration writes to SIAC saying there is no arbitration agreement. Under the SIAC Rules 2025, which is CORRECT?

A. The arbitration is automatically suspended until a court decides the objection.
B. The SIAC Court decides the objection finally, and the tribunal cannot revisit it.
C. The arbitration proceeds and the tribunal decides jurisdiction, unless the Registrar refers the matter to the SIAC Court, which decides prima facie whether and how far the arbitration proceeds; a decision to proceed does not limit the tribunal's power to rule on its jurisdiction.
D. The Registrar must terminate the arbitration once any jurisdictional objection is made.

**Answer: C.** Under SIAC25 r 8.1 jurisdictional objections are for the tribunal unless the Registrar, before constitution, refers the matter to the SIAC Court. The SIAC Court makes a prima facie determination (r 8.2). A decision that the arbitration proceeds is without prejudice to the tribunal's power to rule on its jurisdiction; if the SIAC Court decides it shall not proceed, the Registrar terminates (r 8.3). A: no automatic suspension. B: the SIAC Court's view is only prima facie. D: termination follows only a SIAC Court decision not to proceed.
*Cite: SIAC25 rr 8.1–8.3*

### 0.IX Resisting jurisdiction: the respondent's options — drills

Drills 34–39 cover 0.IX.1, 0.IX.3, 0.IX.4, 0.IX.5, 0.IX.6 and 0.IX.7.

### 0.IX.1 — Participate, object and ask for a preliminary ruling

**Qdrill-34** · `0.IX.1` · drill-34 · `drp-m-0-63`

Your client is a respondent in a Singapore-seated IAA arbitration and says it never agreed to arbitrate. What is generally the safest course?

A. Take part, object no later than the statement of defence, and ask for jurisdiction to be decided as a preliminary issue, so that a positive ruling can be taken to the High Court under IAA s 10(3) within 30 days and the final award can later be challenged as well.
B. Ignore the arbitration entirely and wait for enforcement.
C. File a defence on the merits first and raise jurisdiction at the final hearing.
D. Apply to the High Court under s 10(3) before the tribunal has ruled.

**Answer: A.** The safest course is to participate, object in time and seek a preliminary ruling. A positive ruling is then reviewable at two stages: after the preliminary ruling (IAA s 10(3), 30 days) and after the final award (setting aside or resisting enforcement). B: non-participation is permitted but risky. C: a plea of no jurisdiction must be raised no later than the statement of defence (Art 16(2)). D: s 10(3) runs from the tribunal's ruling.
*Cite: IAA s 10(3); Model Law Art 16(2)*

### 0.IX.3 — Jurisdiction decided with the merits: set aside or resist enforcement

**Qdrill-35** · `0.IX.3` · drill-35 · `drp-m-0-65`

The respondent objected to jurisdiction in time. The tribunal declined to bifurcate and, in a single final award, upheld its jurisdiction and found for the claimant on the merits. Which is CORRECT?

A. The respondent must apply under IAA s 10(3) within 30 days, failing which it has no remedy.
B. The respondent has no recourse because the tribunal has competence-competence.
C. The respondent may only appeal to the High Court on a question of law.
D. Section 10(3) is not triggered; the respondent may apply to set aside the award (Art 34(2)(a)(i), (iii)) and/or resist enforcement wherever it is sought (IAA s 31(2)(b), (d); NYC Art V(1)(a), (c)).

**Answer: D.** Section 10(3) applies only to a positive ruling made as a preliminary question (or a negative ruling); where jurisdiction is upheld in an award that also decides the merits, the route is setting aside or resisting enforcement. A: s 10(3) does not apply. B: the tribunal's ruling remains subject to court review. C: there is no appeal on a question of law from an IAA award.
*Cite: Model Law Art 34(2)(a)(i), (iii); IAA s 31(2)(b), (d); NYC Art V(1)(a), (c)*

### 0.IX.4 — Not participating at all (Rakna)

**Qdrill-36** · `0.IX.4` · drill-36 · `drp-m-0-66`

A respondent denies it is party to any arbitration agreement and refuses to take any part in a Singapore-seated arbitration. An award is made against it. Which is CORRECT?

A. Having not participated, it is precluded from seeking to set aside the award for want of jurisdiction.
B. It may still seek to set aside the award at the seat for want of jurisdiction or resist enforcement on that ground, but the course is risky because, if the plea fails, it is bound by an award made without its case being argued.
C. The tribunal cannot proceed without the respondent's participation.
D. It must first have applied under IAA s 10(3) to preserve any challenge.

**Answer: B.** The Court of Appeal in *Rakna*, reversing the High Court, held that a non-participant is not precluded from applying to set aside for want of jurisdiction or resisting enforcement on that ground. It is risky: if the plea fails, the party is bound by an award reached without its case. A: states the reversed High Court position. C: the tribunal may proceed and make the award on the evidence (Art 25(b)–(c)). D: a non-participant never received a preliminary ruling to challenge, and *Rakna* does not require it.
*Cite: Rakna Arakshaka Lanka v Avant Garde Maritime Services [2019] SGCA 33 at [54]–[68]; Model Law Art 25(b)–(c)*

### 0.IX.5 — Boycotting after an adverse preliminary ruling

**Qdrill-37** · `0.IX.5` · drill-37 · `drp-m-0-67`

A respondent takes part, asks for a preliminary ruling on jurisdiction, and loses. It decides to boycott the rest of the arbitration. Which statement best reflects the position?

A. The boycott is a safe course, because the respondent is guaranteed the same recourse as a party that never participated.
B. Boycotting automatically waives every ground of challenge to the eventual award.
C. Boycotting is risky because the case law is unclear on what recourse a boycotting party has against the eventual award; it should at least apply under IAA s 10(3) within 30 days, and non-participation also limits later natural justice complaints.
D. Boycotting suspends the arbitration until the court rules.

**Answer: C.** The recourse of a party that boycotts after an adverse preliminary ruling is unclear in the case law, so the course is risky. The party should at least use s 10(3) within 30 days of the ruling. Non-participation also limits later natural justice complaints (*DEM v DEL*). A: no such guarantee; the position is unsettled. B: overstates the law in the other direction; it is not settled that every ground is lost. D: the tribunal may proceed in the absence of a party.
*Cite: IAA s 10(3); ARB-SN p30 para 101*

### 0.IX.6 — Going to court instead; the other side may stay or waive

**Qdrill-38** · `0.IX.6` · drill-38 · `drp-m-0-68`

Despite an IAA arbitration clause, A sues B in the Singapore High Court. B files a defence on the merits and a counterclaim without objecting to the court's jurisdiction. Six months later B applies for a stay. Which is CORRECT?

A. B has accepted the court's competence and waived the arbitration agreement for this dispute; having taken a step in the proceedings, it cannot obtain a stay under IAA s 6(1).
B. The court must stay the action because the IAA stay is mandatory.
C. B can still obtain a stay because waiver requires an express written agreement.
D. A's commencement of court proceedings itself makes the arbitration agreement void for all future disputes.

**Answer: A.** A party may sue in court instead of arbitrating; the other side will usually apply for a stay. If it instead defends on the merits without objecting to jurisdiction, it accepts the court's competence and waives the arbitration agreement for that dispute, and a step in the proceedings bars a stay under s 6(1). B: the mandatory stay depends on a timely application. C: waiver can arise from conduct. D: waiver is limited to that dispute.
*Cite: IAA s 6(1)*

### 0.IX.7 — Non-participant cannot raise an infra petita challenge (DEM v DEL)

**Qdrill-39** · `0.IX.7` · drill-39 · `drp-m-0-69`

R received notice of a Singapore-seated arbitration but chose not to take part. The award went against it. R applies to set aside, arguing that the arbitrator breached natural justice by failing to consider a limitation defence that R never raised. Which is CORRECT?

A. The application succeeds, because a tribunal must consider every defence that could have been raised.
B. The application succeeds, because non-participation preserves all natural justice grounds.
C. The court must remit the award for the tribunal to consider the limitation point.
D. The application fails: a party that had notice but chose not to participate cannot complain that the arbitrator failed to consider a point it never raised, as an infra petita ground is not open to it.

**Answer: D.** In *DEM v DEL* the Court of Appeal held that an infra petita ground is not available to a party that had notice of the arbitration but chose not to participate; it cannot complain that the tribunal failed to consider arguments it never made. A: the tribunal decides the points the parties put to it. B: non-participation limits such complaints. C: there is no failure to remedy by remission where the point was never raised.
*Cite: DEM v DEL [2025] SGCA 1 at [3], [54]–[58]*

### 0.X Constitution of the tribunal — drills

Drills 40–44 cover 0.X.2, 0.X.3, 0.X.5, 0.X.6 and 0.X.7.

### 0.X.2 — Institutional rules can override an agreed three-member tribunal (AQZ v ARA)

**Qdrill-40** · `0.X.2` · drill-40 · `drp-m-0-71`

A contract provides for SIAC arbitration "before three arbitrators". On the claimant's application, the SIAC President applies the Expedited Procedure and appoints a sole arbitrator. The respondent says the tribunal is improperly constituted. Which statement is CORRECT?

A. The appointment is invalid: an express three-arbitrator clause always prevails over the institution's rules.
B. The appointment is valid only if the respondent gives fresh written consent to a sole arbitrator.
C. The appointment is valid: by agreeing to the institutional rules, the parties agreed to the mechanism that let the institution appoint a sole arbitrator.
D. Under the SIAC Rules 2025 the Streamlined Procedure may have three arbitrators if the President so decides, so the respondent should have asked for that procedure instead.

**Answer: C.** By adopting the rules the parties agreed to the institution's power to appoint a sole arbitrator, despite a three-arbitrator clause; in *AQZ v ARA* the SIAC President's appointment of a sole arbitrator under the Expedited Procedure was upheld. A: this is the argument that failed in *AQZ v ARA*. B: no fresh consent is needed; consent lies in adopting the rules. D: the Streamlined Procedure always has a sole arbitrator (Sch 2 para 1); it is the Expedited Procedure that has a sole arbitrator unless the President decides otherwise (Sch 3 para 1).
*Cite: AQZ v ARA [2015] SGHC 49 at [128]–[137]; SIAC25 Sch 2 para 1, Sch 3 para 1*

### 0.X.3 — Default appointment procedure (ss 9A, 9B IAA; Art 11)

**Qdrill-41** · `0.X.3` · drill-41 · `drp-m-0-72`

An ad hoc IAA arbitration agreement provides for three arbitrators but no appointment procedure. Consider these statements.

I. In a two-party case each party appoints one arbitrator and the parties agree the third (s 9A).
II. If the parties fail to agree the third within 30 days of the first request, the appointing authority appoints on a party's request.
III. In a case with three or more parties, the two appointed arbitrators must appoint the presiding arbitrator within 30 days (s 9B).
IV. Where the parties instead fail to agree a sole arbitrator, the General Division of the High Court appoints.

A. I and II only
B. I, II and III only
C. I, II and IV only
D. I, II, III and IV

**Answer: A.** Statements I and II state s 9A. B: III is wrong; under s 9B the two appointed arbitrators have 60 days to appoint the presiding arbitrator. C: IV is wrong; a sole arbitrator not agreed is appointed by the appointing authority, the President of the SIAC Court (Art 11(3)(b) read with s 8(2)), not the court. D: III and IV are both wrong.
*Cite: IAA ss 9A, 9B, 8(2); MAL Art 11(3)(b)*

### 0.X.5 — Appointment under the SIAC Rules 2025

**Qdrill-42** · `0.X.5` · drill-42 · `drp-m-0-74`

Which statement about appointment under the SIAC Rules 2025 is NOT TRUE?

A. For a sole arbitrator, the parties have 21 days from commencement to make a joint nomination, failing which the President appoints.
B. A co-arbitrator nominated by a party takes office on nomination without any appointment by the President.
C. For a three-member tribunal, the Claimant nominates within 14 days of commencement and the Respondent within 14 days of receiving the Claimant's nomination.
D. A sole or presiding arbitrator is to be of a different nationality from the parties, unless the parties agree or the President decides otherwise.

**Answer: B.** Every nomination, whether by a party, the co-arbitrators or a third person, is subject to appointment by the President, who may refuse it after considering views (r 19.2–19.4). A: correct statement of r 21. C: correct statement of r 22.1. D: correct statement of r 19.7.
*Cite: SIAC25 rr 19.2–19.7, 21, 22.1*

### 0.X.6 — Arbitrator's duty to disclose (Art 12(1); SIAC r 20)

**Qdrill-43** · `0.X.6` · drill-43 · `drp-m-0-75`

Six months into a Singapore-seated SIAC arbitration, an arbitrator learns of a circumstance likely to give rise to justifiable doubts as to her independence. She made full disclosure when she was appointed. What must she do?

A. Nothing: the duty to disclose ends once the arbitrator is appointed.
B. Disclose only if the circumstance falls on the IBA Non-Waivable Red List.
C. Disclose it to the Registrar alone, as before her appointment.
D. Disclose it without delay to the parties and the other arbitrators, because the duty to disclose continues throughout the arbitration.

**Answer: D.** The duty to disclose circumstances likely to give rise to justifiable doubts continues throughout the arbitration (Art 12(1)). Under SIAC r 20.2–20.3 disclosure goes to the Registrar before appointment and to everyone after it. A: the duty is continuing. B: the test is justifiable doubts; the IBA Orange List shows what to disclose, and only Green List matters need no disclosure. C: disclosure to the Registrar alone is the pre-appointment stage.
*Cite: MAL Art 12(1); SIAC25 r 20.2–20.3; IBA-COI Part II paras 3, 7*

### 0.X.7 — Immunity of arbitrators and institutions (ss 25, 25A)

**Qdrill-44** · `0.X.7` · drill-44 · `drp-m-0-76`

After losing an IAA arbitration, R sues the sole arbitrator for a negligent mistake of law in the award, and sues SIAC, which appointed him, on the basis that it appointed him. Which statement is CORRECT?

A. The arbitrator is not liable for negligence or for a mistake of law in the award (s 25), and SIAC is not liable merely because it appointed him (s 25A).
B. SIAC is liable for the arbitrator's negligence because it appointed him.
C. The arbitrator is immune for negligence in procedure, but liable for a mistake of law in the award.
D. The only protection is the contractual exclusion in SIAC r 65.1; the IAA confers no immunity.

**Answer: A.** Section 25 protects the arbitrator from liability for negligence and for any mistake in law, fact or procedure in the proceedings or award. Section 25A protects the appointing institution for its appointment function unless it acted in bad faith, and it is not liable merely because it appointed the arbitrator. B: contrary to s 25A. C: s 25(b) expressly covers mistakes of law in the award. D: the statutory immunities are in ss 25 and 25A; r 65.1 only adds to them.
*Cite: IAA ss 25, 25A; SIAC25 r 65.1*

### 0.XI Challenging an arbitrator — drills

Drills 45–53 cover 0.XI.2, 0.XI.3, 0.XI.4, 0.XI.5, 0.XI.6, 0.XI.7, 0.XI.8, 0.XI.10 and 0.XI.11.

### 0.XI.2 — Test: reasonable suspicion of bias

**Qdrill-45** · `0.XI.2` · drill-45 · `drp-m-0-78`

Which statement of the Singapore test for apparent bias of an arbitrator is CORRECT?

A. Whether there is a real likelihood, on the balance of probabilities, that the arbitrator is biased.
B. Whether a fair-minded, reasonable person with knowledge of the relevant facts would reasonably suspect that the tribunal may be biased; the possibility of bias is enough.
C. Whether a member of the public without knowledge of the relevant facts would suspect bias.
D. Whether, once justifiable doubts are shown, the challenger can also prove actual bias.

**Answer: B.** The test is reasonable suspicion, judged by an informed, fair-minded observer, and the standard is possibility, not probability (*BYL v BYN* at [50]–[51]). A: that is a probability test, which Singapore does not use. C: the observer knows the relevant facts and sees them in context. D: once justifiable doubts are found, actual bias need not be proved.
*Cite: BYL v BYN [2020] SGHC(I) 6 at [50]–[51]; PT Central Investindo v Franciscus Wongso [2014] SGHC 190 at [14], [18]*

### 0.XI.3 — Actual, imputed and apparent bias

**Qdrill-46** · `0.XI.3` · drill-46 · `drp-m-0-79`

An arbitrator has a pecuniary interest in the outcome of the arbitration. How do Singapore courts classify this, and with what consequence?

A. Apparent bias, so the court asks whether a fair-minded observer would reasonably suspect bias.
B. Actual bias, which the challenger must prove on the balance of probabilities.
C. Imputed bias: the arbitrator is in effect a judge in their own cause, and disqualification is automatic without any inquiry into likelihood or suspicion.
D. No bias at all, unless the interest is also on the IBA Non-Waivable Red List.

**Answer: C.** *PT Central Investindo* recognises actual, imputed and apparent bias. A pecuniary or proprietary interest makes the arbitrator a judge in their own cause, which is imputed bias, and disqualification is automatic. A: the reasonable suspicion inquiry is for apparent bias and is not needed here. B: actual bias need not be shown. D: the IBA Guidelines are soft law and do not decide whether the law treats a situation as bias.
*Cite: PT Central Investindo v Franciscus Wongso [2014] SGHC 190 at [15]*

### 0.XI.4 — Private contact with one party

**Qdrill-47** · `0.XI.4` · drill-47 · `drp-m-0-80`

Consider these statements about an arbitrator's private contact with one party.

I. There is an absolute rule that an arbitrator may never correspond directly with a party.
II. Private correspondence with one party can found a challenge to the arbitrator.
III. Initial contact with a party limited to the arbitrator's availability and qualifications is on the IBA Green List.
IV. *Turner (East Asia) v Builders Federal* holds that direct correspondence with one party is acceptable whenever convenient.

A. I and II only
B. II and III only
C. III and IV only
D. II, III and IV only

**Answer: B.** Private contact or correspondence with one party can found a challenge (II), and initial contact limited to availability and qualifications is Green List 4.4.1 (III). A: I is wrong; *Turner* says there is no absolute rule. C and D: IV is wrong; *Turner* says such correspondence should happen only in very exceptional circumstances.
*Cite: Turner (East Asia) v Builders Federal (Hong Kong) [1988] SGHC 47 at [135]; IBA-COI 4.4.1*

### 0.XI.5 — IBA Non-Waivable Red List

**Qdrill-48** · `0.XI.5` · drill-48 · `drp-m-0-81`

Which situation falls on the IBA Non-Waivable Red List (2024)?

A. The arbitrator holds shares in a privately held party.
B. The arbitrator is in the same law firm as one party's counsel.
C. The arbitrator acted as counsel for one party two years ago and has no ongoing relationship with it.
D. The arbitrator regularly advises one party, and the arbitrator's firm derives significant financial income from that work.

**Answer: D.** Regularly advising a party where the arbitrator or their firm derives significant financial income from it is Non-Waivable Red List 1.4; the parties' acceptance cannot cure it. A: Waivable Red 2.2.1. B: Waivable Red 2.3.3. C: Orange 3.1.1 (counsel for a party within 3 years).
*Cite: IBA-COI 2024 list (1) para 1.4; list (2) paras 2.2.1, 2.3.3; list (3) para 3.1.1*

### 0.XI.6 — IBA Waivable Red List

**Qdrill-49** · `0.XI.6` · drill-49 · `drp-m-0-82`

A proposed arbitrator discloses that she gave legal advice on this very dispute to an affiliate of the claimant. The respondent receives the disclosure and says nothing. Which statement is CORRECT under the IBA Guidelines (2024)?

A. This is on the Waivable Red List, so she may act only if the parties, aware of the conflict, expressly agree to her acting; the respondent's silence is not enough.
B. This is on the Orange List, so the respondent is deemed to accept her because it made no timely objection.
C. This is on the Non-Waivable Red List, so she cannot act even with both parties' express agreement.
D. This is on the Green List, so she did not need to disclose it at all.

**Answer: A.** Giving legal advice on the dispute to a party or an affiliate is Waivable Red 2.1.1. It is cured only by the parties' express agreement, given with knowledge of the conflict. B: deemed acceptance on no timely objection is the Orange List rule. C: the Non-Waivable Red List covers cases such as identity with a party or a significant interest in the outcome. D: wrong list.
*Cite: IBA-COI 2024 list (2) para 2.1.1*

### 0.XI.7 — IBA Orange List

**Qdrill-50** · `0.XI.7` · drill-50 · `drp-m-0-83`

Which situation falls on the IBA Orange List (2024), so that the arbitrator must disclose it?

A. The arbitrator published a law review article on an issue in the case, not focused on the case.
B. The arbitrator is an employee of one of the parties.
C. The arbitrator has publicly advocated a position on the case, including on social media.
D. The arbitrator is in the same law firm as the respondent's counsel.

**Answer: C.** Publicly advocating a position on the case, including on social media, is Orange List 3.4.2. It must be disclosed, and the parties are deemed to accept the arbitrator if they make no timely objection. A: Green List 4.1.1. B: Non-Waivable Red 1.1. D: Waivable Red 2.3.3.
*Cite: IBA-COI 2024 list (3) para 3.4.2; list (4) para 4.1.1; list (1) para 1.1; list (2) para 2.3.3*

### 0.XI.8 — IBA Green List

**Qdrill-51** · `0.XI.8` · drill-51 · `drp-m-0-84`

An arbitrator considers whether to disclose these facts.

I. She previously sat as co-arbitrator with the claimant's counsel in an unrelated case.
II. She is connected with the respondent's counsel on a social media network.
III. She holds an insignificant number of shares in a listed company that is a party.
IV. She has a close personal friendship with the claimant's counsel.

Which are on the IBA Green List, so that she has no duty to disclose them?

A. I and II only
B. I, II and III only
C. II, III and IV only
D. I, II, III and IV

**Answer: B.** I is Green 4.3.2, II is Green 4.3.1 and III is Green 4.4.2; Green List situations need no disclosure. C and D: IV is wrong; a close personal friendship with counsel is Orange List 3.2.6 and must be disclosed. A: leaves out III, which is also Green.
*Cite: IBA-COI 2024 list (4) paras 4.3.1, 4.3.2, 4.4.2; list (3) para 3.2.6*

### 0.XI.10 — Challenge procedure under the SIAC Rules 2025

**Qdrill-52** · `0.XI.10` · drill-52 · `drp-m-0-86`

Which statement about challenging an arbitrator under the SIAC Rules 2025 is NOT TRUE?

A. If, within 7 days, the other parties agree to the challenge or the arbitrator withdraws, a substitute is appointed, which does not imply the grounds were valid.
B. The time limit to challenge an emergency arbitrator is 24 hours.
C. Under the Streamlined Procedure the time limit to challenge is 3 days.
D. The notice of challenge is filed with the tribunal within 30 days, and the tribunal itself decides the challenge.

**Answer: D.** Under SIAC25 the notice goes to the Registrar within 15 days of receiving notice of the appointment, or of when the reasons became known or should reasonably have been known (r 27.1). If the challenge is not agreed or the arbitrator does not withdraw, the SIAC Court decides it with reasons, and the decision is final under the Rules (r 28). A: r 27.5. B: Sch 1 para 9. C: Sch 2 para 5.
*Cite: SIAC25 rr 27.1, 27.5, 28; Sch 1 para 9; Sch 2 para 5*

### 0.XI.11 — Failure or inability to act (Art 14); substitute (Art 15)

**Qdrill-53** · `0.XI.11` · drill-53 · `drp-m-0-87`

In a Singapore-seated ad hoc arbitration under the Model Law, an arbitrator has been seriously ill for eight months and is not acting. He will not withdraw, and the other party will not agree to end his mandate. Which statement is CORRECT?

A. The party must first send a written challenge to the tribunal within 15 days under Art 13, and only then go to court.
B. The party may apply directly to the court under Art 14 to decide on termination of the mandate, with no time limit, and the court's decision is not subject to appeal.
C. The party must apply to the court within 30 days of the arbitrator becoming ill, failing which the objection is waived.
D. If the mandate ends, the two remaining arbitrators choose the substitute, whatever rules applied to the original appointment.

**Answer: B.** Where an arbitrator is de facto unable to act, or fails to act without undue delay, and does not withdraw and the parties do not agree, any party may ask the court to decide; there is no appeal (Art 14(1)). Unlike Art 13, Art 14 goes directly to court and has no time limit. A: that is the Art 13 challenge procedure for justifiable doubts. C: Art 14 has no time limit. D: the substitute is appointed under the rules that applied to the original appointment (Art 15).
*Cite: MAL Arts 14–15; ROC O 48 r 2(1)(b)*

### 0.XII Arb-Med, Arb-Med-Arb and multi-tier clauses — drills

Drills 54–59 cover 0.XII.1, 0.XII.2, 0.XII.3, 0.XII.4, 0.XII.5 and 0.XII.6.

### 0.XII.1 — Arbitrator acting as conciliator (ss 16–17 IAA)

**Qdrill-54** · `0.XII.1` · drill-54 · `drp-m-0-89`

During an IAA arbitration, the parties ask the sole arbitrator to try to mediate. Consider these statements.

I. The arbitrator may act as conciliator only if all parties consent in writing, and only while no party withdraws that consent.
II. Information one party gives the arbitrator in private must always stay confidential, even if the conciliation fails and the arbitration resumes.
III. No objection may be taken to the arbitrator's conduct of the arbitration solely because the arbitrator acted as conciliator.
IV. The arbitrator acting as conciliator may communicate with the parties only collectively, never separately.

A. I and III only
B. I, II and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: A.** I states s 17(1) and III states s 17(4). B and D: II is wrong; if conciliation fails, before resuming the arbitration the arbitrator must disclose to the other parties as much of the confidential information as they consider material (s 17(3)). C and D: IV is wrong; the arbitrator may communicate with the parties collectively or separately (s 17(2)(a)).
*Cite: IAA s 17(1)–(4); s 16(5) ("conciliator" includes a mediator)*

### 0.XII.2 — SIAC-SIMC Arb-Med-Arb Protocol

**Qdrill-55** · `0.XII.2` · drill-55 · `drp-m-0-90`

A contract contains the SIAC-SIMC Arb-Med-Arb model clause. Which statement about the process is CORRECT?

A. The arbitral tribunal itself conducts the mediation, and the same individual then resumes as arbitrator.
B. The mediation must be completed within 4 months of the mediator's appointment, failing which it terminates.
C. After the Notice and Response, the arbitration is stayed and the dispute goes to SIMC for mediation by a separate mediator; any settlement may be recorded by the tribunal as a consent award.
D. A settlement reached in the SIMC mediation takes effect only as a contract and cannot be enforced as an arbitral award.

**Answer: C.** Under the AMA Protocol the arbitration is stayed after the Notice and Response, a separate SIMC mediator mediates, and any settlement may be recorded as a consent award, generally enforceable under the New York Convention. If no settlement is reached, the arbitration resumes. A: the Protocol uses a separate mediator, not double-hatting. B: the mediation is to finish within 8 weeks of the Mediation Commencement Date unless the Registrar extends; 4 months is the IAA s 16(4) default for conciliation. D: settlement can be recorded as a consent award.
*Cite: SIAC25 pp85–87 (AMA Protocol), r 6.4(a)*

### 0.XII.3 — Consent award (Art 30; s 18 IAA)

**Qdrill-56** · `0.XII.3` · drill-56 · `drp-m-0-91`

The parties settle midway through a Singapore-seated SIAC arbitration and ask the tribunal to record the settlement. Which statement is NOT TRUE?

A. The award on agreed terms must state the tribunal's reasons, as Art 31(2) requires of every award.
B. The award on agreed terms has the same status and effect as any other award on the merits.
C. Under IAA s 18 it may be enforced with the High Court's permission in the same way as a judgment.
D. The tribunal terminates the proceedings, and records the settlement as an award only if asked and it does not object.

**Answer: A.** Art 31(2) excludes consent awards from the duty to give reasons, and SIAC25 r 52.3 likewise says reasons are not needed. B and D: Art 30. C: s 18 treats the award on agreed terms as an award on an arbitration agreement, enforceable with permission like a judgment.
*Cite: MAL Arts 30, 31(2); IAA s 18; SIAC25 r 52.3*

### 0.XII.4 — "Unless settled amicably": too uncertain to be a condition (CZQ v CZS)

**Qdrill-57** · `0.XII.4` · drill-57 · `drp-m-0-92`

A clause reads: "Unless settled amicably, any dispute shall be finally settled by international arbitration." The claimant starts arbitration without any prior negotiation. The respondent says the tribunal lacks jurisdiction. Which statement is CORRECT?

A. The clause creates a binding condition precedent, so the arbitration was started prematurely.
B. The clause is a binding condition precedent, but non-compliance goes only to admissibility.
C. The clause requires a mandatory 30-day negotiation period before arbitration.
D. The clause did not create a legally binding condition precedent because "settled amicably" was undefined and too uncertain, so arbitration could be started without negotiating first.

**Answer: D.** In *CZQ v CZS* the SICC held this wording too uncertain to impose a binding pre-arbitration step. A, B: no condition precedent arose. C: the clause specified no period at all, which is why it failed. To make a pre-arbitration step binding, the clause must define what is to be done, with whom and for how long.
*Cite: CZQ v CZS [2023] SGHC(I) 16 at [13], [20], [22]*

### 0.XII.5 — Specific performance of an obligation to mediate (Maxx Engineering)

**Qdrill-58** · `0.XII.5` · drill-58 · `drp-m-0-93`

A clause says the parties "shall refer the dispute for mediation at the SMC" if negotiations fail, and adds that mediation is not a condition precedent to arbitration. The respondent refuses to mediate. Following *Maxx Engineering Works v PQ Builders*, which statement is CORRECT?

A. Because mediation is not a condition precedent, the clause imposes no legal obligation to mediate.
B. The clause imposes a legal obligation to mediate, and the court may order specific performance compelling the respondent to refer the dispute to mediation.
C. The only remedy is damages, because courts never compel parties to mediate.
D. The court will refuse specific performance because mediation is always futile once one party refuses to take part.

**Answer: B.** The High Court held that the clause imposed an obligation to mediate despite the "not a condition precedent" wording, and ordered specific performance. Damages were inadequate, there was no substantial hardship, mediation was not shown to be futile, and compliance was easy to assess. A: rejected in *Maxx*. C: the court ordered specific performance. D: futility needs evidence that mediation would fail; there was none.
*Cite: Maxx Engineering Works v PQ Builders [2023] SGHC 71*

### 0.XII.6 — Repudiating the mediation tier: stay refused (Heartronics)

**Qdrill-59** · `0.XII.6` · drill-59 · `drp-m-0-94`

Under a med-arb clause, D delays the mediation, fails to pay the mediation fees and pleads unsubstantiated cash-flow problems. P accepts this as repudiation and sues in court. D applies to stay the action in favour of arbitration. Following *Heartronics Corp v EPI Life*, what is the likely result?

A. Stay granted: the arbitration tier is separable and survives any breach of the mediation tier.
B. Stay granted, but P may claim damages for D's failure to mediate.
C. Stay refused: the mediation and arbitration tiers formed one unitary mechanism, D's conduct was a repudiatory breach, and once P accepted it the med-arb clause, including the arbitration tier, was inoperative.
D. Stay refused, because a failure to pay mediation fees automatically makes any arbitration agreement null and void.

**Answer: C.** In *Heartronics* the two tiers formed a unitary dispute resolution mechanism ([78]–[80]). D's conduct showed it did not intend to mediate, which was a repudiatory breach ([168]–[169]); once P accepted it, the clause was inoperative and the stay was refused ([214]). A and B: the tiers were not treated as separate. D: the result depended on repudiation and acceptance, not on an automatic rule.
*Cite: Heartronics Corp v EPI Life [2017] SGHCR 17 at [78]–[80], [168]–[169], [214]*

### 0.XIII Conduct of the proceedings and evidence — drills

Drills 60–67 cover 0.XIII.3, 0.XIII.4, 0.XIII.5, 0.XIII.8, 0.XIII.9, 0.XIII.10, 0.XIII.11 and 0.XIII.12.

### 0.XIII.3 — Default of a party (Art 25)

**Qdrill-60** · `0.XIII.3` · drill-60 · `drp-m-0-97`

In a Singapore-seated ad hoc arbitration, the respondent fails, without sufficient cause, to communicate its statement of defence by the deadline. The parties have agreed nothing about default. What does the Model Law provide?

A. The tribunal must terminate the proceedings.
B. The tribunal continues the proceedings, without treating the failure as an admission of the claim.
C. The tribunal treats the failure as an admission and makes an award for the claimant without considering the evidence.
D. The tribunal must adjourn until the respondent files its defence.

**Answer: B.** Art 25(b) applies where the respondent fails to communicate its defence: the tribunal continues, and the failure is not an admission. A: termination is the consequence when the claimant fails to communicate its statement of claim (Art 25(a)). C: there is no deemed admission. D: Art 25 lets the tribunal proceed; if a party fails to appear or produce documents, it may make the award on the evidence before it (Art 25(c)).
*Cite: MAL Art 25(a)–(c)*

### 0.XIII.4 — Document production (s 12(1)(b) IAA)

**Qdrill-61** · `0.XIII.4` · drill-61 · `drp-m-0-98`

Consider these statements about a Singapore-seated tribunal's powers over document production.

I. The tribunal may order a party to give discovery of documents.
II. The tribunal may order a party to give discovery of facts.
III. The current s 12(1)(b) IAA refers to "discovery of documents and interrogatories".
IV. The Prague Rules encourage extensive document production.

A. I and II only
B. I, II and III only
C. I, II and IV only
D. I, II, III and IV

**Answer: A.** Section 12(1)(b) empowers the tribunal to order discovery of documents and discovery of facts. B and D: III is wrong; the current text (Act 32 of 2020) reads "discovery of documents and discovery of facts", not interrogatories. C and D: IV is wrong; the Prague Rules discourage document production, whereas the IBA Rules on Evidence provide a request-to-produce procedure.
*Cite: IAA s 12(1)(b); IBA-EV Art 3*

### 0.XIII.5 — Court orders to attend and produce documents (s 13 IAA; ALC v ALF)

**Qdrill-62** · `0.XIII.5` · drill-62 · `drp-m-0-99`

Which statement about court assistance in taking evidence is CORRECT?

A. The High Court may order a witness anywhere in the world to attend a Singapore-seated arbitration.
B. Under an order to produce documents, a person may be compelled to produce documents they could not be compelled to produce at a court trial.
C. *ALC v ALF* was decided under s 13 IAA and held that a party need never consult the tribunal before seeking court assistance.
D. In *ALC v ALF*, a domestic case under AA s 30, the subpoena was set aside because the applicant should first have sought the tribunal's directions on calling the witness, as the procedural order required.

**Answer: D.** In *ALC v ALF* the subpoena was set aside because the applicant had not first sought the tribunal's directions as Procedural Order No 1 required. A: under s 13 the High Court acts where the witness is in Singapore. B: no one can be made to produce a document they could not be compelled to produce at trial (s 13(4)). C: *ALC v ALF* was decided under AA s 30, not the IAA, and it held the opposite.
*Cite: IAA s 13(1)–(2), (4); MAL Art 27; ALC v ALF [2010] SGHC 231 at [40]*

### 0.XIII.8 — Termination of proceedings (Art 32; DRL v DRK)

**Qdrill-63** · `0.XIII.8` · drill-63 · `drp-m-0-102`

A claimant fails for over two years to provide security for costs ordered by the tribunal, despite sanctions. The tribunal orders termination under Art 32(2)(c). Consider these statements in light of *DRL v DRK*.

I. Art 32(2)(c) gives the tribunal a discretion to continue even after finding that continuation has become impossible.
II. The cause of the impossibility is immaterial.
III. On a challenge, the court reviews only the fairness of the process that led to the termination order, not its merits.
IV. The tribunal must refuse to terminate if termination would leave the claimant's claim time-barred.

A. I and II only
B. II and III only
C. II, III and IV only
D. I, III and IV only

**Answer: B.** In *DRL v DRK* the cause of the impossibility was immaterial ([65]), and the court reviews only the fairness of the process leading to the order ([38], [53]). A and D: I is wrong; there is no discretion to proceed once impossibility is found ([57]). C and D: IV is wrong; claimants must guard against limitation themselves ([58]).
*Cite: MAL Art 32(2)(c); DRL v DRK [2026] SGHC 32 at [38], [53], [57], [58], [65]*

### 0.XIII.9 — Early dismissal (SIAC r 47; DBO v DBP)

**Qdrill-64** · `0.XIII.9` · drill-64 · `drp-m-0-103`

Which statement about early dismissal under the SIAC Rules 2025 is NOT TRUE?

A. A party may apply for early dismissal of a claim or defence that is manifestly without legal merit or manifestly outside the tribunal's jurisdiction.
B. The tribunal first decides whether to allow the application to proceed.
C. If the application proceeds, the tribunal must decide it within 90 days of filing.
D. In *DBO v DBP* the Court of Appeal rejected a natural justice challenge to an early-dismissal award.

**Answer: C.** Under r 47 the tribunal decides within 45 days of filing (extendable); 90 days is the period for a preliminary determination under r 46. A, B: r 47. D: in *DBO v DBP* the challenge failed, showing the court's deference to tribunals' case management. Early dismissal is also unavailable under the Streamlined Procedure (Sch 2).
*Cite: SIAC25 rr 46–47, Sch 2; DBO v DBP [2024] SGCA(I) 4 at [29], [48]*

### 0.XIII.10 — Preliminary determination (SIAC r 46)

**Qdrill-65** · `0.XIII.10` · drill-65 · `drp-m-0-104`

In a SIAC arbitration under the 2025 Rules (not under the Streamlined Procedure), the respondent wants a limitation defence decided first. The claimant does not agree. Which statement is CORRECT?

A. The respondent may apply for a final and binding preliminary determination if it is likely to save time and costs, and the tribunal decides within 90 days of filing unless the Registrar extends.
B. A preliminary determination is available only if both parties agree.
C. The tribunal must decide the application within 45 days of filing.
D. Rule 46 removes the tribunal's inherent power to order preliminary issues.

**Answer: A.** Rule 46.1 allows an application where (a) the parties agree, (b) it is likely to save time and costs and make resolution more efficient, or (c) the circumstances otherwise warrant it. The decision is due within 90 days of filing unless the Registrar extends (r 46.4). B: agreement is only one of three grounds. C: 45 days is the early dismissal period (r 47). D: the inherent power remains (r 46.5).
*Cite: SIAC25 r 46.1, 46.3–46.5*

### 0.XIII.11 — Security for costs

**Qdrill-66** · `0.XIII.11` · drill-66 · `drp-m-0-105`

In a Singapore-seated IAA arbitration, the respondent applies for security for costs on the sole ground that the claimant is a BVI company with no assets in Singapore. Which statement is CORRECT?

A. The tribunal has no power to order security for costs; only the High Court has.
B. The tribunal must order security, because the claimant is incorporated outside Singapore.
C. The tribunal may order security, but only for the respondent's claim, not its costs.
D. The tribunal may order security for costs, but must not do so only because the claimant is incorporated outside Singapore.

**Answer: D.** A Singapore-seated tribunal may order security for costs (s 12(1)(a); SIAC25 r 48), but s 12(4) bars an order made only because the claimant is a company incorporated or managed outside Singapore. A: the power lies with the tribunal; the court's s 12A powers do not cover security for costs. B: contrary to s 12(4). C: security for costs is available, and SIAC25 r 49 separately allows security for the claim.
*Cite: IAA s 12(1)(a), (4); SIAC25 rr 48–49*

### 0.XIII.12 — Third-party funding disclosure (SIAC r 38)

**Qdrill-67** · `0.XIII.12` · drill-67 · `drp-m-0-106`

Two months after filing its Notice of Arbitration under the SIAC Rules 2025, the claimant enters into a third-party funding agreement. What must it do?

A. Nothing, unless the tribunal orders disclosure.
B. Disclose the existence of the funding agreement and the funder's identity and contact details as soon as practicable after concluding it.
C. Disclose only that funding exists, keeping the funder's identity confidential.
D. Disclose the funding only at the costs stage after the final award.

**Answer: B.** Rule 38 requires disclosure of the existence of any third-party funding agreement and the funder's identity and contact details. Disclosure is made in the Notice or Response or, if the agreement comes later, as soon as practicable after concluding it, and later changes must also be notified. A: the duty does not depend on an order. C: the funder's identity is required. D: disclosure is early so arbitrators can check conflicts.
*Cite: SIAC25 rr 6.3(h), 7.1(g), 38, 59.1*

### 0.XIV Commencing the arbitration and SIAC procedures — drills

Drills 68–72 cover 0.XIV.1, 0.XIV.2, 0.XIV.3, 0.XIV.4 and 0.XIV.5.

### 0.XIV.1 — Notice of Arbitration: commencement and contents (SIAC r 6)

**Qdrill-68** · `0.XIV.1` · drill-68 · `drp-m-0-107`

C delivers a Notice of Arbitration under the SIAC Rules 2025. The Registrar receives it on 3 March; R receives it on 6 March. When did the arbitration commence, and which item must the Notice include?

A. 6 March; the Notice must include the full Statement of Claim.
B. 6 March; the Notice must include the names of three proposed arbitrators.
C. 3 March; the Notice must include, among other things, a statement on any third-party funding agreement and an initial estimate of the claim amount.
D. 3 March; the Notice need not include a copy or description of the arbitration agreement.

**Answer: C.** Under SIAC25 r 6.2 the date the Registrar receives the Notice is the date of commencement. Rule 6.3 requires, among other things, the relief sought with an initial estimate of the claim amount (r 6.3(f)) and a third-party funding statement (r 6.3(h)). A, B: 6 March is the Model Law Art 21 rule (respondent's receipt); the Statement of Claim may be included (r 6.4) but need not be, and the Notice need only comment on the number of arbitrators and constitution (r 6.3(g)). D: the arbitration agreement is required (r 6.3(d)).
*Cite: SIAC25 r 6.2–6.4*

### 0.XIV.2 — Response to the Notice (SIAC r 7)

**Qdrill-69** · `0.XIV.2` · drill-69 · `drp-m-0-108`

A SIAC arbitration under the 2025 Rules commenced on 1 March. The respondent received the Notice on 5 March. By when must it deliver its Response?

A. 15 March
B. 31 March
C. 4 April
D. 19 March

**Answer: D.** The Response is due within 14 days of commencement or of receipt of the Notice, whichever is later (r 7.1). The later date is 5 March, so the deadline is 19 March. A: 14 days from commencement, the earlier date. B and C: 30-day periods, which r 7.1 does not use. The Response may, but need not, include the Defence and Counterclaim (r 7.2). Failing to respond does not stop the arbitration (r 7.4).
*Cite: SIAC25 r 7.1, 7.2, 7.4*

### 0.XIV.3 — Commencement under the Model Law; limitation (Art 21; s 8A IAA)

**Qdrill-70** · `0.XIV.3` · drill-70 · `drp-m-0-109`

Consider these statements about commencement and limitation in Singapore-seated IAA arbitrations.

I. In an ad hoc arbitration, unless otherwise agreed, proceedings start on the date the respondent receives a request to refer the dispute to arbitration.
II. The Limitation Act 1959 does not apply to arbitrations.
III. If an award is set aside, the court may order that the period between commencement and the setting-aside order be excluded for limitation purposes.
IV. Under the SIAC Rules 2025, the arbitration commences on the date the Registrar receives the Notice.

A. I and II only
B. I and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: C.** I is Art 21, III is s 8A(2) and IV is SIAC25 r 6.2. A and D: II is wrong; s 8A(1) applies the Limitation Act 1959 and the Foreign Limitation Periods Act 2012 to arbitrations as to court proceedings. B: leaves out IV, which is also correct.
*Cite: MAL Art 21; IAA s 8A(1)–(2); SIAC25 r 6.2*

### 0.XIV.4 — Streamlined Procedure (SIAC r 13, Schedule 2)

**Qdrill-71** · `0.XIV.4` · drill-71 · `drp-m-0-110`

Which statement about the SIAC Rules 2025 Streamlined Procedure is CORRECT?

A. It applies automatically where the amount in dispute exceeds S$1,000,000 but not S$10,000,000.
B. The tribunal has three members if the President so decides.
C. The final award is due within 6 months of the tribunal's constitution.
D. The final award is due within 3 months of constitution unless the Registrar extends, and no early dismissal application may be made.

**Answer: D.** Schedule 2 provides for a final award within 3 months of constitution and excludes preliminary determination (r 46) and early dismissal (r 47) applications. A: the Streamlined Procedure applies by agreement or where the amount does not exceed S$1,000,000 (r 13.1); the S$1m–10m band is for an Expedited Procedure application (r 14.2(a)). B: always a sole arbitrator. C: 6 months is the Expedited Procedure.
*Cite: SIAC25 r 13.1, Sch 2*

### 0.XIV.5 — Expedited Procedure (SIAC r 14, Schedule 3)

**Qdrill-72** · `0.XIV.5` · drill-72 · `drp-m-0-111`

A SIAC arbitration under the 2025 Rules involves a S$6 million claim. The parties have not agreed to any expedited procedure, and the tribunal has not been constituted. The claimant wants the Expedited Procedure. Which statement is CORRECT?

A. The claimant may apply, and the President decides after hearing the parties; if it applies, there is a sole arbitrator unless the President decides otherwise, and the final award is due within 6 months of constitution.
B. The Expedited Procedure is unavailable because the claim exceeds S$5 million.
C. The Expedited Procedure applies automatically because the claim is under S$10 million.
D. The Expedited Procedure always requires a full oral hearing.

**Answer: A.** Rule 14.2(a) allows an application where the amount exceeds S$1,000,000 but not S$10,000,000; the President decides after hearing the parties (r 14.3). Schedule 3 provides a sole arbitrator unless the President decides otherwise and a final award within 6 months. B: S$5m was the 2016 Rules threshold. C: without agreement it applies only on application. D: it is decided on documents unless a party requests a hearing or the tribunal thinks one appropriate.
*Cite: SIAC25 r 14.1–14.3, Sch 3*

### 0.XV Interim measures — drills

Drills 73–80 cover 0.XV.1, 0.XV.2, 0.XV.3, 0.XV.4, 0.XV.5, 0.XV.8, 0.XV.9 and 0.XV.10.

### 0.XV.1 — Tribunal's powers (s 12(1) IAA); orders are not awards

**Qdrill-73** · `0.XV.1` · drill-73 · `drp-m-0-112`

A Singapore-seated tribunal orders R, under s 12(1) IAA, to stop pursuing related court proceedings in Indonesia. R applies to the High Court to set the order aside under Art 34 and s 24. What is the likely outcome?

A. The order is set aside, because a tribunal has no power to grant interim injunctions.
B. The court will hear the application on its merits, because every decision of a tribunal is an "award".
C. The application fails: a s 12 order or direction is excluded from the definition of "award" in s 2(1), so the court has no jurisdiction to set it aside.
D. The application fails only because it was not brought within 30 days.

**Answer: C.** *PT Pukuafu Indah v Newmont Indonesia* held that the court had no jurisdiction to set aside such an interim order, because s 2(1) excludes s 12 orders from "award" ([19]). The permission requirement for enforcement under s 12(6) gives residual protection ([27]). A: s 12(1)(i) empowers interim injunctions. B: the definition excludes s 12 orders. D: there is no setting-aside jurisdiction at all, so no time limit question arises.
*Cite: IAA ss 2(1), 12(1)(i); PT Pukuafu Indah v Newmont Indonesia [2012] SGHC 187 at [19], [27]*

### 0.XV.2 — Enforcing a Singapore tribunal's orders (s 12(6))

**Qdrill-74** · `0.XV.2` · drill-74 · `drp-m-0-113`

R ignores an interim order of a Singapore-seated tribunal. C wants to enforce it in Singapore. Which statement is CORRECT?

A. The order is enforceable automatically as a court order, without any application to the court.
B. With the High Court's permission the order is enforceable as if it were a court order, and forum non conveniens arguments are ill-suited to resisting enforcement.
C. The order must be enforced as a foreign award under Part III.
D. The court will review the merits of the order before granting permission.

**Answer: B.** Under s 12(6), orders and directions of the tribunal are enforceable as court orders with the High Court's permission, and judgment may be entered in their terms. In *CXG v CXI* forum non conveniens principles were held ill-suited to enforcing interim measures from a Singapore seat, and the court does not look at the merits. A: permission is needed. C: Part III is for awards made outside Singapore. D: no merits review.
*Cite: IAA s 12(6); CXG v CXI [2023] SGHC 244 at [31], [33], [37], [61]–[63]*

### 0.XV.3 — Model Law 1985 Art 17; the 2006 regime is not in force

**Qdrill-75** · `0.XV.3` · drill-75 · `drp-m-0-114`

Which statement about tribunal-ordered interim measures in a Singapore-seated IAA arbitration is NOT TRUE?

A. Unless otherwise agreed, the tribunal may order a party to take an interim measure it considers necessary on the subject matter of the dispute, and may require security (1985 Art 17).
B. The parties may agree that the tribunal has no power to order interim measures.
C. Singapore did not enact the 2006 Model Law amendments and instead relies on ss 12 and 12A IAA.
D. The tribunal may grant an ex parte preliminary order lasting 20 days under Model Law Art 17B.

**Answer: D.** Arts 17B–17C (ex parte preliminary orders with a 20-day life) are part of the 2006 amendments, which are not law in Singapore. A, B: the 1985 Art 17, which is in force. C: Singapore enacted ss 12 and 12A instead.
*Cite: MAL Art 17 (1985); MAL-2006 Arts 17–17J; IAA ss 12, 12A*

### 0.XV.4 — Emergency arbitrator (SIAC Schedule 1)

**Qdrill-76** · `0.XV.4` · drill-76 · `drp-m-0-115`

Consider these statements about an emergency arbitrator under the SIAC Rules 2025.

I. The President seeks to appoint the emergency arbitrator within 24 hours of the application.
II. The emergency arbitrator makes the order or award within 14 days of appointment, unless extended.
III. The emergency arbitrator's order ceases to bind if the tribunal is not constituted within 90 days.
IV. A Singapore-seated emergency arbitrator's order cannot be enforced by the Singapore courts, because an emergency arbitrator is not an "arbitral tribunal".

A. I and II only
B. I, II and III only
C. II and III only
D. I, II, III and IV

**Answer: B.** I, II and III state Schedule 1. D: IV is wrong; under IAA s 2(1) "arbitral tribunal" includes an emergency arbitrator, so the order is enforceable with permission under s 12(6). A and C: each leaves out a correct statement.
*Cite: SIAC25 r 12.1, Sch 1 paras 7, 12; IAA ss 2(1), 12(6)*

### 0.XV.5 — When to go to court for interim relief

**Qdrill-77** · `0.XV.5` · drill-77 · `drp-m-0-116`

Which of the following is NOT a good reason for a party to seek interim relief from a court rather than from the tribunal?

A. The tribunal has not yet been constituted and urgent relief is needed.
B. The relief will need court help anyway, such as attaching a bank account.
C. Court proceedings protect the confidentiality of the dispute better than arbitration does.
D. The parties have agreed to remove the tribunal's power to order interim measures.

**Answer: C.** Loss of confidentiality is the downside of going to court, not a reason to go there. A, B, D: these are recognised reasons, together with the risk that a tribunal's interim measure may not be enforceable abroad under the NYC. In Singapore, s 12A(6) means the court acts only where the tribunal or institution cannot act effectively, so an emergency arbitrator should be considered first.
*Cite: MAL Art 17; IAA s 12A(6)*

### 0.XV.8 — Urgency and balance of convenience (KBP; Maldives Airports)

**Qdrill-78** · `0.XV.8` · drill-78 · `drp-m-0-119`

Which statement is CORRECT?

A. A delay of five months before applying for urgent relief under s 12A(4) automatically defeats urgency.
B. Urgency is judged by whether the situation justified the application, taking into account what was known of the dissipation risk and any limits on the emergency arbitrator's powers, not by the length of the delay.
C. In *Maldives Airports v GMR Male* the Court of Appeal upheld a broadly worded injunction even though its terms were vague.
D. In *Maldives Airports* the test for the injunction was whether the applicant showed irreparable harm and a strong prima facie case, not the balance of convenience.

**Answer: B.** *KBP Biosciences v Novo Nordisk* at [83]; at [82] a 5–7 month gap did not defeat urgency where the applicants did not know the relevant facts earlier. A: wrong for the same reason. C: the injunction was set aside: damages were adequate, its terms were vague, and it needed unacceptable supervision abroad ([54]–[62]). D: the test was the balance of convenience ([53]).
*Cite: KBP Biosciences v Novo Nordisk [2026] SGCA(I) 2 at [82]–[83]; Maldives Airports v GMR Male International Airport [2013] SGCA 16 at [53]–[62]*

### 0.XV.9 — Asking a court for interim relief is not a waiver (Art 9)

**Qdrill-79** · `0.XV.9` · drill-79 · `drp-m-0-120`

Before the tribunal is constituted in a Singapore-seated SIAC arbitration, C obtains an interim injunction from the High Court. R says C has waived the arbitration agreement. Which statement is CORRECT?

A. There is no waiver: asking a court for an interim measure is not incompatible with the arbitration agreement, but under the SIAC Rules C must promptly notify the application and decision to the tribunal and the Registrar.
B. C has waived the arbitration agreement by taking a step in court proceedings.
C. There is no waiver only if R consented in writing to the court application.
D. There is no waiver, and C need not tell anyone about the court order.

**Answer: A.** Model Law Art 9 provides that a party may ask a court for an interim measure before or during the arbitration without that being incompatible with the arbitration agreement. SIAC25 r 45.2 is to the same effect but requires prompt notification to the tribunal and Registrar. B: contrary to Art 9. C: no consent is required. D: ignores r 45.2.
*Cite: MAL Art 9; SIAC25 r 45.2*

### 0.XV.10 — Enforcing foreign interim orders and emergency awards (s 27(1))

**Qdrill-80** · `0.XV.10` · drill-80 · `drp-m-0-121`

An emergency arbitrator in a Hong Kong-seated arbitration makes an award ordering R to preserve assets. C seeks to enforce it in Singapore. Which statement is CORRECT?

A. It cannot be enforced in Singapore, because the New York Convention covers only final awards.
B. It can be enforced only under s 12(6) IAA, as an order of a Singapore tribunal.
C. Only orders for security for costs or discovery count as foreign awards under Part III.
D. For Part III, "arbitral award" includes a foreign tribunal's order on the s 12(1)(c)–(j) matters, so it can be enforced as a foreign award, subject to the s 31 refusal grounds.

**Answer: D.** Section 27(1) extends "arbitral award" for Part III to orders and directions on the s 12(1)(c)–(j) matters, so foreign interim orders and emergency awards are enforceable as foreign awards, subject to s 31 (*CVG v CVH*, where enforcement was ultimately refused because CVH could not present its case). A: the NYC point is a problem elsewhere, but s 27(1) solves it in Singapore. B: s 12(6) is for Singapore-seated tribunals. C: s 12(1)(a)–(b) are precisely the matters not covered.
*Cite: IAA s 27(1); CVG v CVH [2022] SGHC 249 at [1]–[2]*

### 0.XVI Anti-suit injunctions — drills

Drills 81–82 cover 0.XVI.2 and 0.XVI.3.

### 0.XVI.2 — Source of the power and the court's attitude

**Qdrill-81** · `0.XVI.2` · drill-81 · `drp-m-0-123`

What is the source of the Singapore court's power to grant an anti-suit injunction in aid of arbitration, and what is its attitude once it finds an arbitration agreement exists?

A. Section 12(1)(i) IAA; the court is reluctant to interfere with foreign proceedings.
B. Section 6 IAA; the court will only stay local proceedings and never restrain foreign ones.
C. Civil Law Act s 4(10); once satisfied there is an arbitration agreement, the court has a duty to uphold it and prevent any breach of it.
D. Model Law Art 9; the court may grant the injunction only with the tribunal's permission.

**Answer: C.** The power comes from Civil Law Act s 4(10) (*R1 International v Lonstroff*, reversed on other grounds). In *WSG Nimbus* the court said it has a duty to uphold the arbitration agreement and prevent any breach of it, reflecting the IAA's purpose of facilitating Singapore-seated arbitration. A: s 12(1)(i) is the tribunal's power to order interim injunctions. B: s 6 is the stay provision, and the court does restrain foreign proceedings. D: Art 9 deals with whether seeking court interim measures is compatible with the arbitration agreement.
*Cite: Civil Law Act s 4(10); R1 International v Lonstroff [2014] SGHC 69; WSG Nimbus v Board of Control for Cricket in Sri Lanka [2002] SGHC 104 at [90]–[91]*

### 0.XVI.3 — Enforceability abroad; UniCredit

**Qdrill-82** · `0.XVI.3` · drill-82 · `drp-m-0-124`

Which statement about anti-suit injunctions and *UniCredit Bank v RusChemAlliance* is CORRECT?

A. In *UniCredit* the UK Supreme Court granted an anti-suit injunction to protect a France-seated arbitration whose only English link was the English law governing the arbitration agreement; Singapore's apex courts have not yet considered this approach.
B. *UniCredit* is a Singapore Court of Appeal decision binding on the Singapore courts.
C. A Singapore anti-suit injunction binds the foreign court, which must stay its proceedings.
D. In *UniCredit* the UK Supreme Court refused an injunction because England was not the seat.

**Answer: A.** *UniCredit* is a UK Supreme Court decision granting an ASI for a French-seated arbitration, linked to England only by English law governing the arbitration agreement; Singapore's apex courts have not yet considered it. B: it is an English decision. C: an ASI acts only through the court's coercive power over the party, and a foreign court may ignore it; enforceability abroad depends on that country's law. D: the injunction was granted.
*Cite: UniCredit Bank v RusChemAlliance [2024] UKSC 15*

### 0.XVII The award — drills

Drills 83–92 cover 0.XVII.1, 0.XVII.2, 0.XVII.3, 0.XVII.4, 0.XVII.5, 0.XVII.6, 0.XVII.7, 0.XVII.8, 0.XVII.9 and 0.XVII.11.

### 0.XVII.1 — Decision-making cannot be delegated

**Qdrill-83** · `0.XVII.1` · drill-83 · `drp-m-0-126`

A sole arbitrator lets the tribunal secretary draft the reasoning on the main issue and signs the award without independently assessing it. Which statement is CORRECT?

A. Delegation is permissible as long as the parties were told a secretary had been appointed.
B. The test, from *Neale v Richardson*, is whether the secretary was legally qualified.
C. Improper delegation can be challenged only under the public policy ground in Art 34(2)(b)(ii).
D. The duty to decide cannot be delegated; the test is whether the arbitrator exercised their own judgment in accepting or rejecting the advice, and improper delegation may found a challenge under Art 34(2)(a)(iv).

**Answer: D.** The duty to decide is non-delegable (*Neale v Richardson*). The test for excessive delegation is whether the arbitrator exercised their own judgment (*Anderson v Wallace*). Improper delegation may make the award challengeable as not in accordance with the agreed procedure, or as made by an improperly constituted tribunal (Art 34(2)(a)(iv)). A: notice of a secretary does not permit delegating the decision. B: misstates both the case and the test. C: the usual route is Art 34(2)(a)(iv).
*Cite: Neale v Richardson; Anderson v Wallace; MAL Art 34(2)(a)(iv)*

### 0.XVII.2 — Remedies and interest (s 12(5), s 20 IAA)

**Qdrill-84** · `0.XVII.2` · drill-84 · `drp-m-0-127`

Which statement about remedies and interest in a Singapore-seated IAA arbitration is NOT TRUE?

A. The tribunal may award any remedy the High Court could have ordered in civil proceedings.
B. The tribunal may award interest on sums paid before the award, and on costs.
C. The tribunal may award only simple interest; compound interest is reserved to the court.
D. Unless the award says otherwise, a sum awarded carries interest from the date of the award at the judgment-debt rate.

**Answer: C.** Section 20(1) allows simple or compound interest from any date, at any rate and with any rest. A: s 12(5)(a). B: s 20(1). D: s 20(3).
*Cite: IAA ss 12(5)(a), 20(1), 20(3); SIAC25 r 51.5*

### 0.XVII.3 — Costs

**Qdrill-85** · `0.XVII.3` · drill-85 · `drp-m-0-128`

Consider these statements about costs.

I. In *VV v VW*, a costs award so disproportionate as to breach public policy was set aside, because proportionality in assessing costs is part of Singapore public policy.
II. Costs directed by an award are assessable by the Registrar of SIAC unless the award says otherwise.
III. In *DKB v DKC* the SICC refused costs to a successful stay applicant whose conduct showed no intention to arbitrate.
IV. The tribunal may order each party to bear its own costs.

A. II and III only
B. I, II and IV only
C. II, III and IV only
D. I, II, III and IV

**Answer: C.** II is IAA s 21; III is *DKB v DKC*; IV reflects the usual options (loser pays, proportional allocation, or each party bears its own). B and D: I is wrong; in *VV v VW* the award was not set aside, because proportionality in assessing arbitration costs is not part of Singapore public policy. A: leaves out IV.
*Cite: VV v VW [2008] SGHC 11 at [31]; DKB v DKC [2025] SGHC(I) 21 at [30]–[31]; IAA s 21; SIAC25 r 51.4*

### 0.XVII.4 — What counts as an "award" (s 2(1) IAA)

**Qdrill-86** · `0.XVII.4` · drill-86 · `drp-m-0-129`

A Singapore-seated tribunal issues a document titled "Partial Award" ordering R to make monthly payments pending a final assessment, which the tribunal may vary. R applies to set it aside. Which statement is CORRECT?

A. It is not an "award": substance, not the title, decides, and a provisional decision that does not finally dispose of an issue and can be varied is not an award, so it cannot be set aside.
B. It is an award, because the tribunal called it a "Partial Award".
C. It is an award, because every interim or interlocutory decision of a tribunal is an award.
D. It is an award, but only if it is also enforceable under the New York Convention.

**Answer: A.** Section 2(1) defines an award as a decision on the substance of the dispute, and substance rather than the title decides (*PT Asuransi* at [70]). In *DLS v DLT* an order for "Monthly Payments" pending final assessment was provisional, capable of variation, and not an award ([22], [27]). B: the label does not decide. C: interim awards must still decide the substance finally; s 12 orders are excluded. D: NYC enforceability is a consequence of being an award, not a test for it.
*Cite: IAA s 2(1); PT Asuransi v Dexia [2006] SGCA 41 at [70]; DLS v DLT [2025] SGHC 61 at [19], [22], [27]*

### 0.XVII.5 — Types of award (s 19A IAA)

**Qdrill-87** · `0.XVII.5` · drill-87 · `drp-m-0-130`

In a Singapore-seated IAA arbitration, the tribunal issues a partial award on liability, received on 1 February, and a final award on quantum, received on 1 September. In October the losing party applies to set aside the liability findings. Which statement is CORRECT?

A. The application is in time, because the 3 months run from receipt of the final award for every award in the arbitration.
B. A tribunal may make only one award, so the partial award is void.
C. The application is in time, because a partial award cannot be set aside until the final award is made.
D. The application is out of time: the tribunal may make more than one award on different aspects, and the time to set aside each award runs from its receipt.

**Answer: D.** Unless otherwise agreed, s 19A lets the tribunal make more than one award at different times on different aspects; interim and partial awards dispose of issues or claims before the rest (*PT Perusahaan Gas Negara v CRW* at [45]–[47]). Time to set aside each award runs from its receipt, so for the liability award it expired 3 months after 1 February. A, C: wrong for that reason. B: contrary to s 19A.
*Cite: IAA s 19A; PT Perusahaan Gas Negara v CRW Joint Operation [2015] SGCA 30 at [45]–[47]; MAL Art 34(3)*

### 0.XVII.6 — Finality, functus officio and res judicata (s 19B IAA)

**Qdrill-88** · `0.XVII.6` · drill-88 · `drp-m-0-131`

Which statement is CORRECT?

A. Once an award is delivered, the tribunal may revise its findings whenever new evidence appears.
B. A tribunal becomes functus officio only on making its final award, never on issues decided in an interim or partial award.
C. In *CIX v DGN*, the Court of Appeal held that the extended doctrine of res judicata can apply even without identity of parties, where the earlier proceedings were an arbitration and the later ones a court action.
D. An award binds only the named parties, never those claiming through them.

**Answer: C.** *CIX v DGN* applied the extended (*Henderson v Henderson*) doctrine, which bars points that could with reasonable diligence have been raised earlier, without identity of parties, looking at substance to stop repackaged claims against new parties. A: except under Arts 33 and 34(4), the tribunal must not vary, amend, correct, review, add to or revoke the award (s 19B(2)–(3)). B: a tribunal is functus on the issues any award decides, whether interim, partial or final (*Bloomberry* [2021] SGCA 94 at [157]). D: s 19B(1) binds the parties and those claiming through them.
*Cite: IAA s 19B; CIX v DGN [2025] SGCA 10 at [56]–[57], [66], [68]–[69]; Bloomberry Resorts v Global Gaming Philippines [2021] SGCA 94 at [157]*

### 0.XVII.7 — Form and content (Art 31; SIAC r 52)

**Qdrill-89** · `0.XVII.7` · drill-89 · `drp-m-0-132`

In a three-member Singapore-seated tribunal, one co-arbitrator refuses to sign the final award. Which statement is CORRECT?

A. The signatures of the majority suffice, provided the reason for the omitted signature is stated.
B. The award is invalid unless all three arbitrators sign it.
C. The award need not state the place of arbitration if all parties know it.
D. The award need not state reasons unless a party asks for them.

**Answer: A.** Art 31(1) requires a written, signed award, but with more than one arbitrator the majority's signatures suffice if the reason for any omitted signature is stated. B: contrary to Art 31(1). C: the award must state its date and the place of arbitration, and is deemed made there (Art 31(3)). D: reasons are required unless the parties agree otherwise or it is a consent award (Art 31(2)).
*Cite: MAL Art 31(1)–(3); SIAC25 r 52*

### 0.XVII.8 — Majority decisions (Art 29; SIAC r 51.2)

**Qdrill-90** · `0.XVII.8` · drill-90 · `drp-m-0-133`

In a three-member SIAC tribunal under the 2025 Rules, each arbitrator reaches a different figure on quantum and no majority can be formed. What happens?

A. The tribunal must resign and a new tribunal is constituted.
B. The presiding arbitrator alone makes the award.
C. The SIAC Court decides quantum.
D. The lowest figure prevails as the de facto majority.

**Answer: B.** Under SIAC25 r 51.2, failing a majority the presiding arbitrator alone makes the award. Under Model Law Art 29 decisions are by majority unless otherwise agreed, and the presiding arbitrator may decide procedural questions only if authorised; the SIAC Rules fill the gap where no majority exists. A, C, D: no such rule exists. If an arbitrator refuses to take part after a reasonable opportunity, the others may proceed and must give reasons (r 51.3).
*Cite: MAL Art 29; SIAC25 r 51.2–51.3*

### 0.XVII.9 — Time limits and SIAC scrutiny

**Qdrill-91** · `0.XVII.9` · drill-91 · `drp-m-0-134`

Which statement about the timing and scrutiny of awards under SIAC25 r 53 is NOT TRUE?

A. The tribunal submits the draft award within 90 days of the last submission, unless the Registrar decides otherwise.
B. The Registrar may suggest changes to the form of the award and draw attention to points of substance.
C. No award may be issued until the Registrar has approved it as to form.
D. The Registrar must approve the tribunal's decision on the merits before the award is issued.

**Answer: D.** The Registrar's scrutiny approves only the form. On substance the Registrar may only point out matters, and the decision remains the tribunal's. A, B, C: r 53. Where a time limit is missed, views differ on whether the mandate ends; in *Alphamix* the parties' conduct showed a tacit agreement to extend, so an award 3 days late stood.
*Cite: SIAC25 r 53; Alphamix v District Council of Rivière du Rempart [2023] UKPC 20*

### 0.XVII.11 — Interpretation of the award (Art 33(1)(b))

**Qdrill-92** · `0.XVII.11` · drill-92 · `drp-m-0-136`

A Singapore-seated ad hoc award is ambiguous on one point. Twenty days after receiving it, C asks the tribunal to interpret that point. The parties never agreed to allow requests for interpretation. Which statement is CORRECT?

A. The tribunal must interpret the point within 60 days of the request.
B. The tribunal may interpret the point on its own initiative within 30 days of the award.
C. Interpretation is available only if the parties so agreed, so the tribunal cannot entertain C's request.
D. C may request an interpretation at any time before enforcement.

**Answer: C.** Under Art 33(1)(b) interpretation of a specific point is available only "if so agreed by the parties". Where it is available, the request is made within 30 days of receipt and the interpretation given within 30 days, and it forms part of the award. A: 60 days is the period for an additional award (Art 33(3)). B: the own-initiative power (Art 33(2)) is for correcting errors, not interpretation. D: there is a 30-day limit.
*Cite: MAL Art 33(1)(b), (2), (3)*

### 0.XVIII Setting aside the award — drills

Drills 93–97 cover 0.XVIII.9, 0.XVIII.10, 0.XVIII.11, 0.XVIII.13 and 0.XVIII.15.

### 0.XVIII.9 — Copied awards (DJP v DJO)

**Qdrill-93** · `0.XVIII.9` · drill-93 · `drp-m-0-146`

Which statement about an award that copies material from elsewhere is CORRECT?

A. Copying alone does not taint an award; the court looks at its nature, extent and effect, and copying from one party's submissions is tested by whether it gives rise to a reasonable suspicion that the tribunal adopted that party's case without engaging fairly with both sides.
B. Any copying from a related award is automatically fatal and requires the award to be set aside.
C. Copying is at most an error of law, which cannot be a ground to set aside.
D. In *DJO v DJP* the SICC upheld the award, holding that copying is irrelevant to natural justice.

**Answer: A.** *DJO v DJP* at [98], [114]–[115]; on appeal (*DJP v DJO*) the CA distinguished copying from one party's submissions and copying from a related award ([40]–[46]). B: copying uncontroversial material from a related award may be acceptable; proximity matters. C: copying can found apparent bias or prejudgment, a natural justice concern. D: the SICC set the award aside.
*Cite: DJO v DJP [2024] SGHC(I) 24 at [98], [114]–[115]; DJP v DJO [2025] SGCA(I) 2 at [40]–[46], [61]–[63], [71], [74]*

### 0.XVIII.10 — Inadequate reasons are not a ground (CVV v CWB)

**Qdrill-94** · `0.XVIII.10` · drill-94 · `drp-m-0-147`

A party says the reasons in a Singapore-seated award are thin and fall below the judicial standard. Which statement is CORRECT?

A. Inadequate reasons are a breach of natural justice and always justify setting aside under s 24(b).
B. Arbitrators must give reasons to the same standard as a High Court judge.
C. Inadequate reasons are, without more, an error of law that cannot sustain a challenge; the Court of Appeal left open whether a complete failure to give reasons under Art 31(2) is itself a ground.
D. The Court of Appeal decided that a complete failure to give reasons is never a ground to set aside.

**Answer: C.** *CVV v CWB* at [33]–[35] treats inadequate reasons as an error of law, which is not a setting-aside ground; at [32] the CA said the Art 31(2) question is unsettled and did not decide it. A: no automatic natural justice breach. B: no judicial standard applies. D: the point was left open, not decided.
*Cite: CVV v CWB [2023] SGCA(I) 9 at [32]–[35]; MAL Art 31(2)*

### 0.XVIII.11 — No court intervention mid-arbitration (Art 5; DMZ v DNA)

**Qdrill-95** · `0.XVIII.11` · drill-95 · `drp-m-0-148`

During a Singapore-seated arbitration, the tribunal makes a procedural determination on the date the arbitration commenced. R immediately applies to the High Court to set that determination aside. Which statement is CORRECT?

A. The court may review any procedural ruling at any time under its inherent supervisory jurisdiction.
B. R may challenge the ruling within 30 days under Art 16(3).
C. The court will set the ruling aside if it would have decided the procedural point differently.
D. Art 5 bars court intervention in matters governed by the Model Law except where it provides; "matter" is read broadly to include procedural determinations in an ongoing arbitration, so the application fails.

**Answer: D.** *DMZ v DNA* applies a two-step inquiry under Art 5: (a) whether the application concerns a "matter" governed by the Model Law, read broadly; (b) whether intervention is permitted ([28], [35]–[36], [43]). Absent agreement on the procedural point, the parties must arbitrate in accordance with the tribunal's determinations, and the court will not second-guess them ([46]). A, C: contrary to Art 5. B: Art 16(3) concerns rulings on jurisdiction, not procedure.
*Cite: MAL Art 5; DMZ v DNA [2025] SGCA 52 at [28], [35]–[36], [43], [46]*

### 0.XVIII.13 — Court's discretion not to set aside

**Qdrill-96** · `0.XVIII.13` · drill-96 · `drp-m-0-150`

An applicant proves a procedural irregularity within Art 34(2)(a)(iv), but the irregularity could not have affected the outcome. Which statement is CORRECT?

A. The court must set aside the award once any Art 34(2) ground is made out.
B. Art 34(2) provides that the court "may" set aside, so it keeps a discretion to refuse even where a ground is made out, for example where the breach could not have affected the outcome.
C. The court may refuse only if the applicant has also missed the 3-month time limit.
D. The court must remit the award to the tribunal instead of setting it aside.

**Answer: B.** The word "may" in Art 34(2) preserves a residual discretion not to set aside. A: the provision is permissive, not mandatory. C: the time limit is a separate bar. D: remission under Art 34(4) is available only on a party's request and where appropriate; it is not mandatory.
*Cite: MAL Art 34(2), (4)*

### 0.XVIII.15 — A foreign award cannot be set aside in Singapore

**Qdrill-97** · `0.XVIII.15` · drill-97 · `drp-m-0-152`

An LCIA award is made in a London-seated arbitration. The award creditor seeks enforcement in Singapore. The debtor wants the award set aside by the Singapore High Court. What are the debtor's options in Singapore?

A. It cannot set the award aside in Singapore, because setting aside is available only at the seat; it may resist enforcement under s 31, or ask for an adjournment while the seat court decides a challenge there (s 31(5)).
B. It may apply under Art 34 within 3 months of receiving the award.
C. It may apply under s 24 IAA for breach of natural justice.
D. It has no options in Singapore, and must pay and then sue in London.

**Answer: A.** Setting aside is available only from a court at the seat (Art 1(2)), so a Singapore court cannot set aside a London award. In Singapore the debtor may resist enforcement under s 31 or seek an adjournment pending a seat challenge under s 31(5). B, C: Art 34 and s 24 apply only to Singapore-seated awards. D: it may resist enforcement.
*Cite: MAL Art 1(2); IAA s 31, s 31(5)*

### 0.XIX Enforcement and resisting enforcement — drills

Drills 98–107 cover 0.XIX.4, 0.XIX.5, 0.XIX.6, 0.XIX.7, 0.XIX.8, 0.XIX.10, 0.XIX.11, 0.XIX.12, 0.XIX.14 and 0.XIX.16.

### 0.XIX.4 — Foreign awards: meaning and recognition (ss 27, 29 IAA)

**Qdrill-98** · `0.XIX.4` · drill-98 · `drp-m-0-156`

Consider these statements about "foreign awards" under Part III of the IAA.

I. An award in a Singapore-seated arbitration between two foreign companies is a "foreign award".
II. A foreign award may be enforced in the High Court by action, or in the same manner as an award under s 19.
III. A foreign award may be relied on by way of defence or set-off in Singapore proceedings.
IV. A "foreign award" is one made under an arbitration agreement in the territory of a Convention country other than Singapore.

A. II and III only
B. II, III and IV only
C. I, II and III only
D. I, II, III and IV

**Answer: B.** II is s 29(1), III is s 29(2) and IV is s 27(1). C and D: I is wrong; the test is the place where the award is made, and a Singapore-seated award is not a foreign award, whatever the parties' nationality. A: leaves out IV.
*Cite: IAA ss 27(1), 29(1)–(2)*

### 0.XIX.5 — Documents the enforcing party must produce (s 30; Art IV)

**Qdrill-99** · `0.XIX.5` · drill-99 · `drp-m-0-157`

A creditor seeks to enforce a Chinese-language award made in Shanghai. Which document is NOT required under s 30 IAA?

A. The duly authenticated original award, or a duly certified copy.
B. The original arbitration agreement, or a duly certified copy.
C. A certificate from the seat court confirming that the award has not been set aside.
D. A certified English translation of the award.

**Answer: C.** Section 30(1) (NYC Art IV) requires only the authenticated original award or a certified copy, the original arbitration agreement or a certified copy, and a certified English translation if either is in a foreign language. On mere production they are prima facie evidence of what they record (s 30(2)). A setting-aside at the seat is for the debtor to prove under s 31(2)(f), and the creditor need not prove it has not happened.
*Cite: IAA ss 30(1)–(2), 31(2)(f); NYC Art IV*

### 0.XIX.6 — Procedure: permission without notice, then 14 days (ROC O 48)

**Qdrill-100** · `0.XIX.6` · drill-100 · `drp-m-0-158`

A creditor obtains permission to enforce a foreign award in Singapore on a without-notice application. The order is served on the debtor in Singapore on 1 June. Within what period may the debtor apply to set aside the order?

A. Within 3 months of receiving the award.
B. Within 30 days of service of the order.
C. Within 14 days of the date of the award.
D. Within 14 days of service of the order; the award may not be enforced in the meantime.

**Answer: D.** Under ROC O 48 r 6 the debtor may apply within 14 days of service, or a period the court fixes if the order is served out of Singapore, and the award may not be enforced until that period expires or any application is disposed of. Enforcement has two stages: a without-notice application for permission, then the debtor's challenge (*Hulley v Russia* at [30]–[31]). A: 3 months is the Art 34(3) setting-aside limit. B: wrong period. C: time runs from service of the order, not from the award.
*Cite: ROC O 48 r 6; Hulley Enterprises v Russian Federation [2025] SGHC(I) 27 at [30]–[31]*

### 0.XIX.7 — Grounds the award debtor must prove (s 31(2))

**Qdrill-101** · `0.XIX.7` · drill-101 · `drp-m-0-159`

Resisting enforcement of a Bangkok award in Singapore, the debtor says it never entered into a valid arbitration agreement. The parties chose no law to govern the agreement. Which statement is CORRECT?

A. The debtor must prove under s 31(2)(b) that the agreement is not valid under the law the parties chose or, failing that, the law of the country where the award was made (Thailand).
B. The creditor must prove that the agreement is valid under Singapore law.
C. The court must refuse of its own motion under s 31(4) if it doubts the agreement's validity.
D. Validity is tested under the law of Singapore, as for setting aside under Art 34(2)(a)(i).

**Answer: A.** Section 31(2)(b) (NYC Art V(1)(a)) is the ground for a debtor saying there was no valid agreement, i.e. no jurisdiction. The debtor bears the burden, and the default law is that of the country where the award was made. B: the burden is on the debtor. C: s 31(4) covers only non-arbitrability and public policy. D: the Singapore-law default applies when setting aside a Singapore award under Art 34(2)(a)(i), not when resisting enforcement of a foreign award.
*Cite: IAA s 31(1)–(2)(b), s 31(4); NYC Art V(1)(a)*

### 0.XIX.8 — Grounds the court may raise itself (s 31(4))

**Qdrill-102** · `0.XIX.8` · drill-102 · `drp-m-0-160`

A foreign award is said to conflict with a public policy peculiar to State X, where the award was made, but not with any Singapore public policy. Which statement is CORRECT?

A. The Singapore court must refuse enforcement under s 31(4)(b), because public policy is judged by the law of the seat.
B. The court may consider public policy only if the debtor pleads and proves it.
C. Section 31(4)(b) asks whether enforcement would be contrary to the public policy of Singapore, so State X's peculiar public policy is not a ground.
D. Section 31(4) lists four grounds, including fraud and lack of jurisdiction.

**Answer: C.** Under s 31(4) (NYC Art V(2)) the court may refuse enforcement if the subject matter is not arbitrable under Singapore law, or if enforcement would be contrary to Singapore public policy. It applies its own State's public policy, not one peculiar to another State. A: wrong law. B: the court may raise these grounds itself. D: s 31(4) has only two grounds.
*Cite: IAA s 31(4)(a)–(b); NYC Art V(2)*

### 0.XIX.10 — Fresh examination, but no review of the merits

**Qdrill-103** · `0.XIX.10` · drill-103 · `drp-m-0-162`

Resisting enforcement in Singapore, a debtor argues both that it never agreed to arbitrate and that the tribunal misapplied the governing law of the contract. Which statement is CORRECT?

A. The court must defer to the tribunal's findings on both points.
B. The court may examine afresh whether there was a valid arbitration agreement, but it cannot review the tribunal's errors of law or fact on the merits.
C. The court may review both points afresh, because enforcement is a full rehearing.
D. The court may review the merits, but not the tribunal's jurisdiction.

**Answer: B.** The enforcement court is entitled to examine afresh the issues said to establish a ground of refusal, such as the existence of a valid arbitration agreement (*PT First Media* at [164]). It cannot review the merits, because errors of law or fact are final (*PT Asuransi* at [57]). A: no deference is owed on the jurisdictional ground. C: the merits are not reopened. D: the reverse is true.
*Cite: PT Asuransi v Dexia [2006] SGCA 41 at [57]; PT First Media v Astro [2013] SGCA 57 at [164]*

### 0.XIX.11 — Award set aside at the seat

**Qdrill-104** · `0.XIX.11` · drill-104 · `drp-m-0-163`

Which statement about enforcing an award that has been set aside at the seat is CORRECT?

A. The Singapore Court of Appeal held, as part of its ratio, that such awards must always be enforced.
B. In *Hilmarton*, a US court enforced an award that had been set aside in Egypt.
C. Section 31(2)(f) IAA applies only where the award was set aside by a Singapore court.
D. The Singapore Court of Appeal said, obiter, that Singapore courts will not enforce a foreign award set aside at the seat, because the erga omnes effect of annulment leaves no award to enforce.

**Answer: D.** *PT First Media* at [76]–[77] (obiter). Enforcement may be refused under s 31(2)(f) (NYC Art V(1)(e)) if the award was set aside or suspended by a competent court of the seat. A: the remark was obiter, and to the opposite effect. B: the cases are swapped; in *Hilmarton* France enforced an award set aside in Switzerland, and in *Chromalloy* the US enforced one set aside in Egypt. C: s 31(2)(f) refers to the country in which, or under whose law, the award was made.
*Cite: IAA s 31(2)(f); PT First Media v Astro [2013] SGCA 57 at [76]–[77]; Hilmarton; Chromalloy*

### 0.XIX.12 — Transnational issue estoppel (Deutsche Telekom)

**Qdrill-105** · `0.XIX.12` · drill-105 · `drp-m-0-164`

Consider these statements about transnational issue estoppel.

I. A seat court's earlier decision on the validity of an award can bind the parties in Singapore enforcement proceedings, so they cannot relitigate issues it decided.
II. The "primacy principle" was the unanimous ratio of *Republic of India v Deutsche Telekom*.
III. The elements include that the foreign judgment is capable of recognition in Singapore, the same parties, and the same subject matter.
IV. In *Hulley Enterprises v Russian Federation* Russia was estopped by the Dutch courts' decisions.

A. I and III only
B. I, II and IV only
C. I, III and IV only
D. I, II, III and IV

**Answer: C.** I and III state *Deutsche Telekom* at [64]; IV states *Hulley* at [111], [140]. B and D: II is wrong; the primacy principle was the majority's obiter, and the concurring judge found issue estoppel and abuse of process enough. A: leaves out IV.
*Cite: Republic of India v Deutsche Telekom [2023] SGCA(I) 10 at [46] ff, [64]; Sacofa v Super Sea Cable [2024] SGHC 54 at [65]; Hulley Enterprises v Russian Federation [2025] SGHC(I) 19 at [111], [140]*

### 0.XIX.14 — Due process ground (Art V(1)(b)): what succeeds and fails

**Qdrill-106** · `0.XIX.14` · drill-106 · `drp-m-0-166`

Resisting enforcement under s 31(2)(c) IAA (NYC Art V(1)(b)), which complaint is MOST likely to succeed?

A. The tribunal decided the case on a chain of reasoning of which the parties had no reasonable notice and which had no nexus to their arguments.
B. The tribunal misunderstood my case.
C. The award did not mention my arguments, so the tribunal must have ignored them.
D. The tribunal must have overlooked part of my case because it did not engage with it in detail.

**Answer: A.** A chain of reasoning without reasonable notice or nexus to the parties' arguments has succeeded (*BZW v BZV*). So have failure to consider an important pleaded issue (*Front Row v Daimler*) and no chance to address a claim raised at the eleventh hour. B, C, D: these are the classic failed complaints, which are often disguised attacks on errors of fact or law. The threshold is high.
*Cite: IAA s 31(2)(c); BZW v BZV [2022] SGCA 1; Front Row Investment v Daimler [2010] SGHC 80*

### 0.XIX.16 — More favourable right provision (Art VII(1))

**Qdrill-107** · `0.XIX.16` · drill-107 · `drp-m-0-168`

Which statement about Art VII(1) of the New York Convention is CORRECT?

A. It requires enforcing States to apply only the Convention, displacing any domestic law on enforcing awards.
B. It overrides all bilateral treaties on enforcing awards.
C. It allows the enforcing court to refuse enforcement on any ground available in its domestic law.
D. It preserves a party's right to rely on an award as far as the law or treaties of the enforcing country allow, so a more favourable domestic regime prevails; in Singapore, Part III does not affect other ways of enforcing an award (IAA s 33(1)).

**Answer: D.** Art VII(1) is the "more favourable right" provision. The Convention does not affect other treaties on enforcement or deprive a party of more favourable rights under the enforcing country's law. A, B: the reverse is true. C: Art VII(1) favours enforcement and does not add refusal grounds.
*Cite: NYC Art VII(1); IAA s 33(1)*

## 1 · Mediation Advocacy — Drills

Part 2 for Mediation Advocacy. One drill for each of the 19 Sub-points no past paper has tested, plus 1.VII.5, tested only in passing (drills 108–127), then 12 extra drills on the seven elements (drills 128–139), the MED-4 deck Bennett missed most often in the 10 Nov quiz. Written 11 Nov 2026 from `cheatsheets.md`. Self-study only.

### 1.I Nature of mediation — drills

Drill 108 covers 1.I.6.

### 1.I.6 — The advocate's evolving role, before and during a dispute

**Qdrill-108** · `1.I.6` · drill-108 · `drp-m-1-6`

A company asks its lawyer to review a new 5-year supply contract. No dispute exists yet. Which of the following is part of the mediation advocate's role at this stage?

A. None: the mediation advocate's role begins only when a dispute is referred to mediation.
B. Advising on an ADR or multi-tier dispute resolution clause in the contract and on the duty to consider amicable resolution under ROC 2021 O 5.
C. Preparing an opening statement for a future mediation.
D. Drafting a settlement agreement with the other side's counsel.

**Answer: B.** The advocate's role now starts before any dispute: advising on ADR clauses and on the O 5 duty to consider amicable resolution. A: too narrow; the role has evolved beyond the mediation room. C and D are tasks once a dispute has arisen and a mediation is under way.
*Cite: MED-1 (see `drp-m-1-6`); ROC O 5 r 1*

### 1.II Mediation institutions and schemes — drills

Drills 109–110 cover 1.II.2 and 1.II.3.

### 1.II.2 — Singapore International Mediation Centre (SIMC)

**Qdrill-109** · `1.II.2` · drill-109 · `drp-m-1-8`

Which statement about the Singapore International Mediation Centre (SIMC) is CORRECT?

A. It was set up in 1997 to mediate community and neighbour disputes.
B. It is the approved certification scheme for mediators under the Mediation Act 2017.
C. It works with SIAC to administer the Arb-Med-Arb Protocol and is a designated mediation service provider under the Mediation Act.
D. It is a for-profit body owned by SIAC.

**Answer: C.** SIMC (2014, not-for-profit) provides mediation, administers the SIAC-SIMC Arb-Med-Arb Protocol with SIAC, and is a designated provider under MA s 7. A: 1997 is SMC; community disputes go to the CMC. B: the approved certification scheme is SIMI's. D: it is not-for-profit.
*Cite: MED-2 (see `drp-m-1-8`, `drp-m-1-14`); MA s 7*

### 1.II.3 — SIMI and SIDRA

**Qdrill-110** · `1.II.3` · drill-110 · `drp-m-1-9`

Which pairing is CORRECT?

A. SIMI: research, training and consultancy on negotiation; SIDRA: mediator credentialing.
B. SIMI: mediation standards and credentialing (the approved certification scheme under the Mediation Act); SIDRA: research, training and consultancy on mediation and negotiation.
C. SIMI: designated mediation service provider; SIDRA: court-annexed mediation.
D. SIMI and SIDRA are both divisions of the State Courts.

**Answer: B.** SIMI (2014) sets and enforces mediation standards and runs the credentialing scheme approved under the Mediation Act ("SIMI Certified Mediator"); SIDRA (2016) is an academy for research, training and consultancy. A swaps them. C: neither is a designated provider or a court. D: both are independent not-for-profits.
*Cite: MED-2 (see `drp-m-1-9`)*

### 1.III Legal sources and the basis of mediation — drills

Drills 111–112 cover 1.III.1 and 1.III.2.

### 1.III.1 — Sources of mediation law in Singapore

**Qdrill-111** · `1.III.1` · drill-111 · `drp-m-1-15`

Which of the following are sources of mediation law in Singapore?

I. The Mediation Act 2017 and the Community Mediation Centres Act 1997.
II. The Mediation Rules 2017 and the Legal Profession (Professional Conduct) Rules 2015.
III. The Practice Directions of the Supreme Court, State Courts and Family Justice Courts.
IV. Case law such as *UJN v UJO* and *Legis Point v Tay Choon Ai*.

A. I and II only
B. I, II and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: D.** Mediation law comes from statutes (I), subsidiary legislation (II), practice directions (III) and case law (IV).
*Cite: MED-3 p5–8 (see `drp-m-1-15`)*

### 1.III.2 — Mediation by agreement; stay pending ADR

**Qdrill-112** · `1.III.2` · drill-112 · `drp-m-1-16` `drp-m-1-31`

A and B's contract says disputes "shall first be referred to mediation at SMC". A sues B in the General Division without mediating. B wants the court action paused. What is B's best course?

A. Apply under s 6 of the International Arbitration Act, which makes a stay mandatory.
B. Apply for a stay under s 8 of the Mediation Act 2017; the court may stay on such terms as it thinks fit.
C. Do nothing: a mediation clause is unenforceable as an agreement to agree.
D. Apply to strike out the claim as an abuse of process because mediation is a condition precedent to suit.

**Answer: B.** A party to a mediation agreement may apply for a stay of court proceedings brought in breach of it (MA s 8(1)); the stay is discretionary (s 8(2)), as in *Cable & Wireless v IBM*. A: the IAA applies to arbitration agreements only. C: a clear obligation to mediate is enforceable, even by specific performance (*Maxx Engineering* [2023] SGHC 71). D: a stay, not striking out, is the remedy.
*Cite: MA s 8; [2002] EWHC 2059 (Comm); [2023] SGHC 71*

### 1.IV Duty to consider amicable resolution; costs — drills

Drills 113–116 cover 1.IV.2, 1.IV.3, 1.IV.5 and 1.IV.8.

### 1.IV.2 — Terms of an offer of amicable resolution (O 5 r 2)

**Qdrill-113** · `1.IV.2` · drill-113 · `drp-m-1-20`

Before suing, P's solicitors send D a letter offering to mediate at SMC, "open for 7 days". Which is CORRECT under ROC 2021 O 5 r 2?

A. The offer may be oral as long as it is later confirmed.
B. Unless the parties agree otherwise, the offer must be open for a reasonable period and in any case at least 14 days, so 7 days is too short.
C. The terms of the offer, if refused, may be shown to the judge at trial to show D was unreasonable.
D. An offer with no expiry date stays open indefinitely, even after the court decides the merits.

**Answer: B.** O 5 r 2(2): open for a reasonable period, in any case at least 14 days, unless otherwise agreed. A: the offer and any rejection must be in writing (r 2(1)). C: an unaccepted offer must not be made known to the Court until it has decided the merits and is dealing with costs (r 2(3)). D: absent a stated expiry, it expires once the merits are determined (r 2(4)).
*Cite: ROC 2021 O 5 r 2*

### 1.IV.3 — Court's powers: order ADR, sealed reasons for refusal (O 5 r 3)

**Qdrill-114** · `1.IV.3` · drill-114 · `drp-m-1-21`

In a General Division action the judge proposes mediation; the defendant says it does not wish to mediate. Which is CORRECT?

A. The Court cannot order ADR without both parties' consent.
B. The Court may order the defendant to submit a sealed document giving its reasons, which is opened only after the merits are decided and may be referred to on costs.
C. The defendant's reasons must be filed and served on the claimant within 7 days.
D. The Court must order a stay until mediation has taken place.

**Answer: B.** O 5 r 3(3)–(4); in the Supreme Court it is filed within 7 days as an "ADR Sealed Document", not served (SCPD 54(3)–(4)). A: the Court *may* order the parties to attempt amicable resolution (r 3(1)). C: it is sealed, not served. D: no mandatory stay.
*Cite: ROC O 5 r 3; SCPD 54(3)–(4)*

### 1.IV.5 — Supreme Court PD 53 and 54

**Qdrill-115** · `1.IV.5` · drill-115 · `drp-m-1-23`

Which of the following is NOT a requirement of Supreme Court Practice Directions paras 53–54?

A. Advocates must advise clients to consider ADR and give them enough information about the ADR options.
B. Advocates must state in the Pre-Case Conference Questionnaire whether, when and how amicable resolution was attempted.
C. A party wishing to attempt ADR files and serves an ADR Offer (Form B4), to which the other side responds (Form B5).
D. Parties must attend at least one mediation session before the first case conference.

**Answer: D.** There is no compulsory pre-conference mediation. A: SCPD 53(2). B: 53(5). C: 54(1). Advocates must also warn of adverse costs under O 21 r 4(c) (53(6)).
*Cite: SCPD 53–54 (see `drp-m-1-23`)*

### 1.IV.8 — Unreasonable refusal of ADR: Halsey and later cases

**Qdrill-116** · `1.IV.8` · drill-116 · `drp-m-1-26`

A defendant ignored three letters inviting it to mediate and then won at trial. On costs, which statement is BEST supported by the cases the courts look to?

A. A winning party can never be penalised in costs for its approach to ADR.
B. Silence in the face of an invitation to ADR is, as a general rule, itself unreasonable (*PGF II v OMFS*), and a successful party's costs may be reduced under O 21 r 4(c).
C. Refusing ADR is unreasonable only if the refusing party's case was weak.
D. Under *Halsey*, the only relevant factor is whether ADR had a reasonable prospect of success.

**Answer: B.** *PGF II* [2014] 1 WLR 1386 at [34]; ROC O 21 r 4(c) lets the court disallow or reduce a successful party's costs where it did not discharge its O 5 duty. A: wrong for that reason. C: the merits are one *Halsey* factor among several. D: *Halsey* lists six non-exhaustive factors (nature of dispute, merits, other methods tried, costs of ADR, delay, prospect of success).
*Cite: Halsey [2004] 1 WLR 3002 at [16]; [2014] 1 WLR 1386 at [34]; ROC O 21 r 4(c)*

### 1.V Mediation Act 2017 — drills

Drills 117–122 cover 1.V.1, 1.V.2, 1.V.4 and 1.V.7–1.V.9.

### 1.V.1 — Meaning of "mediation" (s 3)

**Qdrill-117** · `1.V.1` · drill-117 · `drp-m-1-28`

Under s 3 of the Mediation Act 2017, which of the following is NOT one of the things a mediator helps the parties to do?

A. Identify the issues in dispute.
B. Explore and generate options.
C. Communicate with one another.
D. Receive the mediator's binding determination of the dispute.

**Answer: D.** The mediator helps the parties (a) identify issues, (b) explore and generate options, (c) communicate, and (d) *voluntarily* reach an agreement (s 3(1)). A mediator does not decide. Sessions include preparatory and follow-up activity and may be held electronically (s 3(2)–(3)).
*Cite: MA s 3*

### 1.V.2 — Mediation agreement (s 4)

**Qdrill-118** · `1.V.2` · drill-118 · `drp-m-1-29`

X and Y agree on a phone call to mediate their dispute at SMC; X's email the same day records the terms. Is there a "mediation agreement" under the Mediation Act 2017?

A. No: a mediation agreement must be signed by both parties.
B. Yes: it must be in writing, and that is satisfied if its content is recorded in any form, even if it was concluded orally.
C. No: only a clause in a commercial contract can be a mediation agreement.
D. Yes, but only for future disputes, not an existing one.

**Answer: B.** MA s 4(3)–(4): writing is satisfied by a record of the content in any form, even if the agreement was made orally or by conduct. A: no signature requirement. C: it may be a clause or a separate agreement (s 4(2)). D: it covers existing or future disputes (s 4(1)).
*Cite: MA s 4*

### 1.V.4 — Stay of court proceedings (s 8)

**Qdrill-119** · `1.V.4` · drill-119 · `drp-m-1-31` `drp-m-0-47`

Compare a stay under s 8 of the Mediation Act 2017 with a stay under s 6 of the International Arbitration Act. Which is CORRECT?

A. Both are mandatory once their conditions are met.
B. Both are discretionary.
C. The MA stay is discretionary ("may"); the IAA stay is mandatory unless the agreement is null and void, inoperative or incapable of being performed.
D. The MA stay is mandatory; the IAA stay is discretionary.

**Answer: C.** MA s 8(2): the court *may* stay on such terms as it thinks fit. IAA s 6(2): the court "is to" stay, subject only to the null and void exception. A, B and D misstate one or both.
*Cite: MA s 8(2); IAA s 6(2)*

### 1.V.7 — Disclosure with permission of a court or tribunal (s 9(3))

**Qdrill-120** · `1.V.7` · drill-120 · `drp-m-1-34`

C wants to show a judge the mediated settlement agreement D signed, to enforce it. No exception in s 9(2) applies. Under the Mediation Act 2017, C

A. may never disclose it, because mediation communications are absolutely confidential.
B. may disclose it with the permission of the court under s 11, for the purpose of enforcing or disputing a mediated settlement agreement (s 9(3)(a)).
C. may disclose it freely, because a settlement agreement is not a mediation communication.
D. needs only D's consent, not the court's.

**Answer: B.** With permission under s 11, a mediation communication may be disclosed to enforce or dispute a mediated settlement agreement (s 9(3)(a)). A: there are exceptions. C: the s 2(1) definition expressly includes a mediated settlement agreement. D: consent of all parties is a s 9(2)(a) route, but C does not have it here; and admissibility in evidence still needs permission (s 10).
*Cite: MA ss 2(1), 9(3), 10, 11*

### 1.V.8 — Admissibility in evidence; the permission test (ss 10, 11)

**Qdrill-121** · `1.V.8` · drill-121 · `drp-m-1-35`

In deciding whether to grant permission under s 11 of the Mediation Act 2017 to admit a mediation communication in evidence, the court or tribunal must consider which of the following?

I. Whether the communication may be or has been disclosed under s 9(2).
II. Whether admission is in the public interest or the interests of the administration of justice.
III. Any other relevant circumstances or matters.
IV. Whether the mediator consents.

A. I and II only
B. I, II and III only
C. II, III and IV only
D. I, II, III and IV

**Answer: B.** s 11(2)(a)–(c). The mediator's consent is not a listed factor. Without permission, a mediation communication is inadmissible in court, arbitral or disciplinary proceedings (s 10).
*Cite: MA ss 10, 11(2)*

### 1.V.9 — Without prejudice privilege at common law

**Qdrill-122** · `1.V.9` · drill-122 · `drp-m-1-36`

Which statement about without prejudice privilege is CORRECT?

A. A statement in negotiations to settle is protected only if it is expressly labelled "without prejudice".
B. A statement made in negotiations to settle a dispute is without prejudice even if not labelled, and producing the document in court proceedings can waive the privilege.
C. Inadvertent disclosure always waives the privilege.
D. The Mediation Act 2017 abolished without prejudice privilege for mediation.

**Answer: B.** *Mariwu Industrial v Dextra Asia* [2006] SGCA 37 at [24] (no label needed); *Greenline-Onyx v Otto Systems* [2007] SGCA 25 (producing the document waived it). C: waiver needs express or implied agreement; inadvertence is not enough (*Krishna Kumaran v Kuppusamy* [2014] SGHC 158 at [22]–[23]). D: the Act adds statutory protection (ss 9–11); it does not abolish the common law.
*Cite: [2006] SGCA 37 at [24]; [2007] SGCA 25; [2014] SGHC 158 at [22]–[23]*

### 1.VI Mediated settlement agreements — drills

Drills 123–125 cover 1.VI.3, 1.VI.5 and 1.VI.6.

### 1.VI.3 — Settlement agreements in family proceedings (UJN v UJO)

**Qdrill-123** · `1.VI.3` · drill-123 · `drp-m-1-41`

Spouses settle the division of matrimonial assets at a mediation during divorce proceedings. At the ancillary matters hearing the wife says the agreement should be ignored. Which is CORRECT?

A. The court must ignore it, because only the court can divide matrimonial assets.
B. It is automatically binding as an order of court.
C. It is not to be ignored: the court considers whether it is binding and how far to give it effect (*UJN v UJO* [2018] SGFC 16).
D. It can be recorded under s 12 of the Mediation Act like any civil settlement, without restriction.

**Answer: C.** *UJN v UJO*, consistent with *Sita Jaswant Kaur* at [5]–[6]. A and B are the two extremes. D: for Family Justice Courts matters only prescribed classes of agreement can be recorded under s 12 (s 12(6)(a)).
*Cite: [2018] SGFC 16; MA s 12(6)(a)*

### 1.VI.5 — Singapore Convention on Mediation: scope and exclusions

**Qdrill-124** · `1.VI.5` · drill-124 · `drp-m-1-43`

Which settlement agreement falls within the Singapore Convention on Mediation?

A. A settlement between a Singapore employer and a Malaysian employee of an employment claim, reached at SIMC.
B. A settlement recorded as a consent award in a SIAC Arb-Med-Arb.
C. A written settlement, reached through mediation, of a supply dispute between a Singapore company and a Vietnamese company.
D. A settlement between a consumer and an online retailer of a household purchase.

**Answer: C.** The Convention covers a written agreement resulting from mediation that resolves a commercial dispute and is international (parties' places of business in different States) (Art 1(1)). A and D: employment and consumer (personal, family or household) disputes are excluded (Art 1(2)). B: settlements recorded and enforceable as arbitral awards are excluded (Art 1(3)); the consent award goes under the NYC.
*Cite: Singapore Convention Art 1; SCMA s 3*

### 1.VI.6 — Singapore Convention on Mediation Act 2020: recording and refusal

**Qdrill-125** · `1.VI.6` · drill-125 · `drp-m-1-44`

A party applies under the Singapore Convention on Mediation Act 2020 to record an international settlement agreement as an order of court. On which ground may the High Court refuse **of its own motion**, without the resisting party proving it?

A. A party was under some incapacity.
B. The mediator failed to disclose circumstances raising justifiable doubts as to impartiality.
C. Granting relief would be contrary to Singapore public policy.
D. The obligations have already been performed.

**Answer: C.** Under SCMA s 7(3) the court may refuse if relief would be contrary to public policy or the subject matter is not capable of settlement by mediation under Singapore law. A, B and D are s 7(2) grounds that the resisting party must prove. Once recorded, the agreement is enforceable like a High Court judgment (s 5).
*Cite: SCMA ss 5, 7(2)–(3)*

### 1.VII The seven elements of effective negotiation — drills

Drills 126–127 cover 1.VII.5 (tested only in passing) and 1.VII.7 (untested). Drills 128–139 are extra drills on the seven elements.

### 1.VII.1 — Interests, not positions

**Qdrill-128** · `1.VII.1` · drill-128 · `drp-m-1-45`

A tenant says at mediation: "I will not pay a cent more than $3,000 a month." Which of the following is an *interest* rather than a position?

A. "Rent must stay at $3,000."
B. "I need to keep my business's fixed costs predictable while sales recover."
C. "I want the landlord to withdraw the rent increase."
D. "I will move out if the rent goes up."

**Answer: B.** An interest is the need or concern behind a demand. A and C are positions (demands). D is an *alternative* (what the tenant will do without agreement).
*Cite: MED-4 (see `drp-m-1-45`, `drp-m-1-48`)*

**Qdrill-129** · `1.VII.1` · drill-129 · `drp-m-1-45`

Which is NOT part of the recommended approach to interests?

A. Ask "why?" and "why not?" to dig beneath positions.
B. Clarify and prioritise the interests identified.
C. Capitalise on joint interests.
D. Focus only on the client's interests; the other side's interests are for its own counsel.

**Answer: D.** Parties must be helped to see that the other side's interests have to be addressed too; options that meet only one side's interests fail (PYP 2023 Q38). A, B and C are the approach.
*Cite: MED-4 (see `drp-m-1-45`)*

### 1.VII.2 — Options

**Qdrill-130** · `1.VII.2` · drill-130 · `drp-m-1-46`

Which of the following are ground rules for brainstorming options?

I. No commitment.
II. No attribution.
III. No criticism or evaluation.
IV. Decide on each option as soon as it is proposed.

A. I and II only
B. I, II and III only
C. II, III and IV only
D. I, II, III and IV

**Answer: B.** Separate inventing from deciding: no commitment, no attribution, no criticism, no evaluation. IV merges inventing and deciding.
*Cite: MED-4 (see `drp-m-1-46`)*

**Qdrill-131** · `1.VII.2` · drill-131 · `drp-m-1-46` `drp-m-1-48`

What is the key difference between *options* and *alternatives*?

A. Options are unilateral; alternatives need the other party.
B. Options are possible solutions that need the other party's agreement; alternatives are what a party can do on its own if there is no agreement.
C. They are the same thing.
D. Alternatives are generated by brainstorming; options are measured by BATNA.

**Answer: B.** Options are bilateral; alternatives are unilateral. A reverses them. D reverses their roles: options are brainstormed; alternatives (BATNA) are the yardstick for accepting an option.
*Cite: MED-4 (see `drp-m-1-46`, `drp-m-1-48`)*

**Qdrill-132** · `1.VII.2` · drill-132 · `drp-m-1-46`

"Expanding the pie" means

A. demanding more than you expect, to leave room to concede.
B. creating more value so both sides can be better off, since a smaller slice of a bigger pie can beat a larger slice of a small one.
C. adding more parties to the mediation.
D. splitting the difference.

**Answer: B.** A is anchoring; D is a distributive compromise; C is not the concept.
*Cite: MED-4 (see `drp-m-1-46`)*

### 1.VII.3 — Criteria (legitimacy)

**Qdrill-133** · `1.VII.3` · drill-133 · `drp-m-1-47`

Two siblings cannot agree how to divide their late father's furniture, and there is no market or legal standard that helps. Which is a *fair procedure* the mediator may suggest?

A. The elder sibling decides, as the executor.
B. One sibling divides the furniture into two lots and the other chooses first.
C. Whoever offers the higher price takes everything.
D. The sibling with the stronger legal case decides.

**Answer: B.** Absent a standard, fair procedures include one cuts, the other chooses; taking turns; drawing lots; letting a neutral decide. A and D let one party decide, which is not a fair procedure (PYP 2023 Q55). C favours the wealthier party.
*Cite: MED-4 p13–14 (see `drp-m-1-47`)*

**Qdrill-134** · `1.VII.3` · drill-134 · `drp-m-1-47`

Objective criteria are said to act as a "sword and shield". This means they

A. let a party attack the other side's credibility and protect its own witnesses.
B. persuade the other side that an option is fair, and protect against unfair proposals.
C. replace the need for a mediator.
D. are used only by the mediator, not by counsel.

**Answer: B.** Criteria persuade (sword) and resist unfairness (shield), and give a face-saving justification, especially for representatives who must report back. A confuses them with litigation tactics. C and D: criteria are used by everyone in the negotiation.
*Cite: MED-4 (see `drp-m-1-47`)*

### 1.VII.4 — Alternatives: BATNA, WATNA, MLATNA

**Qdrill-135** · `1.VII.4` · drill-135 · `drp-m-1-48`

At mediation a claimant insists "I'm sure to win in court, so I won't take less than the full claim." What should a good mediation advocate do?

A. Agree, since the client's instructions are final.
B. Reality-test the client's BATNA: the risks, costs, time and enforcement of a court judgment, and the WATNA and MLATNA too.
C. Tell the other side the client's bottom line.
D. Refuse to continue the mediation.

**Answer: B.** Reality-testing a party "sure to win" is the core use of alternatives; the decision remains the client's, but it must be informed (PCR r 5). A: the advocate must ensure decisions are well considered. C: breaches confidentiality and weakens the client. D: unhelpful.
*Cite: MED-4 (see `drp-m-1-48`); MED-5 (see `drp-m-1-54`)*

**Qdrill-136** · `1.VII.4` · drill-136 · `drp-m-1-48`

A defendant is offered a settlement of $60,000. Its lawyers estimate that at trial it will most likely pay $80,000 plus $30,000 in costs, at worst $150,000, at best nothing. Using the alternatives framework, which is CORRECT?

A. Reject: the BATNA (pay nothing) is better than any offer.
B. Accept only if the offer is better than the WATNA.
C. The defendant should weigh the offer against its realistic alternatives; at $60,000 it is better than the MLATNA ($110,000) and far better than the WATNA, so accepting is reasonable unless the chance of the best case is high.
D. Alternatives are irrelevant once an offer is on the table.

**Answer: C.** Compare the offer with BATNA, WATNA and the most likely outcome; accept if the offer is at least as good as what you can realistically get without agreement. A treats the best case as certain. B sets the bar too low. D is wrong: alternatives are the yardstick for offers.
*Cite: MED-4 (see `drp-m-1-48`)*

### 1.VII.5 — Communication

**Qdrill-126** · `1.VII.5` · drill-126 · `drp-m-1-49`

In the "Communication" element of the seven elements, what is the first purpose of listening?

A. To find weaknesses in the other side's case to attack later.
B. To understand, not to debate or attack, while listening for "positive" voices that help the parties see the positives.
C. To prepare the rebuttal.
D. To take a verbatim record for later use as evidence.

**Answer: B.** Receiving is first and foremost to understand; conveying lets the parties know they have been heard and helps them hear each other. A and C are adversarial. D defeats confidentiality.
*Cite: MED-4 (see `drp-m-1-49`)*

**Qdrill-137** · `1.VII.5` · drill-137 · `drp-m-1-49`

Which of the following describe the *conveying* side of communication?

I. Letting the parties know they have been heard.
II. Helping the parties hear each other.
III. Winning each exchange with the stronger argument.
IV. Repeating the client's position until the other side gives way.

A. I and II only
B. I, II and III only
C. III and IV only
D. I, II, III and IV

**Answer: A.** Conveying (speaking) is to let parties know they have been heard and to help them hear each other. III and IV are positional bargaining.
*Cite: MED-4 (see `drp-m-1-49`)*

### 1.VII.6 — Relationship

**Qdrill-138** · `1.VII.6` · drill-138 · `drp-m-1-50`

Former business partners are so angry with each other that they cannot discuss the buy-out price. Applying the "Relationship" element, the advocate should

A. insist that emotions be kept out entirely and discuss only figures.
B. separate the people from the problem, allow appropriate venting, help each see the other's perspective, and build rapport, so the substantive issue can be dealt with.
C. advise the client to withdraw until the other side apologises.
D. use the other side's anger to extract a better price.

**Answer: B.** Relationship issues can block settlement of the substance; work on perception (empathy), emotion (venting) and communication (rapport), and be unconditionally constructive. A ignores emotion, which then resurfaces. C makes the relationship conditional. D is an underhanded tactic (PCR r 8(3)).
*Cite: MED-4 (see `drp-m-1-50`); PCR r 8(3)*

### 1.VII.7 — Commitment

**Qdrill-127** · `1.VII.7` · drill-127 · `drp-m-1-51`

When should a party commit to a settlement?

A. As early as possible, to show good faith.
B. Only when interests are understood and prioritised, options have been generated, options have been evaluated against objective criteria or a fair procedure, and alternatives have been considered.
C. As soon as the other side makes an offer better than its opening position.
D. Only after the mediator recommends the terms.

**Answer: B.** Commitment comes last, after the other elements; commitments should preferably be written, realistic, clear and specific, dealing with all issues. A and C commit before options and alternatives have been weighed. D: the mediator does not decide.
*Cite: MED-4 (see `drp-m-1-51`)*

**Qdrill-139** · `1.VII.7` · drill-139 · `drp-m-1-51` `drp-m-1-40`

After a long mediation the parties reach agreement late at night. Which is the BEST practice on commitment?

A. Shake hands and leave the drafting to next week.
B. Record the terms in writing before leaving, in clear and specific language that deals with all issues, including payment, default and confidentiality, and check that each term is realistic.
C. Have the mediator sign on behalf of both parties.
D. Agree only the headline sum; the details will follow.

**Answer: B.** Commitments should preferably be in writing, realistic and clear, dealing with all issues to minimise future disputes (the MED-3 drafting checklist). A and D leave room for disagreement and later disputes. C: the agreement must be signed by or on behalf of the parties (MA s 12(3)(b)), not the mediator.
*Cite: MED-4 (see `drp-m-1-51`); MED-3 p28 (see `drp-m-1-40`); MA s 12(3)(b)*

## Coverage check

Questions per Topic, counted under the Topic of each question's first Key (where it sits in this file). Every Topic has at least one answered question.

| Topic | Past-paper | Drills | Total |
|---|---|---|---|
| 0.I Applicable laws and the IAA framework | 9 | 5 | 14 |
| 0.II Domestic arbitration under the Arbitration Act 2001 | 4 | 2 | 6 |
| 0.III Soft law instruments and arbitral institutions | 0 | 6 | 6 |
| 0.IV The arbitration agreement: form and parties | 0 | 7 | 7 |
| 0.V Arbitrability | 3 | 2 | 5 |
| 0.VI Pathological clauses and drafting | 1 | 3 | 4 |
| 0.VII Stay of court proceedings under the IAA | 2 | 3 | 5 |
| 0.VIII Jurisdiction of the tribunal | 5 | 5 | 10 |
| 0.IX Resisting jurisdiction: the respondent's options | 1 | 6 | 7 |
| 0.X Constitution of the tribunal | 1 | 5 | 6 |
| 0.XI Challenging an arbitrator | 1 | 9 | 10 |
| 0.XII Arb-Med, Arb-Med-Arb and multi-tier clauses | 0 | 6 | 6 |
| 0.XIII Conduct of the proceedings and evidence | 4 | 8 | 12 |
| 0.XIV Commencing the arbitration and SIAC procedures | 0 | 5 | 5 |
| 0.XV Interim measures | 2 | 8 | 10 |
| 0.XVI Anti-suit injunctions | 1 | 2 | 3 |
| 0.XVII The award | 1 | 10 | 11 |
| 0.XVIII Setting aside the award | 10 | 5 | 15 |
| 0.XIX Enforcement and resisting enforcement | 6 | 10 | 16 |
| 1.I Nature of mediation | 7 | 1 | 8 |
| 1.II Mediation institutions and schemes | 8 | 2 | 10 |
| 1.III Legal sources and the basis of mediation | 0 | 2 | 2 |
| 1.IV Duty to consider amicable resolution; costs | 5 | 4 | 9 |
| 1.V Mediation Act 2017 | 4 | 6 | 10 |
| 1.VI Mediated settlement agreements | 0 | 3 | 3 |
| 1.VII The seven elements of effective negotiation | 10 | 14 | 24 |
| 1.VIII Role and ethics of the mediation advocate | 20 | 0 | 20 |
