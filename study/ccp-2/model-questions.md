# CCP-2 — Model Questions and Answers

Paper `ccp-2`, CCP Paper 2 (MCQ), Thu 10 Dec 2026, 2:30–4:30pm, open book. Subjects: 0 Intellectual Property · 1 Mergers & Acquisitions · 2 Competition Law · 3 Taxation. Written 15 Nov 2026 as Markdown only, on Bennett's instruction of 14 Nov. No PDF is built until Phase 2 (`python3 tools/build_pack.py ccp-2 --questions`).

**How the file runs.** *Part 1* holds the questions by Subject → Topic → Sub-point, in `coverage.md` order. Each real question sits under the Sub-point it mainly tests. Any other Sub-point it tests is named in its tag line and gets a "See also" line. Where no real question reaches a Sub-point, an own question fills the gap. Every one of the 149 Sub-points has at least one question whose tag line names it. *Part 2* holds the Drills: timed sets built from Part 1 questions, by Topic or mixed, each with a time limit and an answer key.

**How to read a question.** The tag line gives four things: the question ID, the Sub-point Keys it raises (`coverage.md`), the source, and the end-point block(s) in `cheatsheets.md` that hold the rule. The answer follows the options. It says why the right option is right and why each other option is wrong, then gives the cite. Cites use the source aliases in `coverage.md` → "Source key" and statute sections. Cover the answer, answer the question, then check. Log every miss in `weak-spots.md` under its Key.

**Question IDs.**
- `QSQ-IP<n>`, `QSQ-MA<n>`, `QSQ-CL<n>`, `QSQ-TX<n>`: 2026 Sample Questions, question n of Intellectual Property, M&A, Competition Law or Taxation.
- `Q23-<n>`: 2023 CCP Paper 2, question n.
- `Q<subject>-<n>` (e.g. `Q0-12`): own question n for that Subject.

**Sources.** Real questions come first (RULES source order):

