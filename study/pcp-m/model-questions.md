# PCP-M — Model Questions and Answers

Paper `pcp-m`, PCP Paper 2 (MCQ), Tue 8 Dec 2026, 2:30–4:30pm, open book. Subjects: 0 Probate & Succession Planning · 1 Real Estate (Conveyancing) · 2 Muslim Family & Succession Law · 3 Employment Law · 4 PIPD. Written 15 Nov 2026 as Markdown only, on Bennett's instruction of 14 Nov; no PDF is built until Phase 2 (`python3 tools/build_pack.py pcp-m --questions`).

**How the file runs.** *Part 1* holds the questions by Subject → Topic → Sub-point, in `coverage.md` order. Each real question sits under the Sub-point it mainly tests; any other Sub-point it tests is named in its tag line and carries a "See" line. Where no real question reaches a Sub-point, an own question fills the gap. Every one of the 255 Sub-points has at least one question whose tag line names it. *Part 2* holds the Drills: timed sets built from Part 1 questions, by Topic or mixed, each with a time limit and an answer key.

**How to read a question.** The tag line gives the question ID · the Sub-point Keys it raises (`coverage.md`) · the source · the end-point block(s) in `cheatsheets.md` that hold the rule. The answer follows the options: why the right option is right, why each other option is wrong, then the cite. Cites use the source aliases in `coverage.md` → "Source key" and the statute sections. Cover the answer, answer it, then check; log every miss in `weak-spots.md` under its Key.

**Question IDs.** `QSQ-P<n>`, `QSQ-R<n>`, `QSQ-M<n>`, `QSQ-E<n>`, `QSQ-I<n>` = 2026 Sample Questions, Probate / Real Estate / Muslim / Employment / PIPD question n. `QPP1-<n>`, `QPP2-<n>` = Probate Practice Paper 1 / 2, question n (`QPP1-1d` = Q1(d)). `Q2021R-<part>` = 2021 REP paper, question part (e.g. `Q2021R-1-3-1` = Q1.3.1). `Q<subject>-<n>` (e.g. `Q0-12`) = own question n for that Subject; `Q1-25F<n>` / `Q1-23F<n>` = own question set on the real case facts of the 2025 / 2023 Real Estate paper.

**Sources.** Real questions come first (RULES source order):

- **SQ** — `Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf`, PCP Paper 2: Muslim p67–70, Probate p71–75, Real Estate p76–80, Employment p81–84, PIPD p85–88, ten MCQs each, with the **official key** at p128–129. Qs 1–5 of each are labelled "[Part B 2023-S]" or "[Part B 2024]", Qs 6–10 "[Part B 2024]" or "[Original]". Every SQ answer below matches the official key except SQ Probate Q10, where the key (D) conflicts with s 25(2)(a) MCA and the answer gives both; where the key sits uneasily with the text elsewhere (SQ Probate Q9 D), the answer says so.
- **PR-PP1, PR-PP2** — the two Probate practice papers in `Modules/Private Client Practice/4. Probate & Succession Planning/Practice Papers/`: PP1 Q1 (Kim Seng and Polly, written, parts a–e) and Qs 2–6 (MCQs); PP2 Q1 (Bruce and Wayne, written, parts a–d) and Qs 2–4 (MCQs). **No official answers**: every answer is this project's own, from `cheatsheets.md`. The written parts are answered as short model answers because they show the issues a Topic raises.
- **PYP 2021 REP** — `Seniors Notes/Nic_s Part B Package/3. PYP/2021 PYP/REP 2021 Paper.pdf` (Real Estate Practice, Mon 13 Dec 2021, written). Parts that can be answered without the annexures are given short model answers, on the law as it is now.
- **PYP 2023 and 2025 PCP Paper 2** — `…/3. PYP/2023 PYP/PCP Paper 2.pdf` (Real Estate case facts for Qs 26–44: Mr and Mrs Sham) and `…/2025 PYP/PCP Paper 2 2025 - Instructions & REC case facts.pdf` (Real Estate case facts for Qs 21–40: Mdm Lim and her sons). The MCQs themselves were on Examplify and are not held, so the questions set on these facts are own questions (`Q1-23F…`, `Q1-25F…`).

No other PCP Paper 2 questions are held (see `PYP index.md`). No Muslim, Employment or PIPD past paper is held at all; for those Subjects the SQ questions are the only real ones.

**The law.** Every answer follows `cheatsheets.md`, whose blocks were checked against the course materials and current statutes on 10 Nov 2026 (see `coverage.md`). Where a real question assumed older law, the answer gives the current law and says what changed.

Self-study only: never use this file with a live quiz, the Mock Exam or another assessment (Handbook §7.11).