- **SQ**: `Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf`, CCP Paper 2: IP pp23–27, M&A pp28–32, Competition pp33–38, Taxation pp39–42. Ten MCQs each, with the **official key** at pp115–116. Every SQ answer below matches the official key. Where the key and the course materials differ in a detail, the answer says so (SQ Competition Q10's "10% of global turnover" cap).
- **2023 CCP Paper 2**: `Seniors Notes/Nic_s Part B Package/3. PYP/2023 PYP/CCP Paper 2.pdf`, 60 Examplify screenshots, one question per page, in reverse order. The Subjects run IP Qs 1–16, Taxation 17–30, Competition 31–44 and M&A 45–60. The screenshots were transcribed for this file. **There are no official answers.** Most screens show an earlier candidate's selection, which is not a key and is wrong in places (noted where it is). Every answer is this project's own, from `cheatsheets.md` and, where noted, the course slides, the statute, Cyril's notes or the CCCS register.
- **No other real CCP Paper 2 questions are held.** Nic's index lists no 2024 or 2025 CCP 2 paper, and the 2021 Advanced Corporate Practice paper is written (board composition, rights issues, a privatisation essay), so it is not reproduced.

**The law.** Every answer follows `cheatsheets.md`, whose blocks were checked against the course materials, current statutes and IRAS rates on 11 Nov 2026 (see `coverage.md`). Where a 2023 question assumed older law, the answer gives the current law and says what changed.

Self-study only: never use this file with a live quiz, the Mock Exam or any other assessment (Handbook §7.11).

**Left out of the 2023 paper:** six questions the pack cannot settle to one answer.
- Q22: s 13W and a mix of ordinary and preference shares. Under the current s 13W (see `ccp-2-3-9`) every option is wrong. The 2023 answer depended on the preference-share rules as they then stood, which the pack does not hold.
- Q33: which category of the fresh-chicken conduct the Competition Appeal Board found unproven. The course materials and the CCCS media release do not say.
- Q37: an example of a "temporal" market. The term appears in no course material.
- Q48: whether a cousin and a grandchild are "close relatives" under the Take-over Code. The definition is not in the slides or Cyril's notes.
- Q53: the s 161 Companies Act share-issue mandate, and Q54: s 76 financial assistance. Both are outside the M&A Coverage List (s 76 is only named on the reading list) and the pack holds no rule for them.

| Subject | Real questions | Own questions | Total |
|---|---|---|---|
| 0 Intellectual Property | 26 (SQ 10; 2023 16) | 43 | 69 |
| 1 Mergers & Acquisitions | 23 (SQ 10; 2023 13) | 36 | 59 |
| 2 Competition Law | 22 (SQ 10; 2023 12) | 20 | 42 |
| 3 Taxation | 23 (SQ 10; 2023 13) | 14 | 37 |
| **Total** | **94** (SQ 40; 2023 54) | **113** | **207** |

Part 2 has 12 Drills. The own questions' answer letters were spread across A–D after drafting, so a letter pattern gives nothing away. The real questions keep their original lettering.

---

# Part 1 — Questions by Topic and Sub-point

## 0 · Intellectual Property

### 0.I Trade marks: what a mark is, why register, absolute grounds

Sub-points 0.I.1–0.I.6. Real questions: QSQ-IP1, Q23-1, Q23-3. Own questions: Q0-1, Q0-2, Q0-3.

### 0.I.1 — Definition of trade mark and sign (s 2(1) TMA); graphical representation

**QSQ-IP1** · `0.I.1` `0.I.5` `0.I.6` · SQ p23 Q1, official key B · `ccp-2-0-1` `ccp-2-0-5`

Which of the following statements is CORRECT?

I. A trade mark can be a word, numeral or label.
II. Each absolute ground for refusal of registration under section 7(1) of the Trade Marks Act operates independently although the grounds may overlap.
III. Every mark that is descriptive of the goods claimed is also devoid of any distinctive character; and every mark that is devoid of any distinctive character is also descriptive of the goods claimed.
IV. The mark "LOVE" for jewellery is an example of a trade mark which is not descriptive as it does not designate the intended purpose of jewellery to serve as an expression of love.

A. I only.
B. I and II.
C. II and III.
D. I, II, III and IV.

**Answer: B.** I: "sign" in s 2(1) TMA expressly includes a word, numeral and label. II: each s 7(1) ground operates independently, though they may overlap, and failing one is enough. III is wrong: s 7(1)(b) is a catch-all that includes descriptive marks, but the converse is not necessarily true (*Love & Co* at [44]–[45]), so a non-distinctive mark need not be descriptive. IV is wrong: "LOVE" for jewellery was held descriptive of its intended purpose under s 7(1)(c), as well as devoid of distinctive character.
*Cite: TMA ss 2(1), 7(1)(b)–(c); IP1 s3, s16–23; SQ p115 (key B); `ccp-2-0-1`, `ccp-2-0-5`*

### 0.I.2 — TM and ® symbols; offence of false representation of registration (s 51)

**Q0-1** · `0.I.2` · own question · `ccp-2-0-2`

Your client has applied to register its mark "ZEPHYR" for sportswear. The application is still under examination. The marketing team wants to print "ZEPHYR®" on this season's labels. What is your advice?

A. Use ® now: an application on file is enough.
B. Use ® now, because once the mark is registered its registration is backdated to the application date.
C. Do not use ® until the mark is registered. Using ® with a mark that is not yet registered is an offence, but "TM" may be used now.
D. Neither symbol may be used until registration, and once the mark is registered ® must appear on every product, or the registration lapses.

**Answer: C.** ® shows that a mark is registered, and it is an offence to use it with a mark that is not yet registered (s 51(1) TMA). "TM" only shows that the sign is used as a trade mark and may be used at any time. A is wrong: a pending application is not a registration. B is wrong: the s 15(2) deeming of the registration date does not make the mark registered before registration is completed. D is wrong: using ® is not a statutory requirement, and leaving it off does not affect the registration.
*Cite: TMA s 51(1); IP1 s6; Cyril-IP §1.1; `ccp-2-0-2`*

### 0.I.3 — Benefits of registration: property right (s 4), register prima facie evidence, infringement, opposition, invalidation

**Q0-2** · `0.I.3` · own question · `ccp-2-0-3`

A café owner asks why she should pay to register the name of her café as a trade mark. Which statement is INCORRECT?

A. Registration gives her a statutory property right with the rights and remedies of the Trade Marks Act.
B. The register is prima facie evidence of matters in it, such as her ownership of the mark.
C. Registration lets her oppose a later identical or similar mark for the same or similar goods or services, and seek to invalidate it if it is registered.
D. Registration is compulsory: an unregistered mark gets no protection at all in Singapore.

**Answer: D.** Registration is not compulsory, and an unregistered mark may still be protected by passing off (non-examinable). A: s 4(1) TMA. B: s 101(a). C: the owner of a registered mark can stop others using it (infringement), stop a later identical or similar mark for the same or similar goods from being registered (opposition), and stop it remaining registered (invalidation).
*Cite: TMA ss 4(1), 101(a); IP1 s8–10; Cyril-IP §1.2.1; `ccp-2-0-3`*

### 0.I.4 — Practical considerations before registering; registration and opposition process

**Q0-3** · `0.I.4` · own question · `ccp-2-0-4`

Which sequence correctly describes the Singapore trade mark registration process?

A. Application → publication in the Trade Marks Journal → formalities examination → substantive examination → registration.
B. Application → registration → publication → substantive examination only if a third party objects.
C. Application → substantive examination → registration → opposition period.
D. Application → formalities examination → substantive examination on absolute and relative grounds → acceptance and publication in the Trade Marks Journal → registration if there is no opposition or the opposition fails.

**Answer: D.** The application is first examined for formalities and then on substance (absolute and relative grounds). Objections can be overcome. The application is then accepted and published in the Trade Marks Journal, and anyone may oppose during the opposition period. The mark is registered if there is no opposition or the opposition fails. A puts publication before examination. C and B put the opposition period, or the examination, after registration. A challenge after registration is by invalidation or revocation, not opposition.
*Cite: IP1 s11–14; Cyril-IP §1.2.2–1.2.3; `ccp-2-0-4`*

### 0.I.5 — Absolute grounds: s 7(1)(b) devoid of distinctive character, s 7(1)(c) descriptive; acquired distinctiveness s 7(2)

**Q23-1** · `0.I.5` `0.IX.1` `0.VI.1` · 2023 CCP Paper 2 Q1 (no official answer) · `ccp-2-0-5` `ccp-2-0-36` `ccp-2-0-19`

Which of the following pairs of statements is correct?

A. Patents protect inventions. Confidential information cannot be protected by technical means.
B. Copyright protects music scores. Patents can only protect products but not processes.
C. A colour applied to packaging for aesthetic reasons and which does not in fact designate trade origin can be a registrable trade mark. Patents protect confidential information.
D. A newly derived sign which describes the characteristics of the goods to which the sign will be applied cannot be registered as a trade mark. Copyright protects computer programmes.

**Answer: D.** A sign that consists of indications designating characteristics of the goods is refused under s 7(1)(c) TMA. A newly derived sign has had no use from which it could acquire distinctiveness under s 7(2). A computer program is a literary work protected by copyright (CA ss 8–9). In each other pair one half is wrong. A: confidential information can be protected by technical measures such as encryption and data rooms. B: patents protect processes as well as products (s 66(1)(b) PA). C: a colour must be capable of distinguishing to be a trade mark (s 2(1)), so a purely decorative colour does not qualify; and a patent is the opposite of confidential information, a monopoly granted in exchange for public disclosure.
*Cite: TMA ss 2(1), 7(1)(c), 7(2); CA ss 8–9; PA s 66(1); IP3 s4, s8–9; IP7 s4–8; `ccp-2-0-5`, `ccp-2-0-36`, `ccp-2-0-19`*

See also Q23-3 under 0.I.6 (acquired distinctiveness; descriptive objections at every stage).

### 0.I.6 — Spectrum of marks (fanciful to generic); Han's, Love & Co, Marvelous

**Q23-3** · `0.I.6` `0.I.5` `0.IV.2` · 2023 CCP Paper 2 Q3 (no official answer; the earlier candidate selected B) · `ccp-2-0-5` `ccp-2-0-14`

Which of the following statements is correct?

I. An invented word is an example of a mark that has a high level of inherent distinctiveness.
II. A mark which is devoid of any distinctive character can acquire a distinctive character as a result of the use made of it.
III. The mark "MARVELOUS!" is an example of a mark that is descriptive of computer games and arcade games.
IV. An objection that a trade mark consists exclusively of descriptive indications which may serve, in trade, to designate the quality of the goods claimed may be encountered in examination, in opposition or in an application for a declaration of invalidity.

A. I only
B. I and II only
C. I, II and III only
D. I, II, III and IV

**Answer: D.** I: invented words have high inherent distinctiveness (*Han's* at [61]–[64]). II: a mark refused under s 7(1)(b) or (c) is saved if it has in fact acquired distinctive character through use (s 7(2) TMA), and a registered one is saved by s 23(2). IV: the s 7(1)(c) objection is raised in examination on absolute grounds, and the grounds for opposition overlap with the absolute grounds. An absolute ground is also a ground for invalidation (s 23(1)). Since I, II and IV are each true, D is the only option that can be right. It treats III as true, in line with the course's use of *Marvelous* [2017] SGIPOS 3 (an application refused on s 7(1)(b) and (c) grounds) as its s 7(1)(c) example. The pack holds *Marvelous*'s principles at [29] but not its finding on the facts. Learn the principles, not the result. The earlier candidate's B leaves out IV, which is true.
*Cite: TMA ss 7(1)(b)–(c), 7(2), 23(1)–(2); IP1 s11–23, s57; `ccp-2-0-5`, `ccp-2-0-14`*

See also QSQ-IP1 under 0.I.1 ("LOVE" for jewellery; s 7(1)(b) and (c) overlap).

### 0.II Trade marks: relative grounds and the Staywell test

Sub-points 0.II.1–0.II.4. Real questions: QSQ-IP6, Q23-2. Own questions: Q0-4, Q0-5, Q0-6.

### 0.II.1 — "Earlier trade mark" (s 2(1)); s 8(2)(a) and (b)

**QSQ-IP6** · `0.II.1` `0.II.4` · SQ p25 Q6, official key D · `ccp-2-0-6` `ccp-2-0-9`

Which of the following statements in relation to *Staywell Hospitality Group Pty Ltd v Starwood Hotels & Resorts Worldwide, Inc* [2014] 1 SLR 911 ("Staywell") is CORRECT?

A. The Staywell test comprises three parts which can be considered in any order, depending on the facts of each case.
B. Under the Staywell test, a high degree of marks-similarity can outweigh the lack of goods-similarity, leading to a finding that there is a likelihood of confusion.
C. The court recognised that pricing and marketing choices made by traders can be taken into account as extraneous factors in determining whether there is a likelihood of confusion.
D. Extraneous factors may be considered in the last step of the Staywell test if they inform the court on how the similarity of marks and goods will likely affect the consumer's perception on the source of the goods.

**Answer: D.** Extraneous factors are admissible at step 3 only so far as they show how the similarity of marks and goods will affect the consumer's perception of source (*Staywell* at [83], [95]). A and B are wrong: steps 1 and 2 are threshold requirements taken in turn. If either fails there is no need to go to step 3 ([55]), so high marks-similarity cannot make up for dissimilar goods. C is wrong: differences a trader creates by pricing, packaging or marketing choices are impermissible ([95]).
*Cite: Staywell [2014] 1 SLR 911 at [55], [83], [95]–[96]; IP1 s24–29, s42–47; SQ p115 (key D); `ccp-2-0-6`, `ccp-2-0-9`*

**Q0-4** · `0.II.1` · own question · `ccp-2-0-6`

Alpha filed a trade mark application for "ORBIT" for watches on 1 March. Beta filed an application for "ORBYT" for clocks on 1 May. Alpha's application is still pending. Can Alpha's mark be an "earlier trade mark" against Beta's application?

A. Yes. An earlier trade mark includes a mark applied for earlier (taking account of priorities), including a pending application, subject to its eventual registration. Beta's application is then judged under s 8(2)(b).
B. No. Only a registered mark can be an earlier trade mark.
C. No. An earlier trade mark must be well known in Singapore.
D. Yes, but only under s 8(2)(a), because the goods are different.

**Answer: A.** Under s 2(1) TMA an "earlier trade mark" is a registered mark (or international mark) with an earlier application date, taking account of priorities, or a mark well known at the later application's date, and it includes a pending earlier application. "ORBYT" is similar, not identical, and the goods are similar, so s 8(2)(b) applies and registration is refused if there is a likelihood of confusion. B and C state the definition too narrowly. D is wrong: s 8(2)(a) is for an identical mark on similar goods.
*Cite: TMA ss 2(1), 8(2); IP1 s24–29; `ccp-2-0-6`*

### 0.II.2 — Staywell step 1: marks-similarity (visual, aural, conceptual; distinctiveness; average consumer, Hai Tong)

**Q0-5** · `0.II.2` · own question · `ccp-2-0-7`

When assessing marks-similarity at step 1 of *Staywell*, which statement is CORRECT?

A. The marks are compared side by side, letter by letter, by an expert in the trade.
B. Visual, aural and conceptual similarity must each be established separately before the marks are similar.
C. The marks are compared as a whole by their overall impression, from the viewpoint of an average consumer with imperfect recollection. A mark with greater technical distinctiveness needs a bigger difference before a rival sign is dissimilar.
D. External matter, such as how the goods are packaged in the market, is taken into account at step 1.

**Answer: C.** Marks are judged as a whole by their overall impression, bearing in mind their distinctive and dominant components (*Staywell* at [26]). The viewpoint is the average consumer who takes some care but has imperfect recollection, so the marks are not compared side by side (*Hai Tong* at [40]). A more distinctive mark (e.g. "Nutella" against "Nutello") sets a high threshold before a competing sign is dissimilar ([25]). B is wrong: the three aspects only guide the inquiry and can trade off against each other ([18]). D is wrong: the comparison is mark-for-mark, without external matter ([20]).
*Cite: Staywell at [17]–[26]; Hai Tong [2013] 2 SLR 941 at [40]; IP1 s30–37; `ccp-2-0-7`*

### 0.II.3 — Staywell step 2: goods/services similarity (specifications, Nice classes, British Sugar factors)

**Q0-6** · `0.II.3` · own question · `ccp-2-0-8`

An earlier mark is registered in Class 9 for "computer software". A later application covers "sunglasses", also in Class 9. Which statement BEST describes how goods-similarity is assessed?

A. The goods are identical because they are in the same Nice class.
B. Goods in different Nice classes can never be similar.
C. The class number is relevant but not determinative. Compare the actual specifications and consider the *British Sugar* factors: uses, users, physical nature, trade channels, where they sit in shops, and how far they compete.
D. Goods-similarity is assumed once the marks are found similar.

**Answer: C.** Identify and compare the specifications. Identical specifications mean identical goods. Otherwise assess similarity. The Nice class is relevant but not determinative: Class 9 covers very different goods. The *British Sugar* factors show how the goods are regarded in trade. A and B treat the class as conclusive. D is wrong: goods-similarity is a separate threshold step (*Staywell* at [55]).
*Cite: IP1 s38–41; British Sugar [1996] RPC 281; Staywell at [40]–[41]; `ccp-2-0-8`*

### 0.II.4 — Staywell step 3: likelihood of confusion; permissible and impermissible extraneous factors; opposition v infringement

**Q23-2** · `0.II.4` `0.II.1` · 2023 CCP Paper 2 Q2 (no official answer) · `ccp-2-0-9` `ccp-2-0-6`

The test in *Staywell Hospitality Group Pty Ltd v Starwood Hotels & Resorts Worldwide, Inc* [2014] 1 SLR 911 ___________.

A. is the same test as the global appreciation approach adopted in *Sabel BV v Puma AG* [1998] RPC 199.
B. is applicable in trade mark infringement cases but not in trade mark opposition cases.
C. assesses "marks-similarity" and "goods-similarity" individually before "likelihood of confusion" is assessed in the round.
D. allows all extraneous factors that were not considered in the first two steps to be considered in the third and last step.

**Answer: C.** *Staywell* is a step-by-step test. Marks-similarity and goods-similarity are each threshold requirements assessed in turn. Only if both are met does the court ask how those similarities affect the consumer's perception of source (*Staywell* at [55], [64]). A is wrong: because steps 1 and 2 are thresholds, the test is not a single global appreciation in which strong similarity on one front can make up for its absence on another. B is wrong: the same test applies in opposition and infringement ([15]), though the comparison differs (both parties' notional fair uses in opposition; the defendant's actual use in infringement). D is wrong: only permissible extraneous factors are admitted, never a trader's differentiating steps ([95]–[96]).
*Cite: Staywell at [15], [55], [60]–[64], [95]–[96]; IP1 s24–29, s42–47; `ccp-2-0-9`, `ccp-2-0-6`*

See also QSQ-IP6 under 0.II.1 (step 3 extraneous factors).

### 0.III Trade marks: term, renewal, exclusive rights and dealings

Sub-points 0.III.1–0.III.3. Real question: Q23-4. Own questions: Q0-7, Q0-8.

### 0.III.1 — Registration date, 10-year term and renewal (ss 15(2), 18)

**Q23-4** · `0.III.1` · 2023 CCP Paper 2 Q4 (no official answer) · `ccp-2-0-10`

A trade mark application was filed on 5 May 2023 and the registration process was completed on 10 October 2023. When does the trade mark registration expire?

A. 5 November 2032
B. 5 May 2033
C. 10 October 2033
D. 10 March 2034

**Answer: B.** A mark is registered as of the date of the application, which is deemed the date of registration (s 15(2) TMA). Registration lasts 10 years from that date (s 18(1)), so it expires on 5 May 2033 unless renewed for a further 10 years (s 18(2)). C runs the 10 years from completion of the registration procedure, which is the date that starts the 5-year non-use period under s 22, not the term. A and D match no rule.
*Cite: TMA ss 15(2), 18; IP1 s48–49; `ccp-2-0-10`*

### 0.III.2 — Exclusive rights (s 26); disclaimers and limitations (s 30)

**Q0-7** · `0.III.2` · own question · `ccp-2-0-11`

Kappa applied on 1 June 2025 to register a composite mark (the word "KAPPA KITCHEN" with a plain chef's-hat device) for restaurant services. It disclaimed exclusive rights in the device. The mark was in fact registered on 1 December 2025. In September 2025 a rival began using "KAPPA KITCHEN" for a restaurant. Which statement is CORRECT?

A. Kappa's rights accrue from 1 June 2025, but it could not begin infringement proceedings until the mark was in fact registered. Because of the disclaimer, its exclusive rights do not extend to the chef's-hat device alone.
B. The disclaimer is void, because a proprietor cannot limit its own rights.
C. Kappa has no rights over anything done before 1 December 2025.
D. Kappa could sue in September 2025, because its rights accrued from the application date.

**Answer: A.** The s 26(1) TMA rights accrue from the date of registration, which is the application date (s 15(2)). But no infringement proceedings may be begun before the mark is in fact registered (s 26(4)(a)). An applicant may disclaim exclusive rights in a specified element (s 30(1)), and the s 26 rights are restricted accordingly (ss 26(5), 30(2)). D ignores s 26(4)(a). C ignores the backdating. B is wrong: s 30 permits disclaimers and limitations.
*Cite: TMA ss 15(2), 26(1), (4)(a), (5), 30; IP1 s51–52; `ccp-2-0-11`*

### 0.III.3 — Mark as personal property; assignment and licence formalities (ss 36, 38, 42); recordal (s 39)

**Q0-8** · `0.III.3` · own question · `ccp-2-0-12`

On 1 March, Rho assigned its registered mark to Sigma by a written deed signed by Rho. Sigma did not apply to register the assignment until 1 September. Between March and September a third party infringed the mark. Which statement is CORRECT?

A. The assignment is void because it was not registered.
B. A trade mark is not property and cannot be assigned apart from the business.
C. Sigma may recover damages for the whole period, because the assignment was in writing.
D. The assignment is valid, but Sigma is not entitled to damages or other monetary remedies for the infringement between the assignment and its application to register it.

**Answer: D.** A registered mark is personal property (s 36 TMA) and may be assigned (s 38(1)). An assignment must be in writing signed by or on behalf of the assignor (s 38(3)), which this one is. Until an application to register the assignment is made, the new proprietor gets no monetary remedies for infringements in the gap (s 39(4)). The assignment is also ineffective against someone who acquires a conflicting interest in ignorance of it (s 39(3)). A overstates the effect of non-registration. C ignores s 39(4). B is wrong: s 36.
*Cite: TMA ss 36, 38, 39(3)–(4), 42; IP1 s53–54; `ccp-2-0-12`*

### 0.IV Trade marks: post-registration challenges

Sub-points 0.IV.1–0.IV.3. Real questions: QSQ-IP2, Q23-6. Own question: Q0-9.

### 0.IV.1 — Why challenge; forum (Registrar or Court)

**QSQ-IP2** · `0.IV.1` `0.IV.2` `0.XI.4` · SQ p23 Q2, official key C · `ccp-2-0-13` `ccp-2-0-14` `ccp-2-0-47`

Company DEX sues Company HILT for the infringement of its registered trade mark "DEX". Which of the following statements is INCORRECT?

A. Company HILT may investigate whether the trade mark "DEX" has been put to genuine use in the course of trade in Singapore and consider whether it is possible to counterclaim to revoke Company DEX's registration of "DEX".
B. The three-step Staywell test is relevant both in Company DEX seeking to establish infringement under section 27(2) of the Trade Marks Act and in Company HILT seeking to establish its counterclaim through an application for a declaration of invalidity under section 8(2) of the Trade Marks Act.
C. Company HILT may base its defence and counterclaim on an opposition to the registration of Company DEX's trade mark "DEX".
D. In its defence and counterclaim, Company HILT may challenge the registration of the trade mark "DEX", by an application for a declaration of invalidity, or an application for revocation, in the alternative.

**Answer: C.** Opposition is available only before registration. A registered mark is challenged by invalidation (s 23 TMA) or revocation (s 22), and where proceedings are pending in court the application goes to the court (ss 22(5), 23(5)). A is correct: non-use for 5 years is a revocation ground (s 22(1)). B is correct: *Staywell* applies to infringement under s 27(2) and to invalidation relying on s 8(2) (via s 23(3)). D is correct: invalidity and revocation may be pleaded in the alternative.
*Cite: TMA ss 22, 23; IP1 s56–60; IP2 s14–16; SQ p115 (key C); `ccp-2-0-13`, `ccp-2-0-14`, `ccp-2-0-47`*

### 0.IV.2 — Invalidation (s 23): grounds, effect, partial

**Q0-9** · `0.IV.2` · own question · `ccp-2-0-14`

A registration of "CRISPY" for potato chips is declared invalid because it was registered in breach of s 7(1)(c). Which statement is CORRECT?

A. The registration is treated as revoked from the date of the invalidation application only.
B. The registration cannot be invalidated if it was examined and accepted by the Registrar.
C. The registration is deemed never to have been made, but transactions that are past and closed are not affected. The declaration may be limited to some of the goods.
D. Acquired distinctiveness after registration is irrelevant to an invalidation on s 7 grounds.

**Answer: C.** On a declaration of invalidity the registration is deemed never to have been made, but transactions past and closed are not affected (s 23(10) TMA), and invalidation may be partial (s 23(9)). A describes revocation, which takes effect from the application date or an earlier date (s 22(7)). B is wrong: a registration in breach of s 7 may be declared invalid (s 23(1)). D is wrong: a mark registered in breach of s 7(1)(b)–(d) is not invalidated if it has since acquired distinctive character through use (s 23(2)).
*Cite: TMA ss 22(7), 23(1)–(2), (9)–(10); IP1 s57; `ccp-2-0-14`*

See also QSQ-IP2 under 0.IV.1 (Staywell in invalidation) and Q23-3 under 0.I.6.

### 0.IV.3 — Revocation for non-use (s 22(1)(a)–(b)): 5 years, resumed use, 3-month rule, effective date

**Q23-6** · `0.IV.3` · 2023 CCP Paper 2 Q6 (no official answer) · `ccp-2-0-15`

A trade mark application was filed on 4 April 2017 and the registration process was completed on 9 September 2017. Which of the following statements is INCORRECT?

A. The trade mark proprietor must use the trade mark within 5 years from 9 September 2022 or the registration will be vulnerable to revocation for non-use.
B. The trade mark proprietor may use the trade mark in a form that differs in elements which do not alter the distinctive character of the mark in the form in which it was registered.
C. If the trade mark proprietor has not used his trade mark within the relevant 5-year period, he may still defend its registration by giving proper reasons for non-use.
D. If the trade mark registration is successfully revoked for non-use, and the application for revocation did not claim a specific effective date for the revocation, the rights of the trade mark proprietor would be deemed to have ceased from the date of the application for revocation.

**Answer: A.** The 5 years run from completion of the registration procedure (9 September 2017), so the mark must be put to genuine use by 9 September 2022, not "within 5 years from" that date (s 22(1)(a) TMA). B: use in a differing form that does not alter the distinctive character counts (s 22(2)). C: revocation needs non-use "without proper reasons". D: revocation takes effect from the date of the application, or an earlier date if the grounds existed then (s 22(7)).
*Cite: TMA s 22(1)–(2), (7); IP1 s58–60; `ccp-2-0-15`*

### 0.V Trade marks: infringement and defences

Sub-points 0.V.1–0.V.3. Real questions: QSQ-IP7, Q23-5.

### 0.V.1 — Infringement: s 27(1) identical/identical; s 27(2) with confusion; Staywell applies

**QSQ-IP7** · `0.V.1` `0.V.2` `0.V.3` `0.XI.3` · SQ p25 Q7, official key D · `ccp-2-0-16` `ccp-2-0-17` `ccp-2-0-18` `ccp-2-0-46`

The trade mark "Busy Bees" is registered in the name of Busy Bees Pte Ltd in Class 3 in respect of "Skin care preparations, make-up, perfume". Which of the following statements is INCORRECT?

A. Aaron infringes "Busy Bees" when he offers skin care preparations for sale under the sign "Busy Bees" without the consent of Busy Bees Pte Ltd.
B. Brad does NOT infringe "Busy Bees" when he applies the sign "Busy Bees" to labels for make-up without knowing or having reason to believe that Busy Bees Pte Ltd did not consent to such application of the sign.
C. Colin does NOT infringe "Busy Bees" when he applies the sign "Busy Bees" to a bottle of perfume as a prop in an office play for his company's in-house Christmas party.
D. Busy Bees Pte Ltd may be awarded both damages and statutory damages in an action for infringement.

**Answer: D.** Damages, an account of profits and statutory damages are mutually exclusive for trade marks (s 31(4) TMA). The only exception is that with damages the court may also order an account of profits not already taken into account (s 31(3)). A: an identical sign, identical goods, offering for sale without consent: s 27(1) with s 27(4)(b). B: a person who applies the sign to labelling material without knowing or having reason to believe there was no consent is deemed not to use it (s 27(5)). C: a prop in an in-house play is not use in the course of trade and is for a non-commercial purpose (s 28(4)(b)).
*Cite: TMA ss 27(1), (4)–(5), 28(4)(b), 31(3)–(4); IP1 s62–70; IP2 s10–13; SQ p115 (key D); `ccp-2-0-16`–`ccp-2-0-18`, `ccp-2-0-46`*

### 0.V.2 — What is "use" (s 27(4)); innocent labelling or advertising (s 27(5))

**Q23-5** · `0.V.2` `0.V.3` `0.V.1` · 2023 CCP Paper 2 Q5 (no official answer) · `ccp-2-0-17` `ccp-2-0-18` `ccp-2-0-16`

The trade mark "Sunny Days" is registered in the name of Sunny Private Limited in Class 3 in respect of "Soap". Which of the following actions do NOT infringe this registered trade mark?

I. Adriana sells handmade soap in Singapore as the sole proprietor of a home business and applies the mark "Sunny Days" to the packaging of her soap.
II. Bill exports Adriana's "Sunny Days" soap, packaged with the mark "Sunny Days", from Singapore to Malaysia for sale.
III. Company C conducted some experiments on Sunny Private Limited's "Sunny Days" soap and Company C's "Adventure" soap. The experiments were conducted in a fair manner and it was found that "Adventure" soap is more effective in reducing the bacteria count on washed hands compared to "Sunny Days" soap. Company C publishes this fact in a comparative commercial advertisement, making reference to "Sunny Days" soap.
IV. Diane has a soap carving hobby. She carved the words "Sunny Days" onto a bar of unbranded soap and gives it to her mother as a birthday present.

A. I and II only
B. II and III only
C. III and IV only
D. I and IV only

**Answer: C.** III: fair use in comparative commercial advertising is not an infringement (s 28(4)(a) TMA). IV: a hobby carving given as a present is not use in the course of trade and is for a non-commercial purpose (s 28(4)(b)). I infringes: a home business selling soap is trading, and applying the identical sign to packaging of identical goods is use (s 27(1), (4)(a)). II infringes: exporting goods under the sign is use (s 27(4)(c)).
*Cite: TMA ss 27(1), (4), 28(4); IP1 s62–70; `ccp-2-0-17`, `ccp-2-0-18`, `ccp-2-0-16`*

See also QSQ-IP7 under 0.V.1 (s 27(5) innocent labelling).

### 0.V.3 — Defences (s 28(1)–(4))

See Q23-5 under 0.V.2 (comparative advertising, non-commercial use) and QSQ-IP7 under 0.V.1 (in-house play prop). One more on s 28(1)–(2):

**Q0-10** · `0.V.3` · own question · `ccp-2-0-18`

Tau Pte Ltd owns the registered mark "TAU" for bicycle parts, registered in 2020. Which person has a defence under s 28 TMA?

A. Mr Tau, who since 2015 has run a bicycle repair shop called "Tau's Cycles" and uses that name honestly. Also an independent shop that advertises "spare chains for TAU bicycles" in accordance with honest practices.
B. A rival who sells "TAU-STYLE" bicycle saddles, copying Tau's get-up.
C. A counterfeiter who sells fake "TAU" parts but says he did not know of the registration.
D. A company that started using "TAU" for bicycle parts in 2022 without consent.

**Answer: A.** Use of one's own name or place of business in accordance with honest practices is a defence (s 28(1)(a)), as is use of the mark to indicate the intended purpose of goods such as spare parts (s 28(1)(c)). Mr Tau's continuous use since before the 2020 registration may also give a defence under s 28(2). B, C and D have no defence. Copying get-up is not honest practice. Lack of knowledge is no defence to trade mark infringement (contrast s 27(5), which protects only those who apply labels or advertise). Use that began after registration gets no earlier-use protection.
*Cite: TMA s 28(1)–(2); IP1 s67–70; `ccp-2-0-18`*

### 0.VI Patents: what a patent is and patentability

Sub-points 0.VI.1–0.VI.9. Real questions: QSQ-IP3, Q23-7. Own questions: Q0-11, Q0-12, Q0-13.

### 0.VI.1 — What a patent is; rationale; territorial

**Q0-11** · `0.VI.1` · own question · `ccp-2-0-19`

A client holds a Singapore patent for a water filter and finds copies on sale in China. Which statement is CORRECT?

A. The Singapore patent protects the invention worldwide, because the specification is published.
B. The client can rely on the Singapore patent in China if the copies are later imported into any Paris Convention country.
C. Patents are territorial. The Singapore patent gives no rights in China, where protection had to be sought separately. In exchange for a monopoly of up to 20 years, the client disclosed the invention to the public.
D. A patent, like confidential information, protects the invention only while the invention is kept secret.

**Answer: C.** A patent is a State-granted monopoly, generally for up to 20 years, in exchange for public disclosure in the specification (the patent bargain). Patents are territorial: protection must be sought in each jurisdiction. A and B ignore territoriality. D is the reverse: a patent is granted on disclosure, while confidential information is protected only so long as it stays secret.
*Cite: IP3 s4, s8–9; Cyril-IP §2.1; `ccp-2-0-19`*

See also Q23-1 under 0.I.5 (patents protect processes; a patent is not confidential information).

### 0.VI.2 — Patentable invention (s 13(1)); offensive or immoral inventions (s 13(2)–(3))

**QSQ-IP3** · `0.VI.2` `0.VI.4` `0.VI.5` `0.VI.9` · SQ p24 Q3, official key C · `ccp-2-0-20` `ccp-2-0-22` `ccp-2-0-23` `ccp-2-0-26`

Which of the following statements is CORRECT?

A. An invention is patentable as long as it is novel and capable of industrial application.
B. Priority can be claimed from the date of filing of a later application in a World Trade Organisation member which discloses matter supporting the invention in the present patent application in Singapore.
C. The disclosure of matter constituting an invention is disregarded if such disclosure was in breach of confidence and took place 1 month before a patent application for that invention was filed in Singapore.
D. To fulfil the criteria of sufficiency, the specification of an application must disclose the invention in a manner which is clear and complete for the invention to be performed by a member of the public who reads the specification.

**Answer: C.** A disclosure in breach of confidence within the 12 months before filing is disregarded (s 14(4)(b) PA). A is wrong: an inventive step is also required (s 13(1)(b), s 15). B is wrong: priority is claimed from an earlier application filed in the preceding 12 months (s 17(2)). D is wrong: the test is a person skilled in the art, not a member of the public (s 25(4)).
*Cite: PA ss 13(1), 14(4), 17(2), 25(4); IP3 s11, s18–20, s31–34; IP4 s6–8; SQ p115 (key C); `ccp-2-0-20`, `ccp-2-0-22`, `ccp-2-0-23`, `ccp-2-0-26`*

**Q0-12** · `0.VI.2` · own question · `ccp-2-0-20`

An inventor devises a new, inventive device for cheating at casino card games. Gambling cheats are prohibited by law. Which statement is CORRECT?

A. The device is unpatentable simply because its use is prohibited by law.
B. It is patentable as long as it is new, whatever behaviour it encourages.
C. Morality is never relevant to patentability in Singapore.
D. It is unpatentable only if its publication or exploitation would generally be expected to encourage offensive, immoral or anti-social behaviour. Behaviour is not offensive, immoral or anti-social merely because it is prohibited by law.

**Answer: D.** Section 13(2) PA excludes an invention whose publication or exploitation would generally be expected to encourage offensive, immoral or anti-social behaviour. Section 13(3) provides that behaviour is not so regarded only because it is prohibited by law. So the question is whether the device would be expected to encourage such behaviour, not merely whether it is illegal. A misstates s 13(3). C and B ignore s 13(2).
*Cite: PA s 13(2)–(3); IP4 s9; `ccp-2-0-20`*

### 0.VI.3 — Novelty: state of the art, made available to the public, no mosaicking, enabling disclosure, 3-step assessment; new medical use (s 14(10))

**Q23-7** · `0.VI.3` `0.VI.4` `0.VI.6` `0.VI.7` `0.VII.1` · 2023 CCP Paper 2 Q7 (no official answer) · `ccp-2-0-21` `ccp-2-0-22` `ccp-2-0-24` `ccp-2-0-27`

Which of the following statements is correct?

A. Priority can be claimed from the date of filing of a later application in a Paris Convention country which discloses matter supporting the invention in the present patent application in Singapore.
B. The priority date is the cut-off date for determining the state of the art and also the date from which a patent owner can recover damages for patent infringement.
C. Whether an invention has been anticipated by prior art is determined from the perspective of the person skilled in the art.
D. It is not permissible to mosaic prior art when assessing whether an invention involves an inventive step.

**Answer: C.** Novelty is assessed through the eyes of the person skilled in the art: the claims are construed, and the prior art compared, from that perspective (*Main-Line v UOB* at [54]–[55], [63]). A is wrong: priority comes from an earlier application filed in the preceding 12 months (s 17(2) PA). B is half wrong: the priority date is the cut-off for the state of the art, but once the patent is granted, damages run from publication of the application (s 76). D is wrong: mosaicking is barred for novelty, but for inventive step prior art may be combined if the combination would be obvious to the skilled person.
*Cite: PA ss 14, 15, 17, 76; IP3 s12–30, s35–42; IP4 s11–14; `ccp-2-0-21`, `ccp-2-0-22`, `ccp-2-0-24`, `ccp-2-0-27`*

**Q0-13** · `0.VI.3` · own question · `ccp-2-0-21`

Before the priority date of a Singapore patent for a battery: (1) a single copy of a thesis describing the battery fully sat unread in a public university library in Germany; (2) a magazine article described half the features and a separate brochure described the other half, with no reference to each other; (3) a conference talk vaguely hinted that such a battery "might one day be possible". Which of these destroys novelty?

A. (1) only.
B. (1) and (2).
C. (2) and (3).
D. All three.

**Answer: A.** The state of the art covers matter made available to the public anywhere in the world, in any way (s 14(2) PA). An unread book in a public library can anticipate (*First Currency Choice* at [38]), and disclosure to a single member of the public is enough. (2) does not anticipate: there is no mosaicking for novelty unless documents expressly refer to each other (*Genelabs* at [26]–[28]). (3) does not anticipate: the disclosure must be enabling, and vague disclosures do not anticipate (*Muhlbauer* at [17]).
*Cite: PA s 14(1)–(2); IP3 s12–30; `ccp-2-0-21`*

### 0.VI.4 — Priority date and claiming priority (s 17)

See QSQ-IP3 under 0.VI.2 (later application) and Q23-7 under 0.VI.3 (priority date and damages).

**Q0-14** · `0.VI.4` · own question · `ccp-2-0-22`

An inventor filed a patent application in Japan (a Paris Convention country) on 1 February 2025. She files in Singapore for the same invention on 15 January 2026. A competitor published the invention on 1 July 2025. Which statement is CORRECT?

A. Priority cannot be claimed because the Japanese application was filed outside Singapore.
B. The priority date is always the Singapore filing date.
C. She can claim priority from the Japanese filing, because it was filed in a Paris Convention country within the preceding 12 months and supports the invention. The priority date is then 1 February 2025, and the July 2025 publication is not part of the state of the art.
D. Priority can be claimed only within 6 months of the earlier filing.

**Answer: C.** The priority date is the filing date unless priority is claimed from an earlier application filed in a Paris Convention country or WTO member within the preceding 12 months that discloses matter supporting the invention (s 17(1)–(3) PA). 15 January 2026 is within 12 months of 1 February 2025, so prior art published after the priority date is excluded. A, B and D misstate s 17.
*Cite: PA s 17; IP3 s18–20; `ccp-2-0-22`*

### 0.VI.5 — Grace period: disclosures disregarded within 12 months (s 14(4))

See QSQ-IP3 under 0.VI.2 (breach of confidence 1 month before filing).

**Q0-15** · `0.VI.5` · own question · `ccp-2-0-23`

An inventor presented her invention at an international exhibition in March 2025 and published a paper on it in a learned society's journal in June 2025. She filed in Singapore in January 2026. Which statement is CORRECT?

A. Both disclosures are disregarded in Singapore, because they took place within the 12 months before filing. She should still be warned that other jurisdictions may have narrower grace periods.
B. The grace period is 6 months, so only the June disclosure is disregarded.
C. Only disclosures made in breach of confidence are ever disregarded.
D. Both disclosures destroy novelty in Singapore.

**Answer: A.** Section 14(4) PA disregards disclosures in the 12 months before filing that were made, among others, by the inventor displaying the invention at an international exhibition (s 14(4)(c)) or describing it in a paper read before or published by a learned society (s 14(4)(d)). Disregarded disclosures are excluded for novelty and so for inventive step. Not all jurisdictions have such a broad grace period, so pre-filing disclosure remains risky. D, C and B misstate s 14(4).
*Cite: PA s 14(4); IP3 s31–34; IP4 s16–18; `ccp-2-0-23`*

### 0.VI.6 — Person skilled in the art

See Q23-7 under 0.VI.3 (anticipation judged by the person skilled in the art).

**Q0-16** · `0.VI.6` · own question · `ccp-2-0-21`

Which description of the "person skilled in the art" is CORRECT?

A. A leading expert who would see inventive possibilities others miss.
B. A member of the public with no technical knowledge.
C. A person from the relevant field with the common general knowledge and a practical interest in the subject matter: reasonably intelligent but unimaginative, not inventive, and trying to make the patent's directions work.
D. The patentee's own research team.

**Answer: C.** The person skilled in the art is not an expert. He comes from the relevant field and has its common general knowledge and a practical interest in the subject. He is reasonably intelligent but unimaginative and wants to make the patent work (*Lee Tat Cheng v Maka* [2017] SGHC 48 at [36]–[39]; *First Currency Choice* at [28]). A, B and D set the standard too high, too low, or by the wrong person.
*Cite: IP3 s17; `ccp-2-0-21`*

### 0.VI.7 — Inventive step (s 15); Windsurfing test; indicators

**Q0-17** · `0.VI.7` · own question · `ccp-2-0-24`

Which statement about inventive step is CORRECT?

A. The *Windsurfing* test is applied in Singapore as a useful guide, and its crux is step 4: viewed without knowledge of the invention, are the differences from the prior art obvious, or do they need a degree of invention? Commercial success and a long-felt want point towards an inventive step.
B. A simple invention can never involve an inventive step.
C. If a solution was "obvious to try", that supports an inventive step.
D. The longer the inventor worked on it, the more inventive it is.

**Answer: A.** Section 15 PA asks whether the invention is obvious to a person skilled in the art having regard to the state of the art. *Windsurfing*'s four steps are a "useful guide" (*First Currency Choice* at [45]). Commercial success and long-felt want are indicators for an inventive step (*Mühlbauer* at [107]). B is wrong: simplicity is no bar (*FE Global v Trek* at [46]). C is wrong: "obvious to try" points against an inventive step (*Merck v Pharmaforte* at [42]). D is wrong: the time spent does not measure inventiveness.
*Cite: PA s 15; IP3 s35–42; `ccp-2-0-24`*

See also Q23-7 under 0.VI.3 (mosaicking allowed for inventive step if obvious).

### 0.VI.8 — Industrial application (s 16); methods of treatment and diagnosis excluded

**Q0-18** · `0.VI.8` · own question · `ccp-2-0-25`

A biotech company has invented (1) a new surgical method of removing tumours from the human body and (2) a new drug composition used in that method. Which statement is CORRECT?

A. Both are capable of industrial application.
B. Neither is patentable, because both relate to treatment of the human body.
C. The surgical method is not capable of industrial application. The drug composition, a product invented for use in such a method, can be.
D. The surgical method is patentable but the drug is not.

**Answer: C.** A method of treatment of the human or animal body by surgery or therapy, or of diagnosis practised on the body, is not capable of industrial application (s 16(2) PA). But a substance or composition invented for use in such a method can be (s 16(3)). Industrial application generally means the invention can be made or used in any kind of industry, including agriculture (s 16(1)).
*Cite: PA s 16; IP4 s2–5; `ccp-2-0-25`*

### 0.VI.9 — Sufficiency (s 25(4)); two-step test

See QSQ-IP3 under 0.VI.2 (sufficiency judged by the person skilled in the art, not a member of the public).

**Q0-19** · `0.VI.9` · own question · `ccp-2-0-26`

A competitor says a patent's specification does not tell anyone how to make the claimed alloy. Which statement is CORRECT?

A. Sufficiency is not a ground of revocation once the patent is granted.
B. Sufficiency is a pure question of law for the judge, with no evidence needed.
C. The specification must disclose the invention clearly and completely enough for it to be performed by a person skilled in the art. The test is to identify what the invention claims to enable the skilled person to do, then ask whether the specification enables him to do it. Insufficiency is a ground of revocation.
D. The specification need only disclose enough for an expert scientist to reconstruct the invention after years of research.

**Answer: C.** Section 25(4) PA requires a disclosure clear and complete enough for a person skilled in the art to perform the invention (the patent bargain). The two-step test is in *First Currency Choice* at [60]–[61]. It is a question of fact, and insufficiency is a ground of revocation (s 80(1)(c)). A, B and D misstate the rule and its standard.
*Cite: PA ss 25(4), 80(1)(c); IP4 s6–8; `ccp-2-0-26`*

### 0.VII Patents: grant process and pre-filing considerations

Sub-points 0.VII.1–0.VII.5. All own questions (Q23-7 also touches 0.VII.1): Q0-20 to Q0-24.

### 0.VII.1 — Filing date, publication at 18 months, effect of publication (s 26, 27, 76)

**Q0-20** · `0.VII.1` · own question · `ccp-2-0-27`

A Singapore patent application was filed on 1 March 2024, claiming no priority. Which statement is CORRECT?

A. The application stays confidential until grant.
B. Publication has no legal effect until grant.
C. It will be published at 12 months.
D. It will be published as soon as possible after 18 months from the filing date (around September 2025), unless early publication is requested. On publication the information loses protection as confidential information and becomes prior art worldwide. Once granted, the patentee can recover damages for infringement from the date of publication.

**Answer: D.** Applications are published as soon as possible after 18 months from the filing or priority date (s 27 PA with Patents Rule 29(1)), and the applicant may ask for early publication (s 27(2)). Publication ends confidentiality (*QB Net v Earnson* at [87]), makes the application prior art, and fixes the date from which damages may be recovered once the patent is granted (s 76). A, C and B are wrong.
*Cite: PA ss 26, 27, 76; IP4 s11–14; `ccp-2-0-27`*

See also Q23-7 under 0.VI.3 (damages run from publication, not priority).

### 0.VII.2 — Term of 20 years and renewal fees (s 36; r 51)

**Q0-21** · `0.VII.2` · own question · `ccp-2-0-28`

A Singapore patent application was filed on 10 June 2020 and the patent was granted on 10 June 2023. Which statement is CORRECT?

A. The patent lasts 20 years from grant, until 10 June 2043.
B. The patent lasts 10 years, renewable for 10 more.
C. No renewal fees are payable during the 20-year term.
D. The patent is in force from grant until the end of 20 years from the filing date (10 June 2040), provided annual renewal fees are paid from the end of the 4th year from filing, within the 3 months before each anniversary of filing.

**Answer: D.** A patent is in force from the issue of the certificate of grant until the end of 20 years from the filing date (s 36(1) PA). Renewal fees are payable annually from the end of the 4th year from filing (Patents Rule 51(1)). A runs the term from grant. C ignores renewal. B confuses a patent with a trade mark (10-year renewable terms).
*Cite: PA s 36(1); Patents Rule 51(1); IP4 s15; `ccp-2-0-28`*

### 0.VII.3 — Pre-filing: keep invention confidential, filing strategy, searches

**Q0-22** · `0.VII.3` · own question · `ccp-2-0-29`

A start-up wants to show its unfiled invention to investors next week and to file "later, once we have money". What is the BEST advice?

A. Disclose freely: the Singapore grace period protects them in every country.
B. There is no need to search prior art before filing, because the Registry does that.
C. Keep the invention confidential (e.g. under NDAs) until filing, because disclosure can destroy novelty and inventive step and not all jurisdictions have Singapore's broad 12-month grace period. Plan where and how to file by business objectives and budget, and search patent and non-patent literature first.
D. File only in Singapore, since a Singapore patent covers the region.

**Answer: C.** Pre-filing disclosure risks novelty and inventive step. Singapore's s 14(4) grace period is broad, but other jurisdictions' are narrower. Filing strategy follows business objectives and budget. Due diligence before filing means searching patent literature (granted patents, pending applications) and non-patent literature, to assess patentability and avoid infringement. A and D ignore territoriality. B ignores the value of a pre-filing search.
*Cite: IP4 s16–19, s22; Cyril-IP §2.4.1–2.4.4; `ccp-2-0-29`*

### 0.VII.4 — Employees' inventions (ss 49, 50)

**Q0-23** · `0.VII.4` · own question · `ccp-2-0-30`

Uma is employed in Singapore as an accounts clerk at a robotics company. In her spare time, at home, she invents a new robotic gripper. Her contract says nothing about inventions. Who owns the invention, as between Uma and the employer?

A. Uma. The invention was not made in the course of her normal or specifically assigned duties in circumstances where an invention might reasonably be expected, and as a clerk she had no special obligation to further the employer's undertaking.
B. The employer, because she is an employee.
C. The employer, because the invention relates to its business.
D. Neither: it falls into the public domain.

**Answer: A.** Under s 49(1) PA an employee's invention belongs to the employer only if (a) it was made in the course of the employee's normal duties, or duties specifically assigned, in circumstances where an invention might reasonably be expected, or (b) it was made in the course of duties where the employee had a special obligation to further the employer's interests (e.g. a senior employee). Otherwise it belongs to the employee. The rules apply because she is mainly employed in Singapore (s 50(1)), and a contract could have changed the result (s 50(4)). B and C ignore s 49's conditions.
*Cite: PA ss 49(1), 50(1), (4); IP4 s20–21; `ccp-2-0-30`*

### 0.VII.5 — Patent as personal property; assignments, licences and registration (ss 41, 43, 75)

**Q0-24** · `0.VII.5` · own question · `ccp-2-0-31`

On 1 January Phi orally agreed to assign its Singapore patent to Chi, and Chi paid. On 1 February Phi assigned the same patent in writing, signed, to Psi, who did not know of the deal with Chi. Psi registered the assignment on 1 March. Which statement is CORRECT?

A. Chi owns the patent because it agreed first.
B. Both assignments are valid and the patent is jointly owned.
C. The oral assignment to Chi is void, because an assignment must be in writing and signed by or on behalf of the assignor. Psi's registered written assignment prevails.
D. Neither assignment is effective until the patent expires.

**Answer: C.** A patent is personal property that may be assigned, mortgaged or licensed (s 41(1)–(4) PA). An assignment is void unless in writing and signed by or on behalf of the assignor (s 41(6)). A person claiming under a later transaction also takes priority over an earlier unregistered one if he did not know of it (s 43(1)). Had Psi delayed registration beyond 6 months, it would have lost damages for infringements before registration (s 75). A, B and D are wrong.
*Cite: PA ss 41, 43, 75; `ccp-2-0-31`*

### 0.VIII Patents: infringement, defences and revocation

Sub-points 0.VIII.1–0.VIII.4. Real question: Q23-8. Own questions: Q0-25, Q0-26, Q0-27.

### 0.VIII.1 — Acts of infringement: product and process patents (s 66(1))

**Q0-25** · `0.VIII.1` · own question · `ccp-2-0-32`

Omega owns a Singapore patent for a process of making a coating. Which act infringes, if done in Singapore without consent while the patent is in force?

A. Making the coating by the patented process in Malaysia and selling it in Malaysia.
B. Importing into Singapore and selling coatings obtained directly by the patented process abroad.
C. Reading the published patent specification.
D. Making the coating by a different, non-equivalent process in Singapore.

**Answer: B.** For a process patent, s 66(1) PA makes it an infringement to use the process, offer it for use, or dispose of, offer to dispose of, use, import or keep a product obtained directly by the process. All of these must be done in Singapore without consent while the patent is in force. A happens outside Singapore. C is not an act of infringement. D does not use the claimed process (and Singapore rejects the doctrine of equivalents).
*Cite: PA s 66(1); IP4 s24–26; `ccp-2-0-32`*

### 0.VIII.2 — Claim construction: purposive approach; doctrine of equivalents rejected (Maka; s 113(1))

**Q0-26** · `0.VIII.2` · own question · `ccp-2-0-33`

How does a Singapore court decide whether a product falls within a patent claim?

A. By reading the claim literally, word for word.
B. By asking whether the product performs substantially the same function in substantially the same way to the same result (the doctrine of equivalents).
C. By construing the claim purposively: what a person skilled in the art would have understood the patentee to mean by the claim language, read with the description and drawings. The doctrine of equivalents has been rejected.
D. By the patentee's evidence of what it intended to claim.

**Answer: C.** The invention is that specified in a claim, interpreted by the description and drawings (s 113(1) PA). Claims are construed purposively, balancing fair protection for the patentee with certainty for third parties. *Lee Tat Cheng v Maka GPS* [2018] 1 SLR 856 decisively rejected the doctrine of equivalents (B). A would let imitators escape by immaterial variations. D uses the wrong viewpoint: the question is what the skilled reader would understand, not the patentee's subjective intent.
*Cite: PA s 113(1); IP4 s27–33; `ccp-2-0-33`*

### 0.VIII.3 — Defences (s 66(2)) and restriction on relief for innocent infringer (s 69)

**Q0-27** · `0.VIII.3` · own question · `ccp-2-0-34`

A hobbyist builds the patented device at home for private use. A university lab builds one to test whether the invention works as claimed. A trader sells copies, having seen products marked "patented" with no patent number, and proves he had no reasonable grounds to suppose a patent existed. Which statement is CORRECT?

A. All three are liable for damages.
B. Only the trader has a defence.
C. The hobbyist and the lab have defences: private and non-commercial use (s 66(2)(a)) and experimental purposes relating to the invention (s 66(2)(b)). The trader infringes, but no damages or account of profits can be awarded against him, because "patented" without the number did not fix him with knowledge. An injunction remains available.
D. Marking a product "patented" always fixes the world with knowledge of the patent.

**Answer: C.** Section 66(2)(a) and (b) PA cover private non-commercial acts and experiments relating to the invention. Under s 69(1), a defendant who proves he was not aware, and had no reasonable grounds to suppose, that the patent existed is not liable for damages or an account of profits. Marking with "patent" or "patented" does not fix knowledge unless the patent number accompanies the word (s 69(2)). An injunction can still issue.
*Cite: PA ss 66(2), 69(1)–(2); IP4 s34–37; `ccp-2-0-34`*

### 0.VIII.4 — Revocation: grounds (s 80(1)), IPOS process, effect (s 80(5), (7)); re-examination

**Q23-8** · `0.VIII.4` `0.XI.4` · 2023 CCP Paper 2 Q8 (no official answer; the earlier candidate selected D, which is wrong) · `ccp-2-0-35` `ccp-2-0-47`

Which of the following statements is correct?

I. A patent may be revoked in an application for revocation filed with the Registrar of Patents.
II. A patent may be revoked in an application for revocation filed in the High Court.
III. A patent may be revoked in a counterclaim to patent infringement.
IV. If a patent is revoked, it will be revoked in its entirety in respect of all claims.

A. I only
B. I, II only
C. I, II and III only
D. I, II, III and IV

**Answer: C.** The court or the Registrar may revoke a patent on the s 80(1) PA grounds (I and II), and a defendant sued for infringement may counterclaim for revocation (III). IV is wrong: where a ground invalidates the patent only to a limited extent, the patentee may amend under s 83 to avoid revocation (s 80(5)(b)). So revocation need not take out every claim. Where a patent is revoked, the revocation takes effect from grant (s 80(7)).
*Cite: PA s 80(1), (5), (7); IP4 s39–44; IP2 s14–16; `ccp-2-0-35`, `ccp-2-0-47`*

### 0.IX Copyright: subject matter, protection criteria and ownership

Sub-points 0.IX.1–0.IX.4. Real questions: QSQ-IP4, QSQ-IP10 (Q23-1 also touches 0.IX.1). Own questions: Q0-28, Q0-29, Q0-30.

### 0.IX.1 — Works protected (authorial and non-authorial); what is not protected; fixation; rights subsist independently

**QSQ-IP4** · `0.IX.1` · SQ p24 Q4, official key D · `ccp-2-0-36`

Which of the following subject matter can be protected by copyright?

I. A compilation.
II. A computer programme.
III. A work of mime.
IV. A script for a film.

A. I and II.
B. III and IV.
C. I, II and IV.
D. I, II, III and IV.

**Answer: D.** Literary works include compilations and computer programs. Dramatic works include works of mime and dance (s 15 CA) and film scripts. All are authorial works (ss 8–9).
*Cite: CA ss 8, 9, 15; IP5 s2–6; SQ p115 (key D); `ccp-2-0-36`*

See also Q23-1 under 0.I.5 (copyright protects computer programs).

**Q0-28** · `0.IX.1` · own question · `ccp-2-0-36`

A chef has (1) an original written recipe book, (2) the idea of serving durian ice cream in a coconut shell, and (3) a film of her cooking show with its own soundtrack. Which statement is CORRECT?

A. All three are protected by copyright.
B. The film is protected only while the chef keeps a copy; deleting it destroys copyright.
C. Only works registered with IPOS are protected.
D. The recipe book (a literary work) and the film are protected, and the soundtrack may carry separate sound recording and musical work copyrights. The idea is not protected.

**Answer: D.** Copyright protects authorial works (literary, dramatic, musical, artistic) and non-authorial works such as films and sound recordings (ss 8–9 CA). Ideas, concepts, procedures and methods are not protected. Rights in one product subsist independently, so a film may carry film, sound recording and musical copyrights. C is wrong: protection is automatic. B is wrong: fixation need not be permanent, and deleting a copy does not destroy copyright.
*Cite: CA ss 8, 9; IP5 s2–6; `ccp-2-0-36`*

### 0.IX.2 — Criteria: automatic protection; originality, human author, material form; connecting factors

**Q0-29** · `0.IX.2` · own question · `ccp-2-0-37`

Which work is LEAST likely to attract copyright in Singapore?

A. A novel first published in Singapore by a Singapore citizen.
B. A photograph taken in Japan by a Singapore resident, first published in a Berne Convention country.
C. A database of stock prices generated automatically by a computer system with no human author exercising intellectual effort in creating it.
D. A song the composer recorded on her phone but never wrote down.

**Answer: C.** Copyright arises automatically, but an authorial work must be original: a human author must have applied intellectual effort, creativity or skill to the authorial creation (*Global Yellow Pages* [2017] 2 SLR 185). With no human author there is no original work (*Asia Pacific Publishing* [2011] 4 SLR 381). A and B have connecting factors (a qualified individual; first publication in Singapore or a reciprocating country). D is reduced to material form by the recording (s 16).
*Cite: CA s 16; IP5 s8–16; `ccp-2-0-37`*

See also Q23-9 under 0.X.1 (a Singapore citizen's novel published in Singapore).

### 0.IX.3 — First ownership (s 133); contract; employees (s 134); commissioned works (s 135)

**QSQ-IP10** · `0.IX.3` · SQ p27 Q10, official key C · `ccp-2-0-38`

Employer J is a book publisher and hires Employee K under a contract of service to draw illustrations for the books which Employer J publishes. This contract of service is silent on ownership of copyright in the illustrations for the books. Which of the following statements is INCORRECT?

I. The first owner of copyright in the illustrations is Employer J.
II. The first owner of copyright in the illustrations is Employer J, only to the extent that the copyright relates to making copies of the illustrations.
III. The first owner of copyright in the illustrations is Employee K.
IV. The default position on copyright ownership can be modified by written agreement.

A. All the statements are correct.
B. I and IV are incorrect.
C. II and III are incorrect.
D. Only II is incorrect.

**Answer: C.** A work made by an employee in the course of a contract of service belongs to the employer (s 134(3) CA), so I is correct and III incorrect. II is incorrect: the limited ownership rule applies only to works made for publication in a periodical owned by the employer (s 134(4)), and a book publisher is not a periodical. IV is correct: s 134(5) allows a contrary written agreement.
*Cite: CA ss 133–135; IP5 s18–21; SQ p115 (key C); `ccp-2-0-38`*

**Q0-30** · `0.IX.3` · own question · `ccp-2-0-38`

In 2025 a company commissioned a freelance designer, under a contract silent on copyright, to design its logo. Who owns the copyright in the logo?

A. The company, because it commissioned and paid for the work.
B. The company and the designer jointly.
C. The designer, as author and first owner, because the old rule giving commissioned works to the commissioning party applies only to works commissioned before 21 November 2021. The company should have taken a written assignment.
D. No one, because commissioned works are not protected.

**Answer: C.** The author is the first owner (s 133(1)(a) CA), subject to contract (s 133(3)). The commissioning party owns certain commissioned works only if they were commissioned before 21 November 2021 (s 135). A freelancer is not an employee, so s 134 does not apply. The company should take a written, signed assignment (s 138).
*Cite: CA ss 133, 135, 138; IP5 s18–21; `ccp-2-0-38`*

### 0.IX.4 — Assignment (ss 138–140), exclusive licence (s 142), licence binding successors (s 143)

**Q0-31** · `0.IX.4` · own question · `ccp-2-0-39`

Ada owns copyright in a novel. She orally grants Ben an exclusive licence to publish it in Singapore. She later sells the copyright to Cal, who knows about Ben's licence. Which statement is CORRECT?

A. The exclusive licence is valid although oral, and binds Cal.
B. A licence never binds a purchaser of the copyright.
C. An exclusive licence must be in writing signed by or on behalf of the licensor, so Ben's oral arrangement is not a valid exclusive licence. A valid licence binds every successor in title except a bona fide purchaser for value without notice, so a written licence would have bound Cal.
D. Copyright cannot be assigned in part or for future works.

**Answer: C.** An exclusive licence must be in writing, signed by or on behalf of the licensor (s 142 CA). A licence binds every successor in title except a bona fide purchaser for value without actual or constructive notice and those deriving title from him (s 143(b)). Cal had notice. B misstates s 143. D is wrong: assignments may be partial (s 139), and future copyright may be assigned (s 140).
*Cite: CA ss 138–140, 142–143; IP5 s22–23; `ccp-2-0-39`*

### 0.X Copyright: exclusive rights, duration, infringement and permitted uses

Sub-points 0.X.1–0.X.5. Real questions: Q23-9, Q23-11. Own questions: Q0-32, Q0-33.

### 0.X.1 — Copyright is a negative right; exclusive rights by type of work (reproduce, publish, communicate, perform, adapt)

**Q23-9** · `0.X.1` `0.X.2` `0.IX.2` · 2023 CCP Paper 2 Q9 (no official answer) · `ccp-2-0-40` `ccp-2-0-41` `ccp-2-0-37`

Anne, a Singapore citizen and self-employed writer, writes and publishes a novel in Singapore. Which of the following statements is INCORRECT?

A. Anne has the exclusive right to make copies of her novel.
B. Anne has the exclusive right to authorise others to perform her novel in public.
C. Copyright in Anne's novel expires 70 years after the end of the year in which Anne dies.
D. Anne has no exclusive right to license another person to publish an adaptation of her novel.

**Answer: D.** The owner has the exclusive right to do, and to authorise others to do, the acts in the Act (s 108(1)(a) CA). For an authorial work these include reproduction, public performance and adaptation (s 112(1)(f)), and the rights extend to the adaptation. So Anne can license publication of an adaptation. A and B are correct. C is correct: life plus 70 years from the end of the calendar year of death (s 114). Copyright subsists because Anne is a qualified individual and the work was first published in Singapore.
*Cite: CA ss 108, 112–114; IP6 s2–12; `ccp-2-0-40`, `ccp-2-0-41`, `ccp-2-0-37`*

**Q0-32** · `0.X.1` · own question · `ccp-2-0-40`

A record label owns copyright in a sound recording. Which statement is CORRECT?

A. Copyright gives the label a positive right to sell the recording anywhere, whatever other laws say.
B. Streaming a recording online is not "communication to the public".
C. Copyright in a sound recording carries every right that a literary work has, including adaptation.
D. Copyright is a negative right: the exclusive right to do, and authorise others to do, the acts the Act lists (e.g. copying, communicating to the public by streaming). It does not itself authorise the owner to do those acts.

**Answer: D.** Copyright is the exclusive right to do and authorise the acts in the Act (s 108(1)(a) CA), not a positive right to do them. The rights depend on the type of work: authorial works ss 112–113, sound recordings s 121. Communication to the public covers electronic transmission such as streaming (s 61). C is wrong: the rights differ by type of work. B is wrong.
*Cite: CA ss 61, 108, 112–113, 121; IP6 s2–11; `ccp-2-0-40`*

### 0.X.2 — Duration: life + 70 years; sound recordings and films

**Q0-33** · `0.X.2` · own question · `ccp-2-0-41`

A Singapore author died on 15 March 2000, having published a novel in 1990. A film of the novel was first published in 2010. When does copyright expire?

A. Novel: 15 March 2070. Film: 2060.
B. Both: 70 years from creation.
C. Novel: 2050. Film: 2060.
D. Novel: at the end of 2070 (70 years from the end of the calendar year of death). Film: at the end of 2080 (70 years from the end of the calendar year of first publication).

**Answer: D.** A published authorial work lasts for the author's life plus 70 years, running from the end of the calendar year of death (s 114 CA): end of 2000 + 70 = end of 2070. Films and sound recordings last 70 years from the end of the calendar year of first publication (ss 122, 125): end of 2010 + 70 = end of 2080. A counts from the date of death. C and B use wrong periods.
*Cite: CA ss 114, 122, 125; IP6 s12; `ccp-2-0-41`*

See also Q23-9 under 0.X.1 (life plus 70 years).

### 0.X.3 — Infringement: Global Yellow Pages three questions; substantial part; causal connection; authorisation (RecordTV); commercial dealing (ss 146–148)

**Q23-11** · `0.X.3` `0.X.5` · 2023 CCP Paper 2 Q11 (no official answer) · `ccp-2-0-42`

In which of the following instances can an action be brought in respect of an infringement of copyright?

A. Owen is the copyright owner of an original computer programme. Without Owen's knowledge or consent, Ivan sells copies of Owen's computer programme under a pseudonym online in 2023.
B. Owen is the copyright owner of an original computer programme. Ivan pays Owen for a licence to deploy the computer programme in 50 laptops belonging to Ivan's company.
C. Owen is the copyright owner of an original computer programme. He learns that Ivan reproduced a very small, insubstantial part of the computer programme in Ivan's own portfolio of work in 2022.
D. Owen is the copyright owner of an original computer programme. He learns that Ivan has leaked the source code of the computer programme over the Internet 10 years ago.

**Answer: A.** Selling unauthorised copies is commercial dealing in infringing articles (ss 148, 73 CA), and making them infringes the reproduction right (s 146). The action is within time. B is licensed, so it is done with consent. C copies no substantial part, so it is not infringement. D is time-barred: no action after 6 years from the infringement (s 154).
*Cite: CA ss 73, 146–148, 154; IP6 s14–21, s26; `ccp-2-0-42`*

**Q0-34** · `0.X.3` · own question · `ccp-2-0-42`

A cloud service lets users record free-to-air TV programmes and replay them. Users use it to make copies. The broadcaster sues the service for authorising infringement. Which factors does the court weigh?

A. Only whether the service charged a fee.
B. Only whether the service itself made any copies.
C. Its control over the means of infringement and power to prevent it; the relationship between the service and the users; whether it took reasonable steps to prevent infringement; and its actual or constructive knowledge of the infringement or its likelihood.
D. Whether the programmes were original. Authorisation is irrelevant to copyright.

**Answer: C.** A person infringes by authorising an infringing act (s 146(1)(a) CA). *RecordTV v MediaCorp* [2011] 1 SLR 830 at [50] lists the four factors in C. A and B are too narrow. D is wrong: authorisation is a form of direct infringement.
*Cite: CA s 146(1)(a); IP6 s14–21; Cyril-IP §3.5; `ccp-2-0-42`*

### 0.X.4 — Permitted uses: fair use (ss 190–191); exclusion by contract (ss 186–187); examinations, judicial proceedings, legal advice

**Q0-35** · `0.X.4` · own question · `ccp-2-0-43`

A software licence's standard terms prohibit "any use of the software in legal proceedings or to obtain legal advice". A school also wants to copy a poem into an exam paper. Which statement is CORRECT?

A. The contract term is valid, because parties are free to exclude any permitted use.
B. Fair use is the only permitted use under the Copyright Act.
C. The term is void so far as it excludes the permitted uses for judicial proceedings and legal advice, which cannot be excluded by contract. The school may rely on the permitted use for examinations. Other permitted uses can be excluded only by an individually negotiated, fair and reasonable term.
D. Fair use is assessed only by how much of the work was copied.

**Answer: C.** Terms excluding the permitted uses for judicial proceedings and legal advice (and certain others: computer programs, computational data analysis, most public collections) are void (s 187 CA). Other permitted uses may be excluded only by an individually negotiated contract with a fair and reasonable term (s 186). Examinations are a permitted use (s 202), as are judicial proceedings (s 290) and legal advice (s 291). B is wrong: there are many permitted uses, independent of each other (s 184). D is wrong: s 191 has four factors (purpose and character, nature of the work, amount and substantiality, effect on the market).
*Cite: CA ss 184, 186–187, 190–191, 202, 290–291; IP6 s22–25; `ccp-2-0-43`*

### 0.X.5 — Limitation: 6 years (s 154)

See Q23-11 under 0.X.3 (option D: a leak 10 years ago is time-barred).

### 0.XI Remedies; defence and counterclaim

Sub-points 0.XI.1–0.XI.4. Real question: Q23-10 (QSQ-IP7, QSQ-IP2 and Q23-8 also touch it). Own questions: Q0-36, Q0-37.

### 0.XI.1 — Statutory damages: copyright (s 308) and counterfeit trade marks (s 31(5)–(6))

**Q0-36** · `0.XI.1` · own question · `ccp-2-0-44`

A claimant cannot easily prove its actual loss. Which statement on statutory damages is CORRECT?

A. Statutory damages are available for every trade mark infringement, up to $10,000 per mark.
B. Statutory damages for patents are available up to $1 million.
C. For copyright, if the claimant elects, the court may award up to $10,000 per work and $200,000 in aggregate, unless actual loss above $200,000 is proved. For trade marks, statutory damages are available only where the infringement involves a counterfeit trade mark: up to $100,000 for each type of goods or service and $1 million in aggregate, unless actual loss above $1 million is proved.
D. Statutory damages can be added to an award of damages for the same infringement.

**Answer: C.** Copyright: s 308(1)–(3) CA. Trade marks: s 31(5)(c) TMA, counterfeit marks only. A is wrong on availability and amount. B is wrong: the Patents Act has no statutory damages. D is wrong: statutory damages are an alternative to damages (s 305(2) CA; s 31(4) TMA). The factors include flagrancy, benefit to the defendant and the need to deter (s 308(5) CA; s 31(6) TMA; *PH Hydraulics* at [81]).
*Cite: CA ss 305, 308; TMA s 31(4)–(6); IP2 s4–7; `ccp-2-0-44`*

### 0.XI.2 — Additional damages (copyright s 307) and account of profits

**Q0-37** · `0.XI.2` · own question · `ccp-2-0-45`

A pirate sold counterfeit DVDs advertised as "original", complete with fake anti-piracy stickers. The copyright owner elects damages. Which statement is CORRECT?

A. Additional damages are available in trade mark and patent cases as well as copyright.
B. Additional damages are compensatory only.
C. An account of profits recovers the infringer's whole revenue, with no deduction of costs.
D. In copyright, the court may award additional damages as part of damages, having regard to the flagrancy of the infringement and the benefit gained by the defendant. Such deplorable conduct justifies them, though they should not give the claimant an extraordinary profit.

**Answer: D.** Additional damages are a copyright remedy forming part of damages (ss 305(1)(b), 307 CA). They are punitive in nature, and conduct like this is the classic case (*New Line Productions v Aglow* [2005] 3 SLR(R) 660). A is wrong: they are copyright only. C is wrong: an account of profits deducts costs and expenses and apportions where the infringement is only part of the chain (*Bosch v Wiedson* [2015] SGHC 105). B is wrong.
*Cite: CA ss 305(1), 307; IP2 s8–9; `ccp-2-0-45`*

### 0.XI.3 — Election of remedies (s 305(2)–(3) CA, s 31(3)–(4) TMA, s 67(2) PA; Main-Line)

**Q23-10** · `0.XI.3` · 2023 CCP Paper 2 Q10 (no official answer) · `ccp-2-0-46`

Which of the following remedy or combination of remedies is NOT available to a claimant who establishes copyright infringement?

A. An injunction.
B. An injunction and an account of profits.
C. Damages under section 305(1)(b) of the Copyright Act and an account of profits insofar as the profits have not been taken into account in computing the damages.
D. Damages under section 305(1)(b) of the Copyright Act and statutory damages.

**Answer: D.** Damages, an account of profits and statutory damages are mutually exclusive (s 305(2) CA). The only exception is that with damages the court may order an account of profits not taken into account in computing the damages (s 305(3)), so C is available. An injunction may be combined with a monetary remedy (A, B).
*Cite: CA s 305(2)–(3); IP2 s10–13; `ccp-2-0-46`*

**Q0-38** · `0.XI.3` · own question · `ccp-2-0-46`

A patentee sues two defendants: Fintech, which created an infringing system, and Bank, which used it. Which statement is CORRECT?

A. The patentee may claim both damages and an account of profits against Bank for the same infringement.
B. The patentee must elect one remedy against both defendants.
C. For the same infringement the court must not award both damages and an account of profits, but the patentee may elect different remedies for separate causes of action, e.g. an account of profits against Bank and damages against Fintech, as in *Main-Line v UOB*.
D. Election applies only to copyright.

**Answer: C.** Section 67(2) PA bars both damages and an account of profits for the same infringement. In *Main-Line v UOB* [2009] SGHC 232 at [44]–[45], [49] the claimant took an account of profits against UOB (which used the system) and damages against FCC (which created it), because they were separately liable for different damage. A, B and D are wrong.
*Cite: PA s 67(2); IP2 s10–13; `ccp-2-0-46`*

See also QSQ-IP7 under 0.V.1 (damages and statutory damages for a trade mark).

### 0.XI.4 — Defence and counterclaim putting validity in issue

See QSQ-IP2 under 0.IV.1 (trade mark: invalidation or revocation in the alternative, not opposition) and Q23-8 under 0.VIII.4 (patent revocation by counterclaim).

**Q0-39** · `0.XI.4` · own question · `ccp-2-0-47`

Your client is sued for infringing a registered patent for a coffee capsule. You believe the capsule was on sale in Europe before the priority date. What is the BEST response?

A. File a defence and counterclaim seeking revocation of the patent under s 80 PA for lack of novelty. If it succeeds, the claimant has no right to sue on.
B. Wait and apply for re-examination after judgment.
C. File an opposition to the patent.
D. File a defence only. Validity cannot be raised in infringement proceedings.

**Answer: A.** When sued on a patent or registered mark, the defendant files a defence and counterclaim putting validity in issue: revocation of a patent under s 80 PA (here for lack of novelty, s 80(1)(a)), or invalidation or revocation of a mark under ss 23 or 22 TMA. If the counterclaim succeeds there is no right to sue on. D is wrong. C: there is no opposition to a granted patent. B: re-examination (non-examinable) is no answer to a pending infringement claim.
*Cite: PA s 80(1); IP2 s14–16; `ccp-2-0-47`*

### 0.XII Confidential information

Sub-points 0.XII.1–0.XII.3. Real questions: Q23-12, QSQ-IP8, Q23-13. Own questions: Q0-40, Q0-41.

### 0.XII.1 — Protecting confidential information: contract, access, awareness; NDA considerations

**Q23-12** · `0.XII.1` · 2023 CCP Paper 2 Q12 (no official answer) · `ccp-2-0-48`

How can confidential information be protected?

I. Use confidentiality clauses in contracts.
II. Restrict access on a need-to-know basis.
III. Protect it as a patent.
IV. Train employees to keep such information confidential e.g., not leave confidential documents unattended to in their workspace.

A. I and II only
B. I, II and III only
C. II, III and IV only
D. I, II and IV only

**Answer: D.** Confidential information is protected by contract (NDAs or confidentiality clauses), by restricting access (technical measures, need-to-know), and by raising awareness (marking documents, records, on-boarding and off-boarding). III is wrong: a patent requires public disclosure of the invention, which ends its confidentiality.
*Cite: IP7 s2, s4–8; IP3 s8–9; `ccp-2-0-48`*

**Q0-40** · `0.XII.1` · own question · `ccp-2-0-48`

You are drafting an NDA for a client disclosing its manufacturing process to a potential partner. Which is NOT one of the contractual considerations the course flags?

A. What happens to copies and physical documents after the project ends.
B. How to handle compelled disclosure, e.g. a court order or regulator's request.
C. Whether disclosure to group companies, affiliates or third parties will be needed to perform the agreement.
D. Whether the receiving party's directors are Singapore citizens.

**Answer: D.** The flagged considerations are A, B and C, plus whether litigating the agreement would itself expose the information (so consider private dispute resolution). The directors' nationality is irrelevant.
*Cite: IP7 s7–8; `ccp-2-0-48`*

### 0.XII.2 — Breach of confidence: Coco v Clark elements; I-Admin modified approach (Lim Oon Kuin)

**QSQ-IP8** · `0.XII.2` · SQ p26 Q8, official key A · `ccp-2-0-49`

Company JKL employed Researcher M to develop a new technological product. Researcher M came into contact with confidential information in the ordinary course of his employment with Company JKL. Researcher M left Company JKL and set up his own company in the same field. He copied information from Company JKL's server and referred to it in the course of developing his new company's business. Which of the following statements is CORRECT based solely on the given facts?

A. Company JKL can claim that Researcher M committed a breach of confidence but has to prove that the information copied was confidential in the first place.
B. Company JKL can claim that Researcher M committed a breach of confidence and does not need to prove that the information copied was confidential in the first place.
C. Company JKL can claim that Researcher M committed a breach of confidence, but Researcher M can defend himself on the basis that mere possession and referencing of Company JKL's confidential information did not constitute acts in breach of confidence.
D. Company JKL can claim that Researcher M committed a breach of confidence in a scenario of "wrongful gain" because of unauthorised disclosure of its confidential information, leading to profits to Researcher M.

**Answer: A.** In a "wrongful loss" case where the defendant took the information, *I-Admin* [2020] SGCA 32, as confined by *Lim Oon Kuin* [2022] SGCA 29, reverses only the third element. The claimant must still prove (a) the information has the quality of confidence and (b) it was imparted in circumstances importing an obligation of confidence. The burden then shifts to the defendant to show his conscience was not affected. So B is wrong. C is wrong: taking and referring to the information is enough. D is wrong: the facts show no disclosure for profit.
*Cite: IP7 s9–13; Cyril-IP §5.2; SQ p115 (key A); `ccp-2-0-49`*

**Q23-13** · `0.XII.2` `0.XII.3` · 2023 CCP Paper 2 Q13 (no official answer) · `ccp-2-0-49` `ccp-2-0-50`

The Court of Appeal in *I-Admin (Singapore) Pte Ltd v Hong Ying Ting and others* [2020] SGCA 32 ___________________.

A. determined that the wrongful loss interest is not a legitimate objective undergirding the law of confidence.
B. made clear that the burden is on a claimant to prove that the defendant's conscience is affected.
C. determined that equitable damages were the appropriate remedy and this would be the value of the claimant's confidential information to the defendant e.g. as assessed with regard to the reduction in time taken to set up the defendant's business.
D. clarified it was not needed to establish that the information in question has the necessary quality of confidence.

**Answer: C.** The sources contradict A, B and D. A: *I-Admin* is the case that protects the "wrongful loss" interest; *Lim Oon Kuin* confines its test to wrongful loss cases. B: after the first two elements are shown, the burden shifts to the defendant to show his conscience was not affected. D: the claimant must still show the information has the quality of confidence. C is the only option consistent with the sources. In *I-Admin* the defendants used the claimant's compiled materials to save themselves time and expense (springboarding, Cyril-IP §5.2). The bases of damages include the cost of obtaining the information and its market value, measured as a benefit to the defendant (IP7 s14). The pack does not hold *I-Admin*'s remedy ruling in terms, so learn C from this question.
*Cite: IP7 s9–15; Cyril-IP §5.2–5.3; `ccp-2-0-49`, `ccp-2-0-50`*

### 0.XII.3 — Damages for breach of confidence; Wrotham Park

**Q0-41** · `0.XII.3` · own question · `ccp-2-0-50`

The court declines to grant an injunction against a defendant who misused the claimant's confidential customer analytics, and awards *Wrotham Park* damages instead. What is the consequence?

A. Once the damages are assessed and paid, the defendant is treated as having bought the information outright, as if under an agreement of sale.
B. The claimant keeps exclusive rights to the information and can sue again for later use.
C. Wrotham Park damages are available only to private individuals for mental distress.
D. The defendant must pay the claimant's lost profits and a licence fee cumulatively.

**Answer: A.** *Wrotham Park* damages are an alternative to an injunction. Once they are paid, the defendant is regarded as having made an outright purchase of the information (*Clearlab* at [335]). C confuses them with the damages for hurt feelings and mental distress that only private individuals can claim. D is wrong: lost profits apply if the claimant would not have licensed the information, and licence fees if it would have; they are alternatives.
*Cite: IP7 s14–15; `ccp-2-0-50`*

### 0.XIII IP in business

Sub-points 0.XIII.1–0.XIII.3. Real questions: QSQ-IP5, QSQ-IP9, Q23-14, Q23-15, Q23-16. Own questions: Q0-42, Q0-43.

### 0.XIII.1 — SWOT analysis of a company's IP position

**QSQ-IP5** · `0.XIII.1` · SQ p24 Q5, official key D · `ccp-2-0-51`

Which of the following statements is INCORRECT in relation to a company's IP position, under the SWOT analysis framework?

A. Its strength is that it has many staff members who are experts in the field and can develop new technology.
B. Its weakness is that its novel inventions are neither protected by patents nor measures preserving confidentiality.
C. It has an opportunity to make use of the government's tax rebates for investment in developing IP.
D. It faces a threat from confidential documents being openly left around the office.

**Answer: D.** Confidential documents left around the office are an internal matter, so a weakness, not a threat (threats are external). A is an internal positive (strength). B is an internal negative (weakness). C is a favourable external factor (opportunity).
*Cite: IP8 s5–13; SQ p115 (key D); `ccp-2-0-51`*

**QSQ-IP9** · `0.XIII.1` · SQ p26 Q9, official key D · `ccp-2-0-51`

Under the SWOT analysis framework, which of the following pairs of statements in relation to a company's IP position is CORRECT?

A. Its strength is that its employees are experts in the field and can develop new technology; its opportunity is that the employees are well trained to protect the confidentiality of its research breakthroughs.
B. Its weakness is that the government has stopped tax rebates for investment in IP development; its threat is that its novel inventions are neither protected by patents nor measures preserving confidentiality.
C. Its strength is that the land on which its factory sits has just been fully paid for; its weakness is that corporate income tax rates have increased.
D. Its opportunity is that there is a demand for its new inventions in Foreign Country A where IP protection is strong; its threat is that a former key employee did not sign any confidentiality undertaking and has set up a competing business.

**Answer: D.** Demand in a foreign country with strong IP protection is a favourable external factor (opportunity). A competing business set up by a former key employee is an external factor that could harm the company (threat). A: well-trained employees are internal, so a strength, not an opportunity. B: the stopping of rebates is external, so a threat; unprotected inventions are internal, so a weakness. C: neither half relates to the IP position, and a tax rate rise is external.
*Cite: IP8 s5–13; SQ p115 (key D); `ccp-2-0-51`*

**Q23-14** · `0.XIII.1` · 2023 CCP Paper 2 Q14 (no official answer) · `ccp-2-0-51`

Which of the following is a strength in a company's IP position, under the SWOT analysis framework?

A. Healthy cashflow.
B. Uncertain geo-political situation among major economies.
C. Improved IP legislation in foreign countries of interest to the company.
D. Strong employee awareness of the importance of protecting the confidential quality of proprietary information.

**Answer: D.** A strength is internal, positive and related to the IP position. Employee awareness of confidentiality fits. A is internal and positive but does not relate to the IP position. B is external, so a threat. C is external and favourable, so an opportunity.
*Cite: IP8 s5–13; `ccp-2-0-51`*

### 0.XIII.2 — Extracting value: working, licensing (franchise, cross-licence), collaboration, sale, collateralisation

**Q23-15** · `0.XIII.2` · 2023 CCP Paper 2 Q15 (no official answer) · `ccp-2-0-52`

Which of the following would you plausibly say to your client about licensing IP?

A. You can consider an exclusive licence arrangement where there is only one licensee and both you and your licensee can use your IP.
B. If you do not plan to use your Patent XYZ, you can consider licensing it to others who are willing to pay you for permission to use it.
C. Your returns from licensing your copyright to others will only be in the form of a running royalty.
D. You can consider the cross-licensing proposal from Company ABC, but be advised that the consideration is only in monetary terms and not in mutual licences.

**Answer: B.** The slides say: "If you don't work the IP, you can let others do so" for licence fees and royalties (IP8 s16). A is wrong: an exclusive licence authorises the licensee to the exclusion of any other person, the owner included (CA s 103(1)). One licensee with the owner still using the IP is the separate "sole" category the slides list. C is wrong: returns may be a fully paid-up fee, a running royalty, or both. D is wrong: cross-licensing is the exchange of mutual licences.
*Cite: IP8 s14–20; CA s 103(1); `ccp-2-0-52`*

**Q0-42** · `0.XIII.2` · own question · `ccp-2-0-52`

A company in financial difficulty holds a portfolio of patents it no longer uses and a stream of royalty receivables. Which pairing of method and description is CORRECT?

A. Securitisation: the patents are pledged to a bank as security for a loan.
B. Collateralisation: royalty receivables are transferred to an entity that issues securities to investors.
C. Sale: immediate returns, usually of non-core IP or in distress (e.g. Kodak's patent sale). Securitisation: royalty receivables are transferred to an entity that issues securities (e.g. Bowie bonds).
D. Franchising: two companies exchange patent licences to gain freedom to operate.

**Answer: C.** A and B swap collateralisation (IP as security for a loan) with securitisation (royalty receivables transferred to an issuing entity). D describes cross-licensing. Franchising is a licence of IP plus a business system, with the franchisor keeping a continuing interest.
*Cite: IP8 s14–28; `ccp-2-0-52`*

### 0.XIII.3 — Issues in IP deals and due diligence

**Q23-16** · `0.XIII.3` `0.XIII.2` · 2023 CCP Paper 2 Q16 (no official answer) · `ccp-2-0-53` `ccp-2-0-52`

You act for Party Q, who intends to collaborate with Party R to use the parties' IP to jointly develop, manufacture and sell new Product DEF. Which of the following should be a cause for concern in an IP due diligence exercise or in the draft collaboration agreement?

A. The background IP which Party R brings to the collaboration, and claims to own, has a clear chain of title.
B. Party R does not give warranties and indemnities in relation to the use of the IP it claims to own.
C. The draft collaboration agreement sets out how new IP created in the course of the collaboration will be owned.
D. The IP involved in the collaboration pertains to Mexico and the USA, and the parties intend to manufacture Product DEF in Mexico for export to and sale in the USA.

**Answer: B.** IP due diligence checks ownership and validity. The absence of warranties and indemnities on IP a party claims to own is a red flag. A is reassuring: a clear chain of title confirms ownership. C is good practice: a collaboration should deal with foreground IP. D matches territory to plans: the IP covers the countries where the product will be made and sold. A concern would arise only if it did not.
*Cite: IP8 s22–37; `ccp-2-0-53`, `ccp-2-0-52`*

**Q0-43** · `0.XIII.3` · own question · `ccp-2-0-53`

Your client will buy a patent from a seller for its business in China. Which finding should MOST concern you?

A. The seller's name matches the registered proprietor on the register.
B. The patent is a Singapore patent only, it expires in 18 months, and a licence to a competitor is recorded on the register.
C. The sale agreement is governed by Singapore law.
D. The seller has given warranties of title and validity.

**Answer: B.** Check scope, term and encumbrances. A Singapore patent does not cover China. Expiry in 18 months may not fit the client's plans. A recorded licence means the client would have to compete with the licensee. A and D are reassuring. C raises no enforceability concern for a Singapore client. The course's lesson: Volkswagen bought Rolls-Royce's car assets but not the Rolls-Royce trade mark, which BMW owned.
*Cite: IP8 s29–37; `ccp-2-0-53`*

## 1 · Mergers & Acquisitions

### 1.I Structuring a private acquisition and pre-acquisition steps

Sub-points 1.I.1–1.I.4. Real questions: Q23-56, Q23-58. Own questions: Q1-1, Q1-2, Q1-3.

### 1.I.1 — M&A road map

**Q1-1** · `1.I.1` · own question · `ccp-2-1-1`

What is the usual order of the stages of a private acquisition?

A. Identify the target → pre-acquisition (confidentiality agreement, MOU, due diligence) → negotiate and sign the SPA and disclosure letter → completion.
B. Completion → due diligence → disclosure letter.
C. Sign the SPA → identify the target → due diligence → MOU.
D. Due diligence → identify the target → completion → sign the SPA.

**Answer: A.** The road map runs: identify the target; pre-acquisition (preliminary documents such as a confidentiality agreement and MOU, then due diligence); negotiation and definitive documents (SPA and disclosure letter); completion (legal transfer of the shares or business). If the SPA has conditions precedent, completion follows signing; if not, signing and completion can be simultaneous. The other options put the stages out of order.
*Cite: MA1 s2; Cyril-MA §1.1; `ccp-2-1-1`*

### 1.I.2 — Share acquisition v business acquisition: factors and comparison (proceeds, minorities, GST, stamp duty, employees s 18A EA)

**Q23-56** · `1.I.2` `1.II.9` · 2023 CCP Paper 2 Q56 (no official answer) · `ccp-2-1-2` `ccp-2-1-13`

Which of the following statements describes an acquisition of all shares in a Singapore private company by a buyer?

I. The buyer purchasing the shares of the Singapore private company acquires everything owned by that company (including the liabilities).
II. The buyer enters into a share purchase agreement with the Singapore private company to acquire the shares of the Singapore private company.
III. In an acquisition of shares, the contracts to which the Singapore private company is a party will have to be individually novated to the buyer acquiring the shares of the Singapore private company.

A. I only
B. I and II only
C. II and III only
D. All of the statements

**Answer: A.** In a share acquisition the buyer takes the company with all its assets and liabilities, and the business carries on undisturbed (I). II is wrong: the buyer buys the shares from the company's shareholders, not from the company. III is wrong: the company remains party to its contracts, so nothing is novated. Assignment and novation are features of a business sale, though change-of-control clauses must be checked.
*Cite: MA1 s3–6, s23; MA2 s22–23; `ccp-2-1-2`, `ccp-2-1-13`*

**Q23-58** · `1.I.2` `1.II.3` · 2023 CCP Paper 2 Q58 (no official answer) · `ccp-2-1-2` `ccp-2-1-7`

Which of the following statements describes an acquisition by a buyer of assets of a Singapore private company?

I. The buyer will have to identify the assets of the Singapore private company it wishes to acquire.
II. The buyer will not assume the liabilities of the Singapore private company, unless otherwise agreed with the Singapore private company.
III. Approval of the shareholders of the Singapore private company will be required if the buyer is acquiring all or substantially all the assets of the Singapore private company.

A. I only
B. I and II only
C. II and III only
D. I, II and III

**Answer: D.** In a business acquisition the buyer selects the assets (I) and the liabilities it takes on (II), and buys them from the company itself. A disposal of the whole or substantially the whole of a company's undertaking or property needs shareholders' approval under s 160 Companies Act, which is usually a condition precedent in a business sale (III).
*Cite: MA1 s3–6, s15; Cyril-MA §1.2–1.3; `ccp-2-1-2`, `ccp-2-1-7`*

**Q1-2** · `1.I.2` · own question · `ccp-2-1-2`

A buyer wants a target's manufacturing business but not its pending product-liability claims. A 10% minority shareholder opposes any sale. Which statement is CORRECT?

A. A share acquisition lets the buyer leave the claims behind and avoid the minority.
B. A share acquisition bears no stamp duty.
C. In a business acquisition the proceeds go directly to the shareholders.
D. A business acquisition lets the buyer select the assets and leave the claims behind, and the minority shareholder cannot block it as a seller of shares would. The proceeds go to the company, GST may be avoided if the sale qualifies for the excluded-transaction treatment, and employees transfer under s 18A Employment Act.

**Answer: D.** This follows the MA1 s6 comparison. Only a business acquisition lets the buyer select assets and liabilities. A minority's objection can be avoided in a business sale but not in a share sale (unless there is a drag-along right). Proceeds go to the company in a business sale and to the shareholders in a share sale. A share sale bears stamp duty and no GST. In a business sale GST may be avoided under the GST (Excluded Transactions) Order, and employees move under s 18A EA. A, C and B reverse the comparison.
*Cite: MA1 s3–6; `ccp-2-1-2`*

### 1.I.3 — Confidentiality agreement

**Q1-3** · `1.I.3` · own question · `ccp-2-1-3`

Which provision is LEAST likely to appear in a confidentiality agreement signed before a buyer receives information about a target?

A. Use of information only to evaluate the deal.
B. Return or destruction of the information if the buyer does not proceed.
C. Non-solicitation / no-hire of the target's staff.
D. The purchase price and completion accounts mechanism.

**Answer: D.** A confidentiality agreement is usually the target's counsel's standard form, signed before any information is exchanged. Typical terms: use of information, term, permitted disclosures (advisers, financiers), return or destruction, and non-solicitation / no-hire. Price mechanics belong in the MOU and the SPA.
*Cite: MA1 s8; Cyril-MA §1.4.1; `ccp-2-1-3`*

### 1.I.4 — Memorandum of understanding / letter of intent; exclusivity, break fee

**Q1-4** · `1.I.4` · own question · `ccp-2-1-4`

A buyer and seller sign a letter of intent recording the price and key terms, a 60-day exclusivity period and a break fee. Which statement is CORRECT?

A. The whole letter of intent is legally binding.
B. Nothing in a letter of intent can ever be binding.
C. The letter is generally non-binding, except for the exclusivity, the break fee and certain boilerplate such as confidentiality and governing law.
D. A letter of intent replaces the need for an SPA.

**Answer: C.** An MOU or letter of intent records the principal terms and the agreement in principle and is non-binding, save for (i) exclusivity, (ii) the break fee and (iii) certain boilerplate. Advantages: moral commitment, agreed key terms, differences flushed out early. Disadvantages: the delay and cost of an extra layer of negotiation, and less flexibility.
*Cite: MA1 s10; Cyril-MA §1.4.3; `ccp-2-1-4`*

### 1.II The sale and purchase agreement

Sub-points 1.II.1–1.II.9. Real questions: QSQ-MA7, Q23-57 (Q23-58 also touches 1.II.3). Own questions: Q1-5 to Q1-12.

### 1.II.1 — Parties: seller's and buyer's covenant strength; escrow, guarantor

**Q1-5** · `1.II.1` · own question · `ccp-2-1-5`

The seller of a target is a special purpose vehicle that will distribute the sale proceeds to its owners at completion. What is the buyer's BEST protection for later warranty claims?

A. None is needed, because warranties are always paid by the target.
B. Ask for a longer long-stop date.
C. Hold back or escrow part of the price, or obtain a guarantee from a seller guarantor such as the ultimate parent.
D. Insist on a locked-box price.

**Answer: C.** A buyer must ask whether the seller will have the resources to pay post-completion warranty or indemnity claims. An SPV may not. The protections are a hold-back or escrow of part of the proceeds, or a seller guarantor. A is wrong: warranties are given by the seller. B and D do not address the seller's covenant strength.
*Cite: MA1 s12; Cyril-MA §1.5.1; `ccp-2-1-5`*

### 1.II.2 — Consideration: fixed price, completion accounts, locked box, earn-outs

**Q1-6** · `1.II.2` · own question · `ccp-2-1-6`

Which statement about pricing mechanisms is CORRECT?

A. In a locked-box deal the price is adjusted after completion by reference to completion accounts.
B. Completion accounts give price certainty at signing.
C. In a locked-box deal the price is fixed at signing on a recent balance sheet, with leakage protection, so the buyer usually needs enhanced due diligence. An earn-out bridges a valuation gap by sharing the risk of future performance.
D. An earn-out pays the whole price at signing.

**Answer: C.** Locked box: price fixed at signing from a historical balance sheet, with protection against leakage of value to the seller. It is certain and simpler, but needs enhanced due diligence. Completion accounts (A, B): the price is estimated at completion and adjusted after closing, so the final price comes later and may be disputed. Earn-outs (contingent value rights) defer part of the price to future performance.
*Cite: MA1 s13–14; Cyril-MA §1.5.2; `ccp-2-1-6`*

### 1.II.3 — Conditions precedent (incl. s 160 CA), long-stop date; pre-completion covenants

**Q1-7** · `1.II.3` · own question · `ccp-2-1-7`

Between signing and completion of a share sale, the seller wants the target to pay a large special dividend. The SPA has standard pre-completion covenants and a long-stop date. Which statement is CORRECT?

A. The negative pre-completion covenants typically prohibit dividends or returns of capital without the buyer's consent. If the conditions precedent are not satisfied by the long-stop date, the SPA can be terminated.
B. Pre-completion covenants apply only after completion.
C. The seller may do as it likes until completion.
D. Conditions precedent can be satisfied after the long-stop date without consequence.

**Answer: A.** Pre-completion covenants preserve the target between signing and completion. Positive: carry on business in the ordinary course. Negative: no changes to the constitution or share capital, no dividends or returns of capital, no acquisitions, disposals, borrowings or capex without consent. Conditions precedent (regulatory and third-party approvals, pre-emption waivers, s 160 approval in a business sale) must be met by the long-stop date, failing which the SPA can be terminated.
*Cite: MA1 s15–16; Cyril-MA §1.5.3–1.5.4; `ccp-2-1-7`*

See also Q23-58 under 1.I.2 (s 160 shareholder approval).

### 1.II.4 — Termination rights: MAC clause, breach

**Q1-8** · `1.II.4` · own question · `ccp-2-1-8`

After signing but before completion, a fire destroys the target's main factory. The SPA has a MAC clause. Which statement is BEST?

A. The buyer must complete regardless.
B. A MAC clause applies only after completion.
C. A MAC clause allows the seller, not the buyer, to walk away.
D. The buyer may terminate by notice if the event has or is likely to have a material adverse effect on the target's turnover, profitability, financial or trading position or prospects. A MAC clause is a risk allocation the seller will resist.

**Answer: D.** A MAC clause lets the buyer terminate before completion if an event has or is likely to have a material adverse effect on the target. It is a risk allocation exercise, and the seller resists it. The buyer may also terminate for (usually material) breach of warranties or covenants.
*Cite: MA1 s17; Cyril-MA §1.5.5; `ccp-2-1-8`*

### 1.II.5 — Warranties: purpose, qualifications, types

**Q1-9** · `1.II.5` · own question · `ccp-2-1-9`

Which pairing of warranty type and example is CORRECT?

A. Title warranty: the target's financial statements are true and fair.
B. Transaction warranty: the shares are fully paid and free from encumbrances.
C. Title warranty: the shares are duly authorised, validly issued, fully paid and free from encumbrances. Business warranty: no undisclosed liabilities and compliance with laws.
D. Business warranty: the seller has authority to enter into the SPA.

**Answer: C.** Transaction warranties: due authorisation, no breach, enforceability (so D is a transaction warranty). Title warranties: the shares are duly authorised, validly issued, fully paid and unencumbered. Business warranties: overall (financial statements, no undisclosed liabilities, compliance with laws) and specific (IP, employees, tax and so on). Warranties serve discovery and risk allocation, and their scope is limited by materiality and knowledge qualifiers and by whether they are brought down to completion.
*Cite: MA1 s18–19; MA2 s12–13; `ccp-2-1-9`*

### 1.II.6 — Indemnities; W&I insurance

**Q1-10** · `1.II.6` · own question · `ccp-2-1-10`

Due diligence reveals a known $5m tax dispute. The seller wants a clean exit. Which statement is BEST?

A. A general warranty that there are no tax disputes fully protects the buyer, even though the dispute has been disclosed.
B. Warranties and indemnities replace due diligence.
C. The buyer should seek a specific indemnity for the identified dispute. W&I insurance can bridge risk allocation gaps where the seller wants a clean exit: under a buy-side policy the buyer claims directly on the policy, under a sell-side policy the buyer claims against the seller, who claims on the policy.
D. Under a buy-side W&I policy the buyer must first sue the seller.

**Answer: C.** A specific indemnity addresses a negative due diligence finding. A disclosed matter neutralises the warranty, so A fails. W&I insurance covers losses from breach of warranty or under an indemnity and suits a seller wanting a clean exit. B is wrong: warranties and indemnities complement due diligence. D reverses buy-side and sell-side.
*Cite: MA1 s20; MA2 s14–15; `ccp-2-1-10`*

### 1.II.7 — Disclosure letter; fair disclosure

**QSQ-MA7** · `1.II.7` · SQ p31 Q7 [Original], official key A · `ccp-2-1-11`

Your client is purchasing all of the issued shares in a private company. The seller has provided warranties that the target company has complied with all applicable laws. Prior to signing, the seller informs your client that the target company is currently involved in an environmental investigation and includes details of the investigation in the disclosure letter. Which of the following statements is MOST ACCURATE?

A. The disclosure letter generally qualifies the warranties by disclosing matters that would otherwise constitute a breach.
B. The disclosure letter automatically terminates the warranties.
C. The disclosure letter replaces the sale and purchase agreement.
D. The disclosure letter prevents the purchaser from carrying out due diligence.

**Answer: A.** Disclosure "neutralises" a warranty: the buyer cannot claim for breach of a warranty against which the seller has fairly disclosed. The buyer should therefore seek a specific indemnity, a price cut or a different structure. The disclosure letter does not end the warranties (B), replace the SPA (C) or stop due diligence (D).
*Cite: MA1 s21; MA2 s15; SQ p115 (key A); `ccp-2-1-11`*

### 1.II.8 — Limitations of liability: de minimis, basket, caps, time limits

**Q1-11** · `1.II.8` · own question · `ccp-2-1-12`

An SPA has a de minimis of $10,000 and a $200,000 basket structured as a "deductible". The buyer has five valid claims of $50,000 each. How much can it recover?

A. $250,000.
B. $200,000.
C. Nothing, because the claims are individually below the basket.
D. $50,000: each claim is above the de minimis, the total of $250,000 exceeds the basket, and with a deductible the seller is liable only for the excess over $200,000.

**Answer: D.** De minimis claims are ignored claim by claim, and all five clear $10,000. A basket structured as a threshold makes the seller liable from the first dollar once exceeded (that would give $250,000). Structured as a deductible, the seller pays only the excess: $250,000 − $200,000 = $50,000. Caps and claim notice periods may limit liability further.
*Cite: MA1 s22; Cyril-MA §1.5.9; `ccp-2-1-12`*

### 1.II.9 — Completion deliverables: share transfer v business transfer

**Q23-57** · `1.II.9` `1.I.2` · 2023 CCP Paper 2 Q57 (no official answer) · `ccp-2-1-13` `ccp-2-3-12`

In an acquisition of shares in a Singapore private company by a buyer, which of the following actions and/or documents are involved in the transfer of shares of the Singapore private company to the buyer?

I. The seller will have to execute and deliver a share transfer form in favour of the buyer.
II. A stamp duty working sheet will need to be completed and stamp duty will need to be paid in respect of the transfer of shares.
III. A notice of transfer will need to be lodged with ACRA and the transfer is effective upon ACRA updating the Electronic Register of Members (EROM).

A. I only
B. I and II only
C. II and III only
D. I, II and III

**Answer: D.** Share sale completion involves share transfer forms and certificates (I), payment of stamp duty on the transfer (II; 0.2% on the higher of the consideration and market value, within 14 days of execution in Singapore), and lodgement with ACRA to update the electronic register of members, which is the register for a private company (III). The target's board also passes resolutions approving the transfer and appointing new directors.
*Cite: MA1 s23; TX2 s9–10; Cyril-MA §1.6; `ccp-2-1-13`, `ccp-2-3-12`*

**Q1-12** · `1.II.9` · own question · `ccp-2-1-13`

How are the target's customer contracts dealt with at completion of a business (asset) sale?

A. Each asset, liability and contract is transferred by the appropriate method: assignment, novation (with the counterparty's consent) or physical delivery.
B. Automatically, by a single share transfer form.
C. They stay with the seller company and continue to bind the buyer.
D. By lodging a notice with ACRA.

**Answer: A.** In a business sale completion depends on each asset, liability and contract. That is why business sales cause more disruption. B and D describe a share sale. C is wrong: the buyer is not bound by the seller's contracts unless they are transferred.
*Cite: MA1 s6, s23; `ccp-2-1-13`*

### 1.III Due diligence

Sub-points 1.III.1–1.III.5. Real questions: QSQ-MA6, Q23-60, Q23-59, Q23-55. Own questions: Q1-13, Q1-14.

### 1.III.1 — What due diligence is; types (legal, business, financial/tax, environmental)

**Q1-13** · `1.III.1` · own question · `ccp-2-1-14`

A buyer's advisers check the target's sites for soil contamination, its tax filings, its market position against competitors, and its material contracts. Which pairing is CORRECT?

A. Soil contamination: legal due diligence.
B. Tax filings: business due diligence.
C. Soil contamination: environmental. Tax filings: financial/tax. Market position: business/operational. Material contracts: legal.
D. Market position: legal due diligence.

**Answer: C.** Due diligence is the gathering, organising, analysing and verifying of information about a transaction, fact-finding that stems from caveat emptor. Its types are legal, business/operational (industry, competitors, R&D), financial/tax, and environmental (contamination at sites).
*Cite: MA2 s4–8; Cyril-MA §2.1; `ccp-2-1-14`*

### 1.III.2 — Purpose: seller's and buyer's perspective; relationship with warranties and indemnities

**QSQ-MA6** · `1.III.2` `1.III.5` · SQ p31 Q6 [Original], official key B · `ccp-2-1-15` `ccp-2-1-18`

Which of the following statements concerning due diligence is/are CORRECT?

I. One purpose of legal due diligence is to identify legal risks that may affect the purchaser's decision to proceed with the transaction.
II. If due diligence reveals material legal risks, the purchaser may seek to negotiate warranties, indemnities or an adjustment to the purchase price.
III. Once due diligence has been completed, the seller is no longer required to make any warranties regarding the target company.

A. I only.
B. I and II.
C. II and III.
D. All of the statements.

**Answer: B.** I: the buyer uses due diligence to check what it is buying and to structure and negotiate the deal. II: negative findings lead to warranties, indemnities or price adjustments. III is wrong: warranties do not replace due diligence and due diligence does not replace warranties. They complement each other.
*Cite: MA2 s10–15, s29–30; SQ p115 (key B); `ccp-2-1-15`, `ccp-2-1-18`*

**Q23-60** · `1.III.2` `1.III.3` · 2023 CCP Paper 2 Q60 (no official answer) · `ccp-2-1-15` `ccp-2-1-16`

Which of the following statements best describes how a seller should manage the disclosure of commercially sensitive information to a potential buyer during a due diligence process?

I. Stagger or time the release of such information to the potential buyer, depending on the status of negotiations with the potential buyer.
II. Redact commercially sensitive details of such information before sharing with the potential buyer.
III. Grant unlimited and unfettered access to such information to the potential buyer.

A. I and II only
B. II and III only
C. I and III only
D. I, II and III

**Answer: A.** One purpose of seller-side due diligence is to keep commercially sensitive documents from bidders. At the "vet and review" step the seller decides what is suitable to disclose, bearing in mind the stage of negotiations. Options include summaries, redacted contracts, release to counsel only, and tiered release, with the most sensitive documents disclosed only when a deal is likely (Cyril-MA §2.3, step 3). III defeats that purpose.
*Cite: MA2 s10–11, s17; Cyril-MA §2.2–2.3; `ccp-2-1-15`, `ccp-2-1-16`*

### 1.III.3 — The 8-step due diligence process

**Q1-14** · `1.III.3` · own question · `ccp-2-1-16`

Which step of the eight-step due diligence process is undertaken by the seller only?

A. Protect the data to be disclosed.
B. Report it.
C. Analyse the data.
D. Collaborate with teams.

**Answer: A.** The eight steps are: (1) protect the data to be disclosed (seller only); (2) acquire data; (3) vet and review it; (4) index, store and organise it; (5) distribute it; (6) collaborate with teams; (7) analyse it; (8) report it.
*Cite: MA2 s17; Cyril-MA §2.3; `ccp-2-1-16`*

See also Q23-60 under 1.III.2 (vetting sensitive data).

### 1.III.4 — Preparing the report: considerations, documents reviewed and issues, long form v exceptions-only

**Q23-59** · `1.III.4` · 2023 CCP Paper 2 Q59 (no official answer; the earlier candidate selected C) · `ccp-2-1-17`

Which of the following statements describe what a buyer looks out for when conducting legal due diligence for the purpose of an acquisition of assets of the Singapore private company?

I. Review contracts relating to the assets to determine if there are any restrictions on the transfer of such contracts.
II. Review corporate secretarial records of the Singapore private company to assess if there is a valid chain of title in respect of the shares of the Singapore private company.
III. Check on the title of any real property that the buyer will be acquiring as part of the acquisition of assets.

A. I and II only
B. II and III only
C. I and III only
D. I, II and III

**Answer: C.** The scope of due diligence depends on the deal structure. In an asset sale the key contract issue is any prohibition on assignment (I), and title to land being bought matters (III). II is a share-sale issue: chain of title to the shares matters when the buyer buys shares, not assets.
*Cite: MA2 s19–27; `ccp-2-1-17`*

**Q1-15** · `1.III.4` · own question · `ccp-2-1-17`

A buyer with a tight budget wants a due diligence report that flags only material problems. Which form should it ask for?

A. A long form report describing every document reviewed.
B. No report at all: the SPA warranties are enough.
C. A short form, "exceptions only" report covering material issues only, stating its exclusions (e.g. financial, tax, environmental) and assumptions.
D. An information memorandum prepared by the seller.

**Answer: C.** Long form reports are rare. The common form is the short form, exceptions-only report, which states its exclusions and assumptions. B is wrong: warranties do not replace due diligence. D is a seller's marketing document, not the buyer's due diligence report.
*Cite: MA2 s19–27; `ccp-2-1-17`*

### 1.III.5 — Dealing with negative findings

**Q23-55** · `1.III.5` · 2023 CCP Paper 2 Q55 (no official answer) · `ccp-2-1-18`

The buyer's advisers have conducted due diligence on a target company in connection with the buyer's evaluation of whether to acquire shares in the target company. The buyer's advisers have made negative findings in relation to the target company. Which of the following can buyer consider doing to deal with such negative findings?

I. Negotiate an adjustment to consideration to be paid by the buyer to the seller.
II. Require the seller to procure the target company to undertake the necessary rectification to address the negative findings as a condition to completion of the acquisition.
III. "Walk away" from making the acquisition.

A. I only
B. I and II only
C. II and III only
D. I, II and III

**Answer: D.** The options for negative findings include adjusting the price, restructuring, conditions to closing (rectification as a condition precedent), performance-related payments, specific indemnities and lower limits, escrow, dealing with minor issues after closing, and walking away where nothing else is adequate.
*Cite: MA1 s9; MA2 s29–30; `ccp-2-1-18`*

See also QSQ-MA6 under 1.III.2.

### 1.IV Public take-overs: the Take-over Code and other sources of law

Sub-points 1.IV.1–1.IV.4. Real question: Q23-50. Own questions: Q1-16, Q1-17, Q1-18.

### 1.IV.1 — Ambit of the Take-over Code; persons and acts covered

**Q23-50** · `1.IV.1` `1.IV.2` `1.V.1` · 2023 CCP Paper 2 Q50 (no official answer) · `ccp-2-1-19` `ccp-2-1-22`

Which of the following transactions are governed by the Singapore Takeover Code?

I. An offer to acquire all the shares of an unlisted Singapore incorporated public company with more than 50 shareholders with net tangible assets exceeding S$5 million.
II. An offer to acquire the shares of a Hong Kong company with a secondary listing on the Singapore Exchange Securities Trading Limited.
III. An offer to acquire all the shares of a Bermuda company with a primary listing on the Singapore Exchange Securities Trading Limited.
IV. The subscription for new shares in a Singapore company which is listed on the Singapore Exchange Securities Trading Limited which would result in the subscriber acquiring more than 30% of the voting rights of said company.

A. I and III only
B. I, II and III only
C. I, III and IV only
D. I, II, III and IV

**Answer: C.** The Code applies to take-overs of companies (including foreign-incorporated ones) with a primary listing on the SGX-ST (III) and of unlisted Singapore companies with more than 50 shareholders and net tangible assets of S$5 million or more (I). A subscription that takes the subscriber to 30% or more of the voting rights triggers the mandatory offer rule (IV). II is not caught: a secondary SGX listing does not bring a foreign company within the Code.
*Cite: MA3 s4–8, s16–18; Cyril-MA §3.1; `ccp-2-1-19`, `ccp-2-1-22`*

**Q1-16** · `1.IV.1` · own question · `ccp-2-1-19`

Which statement about the Take-over Code is CORRECT?

A. It is a statute passed by Parliament and enforced by the courts.
B. It applies only to companies incorporated in Singapore.
C. It applies only to offerors resident in Singapore.
D. It is a non-statutory set of rules administered by the Securities Industry Council. It binds all offerors, resident or not, and acts done or omitted both in and outside Singapore, and it also applies to REITs.

**Answer: D.** The Code is non-statutory and administered by the SIC (which acts under s 139 SFA). It binds all offerors and all acts in and outside Singapore, and covers primary-listed companies (including foreign ones), registered business trusts, qualifying unlisted public companies and trusts, and REITs. A, C and B are wrong.
*Cite: MA3 s4–8; `ccp-2-1-19`*

### 1.IV.2 — SIC waiver of the Code

**Q1-17** · `1.IV.2` · own question · `ccp-2-1-19`

A Singapore-incorporated company has its primary listing in London. Almost all its shareholders are in Europe, little of its trading happens in Singapore, and UK law protects its shareholders. Which statement is CORRECT?

A. The SIC can never waive the Code.
B. A waiver is automatic for any foreign listing.
C. The Code applies only if the company is listed in Singapore, so no waiver is needed.
D. The SIC may waive the Code for a Singapore company with a primary listing overseas, if the applicant shows few affected Singapore-based holders, limited trading in Singapore, and protection under another jurisdiction's laws.

**Answer: D.** The SIC may waive the Code for (a) foreign companies or trusts with a primary SGX-ST listing, (b) Singapore companies or trusts with a primary listing overseas, or (c) unlisted public companies or trusts otherwise caught. The applicant must show few affected Singapore-based holders, limited trading in Singapore and protection under another jurisdiction's laws. B is wrong: a waiver must be applied for.
*Cite: MA3 s4–8; Cyril-MA §3.1; `ccp-2-1-19`*

See also Q23-50 under 1.IV.1.

### 1.IV.3 — Sanctions for breach

**Q1-18** · `1.IV.3` · own question · `ccp-2-1-20`

An offeror flagrantly breaches the Take-over Code by paying one shareholder a higher price than the others. Which is NOT a sanction the SIC can impose?

A. A private reprimand or public censure.
B. Depriving the offender of the facilities of the securities market.
C. A ruling that the offeror pay other holders what they would have received had the Code been complied with, with interest.
D. A term of imprisonment imposed by the SIC itself.

**Answer: D.** The SIC can reprimand, censure, deprive the offender of market facilities, require an adviser to abstain from Code work, refer criminal offences to the authorities, and rule that holders be paid what they should have received, with interest. It cannot itself imprison anyone. Criminal matters go to the authorities.
*Cite: MA3 s9–10; Cyril-MA §3.1; `ccp-2-1-20`*

### 1.IV.4 — Other sources: Companies Act, SFA ss 139–140, Listing Manual rr 723, 1105, 1307–1309

**Q1-19** · `1.IV.4` · own question · `ccp-2-1-21`

Which pairing of provision and subject matter is CORRECT?

A. Section 140 SFA: free float requirement of 10%.
B. Rule 723 Listing Manual: offence to announce an offer without reasonable grounds to perform it.
C. Section 140 SFA: offence to make or announce a take-over offer without reasonable grounds for believing the offeror can perform its obligations if the offer is accepted. Rule 1105: trading suspended when the offeror and concert parties hold 90%.
D. Section 210 Companies Act: compulsory acquisition.

**Answer: C.** Section 140 SFA creates the offence. Rule 1105 suspends trading at 90%. Rule 723 is the 10% free float, so A and B swap them. Section 210 CA is schemes of arrangement; compulsory acquisition is s 215 (D).
*Cite: MA3 s11–14; `ccp-2-1-21`*

### 1.V General offers: mandatory, voluntary and partial

Sub-points 1.V.1–1.V.6. Real questions: Q23-49, Q23-52 (Q23-50 and Q23-51 also touch it). Own questions: Q1-20 to Q1-24.

### 1.V.1 — Mandatory offer triggers (30%; 30–50% creeping 1% in 6 months)

**Q1-20** · `1.V.1` · own question · `ccp-2-1-22`

Which acquisition triggers a mandatory general offer for a listed Singapore company?

A. Offeror X, holding 25%, buys a further 4%. Its concert parties hold nothing.
B. Offeror Z, holding 55%, buys 2% more in one month.
C. Offeror Y, holding 35%, buys 0.6% in March and 0.6% in July of the same year (within 6 months), so it has acquired 1.2% in a rolling 6-month period.
D. Offeror W, holding 20%, while its concert party holds 5%.

**Answer: C.** A mandatory offer is triggered when the offeror, with its concert parties, acquires shares carrying 30% or more of the voting rights, or when, holding between 30% and 50%, they acquire more than 1% in any rolling 6-month period. Y's 1.2% in under 6 months while between 30% and 50% triggers it. A ends at 29%. B is above 50%, where creeping does not apply. D totals 25%.
*Cite: MA3 s16–18; `ccp-2-1-22`*

See also Q23-50 under 1.IV.1 (a subscription above 30%).

### 1.V.2 — Mandatory offer conditions and price (Rule 14.3)

**Q23-49** · `1.V.2` · 2023 CCP Paper 2 Q49 (no official answer) · `ccp-2-1-23`

Which of the following requirements applies to a mandatory general offer?

I. The offer price must be in cash or accompanied by a cash alternative.
II. The mandatory general offer must be conditional upon the offeror obtaining acceptances which will result in the offeror and its concert parties holding shares carrying more than 50% of voting rights of the offeree company.
III. The offer price must be at not less than the highest price paid by the offeror or any concert party for any voting shares during the offer period and in the 3 months leading up to the date of the announcement of the mandatory general offer.

A. I only
B. I and II only
C. II and III only
D. I, II and III

**Answer: B.** A mandatory offer must be in cash or with a cash alternative (I), and conditional only on acceptances taking the offeror and concert parties above 50% (II). If they already hold more than 50%, it is unconditional. III is wrong: the look-back period for a mandatory offer is 6 months before the announcement plus the offer period (Rule 14.3). Three months is the voluntary offer rule.
*Cite: MA3 s19–24; `ccp-2-1-23`*

### 1.V.3 — Voluntary offer conditions and price

**Q1-21** · `1.V.3` · own question · `ccp-2-1-24`

An offeror launching a voluntary general offer wants to make it conditional on (1) acceptances giving it 90%, (2) regulatory approval, and (3) "the offeror being satisfied with the target's prospects". Which statement is CORRECT?

A. All three conditions are allowed.
B. A voluntary offer cannot have any condition other than 50% acceptances.
C. (1) and (2) are allowed: a voluntary offer must be conditional on more than 50% and may set a higher level, and other objective conditions may be added. (3) is not allowed, because it depends on the offeror's subjective judgment. The price may be cash, securities or both, at not less than the highest price paid in the offer period and the 3 months before the announcement.
D. A voluntary offer must be in cash.

**Answer: C.** A voluntary offer must always be conditional on acceptances above 50%. A higher level (e.g. 75% or 90%) and other conditions such as shareholder or regulatory approvals are allowed, but not conditions depending on the offeror's subjective judgment. The price may be in cash, securities or both, with a 3-month look-back.
*Cite: MA3 s22–24; `ccp-2-1-24`*

### 1.V.4 — Partial offers: SIC consent and conditions (Rule 16)

**Q1-22** · `1.V.4` · own question · `ccp-2-1-25`

An offeror holding 10% wants to make a partial offer that would take it to (a) 25% or (b) 40%. Which statement is CORRECT?

A. Partial offers never need SIC consent.
B. Consent is granted for (b) but not (a).
C. The SIC's consent is normally granted for (a), a partial offer not resulting in 30% or more (Rule 16.2), but is not granted for (b), which would result in 30% to 50% (Rule 16.3).
D. Both are prohibited outright.

**Answer: C.** A partial offer needs the SIC's consent. Below 30%: normally granted (r 16.2). 30% to 50%: not granted (r 16.3). Above 50%: granted only on conditions (r 16.4), including no acquisitions in the 6 months before and after, approval by target shareholders (the offeror and concert parties abstaining), and disclosure of statutory control.
*Cite: MA3 s25–30; `ccp-2-1-25`*

See also Q23-51 under 1.VI.4 (a partial offer for 51% needs shareholder approval).

### 1.V.5 — Offer timetable (Rule 22)

**Q23-52** · `1.V.5` · 2023 CCP Paper 2 Q52 (no official answer) · `ccp-2-1-26`

Which of the following statements about general offers are true?

I. The board of the offeree company should advise its shareholders of its views as soon as possible, and in any event no later than 14 days after the posting of the offer document.
II. The offeror must despatch its offer document no earlier than 14 days after the date of announcement of the general offer.
III. A general offer must be kept open for at least 30 days from the date the offer document is despatched.

A. I and II only
B. II and III only
C. I and III only
D. I, II and III

**Answer: A.** Under the Rule 22 timetable the offer document is posted between D+14 and D+21 after the announcement (II), and the offeree circular follows within 14 days (T+14) (I). III is wrong: the earliest closing date is T+28, so the offer must stay open at least 28 days, not 30. It must become unconditional as to acceptances by T+60.
*Cite: MA3 s31; Cyril-MA §3.2.1; `ccp-2-1-26`*

### 1.V.6 — Irrevocables, no special deals, when cash or securities offer required

**Q1-23** · `1.V.6` · own question · `ccp-2-1-27`

In the 6 months before announcing a voluntary offer, the offeror bought 12% of the target's voting shares for cash. It now wants to offer only its own shares as consideration. Which statement is CORRECT?

A. It may offer shares only, because a voluntary offer may be in securities.
B. Because it bought 10% or more of the voting rights for cash during the offer period and the 6 months before, the offer must be in cash or include a cash alternative at not less than the highest price paid.
C. It must offer cash only because it is a voluntary offer.
D. It may pay a higher price to its friends among the shareholders.

**Answer: B.** A cash offer (or cash alternative) is required where the offeror and concert parties bought for cash 10% or more of the voting rights of the class during the offer period and the 6 months before. Conversely, where they acquired 10% or more in exchange for securities in the offer period and the 3 months before, those securities must be offered to all. D breaches the no special deals rule (equal treatment). The offeror may seek irrevocable undertakings to accept.
*Cite: MA3 s32–33; `ccp-2-1-27`*

**Q1-24** · `1.V.6` · own question · `ccp-2-1-27`

Before announcing its offer, an offeror obtains from three large shareholders written promises to accept the offer. What are these, and are they allowed?

A. Irrevocable undertakings, and allowed, provided the shareholders get the same terms as everyone else (no special deals).
B. Break fees, and payable by the target.
C. Special deals, and prohibited.
D. Concert party agreements that automatically trigger a mandatory offer.

**Answer: A.** The offeror may seek irrevocable undertakings from target shareholders to accept. All shareholders must be treated equally, so the givers may not get better terms. C, B and D misdescribe them: the course treats irrevocables as a normal, permitted step in a general offer.
*Cite: MA3 s32–33; `ccp-2-1-27`*

### 1.VI Schemes, delisting, amalgamation and approvals

Sub-points 1.VI.1–1.VI.4. Real questions: Q23-47, QSQ-MA4, Q23-51. Own questions: Q1-25, Q1-26.

### 1.VI.1 — Scheme of arrangement (s 210 CA): approvals and thresholds

**Q23-47** · `1.VI.1` `1.VI.4` · 2023 CCP Paper 2 Q47 (no official answer) · `ccp-2-1-28` `ccp-2-1-31`

Which of the following approvals are required for a privatization of an offeree company listed on the Singapore Exchange Securities Trading Limited by way of a scheme of arrangement under the Companies Act 1967?

I. Approval of the Securities Industry Council.
II. Clearance of the scheme document by the SGX-ST.
III. Approval of the shareholders of the offeree company in a scheme meeting.
IV. Sanction of the scheme of arrangement by the High Court of Singapore.

A. I, II and III only
B. I, III and IV only
C. III and IV only
D. I, II, III and IV

**Answer: D.** A scheme under s 210 CA needs: SIC clearance (as all four public structures do, though the SIC exempts schemes from some rules); SGX-ST clearance of the scheme document and of the delisting; shareholders' approval at a court-convened meeting (a majority in number holding at least 75% in value of those present and voting, the offeror and concert parties abstaining); and the High Court's leave to convene the meeting and sanction of the scheme.
*Cite: MA3 s34–37, s45–47; `ccp-2-1-28`, `ccp-2-1-31`*

**Q1-25** · `1.VI.1` · own question · `ccp-2-1-28`

At a scheme meeting, 100 shareholders vote (excluding the offeror and its concert parties, who abstain). 55 vote for, holding 70% of the shares voted; 45 vote against, holding 30%. Is the scheme approved?

A. Yes: a majority in number voted for it.
B. Only the Court's sanction matters.
C. Yes: 70% is a special majority.
D. No: a majority in number is not enough. Those in favour must also hold at least 75% in value of the shares voted, and 70% falls short.

**Answer: D.** The scheme needs a majority in number of those present and voting, holding at least 75% in value of the shares voted. Both limbs must be met. Only the target's board can propose a scheme, and it takes effect when the court order is lodged with ACRA.
*Cite: MA3 s34–37; `ccp-2-1-28`*

### 1.VI.2 — Voluntary delisting (Listing Manual rr 1307, 1309): approvals, exit offer

**QSQ-MA4** · `1.VI.2` `1.VI.4` · SQ p30 Q4 [Part B 2024], official key C · `ccp-2-1-29` `ccp-2-1-31`

Which of the following approvals are required for a privatisation of an offeree company listed on the Singapore Exchange Securities Trading Limited (the "SGX-ST") by way of a voluntary delisting under Rules 1307 and 1309 of the SGX-ST Listing Manual?

I. Approval of the Securities Industry Council.
II. Approval of the SGX-ST.
III. Approval of the shareholders of the offeree company in a general meeting.
IV. Sanction of the delisting by the High Court of Singapore.

A. I only.
B. II and IV.
C. I, II and III.
D. All of the approvals.

**Answer: C.** A voluntary delisting needs: shareholders' approval in general meeting (at least 75% of the shares held by those present and voting, on a poll, the offeror and concert parties abstaining: r 1307); SGX-ST approval, subject to a fair and reasonable exit offer with a cash alternative and an IFA opinion (r 1309); and the SIC, because the exit offer must comply with the Code. No Court sanction is needed.
*Cite: MA3 s38–41, s45–47; SQ p115 (key C); `ccp-2-1-29`, `ccp-2-1-31`*

### 1.VI.3 — Amalgamation (ss 215A–215J CA)

**Q1-26** · `1.VI.3` · own question · `ccp-2-1-30`

A foreign offeror proposes to take over a Singapore-listed company by statutory amalgamation of the target with the offeror's Cayman Islands company. Which statement is CORRECT?

A. Amalgamation is available, and it needs Court sanction.
B. Amalgamation is the most common take-over structure in Singapore.
C. Statutory amalgamation under ss 215A–215J CA is available only for Singapore-incorporated companies, needs no Court approval, and is rarely used because of the directors' solvency statement requirements.
D. Amalgamation needs no shareholder approval.

**Answer: C.** Amalgamation is a statutory merger for Singapore companies only, so the Cayman company cannot amalgamate. It needs no Court approval, but it does need shareholder approval and SIC clearance. It is rarely used because of the solvency statements.
*Cite: MA3 s42–47; `ccp-2-1-30`*

### 1.VI.4 — Approvals table: shareholder, Court, SIC

**Q23-51** · `1.VI.4` `1.V.4` · 2023 CCP Paper 2 Q51 (no official answer) · `ccp-2-1-31` `ccp-2-1-25`

Which of the following take-over transactions requires shareholder approval:

I. A voluntary general offer for all the shares of the offeree company.
II. A partial offer for 51% of the shares of the offeree company.
III. A privatization of the offeree company by way of a scheme of arrangement under the Companies Act 1967.
IV. A voluntary delisting of the offeree company under Rules 1307 and 1309 of the SGX-ST Listing Manual.

A. I only
B. I and II only
C. I, II and III only
D. II, III and IV only

**Answer: D.** A general offer needs no shareholder approval; it is conditional on acceptances instead (I). A partial offer resulting in more than 50% is consented to by the SIC only on condition of approval by the target's shareholders, the offeror and concert parties abstaining (Rule 16.4) (II). A scheme and a voluntary delisting each need shareholder approval (III, IV).
*Cite: MA3 s25–30, s44–47; `ccp-2-1-31`, `ccp-2-1-25`*

See also Q23-47 under 1.VI.1 and QSQ-MA4 under 1.VI.2.

### 1.VII Concert parties

Sub-points 1.VII.1–1.VII.2. Real question: QSQ-MA5. Own question: Q1-27.

### 1.VII.1 — Definition of persons acting in concert

**Q1-27** · `1.VII.1` · own question · `ccp-2-1-32`

Investors A and B, unrelated, informally agree over dinner to buy target shares together so that between them they can control the board. Which statement is CORRECT?

A. They are not acting in concert, because there is no written agreement.
B. They are acting in concert: concert parties co-operate, under an agreement, arrangement or understanding (formal or informal), through acquiring shares to obtain or consolidate effective control. Their holdings are aggregated for the mandatory offer thresholds.
C. Only companies in the same group can act in concert.
D. Acting in concert matters only for schemes of arrangement.

**Answer: B.** The definition covers informal understandings, and the presumptions are additional categories presumed unless the contrary is shown. Acquisitions by concert parties count towards the offeror's 30% and creeping thresholds.
*Cite: MA3 s48–51; `ccp-2-1-32`*

### 1.VII.2 — Presumed concert parties (associated company = 20–50%)

**QSQ-MA5** · `1.VII.2` `1.VII.1` · SQ p29 Q5 [Part B 2024], official key C · `ccp-2-1-32`

Under the Singapore Code on Take-overs and Mergers, which of the following parties would be presumed to be acting in concert with each other?

I. A company with a corporation in which the company has a 15% shareholding interest.
II. A company with subsidiaries of its parent corporation.
III. A person with a fund that the person manages on a discretionary basis.

A. I only.
B. I and II.
C. II and III.
D. All of the parties.

**Answer: C.** A company is presumed to act in concert with its parent, subsidiaries, fellow subsidiaries and associated companies (II), and a person with any fund he manages on a discretionary basis (III). I is wrong: an associated company is one in which 20% to 50% of the equity is owned or controlled, so a 15% holding does not qualify.
*Cite: MA3 s48–51; SQ p115 (key C); `ccp-2-1-32`*

### 1.VIII Joint ventures: nature, forms and documents

Sub-points 1.VIII.1–1.VIII.4. Real questions: QSQ-MA1, QSQ-MA8, Q23-45, QSQ-MA2, QSQ-MA9, Q23-46. Own questions: Q1-28, Q1-29.

### 1.VIII.1 — What a JV is; why parties enter one; the lawyer's role

**Q1-28** · `1.VIII.1` · own question · `ccp-2-1-33`

Which statement about joint ventures in Singapore is CORRECT?

A. "Joint venture" is defined in the Companies Act.
B. Lawyers play no role until a dispute arises.
C. A joint venture must always be a partnership.
D. "Joint venture" is not legally defined. It is a collaborative business arrangement with significant integration between the parties, entered into for reasons such as cost and risk savings, access to technology or new markets. The lawyer structures it, does due diligence, obtains consents, documents it and sets up the vehicle.

**Answer: D.** There is no legal definition. A JV is an association for a particular undertaking with a view to mutual profit, each party usually contributing money, property or skill (*United Dominions Corp v Brian* (1985) 157 CLR 1). C and B are wrong.
*Cite: MA4 s3–6; Cyril-MA §4.1; `ccp-2-1-33`*

### 1.VIII.2 — Forms: corporate JV v contractual alliance

**QSQ-MA1** · `1.VIII.2` · SQ p28 Q1 [Part B 2024], official key D · `ccp-2-1-34`

Your client wishes to form a joint venture with another party to establish a manufacturing business in Singapore. The joint venture will need to borrow money from a bank and engage a contractor to build the manufacturing facility and your client does not wish to be subject to any contractual liability from the arrangements that the joint venture is a party to. Which of the following forms of joint ventures / corporate vehicles will best meet your client's criteria?

A. A company limited by guarantee.
B. A general partnership.
C. A contractual alliance.
D. A private company limited by shares.

**Answer: D.** A corporate JV is a jointly owned company that contracts in its own name, with members' liability limited to their shares. It suits equity investment and bank finance. B exposes the partners to the firm's liabilities. C has no separate entity, so each party bears the liabilities it incurs. A guarantee company is not suited to an equity-funded, profit-making business; this follows the answer key, as the slides list only corporate JVs and contractual alliances.
*Cite: MA4 s7; SQ p115 (key D); `ccp-2-1-34`*

**QSQ-MA8** · `1.VIII.2` · SQ p32 Q8 [Original], official key D · `ccp-2-1-34`

Your client intends to enter into a joint venture with another company to establish and operate a manufacturing business in Singapore. The joint venture company will enter into contracts with banks, suppliers and construction contractors. Your client wishes to minimise its exposure to personal contractual liability arising from those contracts. Which of the following forms of joint venture would BEST meet your client's objective?

A. A company limited by guarantee.
B. A general partnership.
C. A limited liability partnership.
D. A private company limited by shares.

**Answer: D.** As in QSQ-MA1: a private company limited by shares is the standard corporate JV vehicle for a continuing business funded by equity and bank loans, with members' liability limited. B exposes the partners. The answer key prefers the private company over a guarantee company and an LLP. The slides do not discuss those two vehicles, so the key's choice is the authority here.
*Cite: MA4 s7; SQ p115 (key D); `ccp-2-1-34`*

**Q23-45** · `1.VIII.2` · 2023 CCP Paper 2 Q45 (no official answer) · `ccp-2-1-34`

Your client wishes to form a joint venture with another party to invest in and develop real estate in Singapore. The joint venture will enter into the contracts with banks, contractors and suppliers and your client does not wish to be subject to any recourse arising from such contracts. Which of the following vehicles should the client use for the joint venture to best meet the client's criteria?

A. A contractual alliance.
B. A sole proprietorship.
C. A general partnership.
D. A private company limited by shares.

**Answer: D.** Only a company is a separate legal entity with limited liability that contracts in its own name, so the client has no recourse exposure beyond its shares. A contractual alliance has no separate entity, a general partnership exposes the partners, and a sole proprietorship has one owner and no limited liability.
*Cite: MA4 s7; `ccp-2-1-34`*

### 1.VIII.3 — Constitution v shareholders' agreement; key issues in the SHA

**QSQ-MA2** · `1.VIII.3` · SQ p28 Q2 [Part B 2024], official key B · `ccp-2-1-35`

Which of the following statements is/are CORRECT?

I. The constitution binds all shareholders of the joint venture company, including future shareholders.
II. The shareholders' agreement can only be amended with the consent of parties to the shareholders' agreement.
III. The constitution can be amended by shareholders in a general meeting by way of an ordinary resolution.

A. I only.
B. I and II.
C. II and III.
D. All of the statements.

**Answer: B.** The constitution is regulated by the Companies Act and binds all shareholders, present and future (I). It is amended by special resolution (75%), not ordinary resolution (III wrong). The SHA is governed by contract and binds only its parties, so it is amended only with their consent (II).
*Cite: MA4 s9–11; SQ p115 (key B); `ccp-2-1-35`*

**QSQ-MA9** · `1.VIII.3` · SQ p32 Q9 [Original], official key B · `ccp-2-1-35`

Which of the following statements concerning the constitutional documents of a joint venture company is/are CORRECT?

I. The constitution binds all shareholders of the joint venture company, including persons who become shareholders after its adoption.
II. A shareholders' agreement generally may only be amended with the consent of the parties to that agreement.
III. The constitution may be amended by the shareholders passing an ordinary resolution at a general meeting.

A. I only.
B. I and II only.
C. II and III only.
D. All of the statements.

**Answer: B.** Same rule as QSQ-MA2: I and II are correct, and III is wrong because a special resolution (75%) is needed.
*Cite: MA4 s9–11; SQ p115 (key B); `ccp-2-1-35`*

**Q23-46** · `1.VIII.3` `1.X.1` `1.X.2` `1.X.4` `1.IX.2` · 2023 CCP Paper 2 Q46 (no official answer) · `ccp-2-1-35` `ccp-2-1-39` `ccp-2-1-40` `ccp-2-1-42` `ccp-2-1-37`

Which of the following matters are commonly set out in a joint venture agreement:

I. Pre-emption, tag-along and drag-along rights.
II. Reserved matters which require the approval of shareholders.
III. Board representation rights.
IV. Deadlock resolution or divorce mechanisms.

A. I and II only
B. I, II and III only
C. II, III and IV only
D. I, II, III and IV

**Answer: D.** The key SHA issues include governance (board composition and representation, reserved matters), transfers of shares (pre-emption, tag-along, drag-along), and default and deadlock provisions, including divorce mechanisms.
*Cite: MA4 s11, s16–39; `ccp-2-1-35`, `ccp-2-1-39`, `ccp-2-1-40`, `ccp-2-1-42`, `ccp-2-1-37`*

### 1.VIII.4 — Should the JV company be a party to the SHA?

**Q1-29** · `1.VIII.4` · own question · `ccp-2-1-36`

Your client asks whether the JV company itself should sign the shareholders' agreement. Which statement is BEST?

A. The JV company must always be a party.
B. Making the JV company a party lets the shareholders amend the constitution by ordinary resolution.
C. The JV company can never be a party.
D. Making the JV company a party means it undertakes obligations directly, which are easier to enforce, especially where directors ignore shareholders' wishes or there are many parties. But in a dispute its consent may be needed, and terms that fetter its statutory powers may be unenforceable against it.

**Answer: D.** The key parties are the shareholders; the parent companies and the JV company are optional. D states the advantages and disadvantages of adding the JV company. B is wrong: the constitution is amended by special resolution.
*Cite: MA4 s12–14; `ccp-2-1-36`*

### 1.IX Joint ventures: minority protection, governance and financing

Sub-points 1.IX.1–1.IX.3. Real questions: QSQ-MA3, QSQ-MA10. Own questions: Q1-30, Q1-31.

### 1.IX.1 — Statutory minority protection under the Companies Act

**Q1-30** · `1.IX.1` · own question · `ccp-2-1-37`

Your client holds 30% of a JV company with no shareholders' agreement. Which right does it NOT have under the Companies Act alone?

A. Blocking a special resolution, because it holds more than 25%.
B. Seeking a remedy for unfairly prejudicial conduct, or winding up on just and equitable grounds.
C. Bringing a statutory derivative action for directors' breaches.
D. A veto over the company's annual budget and business plan.

**Answer: D.** A veto over the budget and business plan is a reserved matter that must be negotiated. Statutory rights are limited: blocking resolutions needing 75% (A), requisitioning meetings, information and investigations, statutory derivative actions (C), unfair prejudice (oppression) remedies and just and equitable winding up (B).
*Cite: MA4 s16–19; `ccp-2-1-37`*

### 1.IX.2 — Rights a minority should negotiate

**QSQ-MA3** · `1.IX.2` · SQ p29 Q3 [Part B 2024], official key B · `ccp-2-1-37`

Your client is a minority shareholder in a joint venture. In order to best protect his position, which of the following rights should you negotiate for?

I. Reserved matters which require the approval of the minority shareholder.
II. Board representation and information rights for the minority shareholder.
III. Call option arrangements which allow the majority shareholder to acquire the shares of the minority shareholder, if the company is sold to a third party.
IV. A provision that grants the majority shareholder the right to conduct a rights issue, which provides that the minority shareholder will pay fair market value.

A. I only.
B. I and II.
C. II and IV.
D. All of the rights.

**Answer: B.** A minority should negotiate reserved matters (a veto), board representation, information rights, protection against dilution, safeguards against the majority's breaches and exit rights. III and IV favour the majority: a call option over the minority's shares and a majority-controlled rights issue can squeeze or dilute the minority.
*Cite: MA4 s16–19; SQ p115 (key B); `ccp-2-1-37`*

**QSQ-MA10** · `1.IX.2` · SQ p32 Q10 [Original], official key B · `ccp-2-1-37`

Your client will hold a 30% shareholding in a joint venture company, with the remaining shares held by a strategic investor. Your client is concerned that the majority shareholder may make important decisions without its involvement or dilute its interest in the joint venture. Which of the following rights would BEST protect your client's interests?

I. Reserved matters requiring the minority shareholder's approval before specified decisions may be implemented.
II. The right to appoint a director to the board and receive regular financial and operational information.
III. A call option allowing the majority shareholder to require the minority shareholder to sell its shares if the joint venture is sold to a third party.

A. I only.
B. I and II only.
C. II and III only.
D. All of the above.

**Answer: B.** As in QSQ-MA3: reserved matters, a board seat and information rights protect the minority. A call option in the majority's favour (III) does not.
*Cite: MA4 s16–19; SQ p115 (key B); `ccp-2-1-37`*

### 1.IX.3 — Governance/management and financing issues

**Q1-31** · `1.IX.3` · own question · `ccp-2-1-38`

A JV's partners disagree on how future funding will be provided and what happens if one partner fails to fund. Which SHA topics address this?

A. Tag-along and drag-along rights.
B. The confidentiality agreement.
C. Financing: each party's funding obligations, shareholder loans versus outside loans, provision of security, and the consequences of default in funding.
D. Rule 14 of the Take-over Code.

**Answer: C.** Financing issues: funding obligations, shareholder loans v outside loans, security, and default consequences. Governance issues cover board composition, appointment and removal of directors (adjusted when shareholdings change), key management appointment rights, and board and shareholder proceedings (quorum, notice, approval thresholds). A deals with share transfers, and B and D are irrelevant here.
*Cite: MA4 s20–23; `ccp-2-1-38`*

### 1.X Joint ventures: share transfers, exit, deadlock and default

Sub-points 1.X.1–1.X.5. Own questions: Q1-32 to Q1-36 (Q23-46 also touches 1.X).

### 1.X.1 — Transfer restrictions; pre-emption (first offer v first refusal); transfer price

**Q1-32** · `1.X.1` · own question · `ccp-2-1-39`

Under a JV agreement, a party wishing to sell must first find a bona fide third-party buyer and notify the other party, who may buy on the same terms. If the other party declines, the seller may sell only to that buyer at the notified price. What is this right?

A. A right of first refusal.
B. A right of first offer.
C. A drag-along right.
D. An absolute prohibition on transfer.

**Answer: A.** Under a right of first refusal the seller must first find a bona fide third-party buyer, and if the right is not exercised may sell only to that buyer at the notified price. Under a right of first offer (B) the seller need not find a buyer first. The other party gets the first opportunity, and if it declines the seller may usually sell to anyone at not less than the price offered. The price may be set by the seller, by a third party's offer, or by independent valuation.
*Cite: MA4 s24–28; `ccp-2-1-39`*

### 1.X.2 — Tag-along and drag-along rights

**Q1-33** · `1.X.2` · own question · `ccp-2-1-40`

A 70% shareholder agrees to sell to a buyer who wants 100% of the JV company. The 30% minority (a) wants to sell on the same terms, or (b) refuses to sell. Which rights are relevant?

A. (a) drag-along; (b) tag-along.
B. Both are pre-emption rights.
C. (a) tag-along: the minority can require the buyer to extend the offer to it on the same terms. (b) drag-along: the majority can oblige the minority to sell at the same price, so the buyer gets 100%.
D. Neither: minorities can always block a sale.

**Answer: C.** Tag-along ("piggy-back") protects a minority from being locked in with a newcomer and gets it the same price. Drag-along lets a majority deliver the entire company. A swaps them.
*Cite: MA4 s29–30; `ccp-2-1-40`*

### 1.X.3 — Exit provisions

**Q1-34** · `1.X.3` · own question · `ccp-2-1-41`

Which is NOT one of the key exit provisions in a JV agreement?

A. A fixed term or joint renewal.
B. Put or call options.
C. A sale or IPO of the JV company.
D. A MAC clause allowing a buyer to walk away before completion of an acquisition.

**Answer: D.** A MAC clause belongs in an SPA. The exit provisions are a fixed term or joint renewal, termination for convenience or for cause, put or call options, a sale or public offering of the JV company, and deadlock provisions.
*Cite: MA4 s32; `ccp-2-1-41`*

### 1.X.4 — Deadlock: avoidance, continuity and divorce mechanisms

**Q1-35** · `1.X.4` · own question · `ccp-2-1-42`

Which pairing of deadlock mechanism and category is CORRECT?

A. Casting vote, escalation, mediation or expert determination: continuity mechanisms. Shoot-out, put/call options and winding up: divorce mechanisms. Giving one party clear voting control or limiting reserved matters: avoidance.
B. Winding up: avoidance.
C. Mediation: divorce mechanism.
D. Shoot-out (Russian roulette): continuity mechanism.

**Answer: A.** Deadlock can be handled by (1) avoiding it through the management structure, (2) continuity mechanisms that keep the JV going, or (3) divorce mechanisms that end it. D, C and B put the mechanisms in the wrong category.
*Cite: MA4 s33–39; `ccp-2-1-42`*

See also Q23-46 under 1.VIII.3.

### 1.X.5 — Default events and mechanisms

**Q1-36** · `1.X.5` · own question · `ccp-2-1-43`

A JV partner becomes insolvent. Which default mechanism is typical?

A. The insolvent partner may buy out the others at a premium.
B. Nothing: insolvency is not a default event.
C. The non-defaulting party may buy out the defaulter, or sell to it, under put/call options, often priced at a discount (or premium) against the defaulter, alongside unwinding arrangements.
D. The JV is automatically converted into a partnership.

**Answer: C.** Default events include insolvency, breach, cross-default and change in control of a party. Default mechanisms are put/call options, pricing against the defaulter, and unwinding arrangements.
*Cite: MA4 s40; `ccp-2-1-43`*

## 2 · Competition Law

### 2.I Overview: objective, CCS, the Act and its scope

Sub-points 2.I.1–2.I.3. Real questions: Q23-43, Q23-36. Own questions: Q2-1, Q2-2.

### 2.I.1 — Objective of competition law; CCS; Act and Guidelines; consumer protection and sectoral regulators

**Q23-43** · `2.I.1` · 2023 CCP Paper 2 Q43 (no official answer) · `ccp-2-2-1`

What is the objective of competition law in Singapore?

A. To protect the process of competition in Singapore and to correct market failure caused by anti-competitive behaviour which might disadvantage consumers but also other competitors and potential market entrants.
B. To prevent all unfair competition in Singapore.
C. To protect only consumers in Singapore.
D. To protect only smaller competitors.

**Answer: A.** Competition law assumes competition is good: it allocates resources efficiently and gives consumers more choice at lower prices. It corrects market failure caused by anti-competitive behaviour such as collusion or abuse of dominance. B is too wide: the Act targets the three prohibitions, not all "unfair" competition. C and D are too narrow.
*Cite: CL1 s3–7; Cyril-CL §1; `ccp-2-2-1`*

**Q23-36** · `2.I.1` `2.I.3` · 2023 CCP Paper 2 Q36 (no official answer) · `ccp-2-2-1` `ccp-2-2-3`

Which of the following products or services are not regulated by the CCCS because they are regulated under another sectoral competition law regime?

A. Telecommunications
B. Ride-hailing
C. Freight-forwarding
D. Credit cards

**Answer: A.** The CCS has no jurisdiction over sectors governed by sectoral competition legislation. The slides' examples are the Energy Market Authority and the Infocomm Media Development Authority, the regulator for telecommunications (CL1 s6). Cyril-CL §1 likewise names "telecommunications and media licensees, electricity and gas licensees". Ride-hailing is within the CCS's remit (Grab/Uber), and so are freight-forwarding and credit card services. Cyril's longer list of sector regulators (§2.2) includes MAS for financial services, but telecommunications is the clear case the slides give.
*Cite: CL1 s6; Cyril-CL §1, §2.2; `ccp-2-2-1`, `ccp-2-2-3`*

### 2.I.2 — "Undertaking"; government-owned companies; single economic unit; Government and statutory bodies

**Q2-1** · `2.I.2` · own question · `ccp-2-2-2`

A parent company and its wholly owned subsidiary, which has no real economic independence, agree that the subsidiary will not sell in Malaysia. Separately, a statutory board agrees prices with a private company for a public function. Which statement is CORRECT?

A. The parent–subsidiary agreement infringes s 34.
B. Only Singapore-owned companies are undertakings.
C. Government-owned companies are never subject to the Act.
D. The parent and the subsidiary form a single economic unit, so they are not separate undertakings and their agreement is outside s 34. The Act does not apply to statutory bodies (or the Government, or persons acting on their behalf).

**Answer: D.** An undertaking is any person capable of commercial or economic activity, whether foreign- or Singapore-owned. A parent and a subsidiary with no real economic independence (judged by shareholding, board control and influence over commercial policy) are one undertaking. Government-owned companies are covered when they engage in commercial activity (so C is wrong), but the Government and statutory bodies are not.
*Cite: CL1 s8; Cyril-CL §1, §2.1.1; `ccp-2-2-2`*

### 2.I.3 — Three prohibitions (ss 34, 47, 54); statutory exclusions in Third and Fourth Schedules

**Q2-2** · `2.I.3` · own question · `ccp-2-2-3`

Which pairing of prohibition and conduct is CORRECT?

A. Section 34: anti-competitive agreements. Section 47: abuse of a dominant position. Section 54: mergers that substantially lessen competition. The Third Schedule excludes matters from ss 34 and 47; the Fourth Schedule from s 54.
B. Section 47: two competitors agree to fix prices.
C. Section 54: a dominant firm's predatory pricing.
D. The Fourth Schedule excludes matters from s 34.

**Answer: A.** The behavioural prohibitions are s 34 ("cartel-like") and s 47 ("monopoly-like"), and the structural prohibition is s 54. B belongs under s 34 and C under s 47. D is wrong: the Fourth Schedule excludes mergers from s 54.
*Cite: CL1 s9, s11; `ccp-2-2-3`*

See also Q23-36 under 2.I.1 (sector regulators).

### 2.II Section 34: anti-competitive agreements

Sub-points 2.II.1–2.II.6. Real questions: Q23-31, Q23-32, QSQ-CL2. Own questions: Q2-3 to Q2-7.

### 2.II.1 — Agreements, decisions of associations, concerted practices; extraterritorial reach

**Q23-31** · `2.II.1` · 2023 CCP Paper 2 Q31 (no official answer) · `ccp-2-2-4`

In CCS 500/001/11 (Indonesian Foreign Domestic Workers), if anticompetitive information is being discussed in a meeting, what should a mere participant do to avoid liability for the entity he represents?

A. Remain in the meeting and take notes.
B. Remain in the meeting but subsequently not act on the information received.
C. Leave the meeting quietly when no-one is noticing.
D. Leave the meeting while expressing manifest opposition to the other participants and publicly distance themselves from the anticompetitive conduct discussed at the meeting.

**Answer: D.** Attending a meeting with an anti-competitive purpose, without manifest opposition or public distancing, is treated as tacit approval (CCS 500/001/11, as summarised by Cyril). A participant must object openly and distance itself. A, B and C each leave it looking like a party to the arrangement: there is no public distancing, and a recipient of sensitive information is presumed to take it into account.
*Cite: CL2 s6–7; Cyril-CL §2.1; `ccp-2-2-4`*

**Q2-3** · `2.II.1` · own question · `ccp-2-2-4`

A trade association circulates a "non-binding recommended fee schedule" to its members, most of whom follow it. Separately, two foreign manufacturers agree in Tokyo to fix prices for goods sold into Singapore. Which statement is CORRECT?

A. Neither is caught: the recommendation is non-binding, and the agreement was made abroad.
B. Only written, legally enforceable agreements are caught.
C. Both may be caught by s 34. Decisions of associations include even non-binding recommendations that coordinate members' conduct, and both the association and its members can be fined. Agreements made outside Singapore are caught if they affect competition in Singapore.
D. Only the trade association can be liable, never its members.

**Answer: C.** Section 34 covers agreements, decisions by associations of undertakings and concerted practices whose object or effect is to restrict competition in Singapore. An agreement needs only a meeting of minds: it may be oral, informal or unenforceable. Extraterritorial agreements are caught by their effect in Singapore.
*Cite: CL2 s6–7; Cyril-CL §2.1; CL-CS1 s14, s17; `ccp-2-2-4`*

### 2.II.2 — Object v effect; hard-core restrictions; appreciability (20%/25%; SMEs)

**Q2-4** · `2.II.2` · own question · `ccp-2-2-5`

Two competitors with a combined market share of 12% agree to rotate which of them wins government tenders. Which statement is CORRECT?

A. The agreement is not appreciable because their combined share is below 20%.
B. Bid rotation is lawful if each party wins equally.
C. The CCS must prove actual price effects.
D. Bid-rigging is a hard-core restriction by object, presumed always to have an appreciable adverse effect on competition, whatever the parties' market shares or intentions.

**Answer: D.** Price-fixing, market sharing, bid-rigging (cover pricing, bid suppression, bid rotation), output limitation and sharing sensitive information are hard-core and presumed appreciable. The 20% (competitors) and 25% (non-competitors) safe harbours, and the SME safe harbour, apply only to agreements assessed on their effects. C is wrong: a restriction by object needs no proof of effect.
*Cite: CL2 s7–8; CL-CS1 s5; Cyril-CL §2.1.2; `ccp-2-2-5`*

### 2.II.3 — Information exchange: when dangerous, when acceptable; one-way disclosure (Ferry Operators)

**Q23-32** · `2.II.3` `2.II.6` · 2023 CCP Paper 2 Q32 (no official answer) · `ccp-2-2-6` `ccp-2-2-9`

In CCS 500/006/9 (Ferry Operators), what principle was established?

A. Competitors must exchange competitively-sensitive information on a reciprocal basis in order for liability to be established.
B. Mere receipt of competitively-sensitive information is sufficient to establish liability.
C. Exchange of competitively-sensitive information is only problematic in cases of duopolies.
D. To avoid liability, exchange of competitively-sensitive information should not be by email. Instead it should be by text messaging.

**Answer: B.** In *Ferry Operators to Batam* the exchange and one-way provision of sensitive price information was a concerted practice with an anti-competitive object (para 68). Even mere receipt, without reciprocity, raises the presumption that the recipient's future conduct will not be independent, so a recipient should reply that it does not want the information. A is the opposite. C and D are wrong: the medium and the number of firms do not cure the exchange, though market structure informs the analysis.
*Cite: CL2 s8–10, s13; CL-CS1 s4–7; `ccp-2-2-6`, `ccp-2-2-9`*

**Q2-5** · `2.II.3` · own question · `ccp-2-2-6`

Which information exchange between competitors is generally ACCEPTABLE?

A. Each firm's planned price increases for next quarter.
B. Individualised data on intended future output.
C. Industry-wide sales figures from three years ago, aggregated so that no firm's data can be identified.
D. Each firm's current customer-by-customer prices.

**Answer: C.** Information that is publicly available or non-commercially sensitive (non-strategic, sufficiently historic, sufficiently aggregated) is generally acceptable. Exchanging individualised data on intended future prices, output or production is a restriction by object (A, B; CCS Guidelines para 3.25). D is current, individualised and strategic.
*Cite: CL2 s8–10; CL-CS1 s4–5; `ccp-2-2-6`*

### 2.II.4 — Vertical agreements exclusion; hub-and-spoke; IP licences

**Q2-6** · `2.II.4` · own question · `ccp-2-2-7`

A supplier agrees with each of its retailers on the terms for reselling its goods. Through the supplier, the retailers also pass each other their planned retail prices. Which statement is CORRECT?

A. Both arrangements are excluded from s 34 as vertical agreements.
B. Pure IP licensing agreements are excluded as vertical agreements.
C. Vertical agreements are always hard-core.
D. The supply terms between supplier and retailer are a vertical agreement excluded from s 34 (Third Schedule). But a vertical relationship does not stop a horizontal concerted practice: passing rivals' prices through a common supplier is a hub-and-spoke arrangement, judged by the nature of the agreement, not the relationship.

**Answer: D.** Vertical agreements, between undertakings at different levels of the chain on the conditions for buying, selling or reselling, are excluded because they are generally pro-competitive. But the key is the nature of the agreement, so hub-and-spoke exchanges between retailers are not excluded. B is wrong: IP provisions are covered only if ancillary to the sale or resale of goods, and pure IP licences are not excluded.
*Cite: CL2 s11; CL-CS1 s9, s12; Cyril-CL §2.1.2, §2.2; `ccp-2-2-7`*

### 2.II.5 — Other Third Schedule exclusions; net economic benefit; block exemptions; guidance and decisions

**Q2-7** · `2.II.5` · own question · `ccp-2-2-8`

Two competitors plan an R&D collaboration that will speed up new product development. They want comfort that it does not infringe s 34. Which statement is CORRECT?

A. They must notify the CCS before starting.
B. The agreement is excluded if it has a net economic benefit (Third Schedule para 9): it improves production or distribution or promotes technical or economic progress, imposes no restrictions that are not indispensable, and does not allow competition to be eliminated for a substantial part of the goods or services. Notification is voluntary, but they may seek CCS guidance or a decision, which can give immunity from penalties.
C. Net economic benefit is available only for mergers.
D. Block exemptions must be notified agreement by agreement.

**Answer: B.** Notification is voluntary (A wrong). The net economic benefit exclusion applies to s 34 agreements (C wrong). The Minister may make block exemption orders for categories of agreements meeting the same criteria (s 41), and agreements within them need not be notified (D wrong).
*Cite: CL2 s15; Cyril-CL §2.2–2.4; `ccp-2-2-8`*

### 2.II.6 — Core cases: Broiler Chickens, Ferry Operators, Ball Bearings, SIA/ANA; pricing algorithms

**QSQ-CL2** · `2.II.6` `2.II.1` · SQ p33 Q2 [Part B 2024], official key A · `ccp-2-2-9` `ccp-2-2-4`

Manufacturer A (60% market share) and Manufacturer B (30% market share) are the only suppliers of medical device X in Singapore. They implement nearly identical "dynamic pricing" algorithms that adjust prices based on market conditions. A smaller competitor complains of de facto price coordination. However: A developed its algorithm internally; B licensed a third-party algorithm; both claim the similarity is due to responding to the same market factors. Which scenario is MOST LIKELY to raise concerns under Section 34 of the Competition Act 2004?

A. Only if there's evidence of direct communication about the algorithms.
B. The use of similar algorithms alone is sufficient for a violation.
C. Only if the algorithms explicitly take into account each other's prices.
D. This scenario is unlikely to raise concerns without additional evidence.

**Answer: A.** Section 34 needs an agreement or concerted practice: a meeting of minds or practical cooperation knowingly substituted for the risks of competition. Independently developed algorithms reacting to the same market factors amount to parallel behaviour. Concern arises with evidence of communication or coordination about the algorithms. B is wrong: similarity alone is not collusion. C is wrong: reacting to rivals' prices unilaterally is not itself an agreement. D is closer, but the key picks A because it names the evidence that would raise the concern.
*Cite: CL2 s6–7, s12–16; SQ p115 (key A); `ccp-2-2-9`, `ccp-2-2-4`*

See also Q23-32 under 2.II.3 (Ferry Operators).

### 2.III Market definition

Sub-point 2.III.1. Real questions: QSQ-CL4, QSQ-CL9. Own question: Q2-8.

### 2.III.1 — Product and geographic market; SSNIP / hypothetical monopolist; demand- and supply-side substitution; SATS/SFI

**QSQ-CL4** · `2.III.1` · SQ p34 Q4 [Part B 2024], official key D · `ccp-2-2-10`

The CCS considers various factors when defining relevant markets in its assessments. In relation to geographic market definition, which of the following statements is MOST ACCURATE based on CCS' guidelines and past decisions?

A. CCS always limits its geographic market definition to Singapore's national boundaries.
B. CCS consistently defines global markets for all industries due to Singapore's open economy.
C. CCS considers only ASEAN countries in its geographic market definitions.
D. CCS defines geographic markets flexibly, which may extend beyond Singapore depending on the specific facts of the relevant matter.

**Answer: D.** The geographic market, like the product market, is the smallest area in which a hypothetical monopolist could profitably sustain a SSNIP. It depends on the facts and may extend beyond Singapore. A, B and C impose fixed rules the CCS does not apply.
*Cite: CL3 s7, s16–17; SQ p115 (key D); `ccp-2-2-10`*

**QSQ-CL9** · `2.III.1` · SQ p37 Q9 [Original], official key A · `ccp-2-2-10`

The Competition Authority of Arcadia ("CAA") is investigating an alleged anti-competitive agreement involving five luxury resorts located on the Paradise Coast. The five resorts are accused of exchanging sensitive pricing and occupancy data. The CAA must define the relevant market to assess whether the agreement significantly restricts competition. The resorts argue that their services compete with a wide range of accommodations, including budget hotels, vacation rentals, and even short-term rental platforms. They claim that if prices increase, corporate customers could easily switch to these alternatives. However, the CAA's preliminary investigation reveals: (i) corporate customers prefer luxury resorts for their bundled services (conference facilities, premium dining, etc.), which are not offered by budget hotels or most vacation rentals; (ii) short-term rental platforms are rarely used by corporate clients due to inconsistent service quality and lack of professional amenities; (iii) the geographic market is limited to the Paradise Coast because corporate customers typically require accommodations close to their event venues in this area. Assuming the competition laws in this country are similar to those in Singapore, which of the following is the MOST LIKELY relevant market in this case?

A. The market for luxury resort accommodation on the Paradise Coast catering specifically to corporate customers.
B. The market for all types of accommodation across Arcadia.
C. The market for all accommodations on the Paradise Coast without distinguishing between customer types.
D. The market for luxury resort accommodation across Arcadia without limiting it to the Paradise Coast.

**Answer: A.** Start from the focal product and ask what buyers regard as reasonable substitutes (demand-side substitution). Facts (i) and (ii) show that corporate customers would not switch to budget hotels or rentals, so the product market is luxury resorts for corporate customers. Fact (iii) confines the geographic market to the Paradise Coast. The authority need not accept the parties' wide definition (compare *SATS/SFI*, where the CCS split contract catering into segments). B, C and D are too wide.
*Cite: CL3 s7, s16–17; SQ p115 (key A); `ccp-2-2-10`*

**Q2-8** · `2.III.1` · own question · `ccp-2-2-10`

In defining a relevant product market, what does the SSNIP test ask?

A. Whether a hypothetical monopolist of the focal product (and area) could profitably sustain a small but significant non-transitory increase in price. If customers would switch to other products in enough numbers to make the increase unprofitable, those products are added to the market, until the smallest group where the increase would be profitable is found.
B. Whether the parties' combined market share exceeds 40%.
C. Whether the products are physically identical.
D. Whether the CCS accepts the parties' own market definition.

**Answer: A.** That is the hypothetical monopolist (SSNIP) test, considering demand-side and supply-side substitution. B confuses it with the merger thresholds. C is wrong: substitutes need not be identical. D is wrong: the CCS need not accept the parties' definition (*SATS/SFI*). In practice competition economists are engaged.
*Cite: CL3 s7, s16–17; CL-LP p6; `ccp-2-2-10`*

### 2.IV Section 47: abuse of a dominant position

Sub-points 2.IV.1–2.IV.4. Real questions: QSQ-CL5, QSQ-CL7, Q23-35, Q23-34. Own questions: Q2-9, Q2-10.

### 2.IV.1 — Three-step test; dominance (60% indicative; barriers; buyer power; collective dominance)

**Q2-9** · `2.IV.1` · own question · `ccp-2-2-11`

A firm has a 65% share of a market with high barriers to entry (network effects, sunk costs). Which statement is CORRECT?

A. It infringes s 47 simply by being dominant.
B. A 60% share is indicatively presumed dominant, and barriers to entry support dominance. But dominance itself is not an offence: s 47 is infringed only if the firm abuses its dominant position (after the relevant market is defined, dominance is shown, and abuse is established).
C. Dominance requires a share of at least 80%.
D. Dominance can never be held collectively by two firms.

**Answer: B.** The three steps are market, dominance and abuse. Dominance is the ability profitably to sustain prices above competitive levels, or restrict output or quality below them. 60% is indicative, and dominance may exist below it (C wrong). Two or more independent undertakings may be collectively dominant (D wrong).
*Cite: CL3 s5–8; Cyril-CL §3.1; `ccp-2-2-11`*

See also QSQ-CL7 under 2.IV.2 (market share alone is not abuse).

### 2.IV.2 — Forms of abuse: predation, rebates, exclusivity, tying, refusal to supply, margin squeeze

**QSQ-CL5** · `2.IV.2` · SQ p35 Q5 [Part B 2024], official key C · `ccp-2-2-12`

Company X is the dominant provider of online food delivery services in Singapore, with an estimated market share of 80%. Company X has exclusive arrangements with many popular restaurants, preventing them from listing on other delivery platforms. A new competitor, Company Y, enters the market and starts offering delivery services to restaurants not exclusive to Company X. In response, Company X offers its existing restaurant partners a 30% reduction in commission fees if they extend their exclusive contracts for an additional 2 years. Which of the following statements BEST DESCRIBES whether Company X's actions in this scenario could be considered an abuse of its dominant position under Section 47 of the Competition Act 2004?

A. Company X's actions are clearly an abuse of dominance, as offering discounts to customers is anti-competitive.
B. Company X's actions are not an abuse, as it is simply competing on merit by offering better terms to its customers (the restaurants).
C. Company X's actions may be an abuse if the discounts are predatory and designed to eliminate the new competitor Company Y.
D. Company X's actions are not an abuse, as the new competitor Company Y is still free to compete for non-exclusive restaurants.

**Answer: C.** Discounts are not abusive in themselves (A wrong). But a dominant firm's exclusivity-conditioned discounts aimed at a new entrant can foreclose competition (exclusive contracts, loyalty rebates and predation are all in the foreclosure grid). Whether it is abuse depends on the effect on the competitive process. B and D ignore the exclusionary effect.
*Cite: CL3 s9–10; SQ p115 (key C); `ccp-2-2-12`*

**QSQ-CL7** · `2.IV.2` `2.IV.1` · SQ p36 Q7 [Original], official key C · `ccp-2-2-12` `ccp-2-2-11`

MediLink is a fictional leading medical equipment distribution platform in Singapore, with an estimated market share of 85–95%. MediLink has entered into exclusive agreements with major hospitals, clinics and medical device manufacturers, requiring them to use MediLink as their sole distribution channel for all medical equipment. These agreements typically last for three to five years. As a result, most medical equipment in Singapore can only be accessed through MediLink's platform. A competitor, HealthTech, has lodged a complaint with CCS, alleging that these exclusive agreements make it impossible for it to compete effectively in the market. Which of the following statements most accurately reflects how CCS would be likely to assess the complaint?

A. CCS would need to establish that MediLink intentionally sought to exclude competitors before finding an infringement.
B. MediLink's high market share alone is sufficient to establish an abuse of dominance, regardless of the exclusive agreements.
C. CCS would be likely to conclude that MediLink holds a dominant position and that the exclusive agreements amount to an abuse of that position by foreclosing competition.
D. The exclusive agreements are justified because they generate efficiency benefits for hospitals, clinics and manufacturers, and therefore cannot constitute an abuse of dominance.

**Answer: C.** An 85–95% share is well above the indicative 60%, and long exclusive agreements covering most of the market foreclose rivals: an adverse effect on the competitive process. A is wrong: intent need not be proved; a likely effect is enough. B is wrong: dominance alone is not abuse. D is wrong: objective justification is for the dominant firm to prove, and the conduct must be proportionate. It is not automatic.
*Cite: CL3 s5–10, s15; SQ p115 (key C); `ccp-2-2-12`, `ccp-2-2-11`*

**Q23-35** · `2.IV.2` · 2023 CCP Paper 2 Q35 (no official answer) · `ccp-2-2-12`

What kind of abuse is a "margin squeeze"?

A. A non-price based exclusion resulting in horizontal foreclosure.
B. A non-price based exclusion resulting in vertical foreclosure.
C. A price based exclusion resulting in horizontal foreclosure.
D. A price based exclusion resulting in vertical foreclosure.

**Answer: D.** In the foreclosure grid (CL3 s10), margin squeeze sits under vertical foreclosure, price-based. A covers single branding, tying and exclusive contracts. B covers discrimination and constructive refusal. C covers loyalty rebates and predation.
*Cite: CL3 s10; `ccp-2-2-12`*

### 2.IV.3 — Cases: SISTIC, Coca-Cola; loyalty rebates

**Q23-34** · `2.IV.3` · 2023 CCP Paper 2 Q34 (no official answer) · `ccp-2-2-13`

What was the CCCS' theory of harm in CCS/600/008/7 (Abuse of a dominant position by SISTIC.com)?

A. SISTIC's increase in the booking fee from S$2 to S$3 in 2008.
B. SISTIC's requirements that promoters presenting events at Esplanade and SIS sell tickets through SISTIC, notwithstanding the efficiencies claimed by SISTIC and the fact that such exclusivity agreements were terminable.
C. SISTIC's prohibition on all promoters it worked with to use any other ticketing service provider even when presenting at venues other than Esplanade and SIS.
D. SISTIC sale of 50% of tickets to scalpers who could increase prices as they wished.

**Answer: B.** The CCS built a circular theory of harm: exclusive agreements with venues and promoters, secured with discounts, artificially perpetuated SISTIC's dominance and let it reap monopoly benefits from ticket buyers. The CAB upheld the decision (CAB 1/2010). B is the option that describes the exclusive agreements as the harm. A describes a consequence of dominance (higher booking fees), not the theory of harm. C overstates the exclusivity: the pack ties it to the venues and promoters. D has no basis. The pack does not hold the case's venue-by-venue detail, but the exclusivity theory picks B.
*Cite: CL3 s11–14; Cyril-CL §3.1 (case studies); `ccp-2-2-13`*

**Q2-10** · `2.IV.3` · own question · `ccp-2-2-13`

After a complaint about its supply terms with on-premise retailers, Coca-Cola Singapore Beverages gave undertakings to the CCS in 2013. Which was NOT one of them?

A. No exclusivity restrictions.
B. No loyalty-inducing rebates.
C. No exclusive use of display space: retailers may use up to 20% of Coca-Cola's cooler space for other brands.
D. A divestment of its bottling plant.

**Answer: D.** The undertakings were behavioural: no exclusivity, no right of first refusal, no loyalty-inducing rebates, and no exclusive use of display space (20% of cooler space for others). Loyalty rebates are generally pro-competitive but may exclude depending on their structure, e.g. retroactive rebates on all units once a threshold is met.
*Cite: CL3 s11–14; Cyril-CL §3.1; `ccp-2-2-13`*

### 2.IV.4 — Objective justification; conduct not abusive; exclusions and guidance

**Q2-11** · `2.IV.4` · own question · `ccp-2-2-14`

A dominant supplier refuses to supply a buyer with a record of not paying its bills, and prices cinema tickets differently by time slot according to demand elasticity. Which statement is CORRECT?

A. Both are automatically abusive because the supplier is dominant.
B. Objective justification is available only under s 34.
C. The CCS bears the burden of disproving any justification.
D. Both may be objectively justified: refusing to supply a buyer with poor creditworthiness, and "Ramsey pricing" by price elasticity (e.g. movie tickets). The dominant firm bears the burden of showing objective justification and proportionality.

**Answer: D.** A dominant firm may show objective justification, with the burden on it, and must show that its conduct is proportionate. Examples: Ramsey pricing, long-run incremental cost pricing, refusing to supply poor credit risks. Dominance gained by efficiency, or the legitimate exercise of IP rights, is not abuse. Third Schedule exclusions also apply to s 47.
*Cite: CL3 s15; Cyril-CL §3.1–3.3; `ccp-2-2-14`*

### 2.V Section 54: merger control — substance

Sub-points 2.V.1–2.V.5. Real questions: Q23-38, QSQ-CL6, Q23-39, Q23-40. Own questions: Q2-12, Q2-13, Q2-14.

### 2.V.1 — What is a merger: legal and de facto control, minority shareholdings, full-function JVs

**Q23-38** · `2.V.1` · 2023 CCP Paper 2 Q38 (no official answer) · `ccp-2-2-15`

If a private equity investor acquires a 20% stake in an investee company, in what circumstances would the investor acquire sole control giving rise to merger control rules applying?

A. If the investor company has additional rights which allow them to veto decisions in respect of strategic and business plans, budget and senior management appointments.
B. If the investor company has an existing portfolio company which has horizontal overlaps with the investee company.
C. If the investee company has a market share of 60% in respect of one of its products.
D. If the investee company operates in a market which has high entry barriers.

**Answer: A.** Control means decisive influence (s 54(3)). A minority shareholding confers control if it carries vetoes over strategic decisions (budget, business plan, major investments, senior management). B, C and D go to whether the merger substantially lessens competition, not to whether there is a merger at all.
*Cite: CL4 s6; Cyril-CL §4.2.1; `ccp-2-2-15`*

**Q2-12** · `2.V.1` · own question · `ccp-2-2-15`

Two companies set up a jointly controlled company to do R&D for them only. It has no market access or sales of its own. Is this a merger under s 54?

A. No: a JV is a merger only if it is under joint control, is an autonomous economic entity performing all the functions of a stand-alone business (not just R&D, production or a sales agency), and operates on a lasting basis (s 54(5)).
B. Yes, if the parents hold 50% each.
C. Yes: every joint venture is a merger.
D. No, because JVs are excluded by the Fourth Schedule.

**Answer: A.** An R&D-only JV is not full-function. C and B ignore the full-function test. D is wrong: there is no blanket Fourth Schedule exclusion for JVs.
*Cite: CL4 s6; `ccp-2-2-15`*

### 2.V.2 — Excluded mergers (s 54(7); Fourth Schedule)

**Q2-13** · `2.V.2` · own question · `ccp-2-2-16`

Which acquisition of control is NOT a merger under s 54(7)?

A. Company A buys 60% of a competitor.
B. Two companies form a full-function JV.
C. A private equity fund acquires a 25% stake with veto rights over the budget.
D. A liquidator, acting as such, takes control of an insolvent company. (Likewise: an intra-group restructuring, control acquired on death, and a financial institution's temporary holding of securities for disposal within 12 months.)

**Answer: D.** Section 54(7) excludes control acquired by a receiver, liquidator or underwriter acting as such; undertakings already under common control (intra-group); control acquired on death; and temporary holdings by financial institutions. A, C and B are mergers.
*Cite: CL4 s5; Cyril-CL §4.2.2; `ccp-2-2-16`*

### 2.V.3 — Indicative thresholds (40%; 20–40% with CR3 ≥ 70%)

**Q2-14** · `2.V.3` · own question · `ccp-2-2-17`

After a merger, the merged firm will have 30% of a market in which the three largest firms together hold 75%. Is the merger likely to concern the CCS?

A. Yes, potentially: a merged share of 20% to less than 40% with a CR3 of 70% or more meets the indicative threshold. The thresholds are indicative only, and the shares depend on market definition.
B. No, because its share is below 40%.
C. No, because CR3 is irrelevant.
D. Yes, because any merger above 20% is prohibited.

**Answer: A.** The CCS is unlikely to be concerned unless (a) the merged share is 40% or more, or (b) it is 20% to less than 40% and CR3 is at least 70%. Limb (b) applies here. D overstates: crossing a threshold is not a prohibition.
*Cite: CL4 s5, s8; `ccp-2-2-17`*

### 2.V.4 — SLC test: counterfactual; horizontal, vertical, conglomerate; non-coordinated and coordinated effects; foreclosure

**QSQ-CL6** · `2.V.4` · SQ p35 Q6 [Part B 2024], official key B · `ccp-2-2-18`

Two of the largest e-commerce platforms in a Southeast Asian country, ShopEase and QuickCart, which hold market shares of 50% and 30% respectively, have announced plans to merge. ShopEase owns a widely used payment gateway that many online retailers rely on, while QuickCart has invested heavily in logistics infrastructure, including same-day delivery services. Post-merger, the combined entity would handle 80% of all online retail transactions in the country and gain significant control over payment and delivery systems. Assuming the competition laws in this country are similar to those in Singapore, what is the most likely concern for the competition authority?

A. The merger will result in coordinated effects, as smaller e-commerce platforms will collude with the merged entity to fix prices.
B. The merger will create vertical effects, as the combined entity could restrict access to its payment gateway and logistics services to disadvantage competitors.
C. The merger will lead to conglomerate effects, as the new entity may use its dominance in e-commerce to expand into unrelated markets like digital advertising or cloud computing.
D. The merger will increase competition by lowering prices for consumers due to operational efficiencies and economies of scale.

**Answer: B.** Control of upstream inputs that rivals rely on (payments and logistics) raises vertical foreclosure concerns. A: nothing suggests the market structure makes collusion more likely. C: conglomerate effects rarely raise concerns, and the facts point to foreclosure. D: efficiencies must be proved with verifiable evidence and do not answer the concern.
*Cite: CL4 s4–13; SQ p115 (key B); `ccp-2-2-18`*

**Q23-39** · `2.V.4` · 2023 CCP Paper 2 Q39 (no official answer) · `ccp-2-2-18`

Which of the following market characteristics would the CCCS take into account as to whether a merger will give rise to non-coordinated effects?

A. The market which the merger parties operate in are transparent.
B. The merger parties are each other's closest rivals.
C. Demand and supply in the market the merger parties operate in is stable.
D. One of the merger parties is not headquartered in Singapore.

**Answer: B.** Non-coordinated (unilateral) effects arise where the merged firm can profitably raise prices because lost sales are recaptured by the other party. Closeness of competition is the key factor, along with switching behaviour, buyer power and capacity constraints. A and C (transparency, stable demand and costs) are coordinated-effects factors. D is irrelevant.
*Cite: CL4 s9–12; `ccp-2-2-18`*

**Q23-40** · `2.V.4` · 2023 CCP Paper 2 Q40 (no official answer) · `ccp-2-2-18`

When reviewing a merger, would the CCCS take into account potential competition that has not yet entered Singapore at time the merger takes place?

A. No, it would not.
B. Yes, as long as the potential competitor is in the same market as the merged entity.
C. Yes, if the goods supplied by the merged entity can be purchased online.
D. Yes, if response to any exercise of market power by the merged entity post-merger, entry of new competition can be achieved in a timely and sufficient manner and entry barriers are low.

**Answer: D.** Low barriers to entry and potential competition mitigate competition concerns. The CCS examines barriers to entry and whether new competitors are likely to enter "timely and sufficiently" to maintain competition (Cyril-CL §4.2.4). A ignores potential competition. B and C name the wrong tests.
*Cite: CL4 s9–12; Cyril-CL §4.2.4; `ccp-2-2-18`*

### 2.V.5 — Net economic efficiencies

**Q2-15** · `2.V.5` · own question · `ccp-2-2-19`

Merging parties claim efficiencies that outweigh any substantial lessening of competition. Which evidence is MOST persuasive?

A. A statement that the merger will increase the parties' profits.
B. Efficiencies that would arise anyway without the merger.
C. Detailed and verifiable evidence, such as board papers and internal documents on the rationale, showing efficiencies that are merger-specific, timely and, where possible, quantified, e.g. removal of double mark-ups or increased innovation, ideally passed through to customers.
D. Unquantified press statements.

**Answer: C.** A merger that would substantially lessen competition is not prohibited if net economic efficiencies outweigh it. Profits for the parties alone are unlikely to count (A). Pass-through is not required but is persuasive. Efficiencies must be merger-specific (B fails) and verifiable (D fails).
*Cite: CL4 s13; Cyril-CL §4.2.4; `ccp-2-2-19`*

### 2.VI Section 54: filing, remedies and core merger cases

Sub-points 2.VI.1–2.VI.3. Real questions: QSQ-CL3, QSQ-CL8, Q23-42, Q23-41. Own question: Q2-16.

### 2.VI.1 — Voluntary, non-suspensory regime; risks of not notifying; cross-border mergers

**QSQ-CL3** · `2.VI.1` · SQ p34 Q3 [Part B 2024], official key B · `ccp-2-2-20`

After Company A has acquired Company B, the combined market share of the two companies in the relevant market in Singapore became 45%. Company A's management decided to close the deal quickly due to competitive pressures without notifying the CCS. Which of the following statements MOST ACCURATELY reflect the consequences of doing so under Singapore's merger control regime?

A. Company A is in breach for not notifying as it must notify CCS and obtain approval before closing.
B. Company A is not in breach for not notifying but risks CCS potentially unwinding the merger later.
C. Company A is in breach for not notifying as it must wait for CCS approval before closing the deal.
D. Company A is not in breach for not notifying and not at any risk of penalties.

**Answer: B.** The regime is voluntary and non-suspensory: there is no duty to notify or to wait for approval (A and C wrong). But the parties must self-assess. A 45% share is above the indicative threshold, so they risk an order to unwind (an "evergreen" risk) and higher penalties if the merger is found to infringe (D wrong).
*Cite: CL4 s14–17; SQ p115 (key B); `ccp-2-2-20`*

**QSQ-CL8** · `2.VI.1` · SQ p37 Q8 [Original], official key A · `ccp-2-2-20`

Two global technology companies, Y and Z, have announced plans to merge. Neither company is incorporated in Singapore, but both derive significant revenue from Singaporean customers through their cloud-based services and online platforms. The merger has been approved by the competition authorities in the United States and the European Union. CCS is now considering whether to review the merger. Which of the following approaches is most consistent with CCS's established practice in assessing such cross-border mergers?

A. CCS will conduct its own assessment, focusing on the merger's likely effects on competition in Singapore, regardless of the decisions reached by other competition authorities.
B. CCS will take into account the decisions of the US and EU authorities and will generally clear the merger without conducting any further assessment.
C. CCS will defer to the decisions of the US and EU authorities but will commence its own review if either company maintains a physical office or data centre in Singapore.
D. CCS lacks jurisdiction to review the merger because neither company is incorporated in Singapore, notwithstanding their significant customer base in Singapore.

**Answer: A.** Section 54 asks whether a merger may be expected to substantially lessen competition in any market in Singapore. For foreign-to-foreign mergers with Singapore customers the CCS makes its own assessment of effects in Singapore. B and C wrongly defer to other authorities. D is wrong: jurisdiction turns on effects in Singapore, not incorporation.
*Cite: CL4 s14–17; Cyril-CL-T 00:21:43–00:24:15; SQ p115 (key A); `ccp-2-2-20`*

### 2.VI.2 — Remedies: directions, commitments; structural v behavioural

**Q23-42** · `2.VI.2` `2.VI.3` · 2023 CCP Paper 2 Q42 (no official answer) · `ccp-2-2-21` `ccp-2-2-22`

In CCCS/400/140/2020/004 (LSEG Refinitiv), the merger was approved conditional on commitments in relation to, inter alia, WM/R FX benchmarks:

A. For a period of 10 years from the CCCS' infringement decision to be monitored by a Monitoring Trustee.
B. For a period of 10 years from the CCCS' infringement decision to be monitored by the CCCS.
C. For a period of 8 years from the CCCS' infringement decision based on self-reporting by the merged entity.
D. For a period of 12 years from the CCCS' infringement decision to be monitored by the Monetary Authority of Singapore.

**Answer: A.** The CCS conditionally approved LSEG's acquisition of Refinitiv on 24 May 2021 on commitments about access to the WM/R FX benchmarks. The commitments run for ten years from the CCS's decision (to 23 May 2031), with a Monitoring Trustee who assesses complaints of breach (CCCS-Reg). This fits the general rule that accepted commitments are usually overseen by a monitoring trustee. Note that the decision was a conditional clearance, not an "infringement decision" as the options say. The case is not in the 2026 slides; the answer rests on the CCCS register.
*Cite: CCCS-Reg (LSEG/Refinitiv conditional approval media release, 24 May 2021); CL4 s5; Cyril-CL §4.5; `ccp-2-2-21`, `ccp-2-2-22`*

**Q2-16** · `2.VI.2` · own question · `ccp-2-2-21`

The CCS finds that a completed merger will substantially lessen competition. Which remedy does it generally prefer, and why?

A. Structural remedies (divestment), because they address market structure directly and need less monitoring. Behavioural remedies are used where divestment is impractical or disproportionate, and remedies start from restoring the pre-merger structure.
B. No remedy, because the regime is voluntary.
C. Financial penalties only.
D. Behavioural remedies, because they are easier to monitor.

**Answer: A.** The CCS may give directions (prohibition, modification, divestment) and accept commitments. On the Public Register, "Conditionally Cleared" means cleared subject to accepted commitments, and "Application Withdrawn" usually means the deal was abandoned after concerns were raised. D reverses the preference. C and B are wrong.
*Cite: CL4 s5; CL-LP p6; Cyril-CL §4.5; `ccp-2-2-21`*

### 2.VI.3 — Cases: Grab/Uber, Grab/Delivery Hero, Pathology/Innovative/Quest, iNova/Mundipharma, Times/Penguin

**Q23-41** · `2.VI.3` `2.VI.2` · 2023 CCP Paper 2 Q41 (no official answer) · `ccp-2-2-22` `ccp-2-2-21`

In CCCS 500/001/18 (Grab/Uber) which of the following was not a remedy imposed by the CCCS in its infringement decision?

A. Removing of any exclusivity obligations imposed on Grab drivers.
B. Maintaining Grab's pre-merger pricing algorithm and driver commission rates.
C. Requiring Uber to sell Lion City Rentals to any potential competitor who makes a reasonable offer on fair market value.
D. Requiring Uber to cease operations only 3 months after its infringement decision.

**Answer: D.** The CCS's directions of 24 September 2018 included removing exclusivity obligations, lock-in periods and termination fees for Grab drivers, including those renting from Lion City Rentals (A), and requiring Grab to maintain its pre-merger pricing algorithm and driver commissions until competition revived (B) (CCCS-Reg media release). The directions also dealt with Uber's Lion City Rentals fleet (C). D describes no direction: Uber's exit was part of the merger itself, which completed on 26 March 2018. The parties were also fined a combined S$13m for completing without notifying.
*Cite: CL4 s18; CCCS-Reg (Grab/Uber infringement decision media release, 24 Sep 2018); `ccp-2-2-22`, `ccp-2-2-21`*

**Q2-17** · `2.VI.3` · own question · `ccp-2-2-22`

Which pairing of merger case and outcome is CORRECT?

A. iNova/Mundipharma: fined for failing to notify.
B. Grab/Uber: cleared unconditionally after notification.
C. Pathology Asia/Innovative/Quest: prohibited outright.
D. Grab/Delivery Hero: the CCS issued interim directions (no integration; preserve foodpanda's viability and saleability; deal at arm's length) while it investigated the anticipated merger. Times Publishing/Penguin: conditionally approved on commitments not to discriminate against rival book retailers.

**Answer: D.** iNova/Mundipharma was notified and cleared (5 Dec 2023), so A is wrong. Pathology/Innovative/Quest was conditionally cleared on 4-year commitments with annual audits, so C is wrong. Grab/Uber completed without notification and was penalised, and the CAB dismissed Uber's appeal, so B is wrong.
*Cite: CL4 s18–21, s25; CCCS-Reg; `ccp-2-2-22`*

### 2.VII Enforcement

Sub-points 2.VII.1–2.VII.3. Real questions: Q23-44, QSQ-CL1, QSQ-CL10. Own questions: Q2-18, Q2-19.

### 2.VII.1 — Detection (complaints, horizon-scanning, leniency); investigation powers ss 63–65

**Q2-18** · `2.VII.1` · own question · `ccp-2-2-23`

CCS officers arrive unannounced at a company's office without a warrant. Which statement is CORRECT?

A. The CCS can never enter premises without a warrant.
B. The CCS may arrest the directors.
C. The CCS may require documents and information (s 63), enter premises without a warrant (s 64), and enter and search with a warrant (s 65), using reasonably necessary force, taking copies and requiring explanations of documents. Cases come from complaints, horizon-scanning and leniency applications.
D. Only the police may investigate competition infringements.

**Answer: C.** These are the CCS's investigation powers under ss 63–65. A, B and D are wrong.
*Cite: CL4 s24, s26–27; Cyril-CL §5.2; `ccp-2-2-23`*

### 2.VII.2 — Financial penalties (up to 10% of Singapore turnover, up to 3 years); directions; appeals; private actions

**Q23-44** · `2.VII.2` · 2023 CCP Paper 2 Q44 (no official answer) · `ccp-2-2-24`

What is the financial penalty that may arise as a consequence of an infringement of a prohibition under the Competition Act?

A. A maximum of 90% of the net supernormal profits earned by the infringing undertakings as a result of the prohibited conduct or mergers.
B. A maximum of 10% of the turnover of the infringing undertakings for 3 years after the date of the CCCS' infringement decision.
C. A maximum of 10% of the turnover of the infringing undertakings for each year of infringement up to a maximum of 3 years preceding the CCCS' infringement decision.
D. A maximum of 10% of the turnover of the infringing undertakings over the period of the infringing conduct.

**Answer: C.** For intentional or negligent infringement the CCS may impose a penalty of up to 10% of the undertaking's annual Singapore turnover for each year of infringement, up to a maximum of 3 years (s 69). C is the option that states this. A is not the measure. B looks forward from the decision. D has no 3-year limit.
*Cite: CL4 s28; Cyril-CL §2.5, §5; `ccp-2-2-24`*

**Q2-19** · `2.VII.2` · own question · `ccp-2-2-24`

A customer overcharged by a cartel wants compensation. Which statement is CORRECT?

A. It may sue at any time, even before the CCS investigates.
B. Private actions are not possible in Singapore.
C. A person who suffers loss or damage directly from an infringement may bring a civil action, but only after the infringement has been established and appeals are exhausted. Appeals against CCS decisions go to the Competition Appeal Board, then the General Division of the High Court and the Court of Appeal.
D. Appeals go straight to the Court of Appeal.

**Answer: C.** The right of private action follows an infringement decision and the exhaustion of appeals. The CCS can also direct that infringements end, and an infringing agreement is void. A, B and D are wrong.
*Cite: CL4 s28; Cyril-CL §2.5, §5; `ccp-2-2-24`*

### 2.VII.3 — Six-step penalty calculation; aggravating and mitigating factors; worked examples

**QSQ-CL1** · `2.VII.3` · SQ p33 Q1 [Part B 2024], official key D · `ccp-2-2-25`

The CCS has found Company A to have infringed the Section 34 prohibition of the Competition Act 2004. In determining the financial penalty to be imposed on Company A, which of the following financial statement items is MOST LIKELY to be directly used by the CCS as a starting point for its calculation?

A. The company's total assets as reported on the balance sheet.
B. The company's net profit as reported on the income statement.
C. The company's total shareholder equity as reported on the balance sheet.
D. The company's turnover in the relevant market as reported in the financial statements.

**Answer: D.** Step 1 of the six steps applies the seriousness percentage to the undertaking's Singapore turnover in the affected product and geographic markets in its last business year. Assets, profit and equity are not used.
*Cite: CL4 s30; SQ p115 (key D); `ccp-2-2-25`*

**QSQ-CL10** · `2.VII.3` · SQ p38 Q10 [Original], official key A · `ccp-2-2-25`

Company X has been found to have infringed section 34 of the Competition Act 2004 by engaging in price-fixing with its competitors in the specialty chemicals market. CCS determines the financial penalty by applying its six-step methodology. The relevant facts are as follows: Company X's relevant turnover in the affected market: S$50 million; duration of the infringement: 3 years and 3 months; starting percentage determined by CCS, having regard to the seriousness of the infringement: 15%; mitigating factor: Company X provided significant cooperation (10% reduction); statutory maximum financial penalty: 10% of global turnover; Company X's global turnover: S$300 million. Applying the CCS six-step methodology, what is the final financial penalty?

A. S$21,937,500.
B. S$22,275,000.
C. S$26,812,500.
D. S$80,000,000.

**Answer: A.** Base: S$50m × 15% = S$7.5m. Duration: × 3.25 years = S$24.375m. Mitigation: less 10% = S$21,937,500. That is below the stated cap (10% × S$300m = S$30m), so no reduction is needed at step 5. Note that the course states the cap as 10% of Singapore turnover for up to 3 years (s 69), not "global turnover". Here the answer is the same either way, and the course follows the exact duration (3.25), as the key does.
*Cite: CL4 s30–32; SQ p115 (key A); `ccp-2-2-25`*

**Q2-20** · `2.VII.3` · own question · `ccp-2-2-25`

Which is an AGGRAVATING factor in the CCS's penalty calculation?

A. Ending the infringement as soon as the CCS intervened.
B. Having an adequate compliance programme.
C. The undertaking was the leader or instigator of the cartel, with directors involved.
D. Genuine uncertainty whether the conduct was an infringement.

**Answer: C.** Aggravating factors: leader or instigator, involvement of directors or senior management, coercion of others, and intention rather than negligence. A, B and D are mitigating, as are severe duress and cooperation. Step 3 adjusts for these factors, after the base penalty and duration, and before deterrence, the statutory maximum and leniency.
*Cite: CL4 s30; Cyril-CL §5.1; `ccp-2-2-25`*

## 3 · Taxation

### 3.I Corporate income tax: charge, deductions, capital allowances

Sub-points 3.I.1–3.I.5. Real questions: QSQ-TX2, Q23-17, QSQ-TX1, Q23-20, QSQ-TX3, Q23-19, QSQ-TX4, Q23-21. Own question: Q3-1.

### 3.I.1 — Rate 17%; chargeable income; preceding year basis and year of assessment

**QSQ-TX2** · `3.I.1` · SQ p39 Q2 [Part B 2024], official key C · `ccp-2-3-1`

Company Beta has a financial year end of 30 June. The corporate income tax assessed on Company Beta for the Year of Assessment 2024 relates to income derived by Company Beta during which period?

A. 1 January 2023 to 31 December 2023.
B. 1 January 2024 to 31 December 2024.
C. 1 July 2022 to 30 June 2023.
D. 1 July 2023 to 30 June 2024.

**Answer: C.** Tax is assessed on a preceding year basis: a year of assessment taxes the income of the financial year ending in the preceding calendar year. YA 2024 therefore taxes the financial year ended 30 June 2023. A and B ignore Beta's year end. D is the basis period for YA 2025.
*Cite: TX1 s3; SQ p116 (key C); `ccp-2-3-1`*

**Q23-17** · `3.I.1` · 2023 CCP Paper 2 Q17 (no official answer) · `ccp-2-3-1`

Year of Assessment 2023 refers to tax year for income earned in which financial year?

A. 2020
B. 2023
C. 2019
D. 2022

**Answer: D.** On the preceding year basis, income of financial year 2022 is assessed in YA 2023. The rate is 17% of chargeable income for local and foreign companies alike.
*Cite: TX1 s3; `ccp-2-3-1`*

### 3.I.2 — Charging provision s 10(1): Singapore-sourced income; foreign income received or deemed received (s 10(25)); source test (HY)

**QSQ-TX1** · `3.I.2` `3.I.1` `3.I.3` · SQ p39 Q1 [Part B 2024], official key A · `ccp-2-3-2` `ccp-2-3-1` `ccp-2-3-3`

Which of the following statements is INCORRECT?

I. Only income derived by Singapore incorporated companies is taxable in Singapore.
II. Foreign-sourced income is chargeable to tax in Singapore upon receipt.
III. All gains derived from Singapore are subject to the prevailing corporate income tax rate of 17%.
IV. Royalty income, which is not derived from a trade, business, profession or vocation carried on in Singapore, is not taxable in Singapore.

A. I, III and IV.
B. II, III and IV.
C. I, II and IV.
D. I, II and III.

**Answer: A.** I is incorrect: s 10(1) ITA taxes the income of "any person" accruing in or derived from Singapore, foreign companies included. III is incorrect: only gains of an income nature are taxed; Singapore has no capital gains tax. IV is incorrect: royalties are separately charged under s 10(1)(f) and may be deemed Singapore-sourced (s 12(7)) without any trade. II is correct: foreign-sourced income is taxed when received or deemed received in Singapore (s 10(25)).
*Cite: ITA ss 10(1), 10(25), 12(7); TX1 s4–7; TX2 s22; SQ p116 (key A); `ccp-2-3-2`, `ccp-2-3-1`, `ccp-2-3-3`*

**Q23-20** · `3.I.2` · 2023 CCP Paper 2 Q20 (no official answer) · `ccp-2-3-2`

A company carrying on a trade in Singapore derived foreign-sourced interest income which was kept in its London bank account. The company intends to use the foreign-sourced interest income to settle its trade obligations owing to suppliers. Will this trigger taxation of the foreign-sourced interest income in Singapore?

A. Yes, as long as the foreign-sourced interest income is utilised by the company, it is taxable even if it is used to settle debt incurred in respect of a trade or business carried on outside Singapore.
B. No, because the foreign-sourced interest income is not remitted, transmitted or brought into Singapore.
C. Yes, because the foreign-sourced interest income is used to settle a debt incurred in respect of the company's trade carried on in Singapore.
D. No, because the foreign-sourced interest income is kept in a bank account that is not located in Singapore.

**Answer: C.** Foreign-sourced income is deemed received in Singapore if it is applied to satisfy a debt incurred in respect of a trade or business carried on in Singapore (s 10(25)(b) ITA), even though the money never comes to Singapore. A is wrong: applying it to a foreign trade's debts does not trigger tax. B and D overlook the deemed-receipt rule.
*Cite: ITA s 10(25); TX1 s4–7; `ccp-2-3-2`*

### 3.I.3 — Income v capital; no capital gains tax; badges of trade (NP)

**Q3-1** · `3.I.3` · own question · `ccp-2-3-3`

A manufacturing company sells a factory it has used for 20 years at a large gain. A property-trading company sells a block of flats it bought last year with a view to resale. Which statement is CORRECT?

A. Both gains are taxed at 17%, because Singapore taxes all gains.
B. Both gains are exempt because they relate to property.
C. The manufacturer's gain is likely capital and not taxed, as Singapore has no capital gains tax. The property trader's gain is likely income from trading and taxable. Whether a gain is income or capital is highly fact-specific, and for trading the courts apply the "badges of trade" (*NP v Comptroller*).
D. Only gains on shares can ever be taxable.

**Answer: C.** Singapore taxes gains of an income nature, not capital gains (subject to s 10L for foreign assets). Assets held on revenue account (trading stock of a dealer) produce taxable income. A and B are wrong. D is wrong: any trading gain can be taxable.
*Cite: TX1 s5; TX2 s4; `ccp-2-3-3`*

See also QSQ-TX1 under 3.I.2 (statement III).

### 3.I.4 — Deductions: s 14(1) general formula; specific deductions; s 15(1) prohibitions

**QSQ-TX3** · `3.I.4` `3.VI.1` · SQ p39 Q3 [Part B 2024], official key C · `ccp-2-3-4` `ccp-2-3-19`

Which of the following statements is INCORRECT?

I. An expense is tax deductible once it meets the general deduction rule under Section 14(1) of the Income Tax Act.
II. A tax deduction can be claimed on expenditure incurred to acquire a capital asset that is wholly and exclusively used in the production of income.
III. Interest expense incurred by a taxpayer on a loan that is used to acquire machinery for production of the taxpayer's goods for sale is tax deductible.
IV. Apart from interest expense, all other loan-related expenses or borrowing costs do not rank for tax deduction.

A. All of the above statements.
B. III and IV.
C. I, II and IV.
D. I, II and III.

**Answer: C.** I is incorrect: meeting s 14(1) is not enough if s 15(1) prohibits the deduction. II is incorrect: capital expenditure is not deductible (s 15(1)(c)); relief comes through capital allowances. IV is incorrect: prescribed non-interest borrowing costs are deductible (s 14(1)(a)(ii) with the Deductible Borrowing Costs Regulations). III is correct: s 14(1)(a) interest is deductible if payable on capital employed in acquiring the income, and the s 15(1)(c) capital bar does not apply to it.
*Cite: ITA ss 14(1), 15(1); TX1 s8–10; TX3 s14–16; SQ p116 (key C); `ccp-2-3-4`, `ccp-2-3-19`*

**Q23-19** · `3.I.4` `3.I.5` · 2023 CCP Paper 2 Q19 (no official answer) · `ccp-2-3-4` `ccp-2-3-5`

Which of the following statements is correct?

I. Bad debts incurred by a business from trade are deductible.
II. Capital expenses arising from acquisition of goodwill can be claimed as capital allowances.
III. Rental for premises occupied for purposes of acquiring income are deductible.
IV. Section 15(1) of the Income Tax Act disallows deduction of certain type of expenses under the general deductions provision in Section 14(1).

A. I and III only
B. I, III and IV only
C. All of the statements are accurate
D. II, III and IV only

**Answer: B.** Trade bad debts (s 14(1)(d)) and rent of premises used to earn income (s 14(1)(b)) are specific deductions (I, III). Section 15(1) disallows, among others, expenses not wholly and exclusively incurred and capital expenditure (IV). II is wrong: capital allowances are given for plant or machinery (ss 19, 19A) and, under s 19B, for listed IP rights. Goodwill is neither.
*Cite: ITA ss 14(1), 15(1), 19, 19A, 19B; TX1 s8–11; TX2 s20–21; `ccp-2-3-4`, `ccp-2-3-5`*

### 3.I.5 — Capital allowances: plant or machinery (ss 19, 19A); not buildings (ZF); deferral

**QSQ-TX4** · `3.I.5` · SQ p40 Q4 [Part B 2024], official key D · `ccp-2-3-5`

Which of the following statements is CORRECT?

I. A company can choose to defer its capital allowance claim.
II. Capital expenditure incurred to acquire any tangible assets for the purpose of the taxpayer's trade or business qualifies for capital allowance.
III. "Plant" and "building" are both tangible assets that taxpayers can claim capital allowance on.
IV. Taxpayers can choose to claim capital allowance under either Section 19 or 19A of the Income Tax Act.

A. All of the above statements.
B. I, II and III.
C. II, III and IV.
D. I and IV.

**Answer: D.** A company can choose to defer its capital allowance claim (I, per the key) and can elect between s 19 (over the asset's working life) and s 19A (accelerated, over three years) (IV). II is wrong: not every tangible asset qualifies; the main class is plant or machinery. III is wrong: buildings are not plant (*ZF v Comptroller* [2011] 1 SLR 1044).
*Cite: ITA ss 19, 19A; TX1 s11; SQ p116 (key D); `ccp-2-3-5`*

**Q23-21** · `3.I.5` · 2023 CCP Paper 2 Q21 (no official answer) · `ccp-2-3-5`

Which of the following statements on capital allowance is correct?

I. Capital allowance is available to capital expenditure incurred to acquire all tangible assets.
II. Capital allowance is not available to a company that does not carry on a trade or business.
III. A company can claim accelerated capital allowance under Section 19A of the Income Tax Act.
IV. A company cannot choose to defer its capital allowance claim.

A. All of the statements
B. II, III and IV only
C. II and IV only
D. II and III only

**Answer: D.** Capital allowances are for plant or machinery acquired for a trade, profession or business (II), and s 19A gives accelerated allowances over three years (III). I is wrong: buildings and other non-plant assets do not qualify. IV is wrong: a company can choose to defer its claim (SQ Taxation Q4, official key).
*Cite: ITA ss 19, 19A; TX1 s11; SQ p116 (Taxation Q4 key D); `ccp-2-3-5`*

See also Q23-19 under 3.I.4 (goodwill).

### 3.II Goods and services tax

Sub-points 3.II.1–3.II.3. Real questions: QSQ-TX5, Q23-18. Own questions: Q3-2, Q3-3.

### 3.II.1 — GST rate 9%; charging provision s 8(1) and its five elements; exempt v zero-rated

**Q3-2** · `3.II.1` · own question · `ccp-2-3-6`

A GST-registered Singapore company (1) sells machinery to a Singapore buyer, (2) exports goods to Australia, and (3) leases a residential flat it owns. Which statement is CORRECT?

A. GST at 9% is charged on all three.
B. GST is charged only if the buyer is GST-registered.
C. (2) and (3) are both exempt.
D. (1) is a standard-rated taxable supply at 9%. (2) is zero-rated: a taxable supply at 0%. (3) is an exempt supply, so no GST is charged.

**Answer: D.** GST is charged on a supply of goods or services made in Singapore, being a taxable (not exempt) supply, by a taxable person, in the course or furtherance of business (s 8(1) GSTA). Exports and international services are zero-rated (taxable at 0%). Financial services and the sale or lease of residential property are exempt. C confuses zero-rated with exempt. B is wrong: GST depends on the supplier being a taxable person.
*Cite: GSTA s 8(1), (2), (2A); TX1 s12–14; `ccp-2-3-6`*

### 3.II.2 — Compulsory and voluntary registration

**QSQ-TX5** · `3.II.2` `3.II.1` `3.II.3` · SQ p40 Q5 [Part B 2024], official key B · `ccp-2-3-7` `ccp-2-3-6` `ccp-2-3-8`

Which of the following statements on GST is INCORRECT?

I. A business is required to be GST-registered in Singapore if its total amount of taxable supplies of goods or services made in Singapore has exceeded S$1 million in a calendar year or its total amount of taxable supplies of goods or services made in Singapore is reasonably expected to exceed S$1 million in the next 12 months.
II. Voluntary GST registration would be for a period of at least three (3) years, unless the taxpayer applies to shorten the same (subject to the Comptroller's approval).
III. For GST to be chargeable, the supply must be a taxable and not an exempt supply.
IV. An overseas supplier must register for GST under the OVR regime if in a calendar year, its global turnover has exceeded S$ 1 million and the value of remote services and distantly taxable goods made to non-GST registered customers belonging in Singapore has exceeded S$ 100,000 (i.e., retrospective basis).

A. II and IV.
B. II only.
C. I, II and IV.
D. III only.

**Answer: B.** Voluntary registration lasts at least two years, not three (First Schedule para 8(2) GSTA). I states the retrospective and prospective S$1m tests (para 1(1)). III is one of the five conditions in s 8(1) (s 8(2A)). IV states the OVR retrospective test (para 1A).
*Cite: GSTA s 8, First Schedule paras 1, 1A, 8; TX1 s12–20; SQ p116 (key B); `ccp-2-3-7`, `ccp-2-3-6`, `ccp-2-3-8`*

**Q23-18** · `3.II.2` `3.II.3` · 2023 CCP Paper 2 Q18 (no official answer) · `ccp-2-3-7` `ccp-2-3-8`

Which of the following businesses would be required to undertake compulsory registration for GST?

I. A business whose total amount of taxable supplies of goods or services made in Singapore exceeds SGD 1 million in a calendar year.
II. A business whose global turnover has exceeded SGD 500,000 and the value of remote services and distantly taxable goods made to non-GST registered customers in Singapore has exceeded SGD 100,000.
III. A business whose total amount of taxable supplies of goods or services made in Singapore is reasonably expected to exceed SGD 1 million in the next 12 months.
IV. A business whose global turnover is reasonably expected to exceed SGD 1 million in the next 12 months.

A. I only
B. I, III and IV only
C. I and III only
D. II, III and IV only

**Answer: C.** Compulsory registration applies on the retrospective (I) and prospective (III) S$1m tests for taxable supplies made in Singapore. II misstates the OVR test, whose global turnover threshold is S$1 million, not S$500,000. IV is incomplete: OVR also needs supplies to non-registered Singapore customers of more than S$100,000.
*Cite: GSTA First Schedule paras 1(1), 1A; TX1 s15–20; `ccp-2-3-7`, `ccp-2-3-8`*

### 3.II.3 — Overseas Vendor Registration and Reverse Charge regimes

**Q3-3** · `3.II.3` · own question · `ccp-2-3-8`

A Singapore bank, GST-registered and making mainly exempt financial supplies (so not entitled to full input tax credit), buys consultancy services from a US firm with no Singapore presence. Who accounts for GST?

A. No one: services from overseas are outside GST.
B. The US firm must always register under OVR.
C. The bank, under the reverse charge: where an overseas supplier supplies imported services to a GST-registered recipient belonging in Singapore who is not entitled to full input tax credit, the recipient accounts for GST as if it were the supplier.
D. The US firm, because it is the supplier.

**Answer: C.** That is the reverse charge (s 14(1)–(2) GSTA). OVR (B) applies to supplies of remote services and distantly taxable goods to non-GST-registered customers, with the S$1m global and S$100,000 thresholds. A and D are wrong.
*Cite: GSTA s 14; TX1 s17–20; `ccp-2-3-8`*

See also QSQ-TX5 under 3.II.2 (OVR thresholds) and Q23-18.

### 3.III Share sale v asset sale

Sub-points 3.III.1–3.III.5. Real questions: Q23-26, Q23-24, QSQ-TX9, Q23-23. Own questions: Q3-4, Q3-5, Q3-6.

### 3.III.1 — Share sale: seller's income tax (capital v revenue; s 13W safe harbour); GST exempt

**Q3-4** · `3.III.1` · own question · `ccp-2-3-9`

Holdco Pte Ltd has owned 25% of the ordinary shares of Target Pte Ltd for three years and sells them at a gain. Section 10L does not apply. Which statement is CORRECT?

A. The gain is always taxable, because Holdco is a company.
B. GST at 9% is chargeable on the share sale.
C. Section 13W requires 100% ownership.
D. The gain is exempt under the s 13W safe harbour, because Holdco legally and beneficially owned at least 20% of Target's ordinary shares for a continuous period of at least 24 months immediately before the disposal (other conditions also apply). The share transfer is generally an exempt supply for GST.

**Answer: D.** Absent s 13W, the gain is taxed only if the shares were held on revenue account. The safe harbour gives certainty for disposals by companies of ordinary or preference shares held at the 20% / 24-month level. It no longer has a sunset date (Budget 2025), and it does not apply where s 10L applies. A share transfer is generally exempt for GST. C and B are wrong.
*Cite: TX2 s3–5; IRAS (s 13W e-Tax Guide, checked 11 Nov 2026); `ccp-2-3-9`*

### 3.III.2 — Carry-over of tax attributes: capital allowances (s 23), losses and donations (s 37)

**Q23-24** · `3.III.2` · 2023 CCP Paper 2 Q24 (no official answer) · `ccp-2-3-10`

Company T has unabsorbed trade losses brought forward from the Year of Assessment 2022. It has taxable income in the Year of Assessment 2023, and wishes to utilise its unabsorbed trade losses. What are the relevant comparison dates for the substantial shareholding test?

A. 1 January 2022 and 31 December 2023
B. 31 December 2021 and 1 January 2023
C. 31 December 2022 and 1 January 2023
D. 1 January 2021 and 31 December 2023

**Answer: B.** For losses, the shareholders must be substantially the same (at least 50%) on the last day of the year in which the loss was incurred and on the first day of the YA in which it is to be deducted (s 37(12), (14) ITA). A loss brought forward from YA 2022 was incurred in its basis year, calendar 2021, so the dates are 31 December 2021 and 1 January 2023. C would be the capital-allowance style comparison using the YA (s 23(4): the last day of the YA in which the allowance arose). That is exactly the difference the course flags.
*Cite: ITA ss 23(4), 37(12), (14); TX2 s5–8; Cyril-TX §2.2.3; `ccp-2-3-10`*

**Q3-5** · `3.III.2` · own question · `ccp-2-3-10`

A buyer acquires 100% of a loss-making target to use its unabsorbed losses against the buyer's group profits after the target changes business. Which statement is CORRECT?

A. The losses carry over automatically after a change of ownership.
B. A waiver lets the losses be used against any income.
C. The change of ownership breaks the substantial shareholding test. The Minister may waive the test if the change was not for a tax benefit, but the losses may then be used only against profits from the same trade or business. Capital allowances also need the same business test.
D. Tax attributes can never be carried forward.

**Answer: C.** The rules stop profitable companies buying loss-makers to cut tax: the shareholding test (ss 23(4), 37(12)) is backed by a waiver limited to the same trade or business (ss 23(5)–(6), 37(16)–(17)), and capital allowances also need the same business test (s 23(1)). A, B and D are wrong.
*Cite: ITA ss 23, 37; TX2 s5–8; `ccp-2-3-10`*

### 3.III.3 — Asset sale: no exit tax; GST and TOGC; trading stock (s 32); balancing charge and s 24 election

**QSQ-TX9** · `3.III.3` · SQ p42 Q9 [Original], official key B · `ccp-2-3-11`

Your client intends to acquire the entire operating business of a GST-registered company. Which of the following statements is MOST ACCURATE?

A. GST is always chargeable on the sale of a business.
B. The transfer may qualify as a transfer of a business as a going concern and be treated as an excluded transaction for GST purposes if the prescribed conditions are satisfied.
C. GST is never chargeable on the sale of business assets.
D. GST is payable only if the purchaser is not GST-registered.

**Answer: B.** GST is payable on a taxable person's sale of business assets unless the sale qualifies as a transfer of a business as a going concern (TOGC), which is an excluded transaction under the GST (Excluded Transactions) Order. A and C are absolutes. D is wrong: the TOGC rules, not the buyer's registration alone, decide.
*Cite: TX2 s16–19; SQ p116 (key B); `ccp-2-3-11`*

**Q3-6** · `3.III.3` · own question · `ccp-2-3-11`

A seller sells machinery with a tax written-down value of $100,000 for $250,000 (cost $300,000), together with trading stock, to an unrelated buyer who will carry on the trade in Singapore. Which statement is CORRECT?

A. No tax arises: there is an exit tax only on share sales.
B. The balancing charge is $200,000.
C. A balancing charge arises because the disposal value exceeds the tax written-down value, clawing back excess allowances ($150,000). The trading stock is valued at the consideration, since the buyer carries on a trade in Singapore and can deduct its cost (s 32). The s 24 election to use the TWDV is available only for certain related-party sales.
D. The trading stock must always be valued at open market value.

**Answer: C.** Disposal value of $250,000 less TWDV of $100,000 gives a $150,000 balancing charge (within the $200,000 of allowances claimed). Under s 32, trading stock is valued at the consideration if sold to a Singapore trader who can deduct it, and otherwise at open market value (D wrong). There is no exit tax as such on a business transfer (A misdescribes the position). B uses cost instead of disposal value.
*Cite: ITA ss 24, 32; TX2 s16–19; `ccp-2-3-11`*

### 3.III.4 — Stamp duty on share and property transfers; timing (s 46); ACD

**Q23-23** · `3.III.4` · 2023 CCP Paper 2 Q23 (no official answer) · `ccp-2-3-12`

Gamma Pte. Ltd. is a Singapore incorporated company. It issues 10,000 new shares to Alpha Pte. Ltd., another Singapore incorporated company, in consideration for $1,000,000. This means that Alpha Pte. Ltd. will now own 25% of Gamma Pte. Ltd.'s entire issued share capital and its net asset value at the time of issuance is SGD 10,000,000. How much stamp duty is chargeable on the shares issued by Gamma Pte. Ltd. to Alpha Pte. Ltd.?

A. SGD 20,000
B. No stamp duty is chargeable
C. SGD 2,000
D. SGD 5,000

**Answer: B.** Stamp duty is a tax on instruments, and for shares it is imposed on instruments transferring shares. An issue (allotment) of new shares by the company is not a transfer, so no duty is chargeable. On a transfer the duty would be 0.2% of the higher of the consideration and the market value (with NAV as a proxy). For a transfer of 25% of a company with NAV of $10m, that is 0.2% × $2.5m = $5,000 (D). A uses 2% of $1m. C uses 0.2% of the $1m consideration.
*Cite: TX2 s9–10; TX3 s11; `ccp-2-3-12`*

**Q23-26** · `3.III.4` `3.III.1` `3.III.5` · 2023 CCP Paper 2 Q26 (no official answer) · `ccp-2-3-12` `ccp-2-3-9` `ccp-2-3-13`

Company A is a company incorporated in the United States. Company B, a Singapore-incorporated company, is a wholly-owned subsidiary of Company A and holds the shares of other operating companies in countries such as Vietnam, India and Indonesia. Company A is contemplating a potential sale of Company B to a third party buyer. Which of the following statements is true?

I. Stamp duty is chargeable in Singapore on the transfer of the shares in the subsidiaries of Company B in countries such as Vietnam, India and Indonesia.
II. The transfer of the shares in Company B to the third party buyer will be subject to GST in Singapore.
III. Stamp duty is chargeable on the instrument effecting the transfer of shares in Company B as it is a Singapore company.
IV. The sale of Company B may potentially trigger adverse tax consequences in the jurisdictions of its subsidiaries.

A. III and IV only
B. All of the statements
C. I and II only
D. I and IV only

**Answer: A.** Singapore stamp duty applies to transfers of shares in a Singapore company (or a foreign company with a share or branch register in Singapore) (III). The foreign subsidiaries' shares are not transferred and are not chargeable property (I wrong). A share transfer is generally an exempt supply for GST (II wrong). Some countries (the course names China and Indonesia) may tax the sale of a Singapore holding company as an indirect transfer of the local subsidiary (IV).
*Cite: TX2 s3–5, s9–15; `ccp-2-3-12`, `ccp-2-3-9`, `ccp-2-3-13`*

### 3.III.5 — Tax due diligence, tax warranties, tax indemnity; indirect share transfers

**Q3-7** · `3.III.5` · own question · `ccp-2-3-13`

A buyer of shares worries about the target's unpaid tax for the years before completion. Which statement is CORRECT?

A. Tax warranties are enough, because they give pound-for-pound recovery without proof of loss.
B. Tax due diligence is unnecessary if there is an indemnity.
C. In a share sale tax liabilities stay with the seller automatically.
D. Tax warranties give damages subject to proof of loss, remoteness and mitigation, and they prompt disclosure. A tax indemnity (tax deed) makes the seller pay, pound for pound, the target's tax liabilities from pre-completion income and events. Its definition of "Tax Liability" (actual payments; loss of tax assets) is key, and the seller will negotiate limitations.

**Answer: D.** In a share sale tax issues follow the company, so the buyer relies on tax due diligence, warranties and an indemnity. A confuses warranties with indemnities. C is wrong: liabilities stay in the company. B is wrong: due diligence drives price, retention, escrow and the scope of protection.
*Cite: TX2 s11–15; Cyril-TX §2.3; `ccp-2-3-13`*

See also Q23-26 under 3.III.4 (indirect transfers).

### 3.IV Acquisition of IP and royalties

Sub-points 3.IV.1–3.IV.2. Real questions: Q23-30, QSQ-TX10, Q23-25.

### 3.IV.1 — Section 19B writing-down allowances for IP rights

**Q23-30** · `3.IV.1` `3.VI.1` `3.VI.2` · 2023 CCP Paper 2 Q30 (no official answer) · `ccp-2-3-14` `ccp-2-3-19` `ccp-2-3-20`

Company S carries on the business of designing and manufacturing highly complex precision equipment in Singapore. It acquired patented technology from an inventor in the United States. Company S funded the acquisition of the patent technology via an interest-bearing loan from its parent company in the United States. Which of the following statements is correct?

A. No tax deduction on interest expense incurred by Company S is available as the loan is not from another Singapore company.
B. Withholding tax at the applicable rate of 10% could apply to the interest payment made to the parent company.
C. Patented technology is a qualifying intellectual property right under Section 19B of the Income Tax Act.
D. None of the statements.

**Answer: C.** A patent is among the IP rights listed in s 19B(11) ITA, so a company carrying on a trade may claim writing-down allowances on the capital cost over 5, 10 or 15 years. A is wrong: interest is deductible under s 14(1)(a) if there is a direct link between the borrowing and the income (*Andermatt*; *JD*). The lender's location is irrelevant. B is wrong: withholding tax on interest paid to a non-resident is 15% (s 12(6)); 10% is the royalty rate.
*Cite: ITA ss 12(6), 14(1)(a), 19B; TX2 s20–21; TX3 s14–17; `ccp-2-3-14`, `ccp-2-3-19`, `ccp-2-3-20`*

**Q3-8** · `3.IV.1` · own question · `ccp-2-3-14`

A company buys a competitor's customer list and a registered trade mark for its business. Which statement is CORRECT?

A. Writing-down allowances under s 19B can be claimed on both.
B. Only the customer list qualifies.
C. Neither qualifies.
D. Section 19B allowances can be claimed on the trade mark (over 5, 10 or 15 years, straight-line, at the company's election), but not on the customer list, which is excluded by s 19B(11A).

**Answer: D.** IP rights under s 19B(11) include patents, copyright, trade marks, registered designs, geographical indications, layout-designs, trade secrets and plant variety protection. Customer information, customer lists and work-process information are excluded (s 19B(11A)). Allowances stop once the rights end or are sold, and a sale may trigger a balancing charge.
*Cite: ITA s 19B; TX2 s20–21; `ccp-2-3-14`*

### 3.IV.2 — Royalties: deemed source (s 12(7)) and 10% withholding tax (s 43(3A)); treaties

**QSQ-TX10** · `3.IV.2` · SQ p42 Q10 [Original], official key B · `ccp-2-3-15`

Which of the following statements concerning the tax treatment of royalties is MOST ACCURATE?

A. Royalty payments are never subject to withholding tax.
B. Royalty payments made to a non-resident may give rise to withholding tax obligations, depending on the applicable tax rules.
C. Royalty payments are treated in the same manner as dividend payments for tax purposes.
D. Royalty payments are always deductible for income tax purposes.

**Answer: B.** A royalty borne by a Singapore resident or permanent establishment, or deductible against Singapore income, is deemed Singapore-sourced (s 12(7) ITA). Paid to a non-resident, it is generally subject to 10% withholding tax on the gross payment (s 43(3A)), subject to treaty relief. A, C and D are absolutes or wrong.
*Cite: ITA ss 12(7), 43(3A); TX2 s22–23; SQ p116 (key B); `ccp-2-3-15`*

**Q23-25** · `3.IV.2` · 2023 CCP Paper 2 Q25 (no official answer) · `ccp-2-3-15`

Royalty payment made by a Singapore payor to a non-Singapore tax resident attracts withholding tax. Which of the following statement is incorrect?

A. Where the royalty is deemed to be Singapore-sourced income, the payment of such royalty to a non-Singapore tax resident is generally subject to withholding tax at 10% on the gross payment.
B. If withholding tax applies on the royalty payment, it is the obligation of the non-Singapore tax resident payee to report and pay the withholding tax to the Inland Revenue Authority of Singapore.
C. Late payment of the withholding tax to the Inland Revenue Authority of Singapore is subject to penalties.
D. It is possible that the Singapore payor bears the withholding tax on behalf of the non-resident recipient of the royalty, if this is provided in the contractual agreement between the two parties.

**Answer: B.** The obligation to withhold and pay the tax to IRAS falls on the payer, not the non-resident payee. A states the 10% gross rule (s 43(3A)). D is correct: the economic burden can be shifted by contract (e.g. a gross-up). C is not contradicted by the sources, and B is plainly wrong.
*Cite: ITA ss 12(7), 43(3A); TX2 s22–23; `ccp-2-3-15`*

### 3.V Corporate restructurings

Sub-points 3.V.1–3.V.3. Real questions: Q23-27, Q23-29, Q23-28. Own question: Q3-9.

### 3.V.1 — Liquidation and striking off: tax consequences

**Q23-27** · `3.V.1` · 2023 CCP Paper 2 Q27 (no official answer; the earlier candidate selected A, which is wrong) · `ccp-2-3-16`

Which of the following is not a common corporate restructuring option?

I. Share sale
II. Asset sale
III. Liquidation or striking-off
IV. Amalgamation

A. I and II only
B. III only
C. III and IV only
D. None of the options, as I, II, III and IV are all common corporate restructuring options

**Answer: D.** The course lists the restructuring options as share sale, asset sale, liquidation (including striking off) and amalgamation (TX3 s3).
*Cite: TX3 s2–3; `ccp-2-3-16`*

**Q3-9** · `3.V.1` · own question · `ccp-2-3-16`

A group plans to liquidate a dormant subsidiary that has unabsorbed losses, and to strike off another. Which statement is CORRECT?

A. The liquidating distribution is taxed as a dividend.
B. Based on persuasive UK cases, a liquidating distribution should be treated as a return of capital and not taxed. But the tax attributes are lost (no carry-over of losses or capital allowances to the group), a GST-registered entity must deregister, and before striking off the company must reduce its balance sheet to zero.
C. The losses pass to the parent automatically on liquidation.
D. A company can be struck off with assets still on its balance sheet.

**Answer: B.** There is no Singapore case or ITA provision on the point, so UK cases are persuasive. Liquidation loses the tax attributes (C wrong). Striking off needs a zero balance sheet, with all assets distributed or liabilities novated (D wrong).
*Cite: TX3 s3–5; `ccp-2-3-16`*

### 3.V.2 — Amalgamation: s 34C tax-neutral election; short-form amalgamation (s 215D CA); GST

**Q23-29** · `3.V.2` · 2023 CCP Paper 2 Q29 (no official answer) · `ccp-2-3-17`

Companies W and X completed a statutory short form amalgamation pursuant to Section 215D(1) of the Companies Act. Company W is the surviving company. Company X, the amalgamating company, has unabsorbed trade losses. Section 34C of the Income Tax Act provides for a tax neutral treatment of corporate amalgamation. Which of the following statements is correct?

A. As the amalgamation of Companies W and X is a qualifying amalgamation under Section 34C, Company W can make an irrevocable election for the Section 34C treatment to apply.
B. The unabsorbed trade losses of Company W can be carried forward and utilised by Company X under the Section 34C treatment.
C. All amalgamations can qualify for Section 34C election.
D. If the Section 34C treatment is elected, Company W will not inherit all outstanding tax liabilities of Company X.

**Answer: A.** A short-form amalgamation under s 215D CA is a qualifying amalgamation (s 34C(2) ITA), so the amalgamated company may elect tax-neutral treatment. B reverses the companies: X's losses may pass to W, the survivor, subject to the same-business and shareholding tests. C is wrong: only qualifying amalgamations. D is wrong: the amalgamated company inherits all outstanding tax liabilities.
*Cite: ITA s 34C; TX3 s6–8; `ccp-2-3-17`*

**Q3-10** · `3.V.2` · own question · `ccp-2-3-17`

Two GST-registered, wholly owned Singapore subsidiaries of a Japanese parent amalgamate under s 215D(2) CA and make a s 34C election. Which statement is CORRECT?

A. A horizontal short-form amalgamation is available only if the parent is Singapore-incorporated.
B. It is a horizontal short-form amalgamation (wholly owned Singapore subsidiaries of the same corporation, wherever incorporated). Under s 34C assets pass at net book value. For GST, the amalgamation is by administrative concession treated as a TOGC (an excluded transaction), unless the survivor will be in a GST group.
C. GST at 9% is always chargeable on the transfer of assets on amalgamation.
D. A s 34C election transfers the assets at market value.

**Answer: B.** Section 215D(2) covers subsidiaries of the same corporation wherever it is incorporated (A wrong). A s 34C election passes assets at net book value, with the survivor stepping into the shoes (D wrong). The GST TOGC concession applies where both companies are GST-registered and the election is made (C wrong).
*Cite: ITA s 34C; Companies Act s 215D; TX3 s6–8; `ccp-2-3-17`*

### 3.V.3 — Stamp duty on amalgamation (s 32C SDA); relief (s 15 SDA; Reconstruction and APE Rules); timing

**Q23-28** · `3.V.3` `3.III.4` · 2023 CCP Paper 2 Q28 (no official answer) · `ccp-2-3-18` `ccp-2-3-12`

Company A is a company incorporated in Singapore, which holds another Singapore company, Company C indirectly, through Company B, which is incorporated in Hong Kong. A corporate restructuring is contemplated such that Company C will become wholly and directly owned by Company A instead. Which of the following statements is true:

A. Company B may be liquidated to achieve this objective, but Singapore stamp duty will not apply on the transfer of the Company C shares to Company A even though Company C is a Singapore company.
B. Stamp duty can be paid upfront and a refund may be available if all the prescribed conditions for stamp duty relief can be met.
C. Company A does not need to consider any stamp duty implications arising from this proposed restructuring.
D. Company B may consider selling Company C shares to Company A but no stamp duty relief is available even if all prescribed conditions for stamp duty relief can be met.

**Answer: B.** Stamp duty may have to be paid upfront before the transfer of legal and beneficial interest in shares, even where relief will be applied for afterwards (Cyril-TX §3.2.3). Relief under the Reconstruction Rules or the APE Rules is available if the prescribed conditions are met, with the application made within 14 days (or 30 days if executed abroad). A and C are wrong: any restructuring involving a transfer of chargeable property, such as shares in Singapore company C, has stamp duty consequences (TX3 s11). D is wrong: relief is possible for share sales as well as amalgamations (TX3 s13).
*Cite: SDA s 15; TX3 s9–13; Cyril-TX §3.2.3; `ccp-2-3-18`, `ccp-2-3-12`*

**Q3-11** · `3.V.3` · own question · `ccp-2-3-18`

Two Singapore companies amalgamate. The amalgamating company owns Singapore land. What triggers stamp duty, and can relief be claimed?

A. Nothing: amalgamations are outside stamp duty.
B. Duty is chargeable only on the shares, never on land.
C. The notice of amalgamation (s 215F CA) is treated as the instrument effecting a deemed conveyance on sale of chargeable property (Singapore immovable property and Singapore-registered shares) to the amalgamated company (s 32C SDA). Relief from ad valorem duty is available under s 15 SDA (Reconstruction Rules or APE Rules) if the highly prescriptive conditions are met, applied for within 14 days of execution (30 if executed entirely abroad).
D. Relief is automatic for every amalgamation.

**Answer: C.** Section 32C SDA catches the vesting of chargeable property. Relief is most straightforward for a short-form amalgamation, but it is never automatic (D wrong). A and B are wrong.
*Cite: SDA ss 15, 32C; TX3 s9–13; `ccp-2-3-18`*

### 3.VI Borrowing costs and withholding tax on interest

Sub-points 3.VI.1–3.VI.2. Real question: QSQ-TX8 (QSQ-TX3 and Q23-30 also touch it). Own questions: Q3-12, Q3-13.

### 3.VI.1 — Interest deduction s 14(1)(a); direct link test (Andermatt; JD); interaction with s 15; other borrowing costs

**QSQ-TX8** · `3.VI.1` · SQ p42 Q8 [Original], official key B · `ccp-2-3-19`

Which of the following statements concerning the deductibility of borrowing costs is/are CORRECT?

I. Interest incurred on borrowings used to produce taxable income may be deductible, subject to the Income Tax Act and applicable regulations.
II. All borrowing costs are automatically deductible once they are incurred.
III. Certain non-interest borrowing costs may also qualify for tax deduction where the prescribed statutory requirements are satisfied.

A. I only.
B. I and III only.
C. II and III only.
D. All of the statements.

**Answer: B.** Interest, and prescribed sums payable in lieu of or to reduce interest (the Deductible Borrowing Costs Regulations 2008), are deductible where payable on capital employed in acquiring the income (s 14(1)(a) ITA) (I, III). II is wrong: deduction needs the direct link test (*Andermatt*; *JD*).
*Cite: ITA s 14(1)(a); TX3 s14–16; SQ p116 (key B); `ccp-2-3-19`*

**Q3-12** · `3.VI.1` · own question · `ccp-2-3-19`

A company borrowed to buy shares in a property-holding company. The property company was later liquidated, and the company took over the property and earned rent. It claims the interest against the rent. Which statement is CORRECT?

A. The interest is deductible because it relates to the company's overall income.
B. Interest is never deductible if the loan financed a capital asset.
C. Interest on any loan is always deductible.
D. The interest is not deductible against the rent. There must be a direct link between the money borrowed and the income produced, and here both the asset (shares, then property) and the income (dividends, then rent) changed (*Andermatt*). *JD Ltd* adds that the link is to "the income", a particular source, not "any income".

**Answer: D.** These are the facts of *Andermatt* [1995] 2 SLR(R) 866, and *JD Ltd* [2006] 1 SLR(R) 484 narrows the test further. B is wrong: s 15(1)(c) does not bar s 14(1)(a) interest on a loan for capital expenditure that meets the test.
*Cite: TX3 s14–16; `ccp-2-3-19`*

See also QSQ-TX3 under 3.I.4 (machinery loan interest) and Q23-30 under 3.IV.1.

### 3.VI.2 — Withholding tax on interest (s 12(6), 15%)

**Q3-13** · `3.VI.2` · own question · `ccp-2-3-20`

A Singapore company pays interest on a loan from a non-resident lender, and the interest is deemed sourced in Singapore. What withholding tax applies?

A. 10%, the same as royalties.
B. 17%, the corporate tax rate.
C. 15% under s 12(6), which an applicable double tax treaty may reduce if its conditions are met.
D. None: interest is never subject to withholding tax.

**Answer: C.** Interest deemed Singapore-sourced (s 12(6) ITA) and paid to a non-resident bears 15% withholding tax, subject to treaty relief. A is the royalty rate (s 43(3A)).
*Cite: ITA s 12(6); TX3 s17; `ccp-2-3-20`*

See also Q23-30 under 3.IV.1 (option B: 10% is wrong for interest).

### 3.VII Section 10L and Pillar Two

Sub-points 3.VII.1–3.VII.2. Real questions: QSQ-TX6, QSQ-TX7. Own question: Q3-14.

### 3.VII.1 — Section 10L: gains from sale of foreign assets by an entity of a relevant group; exceptions

**QSQ-TX6** · `3.VII.1` · SQ p41 Q6 [Original], official key B · `ccp-2-3-21`

Singapore HoldCo Pte Ltd is part of a multinational group. It disposes of shares in a foreign subsidiary and realises a gain. The gain is received in Singapore. The company argues that because the shares disposed of are foreign assets and the disposal took place outside Singapore, the gain cannot be subject to Singapore income tax. Which of the following statements is MOST ACCURATE regarding Section 10L of the Income Tax Act?

A. The gain cannot be taxed in Singapore because gains from the disposal of foreign assets are always foreign-sourced.
B. Section 10L may apply to treat the gain as taxable in Singapore if the statutory conditions are satisfied, notwithstanding that the assets disposed of are foreign assets.
C. Section 10L applies only where the asset disposed of is intellectual property.
D. Section 10L applies only where the disposal takes place in Singapore.

**Answer: B.** Section 10L treats gains from the sale, on or after 1 January 2024, of foreign assets by an entity of a relevant (multinational) group, received or deemed received in Singapore, as income under s 10(1)(g), where they would otherwise not be taxable (e.g. capital gains) or would be exempt. There are exceptions, e.g. for an excluded entity with adequate economic substance in Singapore. A and D contradict s 10L. C is wrong: it covers foreign movable or immovable property, with IP subject to tighter rules.
*Cite: ITA s 10L; TX4 s3–5; SQ p116 (key B); `ccp-2-3-21`*

### 3.VII.2 — Pillar Two: 15% minimum; EUR 750m; IIR (MTT) and QDMTT (DTT) in Singapore from 2025

**QSQ-TX7** · `3.VII.2` · SQ p41 Q7 [Original], official key C · `ccp-2-3-22`

Which of the following statements concerning the OECD Pillar Two Global Minimum Tax is MOST ACCURATE?

A. Pillar Two applies to every company incorporated in Singapore, regardless of size.
B. Pillar Two replaces Singapore corporate income tax.
C. Pillar Two seeks to ensure that large multinational enterprise groups are subject to a minimum effective level of taxation, thereby reducing incentives for profit shifting to low-tax jurisdictions.
D. Pillar Two applies only where a multinational group has subsidiaries located within ASEAN.

**Answer: C.** Pillar Two imposes a 15% global minimum effective tax rate on MNE groups with annual consolidated revenue of EUR 750 million or more in at least two of the four preceding years. A is wrong (size threshold). B is wrong: it operates through top-up taxes alongside corporate income tax. D is wrong: it is global.
*Cite: TX4 s6–8; SQ p116 (key C); `ccp-2-3-22`*

**Q3-14** · `3.VII.2` · own question · `ccp-2-3-22`

A Singapore subsidiary of an in-scope MNE group has Net GloBE Income of $3,000 and a jurisdictional effective tax rate of 5%. Which statement is CORRECT?

A. No top-up tax arises, because Singapore has not implemented Pillar Two.
B. Top-up tax is $3,000 × (15% − 5%) = $300. Singapore implemented a QDMTT (the domestic top-up tax, DTT) and the IIR (the multinational enterprise top-up tax, MTT) for financial years starting on or after 1 January 2025 under the Multinational Enterprise (Minimum Tax) Act 2024, so Singapore can collect this top-up tax itself rather than leave it to the parent's jurisdiction under its IIR.
C. Top-up tax is $3,000 × 15% = $450.
D. Singapore has implemented the UTPR.

**Answer: B.** Top-up tax = Net GloBE Income × (15% − ETR). A QDMTT lets a jurisdiction collect top-up tax on its own group entities up to 15%, and this is credited against IIR top-up tax. Singapore reserved its position on the UTPR (D wrong). C ignores the 5% already paid.
*Cite: TX4 s6–8; TX-LP p4; `ccp-2-3-22`*

---

# Part 2 — Drills

Timed sets built only from Part 1 questions; find each by its ID (Ctrl-F the ID). Sit the set closed-book first, then check against the answer key and the explanation in Part 1, and log every miss in `weak-spots.md` under its Key. **Time limits** follow the real pace: CCP Paper 2 is a two-hour MCQ paper, and the 2023 sitting had 60 questions ("24 of 60 questions" on the Examplify screens), so each Drill allows 2 minutes per question, rounded up to the next 5 minutes. Drills 1–9 run by Topic and together use every one of the 207 questions in Part 1 once. Drills 10–12 re-use them as mixed mocks. Drill 10 is the 40 Sample Questions with the official key. Drill 11 is the 54 held questions of the 2023 paper in their original order (Subject split: IP 16, Taxation 13, Competition 12, M&A 13), the closest thing to a full sitting. Drill 12 samples the own questions across all four Subjects.

| Drill | Covers | Questions | Time |
|---|---|---|---|
| 1 | Intellectual Property: trade marks (0.I–0.V) | 20 | 40 min |
| 2 | Intellectual Property: patents (0.VI–0.VIII) | 20 | 40 min |
| 3 | Intellectual Property: copyright, remedies, confidential information, IP in business (0.IX–0.XIII) | 29 | 60 min |
| 4 | Mergers & Acquisitions: private acquisitions, the SPA, due diligence (1.I–1.III) | 23 | 50 min |
| 5 | Mergers & Acquisitions: public take-overs and concert parties (1.IV–1.VII) | 19 | 40 min |
| 6 | Mergers & Acquisitions: joint ventures (1.VIII–1.X) | 17 | 35 min |
| 7 | Competition Law: overview, s 34, market definition, s 47 (2.I–2.IV) | 22 | 45 min |
| 8 | Competition Law: merger control and enforcement (2.V–2.VII) | 20 | 40 min |
| 9 | Taxation: all Topics (3.I–3.VII) | 37 | 75 min |
| 10 | Mixed mock: all 40 Sample Questions, official key | 40 | 80 min |
| 11 | Mixed mock: the 2023 CCP Paper 2 questions held, in paper order | 54 | 110 min |
| 12 | Mixed mock: every third own question, across all four Subjects | 38 | 80 min |

### Drill 1 — Intellectual Property: trade marks (0.I–0.V) · 20 questions · 40 minutes

**Questions:** QSQ-IP1, Q0-1, Q0-2, Q0-3, Q23-1, Q23-3, QSQ-IP6, Q0-4, Q0-5, Q0-6, Q23-2, Q23-4, Q0-7, Q0-8, QSQ-IP2, Q0-9, Q23-6, QSQ-IP7, Q23-5, Q0-10.

**Answer key:** QSQ-IP1 B · Q0-1 C · Q0-2 D · Q0-3 D · Q23-1 D · Q23-3 D · QSQ-IP6 D · Q0-4 A · Q0-5 C · Q0-6 C · Q23-2 C · Q23-4 B · Q0-7 A · Q0-8 D · QSQ-IP2 C · Q0-9 C · Q23-6 A · QSQ-IP7 D · Q23-5 C · Q0-10 A.

### Drill 2 — Intellectual Property: patents (0.VI–0.VIII) · 20 questions · 40 minutes

**Questions:** Q0-11, QSQ-IP3, Q0-12, Q23-7, Q0-13, Q0-14, Q0-15, Q0-16, Q0-17, Q0-18, Q0-19, Q0-20, Q0-21, Q0-22, Q0-23, Q0-24, Q0-25, Q0-26, Q0-27, Q23-8.

**Answer key:** Q0-11 C · QSQ-IP3 C · Q0-12 D · Q23-7 C · Q0-13 A · Q0-14 C · Q0-15 A · Q0-16 C · Q0-17 A · Q0-18 C · Q0-19 C · Q0-20 D · Q0-21 D · Q0-22 C · Q0-23 A · Q0-24 C · Q0-25 B · Q0-26 C · Q0-27 C · Q23-8 C.

### Drill 3 — Intellectual Property: copyright, remedies, confidential information, IP in business (0.IX–0.XIII) · 29 questions · 60 minutes

**Questions:** QSQ-IP4, Q0-28, Q0-29, QSQ-IP10, Q0-30, Q0-31, Q23-9, Q0-32, Q0-33, Q23-11, Q0-34, Q0-35, Q0-36, Q0-37, Q23-10, Q0-38, Q0-39, Q23-12, Q0-40, QSQ-IP8, Q23-13, Q0-41, QSQ-IP5, QSQ-IP9, Q23-14, Q23-15, Q0-42, Q23-16, Q0-43.

**Answer key:** QSQ-IP4 D · Q0-28 D · Q0-29 C · QSQ-IP10 C · Q0-30 C · Q0-31 C · Q23-9 D · Q0-32 D · Q0-33 D · Q23-11 A · Q0-34 C · Q0-35 C · Q0-36 C · Q0-37 D · Q23-10 D · Q0-38 C · Q0-39 A · Q23-12 D · Q0-40 D · QSQ-IP8 A · Q23-13 C · Q0-41 A · QSQ-IP5 D · QSQ-IP9 D · Q23-14 D · Q23-15 B · Q0-42 C · Q23-16 B · Q0-43 B.

### Drill 4 — Mergers & Acquisitions: private acquisitions, the SPA, due diligence (1.I–1.III) · 23 questions · 50 minutes

**Questions:** Q1-1, Q23-56, Q23-58, Q1-2, Q1-3, Q1-4, Q1-5, Q1-6, Q1-7, Q1-8, Q1-9, Q1-10, QSQ-MA7, Q1-11, Q23-57, Q1-12, Q1-13, QSQ-MA6, Q23-60, Q1-14, Q23-59, Q1-15, Q23-55.

**Answer key:** Q1-1 A · Q23-56 A · Q23-58 D · Q1-2 D · Q1-3 D · Q1-4 C · Q1-5 C · Q1-6 C · Q1-7 A · Q1-8 D · Q1-9 C · Q1-10 C · QSQ-MA7 A · Q1-11 D · Q23-57 D · Q1-12 A · Q1-13 C · QSQ-MA6 B · Q23-60 A · Q1-14 A · Q23-59 C · Q1-15 C · Q23-55 D.

### Drill 5 — Mergers & Acquisitions: public take-overs and concert parties (1.IV–1.VII) · 19 questions · 40 minutes

**Questions:** Q23-50, Q1-16, Q1-17, Q1-18, Q1-19, Q1-20, Q23-49, Q1-21, Q1-22, Q23-52, Q1-23, Q1-24, Q23-47, Q1-25, QSQ-MA4, Q1-26, Q23-51, Q1-27, QSQ-MA5.

**Answer key:** Q23-50 C · Q1-16 D · Q1-17 D · Q1-18 D · Q1-19 C · Q1-20 C · Q23-49 B · Q1-21 C · Q1-22 C · Q23-52 A · Q1-23 B · Q1-24 A · Q23-47 D · Q1-25 D · QSQ-MA4 C · Q1-26 C · Q23-51 D · Q1-27 B · QSQ-MA5 C.

### Drill 6 — Mergers & Acquisitions: joint ventures (1.VIII–1.X) · 17 questions · 35 minutes

**Questions:** Q1-28, QSQ-MA1, QSQ-MA8, Q23-45, QSQ-MA2, QSQ-MA9, Q23-46, Q1-29, Q1-30, QSQ-MA3, QSQ-MA10, Q1-31, Q1-32, Q1-33, Q1-34, Q1-35, Q1-36.

**Answer key:** Q1-28 D · QSQ-MA1 D · QSQ-MA8 D · Q23-45 D · QSQ-MA2 B · QSQ-MA9 B · Q23-46 D · Q1-29 D · Q1-30 D · QSQ-MA3 B · QSQ-MA10 B · Q1-31 C · Q1-32 A · Q1-33 C · Q1-34 D · Q1-35 A · Q1-36 C.

### Drill 7 — Competition Law: overview, s 34, market definition, s 47 (2.I–2.IV) · 22 questions · 45 minutes

**Questions:** Q23-43, Q23-36, Q2-1, Q2-2, Q23-31, Q2-3, Q2-4, Q23-32, Q2-5, Q2-6, Q2-7, QSQ-CL2, QSQ-CL4, QSQ-CL9, Q2-8, Q2-9, QSQ-CL5, QSQ-CL7, Q23-35, Q23-34, Q2-10, Q2-11.

**Answer key:** Q23-43 A · Q23-36 A · Q2-1 D · Q2-2 A · Q23-31 D · Q2-3 C · Q2-4 D · Q23-32 B · Q2-5 C · Q2-6 D · Q2-7 B · QSQ-CL2 A · QSQ-CL4 D · QSQ-CL9 A · Q2-8 A · Q2-9 B · QSQ-CL5 C · QSQ-CL7 C · Q23-35 D · Q23-34 B · Q2-10 D · Q2-11 D.

### Drill 8 — Competition Law: merger control and enforcement (2.V–2.VII) · 20 questions · 40 minutes

**Questions:** Q23-38, Q2-12, Q2-13, Q2-14, QSQ-CL6, Q23-39, Q23-40, Q2-15, QSQ-CL3, QSQ-CL8, Q23-42, Q2-16, Q23-41, Q2-17, Q2-18, Q23-44, Q2-19, QSQ-CL1, QSQ-CL10, Q2-20.

**Answer key:** Q23-38 A · Q2-12 A · Q2-13 D · Q2-14 A · QSQ-CL6 B · Q23-39 B · Q23-40 D · Q2-15 C · QSQ-CL3 B · QSQ-CL8 A · Q23-42 A · Q2-16 A · Q23-41 D · Q2-17 D · Q2-18 C · Q23-44 C · Q2-19 C · QSQ-CL1 D · QSQ-CL10 A · Q2-20 C.

### Drill 9 — Taxation: all Topics (3.I–3.VII) · 37 questions · 75 minutes

**Questions:** QSQ-TX2, Q23-17, QSQ-TX1, Q23-20, Q3-1, QSQ-TX3, Q23-19, QSQ-TX4, Q23-21, Q3-2, QSQ-TX5, Q23-18, Q3-3, Q3-4, Q23-24, Q3-5, QSQ-TX9, Q3-6, Q23-23, Q23-26, Q3-7, Q23-30, Q3-8, QSQ-TX10, Q23-25, Q23-27, Q3-9, Q23-29, Q3-10, Q23-28, Q3-11, QSQ-TX8, Q3-12, Q3-13, QSQ-TX6, QSQ-TX7, Q3-14.

**Answer key:** QSQ-TX2 C · Q23-17 D · QSQ-TX1 A · Q23-20 C · Q3-1 C · QSQ-TX3 C · Q23-19 B · QSQ-TX4 D · Q23-21 D · Q3-2 D · QSQ-TX5 B · Q23-18 C · Q3-3 C · Q3-4 D · Q23-24 B · Q3-5 C · QSQ-TX9 B · Q3-6 C · Q23-23 B · Q23-26 A · Q3-7 D · Q23-30 C · Q3-8 D · QSQ-TX10 B · Q23-25 B · Q23-27 D · Q3-9 B · Q23-29 A · Q3-10 B · Q23-28 B · Q3-11 C · QSQ-TX8 B · Q3-12 D · Q3-13 C · QSQ-TX6 B · QSQ-TX7 C · Q3-14 B.

### Drill 10 — Mixed mock: all 40 Sample Questions, official key · 40 questions · 80 minutes

**Questions:** QSQ-IP1, QSQ-IP6, QSQ-IP2, QSQ-IP7, QSQ-IP3, QSQ-IP4, QSQ-IP10, QSQ-IP8, QSQ-IP5, QSQ-IP9, QSQ-MA7, QSQ-MA6, QSQ-MA4, QSQ-MA5, QSQ-MA1, QSQ-MA8, QSQ-MA2, QSQ-MA9, QSQ-MA3, QSQ-MA10, QSQ-CL2, QSQ-CL4, QSQ-CL9, QSQ-CL5, QSQ-CL7, QSQ-CL6, QSQ-CL3, QSQ-CL8, QSQ-CL1, QSQ-CL10, QSQ-TX2, QSQ-TX1, QSQ-TX3, QSQ-TX4, QSQ-TX5, QSQ-TX9, QSQ-TX10, QSQ-TX8, QSQ-TX6, QSQ-TX7.

**Answer key:** QSQ-IP1 B · QSQ-IP6 D · QSQ-IP2 C · QSQ-IP7 D · QSQ-IP3 C · QSQ-IP4 D · QSQ-IP10 C · QSQ-IP8 A · QSQ-IP5 D · QSQ-IP9 D · QSQ-MA7 A · QSQ-MA6 B · QSQ-MA4 C · QSQ-MA5 C · QSQ-MA1 D · QSQ-MA8 D · QSQ-MA2 B · QSQ-MA9 B · QSQ-MA3 B · QSQ-MA10 B · QSQ-CL2 A · QSQ-CL4 D · QSQ-CL9 A · QSQ-CL5 C · QSQ-CL7 C · QSQ-CL6 B · QSQ-CL3 B · QSQ-CL8 A · QSQ-CL1 D · QSQ-CL10 A · QSQ-TX2 C · QSQ-TX1 A · QSQ-TX3 C · QSQ-TX4 D · QSQ-TX5 B · QSQ-TX9 B · QSQ-TX10 B · QSQ-TX8 B · QSQ-TX6 B · QSQ-TX7 C.

### Drill 11 — Mixed mock: the 2023 CCP Paper 2 questions held, in paper order · 54 questions · 110 minutes

**Questions:** Q23-1, Q23-2, Q23-3, Q23-4, Q23-5, Q23-6, Q23-7, Q23-8, Q23-9, Q23-10, Q23-11, Q23-12, Q23-13, Q23-14, Q23-15, Q23-16, Q23-17, Q23-18, Q23-19, Q23-20, Q23-21, Q23-23, Q23-24, Q23-25, Q23-26, Q23-27, Q23-28, Q23-29, Q23-30, Q23-31, Q23-32, Q23-34, Q23-35, Q23-36, Q23-38, Q23-39, Q23-40, Q23-41, Q23-42, Q23-43, Q23-44, Q23-45, Q23-46, Q23-47, Q23-49, Q23-50, Q23-51, Q23-52, Q23-55, Q23-56, Q23-57, Q23-58, Q23-59, Q23-60.

**Answer key:** Q23-1 D · Q23-2 C · Q23-3 D · Q23-4 B · Q23-5 C · Q23-6 A · Q23-7 C · Q23-8 C · Q23-9 D · Q23-10 D · Q23-11 A · Q23-12 D · Q23-13 C · Q23-14 D · Q23-15 B · Q23-16 B · Q23-17 D · Q23-18 C · Q23-19 B · Q23-20 C · Q23-21 D · Q23-23 B · Q23-24 B · Q23-25 B · Q23-26 A · Q23-27 D · Q23-28 B · Q23-29 A · Q23-30 C · Q23-31 D · Q23-32 B · Q23-34 B · Q23-35 D · Q23-36 A · Q23-38 A · Q23-39 B · Q23-40 D · Q23-41 D · Q23-42 A · Q23-43 A · Q23-44 C · Q23-45 D · Q23-46 D · Q23-47 D · Q23-49 B · Q23-50 C · Q23-51 D · Q23-52 A · Q23-55 D · Q23-56 A · Q23-57 D · Q23-58 D · Q23-59 C · Q23-60 A.

### Drill 12 — Mixed mock: every third own question, across all four Subjects · 38 questions · 80 minutes

**Questions:** Q0-1, Q0-4, Q0-7, Q0-10, Q0-13, Q0-16, Q0-19, Q0-22, Q0-25, Q0-28, Q0-31, Q0-34, Q0-37, Q0-40, Q0-43, Q1-3, Q1-6, Q1-9, Q1-12, Q1-15, Q1-18, Q1-21, Q1-24, Q1-27, Q1-30, Q1-33, Q1-36, Q2-3, Q2-6, Q2-9, Q2-12, Q2-15, Q2-18, Q3-1, Q3-4, Q3-7, Q3-10, Q3-13.

**Answer key:** Q0-1 C · Q0-4 A · Q0-7 A · Q0-10 A · Q0-13 A · Q0-16 C · Q0-19 C · Q0-22 C · Q0-25 B · Q0-28 D · Q0-31 C · Q0-34 C · Q0-37 D · Q0-40 D · Q0-43 B · Q1-3 D · Q1-6 C · Q1-9 C · Q1-12 A · Q1-15 C · Q1-18 D · Q1-21 C · Q1-24 A · Q1-27 B · Q1-30 D · Q1-33 C · Q1-36 C · Q2-3 C · Q2-6 D · Q2-9 B · Q2-12 A · Q2-15 C · Q2-18 C · Q3-1 C · Q3-4 D · Q3-7 D · Q3-10 B · Q3-13 C.