**Left out.** Two real questions are not answered, because neither the course materials nor the pack settle them and Singapore Statutes Online could not be reached to check the statute: PR-PP2 Q3 (what an LPA donee may do: gifts to herself under an LPA authorising unlimited gifts, settling the donor's assets on trust; PR6 s31 gives the cash-gift restriction only in outline, "note s 14(3)") and 2021 REP Q2.3 (whether a flat under contract to be sold drops out of the ABSD count before completion; IRAS's count list does not say, and Cyril's contrary note is unconfirmed). 2021 REP Q1.1, Q1.2, Q1.3.2, Q1.4, Q2.1, Q2.4.1, Q2.4.3 and Q2.4.4 turn on the annexures (title search, tenancy, completion figures, developer documents) or the non-examinable developer sale, so they are not reproduced.

| Subject | Real questions | Own questions | Total |
|---|---|---|---|
| 0 Probate & Succession Planning | 25 (SQ 10; PR-PP1 9; PR-PP2 6, of which 8 are written parts) | 83 | 108 |
| 1 Real Estate (Conveyancing) | 14 (SQ 10; 2021 REP 4 written parts) | 48 (7 set on the 2023 and 2025 exam facts) | 62 |
| 2 Muslim Family & Succession Law | 10 (SQ) | 40 | 50 |
| 3 Employment Law | 10 (SQ) | 31 | 41 |
| 4 PIPD | 10 (SQ) | 27 | 37 |
| **Total** | **69** (57 MCQs, 12 written parts) | **229** | **298** |

Own questions Q0-78 to Q0-83, Q2-39, Q2-40, Q3-31, Q4-26 and Q4-27 were added on 18 Nov 2026 for the syllabus cases and the PD 2014 protocols filled in after the audit (`audits/pcp-m-audit.md`).

Part 2 has 15 Drills.

---

# Part 1 — Questions by Topic and Sub-point

## 0 · Probate & Succession Planning

### 0.I Succession planning tools and assets outside the will

Sub-points 0.I.1–0.I.7. No real question; own questions Q0-1 to Q0-7.

### 0.I.1 — Succession planning tools

**Q0-1** · `0.I.1` · own question · `pcp-m-0-1`

Which of the following is NOT one of the succession planning tools listed in the Probate syllabus?

A. Inter vivos gifts.
B. Lasting powers of attorney.
C. Trusts.
D. Statutory declarations of heirship.

**Answer: D.** The syllabus lists five tools: wills, inter vivos gifts, LPAs, trusts and the family office (the last non-core). A, B, C are on the list. D is not a succession planning tool at all.
*Cite: PR-SYL p1 item 1; `pcp-m-0-1`*

### 0.I.2 — What a will can and cannot dispose of

**Q0-2** · `0.I.2` · own question · `pcp-m-0-2`

Tan's will gives "all my property" to his daughter. Which of the following assets passes under the will?

A. His CPF savings, for which he made no nomination.
B. A condominium he held with his wife as joint tenants.
C. A life policy on which he made a trust nomination under s 132 Insurance Act.
D. Shares in his sole name in his CDP account.

**Answer: D.** A will disposes of all real and personal estate the testator is entitled to at death (WA s 3), and shares in his sole name are his estate. A: CPF monies pass only by CPF nomination; with none they go through the Public Trustee under the intestacy rules. B: joint tenancy property passes by survivorship to the wife. C: a s 132 trust policy is held for the nominees, outside the estate.
*Cite: WA s 3; PR-6a p9 para 3; PR1 s19–20; `pcp-m-0-2`*

### 0.I.3 — Joint tenancy: survivorship, severance

**Q0-3** · `0.I.3` · own question · `pcp-m-0-3`

Husband and wife own their condominium unit (registered land) as joint tenants. The husband's will gives "my half share in the condominium" to his son. The husband dies first. Which statement is CORRECT?

A. The son takes a half share as tenant in common with the wife.
B. The will severed the joint tenancy when it was executed.
C. The wife takes the whole property by survivorship; the gift to the son has no effect.
D. The half share falls into the husband's residuary estate.

**Answer: C.** Survivorship applies to joint tenancy property, so it passes to the surviving joint tenant and not under the will; a will cannot sever a joint tenancy. To sever, the husband had to serve an instrument of declaration (registered land, s 53(5) LTA) in his lifetime. A, B, D all assume the will can sever or reach the share.
*Cite: LTA s 53(5)–(6); CLPA s 66A(3); PR1 s20; `pcp-m-0-3`*

**Q0-78** · `0.I.3` · own question · `pcp-m-0-3`

Husband and wife bought a house in the wife's sole name. The husband paid about 85% of the price; there is no declaration of trust and no evidence of any agreement about shares. By the time of purchase the marriage had broken down, and the husband did not intend to benefit the wife. Applying *Chan Yuen Lan v See Fong Mun*, who owns the beneficial interest?

A. The wife alone, because legal title is conclusive.
B. The wife alone, because the presumption of advancement from husband to wife always applies.
C. The wife holds about 85% on resulting trust for the husband and keeps about 15%.
D. They hold beneficially as joint tenants in equal shares.

**Answer: C.** Unequal, provable contributions and no declaration of trust raise a presumed resulting trust in proportion to contributions (step (a)). There was no common intention to hold differently (step (b)) and no intention to give (step (d)). On the facts the presumption of advancement did not operate (step (e)), so the shares follow contributions; in the case itself the wife held 84.17% on trust for the husband. A: legal title is only the starting point where contributions cannot be proved. B: advancement is a rebuttable presumption and did not apply on these facts. D: equal beneficial joint tenancy arises only if advancement operates and the property is in joint names.
*Cite: Chan Yuen Lan v See Fong Mun [2014] 3 SLR 1048 at [160]–[162]; `pcp-m-0-3`*

**Q0-79** · `0.I.3` · own question · `pcp-m-0-3`

The eldest son is the sole registered owner of an HDB property that the family bought with their late mother's money. His five siblings, all eligible to hold an interest in HDB property, claim that he holds it on a common intention constructive trust for all six equally. He relies on s 51(10) of the Housing and Development Act ("no person shall become entitled to any protected property … under any resulting trust or constructive trust"). Which statement is CORRECT?

A. s 51(10) bars any trust over HDB property, so the claim fails.
B. s 51(10) bars only ineligible persons; eligible siblings may establish a constructive trust.
C. s 51(10) allows a trust only between persons who are already registered co-owners.
D. A constructive trust over HDB property needs HDB's prior written consent.

**Answer: B.** The Court of Appeal adopted the Eligibility Interpretation: s 51(10) only stops ineligible persons acquiring interests under resulting or constructive trusts. It rejected the view in C (the "Pre-Existing Interest Interpretation", which would confine trusts to registered co-owners). A overstates the bar. D is not a requirement the case states.
*Cite: Ong Chai Soon v Ong Chai Koon [2022] 2 SLR 457 at [2]–[3], [108], [125]; `pcp-m-0-3`*

### 0.I.4 — Joint bank accounts

**Q0-4** · `0.I.4` · own question · `pcp-m-0-4`

An elderly widow opened a joint bank account with her adult son. She contributed every dollar; there is no clear evidence she meant to give him the money. She dies. Which presumption most directly displaces the son's right of survivorship?

A. The presumption of advancement.
B. The presumption of resulting trust.
C. The presumption of due execution.
D. The presumption of survivorship in s 30 Civil Law Act.

**Answer: B.** Survivorship is the starting point, but unequal contributions with no clear evidence of a gift raise a resulting trust, so the son holds the balance for her estate (*Estate of Yang Chun*). A: advancement (parent–child) can rebut a resulting trust in the son's favour; it does not displace survivorship. C concerns wills. D concerns deaths in a common calamity.
*Cite: Estate of Yang Chun [2019] 5 SLR 593; Lim Chen Yeow Kelvin [2008] 4 SLR(R) 783 (PR-SYL p3 item 6(c)); `pcp-m-0-4`*

### 0.I.5 — CPF monies: nomination only

**Q0-5** · `0.I.5` · own question · `pcp-m-0-5`

Which statement about CPF monies on a member's death is CORRECT?

A. A will may override an earlier CPF nomination if it refers to the CPF account expressly.
B. A CPF nomination is revoked by the member's later marriage.
C. A CPF nomination is revoked by the member's divorce.
D. The member's LPA donee may make a CPF nomination once the member loses capacity.

**Answer: B.** A nomination is revoked by the member's marriage (CPF Act s 25(5)(a)). A: CPF monies can be dealt with only by nomination, never by will. C: divorce is not a statutory ground of revocation. D: neither an LPA donee nor a deputy can make or revoke a CPF nomination.
*Cite: CPF Act s 25(1), (5); PR1 s19; `pcp-m-0-5`*

### 0.I.6 — Insurance nominations and payment without grant

**Q0-6** · `0.I.6` · own question · `pcp-m-0-6`

Which statement about insurance nominations is CORRECT?

A. A s 133 Insurance Act nomination can be changed only with the nominee's consent.
B. Proceeds under a s 132 trust nomination form part of the deceased's estate.
C. An insurer may pay up to S$150,000 of policy moneys without a grant of representation.
D. A deputy may revoke the protected person's insurance nomination.

**Answer: C.** s 150(2) Insurance Act with reg 7 of the Insurance (General Provisions) Regulations lets an insurer pay up to S$150,000 without a grant. A: a s 133 nomination is revocable without the nominee's consent; it is the s 132 trust nomination that is irrevocable. B: s 132 proceeds are held for the nominees, outside the estate. D: neither a deputy nor a donee can make or revoke one.
*Cite: Insurance Act ss 132, 133, 150(2); Insurance (General Provisions) Regs reg 7(1); `pcp-m-0-6`*

### 0.I.7 — Landed property, HDB flats and mortgaged property

**Q0-7** · `0.I.7` · own question · `pcp-m-0-7`

Kim Seng's will gives his semi-detached house (mortgaged for S$350,000) to his daughter, an American citizen. The will contains only a general direction to pay "my just debts". Which statement is CORRECT?

A. The mortgage is paid out of the residuary estate because of the general direction to pay debts.
B. The daughter can be registered as owner of the house without any approval.
C. Unless approval is obtained from the Land Dealings Approval Unit, the executors must sell the house and give her the net proceeds, and the house bears its own mortgage.
D. The gift fails and the house falls into residue.

**Answer: C.** A foreign person cannot take restricted residential (landed) property without LDAU approval (s 25(5) RPA); otherwise the PRs sell to a citizen or approved purchaser and pay her the proceeds (s 3(3)–(4) RPA). The land is primarily liable for its own mortgage, and a general direction to pay debts does not shift it (s 26 CLA). A ignores s 26(3) CLA. B ignores the RPA. D: the gift does not fail; it is converted into proceeds.
*Cite: RPA ss 3(3)–(4), 25(5); CLA s 26(1)–(3); PR1 s23; PR-PP1 Q1; `pcp-m-0-7`*

### 0.II Wills: who can make one, formalities, witnesses, capacity

Sub-points 0.II.1–0.II.9. Real questions: SQ Probate Q5 and PP1 Q2 (both 0.II.7). Own questions Q0-8 to Q0-15 cover the rest.

### 0.II.1 — What a will is; ambulatory nature

**Q0-8** · `0.II.1` · own question · `pcp-m-0-8`

In 2015 Lim made a will giving "all my shares" to his nephew. At his death in 2026 he owns shares he bought in 2024. Which principle explains why the nephew takes the 2024 shares?

A. The will is construed as if executed immediately before Lim's death (s 19 WA).
B. A will can only operate on property owned at the date of execution.
C. The doctrine of ademption.
D. The doctrine of republication by codicil.

**Answer: A.** A will is ambulatory: it speaks and takes effect as if executed immediately before death, unless a contrary intention appears (WA s 19). B is the opposite of s 19. C: ademption defeats a specific gift whose subject matter has gone; it does not add property. D: there is no codicil.
*Cite: WA s 19; PR1 s2–3; PR-6a p5; `pcp-m-0-8`*

### 0.II.2 — Mutual wills, mirror wills, joint wills

**Q0-9** · `0.II.2` · own question · `pcp-m-0-9`

A husband and wife made wills in identical reciprocal terms, each leaving everything to the other and then to their children. There was no agreement not to revoke. After the husband's death the wife makes a new will leaving everything to a charity. Which is CORRECT?

A. The wife's new will is ineffective because the earlier wills were mutual wills.
B. The earlier wills were mirror wills, so the wife was free to revoke and her new will is effective.
C. The earlier wills were a joint will, which the wife cannot revoke after the first death.
D. Equity imposes a trust on the wife's property for the children.

**Answer: B.** Reciprocal terms alone make mirror wills, which each party can revoke freely. A and D describe mutual wills, which need a legally binding agreement not to revoke; only then does equity impose a trust on the survivor's property after the first death. C: a joint will is one document executed by two or more persons; these were separate wills.
*Cite: PR-6a p27–28 para 15.2; Cyril-PR §1.1; `pcp-m-0-9`*

**Q0-80** · `0.II.2` · own question · `pcp-m-0-9`

In 2001 a husband and wife made mutual wills before a solicitor, each stating it was irrevocable. A GP certified both of sound mind three days before execution, and their son (a beneficiary) was at the solicitor's office. The husband died in 2004. In 2017 the wife made a new will leaving everything to two daughters. The daughters say the mutual wills are invalid. Following *VTL v VTM*, which statement is CORRECT?

A. The mutual wills are invalid because the medical certificate was not dated the day of execution.
B. The mutual wills are invalid because a beneficiary was present at the solicitor's office.
C. The 2017 will prevails because a later will always revokes an earlier one.
D. The mutual wills were validly made and take precedence over the 2017 will.

**Answer: D.** The court accepted the solicitor's standard practice and found no suspicious circumstances; the mutual wills took precedence over the 2017 will, whose grant was revoked. A: no medical certificate is needed unless there are grounds to suspect unsoundness, and one dated three days before suffices. B: mere presence proves nothing. C ignores the binding agreement not to revoke once the first party has died.
*Cite: VTL v VTM [2021] SGHCF 30 at [12]–[16]; `pcp-m-0-9`*

### 0.II.3 — Who can make a will: age 21, s 27 exceptions, Muslims

**Q0-10** · `0.II.3` · own question · `pcp-m-0-10`

Which of the following persons can make a valid will in Singapore?

A. A 19-year-old university student, in a will duly signed and witnessed.
B. A 20-year-old soldier in actual military service.
C. A 20-year-old who has married.
D. A Muslim domiciled in Singapore, giving his whole estate to a friend.

**Answer: B.** A will made by a person under 21 is invalid (WA s 4), but a soldier in actual military service, or a mariner or seaman at sea, may make a will under 21 (s 27). A and C: under 21, and marriage is not an exception. D: a Muslim domiciled in Singapore can dispose of no more than one-third of his estate by will.
*Cite: WA ss 4, 27; PR1 s4; PR-6a p3–5; `pcp-m-0-10`*

### 0.II.4 — Testamentary capacity, knowledge and approval, undue influence

**Q0-11** · `0.II.4` · own question · `pcp-m-0-11`

A testator with early-stage dementia executes a rational-looking will in a solicitor's office. A disappointed son challenges it. Which statement is CORRECT?

A. A diagnosis of dementia is enough by itself to prove lack of testamentary capacity.
B. The son bears the legal burden of proving the testator lacked capacity.
C. Capacity is presumed if the will looks rational and was duly executed, but the propounder bears the burden of proving capacity and knowledge and approval.
D. Undue influence is made out wherever a beneficiary helped arrange the appointment.

**Answer: C.** The propounder must prove capacity and knowledge and approval on a balance of probabilities; a rational, duly executed will raises a presumption of capacity, and of knowledge and approval absent suspicious circumstances. A: dementia alone does not prove incapacity (*XBO v XBP*). B: the burden is on the propounder. D: undue influence needs coercion overpowering free will, a high bar (*ULV v ULW*).
*Cite: Chee Mu Lin Muriel [2010] 4 SLR 373; ULV v ULW [2019] 3 SLR 1270; XBO v XBP [2024] SGHCF 36; `pcp-m-0-11`*

**Q0-81** · `0.II.4` · own question · `pcp-m-0-11`

An 88-year-old woman scores 14/28 on a Mini-Mental State Examination and her doctor recommends a full assessment. Ten days later her son, without arranging the assessment, takes her to sign a will leaving him her whole estate. Two estate planners witness it after asking a few general questions. The terms look rational. Which statement is CORRECT?

A. The will is valid because it was duly executed and its terms are rational.
B. The will is valid because the estate planners were independent witnesses.
C. The will is likely invalid: capacity is doubtful and the circumstances are suspicious, and a rational-looking will does not cure a lack of capacity.
D. The MMSE score alone proves incapacity as a matter of law.

**Answer: C.** On similar facts the court held the will invalid: suspicious circumstances displaced the presumption, the more thorough medical evidence showed moderate dementia, and the rational terms may simply reflect the beneficiary's wishes. A and B: due execution and witnesses do not answer capacity once suspicion arises. D: no single test score is decisive; the court looks at all the evidence.
*Cite: WWI v WWJ [2024] SGFC 22, affirmed [2024] SGHCF 28 at [19]–[22]; `pcp-m-0-11`*

### 0.II.5 — Formal validity of wills made abroad (s 5 WA)

**Q0-12** · `0.II.5` · own question · `pcp-m-0-12`

A Singapore citizen domiciled in Singapore executes a will while on holiday in Japan, following Japanese formalities but not s 6 WA. Is the will formally valid in Singapore?

A. No. Only a will complying with s 6 WA is valid.
B. Yes. A will is properly executed if it conforms to the internal law of the place where it was executed.
C. Yes, but only as to his immovable property in Japan.
D. No, unless he was habitually resident in Japan.

**Answer: B.** s 5(2) WA: a will is properly executed if it conforms to the internal law of the place of execution, or of the testator's domicile, habitual residence or nationality at execution or death. The court may want an affidavit of foreign law. A ignores s 5. C: s 5(3)(b) is an extra ground for immovables, not a limit. D: habitual residence is only one alternative.
*Cite: WA s 5(2)–(3); PR1 s5; PR3 s9; `pcp-m-0-12`*

### 0.II.6 — Execution under s 6 WA

**Q0-13** · `0.II.6` · own question · `pcp-m-0-13`

Which of the following home-made wills is validly executed?

A. The testator signs at the top of the first page; two witnesses sign the envelope.
B. The testator signs at the end in front of witness 1; an hour later he acknowledges his signature to witness 2 alone, who signs.
C. The testator signs at the end; two witnesses present at the same time see him sign and then each sign in his presence, with no attestation clause.
D. The testator signs at the end, then adds a further gift below his signature, and the witnesses sign.

**Answer: C.** s 6(2) WA: signature at the foot or end, made or acknowledged before two witnesses present at the same time, who subscribe in his presence; no form of attestation is needed. A fails (*Re Beadle*). B: the witnesses were not present at the same time. D: the will may be valid, but the gift below the signature is inoperative (s 6(4)).
*Cite: WA s 6(1)–(4); Re Beadle [1974] 1 All ER 493 (PR-6a p3–4); `pcp-m-0-13`*

### 0.II.7 — Who can witness a will (ss 9–12 WA)

**QSQ-P5** · `0.II.7` · SQ Probate Q5 [Part B 2023-S], official key D · `pcp-m-0-14`

In 2019, Ron Wee executed a Will which was witnessed by Agnes Ching and Cherie Sim, with all three of them being present at the same time. In which of the following circumstances will Ron Wee's Will be invalid?

I. Cherie Sim's daughter is a beneficiary in Ron Wee's Will.
II. In 2023, Agnes Ching suffered a serious stroke and was thereafter declared to be mentally incompetent by the Family Courts of Singapore.
III. Ron Wee named Cherie Sim's husband as the executor in Ron Wee's will.

A. I only.
B. II only.
C. III only.
D. None of the options.

**Answer: D.** None makes the will invalid. I: s 10 WA voids a gift only to the witness or the witness's spouse, and even then the will stays valid; a witness's daughter is outside s 10. II: later incompetence of a witness does not invalidate the will (s 9). III: an executor, or an executor's spouse, may witness (s 12). Official key: D.
*Cite: WA ss 9, 10, 12; SQ p73 Q5, key p128; `pcp-m-0-14`*

**QPP1-2** · `0.II.7` · PR-PP1 Q2 (no official answer) · `pcp-m-0-14`

Mabel's will appoints her friends Anna and Belle as her executors. The will contains a gift to Belle of S$100,000 and leaves the rest of the estate to a charity. The two witnesses to the will are Mabel's friends Catherine and Anna. Which one or more of the following statements is correct?

a. The will is invalid as it was witnessed by an executor.
b. The will is valid but the gift to Belle cannot take effect.
c. The will is valid and the gift to Belle can take effect.
d. The will is valid but only Belle can be the executor.

**Answer: c only.** An executor may witness (s 12 WA), so Anna's attestation leaves the will valid and her appointment stands. Belle is a beneficiary but did not witness, so s 10 does not touch her gift. a: wrong, s 12. b: wrong, s 10 applies only to a witnessing beneficiary or spouse. d: wrong, Anna's appointment is not affected.
*Cite: WA ss 10, 12; PR-PP1 Q2; `pcp-m-0-14`*

### 0.II.8 — Solicitor's duties in will preparation; negligence

**Q0-14** · `0.II.8` · own question · `pcp-m-0-15`

A solicitor sends a will to the client's home for signing without supervising execution. Only one witness signs, so the will fails. The intended beneficiaries take nothing on intestacy. Which is CORRECT?

A. The solicitor owes no duty to the beneficiaries because they were not his clients.
B. The solicitor is liable in negligence to the disappointed beneficiaries.
C. The court will save the will by rectification under s 28 WA.
D. The will is valid because the testator intended it to be.

**Answer: B.** A solicitor whose will fails for defective execution is liable in negligence to the disappointed beneficiaries (*Cheo Yeoh & Associates LLC v AEL*); he should supervise execution or check the will afterwards, and taking wills away to execute is perilous. A is wrong for that reason. C: rectification cures clerical errors or failures to understand instructions, not defective execution. D: s 6 formalities are mandatory.
*Cite: Cheo Yeoh & Associates LLC v AEL [2015] 4 SLR 325; Low Ah Cheow; PR-6a p24, p32; `pcp-m-0-15`*

### 0.II.9 — Evidence of due execution: affidavits required by the Registrar

**Q0-15** · `0.II.9` · own question · `pcp-m-0-16`

In which situation will the Registrar require an affidavit of due execution from an attesting witness?

A. The will has a standard attestation clause and no alterations.
B. The will was signed on the testator's behalf by another person at his direction.
C. The will was prepared by a lawyer who is also the executor.
D. The testator died more than six months after executing the will.

**Answer: B.** Under P 6 r 7 FJ(PAOM)R 2024 an affidavit is needed where the will was signed by a blind or illiterate testator or by another at his direction. Rr 6, 8 and 9 add: no or insufficient attestation clause or doubt about execution; non-compliant alterations; an appearance of attempted revocation. A, C and D raise none of these.
*Cite: FJ(PAOM)R 2024 P 6 rr 6–10; PR5 s19; `pcp-m-0-16`*

### 0.III Construction of wills, failure of gifts, revocation and alteration

Sub-points 0.III.1–0.III.15. Real questions: PP1 Q3 (0.III.7), PP1 Q4 (0.III.8, 0.III.5), PP1 Q6 (under 0.VIII.6, also 0.III.15). Own questions Q0-16 to Q0-28 cover the rest.

### 0.III.1 — Principles of construction; precatory words

**Q0-16** · `0.III.1` · own question · `pcp-m-0-17`

A will says: "I give my house to my wife, and it is my wish and strong desire that she leave it to our son." Which is CORRECT?

A. The wife holds the house on trust for the son.
B. The wife takes the house absolutely; the words about the son are precatory and not binding.
C. The gift is void for uncertainty.
D. The son takes the house on the wife's death under the will.

**Answer: B.** Precatory words such as "my wish and strong desire" only express a hope; they are not binding and the court will not strain to make them imperative (*Lau Tyng Tyng*). The court seeks the testator's intention mainly from the words used. A and D treat a hope as a trust or gift over. C: the gift to the wife is certain.
*Cite: Lau Tyng Tyng; Foo Jee Seng [17] (PR-6a p8–9); `pcp-m-0-17`*

### 0.III.2 — Trust for sale v power of sale; executor's power of sale

**Q0-17** · `0.III.2` · own question · `pcp-m-0-18`

Clause 6 of Kim Seng's will declares that his trustees "shall have power to convert into ready money all such parts of my estate as shall not consist of ready money with absolute power to postpone sale". Which is CORRECT?

A. A power of sale is a duty to sell, and the land is treated as money from death.
B. A trust for sale converts land notionally into money from death even if the trustees may postpone sale; a power of sale changes the property's character only on actual sale.
C. An executor has no power to sell estate land unless the will gives one.
D. Once administration ends, the executor may always sell "as executor".

**Answer: B.** A trust for sale imposes a duty to sell and converts land notionally into personalty from death, even with power to postpone; a power of sale is a discretion and changes the character only on sale (*Foo Jee Seng* [22]–[23]). A confuses the two. C: an executor has a statutory power of sale for administration (s 35(1) CLPA). D: after administration he holds as trustee and needs an express trustee power, or sells as executor only where appropriate.
*Cite: Foo Jee Seng [22]–[23]; CLPA s 35(1); PR-6a p16–18; `pcp-m-0-18`*

### 0.III.3 — Types of gift

**Q0-18** · `0.III.3` · own question · `pcp-m-0-19`

"I give S$20,000 to my niece, to be paid out of my DBS savings account." What kind of gift is this?

A. Specific.
B. General.
C. Demonstrative.
D. Residuary.

**Answer: C.** A demonstrative gift is a general gift payable from a named fund. A: a specific gift is a particular identified item. B: a general gift is a value from anywhere in the estate. D: residue is what is not otherwise disposed of. Demonstrative gifts, like general gifts, do not adeem.
*Cite: PR1 s11–16; PR-6d p1–2; `pcp-m-0-19`*

### 0.III.4 — What passes: ss 18–25 WA

**Q0-19** · `0.III.4` · own question · `pcp-m-0-20`

Under the Wills Act, a devise of real estate made without words of limitation passes

A. a life interest only.
B. the fee simple or the whole interest the testator could dispose of.
C. nothing, unless the will uses the words "in fee simple".
D. only the interest the testator held when he executed the will.

**Answer: B.** s 22 WA: a devise without words of limitation passes the fee simple or the whole interest the testator could dispose of. A and C state the old common law rule that s 22 reversed. D ignores s 19 (the will speaks from death).
*Cite: WA ss 19, 22; `pcp-m-0-20`*

### 0.III.5 — Lapse: beneficiary predeceases; gift over

See also QPP1-4 under 0.III.8 (residue to a boyfriend who predeceased).

**Q0-20** · `0.III.5` · own question · `pcp-m-0-21`

A will leaves "my Rolex watch to my friend Ali" and "the residue to my sister". Ali dies before the testator. There is no gift over. What happens to the watch?

A. It passes to Ali's estate.
B. It falls into residue and goes to the sister.
C. It passes on intestacy.
D. It goes to Ali's children under s 26 WA.

**Answer: B.** A gift lapses if the beneficiary predeceases, unless there is a gift over or s 26 applies; a lapsed specific gift falls into residue. A: lapse means the gift does not reach Ali's estate. C: only a lapsed residuary gift passes on intestacy. D: s 26 applies only to the testator's own issue.
*Cite: PR1 s21; PR-6a p20–21; `pcp-m-0-21`*

### 0.III.6 — s 26 WA: gifts to children or issue; class gifts (Re Loke Soh Lui)

**Q0-21** · `0.III.6` · own question · `pcp-m-0-22`

Clause 5 of a will leaves residue "to my children Maureen, Mark, Peter, Paul and Mary in equal shares". Mark predeceased the testator, survived by his widow and his son Martin. Mark died intestate. Who takes Mark's one-fifth share?

A. Martin directly, under s 26 WA.
B. The other four children, because the share lapses.
C. Mark's estate, so it is distributed on Mark's intestacy (to his widow and Martin).
D. It passes on the testator's partial intestacy.

**Answer: C.** Mark is the testator's issue and left issue alive at the testator's death, so s 26 WA saves the gift as if Mark had died immediately after the testator; it goes into Mark's estate, not straight to the grandchild (*Re Loke Soh Lui*). A is the ISA r 3 rule, not s 26. B is the class-gift result, but these are named children, not "such of my children as are living at my death". D: the gift does not lapse.
*Cite: WA s 26; Re Loke Soh Lui [1997] 3 SLR(R) 956; PR-PP1 Q1(c); `pcp-m-0-22`*

### 0.III.7 — Commorientes: s 30 Civil Law Act

**QPP1-3** · `0.III.7` · PR-PP1 Q3 (no official answer) · `pcp-m-0-23`

Colin (28 years old) and David (26 years old) were killed in a car accident when their car hit a building and burst into flames. It was not possible to ascertain their respective times of death. In Colin's will, he gave S$200,000 to David and the rest to Colin's parents. Colin is not married and is survived by his parents. Which one or more of the following statements is correct?

a. The S$200,000 will be given to David's personal representatives.
b. The S$200,000 will be given to Colin's parents as residuary estate.
c. The gift to David fails because it cannot be proven that David survives Colin.
d. The gift to David fails, the S$200,000 will become Colin's residuary estate.

**Answer: a only.** Where the order of deaths is uncertain, the deaths are presumed to occur in order of seniority, so the younger (David) is deemed to survive the elder (Colin) (CLA s 30). The gift does not lapse and passes to David's personal representatives. b, c and d all assume the gift fails.
*Cite: CLA s 30; PR1 s32; PR-6a p12 fn 1; `pcp-m-0-23`*

### 0.III.8 — Ademption

**QPP1-4** · `0.III.8` `0.III.5` · PR-PP1 Q4 (no official answer) · `pcp-m-0-24` `pcp-m-0-21`

Lucy's only living relative is her sister Lorraine. Lucy's will states as follows:

- Her Audi car to be given to her sister Lorraine;
- Her diamond necklace be given to her secretary Sophia;
- The residue be given to her boyfriend Benjamin.

Lucy lived a long life and at the time of her death, her Audi car has been replaced a few times and lastly by a BMW. She has given her diamond necklace to a nurse who took care of her when she had COVID19. Her boyfriend Benjamin died before her. Which one or more of the following statements is wrong?

a. The gifts of the Audi car and the diamond necklace fail as a result of ademption and Lorraine and Sophia will not receive their respective stated gifts.
b. The gift to Benjamin fails as a result of the doctrine of lapse.
c. All of Lucy's estate does not pass under her Will, but under the laws of intestacy to Lorraine.
d. All of Lucy's estate will be regarded as residuary and received by the estate of Benjamin.

**Answer: d only is wrong.** a is right: both specific gifts adeem, the Audi because the subject no longer matches the description, the necklace because it was given away. b is right: the residuary gift to Benjamin lapses, with no gift over and s 26 not applying. c is right: the adeemed gifts would fall into residue, the residue has lapsed, so the whole estate passes on intestacy to the sole relative, Lorraine (ISA). d is wrong: a lapsed gift never reaches the dead beneficiary's estate.
*Cite: Low Gim Har [57]–[59]; ISA s 7; PR1 s20–21; PR-PP1 Q4; `pcp-m-0-24`, `pcp-m-0-21`*

### 0.III.9 — Abatement

**Q0-22** · `0.III.9` · own question · `pcp-m-0-25`

After debts, an estate is worth S$100,000. The will gives a specific gift of a painting (worth S$30,000), pecuniary legacies of S$60,000 and S$40,000, and residue to a cousin. There is no named fund and the will says nothing on the order. Which is CORRECT?

A. The painting is sold first to pay the legacies.
B. The cousin gets nothing; the legacies abate rateably to fit the S$70,000 left after the painting, and the painting passes intact.
C. The legacies are paid in full and the painting abates.
D. All gifts abate equally by 30%.

**Answer: B.** Under the PAA Second Schedule, assets are applied in order: undisposed property, residue, then (after property appropriated for or charged with debts) the fund for pecuniary legacies, and only then specifically given property. So residue is used up first, then the pecuniary legacies abate proportionately (pari passu: S$42,000 and S$28,000), and the specific gift is used last. A and C reverse the order. D ignores the order.
*Cite: PAA Second Schedule (s 57(4)); PR-6a p22 para 8.4; `pcp-m-0-25`*

### 0.III.10 — Disclaimer and other reasons a gift fails

**Q0-23** · `0.III.10` · own question · `pcp-m-0-26`

A beneficiary disclaims a specific legacy of S$50,000. The will contains no gift over. What happens to the S$50,000?

A. The executor must pay it to the beneficiary anyway.
B. It passes to the beneficiary's children.
C. It falls into residue.
D. It passes on intestacy.

**Answer: C.** A beneficiary cannot be forced to take a gift. A disclaimed gift goes to any gift over; failing that it follows the lapse rules, so a specific gift falls into residue. A: a gift cannot be forced. B: no gift over names the children. D applies to disclaimed residue.
*Cite: PR-6a p21–22 paras 8.1, 8.4; `pcp-m-0-26`*

### 0.III.11 — Revocation: marriage, later will, destruction; revival

**Q0-24** · `0.III.11` · own question · `pcp-m-0-27`

Which of the following events revokes a will made in Singapore?

A. The testator's divorce.
B. The birth of the testator's child.
C. The testator's marriage, where the will says nothing about contemplating that marriage.
D. The testator writing "cancelled" across the will without signature or witnesses.

**Answer: C.** Marriage revokes a will (s 13(1) WA) unless the will is expressed to be made in contemplation of that marriage (s 13(2)). A and B: no revocation by presumption from changed circumstances (s 14). D: revocation is only by marriage, a later duly executed will or codicil, a duly executed writing declaring intention to revoke, or destruction with intent (s 15); unexecuted words are none of these.
*Cite: WA ss 13–15, 17; PR1 s8; PR-6a p7–8; `pcp-m-0-27`*

### 0.III.12 — Alterations after execution (s 16 WA)

**Q0-25** · `0.III.12` · own question · `pcp-m-0-28`

After executing her will, Ms Ng crosses out "S$10,000" in a legacy and writes "S$20,000" above it, but does not sign or have it witnessed. "S$10,000" is still legible. What is the effect?

A. The legacy is S$20,000.
B. The legacy is S$10,000.
C. The legacy fails entirely.
D. The whole will is revoked.

**Answer: B.** An alteration after execution has no effect unless executed like a will (s 16 WA), so the original legible words stand. If the original were no longer apparent, those words would be lost. A needs due execution of the alteration (testator signs and witnesses subscribe near it, s 16(2)). C and D: an unexecuted alteration neither destroys the gift nor revokes the will. The Registrar will want an affidavit for a non-compliant alteration (P 6 r 8).
*Cite: WA s 16; FJ(PAOM)R 2024 P 6 r 8; PR-6a p6–7; `pcp-m-0-28`*

### 0.III.13 — Codicils

**Q0-26** · `0.III.13` · own question · `pcp-m-0-29`

Which statement about a codicil is CORRECT?

A. A codicil need not be witnessed if it only changes one gift.
B. A codicil must be executed with the same formalities as a will, and confirming the will republishes it as at the codicil's date.
C. A codicil revokes the whole of the earlier will.
D. A codicil can be made only by the solicitor who drew the will.

**Answer: B.** A codicil is itself a will and must be executed with the same formalities; confirming the will as varied republishes it as at the codicil's date. A: no exception for small changes. C: it alters or supplements; it does not revoke the whole. D: no such rule.
*Cite: PR-6a p25 para 13; PR-6d p1; WA s 2; `pcp-m-0-29`*

### 0.III.14 — Rectification of a will (s 28 WA)

**Q0-27** · `0.III.14` · own question · `pcp-m-0-30`

The draftsman typed "my son Peter" instead of "my son Paul", contrary to the testator's clear instructions. Within what time must an application to rectify be made, without the court's permission?

A. 3 months after the testator's death.
B. 6 months after the grant is first made.
C. 6 months after the testator's death.
D. 12 months after the grant is first made.

**Answer: B.** The court may rectify a will for a clerical error or a failure to understand instructions (s 28(1) WA); the application must be made within 6 months after the grant is first made, unless the court permits otherwise (s 28(2)). PRs who distribute after 6 months are protected (s 28(3)). A, C and D give the wrong period or start.
*Cite: WA s 28(1)–(3); PR-SYL p5 item 10(b); `pcp-m-0-30`*

### 0.III.15 — Civil Law Act provisions on wills (ss 23–27, 30)

See also QPP1-6 under 0.VIII.6 (s 25 CLA chain of executorship).

**Q0-28** · `0.III.15` · own question · `pcp-m-0-31`

A will appoints Ali as executor and gives specific legacies, but has no residuary clause. Ali is not a beneficiary. Who is entitled to the undisposed residue?

A. Ali, as executor, beneficially.
B. Ali, as trustee for the persons entitled on intestacy.
C. The State, as bona vacantia.
D. The specific legatees rateably.

**Answer: B.** s 24 CLA: an executor is trustee of undisposed residue for those entitled on intestacy, unless the will shows he was meant to take it beneficially. A is the old rule s 24 displaced. C: bona vacantia (s 27 CLA) arises only if no one takes on intestacy. D: no rule gives residue to specific legatees.
*Cite: CLA s 24; PR2 s28–29; `pcp-m-0-31`*

### 0.IV Taking instructions, will clauses, executors and ethics

Sub-points 0.IV.1–0.IV.6. Real question: SQ Probate Q3 (0.IV.3). Own questions Q0-29 to Q0-33 cover the rest.

### 0.IV.1 — Taking instructions to prepare a will

**Q0-29** · `0.IV.1` · own question · `pcp-m-0-32`

An elderly client arrives with her nephew, the main intended beneficiary, who does most of the talking. What should the solicitor do?

A. Take instructions from the nephew, who knows the family assets best.
B. See the client alone, confirm her instructions and capacity, and keep an attendance note.
C. Refuse to act because a beneficiary introduced the client.
D. Ask the nephew to sign the attendance note as a witness.

**Answer: B.** Instructions come from the testator, alone if a beneficiary brought her; check capacity and freedom from pressure and keep a contemporaneous attendance note. A risks undue influence and a challenge. C: no rule bars acting. D: a beneficiary should not be a witness to the process (and if he witnessed the will, s 10 WA would void his gift).
*Cite: PR-SYL p4 item 8; PR1 s26–29; PR-6c p1–3; `pcp-m-0-32`*

### 0.IV.2 — Structure and clauses of a will

**Q0-30** · `0.IV.2` · own question · `pcp-m-0-33`

Which clause in a will states "In witness whereof I have set my hand this [date]"?

A. The commencement.
B. The revocation clause.
C. The testimonium.
D. The attestation clause.

**Answer: C.** The testimonium comes after the gifts and powers and records the testator setting his hand. A: the commencement identifies the testator. B: the revocation clause revokes former wills. D: the attestation clause records signing in the presence of two witnesses present at the same time (with variants for a blind testator or one who cannot read English).
*Cite: PR-6a p10–25; Cyril-PR §1.7.2; `pcp-m-0-33`*

### 0.IV.3 — Who cannot or should not be appointed executor

**QSQ-P3** · `0.IV.3` `0.VIII.3` · SQ Probate Q3 [Part B 2023-S], official key A · `pcp-m-0-34` `pcp-m-0-57`

Veronica Teo, by her last will and testament appointed her brother Vernon Teo to be the executor of her estate. In her Will, Veronica Teo gave her house to her husband William Soh and her residuary estate to her only child Violet Soh (now 28 years old). Veronica Teo passed away in December 2022. Around January 2019, Vernon Teo was found to have no mental capacity and the conduct of his personal welfare and property and affairs are managed by his sister Viola Teo. Viola Teo is the appointed donee in Vernon Teo's lasting power of attorney. Who are the persons who can apply for a grant of representation for Veronica Teo's estate?

A. Viola Teo as Vernon Teo's donee.
B. Violet Soh as the residuary legatee.
C. William Soh as the husband and the person having prior rights under the Intestate Succession Act.
D. William Soh and Violet Soh as the beneficiaries under Veronica Teo's Will.

**Answer: A.** Where the named executor lacks capacity to manage his property and affairs, administration with the will annexed may be granted to the person lawfully entrusted with the care of his estate, for his use and benefit (s 22 PAA, as amended wef 15 Oct 2024): here his donee, Viola. B and D: the residuary legatee or beneficiaries come in only if the executor's claim is cleared off. C: ISA priority applies on intestacy, and there is a will. Official key: A.
*Cite: PAA s 22; SQ p72 Q3, key p128; `pcp-m-0-34`*

**Q0-31** · `0.IV.3` · own question · `pcp-m-0-34`

Which person may NOT act as executor without the court's permission?

A. A 23-year-old named executor.
B. A named executor who is an undischarged bankrupt.
C. A named executor who is a beneficiary.
D. A named executor who witnessed the will.

**Answer: B.** An undischarged bankrupt is disqualified from being appointed or acting as a personal representative without the court's permission (s 400(1) IRDA); acting while disqualified is an offence (s 400(3)). A: only a minor (under 21) cannot take the grant (s 21 PAA). C: beneficiaries often act. D: an executor may witness (s 12 WA).
*Cite: IRDA s 400; PAA s 21; WA s 12; `pcp-m-0-34`*

### 0.IV.4 — Testamentary guardians

**Q0-32** · `0.IV.4` · own question · `pcp-m-0-35`

A father's will appoints his sister as guardian of his children aged 10 and 14. He dies; the mother survives. Which is CORRECT?

A. The sister becomes sole guardian and the mother loses guardianship.
B. The sister acts jointly with the mother; if the mother objects, the sister may apply to court.
C. The appointment is void because the mother is alive.
D. The appointment takes effect only when the children turn 18.

**Answer: B.** s 7 GIA lets a parent appoint a guardian for children under 21 by will; the guardian acts jointly with the surviving parent unless the parent objects, in which case the guardian may apply and the court may refuse, order joint guardianship or make the guardian sole guardian (s 7(4)). A overstates it. C and D are wrong.
*Cite: Guardianship of Infants Act s 7; PR3 s8; `pcp-m-0-35`*

### 0.IV.5 — Conflicts of interest and ethics in will work

**Q0-33** · `0.IV.5` · own question · `pcp-m-0-36`

A client tells his lawyer he wants to leave one-third of his estate to the lawyer's husband. What must the lawyer do?

A. Draft the will as instructed, since the gift is to her husband, not to her.
B. Not act on that gift and advise the client to get independent advice.
C. Draft the will but not act as executor.
D. Draft the will if a second partner witnesses it.

**Answer: B.** If a client intends a significant gift to the lawyer, the practice, its people or their immediate family, the lawyer must not act on it and must advise independent advice (r 25 PCR; *Law Society v Lee Suet Fern* [2020] SGDT 1, on exactly these facts). A, C and D let her act on the gift.
*Cite: PCR 2015 r 25; Law Society v Lee Suet Fern [2020] SGDT 1; `pcp-m-0-36`*

### 0.IV.6 — After execution: safekeeping and the Wills Registry

**Q0-34** · `0.IV.6` · own question · `pcp-m-0-37`

Which statement about the SAL Wills Registry is CORRECT?

A. It stores the original signed will.
B. It records that a will exists, who prepared it and where the original is kept.
C. A will must be registered there to be valid.
D. A digital copy deposited through the Wills Repository Service replaces the need for the original.

**Answer: B.** The Registry records the existence of a will, who prepared it and where the original is kept; it does not store the will. A: it does not. C: registration is not a formality of validity. D: the original signed will is still needed.
*Cite: PR-SYL p4–5 item 10(a); PR1 s30; SAL notices; `pcp-m-0-37`*

### 0.V Intestate Succession Act

Sub-points 0.V.1–0.V.9. Real questions: SQ Probate Q2 (0.V.9, 0.V.4) and PP1 Q1(b) (0.V.2). Own questions Q0-35 to Q0-41 cover the rest.

### 0.V.1 — Scope of the ISA

**Q0-35** · `0.V.1` · own question · `pcp-m-0-38`

A man domiciled in Malaysia dies intestate owning a condominium in Singapore and money in a Singapore bank account. Which is CORRECT?

A. Both assets are distributed under the ISA.
B. The condominium is distributed under the ISA; the bank money under the law of Malaysia.
C. Both assets are distributed under the law of Malaysia.
D. The ISA would apply to both if he were a Muslim.

**Answer: B.** Movables go by the law of the domicile at death (ISA s 4(1)); immovables in Singapore go by the ISA whatever the domicile (s 4(2)). A and C ignore the split. D: the ISA does not apply to a Muslim's estate at all (s 2); faraid applies.
*Cite: ISA ss 2, 4, 5; PR2 s3–5; `pcp-m-0-38`*

### 0.V.2 — Distribution on intestacy: s 7 rules 1–9

**Q0-36** · `0.V.2` · own question · `pcp-m-0-39`

A woman dies intestate, domiciled in Singapore, leaving her husband, her mother and her brother. She had no children. How is her estate distributed?

A. Husband 100%.
B. Husband 50%, mother 50%.
C. Husband 50%, mother 25%, brother 25%.
D. Husband 50%, brother 50%.

**Answer: B.** Spouse and parent(s), no issue: spouse 50%, parents 50% (ISA s 7 r 4). A applies only if there is no issue and no parent (r 1). C and D: siblings never share with parents; they take only under r 6, when there is no spouse, issue or parent.
*Cite: ISA s 7 rr 1, 4, 6; PR2 s7–14; `pcp-m-0-39`*

**QPP1-1b** · `0.V.2` `0.III.7` `0.V.4` · PR-PP1 Q1(b), written (no official answer); short model answer · `pcp-m-0-39` `pcp-m-0-23` `pcp-m-0-41` `pcp-m-0-22`

[Facts in brief.] Kim Seng (65) and his wife Polly (67), atheists domiciled in Singapore, died together in an avalanche; the order of death is unknown. They had three children together: Peter (24), Paul (23) and Mary (19). Kim Seng had two children by an earlier marriage: Maureen (28, US citizen) and Mark, who died in 2017 leaving a widow and a son. Polly had a son by an earlier marriage, Tony, who died in 2017 leaving a widow and two children; she also had a daughter, Sarah, whom she gave up for adoption. The bungalow, the Johor flat and an OCBC deposit were held jointly by the couple. Kim Seng's will gives S$20,000 to the Atheist Society, his King's Road house (mortgaged) to Maureen, and residue "to my wife the said Polly Chua and my children in equal shares as shall be living at my death". Advise how Kim Seng's estate and Polly's estate (assuming Polly died intestate) are to be administered and distributed.

**Answer (short model answer).** *Order of deaths:* the deaths are presumed to occur in order of seniority, so Kim Seng (younger) is deemed to survive Polly (CLA s 30). *Joint assets* (bungalow, Johor flat, OCBC deposit) pass by survivorship to Kim Seng and so into his estate. *Polly's estate* (intestate) goes under ISA s 7 r 2: the spouse (Kim Seng) takes 50%, which falls into Kim Seng's estate; her issue take 50% per stirpes (r 3) in four stocks of 12.5%: Peter, Paul, Mary, and Tony's two children (6.25% each). Tony's widow takes nothing (proviso to r 3). Sarah was adopted by others, so she is the child of her adopters and not Polly's "child" under the ISA (ACA s 47; ISA s 3). *Kim Seng's estate* passes under his will: S$20,000 to the Society (the receipt clause discharges the executors); King's Road to Maureen subject to its own mortgage (CLA s 26), and, as she is a foreign person and it is landed, sold and the proceeds paid to her unless LDAU approval is given (RPA s 3(4)). Residue is a class gift to those "living at my death": Polly is deemed to have died first and Mark died in 2017, so it goes in equal quarters to Maureen, Peter, Paul and Mary; s 26 WA does not save Mark's share because the gift is to a class. CPF passes only by nomination, not under either estate.
*Cite: CLA ss 26, 30; ISA ss 3, 7 rr 2–3; ACA s 47; WA s 26; RPA s 3(4); `pcp-m-0-23`, `pcp-m-0-39`, `pcp-m-0-41`, `pcp-m-0-22`, `pcp-m-0-7`*

### 0.V.3 — Per stirpes and the two provisos to rule 3

**Q0-37** · `0.V.3` · own question · `pcp-m-0-40`

An intestate widower had three children. Son A survives him. Son B predeceased him leaving a wife and two children. Daughter C predeceased him leaving no children but a husband. The estate is S$600,000. How much does each of B's children take?

A. S$100,000.
B. S$150,000.
C. S$200,000.
D. S$75,000.

**Answer: B.** C died without descendants, so her share goes to the other stocks: two stocks of S$300,000 (A, and B's stock). B's descendants stand in his place and share his S$300,000 equally: S$150,000 each (r 3 proviso 2). B's wife and C's husband take nothing (proviso 1: "legally represent" means descendants, not next of kin). A wrongly treats C's stock as surviving; C and D miscount the stocks.
*Cite: ISA s 7 r 3 and provisos; PR2 s8–10; `pcp-m-0-40`*

### 0.V.4 — Who counts as a "child": illegitimate, adopted, step and foster children

**Q0-38** · `0.V.4` · own question · `pcp-m-0-41`

Which of the following is a "child" entitled to share in the parent's estate under the ISA?

A. A step-son brought up by the deceased since infancy.
B. A foster daughter who lived with the deceased for 20 years.
C. A son adopted by the deceased under a Singapore adoption order.
D. An illegitimate son claiming his father's estate.

**Answer: C.** An adopted child is the child of the adopter (ISA s 3; ACA s 47). A: a step-child is not a child; a legal and biological link is needed (*Low Guang Hong David*). B: a foster child is not a child (*Lim Weipin*). D: an illegitimate child is not a child under the ISA (*AAG v Estate of AAH*); he takes only his mother's estate, and only if she leaves no legitimate children (Legitimacy Act s 10).
*Cite: ISA s 3; ACA s 47; Legitimacy Act s 10; AAG v Estate of AAH [2010] 1 SLR 769; `pcp-m-0-41`*

### 0.V.5 — Whole blood and half blood; child en ventre sa mere

**Q0-39** · `0.V.5` · own question · `pcp-m-0-42`

An intestate leaves no spouse, issue, parents, siblings or grandparents. Her only relatives are one aunt of the whole blood and two uncles of the half blood. Who takes the estate?

A. The three share equally.
B. The aunt takes everything.
C. The aunt takes half; the uncles share half.
D. The State, as bona vacantia.

**Answer: B.** Half-blood relatives rank immediately after whole-blood relatives of the same degree (ISA s 6(b)), so a whole-blood aunt excludes half-blood uncles entirely (*Chng Heng Tee v Estate & Trust Agencies*). A and C ignore s 6(b). D: r 8 (uncles and aunts) applies before r 9.
*Cite: ISA s 6; Chng Heng Tee [2010] 1 SLR 681; PR2 s15–20; `pcp-m-0-42`*

### 0.V.6 — No hotchpot for lifetime gifts (s 9)

**Q0-40** · `0.V.6` · own question · `pcp-m-0-43`

An intestate gave his elder son S$500,000 in his lifetime to buy a flat. He leaves a widow and two sons. The younger son says the S$500,000 must be brought into account. Which is CORRECT?

A. The gift is deducted from the elder son's share.
B. The gift is ignored in fixing the elder son's share (s 9 ISA).
C. The gift is deducted from the widow's share.
D. The gift is added back to the estate and divided under r 2.

**Answer: B.** Money paid for a child's advancement in the intestate's lifetime is not taken into account in fixing that child's or his descendants' share (s 9). A, C and D all apply a hotchpot rule the ISA excludes.
*Cite: ISA s 9; PR2 s26; `pcp-m-0-43`*

### 0.V.7 — Partial intestacy (s 10 ISA; s 24 CLA)

**Q0-41** · `0.V.7` · own question · `pcp-m-0-44`

A will appoints an executor and disposes of only half the estate; the residuary gift lapsed. The beneficiaries of the undisposed half include a minor. What grant should be sought?

A. Probate only; the executor holds the undisposed part on trust for those entitled under the ISA.
B. Probate for the will and separate letters of administration for the undisposed half.
C. Letters of administration with the will annexed, to two administrators.
D. Letters of administration only, since the will failed in part.

**Answer: A.** On a partial intestacy the ISA applies to the undisposed part, subject to the will (s 10), and the PR holds it on trust for those entitled (s 10 proviso; s 24 CLA). The executor simply applies for probate; no separate letters of administration are needed, even for infant beneficiaries. B and D add a grant that is not needed. C applies only where no executor can or will act.
*Cite: ISA s 10; CLA s 24; PR2 s27–30; `pcp-m-0-44`*

### 0.V.8 — Bona vacantia (rule 9; s 27 CLA)

**Q0-42** · `0.V.8` · own question · `pcp-m-0-45`

A bachelor dies intestate with no relatives within rules 1–8. His step-daughter cared for him for 15 years. What can she do?

A. Nothing; the Government takes the estate absolutely.
B. Claim as a "child" under rule 3.
C. Ask the Minister to release the Government's right to her, in whole or part, on an equitable or moral claim.
D. Apply under the IFPA as a dependant.

**Answer: C.** The Government takes as bona vacantia (r 9; s 27(1)–(2) CLA), but the Minister may disclaim and release its right to anyone with an equitable or moral claim, such as a step-child or carer (s 27(3) CLA). A ignores s 27(3). B: a step-child is not a child. D: a step-daughter is not a dependant under the IFPA.
*Cite: ISA s 7 r 9; CLA s 27; PR2 s31–32; `pcp-m-0-45`*

### 0.V.9 — Spouse during divorce; step-children (exam pattern)

**QSQ-P2** · `0.V.9` `0.V.4` · SQ Probate Q2 [Part B 2023-S], official key B · `pcp-m-0-46` `pcp-m-0-41`

Jasmine Tan passed away without having made any will. She has just been granted an interim judgment in her divorce proceedings with her husband Joel Tan. Jasmine and Joel have two children Jasper Tan and Jilian Tan from their marriage. During their marriage, Jasmine had also welcomed Joel's daughter from his previous marriage Jessie Tan into their family. Who are the beneficiaries to Jasmine Tan's estate?

A. Jasper Tan, Jilian Tan and Jessie Tan only.
B. Joel Tan, Jasper Tan and Jilian Tan only.
C. Joel Tan, Jasper Tan, Jilian Tan and Jessie Tan only.
D. Jasper Tan and Jilian Tan only.

**Answer: B.** An interim judgment is made final no earlier than 3 months later (WC s 99(1)); until then Joel is still her spouse and takes 50% under ISA s 7 r 2, the two children the other 50%. Jessie is a step-daughter, not a "child" (*Low Guang Hong David*). A and D wrongly drop Joel; A and C wrongly include Jessie. Official key: B.
*Cite: WC s 99(1); ISA s 7 r 2; SQ p71 Q2, key p128; `pcp-m-0-46`*

### 0.VI Dying testate v dying intestate

Sub-point 0.VI.1. Real question: SQ Probate Q4.

### 0.VI.1 — Advantages of dying testate over dying intestate

**QSQ-P4** · `0.VI.1` · SQ Probate Q4 [Part B 2023-S], official key D · `pcp-m-0-47`

Jeremy Lee, a newly called lawyer, was trying to explain to his client the benefits of having a Will. Which of the following of his statements is NOT CORRECT?

A. With a Will, the testator has testamentary freedom to decide how his assets may be distributed.
B. So long as the executors named in the Will apply for the grant of representation, sureties will not be required for the grant.
C. The process for the application for the grant of probate requires less information to be provided to the courts than for the application for the grant of letters of administration.
D. Where there is a Will, there is no requirement to explain the delay of more than 6 months to apply for the grant.

**Answer: D.** A delay of more than 6 months from death must be explained in both probate and administration applications (P 6 r 3(8) FJ(PAOM)R 2024), so D is the incorrect statement. A is correct (subject to the IFPA). B is correct: no administration bond or sureties for probate (s 29 PAA applies to administration). C is correct: administration needs religion, relationships, ages and shares. Official key: D.
*Cite: FJ(PAOM)R 2024 P 6 r 3(8); PAA s 29; SQ p72 Q4, key p128; `pcp-m-0-47`*

**Q0-43** · `0.VI.1` · own question · `pcp-m-0-47`

Which is an advantage of dying testate rather than intestate?

A. The estate vests in the Public Trustee until the grant.
B. An executor may start legal proceedings for the estate before the grant.
C. Step-children share in the estate automatically.
D. A deed of family arrangement redistributing a house attracts no stamp duty.

**Answer: B.** An executor's authority comes from the will, so he may start proceedings before probate (*Lee Han Tiong*); an administrator has none until the grant. A describes intestacy (vesting in the Public Trustee until the grant). C: step-children take only if the will provides for them. D: redistribution by deed of family arrangement on intestacy attracts ad valorem duty and ABSD; it is an assent of a devised house under a will that attracts none.
*Cite: Lee Han Tiong v Tay Yok Swee [1996] 2 SLR(R) 833; PR3 s3–18; `pcp-m-0-47`*

### 0.VII Inheritance (Family Provision) Act and maintenance of parents

Sub-points 0.VII.1–0.VII.7. No real question; own questions Q0-44 to Q0-50.

### 0.VII.1 — Scope of the IFPA

**Q0-44** · `0.VII.1` · own question · `pcp-m-0-48`

In which case can a dependant apply under the IFPA?

A. The deceased was a Muslim domiciled in Singapore.
B. The deceased was domiciled in Australia but owned a Singapore flat.
C. The deceased, domiciled in Singapore, died intestate and the ISA shares do not make reasonable provision for his disabled son.
D. The deceased, domiciled in Singapore, left a will that makes reasonable provision for every dependant.

**Answer: C.** The IFPA applies where the will, the intestacy rules or both fail to make reasonable provision for a dependant, and the deceased died domiciled in Singapore (s 3(1)). A: it does not apply to Muslim estates (s 1(2)). B: the deceased must be domiciled in Singapore. D: no claim where reasonable provision is made.
*Cite: IFPA ss 1(2), 3(1); PR4 s2–3; `pcp-m-0-48`*

### 0.VII.2 — Who is a dependant

**Q0-45** · `0.VII.2` · own question · `pcp-m-0-49`

Which of the following is a "dependant" under the IFPA?

A. A 25-year-old able-bodied son studying overseas.
B. A 61-year-old daughter who has never married.
C. A 40-year-old divorced daughter with no disability.
D. An illegitimate 10-year-old daughter.

**Answer: B.** A daughter who has not been married, of any age, is a dependant (s 3(1); *Jeanne Christine Monteiro*: aged 61). A: a son is a dependant only if an infant (under 21) or disabled (*AOS v Estate of AOT*). C: a once-married daughter is not, unless disabled. D: an illegitimate child is not a dependant (*AAG v Estate of AAH*).
*Cite: IFPA ss 2, 3(1); AAG [2010] 1 SLR 769; AOS [2012] 3 SLR 721; `pcp-m-0-49`*

### 0.VII.3 — What the court may order; the two-thirds exception; lump sum

**Q0-46** · `0.VII.3` · own question · `pcp-m-0-50`

When may the court order a lump sum under the IFPA?

A. Whenever the dependant asks for one.
B. Only if the net estate does not exceed S$50,000.
C. Only if the net estate exceeds S$5 million.
D. Only for a surviving spouse.

**Answer: B.** Provision is normally by periodical payments not exceeding the annual income of the net estate (s 3(2)–(3)); a lump sum is possible only where the net estate does not exceed $50,000 (s 3(4); *APZ v AQA*). A, C and D are wrong. Note also the two-thirds proviso: no claim where the spouse gets at least two-thirds of the income and the only other dependants are that spouse's children.
*Cite: IFPA s 3(1)–(4); APZ v AQA [2011] 3 SLR 1110; `pcp-m-0-50`*

### 0.VII.4 — Time limit for an IFPA application

**Q0-47** · `0.VII.4` · own question · `pcp-m-0-51`

When must an IFPA application be made?

A. Within 6 months of the death.
B. Within 6 months from the date representation is first taken out, unless the court extends time.
C. Within 12 months of the death.
D. Within 6 years of the death.

**Answer: B.** s 4(1): within 6 months from the date representation is first taken out, not from death. The court may extend time if the limit would operate unfairly, e.g. a will discovered later or an undetermined question of interest (s 4(2)). A, C and D use the wrong period or start.
*Cite: IFPA s 4; PR4 s7; `pcp-m-0-51`*

### 0.VII.5 — Matters the court considers; deceased's reasons; effect of an order

**Q0-48** · `0.VII.5` · own question · `pcp-m-0-52`

A client wants to leave nothing to his unmarried adult daughter, from whom he is estranged. What is the best advice to reduce the risk of a successful IFPA claim?

A. Insert a clause forbidding her from applying to court.
B. Record his reasons in a signed and dated written statement.
C. Give her S$1 so she is not "omitted".
D. Make the will in another country.

**Answer: B.** The court considers the deceased's reasons for his dispositions or omissions, including a signed and dated written statement, weighed for accuracy (s 3(7)), with the dependant's means and conduct (s 3(5)–(6)). A: the statute cannot be ousted. C: a token gift is not reasonable provision. D: the IFPA turns on domicile, not where the will was made. An order takes effect as if the will had been varied from death (s 5(1)).
*Cite: IFPA ss 3(5)–(7), 5; PR4 s9–11; `pcp-m-0-52`*

### 0.VII.6 — Court of Appeal IFPA cases: AAG and AOS

**Q0-49** · `0.VII.6` · own question · `pcp-m-0-53`

In *AOS v Estate of AOT* the husband died after decree nisi but before ancillary matters, leaving everything to a grandson. Which proposition did the Court of Appeal accept?

A. The widow was entitled to a share of the matrimonial assets as under the Women's Charter.
B. The IFPA provides maintenance, not a share of assets, and the widow, already reasonably provided for, got no order.
C. The adult sons studying abroad were dependants.
D. The mother could apply on behalf of the disabled adult son.

**Answer: B.** The IFPA gives maintenance, not a WC-style division; the widow had properties and income above her expenses, so no order. C: able-bodied adult sons, even studying, are not dependants. D: the disabled adult son had to apply himself. A is the argument the court rejected. (*AAG v Estate of AAH*: illegitimate children cannot claim.)
*Cite: AOS v Estate of AOT [2012] 3 SLR 721; AAG [2010] 1 SLR 769; PR4 s12–18; `pcp-m-0-53`*

### 0.VII.7 — Maintenance of Parents Act

**Q0-50** · `0.VII.7` · own question · `pcp-m-0-54`

A 62-year-old father, domiciled and resident in Singapore and unable to maintain himself, wants his three children to pay him a monthly allowance. Which is CORRECT?

A. He must apply under the IFPA.
B. He must first have his claim referred to the Commissioner before the Tribunal can hear it.
C. He can claim only against his eldest child.
D. If one child dies, the order against the other children ends.

**Answer: B.** A parent aged 60 or above who cannot maintain himself may apply to the Tribunal (MPA s 3(1)), but the claim must first be referred to the Commissioner (s 3(3)). A: the IFPA concerns estates. C: one or more children may be ordered to pay. D: one respondent's death does not end the others' liability (s 7(2)).
*Cite: MPA ss 3, 5, 7; PR-SYL p14; `pcp-m-0-54`*

### 0.VIII Grants of representation: probate, administration, resealing, contentious matters

Sub-points 0.VIII.1–0.VIII.17. Real questions: SQ Probate Q1 (0.VIII.10), Q3 (under 0.IV.3, also 0.VIII.3), Q6 (0.VIII.6), Q7 (0.VIII.7, 0.VIII.12, 0.VIII.10), Q8 (0.VIII.17); PP1 Q5 (0.VIII.10), PP1 Q6 (0.VIII.6), PP1 Q1(a), (d), (e). Own questions cover the rest.

### 0.VIII.1 — Probate terms

**Q0-51** · `0.VIII.1` · own question · `pcp-m-0-55`

Which statement about probate terms is CORRECT?

A. An administrator is appointed by the will.
B. "Personal representative" covers both an executor and an administrator.
C. A caveator is a person who applies for the grant.
D. Letters of administration are granted where there is a will and a willing executor.

**Answer: B.** A personal representative is an executor or an administrator. A: an executor is appointed by the will, an administrator by the court. C: a caveator files a caveat so no grant is made without notice to him. D: that is probate; administration is granted where there is no will or no executor able and willing.
*Cite: PR-6d (glossary); PR-SYL p6 item 1(a); `pcp-m-0-55`*

### 0.VIII.2 — First steps on a death; lost will; will proved abroad

**Q0-52** · `0.VIII.2` · own question · `pcp-m-0-56`

The family cannot find the original of a will the deceased signed, but the solicitor kept a signed copy. What may the court grant?

A. Nothing; a copy can never be proved.
B. Letters of administration on intestacy only.
C. Probate of the copy, on affidavit evidence of due execution, survival of the will after death and the copy's accuracy.
D. Probate of the copy without any evidence.

**Answer: C.** Where the original is lost, the court may grant probate of a copy or draft (s 9(a) PAA) or of its contents if proved (s 9(b)), on evidence of due execution, survival after death (to rebut the presumption of revocation) and accuracy. A and B ignore s 9. D: evidence is needed. A will proved and deposited in a foreign court may be proved by an authenticated copy (s 11 PAA).
*Cite: PAA ss 9, 11; PR-SYL p6 item 2; `pcp-m-0-56`*

### 0.VIII.3 — Types of grant and which one to apply for

See also QSQ-P3 under 0.IV.3 (named executor lacks capacity: grant to his donee).

**Q0-53** · `0.VIII.3` · own question · `pcp-m-0-57`

A testator's valid will names his brother as sole executor. The brother predeceased him, and there is no substitute. Which grant should be applied for?

A. Probate.
B. Letters of administration with the will annexed.
C. Letters of administration, with distribution under the ISA.
D. Resealing.

**Answer: B.** A valid will with no executor able and willing leads to letters of administration with the will annexed (ss 13, 14 PAA); the will still governs distribution. A needs an executor who can act. C applies where there is no valid will. D applies to Commonwealth or Hong Kong grants.
*Cite: PAA ss 8, 13, 18, 47; PR5 s3–7; `pcp-m-0-57`*

### 0.VIII.4 — Which court hears the application

**Q0-54** · `0.VIII.4` · own question · `pcp-m-0-58`

A deceased's estate, excluding assets held as trustee and before deducting debts, is worth about S$6 million. Where is the application for a grant filed?

A. The Family Courts.
B. The Family Division of the High Court.
C. The General Division of the High Court.
D. The State Courts.

**Answer: B.** If the estate (excluding trust assets, without deducting debts) is believed to exceed S$5 million, the application goes to the Family Division of the High Court; otherwise to the Family Courts (Family Justice (Family Proceedings before Family Division of High Court) Order 2014). A is for estates up to S$5 million. C and D do not hear probate.
*Cite: FJ (Family Proceedings before Family Division of High Court) Order 2014 s 2(a); PR5 s11; `pcp-m-0-58`*

### 0.VIII.5 — Deceased domiciled outside Singapore (P 6 r 22)

**Q0-55** · `0.VIII.5` · own question · `pcp-m-0-59`

A deceased domiciled in Indonesia left movables in Singapore. The Indonesian court has entrusted administration to his widow. To whom may the Registrar order a Singapore grant?

A. Only to a Singapore citizen.
B. To the widow, as the person entrusted with administration by the court of the domicile.
C. Only to the Public Trustee.
D. To no one until a Singapore probate action is decided.

**Answer: B.** Under P 6 r 22 the Registrar may order a grant to (a) the person entrusted by the court of the domicile, (b) the person entitled under the law of the domicile, or (c) whoever the Registrar directs. An affidavit of foreign law is usually needed. A, C and D are not in the rule.
*Cite: FJ(PAOM)R 2024 P 6 r 22; PR5 s12, s20; `pcp-m-0-59`*

### 0.VIII.6 — Letters of administration with will annexed: failure of executors and the s 13(2) order

**QSQ-P6** · `0.VIII.6` · SQ Probate Q6 [Part B 2024], official key B · `pcp-m-0-60`

Terrence recently passed away leaving a validly executed will. His will did not appoint any executors. He made specific gifts to his parents, Tony and Penny, and to his wife, Amy. He also acknowledged an outstanding debt of S$100,000 owing to his friend, George. The remainder of his estate was left to his sister, Daisy, who predeceased him. Who has the prior right to apply for a grant in respect of Terrence's estate?

A. His parents, Tony and Penny.
B. The personal representative of Daisy.
C. His wife, Amy.
D. His friend, George.

**Answer: B.** With no executor, the court grants administration with the will annexed in the s 13(2) PAA order: (1) residuary legatee; (2) the legal personal representative of a deceased residuary legatee; (3) those entitled on intestacy; (4) a legatee; (5) a creditor. Daisy was the residuary legatee and is dead, so her PR comes second, ahead of A and C (specific legatees, or intestacy beneficiaries) and D (creditor). Official key: B.
*Cite: PAA s 13(1)–(2); SQ p73 Q6, key p128; `pcp-m-0-60`*

**QPP1-6** · `0.VIII.6` `0.III.15` `0.IV.3` · PR-PP1 Q6 (no official answer) · `pcp-m-0-60` `pcp-m-0-31` `pcp-m-0-34`

Andrew in his will appointed his wife Julie and his best friend Thomas as the executors. Andrew and Julie died at the same time in a fire attending a relative's wedding dinner. Thomas is an undischarged bankrupt. Who can apply for Grant of representation for Andrew's estate?

A. The residuary legatee of Andrew's Will or the legal representative of that residuary legatee.
B. The executor of Julie's will can apply, in accordance with section 25 of the Civil Law Act 1909.
C. Thomas as the named executor of Andrew's will.
D. [as printed, unlettered] The person who can apply is determined by the priority as set out in section 7 of the Intestate Succession Act 1967.

**Answer: A.** Julie cannot act (she died with Andrew), and Thomas, an undischarged bankrupt, is disqualified from acting as PR without the court's permission (s 400 IRDA), so there is a failure of executors and administration with the will annexed goes in the s 13(2) PAA order, led by the residuary legatee or his legal personal representative. B: the chain of executorship (s 25 CLA) needs an executor who has proved the will; Julie never did. C: not without the court's permission. D: ISA priority governs administration on intestacy, not where there is a will. (Answer: A, on the usual reading that Thomas does not get permission.)
*Cite: PAA s 13; CLA s 25; IRDA s 400; PR-PP1 Q6; `pcp-m-0-60`, `pcp-m-0-31`, `pcp-m-0-34`*

### 0.VIII.7 — Letters of administration: who may apply (s 18 PAA)

**QSQ-P7** · `0.VIII.7` `0.VIII.12` `0.VIII.10` · SQ Probate Q7 [Part B 2024], official key B · `pcp-m-0-61` `pcp-m-0-66` `pcp-m-0-64`

Which of the following statements is CORRECT in relation to an application for a grant of letters of administration?

A. Where two or more persons are entitled in the same degree to apply for the grant, all such persons must either join in the application or renounce their right to apply.
B. The applicant is required to provide two sureties to the administration bond where the value of the estate exceeds S$5 million.
C. The applicant must produce documents, such as marriage and birth certificates, to establish the relationship between the beneficiaries and the deceased.
D. Before filing the originating application, the applicant must conduct searches of the probate caveat register and probate application register to determine whether any caveats or previous probate applications have been lodged in respect of the estate.

**Answer: B.** An administration bond with 2 sureties is required where the gross estate exceeds S$5 million (s 29 PAA; P 6 r 31). A: persons in the same class need not join or renounce (*Tan Hui Cheng Lily*). C: the application states the relationships (Form 162); documents proving them are not required to be produced as stated. D: searches are optional for deaths on or after 15 Dec 2003, as the system checks. Official key: B.
*Cite: PAA ss 18, 29; FJ(PAOM)R 2024 P 6 r 31; SQ p73 Q7, key p128; `pcp-m-0-61`, `pcp-m-0-66`, `pcp-m-0-64`*

**QPP1-1d** · `0.VIII.7` `0.VIII.9` · PR-PP1 Q1(d), written (no official answer); short model answer · `pcp-m-0-61` `pcp-m-0-63`

[Facts as in QPP1-1b.] Explain to Peter who can apply for a grant of letters of administration in respect of Polly's estate.

**Answer (short model answer).** The court grants administration having regard to the rights of all persons interested, the most suitable applicant being found by the order of entitlement under s 7 ISA (s 18 PAA; *Toh Seok Kheng*). Kim Seng, the spouse, is dead, so the children of Polly come next: Peter (24), Paul (23) and Mary (19), with Tony's children taking his share by representation. Children in the same class need not all join or renounce (*Tan Hui Cheng Lily*). Mary, Trisha and Terrence are minors, so the grant must go to a trust corporation or at least two individuals (s 6 PAA): in practice Peter and Paul jointly. Sarah, adopted by others, is not Polly's child and has no right to a grant.
*Cite: PAA ss 6, 18; ISA ss 3, 7; `pcp-m-0-61`, `pcp-m-0-63`*

### 0.VIII.8 — Renunciation and clearing off prior rights

**Q0-56** · `0.VIII.8` · own question · `pcp-m-0-62`

A niece wants to apply for letters of administration of her uncle's estate, but the uncle's two sisters rank ahead of her. What must she do?

A. Nothing; any relative may apply.
B. Clear off the sisters by express renunciations, signed and attested, or cite them to accept or refuse the grant.
C. Obtain the Public Trustee's consent.
D. File a caveat against the sisters.

**Answer: B.** An applicant without priority must clear off everyone above him by express renunciations (Form 166; s 3(2)(b) PAA; P 6 r 28(5)), made orally at a hearing or in writing attested by a solicitor or commissioner (s 3(2)). If one cannot be had, cite the person to accept or refuse the grant. A ignores priority. C and D are not the mechanism. A person who renounces cannot later apply unless the court allows withdrawal (s 5).
*Cite: PAA ss 3(2), 5; FJ(PAOM)R 2024 P 6 r 28(5); PR5 s12, s18, s36; `pcp-m-0-62`*

### 0.VIII.9 — Number of administrators (s 6 PAA)

**Q0-57** · `0.VIII.9` · own question · `pcp-m-0-63`

A will names one executor; a beneficiary is 15 years old. A separate intestate estate also has a 15-year-old beneficiary. Which is CORRECT?

A. Both grants need at least two individuals or a trust corporation.
B. The sole executor may take probate; the letters of administration need at least two individuals or a trust corporation.
C. Neither grant is affected by the minor.
D. Only the probate needs two grantees.

**Answer: B.** s 6 PAA requires a trust corporation or at least two individuals for letters of administration where a minor is a beneficiary or a life interest arises; it does not apply to probate, so named executors take probate however many they are. A, C and D misstate s 6.
*Cite: PAA s 6; PR5 s33, s37; `pcp-m-0-63`*

### 0.VIII.10 — Filing the originating application: documents and timing

**QSQ-P1** · `0.VIII.10` · SQ Probate Q1 [Part B 2023-S], official key C · `pcp-m-0-64`

Lovely Low has consulted you as to the application for a grant of probate for her mother Lily Low who has just passed away unexpectedly while shopping in Dubai. Which of the following statement relating to documents that you will require to apply for the grant of probate is CORRECT?

I. You will require the translation of Lily Low's death certificate into English. The death certificate in Arabic language is not required.
II. You will require Lily Low's original passport.
III. You will require Lily Low's original last will and testament.

A. I only.
B. II only.
C. III only.
D. I, II and III.

**Answer: C.** The original will must be lodged at the Probate Counter (by 4.30pm the next working day after filing). I is wrong because the foreign-language death certificate must be filed together with its translation, not replaced by it (P 1 r 11 FJ(G)R 2024; FJC PD 218). II: the passport is not a required document. Official key: C.
*Cite: PR5 s10–21; FJ(G)R 2024 P 1 r 11; SQ p71 Q1, key p128; `pcp-m-0-64`*

**QPP1-5** · `0.VIII.10` `0.VIII.11` · PR-PP1 Q5 (no official answer) · `pcp-m-0-64` `pcp-m-0-65`

What is the correct sequence for an application for Grant of Probate?

A. File the originating application; a certified true copy of the will and death certificate; produce the original will to the courts; file the supporting affidavit and administration oath; file the schedule of assets; file supplementary affidavit.
B. Get the checklist from the courts; file the originating application and other documents according to the checklist; file the schedule of assets; file the Administration Oath and Affidavit.
C. Conduct a search in the record of caveats and record of probate application; produce the original will and death certificate to the courts to obtain the checklist; file originating application; file supporting affidavit and administration oath; file the schedule of assets and supplementary affidavit.
D. Conduct a search in the record of caveats and record of probate application; file originating application; file supporting affidavit and administration oath; produce the original will and death certificate to the courts to obtain the checklist; file the schedule of assets and supplementary affidavit.

**Answer: A.** Under the 2024 procedure the originating application (Form 162) is filed with a certified true copy of the will and the death certificate; the original will reaches the Probate Counter by 4.30pm the next working day; the supporting affidavit (Form 163) with the Administration Oath follows within 14 days, exhibiting the Schedule of Assets if available, which may be filed later by supplementary affidavit. B, C and D describe an older checklist procedure; and searches are optional for deaths from 15 Dec 2003, as the system checks.
*Cite: PR5 s10–30; FJ(PAOM)R 2024 Part 6; FJC PD 2024 Part 24; `pcp-m-0-64`, `pcp-m-0-65`*

**QPP1-1a** · `0.VIII.10` `0.VIII.4` `0.VIII.8` · PR-PP1 Q1(a), written (no official answer); short model answer · `pcp-m-0-64` `pcp-m-0-58` `pcp-m-0-62`

[Facts as in QPP1-1b. Kim Seng's will names Polly, Peter and Lucy as executors; Lucy will not act as she is migrating; assume Peter agrees to act.] Advise on what needs to be considered and the procedural steps to be taken in Kim Seng's estate for the application for a grant of representation.

**Answer (short model answer).** *Grant:* a valid will with an executor able and willing, so probate (s 8 PAA). Polly died with Kim Seng (deemed first, CLA s 30) and cannot act; Lucy should renounce in writing, attested by a solicitor or commissioner (s 3(2) PAA); Peter applies alone. s 6 PAA (two administrators where a minor benefits) does not apply to probate, although Mary is 19. *Court:* the estate exceeds S$5 million (e.g. the S$10 million Bank of Singapore account), so the Family Division of the High Court. *Documents and timing:* originating application (Form 162) with a certified true copy of the will and the death certificate (French, so with an English translation); Administration Oath; the original will to the Probate Counter by 4.30pm the next working day; supporting affidavit within 14 days exhibiting the Schedule of Assets (joint assets, which pass by survivorship, are usually left out; CPF is not an estate asset). The deaths were in February 2018, so the delay of more than 6 months must be explained (P 6 r 3(8)). The will was attested by two solicitors, so no affidavit of due execution should be needed.
*Cite: PAA ss 3(2), 6, 8; CLA s 30; FJ(PAOM)R 2024 P 6 r 3(8); `pcp-m-0-64`, `pcp-m-0-58`, `pcp-m-0-62`, `pcp-m-0-65`*

### 0.VIII.11 — Supporting affidavit, Schedule of Assets and issue of the grant

**Q0-58** · `0.VIII.11` · own question · `pcp-m-0-65`

Which statement about the supporting affidavit and Schedule of Assets is CORRECT?

A. The supporting affidavit must be filed within 14 days of the originating application.
B. Assets are listed at their value at the date of the application.
C. Assets held as joint tenants must always be listed at full value.
D. Amending the Schedule of Assets needs the court's leave.

**Answer: A.** File the supporting affidavit (Form 163) within 14 days of the originating application, exhibiting the application, the will and death certificate, and the Schedule of Assets (Form 177) if available. B: market value at the date of death. C: joint assets pass by survivorship and are usually left out. D: the Schedule may be amended without leave by supplementary affidavit. The grant then issues automatically as a digital copy.
*Cite: PR5 s22–30, s58; FJC PD 212(5); `pcp-m-0-65`*

### 0.VIII.12 — Administration bond and sureties (s 29 PAA)

**QPP1-1e** · `0.VIII.12` · PR-PP1 Q1(e), written (no official answer); short model answer · `pcp-m-0-66`

[Facts as in QPP1-1b. Polly's estate includes S$2 million in a current account, shares worth S$4 million, an Audi and a London flat worth GBP1 million.] Explain to Peter whether the court will require security before a grant of letters of administration issues for Polly's estate, and what can be done.

**Answer (short model answer).** Yes. A grantee of letters of administration must give an administration bond (Form 168) with 2 sureties where the gross estate exceeds S$5 million, or there is a minority interest (s 29 PAA; P 6 r 31; FJC PD 214). Both apply: the estate is well over S$5 million and Mary, Trisha and Terrence are minors. The administrators sign the bond jointly. The court may vary or dispense with sureties (s 29(3)) on a summons and affidavit by all administrators, with the written consent of all adult beneficiaries (FJC PD 215). Sureties are ordinarily dispensed with where the administrator takes the whole estate (s 29(5)), which is not this case.
*Cite: PAA s 29; FJ(PAOM)R 2024 P 6 r 31; FJC PD 214–215; `pcp-m-0-66`*

**Q0-59** · `0.VIII.12` · own question · `pcp-m-0-66`

In which case is an administration bond with sureties NOT ordinarily required?

A. The gross estate is S$7 million.
B. A beneficiary is a minor.
C. The grantee is a creditor.
D. The grant is probate to the named executors.

**Answer: D.** No bond is needed for probate. A, B and C are all listed cases under s 29 PAA and P 6 r 31 (estate over S$5 million; minority interest; grantee a creditor), with life interests, a beneficiary lacking capacity, and where the Registrar thinks fit.
*Cite: PAA s 29; FJ(PAOM)R 2024 P 6 r 31; `pcp-m-0-66`*

### 0.VIII.13 — Resealing a foreign grant (ss 47–49 PAA)

**Q0-60** · `0.VIII.13` · own question · `pcp-m-0-67`

A deceased domiciled in Australia left shares in Singapore. Probate was granted in New South Wales. What is the simplest way to deal with the Singapore shares?

A. Apply for resealing of the Australian grant in Singapore.
B. Apply for a fresh Singapore grant; foreign grants can never be resealed.
C. Ask the Singapore company to transfer the shares on the Australian grant alone.
D. Apply to the Public Trustee.

**Answer: A.** A grant by a court of a Commonwealth country or Hong Kong may be resealed in Singapore (ss 47–49 PAA) and then has the same effect as a Singapore grant (s 47(2)); the court issues a Memorandum of Resealing. B: only a grant from outside the Commonwealth and Hong Kong needs a fresh application. C: a foreign grant has no effect in Singapore until resealed. D is not the route.
*Cite: PAA ss 47–49; PR5 s5, s47–56; `pcp-m-0-67`*

**Q0-82** · `0.VIII.13` · own question · `pcp-m-0-67`

A widow applies to reseal in Singapore a grant made in a Commonwealth country where the deceased held citizenship. The deceased's father enters a caveat, alleging the deceased was never domiciled there and the widow obtained the foreign grant by fraud. Which statement is CORRECT?

A. A Commonwealth grant must be resealed once it is produced, so the caveat has no effect.
B. The applicant must prove domicile in the granting jurisdiction; even then resealing is discretionary, and if the caveator raises a serious question to be tried the court should direct a probate action.
C. Fraud allegations can never be raised in Singapore; they belong only in the foreign court.
D. Citizenship of the granting country conclusively proves domicile.

**Answer: B.** s 47(4) PAA makes domicile the threshold (burden on the applicant), and "may" in s 47(1) gives a discretion. A contested resealing may be disposed of summarily only if there is no serious question to be tried. A ignores both. C: extrinsic fraud may be raised; intrinsic fraud needs fresh evidence. D: domicile needs residence and intention; buying citizenship without ever entering the country did not establish it.
*Cite: PAA s 47; WKR v WKQ [2023] SGHC(A) 35 at [39], [44]–[45], [50]–[71]; `pcp-m-0-67`*

### 0.VIII.14 — Contentious probate: probate actions

**Q0-61** · `0.VIII.14` · own question · `pcp-m-0-68`

A son wants a will declared invalid for undue influence. How does he begin a probate action, and what can the court do meanwhile?

A. By originating application without notice; the court may distribute the estate pending the action.
B. By originating claim issued out of the Registry; pending the action the court may grant administration to someone who cannot distribute.
C. By filing a caveat; the caveat itself decides validity.
D. By summons in the Family Courts; no interim grant is possible.

**Answer: B.** A probate action is begun by originating claim issued out of the Registry, endorsed with the parties' interests (P 7 r 2); pending it, the court may grant administration under s 20 PAA, without power to distribute, on summons in the action (P 7 r 21). A: no distribution pending the action. C: a caveat only stops a grant without notice. D: wrong process.
*Cite: PAA s 20; FJ(PAOM)R 2024 P 7 rr 2, 21; `pcp-m-0-68`*

### 0.VIII.15 — Caveats

**Q0-62** · `0.VIII.15` · own question · `pcp-m-0-69`

A caveator is served with a warning (Form 171). Within what time must he file a notice of intention to contest or not to contest?

A. 8 days after service of the warning.
B. 14 days after service of the warning.
C. 21 days after service of the warning.
D. 6 months after entry of the caveat.

**Answer: B.** Under P 6 r 34(11) FJ(PAOM)R 2024 the caveator files Form 172 within 14 days after service of the warning; a caveator who contests must file and serve a summons for directions within 21 days after service of the warning (r 34(13)). A is the old 2014 period for an appearance. C is the summons-for-directions period. D is how long a caveat lasts (r 34(3)).
*Cite: PAA s 33; FJ(PAOM)R 2024 P 6 r 34; `pcp-m-0-69`*

### 0.VIII.16 — Citations

**Q0-63** · `0.VIII.16` · own question · `pcp-m-0-70`

An executor named in a will has been collecting rents from estate property for a year but refuses to apply for probate. What can an interested beneficiary do?

A. Nothing until the executor applies.
B. After 6 months from death, cite the executor to show cause why he should not be ordered to take a grant.
C. Apply for probate in his own name immediately.
D. File a caveat, which compels the executor to apply.

**Answer: B.** An executor who has intermeddled may, after 6 months from death, be cited by any interested person to show cause why he should not be ordered to take a grant (P 6 r 39(3)). The citor must first enter a caveat (r 38(4)) and serve the citation personally. A, C and D are wrong.
*Cite: FJ(PAOM)R 2024 P 6 rr 38–39; `pcp-m-0-70`*

### 0.VIII.17 — When personal representatives can act; acting jointly

**QSQ-P8** · `0.VIII.17` · SQ Probate Q8 [Part B 2024], official key A · `pcp-m-0-71`

Which of the following persons has the legal capacity to commence and continue legal proceedings on behalf of the deceased's estate?

A. An executor named in the deceased's will, even though a grant of probate has not yet been extracted.
B. The spouse or child of the deceased.
C. An applicant for a grant of letters of administration in whose favour the court has ordered that the grant be made.
D. The deceased's donee appointed under a lasting power of attorney.

**Answer: A.** An executor's authority comes from the will, so he may start proceedings before probate, though he needs the grant to get judgment or enforce (*Lee Han Tiong*). B: next of kin have no authority as such (*Teo Gim Tiong*). C: an administrator has no authority until the grant itself. D: an LPA donee's authority ends on the donor's death. Official key: A.
*Cite: Lee Han Tiong [1996] 2 SLR(R) 833; Teo Gim Tiong [2014] 4 SLR 15; SQ p74 Q8, key p128; `pcp-m-0-71`*

**Q0-64** · `0.VIII.17` · own question · `pcp-m-0-71`

Two administrators hold a grant. One of them alone signs a contract to sell an estate asset. Which is CORRECT?

A. The contract binds the estate, as it would for one of two executors.
B. The contract does not bind the estate unless both administrators ratify it.
C. Administrators may always act severally.
D. The contract binds the signing administrator's own share only.

**Answer: B.** Administrators must act jointly, and one administrator's act does not bind the estate unless all ratify (*Tacplas Property Services v Lee Peter Michael*). A: the rule differs for executors, where one's act binds the estate. C is wrong. D has no basis.
*Cite: Tacplas Property Services v Lee Peter Michael [2000] 1 SLR(R) 159; `pcp-m-0-71`*

### 0.IX Mental Capacity Act: principles, LPAs, deputies, Public Guardian

Sub-points 0.IX.1–0.IX.16. Real questions: SQ Probate Q9 (0.IX.10), Q10 (0.IX.15); PP2 Q2 (0.IX.10), Q4 (0.IX.13, 0.IX.14), PP2 Q1(a)–(d). PP2 Q3 (what a donee may do: gifts to herself, settling P's assets on trust, insurance nomination) is left out: the course materials state the cash-gift restriction only in outline (PR6 s31, "note s 14(3)") and say nothing on a donee settling assets on trust, and SSO could not be reached to check ss 13–14 MCA, so it is not answered by guesswork. Own questions cover the rest.

### 0.IX.1 — Statutory principles (s 3 MCA)

**Q0-65** · `0.IX.1` · own question · `pcp-m-0-72`

An 80-year-old client insists on giving away most of her savings to a temple, against her children's advice. Which MCA principle is most relevant?

A. A person is assumed to lack capacity once over 75.
B. An unwise decision does not by itself mean a person lacks capacity.
C. Any decision against family advice must be in the person's best interests.
D. A person is unable to decide if she refuses help.

**Answer: B.** s 3(4) MCA: an unwise decision does not by itself mean a person lacks capacity. s 3(2): capacity is assumed unless shown otherwise, so A is wrong. C: best interests (s 3(5)) governs acts done for a person who lacks capacity. D: a person is not treated as unable to decide until all practicable steps to help have failed (s 3(3)).
*Cite: MCA s 3(2)–(6); PR6 s4–5; `pcp-m-0-72`*

### 0.IX.2 — Lack of capacity: the test (ss 4–5; Re BKR)

**Q0-66** · `0.IX.2` · own question · `pcp-m-0-73`

Which statement about the MCA test of incapacity is CORRECT?

A. A person who can retain information only briefly is unable to decide.
B. The test is decision-specific and time-specific, and requires an impairment of the mind or brain causing the inability.
C. Lack of capacity must be proved beyond reasonable doubt.
D. A medical certificate is conclusive.

**Answer: B.** A person lacks capacity if, at the material time, he cannot decide because of an impairment of or disturbance in the mind or brain (s 4(1)); *Re BKR* requires functional inability, clinical impairment and a causal link. A: retaining information briefly is enough (s 5(3)). C: balance of probabilities (s 4(4)). D: courts look at actual circumstances (*BUV v BUU*).
*Cite: MCA ss 4–5; Re BKR [2015] 4 SLR 81; BUV v BUU [2020] 3 SLR 1041; `pcp-m-0-73`*

### 0.IX.3 — Best interests (s 6)

**Q0-67** · `0.IX.3` · own question · `pcp-m-0-74`

In deciding what is in P's best interests concerning his property, which must a deputy consider?

A. Only the wishes of P's eldest child.
B. P's past and present wishes, beliefs and values, and preserving the property for P's maintenance in his lifetime.
C. What the deputy would want in P's place.
D. P's age and appearance.

**Answer: B.** s 6 MCA: consider all relevant circumstances, including P's past and present wishes, beliefs and values (s 6(8)), preserving property for his maintenance (s 6(7)), regaining capacity and P's participation, and the views of carers, donees and deputies (s 6(9)). A and C are not the test. D: the decision cannot rest on age, appearance or behaviour (s 6(1)).
*Cite: MCA s 6; PR6 s11–16; `pcp-m-0-74`*

### 0.IX.4 — Acts in connection with care or treatment (ss 7–10)

**Q0-68** · `0.IX.4` · own question · `pcp-m-0-75`

A nurse bathes and dresses an elderly patient with advanced dementia who cannot consent. Is the nurse protected from liability?

A. No; the patient's written consent is always needed.
B. Yes, if she took reasonable steps to establish lack of capacity and reasonably believed it and that the act was in the patient's best interests; she remains liable for negligence.
C. Yes, completely, even if she acts negligently.
D. Yes, even if it is against a decision of the patient's deputy.

**Answer: B.** s 7 MCA protects a person doing an act in connection with P's care if he took reasonable steps to establish lack of capacity and reasonably believed P lacked capacity and the act was in P's best interests; liability for negligence remains. A ignores s 7. C: negligence is not excused. D: s 7 does not authorise acts against a donee's or deputy's decision.
*Cite: MCA ss 7–10; PR-SYL p11 item 3(a); `pcp-m-0-75`*

### 0.IX.5 — General powers of the court (ss 19, 20, 22, 23)

**Q0-69** · `0.IX.5` · own question · `pcp-m-0-76`

P lacks capacity and needs a single decision to sell one investment. There is no LPA. What does the court prefer?

A. To appoint a deputy with wide general powers.
B. To make the decision itself by order, rather than appoint a deputy.
C. To refuse, because only a donee can sell P's property.
D. To refer the matter to the Public Guardian for decision.

**Answer: B.** Under s 20 MCA the court may make the decision itself or appoint a deputy, and a court decision is preferred to appointing a deputy; any deputy's powers should be as limited in scope and duration as practicable (s 20(4)). A, C and D are wrong. The court may also make declarations (s 19).
*Cite: MCA ss 19, 20(4), 22, 23; `pcp-m-0-76`*

### 0.IX.6 — Excluded decisions (ss 26–29)

**Q0-70** · `0.IX.6` · own question · `pcp-m-0-77`

Which decision may the court authorise a deputy to make for P?

A. Consenting to P's divorce on 3 years' separation.
B. Voting for P in a general election.
C. Selling P's house to pay for his nursing care.
D. Making an advance medical directive for P.

**Answer: C.** Selling P's property is a property and affairs matter within s 23 MCA. A and D are excluded decisions under s 26 (divorce on separation; making or revoking an advance medical directive); B is excluded by s 28 (voting). No donee, deputy or court can make them.
*Cite: MCA ss 23, 26, 28; `pcp-m-0-77`*

### 0.IX.7 — Lasting power of attorney: nature, donor, Form 1 and Form 2

**Q0-71** · `0.IX.7` · own question · `pcp-m-0-78`

Which statement about LPAs is CORRECT?

A. A 19-year-old may make an LPA.
B. Form 1 allows up to 2 donees plus 1 replacement; Form 2 is drafted by a lawyer with tailored powers.
C. An LPA is valid without registration.
D. An LPA operates while the donor still has capacity.

**Answer: B.** Form 1 grants general powers from a fixed checklist with up to 2 donees and 1 replacement; Form 2 has customised powers drafted by a lawyer and no limit on donees. A: the donor must be at least 21 and have capacity (s 11(2)). C: it must be made and registered in the prescribed form. D: it is used when P lacks capacity (s 11(1)).
*Cite: MCA s 11; MCR reg 4C; PR6 s19–22; `pcp-m-0-78`*

### 0.IX.8 — Who may be a donee; joint or joint and several

**Q0-72** · `0.IX.8` · own question · `pcp-m-0-79`

A donor appoints her two sons as donees but the LPA does not say how they are to act. One son is an undischarged bankrupt. The LPA covers property and affairs. What is the effect?

A. The sons act jointly and severally, so the LPA is created for the other son.
B. The sons act jointly because the LPA is silent, so no LPA is created.
C. The LPA is created for both sons.
D. The bankrupt son may act with the court's permission.

**Answer: B.** If the LPA is silent, donees act jointly (s 12(5)); an undischarged bankrupt cannot be a donee for property and affairs (s 12(2)); and where donees act jointly and one fails the requirements, no LPA is created (s 12(6)). A would follow only if they were appointed jointly and severally (s 12(7)). C and D are wrong.
*Cite: MCA s 12(1)–(7); PR6 s25–27; `pcp-m-0-79`*

### 0.IX.9 — Donee's powers and restrictions (ss 11(4), 13, 14)

**Q0-73** · `0.IX.9` · own question · `pcp-m-0-80`

Which act may a property and affairs donee do for a donor who has lost capacity?

A. Execute a will for the donor.
B. Make a CPF nomination in favour of the donor's children.
C. Pay the donor's medical bills from her bank account.
D. Revoke the donor's insurance nomination.

**Answer: C.** Managing the donor's finances in her best interests is within a property and affairs LPA. A, B and D are expressly outside a donee's powers: no will for P, and no making or revoking of a CPF memorandum or a CPF or insurance nomination (s 14). A donee also cannot decide if he reasonably believes P has capacity (s 13(1)).
*Cite: MCA ss 11(4), 13, 14; PR6 s28–33; `pcp-m-0-80`*

### 0.IX.10 — Certificate issuers (reg 7 MCR; Sum Chong Mun)

**QSQ-P9** · `0.IX.10` · SQ Probate Q9 [Part B 2024], official key A · `pcp-m-0-81`

You are a partner in a law firm. In which of the following circumstances may you act as the certificate issuer for a lasting power of attorney?

A. Betty, a tea lady employed by the same law firm, wishes to execute a lasting power of attorney appointing her niece, Priscilla, as her donee.
B. June wishes to execute a lasting power of attorney appointing her brother, Joseph, as her donee. Joseph is a partner in the same law firm as you.
C. Your wife, Gloria, wishes to execute a lasting power of attorney appointing her sister as her donee.
D. Thomas wishes to execute a lasting power of attorney appointing your father-in-law as his donee.

**Answer: A.** Reg 7(2) MCR disqualifies a business partner of the donor or a donee (B: Joseph is your partner), and a family member of the donor or a donee (C: Gloria, the donor, is your spouse). Betty is the firm's employee, but reg 7(2) is about business partners or employees of the donor or donee, not of the issuer, so A is allowed. D: the official key treats it as barred too. On the text of reg 2, "family member" of the donee (your father-in-law) lists his spouse, children, parents, parents-in-law, siblings and same-household relatives, not a son-in-law, so D is barred only if you live in his household. Choose A in the exam. Official key: A.
*Cite: MCR regs 2, 7(1)–(3); SQ p74 Q9, key p128; `pcp-m-0-81`*

**QPP2-2** · `0.IX.10` · PR-PP2 Q2 (no official answer) · `pcp-m-0-81`

Geraldine approached her friend Patrick to be the donee of her lasting power of attorney. Patrick offered to ask his brother-in-law Bill to be the certificate issuer for this lasting power of attorney. Bill can be the certificate issuer because:

A. He is an advocate and solicitor of the Supreme Court, but has left practice for more than 5 years.
B. He is related to the donee Patrick by marriage and stay next door to Patrick.
C. He and Patrick both stay with their spouses' parents.
D. Geraldine and Bill are business partners.

**Answer: B.** A brother-in-law is not on the reg 2 list of a donee's "family members" (spouse, child, parent, parent-in-law, sibling) unless he is a relative by marriage living in the same household; living next door is not the same household, so Bill is not disqualified. A: an advocate and solicitor qualifies only with a practising certificate, practising Singapore law (reg 7(1)). C: if they live in the same household with the same parents-in-law, Bill is a relative by marriage in the donee's household, so disqualified. D: a business partner of the donor is disqualified (reg 7(2)).
*Cite: MCR regs 2, 7(1)–(2); PR6 s34–37; PR-PP2 Q2; `pcp-m-0-81`*

**QPP2-1d** · `0.IX.10` · PR-PP2 Q1(d), written (no official answer); short model answer · `pcp-m-0-81`

[Facts in brief.] Wayne wants to make an LPA and asks his brother-in-law, a trainee in a law firm, to help. Can the trainee be the certificate issuer, and if not, may the trainee bring the LPA, signed by Wayne in front of him, to his partner to certify?

**Answer (short model answer).** No to both. A certificate issuer must be a psychiatrist, an OPG-accredited medical practitioner, or an advocate and solicitor with a practising certificate practising Singapore law (reg 7(1) MCR); a trainee is none of these. (Being Wayne's brother-in-law would disqualify him only if he lived in Wayne's household, reg 2.) Nor can a partner certify on the trainee's say-so: the issuer must meet the donor personally, explain the LPA, satisfy himself of capacity and the absence of fraud or undue pressure, and must not delegate (*Law Society v Sum Chong Mun*). The trainee may help Wayne fill in Form 1 or gather his instructions, and arrange for him to see a qualified issuer in person.
*Cite: MCR regs 2, 7; MCA First Schedule para 2(e); Law Society v Sum Chong Mun [2017] 4 SLR 707; `pcp-m-0-81`*

### 0.IX.11 — Registering an LPA

**Q0-74** · `0.IX.11` · own question · `pcp-m-0-82`

When can a donee under a registered LPA begin to act?

A. As soon as the OPG registers the LPA.
B. Once a registered medical practitioner certifies, in the prescribed report, that the donor has lost capacity.
C. Three weeks after the donees are notified.
D. When the donor signs the LPA.

**Answer: B.** The donee acts only once a registered medical practitioner certifies that P has lost capacity (s 13(10) MCA). A and C describe registration: after a mandatory 3-week wait following notice to the donees, if no valid objection is received, it is registered. D is too early.
*Cite: MCA s 13(10); MCR regs 13, 15; PR6 s38–50; `pcp-m-0-82`*

### 0.IX.12 — Revocation, termination and the court's powers over LPAs (ss 15–18)

**Q0-75** · `0.IX.12` · own question · `pcp-m-0-83`

A donor appointed her husband as sole donee for both personal welfare and property and affairs, with no replacement. The donor is later made bankrupt. What is the effect?

A. The whole LPA is revoked.
B. Only the property and affairs powers are revoked; the personal welfare powers remain.
C. Nothing; bankruptcy has no effect on an LPA.
D. The husband must apply to court to continue.

**Answer: B.** The donor's bankruptcy revokes the LPA's property and affairs powers only (s 15(3)–(8) MCA). A overstates it. C is wrong. D: no application is needed for the welfare powers. The court may also decide validity and revoke an LPA for fraud, undue pressure or misconduct (s 17).
*Cite: MCA ss 15, 17, 18; PR6 s47–48; `pcp-m-0-83`*

### 0.IX.13 — Deputies: when, who and the principles (ss 20, 21, 24, 25A)

**QPP2-4** · `0.IX.13` `0.IX.14` · PR-PP2 Q4 (no official answer) · `pcp-m-0-84` `pcp-m-0-85`

Victor and Janet are married. Victor has however left Janet about 10 years ago and has been residing with his mistress Alice. Janet has been taking care of her two minor children with Victor. Victor has an aneurysm and has been in a coma for about 3 months. It is not clear whether he will recover. In an application for appointment of deputy, which of the following statements are correct?

A. As Victor and Janet's two children are minors, they cannot be deputies.
B. Alice is a "relevant person" and needs to be informed of the application to appoint a deputy for Victor.
C. Janet is a "relevant person" and can make an application for the appointment of Victor's deputy.
D. All of the above are correct.

**Answer: D.** A: an individual deputy must be at least 21 (s 24 MCA), so minors cannot be appointed. B: relevant persons include, beyond immediate family, relatives or friends with a close relationship with P and those caring for him (FJC PD 2024 para 74); Alice, who has lived with Victor for 10 years, is one and should be served. C: Janet, as spouse, is a relevant person, and as she is related by marriage she needs no permission to apply (s 38; P 5 r 7).
*Cite: MCA ss 24, 38; FJ(G)R 2024 P 5 r 7; FJC PD 2024 para 74 (PR6 s64–65); Cyril-PR §5.7.2; `pcp-m-0-84`, `pcp-m-0-85`*

**QPP2-1a** · `0.IX.13` · PR-PP2 Q1(a), written (no official answer); short model answer · `pcp-m-0-84`

[Facts in brief.] Bruce (56) has rapidly worsening Alzheimer's. He lives with his friend Wayne (60), a pre-school teacher. Bruce is separated from his wife Selina (53) and has two sons, Barry (22) and Allen (18). Wayne wants to sell Bruce's unoccupied HDB flat, pay off a personal loan and use the balance for Bruce's care. Advise Wayne on the considerations if he applies to be Bruce's deputy.

**Answer (short model answer).** The court may appoint a deputy where P lacks capacity (s 20 MCA), applying s 3 and best interests, and prefers a court decision to a deputy, and powers as limited in scope and duration as practicable (s 20(4)); it prefers P's parents or guardian (s 21), none here. Wayne is an individual over 21 who would act without pay, so eligible (s 24). He is not related to Bruce by blood or marriage, so he needs the court's permission to apply (s 38; P 5 r 7). Selina (spouse) and Barry (over 21) are relevant persons to be served or to consent; Allen, 18, is not yet a relevant person by age but is a family member likely to have an interest. The court may require security and reports. The powers sought (sale of the flat, paying the loan, operating the bank account) must be drafted specifically; selling an HDB flat also needs HDB's requirements met.
*Cite: MCA ss 3, 20, 21, 24, 38; FJ(G)R 2024 P 5 r 7; `pcp-m-0-84`*

### 0.IX.14 — Deputyship application procedure

**QPP2-1b** · `0.IX.14` · PR-PP2 Q1(b), written (no official answer); short model answer · `pcp-m-0-85`

[Facts as in QPP2-1a.] State the steps to obtain a court order appointing Wayne as Bruce's deputy for personal welfare and property and affairs.

**Answer (short model answer).** (1) Ask for permission in the main application, since Wayne is not related to Bruce (s 38; P 5 r 7). (2) File an originating application stating that it concerns both welfare and property, and the specific powers sought. (3) File a supporting affidavit (Form 60) exhibiting OPG searches (LPA, past MCA orders) and a Wills Registry search. (4) File the doctor's affidavit (Form 61) exhibiting a medical report not more than 6 months old, from an examination less than 12 months before the report, giving a clear opinion on incapacity for both welfare and property, and prognosis. (5) Serve the relevant persons (Selina, Barry) with the papers and Notice of Proceedings, or file their consents (Form 108B). (6) Notify Bruce in a suitable way and file Form 81. Costs come from Bruce's estate unless ordered otherwise.
*Cite: MCA s 38; FJ(G)R 2024 P 5 r 7, P 7 r 22; FJC PD 2024 paras 56–76; PR6 s55–67; `pcp-m-0-85`*

**Q0-76** · `0.IX.14` · own question · `pcp-m-0-85`

Which medical report satisfies the deputyship requirements?

A. A report dated 10 months before filing, based on an examination the day before the report.
B. A report dated 2 months before filing, based on an examination 8 months before the report, with a clear opinion on incapacity and prognosis, exhibited to the doctor's affidavit.
C. A report dated 1 month before filing, attached to the applicant's affidavit without a doctor's affidavit.
D. A report that says only that P "may have some memory problems".

**Answer: B.** The report must be not more than 6 months old when filed, from an examination less than 12 months before the report, with a clear opinion on incapacity and prognosis, exhibited to the doctor's affidavit (Form 61). A is too old. C lacks the doctor's affidavit. D gives no clear opinion.
*Cite: FJC PD 2024 para 59(7)–(8); PR6 s62–63; `pcp-m-0-85`*

**Q0-83** · `0.IX.14` · own question · `pcp-m-0-85`

P was injured in a road accident and lacks capacity. P's daughter applies to be appointed P's deputy. The driver's insurer, defending P's damages claim, applies to be joined to the deputyship application to dispute P's capacity. Which statement is CORRECT?

A. The insurer is a relevant person and must be joined.
B. The court has a discretion to join a party, but an alleged tortfeasor generally should not be joined, as the disadvantages of joinder outweigh the advantages.
C. Anyone who may be affected by the deputy's appointment is entitled to be joined.
D. The costs of the deputyship application are always borne by the applicant.

**Answer: B.** Joinder is discretionary (P 6 r 6 General Rules), and in *TWD v UQE* the court held that joining the alleged tortfeasor would generally delay the application, add costs and give it access to P's information. A and C overstate the position. D: costs are paid by P or charged to P's estate unless the court otherwise directs (P 22 r 4).
*Cite: TWD v UQE [2019] 3 SLR 662 at [56]–[84]; Cyril-PR §5.7.6, §5.7.8; `pcp-m-0-85`*

### 0.IX.15 — Deputy's powers and restrictions (ss 22, 23, 25)

**QSQ-P10** · `0.IX.15` · SQ Probate Q10 [Part B 2024], official key D; answer on the statute C · `pcp-m-0-86`

Louise has suffered a stroke and is now in a coma. Her court-appointed deputy is her 22-year-old daughter, Pansy, who is currently a university student. Which of the following statements is CORRECT?

I. Pansy has the power to restrict Louise's sisters, whom Louise had always found to be bothersome, from visiting Louise.
II. Pansy has the power to collect rent from the tenant leasing Louise's property.
III. Pansy has the power to provide maintenance for Louise's parents and for Pansy's 13-year-old brother.

A. I and II.
B. III only.
C. II and III.
D. I, II and III.

**Answer: C on the statute; the official key says D.** II and III are property and affairs powers the court may confer (s 23 MCA: managing P's property; maintaining P's parents and minor children). I is a power s 25(2)(a) says a deputy may not be given: to prohibit a named person from having contact with P (the court itself may make that order under s 22). The official key gives D, which treats I as within a deputy's powers. Know both: if the exam repeats this question, the examiners' expected answer has been D; the law is C.
*Cite: MCA ss 22, 23, 25(2)(a); PR6 s68–69; SQ p75 Q10, key p128; `pcp-m-0-86`*

**QPP2-1c** · `0.IX.15` `0.IX.6` · PR-PP2 Q1(c), written (no official answer); short model answer · `pcp-m-0-86` `pcp-m-0-77`

[Facts as in QPP2-1a.] Wayne wants the deputyship application to include powers to (i) divorce Selina, as Bruce always wanted; (ii) make a CPF nomination for Bruce's two sons; and (iii) donate to Alzheimer's research. Advise.

**Answer (short model answer).** None can be included. (i) Consent to divorce on 3 years' separation is an excluded decision under s 26 MCA, which no donee, deputy or court can make for P. (ii) A deputy may not be given power to make or revoke a CPF nomination (s 25). (iii) A deputy may not be given power to make gifts of P's property (s 25), and a donation is a gift. Bruce's past wishes are relevant to best interests (s 6(8)) but cannot expand the deputy's powers.
*Cite: MCA ss 6(8), 25, 26; PR6 s68–70; `pcp-m-0-86`, `pcp-m-0-77`*

### 0.IX.16 — The Public Guardian (ss 31–32)

**Q0-77** · `0.IX.16` · own question · `pcp-m-0-87`

Which is a function of the Public Guardian?

A. Appointing deputies.
B. Keeping the registers of LPAs, deputy orders and professional deputies, and supervising court-appointed deputies.
C. Deciding whether P lacks capacity.
D. Acting as donee for every P without an LPA.

**Answer: B.** The Public Guardian keeps the registers, supervises deputies, directs Board of Visitors visits, receives security and reports, reports to the court and investigates complaints (ss 31–32 MCA). A and C are for the court (ss 19–20). D is wrong.
*Cite: MCA ss 31–32; PR6 s72; `pcp-m-0-87`*

## 1 · Real Estate (Conveyancing)

**Real case facts used by the `Q1-25F` questions (PYP 2025 PCP Paper 2, facts for Qs 21–40, transcribed in brief).** Mdm Lim, a Singaporean, redeveloped the family Good Class Bungalow at Pearl's Hill into a four-unit condominium. On 4 April 2023 her eldest son Abel became sole legal owner of Unit #04-01 by a transfer from her without consideration. Abel married Meiniang, a Malaysian citizen, who moved in on 8 December 2023 and later died in a fire. On 8 April 2025 Abel agreed to sell the unit to his brother Better Lim for S$500,000, although its market value was S$1,500,000. The Option to Purchase: option fee S$5,000 (1%) on issue; exercise within 2 weeks; option exercise fee S$20,000 on or before exercise; subject to the LSCS 2020, the option's terms prevailing; completion at Ibrahim and Co LLP, the vendor's lawyers, 12 weeks from the option date; "as-is where-is"; vacant possession; 2% commission payable by the vendor to Abel's agent; and a non-merger clause.

**Real case facts used by the `Q1-23F` questions (PYP 2023 PCP Paper 2, facts for Qs 26–44, in brief).** You act for Mr and Mrs Sham in buying a condominium unit at 1 Second Street #02-01 for S$3,800,000. Mr Sham is a Singapore PR holding a US passport and owns a beachfront resort in the Maldives; Mrs Sham is a Singapore citizen and owns no property. The owner is Miss Junko, a Japanese citizen who bought about 4 years earlier. The OTP (1% paid) was issued on 16 October 2023, exercisable within 2 weeks by delivering the signed Acceptance Copy with 4% to the vendor's solicitors, ABC LLP, as stakeholders; LSCS 2020 applies, the option prevailing; completion at ABC LLP on 25 December 2023; "as-is"; vacant possession. The Shams will use S$500,000 of CPF each and a S$1,000,000 bank loan.

### 1.I Introduction: parties, property types, regulations and formalities

Sub-points 1.I.1–1.I.6. No real question; own questions Q1-1 to Q1-6.

### 1.I.1 — Parties and their capacity

**Q1-1** · `1.I.1` · own question · `pcp-m-1-1`

Which of the following can hold land in its own name?

A. A registered society.
B. A 20-year-old Singapore citizen.
C. A non-profit company limited by guarantee registered under the Companies Act.
D. An undischarged bankrupt individual, freely.

**Answer: C.** A company registered under the Companies Act generally has capacity to own land; the old s 23(2) licence requirement for non-profit companies has been deleted, so they now have full capacity. A: a society holds land only through its trustees. B: an individual must be 21 and sui juris. D: an individual purchaser must not be bankrupt.
*Cite: RE1 s4; RE-CS1 s31; `pcp-m-1-1`*

### 1.I.2 — Types of property and land registration systems

**Q1-2** · `1.I.2` · own question · `pcp-m-1-2`

Which statement is CORRECT?

A. Singapore has a single land registration system, the Torrens system.
B. ABSD applies to the purchase of a commercial shop unit.
C. Singapore has two systems: the Register of Deeds (unregistered land) and the Land Titles Register (Torrens).
D. GST applies to the sale of a condominium unit by a GST-registered owner.

**Answer: C.** The two systems are the Register of Deeds (common law) and the Land Titles Register (Torrens). B: non-residential property attracts no ABSD (GST may apply). D: residential property is GST-exempt. A ignores the Register of Deeds.
*Cite: RE1 s3, s5–6; RE-CS1 s2; `pcp-m-1-2`*

### 1.I.3 — Sale by a deceased owner's personal representative (s 35 CLPA)

**Q1-3** · `1.I.3` · own question · `pcp-m-1-3`

An administrator wants to sell the deceased's house 7 years after the death. The deceased died intestate. What is needed?

A. Nothing; a personal representative may always sell.
B. The court's sanction, because more than 6 years have passed and there is no power of sale or trust for sale in a will.
C. The consent of the purchaser's bank.
D. A fresh grant de bonis non.

**Answer: B.** s 35(2) CLPA: no sale or mortgage of a deceased's land by his PR more than 6 years after death, unless with the court's sanction or under a power of sale or trust for sale in the will. There is no will, so the court must sanction it. A ignores s 35(2). C and D are not the requirement.
*Cite: CLPA s 35(1)–(2); RE1 s7; `pcp-m-1-3`*

### 1.I.4 — Formalities: contracts for the sale of land

**Q1-4** · `1.I.4` · own question · `pcp-m-1-4`

A buyer and seller agree the sale of a terrace house over a series of emails setting out the parties, property and price. Is there an enforceable contract?

A. No; only a signed OTP can create a contract for land.
B. Possibly yes; a contract for land must be evidenced in writing, and email correspondence can satisfy this.
C. No; contracts for land must be by deed.
D. Yes, even if the agreement was purely oral.

**Answer: B.** s 6(d) CLA requires a contract for the sale of land to be evidenced in writing; emails can satisfy it (*Joseph Mathew v Singh Chiranjeev*). A and C overstate the formality. D: an oral contract needs a written memorandum.
*Cite: CLA s 6(d); Joseph Mathew v Singh Chiranjeev [2010] 1 SLR 338; `pcp-m-1-4`*

### 1.I.5 — Ways to conclude a contract; transfers not under a contract

**Q1-5** · `1.I.5` · own question · `pcp-m-1-5`

Which of the following conveyances is NOT made under a contract for sale?

A. A transfer after the exercise of an option to purchase.
B. A transfer under a put and call option.
C. A transfer to a beneficiary on distribution of an intestate estate.
D. A transfer after a public auction.

**Answer: C.** Distributions on intestacy, matrimonial orders and the exercise of statutory rights are conveyances not under a contract. A, B and D are all ways to conclude a contract, as are S&P agreements, exchange of correspondence, prescribed developer agreements, tenders and oral contracts evidenced in writing.
*Cite: RE3 s3; RE1 s11–12; `pcp-m-1-5`*

### 1.I.6 — GST and withholding tax

**Q1-6** · `1.I.6` · own question · `pcp-m-1-6`

A GST-registered company sells an office unit. The contract incorporates the LSCS 2020 and says nothing about GST. Who bears the GST?

A. The vendor, always.
B. The purchaser, under LSCS Condition 7.2.
C. No GST applies to any sale of property.
D. GST is split equally.

**Answer: B.** Only residential property is GST-exempt; a sale of non-residential property by a GST-registered vendor attracts GST, which under Condition 7.2 the purchaser pays. A: the parties may negotiate, but the default is 7.2. C is wrong for non-residential property. D has no basis. Separately, if the vendor were a non-resident property trader, the purchaser's solicitor would withhold 15% (s 45D ITA; Condition 7.3).
*Cite: LSCS 2020 Conditions 7.2–7.3; ITA s 45D; RE3 s15–17; `pcp-m-1-6`*

### 1.II Searches, title and legal requisitions

Sub-points 1.II.1–1.II.6. Real questions: SQ Real Estate Q9 (1.II.1), Q6 (under 1.III.8, also 1.II.1). Own questions cover the rest, including Q1-25F1 on the 2025 facts.

### 1.II.1 — What a title search shows

**QSQ-R9** · `1.II.1` · SQ Real Estate Q9 [Original], official key C · `pcp-m-1-7`

Your client is purchasing a resale private residential property. During the conveyancing process, your title search reveals that the property is subject to a registered mortgage in favour of a bank. Which of the following is the MOST APPROPRIATE advice?

A. The purchaser should immediately terminate the transaction because the seller is unable to convey good title.
B. The purchaser should insist that the mortgage be discharged before signing the sale and purchase agreement.
C. The purchaser's solicitor should ensure that arrangements are made for the mortgage to be redeemed and discharged on or before completion so that the purchaser obtains good title.
D. The purchaser will automatically assume liability for the seller's mortgage upon completion.

**Answer: C.** A title search tells you which encumbrances must be cleared at completion; a mortgage is normal and is redeemed and discharged at completion from the sale proceeds. A: a mortgage does not mean bad title. B: discharge before the contract is neither usual nor needed. D: the purchaser does not take over the seller's loan. Official key: C.
*Cite: RE2 s3–11; SQ p80 Q9, key p128; `pcp-m-1-7`*

**Q1-25F1** · `1.II.1` `1.III.6` · own question on PYP 2025 case facts · `pcp-m-1-7` `pcp-m-1-18`

[2025 facts.] Better Lim's solicitor's title search shows that Abel acquired #04-01 on 4 April 2023 by a transfer from Mdm Lim for no consideration. Why does this matter?

A. It does not; the source of the vendor's title is irrelevant under the Torrens system.
B. Under LSCS Condition 10.2 the vendor warrants that any undervalue transaction or gift in the title is more than 3 years old (5 years in some IRDA cases); this gift is only 2 years old, so the warranty cannot be given and the purchaser bears an insolvency clawback risk.
C. A gift transfer makes the title qualified, so common law investigation is required.
D. It means Abel must pay ABSD on the sale.

**Answer: B.** The instrument of transfer on the title search shows a price or a gift, and a gift raises an undervalue risk addressed by Condition 10.2. Here the gift is about two years old at the April 2025 sale, inside the 3-year period, and the sale itself is at a third of market value. The purchaser's solicitor should raise it. A is wrong for that reason. C: a caution as to title, not a gift, makes title qualified. D: ABSD is a buyer's duty.
*Cite: LSCS 2020 Condition 10.2; RE2 s3–11; `pcp-m-1-7`, `pcp-m-1-18`*

### 1.II.2 — Share value and collective sales

**Q1-7** · `1.II.2` · own question · `pcp-m-1-8`

A condominium completed 12 years ago is the subject of a collective sale. What consent is needed?

A. At least 90% by share value and by strata area.
B. At least 80% by share value and by strata area.
C. A simple majority of owners.
D. Unanimous consent.

**Answer: B.** For a development 10 years or older the threshold is 80% by share value and strata area; under 10 years it is 90% (s 84A LTSA). Share value also fixes maintenance contributions, voting weight and the split of sale proceeds. A applies to developments under 10 years. C and D are wrong.
*Cite: LTSA s 84A(1); RE2 s9; `pcp-m-1-8`*

### 1.II.3 — Lot Base and other searches

**Q1-8** · `1.II.3` · own question · `pcp-m-1-9`

Which search should the purchaser's solicitor update after the contract and before completion, where the vendor is an individual?

A. A winding-up search.
B. A bankruptcy search against the vendor.
C. A judicial management search.
D. No search; the title search at the option stage is enough.

**Answer: B.** On concluding the contract and before completion, update the bankruptcy search against individuals, winding-up and judicial management searches against companies, and the title search. A Lot Base search shows lot particulars and history (e.g. notices of acquisition). A and C are for companies. D is wrong.
*Cite: RE2 s10; RE3 s7; RE7 s12–14; `pcp-m-1-9`*

### 1.II.4 — Title deeds, solicitor's undertakings and documents of title

**Q1-9** · `1.II.4` · own question · `pcp-m-1-10`

Under the LSCS 2020, by when must the vendor provide the title documents for inspection?

A. On completion.
B. At least 1 month before the scheduled completion date.
C. Within 14 days of the option.
D. Only if the purchaser asks.

**Answer: B.** Condition 3.1: title documents (or copies) for inspection at least 1 month before the scheduled completion date; the purchaser has notice of them whether or not he inspects. Title deeds go to the purchaser's solicitor on an undertaking to return them on demand without lien, and a solicitor must honour that undertaking. A, C and D are wrong.
*Cite: LSCS 2020 Conditions 3.1–3.3; RE2 s12; `pcp-m-1-10`*

### 1.II.5 — Investigation of title: good root, indefeasible and qualified title

**Q1-10** · `1.II.5` · own question · `pcp-m-1-11`

Which of the following is a good root of title?

A. A will.
B. A voluntary conveyance.
C. A conveyance on sale.
D. A lease of freehold land.

**Answer: C.** A good root deals with the whole legal and equitable estate, describes the property identifiably and casts no doubt on the title: a conveyance on sale or a legal mortgage. A, B and D are bad roots. Under the Torrens system an indefeasible title is investigated from the current certificate of title only; a qualified title needs the earlier common law title.
*Cite: RE2 s13–17; Cyril-RE §3.3; `pcp-m-1-11`*

### 1.II.6 — Legal requisitions

**Q1-11** · `1.II.6` · own question · `pcp-m-1-12`

The LTA's reply to a legal requisition shows a road line affecting the property. The OTP lets the purchaser rescind if a reply is "unsatisfactory". How is "unsatisfactory" judged?

A. By the purchaser's own subjective view.
B. Objectively, by the standard of a reasonable purchaser.
C. By the vendor's solicitor.
D. By the LTA.

**Answer: B.** Whether a reply is unsatisfactory is judged objectively by a reasonable purchaser (*Soo Nam Thoong v Phang Song Hua*: an LTA reply was unsatisfactory and the standard proviso did not save the vendor). Define "unsatisfactory" clearly in the contract. A, C and D are wrong. For a strata unit a 10th requisition goes to the MCST (s 47(1)(c) BMSMA).
*Cite: Soo Nam Thoong v Phang Song Hua [2011] SGHC 159; BMSMA s 47(1)(c); RE2 s18–24; `pcp-m-1-12`*

### 1.III Option to purchase, contract terms, stakeholding and caveats

Sub-points 1.III.1–1.III.8. Real questions: SQ Real Estate Q3 (1.III.1), Q4 (1.III.2), Q10 (1.III.5), Q6 (1.III.8); 2021 REP Q1.3.1 (1.III.3). Own questions cover the rest.

### 1.III.1 — Granting and exercising an option to purchase

**SQ Real Estate facts for Qs 1–5.** You are a conveyancing lawyer at Justice LLP. Mr Gopal, a Singapore citizen who owns one commercial office unit at High Street Centre, instructs you on the sale of his condominium unit at 25 Maple Street #25-01 (the "Property"). His agent has already issued the original OTP to the purchaser, Mr Tan, a Singapore PR, on receiving the 1% option fee, keeping a photocopy, which Mr Gopal hands you. Mr Gopal used about S$80,000 of CPF to buy the Property in 2009 with a S$500,000 housing loan; the redemption figures are S$100,000 (CPF) and S$350,000 (bank). The OTP: price S$1,200,000; dated 1 April 2024, exercisable within 2 weeks of issue; LSCS 2020 applies, the OTP prevailing; sold "as-is"; vacant possession; exercised by delivering the signed Acceptance Copy with 4% to the vendor's solicitors (CVY) as stakeholders. [SQ p76–77, transcribed in brief.]

**QSQ-R3** · `1.III.1` · SQ Real Estate Q3 [Part B 2023-S], official key B · `pcp-m-1-13`

To exercise the option to purchase, the following must be done:-

A. Mr Tan must sign the portion marked "Acceptance Copy" on either the original or the copy of the Option to Purchase.
B. Mr Tan must sign the portion marked "Acceptance Copy" on the original of the Option to Purchase.
C. Mr Gopal must sign the portion marked "Acceptance Copy" on either the original or the copy of the Option to Purchase.
D. Mr Gopal must sign the portion marked "Acceptance Copy" on the original of the Option to Purchase.

**Answer: B.** The purchaser exercises by signing the Acceptance Copy on the original OTP and delivering it with the exercise money within the option period; acceptance must be unqualified. A: a photocopy will not do. C and D: the vendor grants the option; the purchaser accepts it. Official key: B.
*Cite: RE3 s4–5; RE4 s14–15; SQ p78 Q3, key p128; `pcp-m-1-13`*

### 1.III.2 — Option not exercised

**QSQ-R4** · `1.III.2` · SQ Real Estate Q4 [Part B 2023-S], official key B · `pcp-m-1-14`

[SQ facts above.] Mr Tan decides not to exercise the Option to Purchase. Which of the following statements is CORRECT?

A. Mr Tan must compensate Mr Gopal S$1,200,000.
B. Mr Tan will forfeit 1% of the sale price.
C. Mr Tan will forfeit 5% of the sale price.
D. He can get a refund of the 1% of the sale price that was paid to Mr Gopal.

**Answer: B.** Letting an option lapse is not a breach; the purchaser loses only the option fee (1%) and the vendor may sell elsewhere. A: no damages. C: 5% is the deposit after exercise. D: the option fee is forfeited, not refunded. Official key: B.
*Cite: RE3 s4; RE4 s15; SQ p78 Q4, key p128; `pcp-m-1-14`*

### 1.III.3 — OTP v sale and purchase agreement; vendor as trustee

**Q2021R-1-3-1** · `1.III.3` `1.III.1` · PYP 2021 REP Q1.3.1 (written); short model answer · `pcp-m-1-15` `pcp-m-1-13`

[Facts in brief.] Kenneth and Anni Chow were granted an OTP dated 30 August 2021 over 28 Moonshine Turn #08-01 by the vendors, expiring at 4pm on 13 September 2021. The OTP says it is exercised by signing the Acceptance Copy and delivering it to the vendors' solicitors with the exercise money of S$58,000, and that "This Option and the Acceptance Copy signed by the Purchaser shall constitute a binding contract". They signed the Acceptance Copy and you exercised it for them before expiry. When is the contract of sale constituted?

**Answer (short model answer).** Under an OTP the purchaser has a choice until exercise; the contract comes into being when the option is validly exercised, that is, when the purchasers sign the Acceptance Copy on the original OTP and deliver it, with the S$58,000 exercise money (making the deposit), to the vendors' solicitors before 4pm on 13 September 2021, in the manner the OTP requires. Acceptance must be unqualified and the payment must clear. From then both sides are bound, and the vendors hold the property as trustees for the purchasers until completion (so, e.g., they must consult them on an en bloc vote). Stamp duty runs from the date of exercise. Contrast an S&P agreement, which binds both parties as soon as it is signed.
*Cite: RE3 s4–7; RE4 s14–17, s28; `pcp-m-1-15`, `pcp-m-1-13`*

**Q1-12** · `1.III.3` · own question · `pcp-m-1-15`

After the option is exercised but before completion, the condominium's owners vote on a collective sale proposal. How should the vendor vote?

A. As he wishes; he is still the registered owner.
B. As the purchaser wishes, because the vendor now holds the property as trustee for the purchaser.
C. He may not vote at all.
D. Against the sale, to protect the purchaser.

**Answer: B.** Once the contract is concluded the vendor holds the property as trustee for the purchaser and must consult him, so on an en bloc proposal before completion he votes as the purchaser wishes. A, C and D are wrong.
*Cite: RE4 s28; Cyril-RE; `pcp-m-1-15`*

### 1.III.4 — Salient terms of the OTP or contract

**Q1-13** · `1.III.4` · own question · `pcp-m-1-16`

The OTP incorporates the LSCS 2020 and also states a completion period of 12 weeks. Condition X of the LSCS would give a different result on the same point. Which governs?

A. The LSCS, because it is a standard form.
B. The OTP's own term, because the contract's terms prevail over the Conditions where they conflict.
C. Whichever is more favourable to the purchaser.
D. Neither; the term is void for inconsistency.

**Answer: B.** The 17 Conditions apply only so far as the contract does not vary or conflict with them; most OTPs also say expressly that the option's terms prevail (as in the SQ, 2023 and 2025 facts). A, C and D are wrong. Other salient terms to check: address and parties against the title search, price and payment (1% / 4% / 95%), stakeholding, tenancy, completion period, legal requisitions, vacant possession.
*Cite: RE-CS1 s22–30; RE4 s18–25; `pcp-m-1-16`*

**Q1-25F2** · `1.III.4` · own question on PYP 2025 case facts · `pcp-m-1-16`

[2025 facts.] What is the total deposit Better Lim will have paid once he exercises the option, and how much is payable on completion before apportionments?

A. S$5,000 deposit; S$495,000 on completion.
B. S$25,000 deposit (5%); S$475,000 on completion.
C. S$20,000 deposit; S$480,000 on completion.
D. S$75,000 deposit (5% of market value); S$425,000 on completion.

**Answer: B.** The 1% option fee (S$5,000) plus the 4% exercise fee (S$20,000) make the 5% deposit of S$25,000, leaving 95% (S$475,000) on completion, subject to apportionments. A and C count only one payment. D: payments follow the contract price, not market value (market value matters for stamp duty).
*Cite: RE-CS1 s22–30; RE4 s18; `pcp-m-1-16`*

### 1.III.5 — Stakeholding of the option exercise monies

**QSQ-R10** · `1.III.5` · SQ Real Estate Q10 [Original], official key A · `pcp-m-1-17`

Your client, Michael, has exercised an Option to Purchase for a resale private residential property. Under the terms of the OTP, the option exercise monies are to be held by the seller's solicitors as stakeholders pending completion. One week before the scheduled completion date, the seller informs his solicitors that he requires the monies urgently to redeem an unrelated personal loan and instructs them to release the monies to him immediately. The purchaser has not consented to the release. Which of the following is the MOST APPROPRIATE advice?

A. The seller's solicitors should continue to hold the option exercise monies as stakeholders unless they are entitled to release the monies under the terms of the contract or with the purchaser's consent.
B. The seller's solicitors may release the monies to the seller provided that they are satisfied the monies will be used to facilitate completion of the transaction.
C. The seller's solicitors may release the monies if they first give reasonable notice to the purchaser and the purchaser does not object within a reasonable time.
D. The seller's solicitors may release the monies if the seller undertakes to repay the monies before the completion date should the transaction fail to complete.

**Answer: A.** A stakeholder holds for both parties and may release only as the contract allows or with the purchaser's consent; the vendor's need for money is no ground. B, C and D each invent a release mechanism that the contract and the purchaser have not agreed. Official key: A.
*Cite: RE-CS1 s24; RE4 s18; SQ p80 Q10, key p128; `pcp-m-1-17`*

### 1.III.6 — Law Society's Conditions of Sale 2020: key conditions

See also Q1-25F1 under 1.II.1 (Condition 10.2).

**Q1-14** · `1.III.6` · own question · `pcp-m-1-18`

Under the LSCS 2020, who bears the risk of damage to the property between the contract and completion, where the purchaser has not taken possession?

A. The purchaser, from the date of the contract, under s 3(13) CLPA.
B. The vendor, until completion or possession, whichever is earlier, because Condition 13 excludes s 3(13) CLPA.
C. The insurer, always.
D. Both equally.

**Answer: B.** Condition 13 excludes s 3(13) CLPA, so risk stays with the vendor until completion or the purchaser taking possession, whichever is earlier. A states the position the Condition displaces. C and D are wrong. Other key conditions: 5.1 property delivered in the same state as at the option or contract date; 6 vendor takes rents and bears outgoings to the scheduled completion date; 10.1 no unauthorised alterations.
*Cite: LSCS 2020 Conditions 5, 6, 10, 13; RE4 s19–21; `pcp-m-1-18`*

### 1.III.7 — "As is where is", entire agreement and non-merger clauses

**Q1-25F3** · `1.III.7` · own question on PYP 2025 case facts · `pcp-m-1-19`

[2025 facts.] Clause 12 of Abel's OTP says the contract's terms remain in force after completion and do not merge in the assurance. After completion, an authority reveals a fine for an unauthorised alteration made before the sale. What is the effect of clause 12?

A. None; all terms merge on completion.
B. It is unfavourable to the vendor: Abel's obligations (e.g. under the warranties and the authority-demand condition) survive completion, so he may still be liable.
C. It protects Abel against any later claim.
D. It entitles Better Lim to rescind the completed sale.

**Answer: B.** A non-merger clause keeps the contract's terms alive after completion and registration, which favours the purchaser; without it, notice coming after completion would not bind the vendor. A describes the position without the clause. C reverses it. D: the clause preserves contractual claims, not a right to unwind completion. The "as-is where-is" clause, by contrast, protects Abel: Better Lim buys with full notice of the property's state.
*Cite: RE3 s9; RE4 s24–27; `pcp-m-1-19`*

**Q1-15** · `1.III.7` · own question · `pcp-m-1-19`

What does an entire agreement clause in an OTP do?

A. It makes the purchaser buy with full notice of the property's condition.
B. It supersedes all earlier oral or written representations, protecting the vendor against erroneous verbal statements.
C. It keeps the contract's terms alive after completion.
D. It makes time of the essence.

**Answer: B.** An entire agreement clause supersedes earlier representations. A describes "as is where is". C describes a non-merger clause. D is a separate term.
*Cite: RE3 s9; RE4 s24–27; `pcp-m-1-19`*

### 1.III.8 — Caveats: when and why to lodge

**QSQ-R6** · `1.III.8` `1.II.1` · SQ Real Estate Q6 [Original], official key B · `pcp-m-1-20` `pcp-m-1-7`

Which of the following statements concerning caveats is/are CORRECT?

I. A purchaser may lodge a caveat after exercising an Option to Purchase in order to protect his interest in the property.
II. A caveat prevents the purchaser from completing the transaction.
III. A title search may reveal whether a caveat has been lodged against the property.

A. I only.
B. I and III.
C. II and III.
D. I, II and III.

**Answer: B.** I: the purchaser's solicitor lodges a caveat once the contract is concluded, to give notice of his interest and stop registration of conflicting dealings (s 115 LTA). III: caveats appear as encumbrances on a title search. II is wrong: a caveat protects the purchaser; it does not stop him completing. Official key: B.
*Cite: LTA ss 115, 121; RE3 s18; SQ p79 Q6, key p128; `pcp-m-1-20`, `pcp-m-1-7`*

### 1.IV Stamp duties: BSD, ABSD, SSD, remissions and penalties

Sub-points 1.IV.1–1.IV.8. Real questions: SQ Real Estate Q5 (1.IV.1), Q1 (1.IV.3, 1.IV.6); 2021 REP Q2.2 (1.IV.2, 1.IV.3, 1.IV.4, 1.IV.8). Own questions cover the rest. 2021 REP Q2.3 (whether selling an existing flat takes it out of the ABSD count before completion) is left out: IRAS's count list, which the pack follows, does not deal with property under contract to be sold, and the contrary note in Cyril's notes is unconfirmed, so it is not answered by guesswork.

### 1.IV.1 — When stamp duty is payable

**QSQ-R5** · `1.IV.1` · SQ Real Estate Q5 [Part B 2023-S], official key A · `pcp-m-1-21`

[SQ facts above.] When is the deadline for the payment of stamp duty on Mr Tan's purchase?

A. Within 14 days from the date of exercise of the Option to Purchase.
B. Within 14 days from the date of issuance of the Option to Purchase.
C. Within 14 days from the date of completion of the sale and purchase.
D. Within 7 days from the date of issuance of the Option to Purchase.

**Answer: A.** BSD and ABSD are payable within 14 days after the exercise of the OTP (or of the S&P agreement if there is no OTP; 30 days after receipt in Singapore if signed overseas). B and D: the grant of the option is not the contract. C: completion is too late. Official key: A.
*Cite: RE3 s12; IRAS "Stamp Duty Basics for Property"; SQ p78 Q5, key p128; `pcp-m-1-21`*

### 1.IV.2 — Buyer's Stamp Duty: rates and worked example

**Q2021R-2-2** · `1.IV.2` `1.IV.3` `1.IV.4` `1.IV.8` · PYP 2021 REP Q2.2 (written); short model answer on current rates · `pcp-m-1-22` `pcp-m-1-23` `pcp-m-1-24` `pcp-m-1-28`

[Facts in brief.] Jun-Ho Hwang, a Singapore PR holding South Korean citizenship, is buying a new condominium unit for S$1,500,000. He owns a 2-bedroom apartment in Singapore, which he lives in, co-owns a Korean BBQ shop in a Singapore mall, and owns a terrace house in Johor Bahru. Advise on the stamp duty payable and when, whether his other properties affect his ABSD rate, and what happens if the agreement is not stamped in time.

**Answer (short model answer, current rates).** *BSD* on S$1,500,000 (residential): 1,800 + 3,600 + 19,200 + 20,000 = **S$44,600** (shortcut 4% × price − 15,400). *ABSD:* the Rich Road apartment is a residential property in Singapore and counts; the shop is non-residential and the Johor house is outside Singapore, so neither counts. This is his second residential property and he is a PR, so ABSD is 30% (rates from 27 Apr 2023): **S$450,000**. South Korea is not one of the FTA remission countries. *When:* within 14 days after the contract is made (for a developer sale, the exercise of the option by signing the S&P agreement); 30 days after receipt if signed overseas. *Late stamping:* up to 3 months late, a penalty of the greater of $10 and the duty; more than 3 months, the greater of $25 and 4 times the duty; an unstamped document cannot be registered or relied on. *What changed:* the 2021 paper was set under the pre-2023 BSD and ABSD rates.
*Cite: IRAS BSD and ABSD pages (checked 10 Nov 2026); RE1 s9; RE3 s13; RE-CS1 s19; `pcp-m-1-22`, `pcp-m-1-23`, `pcp-m-1-24`, `pcp-m-1-28`*

**Q1-23F1** · `1.IV.2` · own question on PYP 2023 case facts · `pcp-m-1-22`

[2023 facts.] What BSD is payable on the Shams' purchase at S$3,800,000?

A. S$152,000.
B. S$167,600.
C. S$190,000.
D. S$228,000.

**Answer: B.** Residential BSD above S$3 million: 6% × price − S$60,400 = 228,000 − 60,400 = S$167,600 (1,800 + 3,600 + 19,200 + 20,000 + 75,000 + 48,000). A uses a flat 4%. C applies 5% throughout. D applies 6% throughout.
*Cite: IRAS BSD rates from 15 Feb 2023; RE3 s13; `pcp-m-1-22`*

### 1.IV.3 — Additional Buyer's Stamp Duty: rates

**QSQ-R1** · `1.IV.3` `1.IV.6` · SQ Real Estate Q1 [Part B 2023-S], official key D · `pcp-m-1-23` `pcp-m-1-26`

[SQ facts above.] Which of the following statements is CORRECT regarding the stamp duty payable for this transaction?

A. Mr Tan must pay Additional Buyer's Stamp Duty because Mr Gopal currently owns one commercial office unit at High Street Centre.
B. Mr Gopal must pay Additional Seller's Stamp Duty because Mr Gopal currently owns one commercial office unit at High Street Centre.
C. Mr Tan does not need to pay any Additional Buyer's Stamp Duty as he is a Singapore Permanent Resident.
D. Mr Gopal does not need to pay Seller's Stamp Duty as the Property was purchased by him in 2009 and the Property is sold in 2024.

**Answer: D.** SSD applies only if the seller disposes of residential property within the holding period (at most 4 years); Mr Gopal bought in 2009. A: ABSD depends on the buyer's profile and holdings, not the seller's, and a commercial unit does not count anyway. B: there is no "Additional Seller's Stamp Duty". C: a PR buying his first residential property pays 5% ABSD. Official key: D.
*Cite: IRAS ABSD and SSD pages (checked 10 Nov 2026); SQ p77 Q1, key p128; `pcp-m-1-23`, `pcp-m-1-26`*

**Q1-23F2** · `1.IV.3` `1.IV.5` · own question on PYP 2023 case facts · `pcp-m-1-23` `pcp-m-1-25`

[2023 facts.] What ABSD is payable on the Shams' joint purchase?

A. Nil, without more, because Mrs Sham is a citizen buying her first property.
B. 5% (the PR first-property rate) on the whole price, because for joint buyers the highest applicable rate applies; but as Mr Sham is a US national, he can apply for FTA remission to be treated as a citizen, bringing the rate to nil.
C. 30%, because Mr Sham owns a resort.
D. 60%, because Mr Sham is a foreigner.

**Answer: B.** For joint buyers the highest applicable rate applies to the whole price; Mr Sham is a PR buying his first residential property (the Maldives resort is outside Singapore and non-residential, so it does not count): 5%. US nationals get citizen treatment on application for remission under the FTA remission rules, so the 5% can be remitted. A ignores the highest-rate rule. C: the resort does not count. D: a PR is not charged as a foreigner for ABSD.
*Cite: IRAS ABSD page; Stamp Duties (Free Trade Agreements) (Remission) Rules; RE1 s9; `pcp-m-1-23`, `pcp-m-1-25`*

### 1.IV.4 — ABSD: which properties are counted

**Q1-16** · `1.IV.4` · own question · `pcp-m-1-24`

A Singapore citizen buying a condominium owns: a half share (as tenant in common) in an HDB shop with living quarters; an office unit; a flat in Kuala Lumpur. How many residential properties does she already own for ABSD?

A. None.
B. One.
C. Two.
D. Three.

**Answer: B.** The HDB shop with living quarters counts, and a partly owned property counts in full. The office unit is non-residential and outside ABSD; the KL flat is outside Singapore. So one property, and the condominium is her second (20% for a citizen).
*Cite: IRAS ABSD page, count items 1–8; RE1 s9; `pcp-m-1-24`*

### 1.IV.5 — ABSD remissions and anti-avoidance

**Q1-17** · `1.IV.5` · own question · `pcp-m-1-25`

A mother and son agree that the son will be registered with a 1% share of a condominium and the mother 99%, while the son already owns a flat, and they backdate the contract to avoid ABSD. Which is CORRECT?

A. The arrangement is lawful tax planning.
B. A backdated contract to avoid ABSD is void for illegality, and false statements to IRAS may be prosecuted.
C. Only the son can be liable.
D. ABSD is payable only on 1% of the price.

**Answer: B.** Contracts backdated to avoid ABSD are void for illegality (*Ochroid Trading v Chua Siok Lui*), and the CS1 slide reports the first prosecution of a "99-to-1" scheme (mother and son jailed for lying to IRAS). A, C, D: for joint buyers the highest profile applies to the whole price.
*Cite: Ochroid Trading v Chua Siok Lui [2018] SGCA 5; RE-CS1 s18, s20–21; `pcp-m-1-25`*

### 1.IV.6 — Seller's Stamp Duty

**Q1-25F4** · `1.IV.6` · own question on PYP 2025 case facts · `pcp-m-1-26`

[2025 facts.] Abel acquired #04-01 on 4 April 2023 and agrees on 8 April 2025 to sell it to Better for S$500,000 (market value S$1,500,000). What SSD is payable?

A. Nil; he held it for more than a year.
B. 4% of S$500,000 = S$20,000.
C. 4% of S$1,500,000 = S$60,000.
D. 8% of S$1,500,000 = S$120,000.

**Answer: C.** For residential property acquired between 11 Mar 2017 and 3 Jul 2025, SSD is 4% if sold after more than 2 and up to 3 years. Abel held it just over 2 years. SSD is charged on the higher of price and market value, so 4% × S$1,500,000. A ignores the 3-year period. B uses the price. D uses the rates for property acquired from 4 Jul 2025 (16/12/8/4% over 4 years). If he does not pay, the purchaser may deduct the SSD from the price and pay it (LSCS 7.4.2).
*Cite: IRAS SSD page (checked 10 Nov 2026); LSCS 2020 Condition 7.4; `pcp-m-1-26`*

**Q1-23F3** · `1.IV.6` · own question on PYP 2023 case facts · `pcp-m-1-26`

[2023 facts.] Miss Junko bought the unit about 4 years before the October 2023 sale. Is she liable for SSD?

A. Yes, 4%, because she is a foreigner.
B. No; for residential property acquired from 11 Mar 2017 to 3 Jul 2025 the holding period is 3 years, and she has held it longer.
C. Yes, 12%.
D. No, because SSD is paid by the buyer.

**Answer: B.** SSD depends on the holding period, not the seller's nationality; acquired in 2019, the 3-year period had ended. A and C are wrong. D: SSD is the seller's duty (though the purchaser may deduct and pay it under Condition 7.4.2 if the vendor defaults).
*Cite: IRAS SSD page; `pcp-m-1-26`*

### 1.IV.7 — Mixed-use property

**Q1-18** · `1.IV.7` · own question · `pcp-m-1-27`

A buyer purchases a shophouse whose ground floor is a shop and upper floors are residential. How is stamp duty charged?

A. All at residential rates, with ABSD on the whole.
B. All at non-residential rates, with no ABSD.
C. The value is apportioned: residential BSD rates and ABSD on the residential part, non-residential rates on the rest.
D. Only ABSD is payable.

**Answer: C.** For mixed-use property apportion the value: BSD at residential rates on the residential part and non-residential rates on the rest; ABSD on the residential part only; SSD by the parts' rates and holding period. A and B ignore apportionment. D is wrong.
*Cite: Cyril-RE §2.4; IRAS "Definition of residential property"; `pcp-m-1-27`*

### 1.IV.8 — Late or wrong stamping

**Q1-19** · `1.IV.8` · own question · `pcp-m-1-28`

BSD of S$30,000 is paid 5 months late. What is the maximum penalty?

A. S$10.
B. S$30,000.
C. S$120,000.
D. S$25.

**Answer: C.** More than 3 months late: the greater of $25 and 4 times the duty (4 × 30,000 = S$120,000). Up to 3 months late, the greater of $10 and the duty (S$30,000, option B). A and D are the floors only.
*Cite: RE-CS1 s19; IRAS "Late payment or non-payment of stamp duty"; `pcp-m-1-28`*

### 1.V Foreign ownership: Residential Property Act

Sub-points 1.V.1–1.V.3. Real question: SQ Real Estate Q2 (1.V.2). Own questions Q1-20, Q1-21.

### 1.V.1 — Who is a foreign person

**Q1-20** · `1.V.1` · own question · `pcp-m-1-29`

Which is a "foreign person" under the Residential Property Act?

A. A Singapore citizen living abroad.
B. A Singapore permanent resident.
C. A Singapore company.
D. A Singapore society.

**Answer: B.** A foreign person is anyone who is not a Singapore citizen, Singapore company, Singapore LLP or Singapore society (RPA s 2), so a PR is a foreign person. A, C and D are excluded from the definition.
*Cite: RPA s 2; RE1 s4, s6; `pcp-m-1-29`*

### 1.V.2 — Restricted residential property and LDAU approval

**QSQ-R2** · `1.V.2` · SQ Real Estate Q2 [Part B 2023-S], official key C · `pcp-m-1-30`

[SQ facts above.] If Mr Tan is a foreigner instead of a Singapore Permanent Resident, would he be permitted to purchase the Property? Choose the most appropriate answer.

A. No. Foreigners are not permitted to buy residential properties in Singapore.
B. No. Foreigners are only permitted to buy residential properties in Sentosa Cove.
C. Yes, this Property is a condominium unit.
D. No. Foreigners are only permitted to buy residential properties with another Singapore Citizen.

**Answer: C.** The RPA does not apply to a unit in an approved condominium development or a non-landed flat (s 4(1)), so a foreigner may buy it without approval (though he will pay ABSD at 60%). Landed and other restricted residential property needs LDAU approval. A, B and D misstate the Act. Official key: C.
*Cite: RPA ss 3–4; SQ p77 Q2, key p128; `pcp-m-1-30`*

### 1.V.3 — Foreigners and inheritance, joint tenancy, loss of PR

**Q1-21** · `1.V.3` · own question · `pcp-m-1-31`

A Singapore citizen dies owning a terrace house as sole owner and leaves it by will to her son, an Australian citizen. What must the executors do if no approval is obtained?

A. Transfer the house to the son.
B. Sell it to a citizen or approved purchaser within 5 years of death (or any extension) and pay the son the net proceeds.
C. Hold it on trust for the son indefinitely.
D. Transfer it to the State.

**Answer: B.** Residential property does not pass by will or intestacy to a foreign person (RPA s 3(3)); the PRs must sell within 5 years to a citizen or approved purchaser and pay the net proceeds to him (s 3(4)). A and C would breach s 3. D: the Controller may sell only if the PRs fail (ss 3(5)–(6)). The Act does not apply to a foreign surviving joint tenant (s 3(13)).
*Cite: RPA s 3(3)–(13); `pcp-m-1-31`*

### 1.VI Sale of a residential property: vendor's side, bank and CPF

Sub-points 1.VI.1–1.VI.5 (1.VI.5 non-examinable). No real question tests these directly (the SQ facts give the redemption figures); own questions Q1-22 to Q1-26.

### 1.VI.1 — Vendor's considerations in setting the price

**Q1-22** · `1.VI.1` · own question · `pcp-m-1-32`

[SQ facts above.] Mr Gopal used S$80,000 of CPF in 2009, but CPF's redemption figure is S$100,000. Why?

A. CPF charges a penalty for early sale.
B. The CPF refund is the capital withdrawn plus the accrued interest it would have earned.
C. The figure includes the bank's lock-in penalty.
D. It includes SSD.

**Answer: B.** The vendor must refund the CPF capital withdrawn for the purchase plus the accrued interest it would have earned. He must also meet the bank's redemption amount (with any lock-in penalty), SSD if within the holding period, legal fees and commission. A, C, D misattribute the difference.
*Cite: RE4 s4; `pcp-m-1-32`*

### 1.VI.2 — Shortfall: bank v CPF priority, worked example

**Q1-23** · `1.VI.2` · own question · `pcp-m-1-33`

A flat bought in 2010 is sold for S$800,000. The bank's outstanding loan is S$500,000 plus a S$5,000 redemption penalty; the CPF refund due is S$400,000. Who is paid what, and what must the vendor find (ignoring SSD and fees)?

A. CPF S$400,000; bank S$400,000; vendor finds S$105,000.
B. Bank S$500,000; CPF S$300,000 (vendor loses S$100,000 of CPF); vendor finds the S$5,000 penalty.
C. Bank S$505,000; CPF S$295,000.
D. Bank and CPF share pro rata.

**Answer: B.** For properties bought on or after 1 Sep 2002 the bank has first claim, but only for the outstanding loan and interest, not penalties; CPF is refunded from what remains. A applies the old CPF-first rule. C wrongly gives the penalty priority. D is wrong.
*Cite: RE4 s5–10; `pcp-m-1-33`*

### 1.VI.3 — CPF Board's requirements before completion

**Q1-24** · `1.VI.3` · own question · `pcp-m-1-34`

Which of the following does CPF Board require before completion of a sale of a property charged to it?

A. The purchaser's income tax assessment.
B. A valuation report, the bank's redemption statements and the vendor's confirmation that he is not a relative of the purchaser.
C. The agent's commission invoice.
D. The purchaser's CPF statement.

**Answer: B.** CPF Board wants a valuation report comparing price and valuation, the bank's initial and final redemption statements (to see penalties), and the vendor's confirmation that he is not related to the purchaser. The 2025 facts (Abel selling to his brother at a third of value) are the kind of sale these checks catch. A, C, D are not required.
*Cite: RE4 s7; `pcp-m-1-34`*

### 1.VI.4 — The solicitors involved and their duties

**Q1-25** · `1.VI.4` · own question · `pcp-m-1-35`

By when must the vendor's solicitor send the completion account and mode of payment to the purchaser's solicitor?

A. On the completion date.
B. At least 7 business days before completion.
C. At least 1 month before completion.
D. Within 14 days of the option.

**Answer: B.** The vendor's solicitor sends the completion account and mode of payment at least 7 business days before completion (if late, Condition 9.6 relieves the purchaser of late interest for the shortfall). The vendor's solicitor also serves redemption notices, gets the SSD paid within 14 days, takes the title deed on undertaking, and after completion e-files the Notice of Transfer with IRAS. A, C, D are wrong.
*Cite: RE4 s29–41; LSCS 2020 Condition 9.6; `pcp-m-1-35`*

### 1.VI.5 — Buying from a developer: progress payments and defects liability (non-examinable)

**Q1-26** · `1.VI.5` · own question (non-examinable Sub-point; for context only) · `pcp-m-1-36`

Under the prescribed Form 5 S&P for an uncompleted property, how long is the defects liability period?

A. 3 months from TOP.
B. 12 months from vacant possession (or the 15th day after the TOP or CSC notice, if earlier).
C. 5 years from completion.
D. There is none.

**Answer: B.** The defects liability period is 12 months from vacant possession, or the 15th day after notice of TOP or CSC if earlier; the developer has 1 month to rectify after notice, then 14 more days, after which the buyer may rectify and recover the cost. The Learning Plan marks this non-examinable.
*Cite: RE-LP Schedule 1 A(vi)–(vii); Cyril-RE §1.6.1–1.6.3; `pcp-m-1-36`*

### 1.VII Mortgages and CPF

Sub-points 1.VII.1–1.VII.5. Real question: SQ Real Estate Q7 (1.VII.5). Own questions cover the rest.

### 1.VII.1 — Financing and parties to a mortgage

**Q1-27** · `1.VII.1` · own question · `pcp-m-1-37`

In an "indirect mortgage", which is CORRECT?

A. The mortgagor and the borrower are the same person.
B. The mortgagor (who gives the security) and the borrower (who takes the loan) are different persons.
C. There is no mortgagee.
D. CPF Board is the mortgagee.

**Answer: B.** In a direct mortgage the mortgagor and borrower are the same; in an indirect mortgage they differ. For residential purchase loans, MAS Notice 632 para 25 bars a bank from lending to a borrower who is not a mortgagor of the property. A describes a direct mortgage. C and D are wrong: the bank is the mortgagee; CPF Board holds a statutory charge.
*Cite: RE5 s3–5; MAS Notice 632 paras 25–26; `pcp-m-1-37`*

### 1.VII.2 — Mortgage process and security documents

**Q2021R-2-4-2** · `1.VII.2` · PYP 2021 REP Q2.4.2 (written); short model answer · `pcp-m-1-38`

[Facts in brief.] Jun-Ho is buying an uncompleted condominium unit from a developer with an S$800,000 loan from Pandora Bank. He asks why his loan must be secured by a Deed of Assignment and a Mortgage-in-escrow. Explain the security arrangement for properties under construction.

**Answer (short model answer).** Before completion no title has issued in his name, so he cannot yet give a registered mortgage. The bank therefore takes (1) a Deed of Assignment of his rights and interest under the S&P agreement with the developer, as present security, and (2) a Mortgage-in-escrow, signed now but held in escrow and registered as a legal mortgage over the unit once title issues and the transfer to him is registered. The bank's solicitors also lodge a caveat to protect the bank's interest meanwhile.
*Cite: RE5 s6–12, s21; Cyril-RE §1.7.1–1.7.2; `pcp-m-1-38`*

**Q1-28** · `1.VII.2` · own question · `pcp-m-1-38`

Where a mortgage is "all monies", which document usually contains the detailed further covenants, incorporated by reference and registered?

A. The letter of offer.
B. The memorandum of mortgage.
C. The OTP.
D. The CPF letter of approval.

**Answer: B.** The memorandum of mortgage holds the further covenants, incorporated by reference and registered. A: the letter of offer sets loan type, rates, repayment, prepayment penalties and conditions precedent; the bank's printed standard terms apply unless it negates them. C and D are unrelated.
*Cite: RE5 s6–12; `pcp-m-1-38`*

### 1.VII.3 — Registered mortgages; equity of redemption; company borrowers

**Q1-29** · `1.VII.3` · own question · `pcp-m-1-39`

A company borrower mortgages its office unit to a bank. Within what time must the charge be registered with ACRA?

A. 14 days of creation.
B. 30 days of creation, or it is void against the liquidator and creditors.
C. 3 months of creation.
D. No ACRA registration is needed for land.

**Answer: B.** s 131 Companies Act: file a statement of the charge with ACRA within 30 days of creation, or it is void against the liquidator and creditors. Also check the constitution and obtain directors' resolutions. An LTA mortgage takes effect as security, not a transfer (s 68(3) LTA), and the mortgagor has an equity of redemption (s 77). A, C, D are wrong.
*Cite: Companies Act s 131(1); LTA ss 68(3), 77; RE5 s13–14; `pcp-m-1-39`*

### 1.VII.4 — Using CPF monies for a purchase

**Q1-30** · `1.VII.4` · own question · `pcp-m-1-40`

Which statement about using CPF for a property purchase is CORRECT?

A. CPF may be used to buy a commercial shop unit.
B. CPF may be used only for residential property, capped by the valuation and withdrawal limits.
C. CPF is paid directly to the purchaser.
D. No application is needed before completion.

**Answer: B.** CPF can be used only for residential property, within the valuation and withdrawal limits; the member authorises his solicitor to apply online about 6–8 weeks before completion; CPF Board issues a letter of approval and pays by cashier's order from its solicitor's conveyancing account. A, C, D are wrong. (So in the 2023 facts the Shams may use CPF for the condominium.)
*Cite: RE5 s15; RE1 s8; `pcp-m-1-40`*

### 1.VII.5 — CPF Board's statutory charge and priorities

**QSQ-R7** · `1.VII.5` `1.VII.4` · SQ Real Estate Q7 [Original], official key C · `pcp-m-1-41` `pcp-m-1-40`

Your client intends to finance the purchase of a residential property using both a bank loan and CPF monies. Which of the following statements is MOST ACCURATE?

A. Once CPF monies are used to finance the purchase, no mortgage may be created over the property.
B. A mortgage and the CPF Board's statutory charge cannot co-exist over the same property.
C. The purchaser may finance the purchase using both a bank loan and CPF monies, subject to the applicable legal requirements and the creation of the relevant security interests.
D. CPF monies may only be used after the bank loan has been fully repaid.

**Answer: C.** Using CPF creates a statutory charge for CPF Board (s 21B CPF Act), which co-exists with the bank's mortgage, the priorities being set by the Letter of Confirmation of Priority Arrangements and Memorandum IA/991901M. A, B and D are wrong for that reason. Official key: C.
*Cite: CPF Act s 21B; RE5 s16–20; SQ p79 Q7, key p128; `pcp-m-1-41`, `pcp-m-1-40`*

**Q1-31** · `1.VII.5` · own question · `pcp-m-1-41`

Under Memorandum IA/991901M, where the proceeds of a forced sale cannot pay both the bank and CPF Board in full, what is paid first after the costs of sale?

A. CPF Board's principal withdrawn up to 100% of the Ascribed Value.
B. The bank's loan principal and interest unpaid as at the Date of Default.
C. CPF accrued interest.
D. Other facilities owed to the bank.

**Answer: B.** Clause 8.1: first the bank's First Outstandings (principal and interest unpaid at the Date of Default); second CPF Board's First Outstandings (CPF used for stamp duty, fees and legal costs, plus principal up to 100% of the Ascribed Value); third, pro rata, the Board's Second Outstandings and the bank's balance of interest; fourth, other costs pro rata; fifth, other moneys owed to the bank. A is second, C third, D fifth.
*Cite: Memorandum IA/991901M cl 8.1; RE5 s16–20; `pcp-m-1-41`*

### 1.VIII Completion accounts and conveyancing money

Sub-points 1.VIII.1–1.VIII.6. No real question (2021 REP Q1.4 needs the annexures); own questions Q1-32 to Q1-37, using the RE6 worked figures.

### 1.VIII.1 — Completion accounts: definition and types

**Q1-32** · `1.VIII.1` · own question · `pcp-m-1-42`

Which completion account is rendered by the purchaser's solicitors to the purchaser?

A. Type 1: the amount the purchaser pays the vendor.
B. Type 2: the vendor's net sale proceeds.
C. Type 3: the cash the purchaser must find.
D. None; the purchaser's solicitors render no account.

**Answer: C.** Type 1 goes from the vendor's solicitors to the purchaser's solicitors (amount payable on completion, *Frans Furniture*); Type 2 from the vendor's solicitors to the vendor; Type 3 from the purchaser's solicitors to the purchaser. A and B are rendered by the vendor's solicitors.
*Cite: Frans Furniture v Good Property Land Development; RE6 s3–4; `pcp-m-1-42`*

### 1.VIII.2 — Apportioning outgoings and rent

**Q1-33** · `1.VIII.2` · own question · `pcp-m-1-43`

Completion is on 18 August. The vendor has received rent of S$3,100 for August. Under the LSCS, how much rent is credited to the purchaser?

A. S$1,700.
B. S$1,300.
C. S$3,100.
D. Nil.

**Answer: B.** The vendor takes rents down to and including the scheduled completion date (Condition 6), so 19–31 August (13 days) belongs to the purchaser: 3,100 ÷ 31 × 13 = S$1,300, deducted in the purchaser's favour. A gives the vendor's portion. C and D ignore apportionment. Prepaid outgoings beyond completion are, conversely, added back to the vendor.
*Cite: LSCS 2020 Conditions 6.1–6.2, 7.1; RE6 s5–10; `pcp-m-1-43`*

### 1.VIII.3 — Type 1 account: due from purchaser to vendor (worked)

**Q1-34** · `1.VIII.3` · own question · `pcp-m-1-44`

Price S$1,000,000; 1% option money and 4% stakeholder money paid; rental deposit S$2,000 transferred to the purchaser; rent for the days after completion S$838.71; prepaid property tax refund S$883.87; prepaid maintenance refund S$212.90. What is due from the purchaser to the vendor in the Type 1 account?

A. S$950,000.00.
B. S$948,258.06.
C. S$988,258.06.
D. S$947,161.29.

**Answer: B.** 1,000,000 − 10,000 − 40,000 − 2,000 − 838.71 = 947,161.29; add 883.87 + 212.90 = S$948,258.06. The stakeholder money is deducted because it is already with the vendor's solicitors. A ignores apportionments. C fails to deduct the stakeholder money. D stops before adding the refunds.
*Cite: RE6 s5–11; `pcp-m-1-44`*

### 1.VIII.4 — Type 2 (vendor's net proceeds) and Type 3 (purchaser's cash) accounts (worked)

**Q1-35** · `1.VIII.4` · own question · `pcp-m-1-45`

Using the Type 1 total of S$948,258.06: the purchaser is funding it with S$200,000 CPF and a S$650,000 bank loan, and pays S$3,500 legal fees (no subsidy). How much cash must the purchaser find (Type 3)?

A. S$98,258.06.
B. S$101,758.06.
C. S$94,758.06.
D. S$148,258.06.

**Answer: B.** 948,258.06 + 3,500 − 200,000 − 650,000 = S$101,758.06. A is the RE6 figure, which also deducted a S$3,500 legal subsidy (a practice that ended in late 2012). C subtracts the fees. D ignores the CPF.
*Cite: RE6 s12–17; `pcp-m-1-45`*

### 1.VIII.5 — How the money flows on completion

**Q1-36** · `1.VIII.5` · own question · `pcp-m-1-46`

How are payments made out of a solicitor's conveyancing account on completion?

A. By the solicitor's personal cheque.
B. By a Payout Form on the ePI system (STARS eLodgment), verified and countersigned by the other side's solicitor where required, with the bank issuing cashier's orders.
C. By cash at the completion meeting.
D. By the vendor withdrawing directly.

**Answer: B.** Each funding source is paid in the vendor's prescribed mode; payments out of a conveyancing account go through Payout Form BC (or A) on the ePI system, with countersigning where required, and the bank issues the cashier's orders. A, C, D are wrong.
*Cite: RE6 s18–23; CLP(C)R 2011; `pcp-m-1-46`*

### 1.VIII.6 — Category A, B and C payees; letters of authority

**Q1-37** · `1.VIII.6` · own question · `pcp-m-1-47`

[2025 facts.] Abel asks that the 2% commission be paid from the completion money directly to his agent, Black Lotus Pte Ltd. What kind of payee is the agent, and what is needed?

A. Category A; no countersigning.
B. Category B; countersigning only.
C. Category C; Form BC with countersigning to verify identity and amount, and usually a letter of authority from the vendor.
D. The agent cannot be paid from a conveyancing account.

**Answer: C.** Category A payees are bodies such as the Commissioner of Stamp Duties, CPF Board and HDB (Form A, no countersigning); Category B are the parties, existing mortgagees, the MCST and similar (Form BC, countersigned to verify the payee); anyone else, such as an estate agent, is Category C (Form BC, countersigned for identity and amount, usually with a letter of authority for the third-party payment). A, B, D are wrong.
*Cite: CLP(C)R 2011 r 2; `pcp-m-1-47`*

### 1.IX Completion process and late completion

Sub-points 1.IX.1–1.IX.5. Real questions: SQ Real Estate Q8 (1.IX.5, 1.IX.3); 2021 REP Q1.5 (1.IX.3, 1.IX.5). Own questions cover the rest.

### 1.IX.1 — Legal completion: meaning, attendees, venue

**Q1-38** · `1.IX.1` · own question · `pcp-m-1-48`

The vendor's property is mortgaged and charged to CPF; the purchaser uses CPF and a bank loan. Where does completion take place, absent agreement?

A. The purchaser's solicitors' office.
B. The office of the solicitors for the discharging CPF chargee.
C. The SLA.
D. The purchaser's bank.

**Answer: B.** Venue priority: (1) the discharging CPF chargee's solicitors; else (2) the discharging mortgagee's solicitors; else (3) the vendor's solicitors. Up to six solicitors may attend. A, C, D are wrong. (In the 2025 facts, with no CPF or mortgage to discharge, the OTP fixes the vendor's lawyers, consistent with step 3.)
*Cite: RE7 s3–6; RE-CS1 s27; `pcp-m-1-48`*

### 1.IX.2 — Completion steps and post-completion

**Q1-39** · `1.IX.2` · own question · `pcp-m-1-49`

Who usually stamps the new mortgage and registers the transfer, discharges, new CPF charge and mortgage at the SLA after completion?

A. The vendor's solicitors.
B. The solicitors for the charging CPF Board (the purchaser's side).
C. The purchaser personally.
D. The discharging bank's solicitors.

**Answer: B.** At completion the originals go to the charging CPF Board's solicitors, who stamp the mortgage and register everything at the SLA. The vendor's solicitors e-file the Notice of Transfer and write to the tenant; the discharging bank's solicitors deliver the cashier's order by 10am the next working day. A, C, D are wrong.
*Cite: RE7 s7–25; Cyril-RE §1.8; `pcp-m-1-49`*

### 1.IX.3 — Late completion interest (Conditions 9.1–9.3), worked

**Q1-40** · `1.IX.3` · own question · `pcp-m-1-50`

Price S$1,000,000; 5% deposit paid. Completion is 3 days late solely through the purchaser's default. What late completion interest does the purchaser pay under the LSCS 2020?

A. S$657.53.
B. S$624.66.
C. S$246.58.
D. Nil.

**Answer: B.** Purchaser in default (Condition 9.1): 8% a year on the price less the deposit, from the day after the scheduled date to actual completion: 950,000 × 8% × 3/365 = S$624.66. A is the vendor-default figure on the full price (Condition 9.2). C uses 3%. D is wrong.
*Cite: LSCS 2020 Conditions 9.1–9.3; `pcp-m-1-50`*

### 1.IX.4 — When no late completion interest is payable (Conditions 9.4–9.7)

**Q1-41** · `1.IX.4` · own question · `pcp-m-1-51`

The vendor dies a week before the scheduled completion date, and completion is delayed while his executors obtain probate. Is late completion interest payable?

A. Yes, at 8% from the scheduled date.
B. No, for a reasonable period of up to 3 months to obtain a grant (Condition 9.5).
C. No, ever; the contract ends on death.
D. Yes, but at half the rate.

**Answer: B.** Condition 9.5: if a party dies or loses capacity before the scheduled date, completion may be put off for a reasonable time, not more than 3 months, to get a grant or deputyship, with no interest for that period. Also no interest if the delay is due to neither or both (9.4), the mode of payment came late (9.6), or the EPI system was down over 4 hours (9.7). A, C, D are wrong.
*Cite: LSCS 2020 Conditions 9.4–9.7; `pcp-m-1-51`*

### 1.IX.5 — Notice to complete (Condition 15)

**QSQ-R8** · `1.IX.5` `1.IX.3` · SQ Real Estate Q8 [Original], official key B · `pcp-m-1-52` `pcp-m-1-50`

Which of the following statements concerning late completion under the Law Society's Conditions of Sale 2020 is/are CORRECT?

I. A party who fails to complete on the contractual completion date may become liable for late completion interest.
II. A notice to complete may be served following a failure to complete on the contractual completion date.
III. Failure to complete on time automatically brings the contract to an end.

A. I only.
B. I and II.
C. II and III.
D. I, II and III.

**Answer: B.** I: Condition 9 interest. II: either party may serve a notice to complete after the scheduled date (Condition 15). III is wrong: unless time is of the essence, late completion does not end the contract; a notice to complete makes time of the essence, with 21 days to complete. Official key: B.
*Cite: LSCS 2020 Conditions 9, 15; SQ p79 Q8, key p128; `pcp-m-1-52`, `pcp-m-1-50`*

**Q2021R-1-5** · `1.IX.5` `1.IX.3` `1.IX.4` · PYP 2021 REP Q1.5 (written); short model answer · `pcp-m-1-52` `pcp-m-1-50` `pcp-m-1-51`

[Facts in brief.] Kenneth and Anni Chow (purchasers, cash purchase) hear the vendor may not complete on the scheduled date. Advise on their remedies if the vendor is late or unable to complete (LSCS 2020 applies).

**Answer (short model answer).** *Late completion interest:* if completion is late solely through the vendor's default, the vendor pays interest as liquidated damages at 8% a year on the purchase price, from the day after the scheduled date to actual completion (Condition 9.2), reduced by a notional rent if the purchasers already have rent-free vacant possession (9.3); none if the delay is due to neither or both, or the vendor dies or loses capacity before the date (up to 3 months), or the mode of payment or EPI exceptions apply (9.4–9.7). *Notice to complete:* failing to complete on the date does not end the contract; once ready, able and willing, the purchasers may serve a notice to complete at any time after the scheduled date (15.3–15.6). The parties must then complete within 21 days after service, and time becomes of the essence (15.7). *If the vendor still fails:* the purchasers may either enforce their rights (specific performance and damages) or demand the deposit back with damages, but taking the refund gives up specific performance (15.11–15.12). They should also protect themselves with a caveat.
*Cite: LSCS 2020 Conditions 9.2–9.7, 15; `pcp-m-1-52`, `pcp-m-1-50`, `pcp-m-1-51`*

## 2 · Muslim Family & Succession Law

### 2.I Applicability of Muslim law and AMLA

Sub-points 2.I.1–2.I.3. No real question tests these directly (SQ Muslim Q6 under 2.II.4 touches 2.I.2); own questions Q2-1 to Q2-3.

### 2.I.1 — AMLA and its institutions

**Q2-1** · `2.I.1` · own question · `pcp-m-2-1`

Which statement about the Administration of Muslim Law Act is CORRECT?

A. It is a complete code of substantive Muslim law.
B. It regulates Muslim religious institutions and sets up MUIS, the Syariah Court and the Registry of Muslim Marriages.
C. It replaced the Women's Charter for all Muslims.
D. It came into force in 1957.

**Answer: B.** AMLA (enacted 1966, in force 1968) is not a codified set of substantive Muslim law; it regulates Muslim institutions and establishes MUIS, the SYC and ROMM. A is wrong. C: only specified WC Parts are excluded. D: 1957 is the Muslim Ordinance that first set up the Syariah Court.
*Cite: MU1 s5–8; `pcp-m-2-1`*

### 2.I.2 — Who is a Muslim; laws excluded for Muslims

**Q2-2** · `2.I.2` · own question · `pcp-m-2-2`

Which law does NOT apply to the estate of a Muslim who dies intestate domiciled in Singapore?

A. The Probate and Administration Act.
B. The Intestate Succession Act.
C. The CPF Act (nominations).
D. The Wills Act formalities.

**Answer: B.** The ISA does not apply to any Muslim's estate (ISA s 2); faraid applies. The IFPA also does not apply. A: the PAA grant process applies. C: CPF nominations apply. D: Wills Act formalities apply to Muslim wills. A "Muslim" is one who professes Islam (s 2 AMLA).
*Cite: ISA s 2; AMLA s 2; MU1 s9; MU3 s6; `pcp-m-2-2`*

### 2.I.3 — Civil laws that apply to Muslims

**Q2-3** · `2.I.3` · own question · `pcp-m-2-3`

A Muslim wife, married under Muslim law and not divorcing, needs maintenance for herself and a personal protection order against her husband. Where does she go?

A. The Syariah Court for both.
B. The Family Justice Courts for both, under the Women's Charter (s 69 maintenance; PPO).
C. The Syariah Court for maintenance and the FJC for the PPO.
D. Neither; Muslims are outside the Women's Charter.

**Answer: B.** WC maintenance of a wife during marriage (s 69) and of children, and PPOs, apply to Muslims, with or without SYC proceedings; the SYC's s 51(1) power is not used in practice. What does not apply is WC divorce and post-divorce wife maintenance (s 113). A, C and D are wrong.
*Cite: MU1 s10; MU-CS1 s5–6; `pcp-m-2-3`*

### 2.II Jurisdiction of the Syariah Court

Sub-points 2.II.1–2.II.6. Real questions: SQ Muslim Q6 (2.II.4, 2.II.2), Q8 (2.II.5, 2.II.6), Q2 (2.II.6, 2.II.5), Q4 (2.II.6, 2.VI.1). Own questions cover the rest.

### 2.II.1 — Subject-matter jurisdiction (s 35(2) AMLA)

**Q2-4** · `2.II.1` · own question · `pcp-m-2-4`

Which dispute is within the Syariah Court's jurisdiction under s 35(2) AMLA, where both parties are Muslims married under Muslim law?

A. A claim by the wife's employer for unpaid salary.
B. A dispute over emas kahwin and mutaah on divorce.
C. A claim under the IFPA.
D. A claim against a third-party co-owner of the matrimonial flat.

**Answer: B.** s 35(2) covers marriage, the four divorces, betrothal or nullity, children on divorce, property on divorce, and emas kahwin, hantaran belanja, maintenance and mutaah. A is not family. C: the IFPA does not apply to Muslims. D: the SYC cannot decide third parties' rights (*DA v DC*).
*Cite: AMLA s 35(2); ER v ES (2021) 8 SSAR 389; `pcp-m-2-4`*

### 2.II.2 — Personal jurisdiction: Muslims married under Muslim law

**Q2-5** · `2.II.2` · own question · `pcp-m-2-5`

A couple married at the ROM as non-Muslims. Both later converted and also married under Muslim law at ROMM. Which court can dissolve the marriage, and with what effect?

A. Only the FJC, because the first marriage was civil.
B. The SYC, and its decree dissolves the whole marriage, the civil marriage included.
C. The parties may choose the FJC or the SYC.
D. Both courts must each grant a divorce.

**Answer: B.** Where parties married civilly and later under Muslim law, an SYC decree dissolves the whole marriage (*Noor Azizan bte Colony v Tan Lip Chin*; *BO v BP*). A and D are wrong. C: a ROMM marriage can be dissolved only at the SYC. Note a valid Muslim marriage is needed in practice (*Yeo Pei Chern*).
*Cite: Noor Azizan [2006] 3 SLR(R) 707; BO v BP [2015] 7 SSAR 19; MU1 s16–24; `pcp-m-2-5`*

### 2.II.3 — Essentials of a valid Muslim marriage

**Q2-6** · `2.II.3` · own question · `pcp-m-2-6`

Which is NOT one of the five essential elements of a valid Muslim marriage?

A. A wali (the bride's guardian).
B. Two Muslim male witnesses.
C. Offer and acceptance.
D. Solemnisation in a mosque.

**Answer: D.** The five elements are a male party, a female party, a wali, two Muslim male witnesses, and offer and acceptance; location does not matter (*Yeo Pei Chern* at [30]). Registration alone neither validates nor invalidates (s 109 AMLA).
*Cite: AMLA s 109; Yeo Pei Chern v Seow Zheng Xin (2007) 4 SSAR 146; MU2 s8–10; `pcp-m-2-6`*

### 2.II.4 — Territorial jurisdiction: domicile or 3 years' habitual residence

**QSQ-M6** · `2.II.4` `2.II.2` · SQ Muslim Q6 [Part B 2024], official key D · `pcp-m-2-7` `pcp-m-2-5`

Which of the following statements is CORRECT?

A. The Singapore Syariah Court is available to any Singapore citizen, regardless of religion, to obtain a divorce.
B. If a marriage is registered with the Singapore Registry of Muslim Marriages, the parties may elect to have their divorce heard either in the Family Justice Courts or the Singapore Syariah Court.
C. A Singaporean Muslim man who is married to a non-Muslim woman in a foreign country may obtain a divorce in the Singapore Syariah Court if his wife consents.
D. A foreign Muslim who was married under Muslim law may commence divorce proceedings in the Singapore Syariah Court if he has been habitually resident in Singapore for a continuous period of at least three years.

**Answer: D.** The SYC has jurisdiction if either party is domiciled in Singapore or habitually resident here for at least 3 years immediately before the action (s 35(3)). A: the parties must be Muslims or married under Muslim law. B: a ROMM marriage is dissolved only at the SYC. C: consent cannot create jurisdiction; there is no Muslim marriage. Official key: D.
*Cite: AMLA s 35(2)–(3), (5); SQ p68 Q6, key p128; `pcp-m-2-7`, `pcp-m-2-5`*

### 2.II.5 — Parties already divorced overseas

**QSQ-M8** · `2.II.5` `2.II.6` `2.IV.3` · SQ Muslim Q8 [Part B 2024], official key A · `pcp-m-2-8` `pcp-m-2-9` `pcp-m-2-16`

In which of the following situations would the Singapore Syariah Court have jurisdiction?

A. An application by a Muslim wife to register a divorce where the husband has already pronounced the talak.
B. An application by a Muslim man seeking permission to marry a second wife.
C. An application by a Muslim wife for a divorce where the parties have already been divorced by a Syariah Court in Malaysia.
D. An application by a Muslim woman against her former husband for spousal maintenance, where their divorce was registered in the Syariah Court six years earlier.

**Answer: A.** A talak pronounced outside court is valid only once registered by the SYC on either party's application (ss 46, 46B). B: a second marriage is solemnised by a Kadi or with a Kadi's consent (s 96), not adjudicated under s 35(2). C: after a recognised overseas divorce the SYC has no jurisdiction over the divorce (*ED v EE*). D: a former wife divorced years ago has no spousal maintenance claim at the SYC (her post-divorce claims were nafkah iddah and mutaah). Official key: A.
*Cite: AMLA ss 35(2), 46B, 96; ED v EE (2021) 8 SSAR 292; SQ p69 Q8, key p128; `pcp-m-2-8`, `pcp-m-2-9`, `pcp-m-2-16`*

**Q2-7** · `2.II.5` · own question · `pcp-m-2-8`

A Muslim couple were divorced by a competent court in Indonesia. The wife, now in Singapore, wants orders on the children and the Singapore flat. Where should she go?

A. The SYC, for a fresh divorce and ancillaries.
B. The SYC for the children and flat.
C. The civil courts: financial relief after an overseas divorce (WC s 121B) and children under the GIA; the SYC can deal only with nafkah iddah and mutaah.
D. Nowhere; the overseas divorce bars all claims.

**Answer: C.** Once there is a recognised overseas divorce, the SYC can deal only with nafkah iddah and mutaah (*ED v EE*; *TMO v TMP*); children and assets go to the civil courts under their residual jurisdiction (WC s 121B; *UJM v UJL*). A, B and D are wrong.
*Cite: WC s 121B; TMO v TMP [2017] 1 SLR 585; UJM v UJL [2021] 2 SLR 1467; `pcp-m-2-8`*

### 2.II.6 — What the Syariah Court cannot do

**QSQ-M2** · `2.II.6` `2.II.5` · SQ Muslim Q2 [Part B 2023-S], official key D · `pcp-m-2-9` `pcp-m-2-8`

In which of the following situations will the Syariah Court of Singapore be able to adjudicate?

I. An application by a Muslim wife for maintenance against her non-Muslim husband
II. An application by a Muslim man to marry a second wife
III. An application by a Muslim wife for a divorce when the parties have already been divorced at the Syariah Court in Johore, Malaysia.

A. I only.
B. II only.
C. III only.
D. None of the options.

**Answer: D.** I: no personal jurisdiction over a non-Muslim husband (not a Muslim marriage). II: polygamous marriages are handled by a Kadi under s 96, not adjudicated by the SYC under s 35(2). III: the parties are already divorced by a competent court. Official key: D.
*Cite: AMLA ss 35(2), 96(2)–(3); SQ p67 Q2, key p128; `pcp-m-2-9`, `pcp-m-2-8`*

**QSQ-M4** · `2.II.6` `2.VI.1` `2.II.5` · SQ Muslim Q4 [Part B 2023-S], official key B · `pcp-m-2-9` `pcp-m-2-29` `pcp-m-2-8`

Which of the following statements is CORRECT?

A. The Syariah Court can grant a Mareva injunction as it has the inherent jurisdiction to do so.
B. The Syariah Court cannot grant a Mareva injunction as it does not have a specific power to do so.
C. To enforce an order of the Syariah Court for nafkah iddah and mutaah at the Family Justice Court, a commencement certificate is required from the Syariah Court.
D. The Syariah Court can adjudicate on the matrimonial assets in Singapore even if parties have already been divorced in a foreign court.

**Answer: B.** The SYC is a creature of statute with no inherent jurisdiction, and has no specific power to grant a Mareva injunction. A is wrong for that reason. C: nafkah iddah and mutaah orders are enforced at the FJC as WC maintenance orders (s 53(1)) with no SYC certificate. D: after a foreign divorce, assets go to the civil courts. Official key: B.
*Cite: AMLA s 53(1); ER v ES (2021) 8 SSAR 389; SQ p68 Q4, key p128; `pcp-m-2-9`, `pcp-m-2-29`, `pcp-m-2-8`*

### 2.III Concurrent and residual jurisdiction with the civil courts; finality

Sub-points 2.III.1–2.III.4. No real question; own questions Q2-8 to Q2-11.

### 2.III.1 — Concurrent jurisdiction: leave to commence or continue

**Q2-8** · `2.III.1` · own question · `pcp-m-2-10`

A Muslim husband's custody application under the Guardianship of Infants Act is pending in the FJC when the wife files for divorce at the SYC. What does the husband need to carry on with the FJC case?

A. Nothing; the two cases run independently.
B. The SYC's leave to continue (s 35A(2) AMLA; s 17A(3)(b) SCJA).
C. The FJC's leave.
D. The wife's written consent only, with no counselling.

**Answer: B.** Civil proceedings on children already running when SYC divorce proceedings begin need SYC leave to continue; proceedings started after need SYC leave to commence (s 35A(1)). Children and assets cannot be heard in both forums at once. A is true only of PPO and maintenance proceedings. C is wrong. D: continuing by consent needs counselling and a certificate (s 35A(5)–(7)).
*Cite: AMLA s 35A; SCJA s 17A(3); MU1 s29–35; `pcp-m-2-10`*

### 2.III.2 — Leave from the SYC: the balancing test; continuing by consent

**Q2-9** · `2.III.2` · own question · `pcp-m-2-11`

Which factor is NOT among those the SYC weighs on an application for leave to proceed in the civil courts?

A. Whether leave allows more expedient resolution.
B. Whether it avoids or causes duplicated proceedings.
C. Whether it affects the children's welfare.
D. Which court would award the applicant more.

**Answer: D.** The SYC balances the parties' legitimate interests: expediency, duplication, undue prejudice or undermining Syariah tenets, and the children's welfare (*AK v AL*; *BU v BV*). Forum shopping for a better award is not a factor.
*Cite: AK v AL [2012] 6 SSAR 184; BU v BV [2018] 7 SSAR 64; `pcp-m-2-11`*

### 2.III.3 — Residual jurisdiction of the civil courts

**Q2-10** · `2.III.3` · own question · `pcp-m-2-12`

Where there is no SYC divorce application, which court decides custody of the children of a Muslim couple who have separated?

A. The SYC.
B. The civil courts (FJC), under their residual jurisdiction (GIA).
C. MUIS.
D. No court; custody follows Muslim law automatically.

**Answer: B.** Where there is no specific exclusion and no SYC divorce, the civil courts have residual jurisdiction (*TMO v TMP*); children issues go to the FJC under the GIA, without SYC leave. A: the SYC makes ancillary orders only with a divorce before it. C and D are wrong.
*Cite: TMO v TMP [2017] SGCA 14; SCJA ss 16–17; `pcp-m-2-12`*

### 2.III.4 — Finality of SYC and Appeal Board decisions (s 56A)

**Q2-11** · `2.III.4` · own question · `pcp-m-2-13`

A husband dissatisfied with a decision of the MUIS Appeal Board wants to challenge it. Which is CORRECT?

A. He may appeal to the Court of Appeal.
B. He may seek a quashing order in the High Court as of right.
C. The decision is final and cannot be challenged, appealed, reviewed or quashed in any court (s 56A).
D. He may appeal to the President of the SYC.

**Answer: C.** s 56A AMLA makes SYC and Appeal Board decisions final; judicial review was dismissed in *Mohamed Yusoff* and permission refused in *Qureshi Mohamed Aslam v MUIS* [2026] SGCA 19. A, B and D are wrong (D: the President hears appeals from the Registrar, below the Board).
*Cite: AMLA s 56A; Mohamed Yusoff [2010] 3 SLR 481; Qureshi [2026] SGCA 19; `pcp-m-2-13`*

### 2.IV Divorce at the Syariah Court: types, grounds, process

Sub-points 2.IV.1–2.IV.8. Real questions: SQ Muslim Q1 (2.IV.2), Q7 (2.IV.7), Q8 (under 2.II.5, also 2.IV.3). Own questions cover the rest.

### 2.IV.1 — FJC v SYC divorce process

**Q2-12** · `2.IV.1` · own question · `pcp-m-2-14`

How does the SYC divorce process differ from the FJC process?

A. The SYC grants an interim judgment first, then hears ancillaries separately.
B. The SYC is not bifurcated: the decree and the ancillary orders are made at the same hearing, and the divorce certificate issues 3 months after the divorce date.
C. The SYC has no appeal.
D. The SYC requires 3 years' separation.

**Answer: B.** The FJC is bifurcated (interim judgment, then ancillaries); the SYC makes the decree and ancillary orders together, and the certificate issues at the end of the wife's iddah (3 months). C: appeal lies within 30 days. D is wrong.
*Cite: MU2 s12–14; MU-CS1 s17; `pcp-m-2-14`*

### 2.IV.2 — Grounds of divorce: WC v AMLA

**QSQ-M1** · `2.IV.2` · SQ Muslim Q1 [Part B 2023-S], official key D · `pcp-m-2-15`

Which of the following statements is CORRECT?

A. In Singapore, only a Muslim male can file for divorce under AMLA.
B. In Singapore, a person who married under the Women's Charter as a non-Muslim but subsequently converted to Islam, can only be divorced at the Singapore Syariah Court.
C. In Singapore, the only way for a Muslim woman to obtain a divorce at the Syariah Court is if the Husband agrees to pronounce the Talak (divorce).
D. In Singapore, a married Muslim woman can still obtain a divorce at the Syariah Court even if the Husband refuses to pronounce the Talak (divorce).

**Answer: D.** The wife may apply for cerai taklik (s 48), fasakh (s 49) or khuluk (s 47(4)), and hakam can pronounce talak for a refusing husband (s 50). A and C are wrong for the same reason. B: a civil marriage of converts who did not also marry under Muslim law is not within the SYC's jurisdiction in practice (a valid Muslim marriage is needed). Official key: D.
*Cite: AMLA ss 47–50; SQ p67 Q1, key p128; `pcp-m-2-15`*

### 2.IV.3 — Talak

**Q2-13** · `2.IV.3` · own question · `pcp-m-2-16`

A husband pronounces a first talak at home. Which is CORRECT?

A. The divorce is effective immediately without registration.
B. It is valid only once registered by the SYC; as a first talak it is revocable by rujuk within 3 months.
C. The parties can never remarry.
D. The wife must prove fault.

**Answer: B.** A talak pronounced outside court is valid only once registered by the SYC (ss 46, 46B). A first or second talak is revocable by reconciliation (rujuk) within 3 months. C applies to a third talak. D: talak needs no fault.
*Cite: AMLA ss 46, 46B; BQ v BR [2016] 7 SSAR 36; MU2 s21; `pcp-m-2-16`*

**Q2-39** · `2.IV.3` · own question · `pcp-m-2-16`

A wife applies to the Syariah Court to register a talak she says her husband pronounced at home. The husband denies saying the words. What does the Syariah Court do?

A. Registers the divorce on the wife's affidavit alone.
B. Dismisses the application, because only the husband can apply to register a talak.
C. Gets the husband's account of what he said and when, hears the evidence of the parties and witnesses, and decides whether the words used were certain and unequivocal.
D. Refers the dispute to the Family Justice Courts.

**Answer: C.** On a disputed talak the SYC confirms with the husband what was said and when, hears the parties and witnesses (*Mohamed Salleh v Habibah*; *AM v AN*), and decides whether the words were unequivocal (*BQ v BR*). A: there must be a finding on the evidence. B: either party may apply to register (ss 46, 46B AMLA). D: talak is within the SYC's exclusive jurisdiction.
*Cite: MU2 s21; AMLA ss 46, 46B; `pcp-m-2-16`*

### 2.IV.4 — Cerai taklik

**Q2-14** · `2.IV.4` · own question · `pcp-m-2-17`

Under the standard ROMM taklik, which breach lets the wife seek cerai taklik?

A. The husband leaves her for 2 months.
B. The husband fails to maintain her for more than 4 months while she is obedient.
C. The husband takes a second wife with a Kadi's consent.
D. The husband changes jobs.

**Answer: B.** The standard taklik: he leaves her for 4 months or more continuously; fails to maintain her for more than 4 months while obedient; or injures her, damages her property or causes loss of self-respect (s 48). A is too short. C and D are not taklik breaches. Some foreign certificates have no taklik, so the ground is unavailable.
*Cite: AMLA s 48; MU2 s24–26; `pcp-m-2-17`*

### 2.IV.5 — Fasakh (s 49)

**Q2-15** · `2.IV.5` · own question · `pcp-m-2-18`

Which is a ground for fasakh under s 49(1) AMLA?

A. The husband has failed to maintain the wife for 3 months.
B. The husband has been sentenced to 1 year's imprisonment.
C. The husband has failed to perform marital obligations for 6 months.
D. The couple have separated for 2 years by mutual agreement.

**Answer: A.** s 49(1)(a): failure to maintain for 3 months. B: the sentence must be 3 years or more and final. C: the period is 1 year without reasonable cause. D: not a s 49 ground. Other grounds include impotence, insanity or injurious disease, cruelty in its listed forms, and any ground valid in Muslim law.
*Cite: AMLA s 49(1); MU2 s28–29; `pcp-m-2-18`*

### 2.IV.6 — Khuluk (divorce by redemption)

**Q2-16** · `2.IV.6` · own question · `pcp-m-2-19`

Which statement about khuluk is CORRECT?

A. The husband pays the wife a sum to redeem the marriage.
B. The wife pays a sum assessed by the SYC; the divorce is irrevocable, and she gets no nafkah iddah.
C. The parties may remarry each other after rujuk.
D. It requires proof of cruelty.

**Answer: B.** In khuluk the SYC assesses the wife's payment by the parties' status and means and has the husband pronounce the divorce (s 47(4)); it is irrevocable and the wife gets no nafkah iddah. A reverses the payment. C: no remarriage. D: no fault needed.
*Cite: AMLA s 47(4); MU2 s31; MU-CS1 s23; `pcp-m-2-19`*

### 2.IV.7 — Hakam (marriage conciliators)

**QSQ-M7** · `2.IV.7` · SQ Muslim Q7 [Part B 2024], official key D · `pcp-m-2-20`

If a wife commences divorce proceedings and the husband refuses to pronounce the talak, what is the practice in the Syariah Court?

A. The Syariah Court will decline to hear the matter until the husband agrees to pronounce the talak.
B. The Syariah Court will order the wife to withdraw her application for divorce.
C. The Syariah Court will direct the wife to commence divorce proceedings in the Family Justice Courts instead.
D. The Syariah Court may direct, or obtain the parties' consent, for the matter to proceed to a Hakam session, where the Hakam is empowered to pronounce the talak on behalf of the husband.

**Answer: D.** If the husband refuses talak, hakam may be appointed whatever the ground (s 50(1)); with full authority they may pronounce the divorce (*AW v AX*). A and B: the SYC does not dismiss her application because he refuses. C: the FJC has no jurisdiction over a Muslim divorce. Official key: D.
*Cite: AMLA s 50; AW v AX [2013] 6 SSAR 309; SQ p69 Q7, key p128; `pcp-m-2-20`*

### 2.IV.8 — SYC structure, appeals and representation

**Q2-17** · `2.IV.8` · own question · `pcp-m-2-21`

A party wants to appeal the President's final order in a divorce. Where and when?

A. To the High Court within 14 days.
B. To the MUIS Appeal Board within 30 days.
C. To the President within 14 days.
D. No appeal lies.

**Answer: B.** From the President's final order, notice of appeal within 30 days to the three-member Appeal Board (s 55(1); r 39 MMDR); appealing a consent order needs the Board's leave. C is the route from a Registrar's direction (14 days, no further appeal). A: civil courts cannot review (s 56A). Lawyers appearing need not be Muslim (*Jamal Mahammath*).
*Cite: AMLA ss 39, 55; MMDR rr 38–39; MU2 s4–5; `pcp-m-2-21`*

### 2.V Ancillary orders: nafkah iddah, mutaah, children and matrimonial assets

Sub-points 2.V.1–2.V.7. Real questions: SQ Muslim Q5, Q10 (2.V.5), Q3 (2.V.7, 2.V.6). Own questions cover the rest.

### 2.V.1 — Orders the SYC makes on divorce (s 52(3))

**Q2-18** · `2.V.1` · own question · `pcp-m-2-22`

Which order can the SYC make under s 52(3) AMLA on a divorce?

A. Maintenance for a child aged 25.
B. Payment of emas kahwin and hantaran belanja to the wife.
C. An order binding the wife's mother as co-owner.
D. A personal protection order.

**Answer: B.** s 52(3): (a) emas kahwin and hantaran belanja; (b) mutaah; (c) custody, maintenance and education of minor children; (d) division of property. A: in practice no orders for children over 21. C: no orders against third parties. D: PPOs are made by the FJC.
*Cite: AMLA s 52(3); MU1 s40–41; `pcp-m-2-22`*

### 2.V.2 — Wife's maintenance during marriage

**Q2-19** · `2.V.2` · own question · `pcp-m-2-23`

A husband pronounced talak in January; the SYC issues the divorce certificate in June. He stopped paying the wife's FJC maintenance order in January. Which is CORRECT?

A. He was not liable after the talak.
B. He remained liable until the certificate issued, since until then she was a "married woman" under WC s 69; arrears can still be claimed.
C. The maintenance order continues for life.
D. The SYC enforces the maintenance order.

**Answer: B.** A husband who has pronounced talak must still pay until the SYC issues the divorce certificate (*Chaytor Alan James v Zaleha Rahman*); the WC order then lapses, but arrears remain claimable. A and C are wrong. D: the FJC enforces.
*Cite: WC s 69; Chaytor Alan James [2001] 1 SLR(R) 504; MU1 s42–43; `pcp-m-2-23`*

### 2.V.3 — Nafkah iddah

**Q2-20** · `2.V.3` · own question · `pcp-m-2-24`

In which case is a divorced wife NOT entitled to nafkah iddah?

A. Divorce by the husband's first talak.
B. Divorce by cerai taklik.
C. Divorce by khuluk.
D. Divorce by fasakh on failure to maintain.

**Answer: C.** Nafkah iddah is payable except where the divorce is by hakam pronouncement, by khuluk, or a third talak (MU-CS1 s23). Quantum turns on the husband's means, standing, lodging and cost of living (norm $500–$1,500 a month for incomes below $7,000).
*Cite: AMLA ss 35(2)(e), 51; MU2 s34; MU-CS1 s23–24; `pcp-m-2-24`*

### 2.V.4 — Mutaah

**Q2-21** · `2.V.4` · own question · `pcp-m-2-25`

A wife who started the divorce and was found to have behaved badly claims mutaah. Which is CORRECT?

A. She is not entitled because she started the divorce.
B. She is entitled; mutaah does not depend on her conduct, and is assessed on the husband's means at divorce and the length of the marriage.
C. Mutaah is a fixed sum of $5,000.
D. Mutaah is not payable if the husband has left Islam.

**Answer: B.** Mutaah is an entitlement, not dependent on conduct (*CQ v CR*), payable even if the wife started the divorce, and computed as a daily rate × days from marriage to divorce, considering the husband's means at the time of divorce. D: still payable (*Daud Salim v Hayati*). A and C are wrong.
*Cite: AMLA s 52(3)(b); CQ v CR [2019] 7 SSAR 210; Daud Salim (2003) 3 SSAR 124; `pcp-m-2-25`*

### 2.V.5 — Children: custody, care and control, access

**QSQ-M5** · `2.V.5` · SQ Muslim Q5 [Part B 2023-S], official key B · `pcp-m-2-26`

Which of the following statements is CORRECT?

A. At the Syariah Court, the mother will automatically lose all rights to the custody of the child if she has committed adultery.
B. The Syariah Court cannot make an order giving grandparents custody, care and control of the child of the marriage.
C. At the Syariah Court, children have no say at all on custody, care and control matters.
D. At the Syariah Court, the principle that the 'welfare of the infant is of paramount consideration' is overridden by the singular factor of which parent is deemed to be more religious.

**Answer: B.** s 52(3)(c) covers only the married couple, so the SYC cannot give custody to grandparents or other third parties (*DA v DC*). A: adultery does not automatically cost custody (*AE v AF*). C: children above 7 of sufficient maturity are usually interviewed. D: welfare is paramount; spiritual welfare is one factor (*AY v AZ*). Official key: B.
*Cite: AMLA s 52(3)(c); DA v DC [2020] 8 SSAR 72; SQ p68 Q5, key p128; `pcp-m-2-26`*

**QSQ-M10** · `2.V.5` · SQ Muslim Q10 [Part B 2024], official key B · `pcp-m-2-26`

Which of the following statements is CORRECT?

A. In proceedings before the Syariah Court, a mother automatically loses all rights to custody of her child if she remarries.
B. In proceedings before the Syariah Court, a child of the marriage may be interviewed if he or she is above seven years of age and is of sufficient maturity to express a view.
C. The Syariah Court cannot make an order for joint custody of a child because such an order is inconsistent with Islamic principles.
D. In proceedings before the Syariah Court, a mother automatically loses all rights to custody, care and control of her child if she earns less than the father, who has greater financial means.

**Answer: B.** Children above 7 (mumaiyiz) of sufficient maturity are usually interviewed by the President with a child expert; their wishes do not override welfare (*AA v AB*). A: remarriage affects care and control only through welfare. C: joint custody is the norm (*Zaini bin Ibrahim*). D: income is not decisive. Official key: B.
*Cite: AA v AB [2011] 6 SSAR 120; Zaini bin Ibrahim [2007] 3 SSAR 135; SQ p70 Q10, key p128; `pcp-m-2-26`*

**Q2-40** · `2.V.5` · own question · `pcp-m-2-26`

Which statement about interviewing children in custody disputes is CORRECT?

A. Neither the Syariah Court nor the civil courts interview children.
B. The Syariah Court usually interviews children above 7 who are mature enough, while the civil courts are more cautious and interview a child only where the child wishes to speak to the judge, is mature enough, and an interview would not drag the child into the dispute.
C. The civil courts interview every child above 7; the Syariah Court never does.
D. Once interviewed, a child's stated wishes decide care and control in both courts.

**Answer: B.** The SYC has a long-standing practice of interviewing children above 7 (mumaiyiz), now done by the President with a CAPS child expert. The civil courts note the risks (judges untrained, no relationship of trust, intimidation, coaching) but may interview in suitable cases (*AZB v AZC*). D: wishes never override welfare (*AA v AB*).
*Cite: MU2 s41, s46; AZB v AZC [2016] SGHCF 1; AA v AB [2011] 6 SSAR 120; `pcp-m-2-26`*

### 2.V.6 — Division of matrimonial assets

**Q2-22** · `2.V.6` · own question · `pcp-m-2-27`

In dividing matrimonial assets in a dual-income marriage, which approach does the SYC apply?

A. Strict faraid shares.
B. The *ANJ v ANK* structured approach, as the civil courts do, giving weight to direct and indirect contributions.
C. Equal division always.
D. The husband keeps all assets in his name.

**Answer: B.** The SYC divides in just and equitable proportions (s 52(7)), guided by the s 52(8) factors, and applies *ANJ v ANK* for dual-income marriages (*CY v CZ*; *DZ v EA*), *TNL v TNK* for single-income ones, or broad brush. A, C, D are wrong. There is no power to divide without a divorce before it.
*Cite: AMLA s 52(7)–(8), (14); ANJ v ANK [2015] 4 SLR 1043; MU2 s52–58; `pcp-m-2-27`*

### 2.V.7 — Third-party claims to matrimonial assets

**QSQ-M3** · `2.V.7` `2.V.6` · SQ Muslim Q3 [Part B 2023-S], official key C · `pcp-m-2-28` `pcp-m-2-27`

Which of the following statements is CORRECT?

A. If the total value of the matrimonial assets exceeds $5million, the Syariah Court will automatically transfer the issue of the matrimonial assets to the High Court.
B. The Syariah Court does not take into account the indirect contributions of a homemaker in determining the division of matrimonial assets.
C. The Syariah Court has no power to make an order against a third party (e.g. Wife's mother) who is a co-owner of the house that the parties reside at.
D. The Syariah Court can make any order on the matrimonial property or CPF, regardless of the HDB and CPF regulations.

**Answer: C.** AMLA gives the SYC no power to decide the rights of anyone but husband and wife (*DA v DC*; *Safie bin Jantan v Zaiton bte Adom*). A: no automatic transfer. B: indirect contributions count (*ANJ v ANK* applied). D: other laws still govern dealings with HDB property and CPF. Official key: C.
*Cite: DA v DC [2020] 8 SSAR 72; Safie bin Jantan [2023] SGHC(A) 8; SQ p68 Q3, key p128; `pcp-m-2-28`, `pcp-m-2-27`*

### 2.VI Enforcement of SYC orders

Sub-points 2.VI.1–2.VI.2. Real questions: SQ Muslim Q9 (2.VI.1, 2.VI.2); Q4 (under 2.II.6).

### 2.VI.1 — Enforcing nafkah iddah and mutaah (s 53(1))

**QSQ-M9** · `2.VI.1` `2.VI.2` · SQ Muslim Q9 [Part B 2024], official key D · `pcp-m-2-29` `pcp-m-2-30`

Which of the following statements is CORRECT?

A. A Muslim wife may enforce a spousal maintenance order made by either the Family Justice Courts or the Syariah Court in either court.
B. The Syariah Court may sentence a husband, who refuses to allow his wife access to their children, to imprisonment.
C. The parties may choose whether to apply to the Family Justice Courts or the Syariah Court for a variation of an order for mutaah.
D. Orders for mutaah and nafkah iddah made by the Syariah Court are enforced through the Family Justice Courts, where they are treated in the same manner as maintenance orders made by the Family Justice Courts.

**Answer: D.** s 53(1) AMLA treats nafkah iddah and mutaah orders as WC maintenance orders, enforced at the FJC. A: the SYC does not enforce financial orders. B: the SYC cannot imprison; access orders are enforced at the FJC (BOSCO, committal, ECAO). C: the key marks this wrong. Official key: D.
*Cite: AMLA s 53(1)–(2); SQ p70 Q9, key p128; `pcp-m-2-29`, `pcp-m-2-30`*

### 2.VI.2 — Enforcing other SYC orders (s 53(2), s 53A)

**Q2-23** · `2.VI.2` · own question · `pcp-m-2-30`

The SYC ordered the matrimonial flat sold. The husband refuses to sign the sale documents. What can the SYC itself do?

A. Commit him to prison.
B. Sign the transfer or sale documents in his place (s 53A).
C. Fine him.
D. Nothing; only the FJC may act.

**Answer: B.** The SYC's only enforcement power is to sign transfer or sale documents when a party, given the chance, is absent, neglects or refuses (s 53A). Other SYC orders are deemed civil court orders and enforced at the FJC (BOSCO complaints, committal, ECAO since 2 Jan 2025) (s 53(2)). A and C are not SYC powers. D ignores s 53A.
*Cite: AMLA ss 53(2), 53A; WC s 126B; VFU v VFV [2020] SGHCF 3; `pcp-m-2-30`*

### 2.VII Muslim law of inheritance (faraid)

Sub-points 2.VII.1–2.VII.5. No real question; own questions Q2-24 to Q2-28. (Share calculations are not examinable: MU3 s3.)

### 2.VII.1 — When Muslim inheritance law applies; statutes table

**Q2-24** · `2.VII.1` · own question · `pcp-m-2-31`

A Malay Muslim domiciled in Singapore dies intestate. Which is CORRECT?

A. His estate is distributed under the ISA.
B. His estate is distributed by Muslim law as modified by Malay custom, and the court may divide harta sepencarian as it thinks fit.
C. His adopted child inherits automatically.
D. His dependants may claim under the IFPA.

**Answer: B.** s 112(1)–(3) AMLA: Muslim law (modified by Malay custom where applicable); the court may divide harta sepencarian for a Malay intestate. A: no ISA. C: adopted children do not inherit automatically. D: no IFPA for Muslims.
*Cite: AMLA s 112; MU3 s6, s9–10; `pcp-m-2-31`*

### 2.VII.2 — Faraid: the basics

**Q2-25** · `2.VII.2` · own question · `pcp-m-2-32`

Which statement about faraid is CORRECT?

A. Females do not inherit.
B. As a general rule a daughter takes half a son's share, and heirs may by consensus redistribute their shares, usually by a deed of family arrangement.
C. Faraid applies before debts and funeral expenses are paid.
D. Faraid shares can never be varied.

**Answer: B.** Faraid fixes Quranic shares of the estate left after funeral expenses, debts and valid bequests; spouses, females and parents inherit; a daughter generally takes half a son's share; heirs may renounce and redistribute by consensus (MUIS Fatwa Committee). A, C, D are wrong.
*Cite: MU3 s3, s11–18; MU-CS1 s29; `pcp-m-2-32`*

### 2.VII.3 — School of law (mazhab)

**Q2-26** · `2.VII.3` · own question · `pcp-m-2-33`

What must a probate or administration affidavit for a Muslim estate state about the school of law?

A. Nothing.
B. The school (mazhab) the deceased professed, which the Inheritance Certificate follows.
C. The school of the applicant.
D. That the Shafii school applies in all cases.

**Answer: B.** The affidavit must state the mazhab the deceased professed (s 113 AMLA), and the Inheritance Certificate follows the deceased's school at death. D: the Fatwa Committee ordinarily follows Shafii (s 33) but others may apply. A dispute is resolved on documents and best evidence (*Fauziyah Mohd Ahbidin v MUIS* [2026] SGHC 104).
*Cite: AMLA ss 33, 113; MU3 s14–15; `pcp-m-2-33`*

### 2.VII.4 — Baitulmal

**Q2-27** · `2.VII.4` · own question · `pcp-m-2-34`

When does the Baitulmal take a share of a Muslim estate?

A. In every estate.
B. Where there is no rightful heir, or no male beneficiaries; heirs may appeal to MUIS on hardship.
C. Only where the deceased was Hanafi.
D. Only if the will says so.

**Answer: B.** The Baitulmal (General Endowment Fund, s 57), administered by MUIS, takes a share where there is no rightful heir (e.g. a convert leaving only non-Muslim heirs) or no male beneficiaries; heirs may appeal for its return on hardship. C: it does not apply where the deceased was Hanafi. D: a will cannot simply exclude its share.
*Cite: AMLA s 57; MU3 s20, s26; `pcp-m-2-34`*

### 2.VII.5 — Grants for Muslim estates: Inheritance Certificate first

**Q2-28** · `2.VII.5` · own question · `pcp-m-2-35`

A Muslim dies leaving a will and an estate worth S$2 million. What must the family obtain before applying for a grant, and from which court is the grant issued?

A. Nothing; apply to the SYC for probate.
B. An Inheritance Certificate from the SYC; the grant is issued by the Family Courts.
C. An Inheritance Certificate only if there is no will; the grant is issued by the SYC.
D. A fatwa from MUIS; the grant is issued by the High Court.

**Answer: B.** All grants for Muslim estates are issued by the FJC (or the High Court if over $5 million), never the SYC. An Inheritance Certificate from the SYC (s 115 AMLA) is needed first, even if there is a will or deed of family arrangement. A, C, D are wrong.
*Cite: AMLA s 115; MU3 s28–29; `pcp-m-2-35`*

### 2.VIII Muslim wills

Sub-points 2.VIII.1–2.VIII.4. No real question; own questions Q2-29 to Q2-32.

### 2.VIII.1 — The one-third rule (s 111)

**Q2-29** · `2.VIII.1` · own question · `pcp-m-2-36`

A Muslim domiciled in Singapore makes a will leaving his whole estate to his wife. His other heirs do not consent. Which is CORRECT?

A. The will is fully effective.
B. The will is ineffective beyond what Muslim law allows: he may bequeath at most one-third, and not to a faraid heir, without all heirs' consent.
C. The wife takes two-thirds.
D. The will is void for want of formality.

**Answer: B.** s 111(1) AMLA: no disposition by will except as his school allows; no more than one-third, and none of it to a faraid heir, unless all heirs consent (*Mohamed Ismail bin Ibrahim*). The wife, a faraid heir, takes her faraid share. A, C, D are wrong.
*Cite: AMLA s 111; Mohamed Ismail bin Ibrahim [2004] 4 SLR(R) 756 at [31]; `pcp-m-2-36`*

### 2.VIII.2 — Who may take under the one-third

**Q2-30** · `2.VIII.2` · own question · `pcp-m-2-37`

A Muslim convert wants to provide by will for his non-Muslim mother. Which is CORRECT?

A. He cannot; recipients must be Muslims.
B. He may leave her up to one-third, since she is not a faraid heir (a non-Muslim does not inherit by faraid).
C. He may leave her his whole estate.
D. He may only do so by CPF nomination.

**Answer: B.** Without the heirs' consent, the one-third must go to non-faraid beneficiaries such as adopted children, step-relations, a child born out of wedlock or unrelated parties, and recipients need not be Muslims, so a convert can provide for non-Muslim family this way. A and C are wrong. D is another route but not the only one.
*Cite: MU3 s23, s26; MU-CS1 s35; `pcp-m-2-37`*

### 2.VIII.3 — Formalities of Muslim wills

**Q2-31** · `2.VIII.3` · own question · `pcp-m-2-38`

Which Wills Act provision does NOT apply to a Muslim's will?

A. s 3 (freedom to dispose of all property by will).
B. s 6 (writing and execution before two witnesses).
C. s 10 (beneficiary-witness loses the gift).
D. s 4 (minimum age 21).

**Answer: A.** s 3 WA does not apply to Muslims (s 111 AMLA restricts disposition), but the formalities do: ss 4, 6, 10, 13, 16 and 28. The Wills Act sets no religion or gender for witnesses, though two Muslim men are often used in practice.
*Cite: AMLA s 111(2)(a); WA ss 3–6, 10; MU3 s22–23; `pcp-m-2-38`*

### 2.VIII.4 — Solicitor's duty: ask the client's religion

**Q2-32** · `2.VIII.4` · own question · `pcp-m-2-39`

A client named Ahmad bin Ismail asks a solicitor to draft a will leaving everything to his wife, and says nothing about religion. What should the solicitor do?

A. Draft as instructed; religion is the client's business.
B. At least ask the client's religion, to consider whether Syariah law affects the instructions.
C. Refuse to act.
D. Refer him to the SYC to draft the will.

**Answer: B.** A solicitor who sees a Muslim name must at least ask the testator's religion; it does not matter that the client did not raise it (*Zailani bin Abdullah Tan v K Jayakumar Naidu* [2017] SGDC 172). A risks negligence. C and D are wrong.
*Cite: Zailani [2017] SGDC 172; MU3 s25; `pcp-m-2-39`*

### 2.IX Civil courts and Muslim inheritance disputes

Sub-points 2.IX.1–2.IX.6. No real question; own questions Q2-33 to Q2-38.

### 2.IX.1 — The civil courts' approach

**Q2-33** · `2.IX.1` · own question · `pcp-m-2-40`

In a civil court dispute over a Muslim estate, which is CORRECT?

A. Muslim law must be proved as foreign law by expert evidence.
B. Muslim law is part of the law of the land; the court first asks whether an asset is outside the estate (joint tenancy, nomination, hibah), and a fatwa does not bind it.
C. A fatwa binds the civil court.
D. The common law of trusts decides whether a wakaf exists.

**Answer: B.** Muslim law need not be proved like foreign law (*LS Investments v MUIS*: wakaf decided by Muslim law, not trust law); the approach is estate by Muslim law, check estate-planning instruments, then faraid; a fatwa is an opinion only. A, C, D are wrong.
*Cite: LS Investments v MUIS [1998] 3 SLR 369; MUIS v Saeed Salman [2016] SGHC 4; MU3 s31–33; `pcp-m-2-40`*

### 2.IX.2 — Challenging an Inheritance Certificate

**Q2-34** · `2.IX.2` · own question · `pcp-m-2-41`

Grandchildren claim they were wrongly left out of an Inheritance Certificate because their grandmother was validly married to the deceased. Where is this decided?

A. The SYC, by appeal to the Appeal Board.
B. The High Court, as a question of fact.
C. MUIS.
D. It cannot be challenged.

**Answer: B.** The SYC issues the certificate on the applicant's information; a challenge goes to the High Court (*Re Will of Shaikh Ahmad bin Abdullah Wahdain Basharil* [2002] SGHC 165).
*Cite: Re Will of Shaikh Ahmad [2002] SGHC 165; MU3 s34–36; `pcp-m-2-41`*

### 2.IX.3 — Letter of wishes and deed of family arrangement (Shiraz)

**Q2-35** · `2.IX.3` · own question · `pcp-m-2-42`

After their father's death, six Muslim siblings agreed in writing to share his bank accounts equally, as his letter of wishes asked. One sibling later demands his faraid share. Which is CORRECT?

A. Faraid prevails; the agreement is void.
B. The agreement is not inconsistent with Muslim law and binds them (*Shiraz Abidally Husain*).
C. The letter of wishes is a valid will.
D. The SYC must decide.

**Answer: B.** Heirs may agree a different distribution; the agreement bound the siblings (*Shiraz Abidally Husain* [2007] SGCA 16). A, C, D are wrong.
*Cite: Shiraz Abidally Husain [2007] SGCA 16; MU3 s37–39; `pcp-m-2-42`*

### 2.IX.4 — Joint tenancy and survivorship (Shafeeq)

**Q2-36** · `2.IX.4` · own question · `pcp-m-2-43`

A Muslim husband and wife held their house as joint tenants. He dies. Do his faraid heirs share the house?

A. Yes; faraid overrides joint tenancy.
B. No; the house passes to the wife by survivorship and is not part of his estate (*Shafeeq*).
C. Only his sons share it.
D. Half passes by faraid.

**Answer: B.** The house passed to the wife by survivorship; it was not part of the husband's estate, so faraid did not apply (*Shafeeq bin Salim Talib v Fatimah*), and a 2019 fatwa treats joint tenancy as religiously valid. A, C, D are wrong.
*Cite: Shafeeq [2010] SGCA 11; MU3 s44–47; `pcp-m-2-43`*

### 2.IX.5 — CPF nominations (Saniah Ali; 2010 fatwa)

**Q2-37** · `2.IX.5` · own question · `pcp-m-2-44`

A Muslim nominated his step-sister for his CPF monies. His faraid heirs say she holds them on trust for them. Which is CORRECT?

A. She holds them on trust for the faraid heirs.
B. The monies are not part of the estate and she keeps them (*Saniah Ali*); the 2010 fatwa treats a nomination as a hibah.
C. The nomination is void because she is not a Muslim heir.
D. The monies pass under s 112 AMLA.

**Answer: B.** CPF paid to a nominee is outside the estate (*Saniah Ali v Abdullah Ali* [1990] 1 SLR(R) 555); the earlier fatwa did not bind the court; the 2010 fatwa treats a nomination as a gift. Without a nomination, faraid applies. A, C, D are wrong.
*Cite: Saniah Ali [1990] 1 SLR(R) 555; MU3 s48–51; `pcp-m-2-44`*

### 2.IX.6 — Hibah (gift) and HDB flats

**Q2-38** · `2.IX.6` · own question · `pcp-m-2-45`

A Muslim mother made a hibah of her HDB flat to her daughter without HDB's consent. MUIS says the hibah is valid in Muslim law. Which is CORRECT?

A. The hibah is valid because MUIS says so.
B. The hibah is void because HDB's prior written consent was not obtained (s 50 HDA); the general law decides whether property was validly disposed of.
C. The flat passes to the daughter on the mother's death.
D. The SYC decides.

**Answer: B.** *Haja Maideen v Roshan Begum* [2017] SGHC 164: the hibah was void without HDB consent; MUIS's view did not bind the court. A, C, D are wrong.
*Cite: HDA s 50; Haja Maideen [2017] SGHC 164; MU3 s40–43; `pcp-m-2-45`*

## 3 · Employment Law

### 3.I Legislative framework and classes of employees

Sub-points 3.I.1–3.I.5. Real question: SQ Employment Q1 (3.I.4). Own questions Q3-1 to Q3-4.

### 3.I.1 — Key legislation

**Q3-1** · `3.I.1` · own question · `pcp-m-3-1`

Which statement about the Employment Act 1968 is CORRECT?

A. It sets terms the parties cannot improve on.
B. It sets a floor: the parties may agree better terms but not worse.
C. The Workplace Fairness Act 2025 has replaced it.
D. Tripartite Guidelines under it have the force of law.

**Answer: B.** The EA is the main labour statute for contracts of service and sets minimum terms. A reverses this. C: the WFA was passed in 2025 but is not yet in force, and supplements rather than replaces the EA. D: Tripartite Advisories and Guidelines add guidance without the force of law.
*Cite: EM1 s4–5; `pcp-m-3-1`*

### 3.I.2 — Who is an employee

**Q3-2** · `3.I.2` · own question · `pcp-m-3-2`

Which person is an "employee" under s 2(1) of the Employment Act?

A. A domestic worker.
B. A seafarer.
C. A freelance graphic designer engaged under a contract for services.
D. A part-time retail assistant working 20 hours a week under a contract of service.

**Answer: D.** An employee is a person under a contract of service, including a workman; part-timers are covered. A and B are excluded from the definition. C: independent contractors (contracts for service) are outside the EA; whether a relationship is in fact employment turns on control, remuneration, leave and benefits, and similar indicia.
*Cite: EA s 2(1); EM1 s7; `pcp-m-3-2`*

### 3.I.3 — Categories of employee

**Q3-3** · `3.I.3` · own question · `pcp-m-3-3`

Which categories of employee are covered by the Employment Act?

A. Full-time employees only.
B. Full-time and part-time employees only.
C. Full-time, part-time (under 35 hours a week), temporary and contract employees.
D. Permanent employees only.

**Answer: C.** All four categories are covered by the EA. A, B and D are too narrow.
*Cite: EM1 s8; Cyril-EM §1.2; `pcp-m-3-3`*

### 3.I.4 — Who Part IV of the EA covers

**QSQ-E1** · `3.I.4` · SQ Employment Q1 [Part B 2024], official key D · `pcp-m-3-4`

Who would Part IV of the Employment Act not apply to?

A. A sales associate who earns $2,500 a month.
B. A bus driver who earns $4,400 a month.
C. A construction worker who earns $ 2,800 a month.
D. A facilities manager who earns $2,500 a month.

**Answer: D.** Part IV applies to workmen earning up to $4,500 a month and to non-workmen earning up to $2,600 a month, but not to persons employed in a managerial or executive position (s 35). The facilities manager is out because he is a manager, whatever his pay. A: non-workman under $2,600. B and C: workmen under $4,500. Official key: D.
*Cite: EA s 35; EM1 s9; SQ p81 Q1, key p129; `pcp-m-3-4`*

### 3.I.5 — Foreign employees; minors

**Q3-4** · `3.I.5` · own question · `pcp-m-3-5`

A 17-year-old signs a contract of service and leaves without notice. Can the employer recover damages from him?

A. Yes, like any adult employee.
B. No; a contract of service with a person under 18 is not enforceable against him and no damages are recoverable, unless it is for his benefit.
C. Yes, but only with MOM's permission.
D. No, because minors cannot be employed at all.

**Answer: B.** EA s 12: a person under 18 may enter a contract of service, but it is not enforceable against him unless it is for his benefit. A and C are wrong. D: minors may be employed. Foreign employees need an MOM work pass.
*Cite: EA s 12; EM1 s10; `pcp-m-3-5`*

### 3.II Statutory rights and obligations: pay, hours, leave, retirement, safety

Sub-points 3.II.1–3.II.8. Real questions: SQ Employment Q3 (3.II.6), Q6 (3.II.5), Q9 (under 3.VIII.3, also 3.II.8). Own questions cover the rest.

### 3.II.1 — Payment of salary and CPF

**Q3-5** · `3.II.1` · own question · `pcp-m-3-6`

An employee's salary period ends on 31 March. By when must the employer pay?

A. By 31 March.
B. Before the end of 7 April (the seventh day after the salary period ends).
C. By 14 April.
D. By 30 April.

**Answer: B.** Salary must be paid before the end of the seventh day after the salary period, which may not exceed one month (EA ss 20(2), 21(1)). There is no general minimum wage. Failure to pay means the employer is deemed to have broken the contract (s 13(1)).
*Cite: EA ss 13(1), 20(2), 21(1); CPF Act s 7(1); EM1 s12; `pcp-m-3-6`*

### 3.II.2 — Hours of work and overtime (Part IV)

**Q3-6** · `3.II.2` · own question · `pcp-m-3-7`

A Part IV employee earns $2,200 basic a month. What is the minimum overtime rate per hour?

A. $11.54.
B. $17.31.
C. $15.38.
D. $22.00.

**Answer: B.** Hourly basic rate = (12 × monthly basic) ÷ (52 × 44) = 26,400 ÷ 2,288 = $11.54; overtime is at least 1.5 times that (s 38(4)): $17.31. A is the basic hourly rate. Normal limits are 8 hours a day or 44 a week (s 38(1)); overtime is capped at 72 hours a month (s 38(5)).
*Cite: EA s 38(1), (4), (5), Fourth Schedule; `pcp-m-3-7`*

### 3.II.3 — Annual leave (s 88A)

**Q3-7** · `3.II.3` · own question · `pcp-m-3-8`

An employee is in her 4th year of continuous service. What is her minimum paid annual leave under the EA?

A. 7 days.
B. 10 days.
C. 14 days.
D. 12 days.

**Answer: B.** s 88A: 7 days in the 1st year, rising by one a year to 14 in the 8th year and after; the 4th year gives 10. Leave is forfeited for unexcused absence over 20% of working days (s 88A(5)).
*Cite: EA s 88A; EM1 s13; `pcp-m-3-8`*

### 3.II.4 — Sick leave and hospitalisation leave (s 89)

**Q3-8** · `3.II.4` · own question · `pcp-m-3-9`

An employee with 8 months' service is certified sick. What are his maximum outpatient and hospitalisation leave entitlements a year?

A. 5 and 15 days.
B. 11 and 45 days.
C. 14 and 60 days.
D. 14 and 30 days.

**Answer: C.** After 6 months' service: 14 days outpatient and 60 days hospitalisation (including outpatient) (s 89). A, B are for 3–4 and 5–6 months' service.
*Cite: EA s 89; EM1 s13; `pcp-m-3-9`*

### 3.II.5 — Maternity, paternity, childcare and shared parental leave

**QSQ-E6** · `3.II.5` · SQ Employment Q6 [Original], official key C · `pcp-m-3-10`

Which of the following employee entitlements is not prescribed under the Employment Act?

A. Annual leave.
B. Maternity leave.
C. Paternity leave.
D. Childcare leave.

**Answer: C.** Paternity leave is provided by the Child Development Co-Savings Act, not the EA (currently 4 weeks of Government-Paid Paternity Leave). The EA provides annual leave (s 88A), maternity leave and childcare leave. Official key: C.
*Cite: EM1 s13; CDCSA; SQ p82 Q6, key p129; `pcp-m-3-10`*

### 3.II.6 — Retirement, re-employment and the EAP

**QSQ-E3** · `3.II.6` `3.VII.4` · SQ Employment Q3 [Part B 2024], official key D · `pcp-m-3-11` `pcp-m-3-32`

Richard is a Singapore citizen who has just turned 63 years old. He has been working with the same company for 20 years. However, the company is undergoing a major restructuring, and he has been informed that his entire department is being made redundant. His employment contract does not provide for any retrenchment benefits. Which of the following statements is CORRECT?

A. Having worked for more than 2 years for the same employer, Richard is statutorily entitled to a retrenchment payment at the rate of one month's pay per year of service.
B. Richard falls within a protected class of employee and therefore cannot be made redundant.
C. Richard's employer should pay him an Employment Assistance Payment as retrenchment payment.
D. Richard can be retrenched and is not statutorily entitled to any retrenchment benefits.

**Answer: D.** No one has a statutory right to retrenchment benefits unless the contract or a collective agreement gives one; s 45 EA only disentitles those with under 2 years' service (so A is wrong). B: s 8 RRA bars dismissal on the ground of age, not retrenchment for redundancy. C: the EAP is paid where no re-employment is offered at the minimum retirement age (now 64, from 1 Jul 2026); it is not a retrenchment payment. Official key: D.
*Cite: EA s 45; RRA s 8; EM-CS1 s10; SQ p81 Q3, key p129; `pcp-m-3-11`, `pcp-m-3-32`*

**Q3-9** · `3.II.6` · own question · `pcp-m-3-11`

From 1 July 2026, what are the minimum retirement age and the re-employment age?

A. 62 and 67.
B. 63 and 68.
C. 64 and 69.
D. 65 and 70.

**Answer: C.** The minimum retirement age rose from 63 to 64 on 1 Jul 2026; employers must offer re-employment to eligible employees up to 69, or pay an EAP if no suitable vacancy.
*Cite: EM-CS1 s10; EM1 s15; RRA; `pcp-m-3-11`*

**Q3-31** · `3.II.6` · own question · `pcp-m-3-11`

Siti, 66, was re-employed by her company at 64. Her department is now being closed and she is retrenched. Neither her contract nor any collective agreement mentions retrenchment benefits. Which statement is CORRECT?

A. Siti is statutorily entitled to one month's salary per year of service.
B. Siti cannot be retrenched because she is a re-employed employee.
C. The employer may follow the EAP recommendations in the Tripartite Guidelines for Re-employment of Older Workers instead of paying a retrenchment benefit.
D. The employer must pay both an EAP and a retrenchment benefit.

**Answer: C.** For retrenched employees aged 64 or above, the tripartite guidance is that employers can follow the EAP recommendations in the re-employment guidelines, unless the contract or collective agreement provides retrenchment benefits. This is guidance, not a statutory entitlement. A: there is no statutory retrenchment benefit. B: re-employed employees can be retrenched for redundancy. D: the guidance offers the EAP in place of, not on top of, a retrenchment benefit.
*Cite: TAFEP, Responsible Retrenchment Practices FAQ; RRA; `pcp-m-3-11`*

### 3.II.7 — Employee personal data (PDPA)

**Q3-10** · `3.II.7` · own question · `pcp-m-3-12`

An employer wants to use an employee's personal data to investigate alleged misconduct. Does it need the employee's consent?

A. Yes, always.
B. No; consent is not required for investigations and proceedings, evaluative purposes, or managing or ending the employment relationship.
C. Only if the employee is a manager.
D. Only with PDPC approval.

**Answer: B.** Under the PDPA consent is not required for investigations and proceedings, evaluative purposes, in the course of employment, or to manage or end the employment relationship. The employer must still protect the data. A, C, D are wrong.
*Cite: EM1 s16; `pcp-m-3-12`*

### 3.II.8 — Workplace safety (WSHA) and work injury compensation (WICA)

See also QSQ-E9 under 3.VIII.3 (a WICA claim cannot go to the ECT).

**Q3-11** · `3.II.8` · own question · `pcp-m-3-13`

Which person is covered by the Work Injury Compensation Act?

A. A self-employed private-hire driver.
B. A domestic worker.
C. A factory employee injured on a work trip overseas.
D. An independent contractor.

**Answer: C.** WICA covers employees for accidents arising out of and in the course of employment, wherever they happen. It excludes independent contractors, the self-employed, domestic workers and uniformed personnel (A, B, D). Claims must be made within 1 year of the accident.
*Cite: WICA; EM1 s17–18; `pcp-m-3-13`*

### 3.III The employment contract: express terms, implied terms, variation

Sub-points 3.III.1–3.III.3. No real question; own questions Q3-12 to Q3-14.

### 3.III.1 — Express terms and restrictive covenants

**Q3-12** · `3.III.1` · own question · `pcp-m-3-14`

When will a post-employment non-compete clause be upheld?

A. Always, if the employee signed it.
B. Only if it protects a legitimate business interest, goes no further than reasonably necessary, and is in the public interest.
C. Never; all restraints are void.
D. Only if it lasts less than 6 months.

**Answer: B.** Restrictive covenants are restraints of trade, prima facie void, upheld only if they protect a legitimate interest (trade secrets, connections, workforce stability) and are reasonable and in the public interest. A, C, D are wrong.
*Cite: EM1 s20; Cyril-EM §1.4; `pcp-m-3-14`*

### 3.III.2 — Implied terms

**Q3-13** · `3.III.2` · own question · `pcp-m-3-15`

Which is CORRECT about the implied term of mutual trust and confidence (IMTC) in Singapore?

A. It does not exist in Singapore law.
B. It exists, and an employer that put an employee on a PIP intending to terminate him was in breach (*Prashant Mudgal v SAP*), but may be modified or excluded by express words.
C. It overrides express terms.
D. It applies only to managers.

**Answer: B.** The IMTC is implied in law (with confidence, care, good faith and fidelity); *Prashant Mudgal v SAP* [2026] SGHC 15 found breach but awarded nominal damages. Employers may modify or exclude it expressly. C: no implied term contradicts an express term.
*Cite: Prashant Mudgal v SAP [2026] SGHC 15; EM1 s21; `pcp-m-3-15`*

### 3.III.3 — Variation of terms

**Q3-14** · `3.III.3` · own question · `pcp-m-3-16`

An employer wants to cut an employee's salary. The contract has no variation clause. What is needed?

A. Nothing; the employer may vary unilaterally with notice.
B. The employee's agreement, supported by consideration and intention to create legal relations (or estoppel).
C. MOM approval.
D. A union ballot.

**Answer: B.** With no variation clause, or for a key term, variation must be consensual and supported by consideration with intention to create legal relations, or arise by estoppel. A, C, D are wrong.
*Cite: EM1 s22; `pcp-m-3-16`*

### 3.IV Industrial relations

Sub-points 3.IV.1–3.IV.3. No real question; own questions Q3-15 to Q3-17.

### 3.IV.1 — Tripartism

**Q3-15** · `3.IV.1` · own question · `pcp-m-3-17`

Who are Singapore's tripartite partners?

A. MOM, NTUC and SNEF.
B. MOM, MUIS and SAL.
C. NTUC, SNEF and the Law Society.
D. MOM, the ECT and TADM.

**Answer: A.** The Ministry of Manpower, the National Trades Union Congress and the Singapore National Employers Federation, who issue the Tripartite Advisories and Guidelines and run TADM.
*Cite: EM1 s24; EM2 s27; `pcp-m-3-17`*

### 3.IV.2 — Trade unions (Trade Unions Act)

**Q3-16** · `3.IV.2` · own question · `pcp-m-3-18`

Within what period must a trade union register after it is established?

A. 7 days.
B. One month.
C. Six months.
D. No registration is required.

**Answer: B.** A trade union must register within one month of being established. Its principal object is to regulate relations to promote good industrial relations, improve workmen's conditions or status, or raise productivity (TUA s 2).
*Cite: Trade Unions Act s 2; EM1 s25; `pcp-m-3-18`*

### 3.IV.3 — Collective bargaining (Industrial Relations Act)

**Q3-17** · `3.IV.3` · own question · `pcp-m-3-19`

Whom does a certified collective agreement bind?

A. All employees of the employer.
B. The employer and the unionised employees, once certified by the Industrial Arbitration Court.
C. All employers in the industry.
D. Only the union officers.

**Answer: B.** The agreement binds only once certified by the IAC, and then only the employer and the unionised employees, not all staff. Any party bound may ask the IAC to interpret it.
*Cite: Industrial Relations Act; EM1 s26–27; Cyril-EM §1.5; `pcp-m-3-19`*

### 3.V Harassment, bullying and discrimination

Sub-points 3.V.1–3.V.5. No real question; own questions Q3-18 to Q3-22.

### 3.V.1 — Workplace harassment and bullying

**Q3-18** · `3.V.1` · own question · `pcp-m-3-20`

An employee is persistently bullied by a co-worker. Which statute lets her seek civil remedies against the harasser?

A. The Employment Act.
B. The Protection from Harassment Act 2014.
C. The Trade Unions Act.
D. The Retirement and Re-employment Act.

**Answer: B.** POHA gives civil remedies and criminal sanctions against the harasser. The employer also has a WSHA duty to take reasonably practicable measures for employees' safety and health. A, C, D are wrong.
*Cite: POHA 2014; WSHA; EM2 s5; `pcp-m-3-20`*

### 3.V.2 — Existing anti-discrimination framework (FCF, TGFEP)

**Q3-19** · `3.V.2` · own question · `pcp-m-3-21`

Before the Workplace Fairness Act comes into force, how is breach of the Tripartite Guidelines on Fair Employment Practices mainly enforced?

A. By damages in the ECT.
B. By administrative penalties such as curtailing the employer's work pass privileges.
C. By criminal prosecution for every breach.
D. It cannot be enforced.

**Answer: B.** The FCF and TGFEP lack the force of law and are enforced administratively (e.g. work pass curtailment); a false declaration in a work pass application may be prosecuted under the EFMA. A, C, D are wrong.
*Cite: EM2 s6; `pcp-m-3-21`*

### 3.V.3 — Flexible work arrangement requests

**Q3-20** · `3.V.3` · own question · `pcp-m-3-22`

Under the Tripartite Guidelines on FWA Requests (from 1 Dec 2024), which is a reasonable ground to reject a request?

A. Management does not believe in flexible work.
B. The arrangement would harm output.
C. No reason need be given.
D. The employee is a woman.

**Answer: B.** Employers should have a process, discuss, and decide in writing with reasons; harm to output is a reasonable ground, disbelief in FWAs is not. Employers keep the final say. C: reasons are expected for a rejection. D is discriminatory.
*Cite: Tripartite Guidelines on FWA Requests; EM2 s7; `pcp-m-3-22`*

### 3.V.4 — Workplace Fairness Act 2025: scope and discrimination

**Q3-21** · `3.V.4` · own question · `pcp-m-3-23`

Which is NOT covered by the Workplace Fairness Act 2025?

A. Refusing to promote an employee because of her pregnancy.
B. A job advertisement stating "Chinese speakers only" for no job reason.
C. Indirect discrimination, such as a numeracy test that disadvantages older applicants.
D. Retrenching an employee because of his nationality.

**Answer: C.** The WFA covers adverse employment decisions on protected characteristics at every stage, discriminatory policies and advertisements, but not indirect discrimination, provision of benefits, or FWAs. It is passed but not yet in force (expected end-2027).
*Cite: WFA 2025 s 17(1); EM2 s8–10; `pcp-m-3-23`*

### 3.V.5 — Workplace Fairness Act 2025: grievances and claims

**Q3-22** · `3.V.5` · own question · `pcp-m-3-24`

Under the WFA, what must happen before a discrimination claim can be filed, and where does a S$100,000 claim go?

A. Nothing; file in the High Court.
B. Mediation (mandatory, after the internal grievance process); then the ECT, which hears claims up to S$250,000.
C. MOM investigation; then the State Courts.
D. A union referral; then the IAC.

**Answer: B.** Raise it internally, then mediation is mandatory; claims go to the ECT (up to $250,000) or High Court (above). No lawyers in the ECT. A, C, D are wrong.
*Cite: WFA 2025; EM2 s11; `pcp-m-3-24`*

### 3.VI Performance management and misconduct

Sub-points 3.VI.1–3.VI.4. Real question: SQ Employment Q2 (3.VI.2, 3.VI.4, 3.VI.3). Own questions cover the rest.

### 3.VI.1 — Performance management

**Q3-23** · `3.VI.1` · own question · `pcp-m-3-25`

An employer places an employee on a PIP with impossible targets, having already decided to dismiss him. What risk does it run?

A. None; PIPs are at the employer's discretion.
B. A sham PIP may found a constructive dismissal or IMTC claim.
C. Criminal liability under the EA.
D. Automatic reinstatement.

**Answer: B.** A PIP must be genuine and reasonable with a real chance to improve; a sham PIP may found constructive dismissal or an IMTC claim (see *Prashant Mudgal v SAP*). A, C, D are wrong.
*Cite: EM2 s13; EM1 s21; `pcp-m-3-25`*

### 3.VI.2 — Dismissal for misconduct after due inquiry (s 14(1))

**QSQ-E2** · `3.VI.2` `3.VI.4` `3.VI.3` · SQ Employment Q2 [Part B 2024], official key C · `pcp-m-3-26` `pcp-m-3-28` `pcp-m-3-27`

Dean works as a cashier at the supermarket. One of his co-workers tells his manager that he has been taking money out of the cash register. Which of the following is his manager entitled to do?

A. Dismiss Dean immediately for misconduct.
B. Suspend Dean without pay for a week while investigating the allegation.
C. Dismiss Dean in accordance with the notice requirements in his contract of employment.
D. Invite Dean to a meeting titled "New Store Policy on Work from Home", where he is asked questions about the alleged theft with a view to considering disciplinary action against him.

**Answer: C.** Either party may end the contract by contractual notice without giving reasons. A: summary dismissal for misconduct needs a due inquiry first (s 14(1)). B: suspension pending inquiry must be on at least half pay (s 14(8)). D: an ambush meeting under a misleading title is not a proper inquiry (*Singapore Recreation Club v Abdul Rashid*). Official key: C.
*Cite: EA ss 10, 14(1), 14(8); Abdul Rashid [2020] SGHC 156; SQ p81 Q2, key p129; `pcp-m-3-26`, `pcp-m-3-28`, `pcp-m-3-27`*

**Q3-24** · `3.VI.2` · own question · `pcp-m-3-26`

After a due inquiry finds misconduct, which may the employer do under s 14(1) instead of dismissing?

A. Fine the employee one month's salary.
B. Instantly downgrade him, or suspend him without pay for up to one week.
C. Suspend him without pay for one month.
D. Withhold his CPF.

**Answer: B.** s 14(1): dismiss without notice, instantly downgrade, or suspend without pay for up to one week. A, C, D are not permitted.
*Cite: EA s 14(1); EM2 s14–15; `pcp-m-3-26`*

### 3.VI.3 — What a proper due inquiry requires

**Q3-25** · `3.VI.3` · own question · `pcp-m-3-27`

Which is a requirement of a proper due inquiry?

A. A hearing before an external tribunal.
B. The employee is told the allegations and evidence, has a fair chance to answer, and the decision-makers are unbiased.
C. Legal representation for the employee.
D. A prescribed MOM form.

**Answer: B.** No form is prescribed, but the employee must know the case, be heard, and face unbiased decision-makers (*Long Kim Wing v LTX-Credence*); failure can make a summary dismissal wrongful (*Wong Sung Boon v Fuji Xerox*: over $1.4m). A, C, D are not required.
*Cite: Long Kim Wing [2017] SGHC 151; Wong Sung Boon [2021] SGHC 24; EM2 s15–17; `pcp-m-3-27`*

### 3.VI.4 — Suspension during the inquiry (s 14(8))

**Q3-26** · `3.VI.4` · own question · `pcp-m-3-28`

An employee is suspended for a week pending a s 14 inquiry, on half pay. No misconduct is found. What follows?

A. Nothing; the half pay is final.
B. The withheld salary must be restored immediately (s 14(9)).
C. He gets interest only.
D. He must claim at the ECT.

**Answer: B.** s 14(8) allows suspension for up to a week (longer with the Commissioner's approval) on at least half pay; s 14(9) requires the withheld pay to be restored immediately if no misconduct is found. A, C, D are wrong.
*Cite: EA s 14(8)–(9); EM2 s18; `pcp-m-3-28`*

### 3.VII Termination of employment

Sub-points 3.VII.1–3.VII.5. Real questions: SQ Employment Q5 (3.VII.1), Q8, Q10 (3.VII.3), Q4 (3.VII.5), Q3 (under 3.II.6, also 3.VII.4). Own questions cover the rest.

### 3.VII.1 — Notice periods (s 10)

**QSQ-E5** · `3.VII.1` · SQ Employment Q5 [Part B 2024], official key D · `pcp-m-3-29`

Christopher has been employed by his company for three years. His employment contract states that his employment may be terminated with one week's notice. His manager tells him that the company is letting him go and is giving him the requisite one week's notice. Which of the following statements is CORRECT?

A. Christopher's employment has been wrongfully terminated, as the one week's notice is shorter than the 2 weeks' notice set out in Section 10(3) of the Employment Act for persons employed between 2 and 5 years.
B. Christopher's employment has been properly terminated, because he has been given the appropriate minimum notice period set out in section 10(3) of the Employment Act.
C. Chrisopher's employment has been wrongfully terminated, since the notice period in his contract of employment cannot be shorter than the notice periods set out in section 10(3) of the Employment Act.
D. Christopher's employment has been properly terminated, since the notice period of one week is the notice period for termination set out in his employment contract.

**Answer: D.** The notice period is fixed by the contract; s 10(3) applies only where the contract is silent (s 10(2)). A and C treat s 10(3) as a floor over the contract. B: one week is not the s 10(3) period for 3 years' service (2 weeks). Official key: D.
*Cite: EA s 10(2)–(3); SQ p82 Q5, key p129; `pcp-m-3-29`*

### 3.VII.2 — Salary in lieu of notice; reasons

**Q3-27** · `3.VII.2` · own question · `pcp-m-3-30`

An employer terminates with salary in lieu of notice and states the reason as "poor performance". Which is CORRECT?

A. It must always give reasons.
B. It need not give reasons, but having given one, it bears the burden of proving it.
C. Salary in lieu is not allowed under the EA.
D. Salary in lieu is calculated on basic pay only.

**Answer: B.** An employer terminating with notice or pay in lieu need not give reasons; if it does, it must prove them. C: s 11(1) allows salary in lieu at the gross rate. D: it is gross pay.
*Cite: EA s 11(1); EM2 s21; `pcp-m-3-30`*

### 3.VII.3 — Termination without notice

**QSQ-E8** · `3.VII.3` · SQ Employment Q8 [Original], official key A · `pcp-m-3-31`

Heather's employment contract provides that either party may terminate the employment by giving 30 days' notice, but in certain circumstances, Heather's employment may be terminated forthwith without notice. One of these circumstances is if she is absent without reason for more than 5 working days in a month. Heather was absent from work for 4 days continuously without prior leave from her employer and has no reasonable excuse for the absence; she also does not inform or attempt to inform her of the excuse for the absence. Her employer:

A. Can terminate her employment without notice as she is deemed to have broken her contract.
B. Cannot terminate her employment, because she has been absent without reason for less than five working days.
C. Cannot terminate her employment, because her unexplained absence for two days does not amount to misconduct.
D. Cannot terminate her employment with thirty days' notice.

**Answer: A.** s 13(2) EA deems an employee who is absent for more than 2 days continuously without prior leave, and without reasonable excuse or without informing the employer, to have broken her contract, so the employer may end it without notice despite the contract's 5-day trigger. B ignores s 13(2). C misstates the facts and the rule. D: the employer can always give contractual notice. Official key: A.
*Cite: EA s 13(2); SQ p83 Q8, key p129; `pcp-m-3-31`*

**QSQ-E10** · `3.VII.3` `3.VII.4` · SQ Employment Q10 [Original], official key C · `pcp-m-3-31` `pcp-m-3-32`

Which of the following is not a ground for immediate termination of the employment relationship without notice under the Employment Act 1968?

A. An employee's absence from work for 10 continuous days without reasonable notice or excuse.
B. The employer's failure to pay the employee's salary.
C. Where an employee's job has become redundant.
D. A finding that the employee has committed misconduct inconsistent with an implied condition of service, following due inquiry.

**Answer: C.** Redundancy is ended by notice under the contract (retrenchment), not without notice. A: s 13(2). B: s 13(1), the employer is deemed to have broken the contract. D: s 14(1). Official key: C.
*Cite: EA ss 13, 14(1); SQ p84 Q10, key p129; `pcp-m-3-31`, `pcp-m-3-32`*

### 3.VII.4 — Retrenchment and redundancy

**Q3-28** · `3.VII.4` · own question · `pcp-m-3-32`

A company with 50 employees retrenches a worker. Which is CORRECT?

A. It need not tell MOM.
B. It must notify MOM within 5 working days of telling the employee.
C. It must pay one month's salary per year of service by statute.
D. A worker with 18 months' service is entitled to retrenchment benefit.

**Answer: B.** An employer with at least 10 employees must notify MOM within 5 working days of informing the employee. C: there is no statutory retrenchment benefit. D: under 2 years' service disentitles (s 45). See the Tripartite Advisory on Responsible Retrenchment.
*Cite: EA s 45; EM2 s24; `pcp-m-3-32`*

### 3.VII.5 — Protected employees

**QSQ-E4** · `3.VII.5` · SQ Employment Q4 [Part B 2024], official key B · `pcp-m-3-33`

Sherry has been working for the same company for two years. She notifies her supervisor that she is approximately 5 months' pregnant, and that she will be going on maternity leave in a few months. Her supervisor is taken aback as she had been planning to terminate Sherry's employment for redundancy. What can her supervisor legally do?

A. Her supervisor can eliminate Sherry's position when Sherry is on maternity leave and issue the termination notice then.
B. Her supervisor can terminate Sherry's employment with notice on grounds of redundancy but must pay her all of her maternity benefits.
C. Her supervisor can proceed with the termination of Sherry's employment without payment of any maternity benefits, since termination is on grounds of redundancy and Sherry is no longer entitled to said benefits.
D. Her supervisor can only terminate Sherry's employment after her maternity leave ends.

**Answer: B.** A pregnant employee with at least 3 months' service who is retrenched (s 84A EA) must still be paid all maternity benefits (s 12 CDCSA). A: she cannot be dismissed while on maternity leave (s 81). C ignores s 12 CDCSA. D: she may be retrenched now, with benefits. Official key: B.
*Cite: EA ss 81, 84A; CDCSA s 12; SQ p82 Q4, key p129; `pcp-m-3-33`*

### 3.VIII Wrongful dismissal and remedies

Sub-points 3.VIII.1–3.VIII.4. Real questions: SQ Employment Q7 (3.VIII.2, 3.VIII.3), Q9 (3.VIII.3, 3.II.8). Own questions cover the rest.

### 3.VIII.1 — Statutory wrongful dismissal claim (s 14(2)–(3) EA)

**Q3-29** · `3.VIII.1` · own question · `pcp-m-3-34`

A manager with 4 months' service is dismissed with one month's notice. Can he bring a statutory wrongful dismissal claim under s 14(2) EA?

A. Yes; every employee can.
B. No; a manager dismissed with notice must have at least 6 months' service.
C. Yes, if he earns under $4,500.
D. No; managers are never covered.

**Answer: B.** Relevant employees (s 14(2A)) are managers or executives dismissed with notice after at least 6 months' service; managers or executives dismissed without notice (any service); and any non-managerial employee. The remedy is reinstatement or compensation (s 14(3)). A, C, D are wrong.
*Cite: EA s 14(2)–(3); EM2 s27; `pcp-m-3-34`*

### 3.VIII.2 — Constructive dismissal

**QSQ-E7** · `3.VIII.2` `3.VIII.3` · SQ Employment Q7 [Original], official key C · `pcp-m-3-35` `pcp-m-3-36`

Daniel is employed as a financial analyst by an investment firm. His employment contract requires him to achieve specified performance targets and to work on client transactions assigned by his manager. Without explanation, his employer ceases assigning him any work for several weeks, despite Daniel remaining ready and willing to perform his duties. Daniel subsequently resigns. More than two months after his resignation, Daniel decides to commence proceedings in the Employment Claims Tribunal ("ECT"), claiming S$70,000 for wrongful dismissal. Which of the following statements is CORRECT?

A. Daniel cannot bring a wrongful dismissal claim before the ECT because he resigned from his employment.
B. Daniel may bring a claim for S$70,000 before the ECT because wrongful dismissal claims are not subject to any monetary limit.
C. Daniel cannot bring a claim before the ECT because the time limit for filing a wrongful dismissal claim under the Employment Claims Act has expired.
D. Daniel cannot bring a claim before the ECT because he was not represented by a trade union.

**Answer: C.** The mediation request for wrongful dismissal must be lodged within 1 month after the dismissal (ECA s 3(2)); over two months is too late. A: "dismissal" includes constructive dismissal, so resigning is no bar (*Cheah Peng Hock*). B: the limit is $20,000 ($30,000 union-assisted). D: union help raises the limit but is not required. Official key: C.
*Cite: ECA s 3(2); EA s 2; Cheah Peng Hock [2013] 2 SLR 577; SQ p83 Q7, key p129; `pcp-m-3-35`, `pcp-m-3-36`*

### 3.VIII.3 — TADM and the Employment Claims Tribunal

**QSQ-E9** · `3.VIII.3` `3.II.8` · SQ Employment Q9 [Original], official key B · `pcp-m-3-36` `pcp-m-3-13`

Under the Employment Claims Act 2016, which of the following claims cannot be heard before the Employment Claims Tribunal?

A. A claim for unpaid maternity benefits under the Child Development Co-Savings Act 2001.
B. A workmen's compensation claim under the Workplace Safety and Health Act 2006.
C. A claim for unpaid retrenchment benefits, which were specified in the employment contract.
D. A wrongful dismissal claim for SGD50,000 where the employee (non-unionised) has indicated he is prepared to cap at SGD20,000.

**Answer: B.** Work injury compensation is claimed under WICA, not in the ECT. A, C: the ECT hears CDCSA maternity benefits and contractual retrenchment benefits. D: a claimant may abandon the excess over the $20,000 limit. Official key: B.
*Cite: ECA; WICA; SQ p84 Q9, key p129; `pcp-m-3-36`, `pcp-m-3-13`*

### 3.VIII.4 — Claims in court; measure of damages

**Q3-30** · `3.VIII.4` · own question · `pcp-m-3-37`

An employee on a contract terminable by 3 months' notice is wrongfully dismissed without notice and sues in court. What are his damages usually limited to?

A. His salary until retirement age.
B. The 3 months' notice pay, under the "minimum obligation" rule.
C. Nothing, since he can find another job.
D. $20,000.

**Answer: B.** The employer is assumed to have performed in the least burdensome way, typically by giving contractual notice (*Alexander Proudfoot v Sim Hua Ngee Alvin*; *Wee Kim San v Robinson*). Court claims can exceed the ECA limits and have the usual 6-year limitation. D is the ECT limit.
*Cite: Alexander Proudfoot [1992] 3 SLR(R) 933; Wee Kim San [2014] 4 SLR 357; EM2 s30; `pcp-m-3-37`*

## 4 · PIPD

### 4.I Legal framework and references

Sub-points 4.I.1–4.I.4. No real question; own questions Q4-1 to Q4-4.

### 4.I.1 — Tort: the four elements

**Q4-1** · `4.I.1` · own question · `pcp-m-4-1`

Which is NOT an element the claimant must prove in a negligence claim for a motor accident?

A. A duty of care.
B. Breach of that duty.
C. That the breach caused the damage, and damage.
D. That the defendant intended the harm.

**Answer: D.** Negligence needs duty, breach, causation and damage; intention is irrelevant. Loss must be proved even in a bifurcated trial (*Tan Woo Thian*).
*Cite: PI1 s3; PI4 s8; `pcp-m-4-1`*

### 4.I.2 — Contract and insurance law in PIPD

**Q4-2** · `4.I.2` · own question · `pcp-m-4-2`

Which body of law governs the relationship between a motor insurer and its insured, including the duty of good faith?

A. Tort law.
B. Insurance law.
C. Criminal law.
D. Land law.

**Answer: B.** Insurance law governs insurer and insured; contract law governs the relationships with repairers, owners and hospitals; tort governs the claim against the wrongdoer. Acting for an insurer, you advise on its rights against the policyholder and third parties.
*Cite: PI1 s4–5; PI-LP p2; `pcp-m-4-2`*

### 4.I.3 — PIPD reference works

**Q4-3** · `4.I.3` · own question · `pcp-m-4-3`

Which reference gives the multipliers for valuing future loss of earnings?

A. The Motor Accident Guide.
B. The Actuarial Tables with Explanatory Notes.
C. MACO.
D. BOLA.

**Answer: B.** The Actuarial Tables give multipliers for future losses using mortality data and a yield curve. A: the MAG gives liability scenarios. C: MACO is a tool, not an authority. D: BOLA is the insurers' liability reference. General damages ranges are in the Guidelines (3rd ed).
*Cite: PI1 s6–10; PI2 s7; `pcp-m-4-3`*

### 4.I.4 — Heads of claim and supporting documents

**Q4-4** · `4.I.4` · own question · `pcp-m-4-4`

A claimant seeks a pre-action interim payment. Within what time must the potential defendant reply?

A. 7 days.
B. 14 days, paying any sum offered within 28 days of the reply.
C. 8 weeks.
D. No reply is required.

**Answer: B.** App B para 12: the defendant replies within 14 days and pays any sum offered within 28 days of that reply. The letter of claim must break down damages by head with supporting evidence (medical bills, tax assessments for income loss, repair bills, COE and PARF for write-offs).
*Cite: PI-PD App B paras 3.2, 3.6, 12; `pcp-m-4-4`*

### 4.II At the scene: immediate steps and the GIA Motor Claims Framework

Sub-points 4.II.1–4.II.4. Real questions: SQ PIPD Q8 (4.II.1), Q1 (4.II.2), Q9 (4.II.3). Own question Q4-5 covers 4.II.4.

### 4.II.1 — Immediate steps after a collision

**QSQ-I8** · `4.II.1` · SQ PIPD Q8 [Original], official key D · `pcp-m-4-5`

Your friend, Annette, got into a minor car accident, and has called you for help. She is currently at the accident scene, and the other driver, Victor, refused to give her his contact particulars. Which of the following actions would be most appropriate for Annette to take?

A. She should call an authorised workshop.
B. She should take a photograph of Victor.
C. She should call the police.
D. She should take down Victor's license plate.

**Answer: D.** If the other driver will not give particulars, take down his licence plate number, which identifies the vehicle and its insurer. The course's at-scene steps are: stop, call police/ambulance if needed, exchange particulars, photograph, do not admit fault, tow truck if needed, call the insurer. C is not wrong in itself but is not the most appropriate step for a minor accident; A and B do not identify him. Official key: D.
*Cite: PI2 s3, s6; SQ p88 Q8, key p129; `pcp-m-4-5`*

### 4.II.2 — GIA Motor Claims Framework (MCF)

**QSQ-I1** · `4.II.2` · SQ PIPD Q1 [Part B 2024], official key A · `pcp-m-4-6`

Which of the following forms part of the reporting procedures under the Motor Claims Framework?

A. Bring your vehicle to a reporting centre or authorized workshop within 24 hours.
B. Bring your vehicle to the workshop that is nearest to the place of accident.
C. Bring your vehicle to the nearest neighbourhood police post.
D. Call a tow truck operator to bring your vehicle to a reporting centre or workshop within 24 hours.

**Answer: A.** The MCF's steps are: exchange particulars; call the insurer's hotline for a tow truck; report and take the vehicle to an approved reporting centre or authorised workshop within 24 hours. B: not the nearest workshop, an authorised one. C: not a police post. D: the tow truck comes through the insurer's hotline, and calling one is not the reporting step. Official key: A.
*Cite: PI2 s4–6, s8; SQ p85 Q1, key p129; `pcp-m-4-6`*

### 4.II.3 — Duty to report; consequences of not reporting

**QSQ-I9** · `4.II.3` · SQ PIPD Q9 [Original], official key B · `pcp-m-4-7`

David was involved in a minor motor accident in which no one was injured. The damage to both vehicles appears insignificant, and the other driver proposes that both parties settle the matter privately without notifying their insurers. Which of the following is the MOST APPROPRIATE advice?

A. David may refrain from reporting the accident provided both parties agree to settle the matter privately.
B. David should comply with the reporting requirements under the Motor Claims Framework even if the parties intend to settle the matter privately.
C. David is only required to report the accident if the repair costs exceed S$3,000.
D. David is only required to report the accident if a police report has been made.

**Answer: B.** The accident report must be made whether or not the motorist intends to claim; failing to report lets the insurer disclaim cover, and late reporting may cut the no-claim discount. Report first, decide later. A, C, D invent exceptions. Official key: B.
*Cite: PI2 s8–9; SQ p88 Q9, key p129; `pcp-m-4-7`*

### 4.II.4 — Content of the accident report; police reports

**Q4-5** · `4.II.4` · own question · `pcp-m-4-8`

A driver's passenger is given 2 days' medical leave after a minor collision. Is a police report generally required?

A. Yes, always after any collision.
B. No; it is generally not needed if no one is injured, or the injured person has under 3 days' medical leave, though one may always be made for the record.
C. Only if the repair cost exceeds $3,000.
D. Only if the insurer asks.

**Answer: B.** A police report is generally not needed where no one is injured or the injured person has under 3 days' MC. The accident report should be detailed (date, time, road, weather, speeds, lights, positions, injuries, photos); as the first account it carries high probative weight.
*Cite: PI2 s10–11; `pcp-m-4-8`*

### 4.III At the lawyer's office: claimant's and defendant's options; repudiation; MIB

Sub-points 4.III.1–4.III.4. Real question: SQ PIPD Q2 (4.III.3). Own questions cover the rest.

### 4.III.1 — Advising a claimant

**Q4-6** · `4.III.1` · own question · `pcp-m-4-9`

A not-at-fault claimant wants the quickest, least troublesome repair and does not mind losing his no-claim bonus. Which option suits him?

A. An own damage claim on his own policy.
B. A third-party claim through lawyers.
C. Suing in the District Court.
D. A FIDReC adjudication.

**Answer: A.** An OD claim is fuss-free, since repairers handle it, but he loses his no-claim bonus. B: a third-party claim against the other driver's insurer keeps the NCB but takes longer. C and D are dispute routes, not the simplest option. Private settlement is a further option.
*Cite: PI2 s12–13; `pcp-m-4-9`*

### 4.III.2 — Advising a defendant

**Q4-7** · `4.III.2` · own question · `pcp-m-4-10`

An at-fault driver wants to settle privately to keep his no-claim bonus. What must he be careful about?

A. Nothing; private settlement is always safe.
B. Not to say or sign anything amounting to an admission of fault, which his motor policy usually prohibits.
C. He must first obtain a court order.
D. He must pay through FIDReC.

**Answer: B.** A defendant may settle privately, let his insurer handle it, or defend in person; but an admission of fault breaches the usual policy terms and can let the insurer repudiate. A, C, D are wrong.
*Cite: PI2 s14; `pcp-m-4-10`*

### 4.III.3 — Repudiation by the motor insurer

**QSQ-I2** · `4.III.3` · SQ PIPD Q2 [Part B 2024], official key B · `pcp-m-4-11`

Which of the following factors can give motor insurers the right to refuse insurance cover?

A. Failing to report the accident to a reporting centre or authorized workshop within 24 hours.
B. Driving without a valid driving license.
C. Using a mobile phone while driving.
D. Failing to conform to a red traffic light.

**Answer: B.** Repudiation grounds include driving under the influence, unregistered or illegally modified vehicles, driving without a valid licence, overloading passengers, admitting fault, and failing to notify the insurer of the accident or proceedings. A: late reporting may affect the no-claim discount; it is not a listed repudiation ground (failing to report at all is). C and D: traffic offences are not listed grounds. Official key: B.
*Cite: PI2 s15–18; India International Insurance v Ho Chai Hong Joanne [2013] SGDC 193; SQ p85 Q2, key p129; `pcp-m-4-11`*

### 4.III.4 — Motor Insurers' Bureau (MIB)

**Q4-8** · `4.III.4` · own question · `pcp-m-4-12`

A pedestrian is injured by a hit-and-run driver who is never traced. How may she be compensated?

A. She cannot be.
B. By applying to the MIB directly under the MIB Agreement.
C. By claiming against her own health insurer only.
D. Through FIDReC.

**Answer: B.** Where the defendant is untraced or unknown, apply to the MIB directly; where he is uninsured, the MIB asks his last known insurer (the "insurer concerned") to handle it. A, C, D are wrong.
*Cite: PI4 s20; MVA; `pcp-m-4-12`*

### 4.IV Pre-action protocol for PI and NIMA claims (State Courts PD Appendix B)

Sub-points 4.IV.1–4.IV.7. Real questions: SQ PIPD Q3 (4.IV.1), Q6 (4.IV.2, 4.IV.6), Q7 (4.IV.3), Q5 and Q10 (4.IV.5). Own questions Q4-9 cover 4.IV.4 and Q4-26 covers 4.IV.7 (added 18 Nov 2026).

### 4.IV.1 — Scope of the pre-action protocol

**QSQ-I3** · `4.IV.1` `4.VII.1` · SQ PIPD Q3 [Part B 2024], official key D · `pcp-m-4-13` `pcp-m-4-25`

The Pre-action Protocol for Personal Injury and Non-Injury Motor Accident Cases (2021) does not apply to which of the following claims?

A. Claims arising out of motor accidents and industrial accidents.
B. Claims arising from fatal accidents.
C. Claims where it is contemplated that action will be commenced on or after 1 April 2022.
D. Claims where quantum is quantified in excess of $500,000.

**Answer: D.** Appendix B covers PI claims in the Magistrates' or District Courts, motor and industrial PI claims transferred down from the High Court (up to $500,000 under the 2016 Transfer Order), and NIMA claims; a claim above $500,000 stays in the High Court, where there is no protocol. A, B, C are within its scope (fatal accidents included; actions from 1 Apr 2022). Official key: D.
*Cite: PI-PD App B para 1.2; SQ p86 Q3, key p129; `pcp-m-4-13`, `pcp-m-4-25`*

### 4.IV.2 — NIMA: notice of accident and pre-repair survey

**QSQ-I6** · `4.IV.2` `4.IV.6` · SQ PIPD Q6 [Original], official key C · `pcp-m-4-14` `pcp-m-4-18`

Following a non-injury motor accident, Mei immediately proceeds to send her vehicle for repair. As a result, the potential defendant or his insurer was not able to conduct a pre-repair survey. There was no clear or good reason for Mei to have failed to follow the Pre-action Protocol (Appendix B, State Court's Practice Directions 2021). Which of the following is the MOST LIKELY consequence?

A. Mei's claim for repair costs, if brought, would automatically be dismissed.
B. Mei's claim for repair costs, if brought, can proceed, but the defendant would be relieved of all liability.
C. Mei's claim for repair costs, if brought, can proceed, but the Court may impose costs sanctions against her for non-compliance.
D. Mei is barred from bringing a claim for repair costs against the potential defendant.

**Answer: C.** Non-compliance with the protocol leads to costs sanctions at the court's discretion, not dismissal (paras 14.1, 15.1). A, B, D overstate the consequence. Official key: C.
*Cite: PI-PD App B paras 2, 14, 15; SQ p86 Q6, key p129; `pcp-m-4-14`, `pcp-m-4-18`*

**Q4-25** · `4.IV.2` · own question · `pcp-m-4-14`

Within what time must a NIMA claimant send the notice of accident to each potential defendant and insurer?

A. 24 hours.
B. 3 working days from the accident.
C. 14 days.
D. 8 weeks.

**Answer: B.** App B para 2: notice within 3 working days; the insurer replies within 2 working days listing at least 3 surveyors if it wants a pre-repair survey; silence counts as agreement at each step; the single joint expert completes the survey within 2 working days of appointment. A is the MCF reporting window. C and D are later protocol steps.
*Cite: PI-PD App B para 2; PI3 s7; `pcp-m-4-14`*

### 4.IV.3 — Letter of claim

**QSQ-I7** · `4.IV.3` · SQ PIPD Q7 [Original], official key D · `pcp-m-4-15`

According to the Pre-action Protocol (Appendix B, State Court's Practice Directions 2021), which of the following is NOT required?

A. A list of potential witnesses.
B. The claimant's name.
C. An estimation of damages claimed and provision of the relevant facts.
D. A formal apology from the defendant.

**Answer: D.** The letter of claim sets out the facts, the damage or injuries, an estimate of damages by head, witnesses' names, investigation references and prosecution results (para 3.2). An apology is no part of it. Official key: D.
*Cite: PI-PD App B paras 3.1–3.6; SQ p87 Q7, key p129; `pcp-m-4-15`*

### 4.IV.4 — Potential defendant's response; joint medical experts

**Q4-9** · `4.IV.4` · own question · `pcp-m-4-16`

A potential defendant receives a letter of claim. By when must it send a substantive reply on liability and quantum?

A. Within 14 days.
B. Within 8 weeks of receiving the letter of claim (or 14 days after inspecting the vehicle, if later).
C. Within 6 months.
D. No reply is required.

**Answer: B.** Acknowledge within 14 days (or the claimant may sue without sanction); for Magistrate's Court PI claims, respond on experts within 14 days of acknowledging (silence = agreement; a single joint expert); substantive reply within 8 weeks (para 4.6). A is the acknowledgement period.
*Cite: PI-PD App B paras 4.3–4.6; `pcp-m-4-16`*

### 4.IV.5 — When the claimant may commence proceedings

**QSQ-I5** · `4.IV.5` · SQ PIPD Q5 [Part B 2024], official key C · `pcp-m-4-17`

According to the Pre-action Protocol for Personal Injury and Non-Injury Motor Accident Cases (2021), what is the period of notice that a claimant must give before he can file an action in Court?

A. 3 days.
B. 7 days.
C. 10 days.
D. 14 days.

**Answer: C.** After at least 8 weeks from receipt of the letter of claim with no reasonable prospect of settlement, the claimant gives 10 clear days' notice of intention to sue (para 11.2). Official key: C.
*Cite: PI-PD App B para 11.2; SQ p86 Q5, key p129; `pcp-m-4-17`*

**QSQ-I10** · `4.IV.5` · SQ PIPD Q10 [Original], official key C · `pcp-m-4-17`

Following a non-injury motor accident, Rachel wishes to commence legal proceedings against the other driver. Her solicitor has complied with the requirements of the Pre-action Protocol for Personal Injury and Non-Injury Motor Accident Cases (2021) by serving the necessary documents on the defendant. Before commencing court proceedings, Rachel must generally:

A. obtain the consent of the defendant's insurer.
B. attend mediation arranged by the State Courts.
C. allow the prescribed notice period under the Pre-action Protocol to expire.
D. obtain a police report confirming that the defendant was at fault.

**Answer: C.** The claimant must let the 10 clear days' notice period expire (para 11.2), unless she had already said an offer was final. A, B, D are not pre-conditions (CDR happens after filing in the State Courts). Official key: C.
*Cite: PI-PD App B para 11.2; SQ p89 Q10, key p129; `pcp-m-4-17`*

### 4.IV.6 — Non-compliance: sanctions and costs guidelines

See also QSQ-I6 under 4.IV.2.

**Q4-10** · `4.IV.6` · own question · `pcp-m-4-18`

A NIMA claim settles before action for $5,000. What pre-action costs do the guidelines suggest?

A. $300.
B. $300–$700.
C. $500–$1,000.
D. $1,500–$2,500.

**Answer: B.** Para 13: NIMA under $1,000 → $300; $1,000–$9,999 → $300–$700; $10,000 and above → $500–$1,000; PI settled under $20,000 → $1,500–$2,500. No sanctions are imposed where there are good reasons, e.g. trying another ADR forum (para 15.1).
*Cite: PI-PD App B paras 13–15; `pcp-m-4-18`*

### 4.IV.7 — State Courts PD 2014: Appendix C (NIMA) and Appendix E (PI)

**Q4-26** · `4.IV.7` · own question · `pcp-m-4-34`

A non-injury motor accident claim is governed by the Pre-action Protocol for Non-Injury Motor Accident Cases in Appendix C of the State Courts Practice Directions 2014. The claimant has sent his notice of accident. How many motor surveyors must the insurer list in its reply if it wants a pre-repair survey, and how is the PD 2014 framework related to the current one?

A. At least 3; the 2014 protocol is identical to the 2021 one.
B. At least 10; the 2021 PD later merged the NIMA protocol (2014 App C) and the PI protocol (2014 App E) into a single Appendix B.
C. None; under PD 2014 the claimant chose the surveyor alone.
D. At least 10; PD 2014 had one combined protocol, which PD 2021 split into two.

**Answer: B.** Under 2014 App C para 2.3 the insurer replies within 2 working days with at least 10 motor surveyors; the 2021 Appendix B (actions contemplated from 1 Apr 2022) needs at least 3 and combines the PI and NIMA protocols. A gets the number wrong. C: the surveyor is a single joint expert chosen by agreement or deemed agreement. D reverses the history.
*Cite: PI-PD2014 App C para 2.3, App E; PI-PD App B paras 1.2, 2; `pcp-m-4-34`*

### 4.V FIDReC Non-Injury Motor Accident scheme

Sub-points 4.V.1–4.V.3. No real question; own questions Q4-11 to Q4-13.

### 4.V.1 — FIDReC: claims below $3,000

**Q4-11** · `4.V.1` · own question · `pcp-m-4-19`

An individual's NIMA claim is for $2,400. Where must it be lodged at first instance, and is a FIDReC adjudication binding on him?

A. The Magistrates' Court; yes.
B. FIDReC; the adjudication binds only the financial institution, so he may still go to court.
C. FIDReC; it binds both parties.
D. The Small Claims Tribunals; no.

**Answer: B.** NIMA claims below $3,000 go to FIDReC first (App B para 17), open to individuals and sole proprietors; mediation is free for the claimant; adjudication fees are $250 + GST for the claimant. An adjudication binds only the institution. A, C, D are wrong.
*Cite: PI-PD App B para 17; PI3 s12–13; `pcp-m-4-19`*

### 4.V.2 — Exceptions to FIDReC

**Q4-12** · `4.V.2` · own question · `pcp-m-4-20`

In which case may a NIMA claimant with a $2,000 claim go directly to court instead of FIDReC?

A. The claimant is an individual.
B. The claimant is a company.
C. The other driver is a private car owner.
D. The claimant prefers court.

**Answer: B.** Para 18 exceptions include a body corporate or partnership claimant, government or diplomatic vehicles, certain counterclaims, insurer repudiation, alleged fraud reported to police, FIDReC delay over 6 months, or another good reason. A, C, D are not exceptions.
*Cite: PI-PD App B para 18; PI3 s14–15; `pcp-m-4-20`*

### 4.V.3 — Bypassing FIDReC: costs, stay and limitation

**Q4-13** · `4.V.3` · own question · `pcp-m-4-21`

A claimant lodged at FIDReC, but the limitation period is about to expire. What can he do?

A. Nothing; FIDReC stops time running.
B. Sue to protect against the time bar; the court may stay the action pending FIDReC.
C. He loses the claim.
D. Ask FIDReC to extend limitation.

**Answer: B.** Lodging at FIDReC does not stop limitation, so he may sue protectively and the court may stay (para 20). A claimant who wrongly bypasses FIDReC risks costs consequences, e.g. if his judgment is no better than the FIDReC award (para 19). A, C, D are wrong.
*Cite: PI-PD App B paras 19–20; PI3 s15; `pcp-m-4-21`*

### 4.VI Other pre-writ issues: multiple collisions, limitation, one action

Sub-points 4.VI.1–4.VI.3. Real question: SQ PIPD Q4 (4.VI.1). Own questions Q4-14, Q4-15.

### 4.VI.1 — Multiple (chain) collisions

**QSQ-I4** · `4.VI.1` · SQ PIPD Q4 [Part B 2024], official key A · `pcp-m-4-22`

Regarding a property damage (PD) claim or a non-injury motor accident case (NIMA) case involving 3 vehicles or more, which of the following statements is true under the market agreement between motor insurers or under Barometer of Liability Agreement (BOLA)?

A. The motor insurers of the vehicle directly behind the claimant's car will settle or manage the claim.
B. The insurers of the motorist who is most at fault must settle or manage the claim.
C. All the vehicles' insurers should be responsible for handling the claim.
D. The insurers of the last vehicle must settle or handle the claim.

**Answer: A.** By the market agreement, the insurer of the vehicle directly behind the claimant pays and settles the NIMA claim, without seeking contribution from those further behind; the agreement binds insurers, not claimants. B, C, D misstate it. Official key: A.
*Cite: PI3 s16; Cyril-PI; SQ p86 Q4, key p129; `pcp-m-4-22`*

### 4.VI.2 — Limitation periods (Limitation Act s 24A)

**Q4-14** · `4.VI.2` · own question · `pcp-m-4-23`

What are the limitation periods for a personal injury claim and for a vehicle-damage (NIMA) claim arising from a road accident?

A. 6 years for both.
B. 3 years (PI) and 6 years (NIMA), each subject to the date-of-knowledge rule.
C. 3 years for both.
D. 1 year (PI) and 3 years (NIMA).

**Answer: B.** s 24A(2) LA: PI, 3 years from accrual or date of knowledge if later; s 24A(3): other damage, 6 years from accrual or 3 years from knowledge if later. A, C, D are wrong. (1 year is the WICA claim period.)
*Cite: Limitation Act s 24A(2)–(3); PI3 s16; `pcp-m-4-23`*

### 4.VI.3 — One accident, one action (Ng Koon Choon)

**Q4-15** · `4.VI.3` · own question · `pcp-m-4-24`

After one accident, a claimant files separate suits for vehicle repairs, personal injury and his insurance excess. Which is CORRECT?

A. That is permitted, since the claims are different.
B. There is one cause of action; all claims must be brought in a single action (*Ng Koon Choon v Tang Wee Goh*).
C. Only the PI claim may proceed.
D. Each suit must be filed in a different court.

**Answer: B.** One accident gives one cause of action with different reliefs, so splitting it into several suits is not allowed (*Ng Koon Choon* [2016] 3 SLR 935). A, C, D are wrong.
*Cite: Ng Koon Choon v Tang Wee Goh [2016] 3 SLR 935; PI3 s17; `pcp-m-4-24`*

### 4.VII Where to sue and how the courts manage PIPD cases

Sub-points 4.VII.1–4.VII.4. Real question: SQ PIPD Q3 (under 4.IV.1, also 4.VII.1). Own questions Q4-16 to Q4-19.

### 4.VII.1 — Deciding where to sue; the 2016 Transfer Order

**Q4-16** · `4.VII.1` · own question · `pcp-m-4-25`

A road-accident personal injury claim is valued at $380,000. Where is it filed and heard?

A. Filed and heard in the District Court.
B. Filed in the High Court and transferred automatically to the District Court under the 2016 Transfer Order.
C. Filed and heard in the High Court.
D. Filed in the Magistrate's Court.

**Answer: B.** Road accident and industrial accident PI actions not exceeding $500,000 started in the High Court are transferred automatically to the District Court, which then has jurisdiction beyond its ordinary $250,000 limit. A: above $250,000 it cannot be filed there directly. C: it is transferred down. D: the Magistrate's limit is $60,000.
*Cite: SCJ (Transfer of Specified Proceedings to District Court) Order 2016 paras 2A, 3; SCA s 2; PI4 s4; `pcp-m-4-25`*

### 4.VII.2 — High Court and State Courts case management

**Q4-17** · `4.VII.2` · own question · `pcp-m-4-26`

Which is a feature of State Courts case management of PIPD claims?

A. No court-assisted settlement.
B. Mandatory Court Dispute Resolution with an early neutral evaluation of fault, and after liability, ADCDR with an indicated figure by head of damage.
C. Assessment of damages always by a High Court judge.
D. CDR fees of $5,000.

**Answer: B.** State Courts: mandatory CDR (often asynchronous) with a percentage evaluation of fault, then ADCDR with a Quantum Indication Form; both free. A describes the High Court (no court indication; consider mediation). C and D are wrong (High Court AD under $1m is by an Assistant Registrar).
*Cite: State Courts PD 2021 App C; PI4 s5–6; `pcp-m-4-26`*

### 4.VII.3 — Enhanced jurisdiction by memorandum (s 23 SCA)

**Q4-18** · `4.VII.3` · own question · `pcp-m-4-27`

During a District Court PI case, the claimant's complications push the claim above the District Court limit. How can the case stay in the District Court?

A. It cannot; it must be transferred to the High Court.
B. The parties sign a memorandum giving the District Court jurisdiction despite the excess (s 23 SCA).
C. The claimant abandons the excess automatically.
D. The judge extends jurisdiction on his own motion.

**Answer: B.** s 23 State Courts Act: by memorandum signed by the parties or their lawyers, the District Court has jurisdiction although the claim exceeds its limit; High Court parties can use this to move down and use CDR/ADCDR. A, C, D are wrong.
*Cite: SCA s 23; PI4 s7; `pcp-m-4-27`*

### 4.VII.4 — Single joint experts

**Q4-19** · `4.VII.4` · own question · `pcp-m-4-28`

Under O 12 r 3 ROC 2021, what is the rule on experts in the High Court?

A. Each party may call as many experts as it likes.
B. The parties must agree one common expert and may not rely on more than one expert per issue.
C. The court always appoints the expert.
D. No experts are allowed in PI cases.

**Answer: B.** Parties should have one common expert; in the High Court they must agree one and may not rely on more than one per issue; in State Courts simplified trials, if they cannot agree, the court may appoint one. The protocol also uses SJEs pre-action (surveyors, medical experts).
*Cite: ROC 2021 O 12 r 3; PI4 s14; `pcp-m-4-28`*

**Q4-27** · `4.VII.4` · own question · `pcp-m-4-28`

In a NIMA claim heading for a simplified trial, the parties cannot agree on a single joint expert. Each has a nominee. Which factor is LEAST relevant when the court chooses (per *Lee Song Yam v Hafizah*)?

A. Whether the proposed surveyor did the pre-repair and post-repair inspection of the vehicle.
B. The experts' fees and the time they need to produce a report.
C. Whether either party breached the pre-action protocol in a way that affects the choice.
D. Which party first proposed its nominee.

**Answer: D.** The court weighs expertise and experience, costs, time to report, (NIMA) whether the expert inspected the vehicle before and after repair, (PIMA) whether the doctor is from a restructured hospital and examined the patient or records, protocol breaches, and allegations of claim inflation, causation, fraud or bias. If no nominee is suitable, it appoints its own. Who proposed first is not a factor.
*Cite: Lee Song Yam v Hafizah binte Abdul Rahman [2019] SGMC 24; Cyril-PI; `pcp-m-4-28`*

### 4.VIII Trials and assessment of damages

Sub-points 4.VIII.1–4.VIII.2. No real question; own questions Q4-20, Q4-21.

### 4.VIII.1 — Proving loss (Tan Woo Thian)

**Q4-20** · `4.VIII.1` · own question · `pcp-m-4-29`

In a bifurcated trial, a claimant proves duty and breach at the liability stage but offers no evidence of loss, intending to prove it at assessment. What happened in *Tan Woo Thian v PwC Advisory Services*?

A. Interlocutory judgment was entered and damages assessed later.
B. The claim was dismissed for want of proof of loss, since loss is an element of negligence that bifurcation does not excuse.
C. Nominal damages were awarded.
D. The trial was adjourned.

**Answer: B.** *Tan Woo Thian* [2021] 1 SLR 1166: the claim failed for want of proof of loss at the liability stage. Since then insurers' lawyers commonly reserve causation in consent interlocutory judgments.
*Cite: Tan Woo Thian [2021] 1 SLR 1166; PI4 s8–9; `pcp-m-4-29`*

### 4.VIII.2 — Consent interlocutory judgment reserving causation (Salmizan; Crapper)

**Q4-21** · `4.VIII.2` · own question · `pcp-m-4-30`

Can parties enter a consent interlocutory judgment that leaves causation of disputed injuries to the assessment of damages?

A. No; the High Court in *Salmizan v Crapper* held causation must be decided at liability, and that remains the law.
B. Yes; the Court of Appeal in *Crapper v Salmizan* [2024] SGCA 21 held parties may consent to interlocutory judgment reserving causation.
C. Only in the High Court.
D. Only if the defendant admits all injuries.

**Answer: B.** The Court of Appeal reversed the High Court: a judgment on duty and breach alone is a proper issue-based judgment, and causation may be reserved to the registrar assessing damages. A states the overruled High Court position. C and D are wrong.
*Cite: Crapper v Salmizan [2024] SGCA 21; Salmizan v Crapper [2023] SGHC 75; PI4 s10–13; `pcp-m-4-30`*

### 4.IX Post-judgment and other matters: Public Trustee, insurers, work injury

Sub-points 4.IX.1–4.IX.3. No real question; own questions Q4-22 to Q4-24.

### 4.IX.1 — Usual consequential orders and the Public Trustee

**Q4-22** · `4.IX.1` · own question · `pcp-m-4-31`

A motor accident PI claim settles for $40,000 plus costs. How are the settlement sum and the claimant's solicitor's costs paid?

A. The whole sum to the solicitor, who deducts his fees.
B. The settlement sum directly to the claimant; only the costs (agreed with or determined by the Public Trustee, or assessed) to the solicitor, by separate cheques.
C. Everything through the court.
D. The solicitor may agree any fee with the client.

**Answer: B.** Under s 18 MVA, where the sum (excluding costs and interest) exceeds the $5,000 "relevant amount", the lawyer may receive only costs agreed with the Public Trustee, assessed costs, or costs it determines if assessment is not begun within 3 months; the insurer pays two cheques (Public Trustee Circular 1 of 2014). D: other agreements are void and breach is an offence (s 18(7)–(8)).
*Cite: MVA ss 2, 18(3), (5), (7), (8); PI4 s15–17; `pcp-m-4-31`*

### 4.IX.2 — Intervention by insurers

**Q4-23** · `4.IX.2` · own question · `pcp-m-4-32`

An insurer has repudiated cover because its insured drove drunk, but it may still have to satisfy a judgment for the third party. What does it commonly do?

A. Nothing until judgment.
B. Apply for the court's permission to intervene and take part in the claim.
C. Sue the third party.
D. Refer the matter to FIDReC.

**Answer: B.** Its financial interest is affected, so the insurer commonly applies to intervene under the Rules of Court. A, C, D are wrong.
*Cite: PI4 s18; `pcp-m-4-32`*

### 4.IX.3 — Work injury: WICA or common law

**Q4-24** · `4.IX.3` · own question · `pcp-m-4-33`

A workman is injured in an industrial accident in the course of his employment. What are his routes to compensation?

A. Only a WICA claim.
B. A WICA claim, or a common law action against the employer in court.
C. Only a common law action.
D. A claim in the Employment Claims Tribunal.

**Answer: B.** He may claim under WICA or sue at common law; in the State Courts, CDR has special provisions for these cases. D: the ECT cannot hear work injury compensation claims.
*Cite: PI4 s19; WICA; `pcp-m-4-33`, see `pcp-m-3-13`*

---

# Part 2 — Drills

Timed sets built only from Part 1 questions; find each by its ID (Ctrl-F the ID). Sit the set closed-book first, then check against the answer key and the explanation in Part 1, and log every miss in `weak-spots.md` under its Key. **Time limits** allow 75 seconds per MCQ, rounded up to the next 5 minutes. That is this file's own pacing assumption, not an exam figure: the number of questions on the PCP Paper 2 is not held (the 2023 and 2025 papers show only that the Real Estate block ran to about 20 questions, Qs 26–44 in 2023 and Qs 21–40 in 2025). Drills 1–11 run by Topic; Drills 12–14 are mixed. Drill 15 holds the written practice-paper and 2021 REP parts, which have marking points instead of a letter key.

| Drill | Covers | Questions | Time |
|---|---|---|---|
| 1 | Probate: wills, gifts and executors (0.I–0.IV) | 39 | 50 min |
| 2 | Probate: intestacy, testate v intestate, IFPA (0.V–0.VII) | 18 | 25 min |
| 3 | Probate: grants of representation (0.VIII) | 20 | 25 min |
| 4 | Probate: Mental Capacity Act (0.IX) | 17 | 25 min |
| 5 | Real Estate: parties, searches, OTP, caveats (1.I–1.III) | 23 | 30 min |
| 6 | Real Estate: stamp duties and foreign ownership (1.IV–1.V) | 13 | 20 min |
| 7 | Real Estate: sale, mortgages, CPF, completion (1.VI–1.IX) | 22 | 30 min |
| 8 | Muslim Family & Succession Law: jurisdiction and divorce (2.I–2.IV) | 23 | 30 min |
| 9 | Muslim Family & Succession Law: ancillaries, enforcement, inheritance (2.V–2.IX) | 25 | 35 min |
| 10 | Employment Law: all Topics (3.I–3.VIII) | 40 | 50 min |
| 11 | PIPD: all Topics (4.I–4.IX) | 35 | 45 min |
| 12 | Mixed mock: all 50 Sample Questions, official key | 50 | 65 min |
| 13 | Mixed mock: the practice-paper and real-facts MCQs | 14 | 20 min |
| 14 | Mixed mock: 50 own questions across all five Subjects | 50 | 65 min |
| 15 | Written parts: Probate practice papers and 2021 REP (short model answers) | 12 | 60 min |

### Drill 1 — Probate: wills, gifts and executors (0.I–0.IV) · 39 questions · 50 minutes

**Questions:** Q0-1, Q0-2, Q0-3, Q0-4, Q0-5, Q0-6, Q0-7, Q0-8, Q0-9, Q0-10, Q0-11, Q0-12, Q0-13, QSQ-P5, QPP1-2, Q0-14, Q0-15, Q0-16, Q0-17, Q0-18, Q0-19, Q0-20, Q0-21, QPP1-3, QPP1-4, Q0-22, Q0-23, Q0-24, Q0-25, Q0-26, Q0-27, Q0-28, Q0-29, Q0-30, QSQ-P3, Q0-31, Q0-32, Q0-33, Q0-34.

**Answer key:** Q0-1 D · Q0-2 D · Q0-3 C · Q0-4 B · Q0-5 B · Q0-6 C · Q0-7 C · Q0-8 A · Q0-9 B · Q0-10 B · Q0-11 C · Q0-12 B · Q0-13 C · QSQ-P5 D · QPP1-2 c only · Q0-14 B · Q0-15 B · Q0-16 B · Q0-17 B · Q0-18 C · Q0-19 B · Q0-20 B · Q0-21 C · QPP1-3 a only · QPP1-4 d (the only wrong statement) · Q0-22 B · Q0-23 C · Q0-24 C · Q0-25 B · Q0-26 B · Q0-27 B · Q0-28 B · Q0-29 B · Q0-30 C · QSQ-P3 A · Q0-31 B · Q0-32 B · Q0-33 B · Q0-34 B.

### Drill 2 — Probate: intestacy, testate v intestate, IFPA (0.V–0.VII) · 18 questions · 25 minutes

**Questions:** Q0-35, Q0-36, Q0-37, Q0-38, Q0-39, Q0-40, Q0-41, Q0-42, QSQ-P2, QSQ-P4, Q0-43, Q0-44, Q0-45, Q0-46, Q0-47, Q0-48, Q0-49, Q0-50.

**Answer key:** Q0-35 B · Q0-36 B · Q0-37 B · Q0-38 C · Q0-39 B · Q0-40 B · Q0-41 A · Q0-42 C · QSQ-P2 B · QSQ-P4 D · Q0-43 B · Q0-44 C · Q0-45 B · Q0-46 B · Q0-47 B · Q0-48 B · Q0-49 B · Q0-50 B.

### Drill 3 — Probate: grants of representation (0.VIII) · 20 questions · 25 minutes

**Questions:** Q0-51, Q0-52, Q0-53, Q0-54, Q0-55, QSQ-P6, QPP1-6, QSQ-P7, Q0-56, Q0-57, QSQ-P1, QPP1-5, Q0-58, Q0-59, Q0-60, Q0-61, Q0-62, Q0-63, QSQ-P8, Q0-64.

**Answer key:** Q0-51 B · Q0-52 C · Q0-53 B · Q0-54 B · Q0-55 B · QSQ-P6 B · QPP1-6 A · QSQ-P7 B · Q0-56 B · Q0-57 B · QSQ-P1 C · QPP1-5 A · Q0-58 A · Q0-59 D · Q0-60 A · Q0-61 B · Q0-62 B · Q0-63 B · QSQ-P8 A · Q0-64 B.

### Drill 4 — Probate: Mental Capacity Act (0.IX) · 17 questions · 25 minutes

**Questions:** Q0-65, Q0-66, Q0-67, Q0-68, Q0-69, Q0-70, Q0-71, Q0-72, Q0-73, QSQ-P9, QPP2-2, Q0-74, Q0-75, QPP2-4, Q0-76, QSQ-P10, Q0-77.

**Answer key:** Q0-65 B · Q0-66 B · Q0-67 B · Q0-68 B · Q0-69 B · Q0-70 C · Q0-71 B · Q0-72 B · Q0-73 C · QSQ-P9 A · QPP2-2 B · Q0-74 B · Q0-75 B · QPP2-4 D · Q0-76 B · QSQ-P10 C (official key D) · Q0-77 B.

### Drill 5 — Real Estate: parties, searches, OTP, caveats (1.I–1.III) · 23 questions · 30 minutes

**Questions:** Q1-1, Q1-2, Q1-3, Q1-4, Q1-5, Q1-6, QSQ-R9, Q1-25F1, Q1-7, Q1-8, Q1-9, Q1-10, Q1-11, QSQ-R3, QSQ-R4, Q1-12, Q1-13, Q1-25F2, QSQ-R10, Q1-14, Q1-25F3, Q1-15, QSQ-R6.

**Answer key:** Q1-1 C · Q1-2 C · Q1-3 B · Q1-4 B · Q1-5 C · Q1-6 B · QSQ-R9 C · Q1-25F1 B · Q1-7 B · Q1-8 B · Q1-9 B · Q1-10 C · Q1-11 B · QSQ-R3 B · QSQ-R4 B · Q1-12 B · Q1-13 B · Q1-25F2 B · QSQ-R10 A · Q1-14 B · Q1-25F3 B · Q1-15 B · QSQ-R6 B.

### Drill 6 — Real Estate: stamp duties and foreign ownership (1.IV–1.V) · 13 questions · 20 minutes

**Questions:** QSQ-R5, Q1-23F1, QSQ-R1, Q1-23F2, Q1-16, Q1-17, Q1-25F4, Q1-23F3, Q1-18, Q1-19, Q1-20, QSQ-R2, Q1-21.

**Answer key:** QSQ-R5 A · Q1-23F1 B · QSQ-R1 D · Q1-23F2 B · Q1-16 B · Q1-17 B · Q1-25F4 C · Q1-23F3 B · Q1-18 C · Q1-19 C · Q1-20 B · QSQ-R2 C · Q1-21 B.

### Drill 7 — Real Estate: sale, mortgages, CPF, completion (1.VI–1.IX) · 22 questions · 30 minutes

**Questions:** Q1-22, Q1-23, Q1-24, Q1-25, Q1-26, Q1-27, Q1-28, Q1-29, Q1-30, QSQ-R7, Q1-31, Q1-32, Q1-33, Q1-34, Q1-35, Q1-36, Q1-37, Q1-38, Q1-39, Q1-40, Q1-41, QSQ-R8.

**Answer key:** Q1-22 B · Q1-23 B · Q1-24 B · Q1-25 B · Q1-26 B · Q1-27 B · Q1-28 B · Q1-29 B · Q1-30 B · QSQ-R7 C · Q1-31 B · Q1-32 C · Q1-33 B · Q1-34 B · Q1-35 B · Q1-36 B · Q1-37 C · Q1-38 B · Q1-39 B · Q1-40 B · Q1-41 B · QSQ-R8 B.

### Drill 8 — Muslim Family & Succession Law: jurisdiction and divorce (2.I–2.IV) · 23 questions · 30 minutes

**Questions:** Q2-1, Q2-2, Q2-3, Q2-4, Q2-5, Q2-6, QSQ-M6, QSQ-M8, Q2-7, QSQ-M2, QSQ-M4, Q2-8, Q2-9, Q2-10, Q2-11, Q2-12, QSQ-M1, Q2-13, Q2-14, Q2-15, Q2-16, QSQ-M7, Q2-17.

**Answer key:** Q2-1 B · Q2-2 B · Q2-3 B · Q2-4 B · Q2-5 B · Q2-6 D · QSQ-M6 D · QSQ-M8 A · Q2-7 C · QSQ-M2 D · QSQ-M4 B · Q2-8 B · Q2-9 D · Q2-10 B · Q2-11 C · Q2-12 B · QSQ-M1 D · Q2-13 B · Q2-14 B · Q2-15 A · Q2-16 B · QSQ-M7 D · Q2-17 B.

### Drill 9 — Muslim Family & Succession Law: ancillaries, enforcement, inheritance (2.V–2.IX) · 25 questions · 35 minutes

**Questions:** Q2-18, Q2-19, Q2-20, Q2-21, QSQ-M5, QSQ-M10, Q2-22, QSQ-M3, QSQ-M9, Q2-23, Q2-24, Q2-25, Q2-26, Q2-27, Q2-28, Q2-29, Q2-30, Q2-31, Q2-32, Q2-33, Q2-34, Q2-35, Q2-36, Q2-37, Q2-38.

**Answer key:** Q2-18 B · Q2-19 B · Q2-20 C · Q2-21 B · QSQ-M5 B · QSQ-M10 B · Q2-22 B · QSQ-M3 C · QSQ-M9 D · Q2-23 B · Q2-24 B · Q2-25 B · Q2-26 B · Q2-27 B · Q2-28 B · Q2-29 B · Q2-30 B · Q2-31 A · Q2-32 B · Q2-33 B · Q2-34 B · Q2-35 B · Q2-36 B · Q2-37 B · Q2-38 B.

### Drill 10 — Employment Law: all Topics (3.I–3.VIII) · 40 questions · 50 minutes

**Questions:** Q3-1, Q3-2, Q3-3, QSQ-E1, Q3-4, Q3-5, Q3-6, Q3-7, Q3-8, QSQ-E6, QSQ-E3, Q3-9, Q3-10, Q3-11, Q3-12, Q3-13, Q3-14, Q3-15, Q3-16, Q3-17, Q3-18, Q3-19, Q3-20, Q3-21, Q3-22, Q3-23, QSQ-E2, Q3-24, Q3-25, Q3-26, QSQ-E5, Q3-27, QSQ-E8, QSQ-E10, Q3-28, QSQ-E4, Q3-29, QSQ-E7, QSQ-E9, Q3-30.

**Answer key:** Q3-1 B · Q3-2 D · Q3-3 C · QSQ-E1 D · Q3-4 B · Q3-5 B · Q3-6 B · Q3-7 B · Q3-8 C · QSQ-E6 C · QSQ-E3 D · Q3-9 C · Q3-10 B · Q3-11 C · Q3-12 B · Q3-13 B · Q3-14 B · Q3-15 A · Q3-16 B · Q3-17 B · Q3-18 B · Q3-19 B · Q3-20 B · Q3-21 C · Q3-22 B · Q3-23 B · QSQ-E2 C · Q3-24 B · Q3-25 B · Q3-26 B · QSQ-E5 D · Q3-27 B · QSQ-E8 A · QSQ-E10 C · Q3-28 B · QSQ-E4 B · Q3-29 B · QSQ-E7 C · QSQ-E9 B · Q3-30 B.

### Drill 11 — PIPD: all Topics (4.I–4.IX) · 35 questions · 45 minutes

**Questions:** Q4-1, Q4-2, Q4-3, Q4-4, QSQ-I8, QSQ-I1, QSQ-I9, Q4-5, Q4-6, Q4-7, QSQ-I2, Q4-8, QSQ-I3, QSQ-I6, Q4-25, QSQ-I7, Q4-9, QSQ-I5, QSQ-I10, Q4-10, Q4-11, Q4-12, Q4-13, QSQ-I4, Q4-14, Q4-15, Q4-16, Q4-17, Q4-18, Q4-19, Q4-20, Q4-21, Q4-22, Q4-23, Q4-24.

**Answer key:** Q4-1 D · Q4-2 B · Q4-3 B · Q4-4 B · QSQ-I8 D · QSQ-I1 A · QSQ-I9 B · Q4-5 B · Q4-6 A · Q4-7 B · QSQ-I2 B · Q4-8 B · QSQ-I3 D · QSQ-I6 C · Q4-25 B · QSQ-I7 D · Q4-9 B · QSQ-I5 C · QSQ-I10 C · Q4-10 B · Q4-11 B · Q4-12 B · Q4-13 B · QSQ-I4 A · Q4-14 B · Q4-15 B · Q4-16 B · Q4-17 B · Q4-18 B · Q4-19 B · Q4-20 B · Q4-21 B · Q4-22 B · Q4-23 B · Q4-24 B.

### Drill 12 — Mixed mock: all 50 Sample Questions, official key · 50 questions · 65 minutes

**Questions:** QSQ-P5, QSQ-P3, QSQ-P2, QSQ-P4, QSQ-P6, QSQ-P7, QSQ-P1, QSQ-P8, QSQ-P9, QSQ-P10, QSQ-R9, QSQ-R3, QSQ-R4, QSQ-R10, QSQ-R6, QSQ-R5, QSQ-R1, QSQ-R2, QSQ-R7, QSQ-R8, QSQ-M6, QSQ-M8, QSQ-M2, QSQ-M4, QSQ-M1, QSQ-M7, QSQ-M5, QSQ-M10, QSQ-M3, QSQ-M9, QSQ-E1, QSQ-E6, QSQ-E3, QSQ-E2, QSQ-E5, QSQ-E8, QSQ-E10, QSQ-E4, QSQ-E7, QSQ-E9, QSQ-I8, QSQ-I1, QSQ-I9, QSQ-I2, QSQ-I3, QSQ-I6, QSQ-I7, QSQ-I5, QSQ-I10, QSQ-I4.

**Answer key:** QSQ-P5 D · QSQ-P3 A · QSQ-P2 B · QSQ-P4 D · QSQ-P6 B · QSQ-P7 B · QSQ-P1 C · QSQ-P8 A · QSQ-P9 A · QSQ-P10 C (official key D) · QSQ-R9 C · QSQ-R3 B · QSQ-R4 B · QSQ-R10 A · QSQ-R6 B · QSQ-R5 A · QSQ-R1 D · QSQ-R2 C · QSQ-R7 C · QSQ-R8 B · QSQ-M6 D · QSQ-M8 A · QSQ-M2 D · QSQ-M4 B · QSQ-M1 D · QSQ-M7 D · QSQ-M5 B · QSQ-M10 B · QSQ-M3 C · QSQ-M9 D · QSQ-E1 D · QSQ-E6 C · QSQ-E3 D · QSQ-E2 C · QSQ-E5 D · QSQ-E8 A · QSQ-E10 C · QSQ-E4 B · QSQ-E7 C · QSQ-E9 B · QSQ-I8 D · QSQ-I1 A · QSQ-I9 B · QSQ-I2 B · QSQ-I3 D · QSQ-I6 C · QSQ-I7 D · QSQ-I5 C · QSQ-I10 C · QSQ-I4 A.

### Drill 13 — Mixed mock: the practice-paper and real-facts MCQs · 14 questions · 20 minutes

**Questions:** QPP1-2, QPP1-3, QPP1-4, QPP1-6, QPP1-5, QPP2-2, QPP2-4, Q1-25F1, Q1-25F2, Q1-25F3, Q1-23F1, Q1-23F2, Q1-25F4, Q1-23F3.

**Answer key:** QPP1-2 c only · QPP1-3 a only · QPP1-4 d (the only wrong statement) · QPP1-6 A · QPP1-5 A · QPP2-2 B · QPP2-4 D · Q1-25F1 B · Q1-25F2 B · Q1-25F3 B · Q1-23F1 B · Q1-23F2 B · Q1-25F4 C · Q1-23F3 B.

### Drill 14 — Mixed mock: 50 own questions across all five Subjects · 50 questions · 65 minutes

**Questions:** Q0-1, Q0-8, Q0-15, Q0-22, Q0-29, Q0-36, Q0-43, Q0-50, Q0-57, Q0-64, Q1-1, Q1-5, Q1-9, Q1-13, Q1-17, Q1-21, Q1-25, Q1-29, Q1-33, Q1-37, Q2-1, Q2-4, Q2-7, Q2-10, Q2-13, Q2-16, Q2-19, Q2-22, Q2-25, Q2-28, Q3-1, Q3-4, Q3-7, Q3-10, Q3-13, Q3-16, Q3-19, Q3-22, Q3-25, Q3-28, Q4-1, Q4-3, Q4-5, Q4-7, Q4-25, Q4-10, Q4-12, Q4-14, Q4-16, Q4-18.

**Answer key:** Q0-1 D · Q0-8 A · Q0-15 B · Q0-22 B · Q0-29 B · Q0-36 B · Q0-43 B · Q0-50 B · Q0-57 B · Q0-64 B · Q1-1 C · Q1-5 C · Q1-9 B · Q1-13 B · Q1-17 B · Q1-21 B · Q1-25 B · Q1-29 B · Q1-33 B · Q1-37 C · Q2-1 B · Q2-4 B · Q2-7 C · Q2-10 B · Q2-13 B · Q2-16 B · Q2-19 B · Q2-22 B · Q2-25 B · Q2-28 B · Q3-1 B · Q3-4 B · Q3-7 B · Q3-10 B · Q3-13 B · Q3-16 B · Q3-19 B · Q3-22 B · Q3-25 B · Q3-28 B · Q4-1 D · Q4-3 B · Q4-5 B · Q4-7 B · Q4-25 B · Q4-10 B · Q4-12 B · Q4-14 B · Q4-16 B · Q4-18 B.

### Drill 15 — Written parts: Probate practice papers and 2021 REP · 12 parts · 60 minutes

**Questions:** QPP1-1b, QPP1-1d, QPP1-1a, QPP1-1e, QPP2-1d, QPP2-1a, QPP2-1b, QPP2-1c, Q2021R-1-3-1, Q2021R-2-2, Q2021R-2-4-2, Q2021R-1-5.

**How to mark.** The 2026 paper is MCQ only, so use these to rehearse the issues a fact pattern raises, not to write essays. Spend about 5 minutes per part listing the issues and rules, then compare with the short model answer under each question in Part 1. Score one mark per issue you identified that the model answer names (statute or case, and its application). These have no official answers; the model answers are this project's own, from `cheatsheets.md`.

### Coverage check

Drills 1–11 together use every one of the 275 MCQs in Part 1 once; Drills 12–14 re-use them in mixed order; Drill 15 holds the 12 written parts. So every Sub-point is drilled at least once.
