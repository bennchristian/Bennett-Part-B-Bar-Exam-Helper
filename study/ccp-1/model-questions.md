# CCP-1 — Model Questions and Answers

Paper `ccp-1`, CCP Paper 1 (MCQ), Wed 9 Dec 2026, 2:30–4:30pm, open book. Subjects: 0 Banking & Fundraising · 1 Corporate Governance · 2 Insolvency & Corporate Restructuring · 3 Admiralty. Written 15 Nov 2026 as Markdown only, on Bennett's instruction of 14 Nov; no PDF is built until Phase 2 (`python3 tools/build_pack.py ccp-1 --questions`).

**How the file runs.** *Part 1* holds the questions by Subject → Topic → Sub-point, in `coverage.md` order. Each real question sits under the Sub-point it mainly tests; any other Sub-point it tests is named in its tag line and carries a "See also" line. Where no real question reaches a Sub-point, an own question fills the gap. Every one of the 196 Sub-points has at least one question whose tag line names it. *Part 2* holds the Drills: timed sets built from Part 1 questions, by Topic or mixed, each with a time limit and an answer key.

**How to read a question.** The tag line gives the question ID · the Sub-point Keys it raises (`coverage.md`) · the source · the end-point block(s) in `cheatsheets.md` that hold the rule. The answer follows the options: why the right option is right, why each other option is wrong, then the cite. Cites use the source aliases in `coverage.md` → "Source key" and statute sections (IRDA-2018 = Nic's copy of the Act as gazetted). Cover the answer, answer it, then check; log every miss in `weak-spots.md` under its Key.

**Question IDs.** `QSQ-B<n>`, `QSQ-G<n>`, `QSQ-I<n>`, `QSQ-A<n>` = 2026 Sample Questions, Banking / Corporate Governance / Insolvency / Admiralty question n. `Q23-<n>` = 2023 CCP Paper 1, question n. `Q21I-<n>` = 2021 Insolvency Law and Practice paper, MCQ n. `QADM-<n>` = the sample questions in the 2026 Admiralty lecture slides (ADM2 s16–23), question n. `QADM1-<n>` = the mock exam questions in the 2023 Admiralty live lecture slides (ADM1), question n; `QADM1-M` = the MABEL mock question on ADM1 s6. `Q<subject>-<n>` (e.g. `Q0-12`) = own question n for that Subject.

**Sources.** Real questions come first (RULES source order):

- **SQ** — `Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf`, CCP Paper 1: Banking pp6–12, Corporate Governance pp13–17, Insolvency pp18–22, Admiralty pp43–47, ten MCQs each, with the **official key** at pp114 and 116. Qs 1–5 of Banking, CG and Insolvency are labelled "[Part B 2024]", Qs 6–10 "[Part B 2025 S1]" or "[Original]". Every SQ answer below matches the official key.
- **2023 CCP Paper 1** — `Seniors Notes/Nic_s Part B Package/3. PYP/2023 PYP/CCP Paper 1 missing questions 42, 44, 53.pdf` (Tue 12 Dec 2023; 60 MCQs: Banking Qs 1–18, CG 19–37, Admiralty 38–42, Insolvency 43–60). Phone screenshots of Examplify, transcribed for this file. **No official answers**: some screens show an earlier candidate's selection, which is not a key and is wrong in places (noted where it is). Every answer is this project's own, from `cheatsheets.md` and, where noted, the IRDA text.
- **2021 INS** — `…/3. PYP/2021 PYP/INS 2021 (Section 1)(MCQ).pdf` (Insolvency Law and Practice, Fri 10 Dec 2021, 35 MCQs). Also screenshots with an earlier candidate's selections and notes; no official key. Answered on the law as it is now.
- **ADM2 sample questions** — `Modules/Corporate & Commercial Practice/8. Admiralty /Video Lecture & Slides/2.2026_Basic_Admiralty_Practice.pdf` s15–23 (Bruno Bunkers, MT MANU, Omar Bank). No answers given; answered from `cheatsheets.md`, which already worked them into the blocks.
- **ADM1 mock exam questions** — `…/8. Admiralty /Video Lecture & Slides/1._Admiralty_Live_Lecture .pdf`: the MABEL scenarios (s6, no options; options added here) and seven MCQs on the MT KESPAR collision facts. No answers given; answered from `cheatsheets.md`.

**The law.** Every answer follows `cheatsheets.md`, whose blocks were checked against the course materials and current statutes and rules on 11 Nov 2026 (see `coverage.md`). Where an older question assumed older law, the answer gives the current law and says what changed.

Self-study only: never use this file with a live quiz, the Mock Exam or another assessment (Handbook §7.11).

**Left out.** 2023 Q38 (the options are below the fold on the screenshot), Q42, Q44 and Q53 (not held), Q54 (stem cut off at the top) and these, because the pack cannot settle one answer: 2023 Q23 (turns on the Listing Manual definition of "associated company", which the pack does not hold), Q34 (the interested persons are directors and the CEO of the unlisted associate, not of the issuer, so the intended answer is unclear), Q41 (on the facts given every option reads as true), Q56 (options B and C both state the law correctly); 2021 INS Q1 (directors' duties to creditors) and Q32 (scheme managers' duties), which are outside the course materials the pack uses, and Q34 (s 440 and an aircraft maintenance contract after a creditors' voluntary winding up: options B and C both lead to "can terminate"). The written 2021 Advanced Corporate Practice paper (board composition under the pre-2023 two-tier vote) and 2021 INS Q36 (a five-question client checklist) are not reproduced.

| Subject | Real questions | Own questions | Total |
|---|---|---|---|
| 0 Banking & Fundraising | 28 (SQ 10; 2023 18) | 37 | 65 |
| 1 Corporate Governance | 27 (SQ 10; 2023 17) | 35 | 62 |
| 2 Insolvency & Corporate Restructuring | 56 (SQ 10; 2023 14; 2021 INS 32) | 39 | 95 |
| 3 Admiralty | 28 (SQ 10; 2023 2; ADM2 8; ADM1 8) | 10 | 38 |
| **Total** | **139** (SQ 40; 2023 51; 2021 INS 32; ADM2 8; ADM1 8) | **121** | **260** |

Part 2 has 14 Drills.

---

# Part 1 — Questions by Topic and Sub-point

## 0 · Banking & Fundraising

### 0.I Corporate finance: why raise funds, equity or debt

Sub-points 0.I.1–0.I.3. Real questions: QSQ-B1, QSQ-B6, Q23-1 (all 0.I.3). Own questions Q0-1, Q0-2.

### 0.I.1 — Why companies raise finance; factors in the choice of finance

**Q0-1** · `0.I.1` · own question · `ccp-1-0-1`

A company's CFO lists the factors the board will weigh in choosing how to finance a new factory. Which of the following is NOT one of the six factors the course gives?

A. The company's credit quality.
B. Tax.
C. The need for flexibility.
D. The nationality of the company's directors.

**Answer: D.** The course lists six factors influencing the choice of finance: credit quality, the company's industry, tax, available sources and market conditions, the need for flexibility, and pricing. A, B and C are on the list; the directors' nationality is not.
*Cite: BF1 s3–4; Cyril-BF §1.1; `ccp-1-0-1`*

### 0.I.2 — Types of finance (equity / debt, private / public); methods of raising debt

**Q0-2** · `0.I.2` · own question · `ccp-1-0-2`

Which pairing of a type of finance with an example is CORRECT?

A. Private equity — an IPO.
B. Public debt — an issue of bonds or notes.
C. Private debt — an offer of shares to existing shareholders.
D. Public equity — a bilateral term loan.

**Answer: B.** Public debt is raised by issuing debt instruments such as notes or bonds. A: an IPO is public equity; private equity is a subscription by private investors such as venture capital. C: an offer of shares to existing shareholders is public equity; private debt is borrowing from banks or other corporates. D: a term loan is private debt.
*Cite: BF1 s5; `ccp-1-0-2`*

### 0.I.3 — Equity v debt: key features (return, maturity, insolvency ranking)

**QSQ-B1** · `0.I.3` · SQ p6 Q1 [Part B 2024], official key A · `ccp-1-0-3`

Your friend owns a company, Part B Course Pte Ltd, and needs more funds. He wants you to invest in ordinary shares in his company. He tells you that, "The shares will be a great investment because as a shareholder you will get annual payouts from the company. When the company does well, you will be able to sell the shares for a profit. If the company goes insolvent – which it won't because it's a great business – you will still get all your money back as a shareholder. It's a no-lose investment." Which set of statements would BEST CORRECT your friend's views?

I. It is incorrect to say that a shareholder gets annual payouts as companies make dividend payments twice a year.
II. It is incorrect to say that a shareholder gets annual payouts as a company may only make dividend payments if it has made profits and any such payments are at the directors' discretion.
III. It is incorrect to say that the shares can be sold for a profit when the company does well as shares are not property that can be sold.
IV. It is incorrect to say that the shares can be sold for a profit when the company does well as there is no market for shares in a private company.
V. It is incorrect to say that a shareholder will get all his money back if the company goes insolvent because when an insolvent company is wound up, the company's assets are used to pay the creditors and the debts owed to them will usually exceed the company's assets.
VI. It is incorrect to say that a shareholder will get all his money back if the company goes insolvent because shareholders are required to pay the company's debts for it on insolvency.

A. II and V.
B. I, IV and V.
C. II and IV.
D. II, III and VI.

**Answer: A.** Dividends are paid only out of profits and at the directors' discretion (II), and on an insolvent winding up the assets go to creditors, whose debts usually exceed them, so shareholders rank last and usually recover nothing (V). I: there is no rule that dividends are paid twice a year. III: shares are property and can be sold. IV: a private company's shares have no ready market, but this was not the keyed correction. VI: shareholders are not liable for the company's debts.
*Cite: BF1 s6; Cyril-BF §1.1; SQ p114 (key A); `ccp-1-0-3`*

**QSQ-B6** · `0.I.3` · SQ p9 Q6 [Part B 2025 S1], official key A · `ccp-1-0-3`

Big Whale LLP is thinking of investing in a promising start-up, either by making a loan for a fixed tenure at a fixed interest rate, or by subscribing for shares. Which combination of statements BEST DESCRIBES the potential effect of each for Big Whale LLP?

I. The loan is a liability while the shares are an asset.
II. For the loan, Big Whale LLP will receive payments at regular intervals or at the end of the loan tenure, while for the shares, Big Whale LLP will only receive payments when the start-up has profits and at the directors' discretion.
III. If the start-up fails, Big Whale LLP will get all of its money back in the liquidation of the start-up in either case.
IV. If the start-up becomes highly profitable, Big Whale LLP will potentially get a large profit on its investments if it subscribes for shares, but Big Whale LLP will be unable to profit additionally from the start-up's success if it gives a loan.

A. II and IV only.
B. I, III and IV only.
C. All of the above.
D. II and III only.

**Answer: A.** A lender is paid interest and repaid on the agreed dates whatever the company's profits (II), but only a shareholder shares in the company's success (IV). I: for the investor both the loan and the shares are assets; the loan is the start-up's liability. III: neither form guarantees full recovery in a liquidation.
*Cite: BF1 s6; Cyril-BF §1.1; SQ p114 (key A); `ccp-1-0-3`*

**Q23-1** · `0.I.3` · 2023 CCP Paper 1 Q1 (no official answer) · `ccp-1-0-3`

Which of these statements best describes the characteristics of a typical equity financing/investment?

A. Accounted for as an asset and carries a potential upside for the investor if the company is highly successful.
B. Accounted for as a liability and the monies invested will still be recoverable if the company is insolvent.
C. Accounted for as an asset and monies invested will be returned by a specified date.
D. Carries a potential upside if the company is highly successful and the monies invested will still be recoverable even if the company is wholly insolvent.

**Answer: A.** For the investor, shares are an asset, and a shareholder can profit from a rise in value if the company does well. B and D: on insolvency shareholders rank last and usually recover nothing. C: share capital is not repaid on a set date; a fixed repayment date is a feature of debt.
*Cite: BF1 s6; Cyril-BF §1.1; `ccp-1-0-3`*

### 0.II Types of bank lending and syndication

Sub-points 0.II.1–0.II.6. Real questions: Q23-2 (0.II.1, 0.II.2), QSQ-B2, Q23-3, Q23-4 (0.II.3), QSQ-B10, Q23-7 (0.II.5). Own questions Q0-3, Q0-4.

### 0.II.1 — Bilateral v syndicated loans

**Q23-2** · `0.II.1` `0.II.2` · 2023 CCP Paper 1 Q2 (no official answer) · `ccp-1-0-4` `ccp-1-0-5`

Which of these best describe the characteristics of a syndicated five-year term loan? Choose all that apply.

I. Several lenders agree to each lend a proportion of the total loan amount to the borrower.
II. Several lenders each enter into unique terms and conditions with the borrower to lend it money.
III. If one of the lenders does not go through with its portion of the loan, the other banks do not have to increase their shares of the loan to cover the lost amount.
IV. The borrower is, in general, required to repay the loan at the end of the five-year term.
V. If the borrower prepays, it can reborrow the sums prepaid.

A. I and IV only.
B. I, II, IV and V only.
C. I, III and IV only.
D. I, II, III and IV only.

**Answer: C.** In a syndicated loan several lenders each lend a share on the same terms under one agreement (I), and their obligations are several, so if one drops out the others need not make up its share (III). A term loan is repaid at the end of its term, in one sum or by instalments (IV). II: the lenders lend on the same terms, not unique ones. V: amounts repaid under a term loan cannot be re-borrowed; that is a revolving facility.
*Cite: BF1 s8–10; RL-Types p2–5; `ccp-1-0-4`, `ccp-1-0-5`*

### 0.II.2 — Term loan, revolving facility, overdraft and other facilities

See Q23-2 under 0.II.1 (term loan: repayment, no re-borrowing).

**Q0-3** · `0.II.2` · own question · `ccp-1-0-5`

A retailer wants a facility it can draw on, repay and draw on again over three years to manage seasonal stock purchases. Which facility fits, and what is its main drawback?

A. A term loan; amounts repaid cannot be re-borrowed.
B. A revolving credit facility; it carries notice periods, drawing limits and high commitment fees.
C. An overdraft; it is always committed for its whole term.
D. A bullet bond; it must be listed on SGX.

**Answer: B.** A revolving credit facility lets the borrower draw, repay and re-draw up to a maximum for almost the whole life of the loan, at the cost of notice periods, minimum and maximum drawing limits and high commitment fees. A: a term loan cannot be re-borrowed, which is why it does not fit. C: an overdraft is usually uncommitted and repayable on demand. D: a bond is not a bank facility.
*Cite: BF1 s10; RL-Types p2–5; `ccp-1-0-5`*

### 0.II.3 — Committed v uncommitted; availability period; commitment fee

**QSQ-B2** · `0.II.3` · SQ p7 Q2 [Part B 2024], official key A · `ccp-1-0-6`

Part B Course Pte Ltd decides to take out a committed five-year term loan. The bank officer tells your friend that a commitment fee is paid to the bank in return for the bank committing to make available the agreed amount of the facility during the availability period, which will be the five-year period of the term loan, and is paid in respect of the amounts that Part B Course Pte Ltd draws down. What corrections would you make to the explanation, if any?

A. The availability period would not be the full five years of the term loan but the shorter period or periods when a draw-down may be made, and the fee is for the committed undrawn amounts, not the amounts drawn down.
B. No corrections are needed. The bank officer's explanation is wholly correct.
C. The commitment fee is paid to the bank in return for the bank committing to enter into the loan agreement, and the availability period would not be the full five years of the term loan but a shorter period or periods when a draw-down may be made.
D. The fee is in respect of the committed undrawn amounts, not the amounts drawn down.

**Answer: A.** The officer is wrong twice: a term loan's availability period is the shorter window in which drawdowns may be made, not the whole term, and the commitment fee is charged on the committed but undrawn amount. B: wrong on both counts. C: the fee is for keeping the facility available, not for entering into the agreement. D: corrects only one error.
*Cite: RL-XB p2; RL-Types p2–3; SQ p114 (key A); `ccp-1-0-6`*

**Q23-3** · `0.II.3` `0.III.2` · 2023 CCP Paper 1 Q3 (no official answer) · `ccp-1-0-6` `ccp-1-0-11`

In a committed loan facility, when a borrower gives the lender a drawdown notice, the lender will…

A. Disburse the funds immediately to the borrower.
B. Check whether all the conditions precedent are satisfied and, if so, consider whether or not to disburse the funds.
C. Check whether all the conditions precedent are satisfied and, if so, disburse the funds.
D. Check whether the borrower is still solvent and, if so, disburse the funds.

**Answer: C.** Under a committed facility the lender must advance on request once the conditions precedent are met; it checks the CPs first. A: the CPs come first. B: a discretion to lend is the mark of an uncommitted facility. D: solvency is not the test; the CPs (including no event of default) are.
*Cite: RL-XB p2–3; BF1 s14; `ccp-1-0-6`, `ccp-1-0-11`*

**Q23-4** · `0.II.3` · 2023 CCP Paper 1 Q4 (no official answer) · `ccp-1-0-6`

Which of these statements best describes a commitment fee?

A. A commitment fee is paid to the bank in return for the bank entering into the loan facility agreement and is a fee charged for agreeing to give the loan to the borrower.
B. A commitment fee is paid to the bank in return for the bank committing to making available the agreed amount of the facility during the availability period and is paid in respect of the sums borrowed by the borrower for the period that they remain borrowed.
C. A commitment fee is paid to the bank in return for the bank committing to making available the agreed amount of the facility during the availability period and is paid in respect of committed undrawn amounts during that period.
D. A commitment fee is paid to the bank in return for the borrower committing to borrow the money from the bank and is paid in respect of the sums drawn down on by the borrower.

**Answer: C.** The fee pays for the lender keeping the facility available and is calculated on the committed but undrawn amount during the availability period. A: it is not a fee for signing. B and D: drawn sums bear interest, not commitment fee; D also wrongly makes the borrower the one committing.
*Cite: RL-XB p2; RL-Types p2–3; `ccp-1-0-6`*

### 0.II.4 — Secured v unsecured loans

**Q0-4** · `0.II.4` · own question · `ccp-1-0-7`

A borrower is deciding whether to offer security for a new loan. Which statement is CORRECT?

A. Security benefits only the borrower, because it makes the loan cheaper.
B. Security gives the lender priority over unsecured creditors on the borrower's insolvency, but restricts the borrower's dealings with the secured assets.
C. An unsecured loan usually carries a lower interest rate than a secured one.
D. A borrower need not check its other agreements before granting security.

**Answer: B.** Security protects the lender on insolvency (priority) and gives it some control in a restructuring; for the borrower it restricts dealing with the secured assets. A: security mainly protects the lender. C: unsecured lenders tend to charge more or refuse to lend. D: the borrower must check it has power to grant security and is not breaching other agreements, such as a negative pledge.
*Cite: BF1 s11; Cyril-BF §1.2.3; `ccp-1-0-7`*

### 0.II.5 — Syndicated loan v bond issue: advantages of each; common features

**QSQ-B10** · `0.II.5` · SQ p12 Q10 [Part B 2025 S1], official key A · `ccp-1-0-8`

Which of these apply to both bonds and syndicated loan facilities (in general)?

I. They both involve the borrower borrowing from multiple lenders.
II. They both provide a return in the form of interest.
III. They can both be secured with collateral.
IV. They are both easily bought and sold on an exchange.

A. I, II and III only.
B. I and III only.
C. All of the above.
D. II and IV only.

**Answer: A.** Both involve several lenders, pay a return as interest and can be secured. IV: only bonds are easily traded on an exchange.
*Cite: BF2 s5; Cyril-BF §2.1.1; SQ p114 (key A); `ccp-1-0-8`*

**Q23-7** · `0.II.5` · 2023 CCP Paper 1 Q7 (no official answer) · `ccp-1-0-8`

Which of these apply to both bonds and syndicated loan facilities (in general)?

I. They both involve the borrower borrowing from multiple lenders that are financial institutions only.
II. They both provide a return in the form of interest.
III. They both involve a debt that has to be repaid in the future.
IV. They both have the advantage of imposing only a few covenants on the borrower.

A. All of them.
B. III only.
C. I, II and III only.
D. II and III only.

**Answer: D.** Both pay interest (II) and are debt to be repaid (III). I: bondholders are a broad investor base, not only financial institutions. IV: having fewer covenants is an advantage of bonds over a syndicated loan.
*Cite: BF2 s4–5; `ccp-1-0-8`*

### 0.II.6 — Syndication: arranger, bookrunner, information memorandum, underwriting, agent, security trustee

**Q0-5** · `0.II.6` · own question · `ccp-1-0-9`

In a syndicated loan, which statement about the parties is CORRECT?

A. On a best-efforts syndication the arranger must take up any shortfall itself.
B. The facility agent owes the lenders fiduciary duties and makes credit decisions for them.
C. A security trustee holds the security on trust for all the lenders, so a lender that transfers its share passes the benefit of the security without re-registration.
D. The information memorandum is the arranger's own document, for which the borrower takes no responsibility.

**Answer: C.** The security trustee holds the security for all lenders, so transfers carry the security without re-registration. A: on a best-efforts basis the borrower bears the shortfall risk; in an underwritten deal the underwriters take it up. B: the agent's role is mechanical and administrative and it excludes fiduciary duties. D: the information memorandum is the borrower's document, which the arranger helps prepare.
*Cite: RL-Synd p1–9; RL-Sec p5; `ccp-1-0-9`*

### 0.III The facility agreement

Sub-points 0.III.1–0.III.8. Real questions: QSQ-B3 (0.III.2), QSQ-B4, Q23-5 (0.III.6). Own questions Q0-6 to Q0-11.

### 0.III.1 — Four categories of clauses

**Q0-6** · `0.III.1` · own question · `ccp-1-0-10`

Representations, covenants and events of default belong to which of the four categories of clauses in a facility agreement?

A. Mechanics.
B. Costs of utilisation.
C. General protection.
D. Boilerplate.

**Answer: C.** The four categories are mechanics (drawdown and CPs, repayment and prepayment), costs of utilisation (interest, default interest, fees), general protection (representations, covenants, events of default) and boilerplate.
*Cite: BF1 s13; Cyril-BF §1.3; `ccp-1-0-10`*

### 0.III.2 — Drawdown and conditions precedent

**QSQ-B3** · `0.III.2` `0.III.5` · SQ p7 Q3 [Part B 2024], official key A · `ccp-1-0-11` `ccp-1-0-14`

Part B Course Pte Ltd has entered into the committed five-year term loan facility. It intends to give the bank a drawdown notice, and your friend wants to know what, if anything, he should ensure before issuing it. Select all of the statements that may apply.

I. He should ensure that all representations and warranties in the facility agreement remain true and accurate.
II. He should ensure that no material adverse change has occurred since the original financial statements were provided by the company.
III. He should prepare a copy of the company's pro forma financial statements for the period up to the date of the drawdown notice.
IV. He should obtain a written confirmation by each of the directors that it is in the company's best interests to drawdown on the facility.
V. He should ensure that there are no events of default in existence and that none would result from borrowing under the facility agreement.

A. I, II and V.
B. All of the above.
C. II, III and IV.
D. I and V.

**Answer: A.** For each advance the borrower typically confirms that the representations remain true (they are repeated on drawdown), that no material adverse change has occurred since the original financial statements, and that no event of default exists or would result. III and IV are not usual drawdown requirements. D omits II.
*Cite: BF1 s14, s16–17; RL-XB p2–3; SQ p114 (key A); `ccp-1-0-11`, `ccp-1-0-14`*

See also Q23-3 under 0.II.3 (lender checks the CPs, then must lend).

### 0.III.3 — Repayment and prepayment

**Q0-7** · `0.III.3` · own question · `ccp-1-0-12`

A borrower with a five-year term loan wants to repay it in year two. The facility agreement has no prepayment clause. Which statement is CORRECT?

A. A borrower may always repay early without cost.
B. Without a prepayment clause the borrower has no right to repay early, and doing so may be a breach.
C. The lender must accept early repayment but may charge any fee it likes.
D. Early repayment automatically cancels the security but not the interest for the full term.

**Answer: B.** The borrower may prepay only if the agreement allows it. A prepayment fee, where provided for, compensates the lender for lost interest and must not be drafted as an unenforceable penalty (so C is wrong). A and D have no basis.
*Cite: BF1 s14; RL-XB p3; `ccp-1-0-12`*

### 0.III.4 — Interest, default interest, fees; benchmarks (SORA)

**Q0-8** · `0.III.4` · own question · `ccp-1-0-13`

Which statement about interest under a Singapore-dollar facility agreement today is CORRECT?

A. Interest is usually set by reference to SIBOR plus a margin.
B. Interest is made up of a benchmark rate plus a margin for credit risk (plus any mandatory costs), and default interest should be reasonable so as not to be an unenforceable penalty.
C. Default interest may be set at any level the lender chooses.
D. The margin represents the lender's cost of funds.

**Answer: B.** Interest = basic (benchmark) rate + margin + associated or mandatory costs; default interest is a higher rate on overdue sums and must be reasonable. A: SORA has replaced SOR and SIBOR. C: an excessive rate risks being a penalty. D: the benchmark reflects the cost of funds; the margin prices credit risk.
*Cite: BF1 s15; RL-XB p4; RL-DCM p5–6; `ccp-1-0-13`*

### 0.III.5 — Representations and warranties

See QSQ-B3 under 0.III.2 (representations repeated on drawdown).

**Q0-9** · `0.III.5` · own question · `ccp-1-0-14`

Six months into a loan, the lender finds that a representation the borrower gave at signing (no litigation pending) was untrue. What may the lender do?

A. Nothing, because representations speak only at signing.
B. Refuse further advances and demand immediate repayment, because misrepresentation is an event of default.
C. Only claim damages in tort.
D. Only refuse to renew the facility at maturity.

**Answer: B.** If a representation is untrue the lender can refuse further advances and accelerate, since misrepresentation is an event of default. A: representations matter at signing and throughout the term, and many are repeated (e.g. on each drawdown or interest period). C and D understate the contractual remedies.
*Cite: BF1 s16–17, s19; RL-XB p4; `ccp-1-0-14`*

### 0.III.6 — Covenants: general (negative pledge, pari passu, disposals), financial, information

**QSQ-B4** · `0.III.6` · SQ p8 Q4 [Part B 2024], official key A · `ccp-1-0-15`

How does a bank ensure that its position vis-à-vis the borrower is protected during the life of the facility?

A. The facility agreement will contain various covenants or undertakings by the borrower which require the borrower to refrain from certain activities that may pose a risk to its creditworthiness, and which will allow the bank to monitor the continued creditworthiness of the borrower.
B. The facility agreement will contain various covenants or undertakings by the borrower which require the borrower to refrain from undertaking any business risks and which will allow the bank to monitor the continued creditworthiness of the borrower.
C. The facility agreement will contain various covenants or undertakings by the borrower which require the borrower to refrain from undertaking any business risks and allow the bank to send auditors to inspect the borrower's accounts annually.
D. The facility agreement will contain various covenants or undertakings by the borrower which require the borrower to refrain from certain activities that may pose a risk to its creditworthiness and allow the bank to send auditors to inspect the borrower's accounts annually.

**Answer: A.** Covenants restrict activities that may put creditworthiness at risk and let the lender monitor it. B and C: covenants do not stop the borrower taking any business risk at all. C and D: monitoring is by information covenants (accounts, compliance certificates), not bank auditors inspecting the books.
*Cite: BF1 s18; RL-XB p4–8; SQ p114 (key A); `ccp-1-0-15`*

**Q23-5** · `0.III.6` · 2023 CCP Paper 1 Q5 (no official answer) · `ccp-1-0-15`

Which of these statements most appropriately describes general undertakings/covenants in a facility agreement?

A. General undertakings/covenants seek to ensure that the borrower repays the lender the correct repayment instalments and interest on time in accordance with the agreed payment schedule.
B. General undertakings/covenants seek to ensure that the borrower's share value and employee composition remain within the limits that formed the basis of the lender's initial credit assessment in relation to the granting of the facility.
C. General undertakings/covenants seek to ensure that the financial condition, business and assets of the borrower remain within the limits that formed the basis of the lender's initial credit assessment in relation to the granting of the facility.
D. General undertakings/covenants seek to ensure that the financial projections provided to the lender when it made its initial credit assessment in relation to the granting of the facility are complied with.

**Answer: C.** Covenants protect the lender's credit position during the facility; general covenants are commercial covenants protecting the borrower's business and assets (negative pledge, pari passu, limits on disposals, acquisitions, further borrowing and change of business). A: payment is the repayment and interest mechanics, not a covenant. B: share value and employee numbers are not what covenants police. D: covenants do not make projections binding; financial ratios are a separate category.
*Cite: BF1 s18; RL-XB p4–8; `ccp-1-0-15`*

### 0.III.7 — Events of default; cross-default; acceleration

**Q0-10** · `0.III.7` · own question · `ccp-1-0-16`

The borrower defaults on a bond issued to other investors, but the bondholders have not accelerated. The facility agreement contains a cross-default clause (not cross-acceleration). Which statement is CORRECT?

A. The lender must wait until the bondholders accelerate.
B. The bond default is itself an event of default under the facility, so the lender may cancel undrawn commitments, accelerate and enforce its security.
C. A cross-default clause only applies to defaults under other loans from the same lender.
D. The lender's only remedy is to charge default interest.

**Answer: B.** Cross-default makes a default under another financing a default under this one; cross-acceleration bites only when the other debt is actually accelerated (A describes cross-acceleration). On an event of default the lender may cancel, accelerate and enforce. C and D have no basis.
*Cite: BF1 s19; RL-XB p8; `ccp-1-0-16`*

### 0.III.8 — Boilerplate; assignment and transfer

**Q0-11** · `0.III.8` · own question · `ccp-1-0-17`

A bank wants to sell its participation in a loan to another lender. Which statement is CORRECT about the usual transfer clause?

A. Transfers by lenders are usually prohibited outright.
B. Transfers are usually expressly allowed, often on condition that the borrower pays no more (e.g. withholding tax) to the new lender, or with borrower consent not to be unreasonably withheld.
C. Transfer clauses belong to the "general protection" clauses.
D. A transfer always needs a court order.

**Answer: B.** Lender transfers are usually expressly allowed, subject to the borrower paying no more or to its consent not withheld without good reason. A and D: no. C: assignment and transfer is boilerplate.
*Cite: BF1 s20; RL-XB p8–9; `ccp-1-0-17`*

### 0.IV Taking security

Sub-points 0.IV.1–0.IV.9. Real questions: QSQ-B8 (0.IV.1), QSQ-B9 (0.IV.3), Q23-6 (0.IV.5, 0.IV.6). Own questions Q0-12 to Q0-16.

### 0.IV.1 — Why take security; what happens on the borrower's insolvency

**QSQ-B8** · `0.IV.1` · SQ p11 Q8 [Part B 2025 S1], official key D · `ccp-1-0-18`

A post on X.com reads: "Where a bank lends money to a company and takes security for the loan, even if the company goes insolvent, the bank will always get back all the money that it lent. It will only lose out on interest." Choose the MOST ACCURATE reply.

A. If the company goes insolvent, the bank can enforce its security by refusing to transfer the secured asset back to the company unless it is paid first before the other creditors. But if the company does not have enough money to pay the bank back at all, the bank will have to transfer the secured asset back to the company.
B. If the company goes insolvent, the bank can enforce its security, typically by selling the secured asset. But if the price it gets for the secured asset is less than the outstanding loan amount, then it will have no further claim against the company.
C. If the company goes insolvent, the bank can enforce its security, typically by selling the secured asset. But the money it gets can only be used to pay for the interest that it should have received. The remaining amount will have to be returned to the company, and it will have to claim the outstanding principal from the company as an unsecured creditor.
D. If the company goes insolvent, the bank can enforce its security, typically by selling the secured asset. But if the price it gets for the secured asset is less than the outstanding loan amount, it will still have to claim the remainder from the company as an unsecured creditor and may not get back the entire remaining amount.

**Answer: D.** The secured lender enforces, typically by sale; any shortfall is claimed as an unsecured creditor and may not be recovered in full. A: enforcement is not withholding the asset, and the bank does not hand it back. B: the shortfall remains provable. C: the proceeds go to the secured debt generally, not only interest.
*Cite: BF1 s22; Cyril-BF §1.4; SQ p114 (key D); `ccp-1-0-18`*

### 0.IV.2 — Mortgage: legal v equitable

**Q0-12** · `0.IV.2` · own question · `ccp-1-0-19`

Under an equitable mortgage, which of the following is CORRECT?

A. The mortgagor transfers legal title and keeps the equity of redemption.
B. The debtor keeps legal title and transfers the equitable interest to the creditor.
C. The creditor takes possession of the asset as of right.
D. No interest in the asset passes; the creditor has only a personal claim.

**Answer: B.** Under an equitable mortgage the debtor keeps legal title and transfers the equitable interest. A describes a legal mortgage. C: the debtor usually keeps possession under a mortgage. D describes an unsecured claim.
*Cite: BF1 s23; Cyril-BF §1.4.1; `ccp-1-0-19`*

### 0.IV.3 — Charge: fixed v floating; crystallisation

**QSQ-B9** · `0.IV.3` · SQ p12 Q9 [Part B 2025 S1], official key A · `ccp-1-0-20`

Charlie and Kate Pte Ltd manufactures and sells ladies' bags and shoes. It takes out a bank loan and offers security over its stock of leather materials and the finished products in its factory in Singapore. Such security should be ____. Choose the MOST APPROPRIATE response.

A. A floating charge, as the secured assets will be a changing pool of assets that Charlie and Kate Pte Ltd will need for its business. On an event of default, the charge will crystallise and the company's ability to deal with the assets will be restricted.
B. A fixed charge, as the secured assets are a fixed set of leather materials and finished manufactured products that Charlie and Kate Pte Ltd have possession of. On an event of default, the company will need to transfer the assets to the bank.
C. A floating charge, as the secured assets will be a changing pool of assets that Charlie and Kate Pte Ltd will need for its business. On an event of default, the company can continue to sell the finished manufactured products but cannot make any more new handbags and shoes.
D. A fixed charge over the shares of Charlie and Kate Pte Ltd. On an event of default, the charge will crystallise and the company's ability to deal with its assets (including the leather goods) will be restricted.

**Answer: A.** Stock and raw materials are a changing pool the company must deal with in the ordinary course, so a floating charge fits; on default it crystallises into a fixed charge and the company's dealings are restricted. B: the pool is not fixed, and the company need not hand the assets over. C: on crystallisation the company cannot keep selling. D: a charge over the company's own shares is the wrong security, and a fixed charge does not "crystallise".
*Cite: BF1 s23; RL-Sec p1–3; SQ p114 (key A); `ccp-1-0-20`*

### 0.IV.4 — Weaknesses of a floating charge (priority; later fixed charge; s 229 IRDA)

**Q0-13** · `0.IV.4` · own question · `ccp-1-0-21`

Bank A holds a floating charge over all of X Pte Ltd's assets. Bank B later takes a fixed charge over X's warehouse without notice that Bank A's charge prohibited later charges. X is then wound up. Which statement is CORRECT?

A. Bank A ranks ahead of Bank B over the warehouse because its charge was created first.
B. Bank B's fixed charge ranks ahead of Bank A's floating charge over the warehouse, and Bank A's floating-charge recoveries also rank behind preferential debts.
C. Preferential debts rank behind all floating charges.
D. A floating charge can never be invalidated because of the timing of its creation.

**Answer: B.** A floating charge is postponed to a later fixed charge unless the fixed chargee had notice of a negative pledge, and it ranks behind preferential debts paid out of floating-charge assets. A: creation date does not save it here. C: the reverse is true. D: s 229 IRDA can invalidate a floating charge created shortly before winding up or JM, except for new value.
*Cite: RL-Sec p1–3, p8; IRDA s 229; `ccp-1-0-21`*

### 0.IV.5 — Registration of charges at ACRA (s 131 CA) and consequences of failure

**Q23-6** · `0.IV.5` `0.IV.6` · 2023 CCP Paper 1 Q6 (no official answer) · `ccp-1-0-22` `ccp-1-0-23`

What is the standard procedure for taking security over real estate in Singapore where the security is granted by a company?

A. The security should be perfected by registering it at the Singapore Land Authority, and the security should also be registered with the Accounting and Corporate Regulatory Authority within 14 days after the security has been registered with the Singapore Land Authority.
B. The security should be perfected by registering it at the Singapore Land Authority, and an advertisement should also be placed in an English newspaper within 30 days to notify all the other creditors of the company that security has been taken.
C. The company giving the security should send an email to the Singapore Land Authority telling it about the security taken, and it should also ensure that the security is registered with the Accounting and Corporate Regulatory Authority within 30 days after the agreement is signed.
D. The security should be perfected by registering it at the Singapore Land Authority, and the security should also be registered with the Accounting and Corporate Regulatory Authority within 30 days after the security is created.

**Answer: D.** Land security is registered at the SLA, and a company's charge on land must also be registered with ACRA within 30 days of its creation (s 131 CA). A: the ACRA period is 30 days from creation, not 14 days from SLA registration. B: no advertisement. C: an email is not registration. (The candidate's selection on the screenshot, D, is right.)
*Cite: BF1 s24; CA s 131(1); RL-Sec p3–5; `ccp-1-0-22`, `ccp-1-0-23`*

**Q0-14** · `0.IV.5` · own question · `ccp-1-0-22`

A company grants a debenture with fixed and floating charges on 1 March but its lawyers forget to register particulars with ACRA. The company goes into liquidation in December. What is the effect?

A. The charge is valid against everyone because registration is only for publicity.
B. The charge is void, so far as it secures the money, against the liquidator and any creditor, and the money secured becomes immediately payable.
C. The charge is void against the company itself, but the lender keeps priority over unsecured creditors.
D. The lender has an extra 7 days because the charge was signed abroad.

**Answer: B.** An unregistered registrable charge is void against the liquidator and any creditor (s 131(1) CA), and the secured money becomes immediately payable (s 131(2)), leaving the lender unsecured. D: the current s 131(1) has no extra period for charges created abroad (older readings say 7 days; the current law is followed).
*Cite: CA s 131(1)–(2) (SSO, current at 11 Nov 2026); RL-Sec p3–4; `ccp-1-0-22`*

### 0.IV.6 — Specialist asset registers: land (SLA), IP (IPOS), ships (MPA), aircraft

See Q23-6 under 0.IV.5 (land: SLA as well as ACRA).

**Q0-15** · `0.IV.6` · own question · `ccp-1-0-23`

A lender takes security over a Singapore-registered ship and over a registered trade mark. Where, besides ACRA, is each perfected?

A. The ship at IPOS; the trade mark at the MPA.
B. The ship with the Maritime and Port Authority of Singapore; the trade mark at IPOS.
C. Both at the Singapore Land Authority.
D. Neither needs any register other than ACRA.

**Answer: B.** Ships are registered with the MPA and registered IP with IPOS; land goes to the SLA and aircraft to the Cape Town Convention International Registry. A swaps them; C and D are wrong.
*Cite: BF1 s24; RL-Sec p4–5, p15–19; `ccp-1-0-23`*

### 0.IV.7 — Security over particular assets: shares, receivables, bank accounts, equipment, inventory

**Q0-16** · `0.IV.7` · own question · `ccp-1-0-24`

A bank lending to a company wants security over the company's deposit account held with that same bank. What is this security usually called?

A. A legal mortgage registered at the SLA.
B. A charge-back.
C. A bill of sale.
D. A possessory lien.

**Answer: B.** Where the lender is the account bank, security over the account is a "charge-back"; otherwise an assignment or charge with notice to the account bank and a waiver of set-off is used. A, C and D are not used for bank accounts.
*Cite: RL-Sec p4, p16–20; `ccp-1-0-24`*

### 0.IV.8 — Enforcing security; effect of winding up, judicial management and schemes

**Q0-17** · `0.IV.8` · own question · `ccp-1-0-25`

A bank holds a charge over a borrower's equipment. The borrower applies for a judicial management order. What is the bank's position?

A. It can enforce at once without anyone's consent.
B. It cannot enforce its security without the leave of court or the judicial manager's consent.
C. Its security is extinguished by the JM application.
D. It must prove as an unsecured creditor.

**Answer: B.** Once a JM application is made, no step may be taken to enforce security without leave (or the JM's consent). A: that is the position in a winding up, where a secured creditor can stand outside the liquidation, enforce and prove for any shortfall. C and D: the security survives.
*Cite: RL-Sec p6–7; IRDA s 95; `ccp-1-0-25`*

### 0.IV.9 — Guarantees and security for others: corporate benefit, ss 162–163 CA, financial assistance (s 76 CA)

**Q0-18** · `0.IV.9` · own question · `ccp-1-0-26`

PubCo Ltd, a public company, is asked to give a guarantee to a bank lending money to an investor to buy PubCo's own shares. Which statement is CORRECT?

A. The guarantee is fine because guarantees are not "financial assistance".
B. The guarantee is prohibited financial assistance under s 76(1) CA unless a whitewash procedure (e.g. s 76(9A), (9B) or (10)) is followed.
C. Section 76 applies only to private companies.
D. Corporate benefit never needs to be considered for a guarantee.

**Answer: B.** A public company (or one whose holding company is public) must not give financial assistance — a loan, guarantee or security — for the acquisition of its own or its holding company's shares, unless a whitewash applies. A and C: wrong. D: a guarantor must have power and must benefit, judged company by company.
*Cite: RL-Sec p9–14; CA s 76; `ccp-1-0-26`*

### 0.V Bonds and bond markets

Sub-points 0.V.1–0.V.5. Real question: Q23-8 (0.V.2). Own questions Q0-19 to Q0-22.

### 0.V.1 — What a bond is; why issue bonds rather than borrow from banks

**Q0-19** · `0.V.1` · own question · `ccp-1-0-27`

Which of the following is NOT an advantage of issuing bonds over borrowing from banks, as the course lists them?

A. Access to a broader investor base.
B. Fewer covenants than a syndicated loan.
C. Disclosure usually limited to publicly available information.
D. Flexibility to draw down only when needed and repay by instalments.

**Answer: D.** Draw-when-needed and instalment repayment are advantages of a syndicated loan; bonds usually repay in one bullet. A, B and C are bond advantages, along with flexible interest options and frequently being unsecured.
*Cite: BF2 s4–5; Cyril-BF §2.1.1; `ccp-1-0-27`*

### 0.V.2 — Eurobond v domestic bond; international debt capital markets

**Q23-8** · `0.V.2` · 2023 CCP Paper 1 Q8 (no official answer) · `ccp-1-0-28`

What are the advantages of issuing bonds on the international instead of the domestic bond market?

A. It gives the issuer access to a much larger pool of investors and funds and a lower and less complex regulatory burden.
B. It gives the issuer access to a much larger pool of investors and allows them to disclose less information to the investors.
C. It gives the issuer access to a supply of funds in Euros.
D. It gives the issuer access to a much larger pool of investors and a larger supply of funds.

**Answer: D.** International debt capital markets offer a larger pool of investors, a larger supply of funds and a reduced cost of funds. A: they bring more regulatory and compliance issues, not fewer. B: lighter disclosure is not the course's point. C: "Euro" means international, not the euro currency.
*Cite: BF2 s6–7; RL-BondOv p1; `ccp-1-0-28`*

### 0.V.3 — Standalone issue v medium-term note (MTN/EMTN) programme

**Q0-20** · `0.V.3` · own question · `ccp-1-0-29`

A frequent issuer wants to tap the bond market quickly several times a year with consistent terms. Which structure suits it, and what is needed for each issue?

A. A standalone issue each time, with a full new prospectus.
B. An MTN programme: costlier to set up, but each drawdown needs only a pricing supplement (final terms; in Singapore, a pricing statement) against the base prospectus.
C. An MTN programme, which needs no documents at all for later issues.
D. A syndicated loan with a market flex clause.

**Answer: B.** An MTN programme is a framework of master agreements for quick, cheap, frequent issues up to a programme limit; each issue uses a pricing supplement or final terms against the base prospectus. A suits unusual or complex one-off terms. C overstates it. D is a loan.
*Cite: BF2 s8; RL-EMTN p1–2; RL-DCM p18; `ccp-1-0-29`*

### 0.V.4 — Wholesale v retail bond markets; listing bonds on SGX

**Q0-21** · `0.V.4` · own question · `ccp-1-0-30`

An issuer lists bonds on SGX-ST that will be offered only to specified investors throughout their tenor and traded in a minimum board lot of S$200,000. Must it appoint a trustee?

A. Yes, a trustee is always required for SGX-listed debt.
B. No, a trustee is not required in this case.
C. Yes, unless the bonds are bearer bonds.
D. No, because wholesale bonds cannot be listed on SGX.

**Answer: B.** A trustee must be appointed for SGX-listed debt unless, for its whole tenor, it is offered only to specified investors and traded in a minimum board lot of S$200,000. D: SGX lists both wholesale and retail bonds.
*Cite: BF2 s9; RL-DCM p9–13; `ccp-1-0-30`*

### 0.V.5 — Bearer v registered; global v definitive; clearing systems

**Q0-22** · `0.V.5` · own question · `ccp-1-0-31`

Which statement about bond form is CORRECT?

A. Title to registered bonds passes by delivery of the certificate.
B. A global bond is a single document representing the whole issue, held for a clearing system (CDP in Singapore; Euroclear and Clearstream internationally), so interests are transferred by book entry.
C. Definitive bonds are the usual form for international issues.
D. Bearer bonds are transferred by entry on a register kept by a registrar.

**Answer: B.** A and D swap bearer and registered: bearer bonds pass by delivery, registered bonds by entry on the register. C: definitive certificates are issued only in limited cases.
*Cite: Cyril-BF §2.2.3.1; RL-BondOv p2–5; RL-DCM p17; `ccp-1-0-31`*

### 0.VI Structure of a bond transaction

Sub-points 0.VI.1–0.VI.5. Real questions: Q23-9 (0.VI.1), Q23-10 (0.VI.2). Own questions Q0-23 to Q0-25.

### 0.VI.1 — Key participants

**Q23-9** · `0.VI.1` · 2023 CCP Paper 1 Q9 (no official answer) · `ccp-1-0-32`

Which of these are the functions of a manager on a bond transaction?

I. Provide advice to the issuer on the transaction.
II. Help with the actual marketing process of the bond.
III. Act on behalf of the bondholders as an intermediary between them and the issuer.
IV. Help with the administrative function of paying the bondholders the interest payments on the interest payment dates.

A. I, II and III only.
B. I and II only.
C. I only.
D. All of them.

**Answer: B.** The managers (investment banks led by a lead manager) structure and market the bonds and may underwrite them. III is the trustee's role; IV is the paying agent's.
*Cite: BF2 s11–12; Cyril-BF §2.2.1; `ccp-1-0-32`*

### 0.VI.2 — Trustee v fiscal agent structure

**Q23-10** · `0.VI.2` · 2023 CCP Paper 1 Q10 (no official answer) · `ccp-1-0-33`

Which of these statements best describes the role of a trustee in a bond transaction?

A. The trustee in a bond transaction represents the bondholders in interactions with the issuer and must act in the interests of the bondholders.
B. A trustee in a bond transaction represents the issuer in interactions with the regulators and must act in the interests of the bondholders.
C. The trustee in a bond transaction represents the bondholders in interactions with the paying agent and must act in the interests of the bondholders.
D. A trustee in a bond transaction represents the bondholders in interactions with the issuer and must act in the interests of the issuer.

**Answer: A.** The trustee represents the bondholders, is their main contact with the issuer and can enforce for all of them; it is duty-bound to act in their interests. B and D misstate whom it serves; C misstates the counterparty.
*Cite: BF2 s11–12; Cyril-BF §2.2.2; `ccp-1-0-33`*

**Q0-23** · `0.VI.2` · own question · `ccp-1-0-33`

An issue uses a fiscal agent structure. A single bondholder wants to sue the issuer after an event of default. Which is CORRECT?

A. Only the fiscal agent can sue, on behalf of all bondholders.
B. Each bondholder monitors and enforces individually, supported by a deed of covenant; the fiscal agent is the issuer's agent.
C. The issue must also have a trustee, which will sue.
D. The bondholder must first obtain the fiscal agent's consent.

**Answer: B.** Under a fiscal agent structure there is no bondholder representative: the fiscal agent is the issuer's agent with administrative functions, and holders enforce individually (deed of covenant). C: there is never both a fiscal agent and a trustee. A and D have no basis.
*Cite: BF2 s11–12; RL-BondDocs p1, p3; `ccp-1-0-33`*

### 0.VI.3 — Stages of a bond issue: pre-launch, launch, signing and closing, post-issue

**Q0-24** · `0.VI.3` · own question · `ccp-1-0-34`

At which stage of a bond issue are the bonds delivered against payment through the clearing systems?

A. Pre-launch.
B. Launch.
C. Closing.
D. Post-issue.

**Answer: C.** At signing the subscription agreement is signed and the prospectus published; at closing (usually 2 days to a week later) the remaining documents are signed and the bonds delivered against payment. A covers checking powers, structuring and due diligence; B the announcement and roadshows; D interest payments and repayment.
*Cite: Cyril-BF §2.2.3; RL-BondSteps p1–8; `ccp-1-0-34`*

### 0.VI.4 — Key documents

**Q0-25** · `0.VI.4` · own question · `ccp-1-0-35`

Which bond document is the agreement under which the issuer agrees to issue the bonds and the managers agree to subscribe for them?

A. The trust deed.
B. The agency agreement.
C. The subscription agreement.
D. The deed of covenant.

**Answer: C.** The subscription agreement is between the issuer and the managers. A constitutes the bonds and appoints the trustee; B appoints the paying agents; D gives holders direct enforcement rights where there is no trustee.
*Cite: BF2 s14; RL-BondDocs p1–7; `ccp-1-0-35`*

### 0.VI.5 — Classifying the product: prescribed capital markets products (s 309B SFA)

**Q0-26** · `0.VI.5` · own question · `ccp-1-0-36`

Before offering plain vanilla bonds that will be listed on SGX, what must the issuer do under s 309B SFA?

A. Nothing; s 309B applies only to shares.
B. Determine whether the bonds are prescribed or non-prescribed capital markets products and notify the classification to the exchange and the relevant CMS licence holder.
C. Obtain MAS approval of the bond's credit rating.
D. Obtain shareholders' approval.

**Answer: B.** The issuer must classify the product (plain vanilla bonds are prescribed CMPs) and notify the exchange (if listed) and the distributing CMS licence holder; this decides what further checks the distributor must make.
*Cite: SFA s 309B(1); RL-DCM p3; `ccp-1-0-36`*

### 0.VII Prospectus requirement and exemptions (SFA)

Sub-points 0.VII.1–0.VII.6. Real questions: Q23-11 (0.VII.1), QSQ-B7 (0.VII.4, under 0.VIII.3), Q23-12 (0.VII.6), Q23-13 (0.VII.1, under 0.IX.4). Own questions Q0-27 to Q0-29.

### 0.VII.1 — Prospectus requirement: contents, product highlights sheet, lodgement and registration

**Q23-11** · `0.VII.1` `0.V.4` · 2023 CCP Paper 1 Q11 (no official answer) · `ccp-1-0-37` `ccp-1-0-30`

Which of these regulators would be involved in a bond offering to the public?

A. SGX-ST, MAS and ICMA.
B. SGX-ST only.
C. MAS only.
D. SGX-ST and MAS.

**Answer: D.** An offer of bonds to the public needs a prospectus lodged with and registered by MAS, and retail bonds are listed and traded on SGX-ST. A: ICMA is a market association, not a regulator. B and C each leave one out. (The candidate's selection, D, is right.)
*Cite: BF2 s9, s15; RL-DCM p9–13, p18; `ccp-1-0-37`, `ccp-1-0-30`*

See also Q23-13 under 0.IX.4 (prospectus is a disclosure document).

**Q0-27** · `0.VII.1` · own question · `ccp-1-0-37`

Which statement about a prospectus for an offer of securities is CORRECT?

A. It is principally a marketing document.
B. It must be accompanied by a product highlights sheet, signed by all the directors, lodged with MAS (on OPERA) and registered before it is circulated.
C. Securities may be issued on it at any time after registration.
D. It needs no registration if the offer is made to the public in Singapore.

**Answer: B.** The prospectus is a legal and disclosure document (A wrong), must carry a PHS, be signed by the directors and registered with MAS after lodgement. C: no securities may be issued on it more than 6 months after registration (24 months for a base prospectus) (s 250(3) SFA). D: a public offer is exactly what needs one.
*Cite: BF2 s15; BF3 s14; SFA ss 240(8), 250(3); `ccp-1-0-37`*

### 0.VII.2 — Prospectus liability; supplementary or replacement prospectus

**Q0-28** · `0.VII.2` · own question · `ccp-1-0-38`

After its prospectus is registered but before the offer closes, an issuer discovers a material misstatement in it. Which is CORRECT?

A. Nothing need be done until the offer closes.
B. It must lodge a supplementary or replacement prospectus; the issuer, its directors and the named issue manager and underwriter face criminal and civil liability for false or misleading statements, subject to a reasonable-inquiries defence.
C. Only the issuer can be liable; directors never are.
D. If the offer had been made by information memorandum instead, no false-statement rule of the SFA would apply at all.

**Answer: B.** A defective prospectus must be corrected by a supplementary or replacement prospectus, and ss 253–254 SFA impose liability on the issuer, directors and named advisers, with a due-diligence defence. C is wrong. D: an IM carries no ss 253–254 liability, but ss 199–200 SFA still apply.
*Cite: BF3 s14; RL-ECM p18–19; RL-DCM p21; `ccp-1-0-38`*

### 0.VII.3 — Exemptions: institutional investors (s 274) and accredited / relevant persons (s 275); information memorandum

**Q0-29** · `0.VII.3` · own question · `ccp-1-0-39`

A company offers bonds only to accredited investors, using an information memorandum, and wants to place newspaper advertisements about the offer. Which is CORRECT?

A. It may advertise freely because accredited investors are sophisticated.
B. The s 275 exemption is available only if the offer is not accompanied by an advertisement making or calling attention to it; the IM carries no prospectus liability.
C. It must register the IM with MAS.
D. The s 275 exemption applies only to individuals with income over S$1 million.

**Answer: B.** The ss 274–275 exemptions require that the offer not be accompanied by an advertisement; such wholesale offers use an IM, which carries no prospectus liability. C: an IM is not registered. D: an individual accredited investor qualifies with e.g. net personal assets over S$2m, net financial assets over S$1m or income of at least S$300,000, and must opt in.
*Cite: BF2 s16; SFA ss 4A(1)(a), 274, 275; `ccp-1-0-39`*

### 0.VII.4 — Exemptions: small offers (S$5m) and private placements (50 persons)

See QSQ-B7 under 0.VIII.3 (50 persons v S$5m).

**Q0-30** · `0.VII.4` · own question · `ccp-1-0-40`

A start-up wants to raise S$4 million from personal offers to about 120 contacts over the next year, without advertising. Which exemption is available?

A. The private placement exemption (s 272B SFA).
B. The small offer exemption (s 272A SFA): total raised in any 12 months not exceeding S$5 million, no advertisement.
C. Neither; a prospectus is required.
D. The offer information statement route.

**Answer: B.** Small offers of up to S$5m in 12 months with no advertisement are exempt (s 272A). A: private placements are limited to 50 persons in 12 months (s 272B), so 120 offerees fails it. D: an OIS is for issuers already listed on SGX.
*Cite: BF3 s8; SFA ss 272A(1), 272B(1); `ccp-1-0-40`*

### 0.VII.5 — Offer information statement for listed issuers (s 277)

**Q0-31** · `0.VII.5` · own question · `ccp-1-0-41`

A company already listed on SGX makes a renounceable rights issue with an offer information statement. Which statement is CORRECT?

A. The OIS must be registered by MAS after a 7-day exposure period.
B. The OIS is lodged with MAS but not registered, has no exposure period and lighter disclosure, but prospectus-type liability still applies.
C. No document of any kind is needed.
D. An OIS can be used by an unlisted company.

**Answer: B.** An OIS (s 277 SFA) is for issuers already listed, has lighter disclosure because issuer information is already public, is lodged but not registered and has no exposure period, and still attracts civil and criminal liability.
*Cite: BF2 s16; RL-DCM p7, p19, p21; RL-ECM p12; `ccp-1-0-41`*

### 0.VII.6 — Bond Seasoning and Exempt Bond Issuer Frameworks

**Q23-12** · `0.VII.6` · 2023 CCP Paper 1 Q12 (no official answer) · `ccp-1-0-42`

Which of these statements best describes the Bond Seasoning Framework and the Exempt Bond Issuer Framework?

A. These frameworks allow issuers that are already listed to issue bonds to institutional investors only without a prospectus.
B. These frameworks allow issuers that meet higher standards of size, listing history and credit to issue bonds to institutional investors only without a prospectus.
C. These frameworks allow issuers that meet higher standards of size, listing history and credit to issue bonds to the public without a prospectus.
D. These frameworks allow issuers that are already listed to issue bonds to the public without a prospectus.

**Answer: C.** Both frameworks let established issuers that meet size, listing history and credit tests reach retail investors without a full prospectus. A and B: offers to institutional investors never need a prospectus anyway. D: being listed is not enough; the higher standards must be met.
*Cite: BF2 s16; RL-DCM p7–9; `ccp-1-0-42`*

### 0.VIII Equity financing for private companies; venture capital

Sub-points 0.VIII.1–0.VIII.6. Real questions: Q23-14 (0.VIII.1, 0.VIII.4), QSQ-B7 (0.VIII.3), QSQ-B5, Q23-15 (0.VIII.5), Q23-16 (0.VIII.6). Own question Q0-32.

### 0.VIII.1 — Why issue shares; methods of equity financing

**Q23-14** · `0.VIII.1` `0.VIII.4` · 2023 CCP Paper 1 Q14 (no official answer) · `ccp-1-0-43` `ccp-1-0-46`

Which of these are factors a private limited company should consider in deciding whether to issue more shares to raise financing?

I. The amount of debt that company has already taken on.
II. Whether its loan agreements restrict how much more debt it can take on.
III. How many shareholders it already has.
IV. Whether its existing shareholders will be willing to see their shareholdings diluted.

A. II and IV only.
B. I, II and IV only.
C. I and II only.
D. All of them.

**Answer: D.** The amount of existing debt and any restrictions on further borrowing favour or disfavour issuing shares (I, II). A private company may have no more than 50 members (III), and new shares need the general meeting's approval (s 161 CA) and dilute existing holders (IV).
*Cite: BF3 s4–5, s9; CA ss 18(1)(b), 161(1); `ccp-1-0-43`, `ccp-1-0-46`*

### 0.VIII.2 — Sources of private equity investment

**Q0-32** · `0.VIII.2` · own question · `ccp-1-0-44`

Which of the following is NOT one of the sources of private equity investment the course lists?

A. Angel investors.
B. Government schemes such as Startup SG.
C. Accredited start-up incubators.
D. A retail public offer of shares on Catalist.

**Answer: D.** A public offer is public equity, not private. The listed sources are friends-and-family rounds, angel investors, government schemes (e.g. Startup SG), accredited incubators and corporate venture capital.
*Cite: BF3 s7; Cyril-BF §3.2; `ccp-1-0-44`*

### 0.VIII.3 — Which prospectus exemptions a private company uses to raise equity

**QSQ-B7** · `0.VIII.3` `0.VII.4` · SQ p10 Q7 [Part B 2025 S1], official key C · `ccp-1-0-45` `ccp-1-0-40`

Raman is the sole shareholder of DeepFind Pte Ltd and needs additional funding of at least S$10 million. He asks his AI engine, DeepFind, whom he can approach to become shareholders without having to issue a prospectus; it says he can ask up to 50 of his friends and family members. A competitor's AI engine, CheapGPT, says he can ask his extensive network of contacts to invest. Which AI engine got it right and why?

A. Both DeepFind and CheapGPT are right as they are each referring to different prospectus exemptions in the SFA that would apply.
B. Only DeepFind was right as it has limited the people that Raman can approach to his friends and family members, so he would be entitled to rely on a prospectus exemption in the SFA.
C. Only DeepFind was right as it has limited the number of people that Raman can approach, so he would be entitled to rely on a prospectus exemption in the SFA.
D. Only CheapGPT was right as Raman only needs S$10 million so he can approach as many people as he needs to get that amount.

**Answer: C.** The private placement exemption limits the number of offerees (50 in 12 months), not who they are. A and D: the small offer exemption caps the amount at S$5m, so it cannot support an unlimited offer for S$10m. B: the relationship is irrelevant.
*Cite: BF3 s8; SFA ss 272A, 272B; SQ p114 (key C); `ccp-1-0-45`, `ccp-1-0-40`*

### 0.VIII.4 — Additional considerations: shareholder limit; approval of existing shareholders

See Q23-14 under 0.VIII.1 (50-member limit; dilution).

**Q0-33** · `0.VIII.4` · own question · `ccp-1-0-46`

The directors of a private company allot new shares to an investor without any prior approval of the company in general meeting. What is the effect?

A. The issue is valid if the board was unanimous.
B. The issue is void (s 161(6) CA), because directors may not issue shares without the general meeting's prior approval (s 161(1)).
C. The issue is valid but the directors must report it at the next AGM.
D. The issue is voidable only at the investor's option.

**Answer: B.** Under s 161(1) CA directors need the prior approval of the company in general meeting to issue shares, and an issue in breach is void (s 161(6)).
*Cite: BF3 s9; CA s 161(1), (6); `ccp-1-0-46`*

### 0.VIII.5 — Steps and documents: due diligence, share subscription agreement, shareholders' agreement

**QSQ-B5** · `0.VIII.5` · SQ p9 Q5 [Part B 2024], official key B · `ccp-1-0-47`

Big Fish VC LLP will provide funding in return for shares in MSH Company Pte Ltd, of which MSH is the sole shareholder. The offering will only be made to Big Fish VC LLP, without an offering to the public. Which of these are steps that will usually take place to implement this deal?

I. MSH Company Pte Ltd will draft and prepare a prospectus for Big Fish VC LLP to review.
II. Big Fish VC LLP will carry out due diligence on MSH Company Pte Ltd.
III. MSH Company Pte Ltd and Big Fish VC LLP will negotiate and agree the terms of the share subscription agreement.
IV. MSH Company Pte Ltd will convert to a public company.
V. MSH will carry out due diligence on Big Fish VC LLP.
VI. MSH and Big Fish VC LLP will negotiate and agree the terms of a shareholders' agreement.

A. All of the above.
B. II, III and VI.
C. I, II, and V.
D. III, IV and VI.

**Answer: B.** The investor does due diligence on the company, the company and investor sign a share subscription agreement, and the shareholders sign a shareholders' agreement. I: no prospectus for an offer to one VC. IV: no need to go public. V: the founder does not usually do due diligence on the VC.
*Cite: BF3 s10; RL-VC p14–17; SQ p114 (key B); `ccp-1-0-47`*

**Q23-15** · `0.VIII.5` · 2023 CCP Paper 1 Q15 (no official answer) · `ccp-1-0-47`

Which of these are the kinds of documents that you would see in a venture capital transaction without a public offering?

I. Prospectus
II. Share subscription agreement
III. Shareholders' agreement
IV. Underwriting agreement

A. I, II and III only.
B. II, III and IV only.
C. II only.
D. II and III only.

**Answer: D.** A VC investment uses a share subscription agreement and a shareholders' agreement. A prospectus (I) and an underwriting agreement (IV) belong to a public offer.
*Cite: BF3 s10; RL-VC p14–17; `ccp-1-0-47`*

### 0.VIII.6 — Venture capital terms and fund structures

**Q23-16** · `0.VIII.6` `0.VIII.5` · 2023 CCP Paper 1 Q16 (no official answer) · `ccp-1-0-48` `ccp-1-0-47`

In a private equity deal, which of these are the kinds of provisions you would be likely to see in a shareholders' agreement that seek to protect the investors' rights?

I. A right to appoint a specified number of directors to the board.
II. Pre-emption rights over the issue of new shares.
III. A right of first refusal over shares to be sold to a third party.
IV. A tag-along right of co-sale enabling the minority investor to sell its shares to a third party along with the majority shareholder.

A. I, II and III only.
B. II, III and IV only.
C. All of them.
D. II and III only.

**Answer: C.** Investor protections include board seats, pre-emption on new issues, transfer restrictions such as rights of first refusal, and co-sale or tag-along rights.
*Cite: RL-VC p2–22; BF3 s10; `ccp-1-0-48`, `ccp-1-0-47`*

### 0.IX Public offer of shares (IPO)

Sub-points 0.IX.1–0.IX.6. Real questions: Q23-17 (0.IX.3), Q23-13 (0.IX.4), Q23-18 (0.IX.6). Own questions Q0-34 to Q0-36.

### 0.IX.1 — Mainboard v Catalist

**Q0-34** · `0.IX.1` · own question · `ccp-1-0-49`

A fast-growing company with no profit track record wants to list on SGX. Which statement is CORRECT?

A. It must list on the Mainboard, which has no quantitative entry criteria.
B. Catalist has no minimum quantitative entry criteria; suitability is assessed by an approved sponsor, and a full sponsor must remain continuing sponsor for at least 3 years after listing.
C. Catalist requires S$300m market capitalisation.
D. Neither board accepts companies without profits.

**Answer: B.** Catalist suits smaller, fast-growing companies and is sponsor-supervised with no minimum quantitative criteria; the Mainboard has profitability or market-cap tests (A wrong). C: S$300m is Mainboard test C. D: Mainboard test C needs only revenue and market cap.
*Cite: BF3 s12; RL-ECM p2, p4; `ccp-1-0-49`*

### 0.IX.2 — Mainboard admission criteria

**Q0-35** · `0.IX.2` · own question · `ccp-1-0-50`

A company had consolidated pre-tax profit of S$12 million in its latest financial year and a 3-year operating track record with the same business and management. Its market capitalisation at listing would be S$90 million. Can it meet a Mainboard quantitative test?

A. No; test A needs S$30 million pre-tax profit.
B. Yes, test A: pre-tax profit of at least S$10 million in the latest financial year and a 3-year operating track record.
C. No; every test needs market capitalisation of at least S$150 million.
D. Yes, but only test C.

**Answer: B.** Current Rule 210(2)(a) requires S$10m pre-tax profit (older readings and Cyril give S$30m; the current figure is followed, so A is out of date). C: only test B (S$150m) and test C (S$300m) have market-cap thresholds. D: test C needs S$300m market cap.
*Cite: SGX Mainboard Rule 210(2) (current at 11 Nov 2026); RL-ECM p4–7; `ccp-1-0-50`*

### 0.IX.3 — Key steps and timetable of an IPO

**Q23-17** · `0.IX.3` `0.IX.5` · 2023 CCP Paper 1 Q17 (no official answer) · `ccp-1-0-51` `ccp-1-0-53`

Which of these statements is the most accurate as to the steps of an IPO?

A. The draft prospectus is submitted to SGX. After review, it is lodged and then registered with the MAS. The shares can be marketed to the public after review by the SGX, before lodgement and registration with the MAS.
B. The draft prospectus is submitted to SGX. After review, it is registered with the SGX. After registration, the shares can be marketed to the public.
C. The draft prospectus is submitted to MAS. After review, it is lodged and then registered with the SGX. The shares can be marketed to the public after review by the MAS, before lodgement and registration with the SGX.
D. The draft prospectus is submitted to SGX. After review, it is lodged and then registered with the MAS. The shares can be marketed to the public after registration of the prospectus with the MAS.

**Answer: D.** The listing application (with the draft prospectus) goes to SGX-ST, the prospectus is lodged with and registered by MAS, and the public offer follows registration. A and C: advertising to the public before lodgement is prohibited. B and C: the prospectus is registered by MAS, not SGX.
*Cite: BF3 s13, s15; RL-ECM p9, p20, p23; `ccp-1-0-51`, `ccp-1-0-53`*

### 0.IX.4 — The IPO prospectus: contents, preparation, responsibility

**Q23-13** · `0.IX.4` `0.VII.1` · 2023 CCP Paper 1 Q13 (no official answer) · `ccp-1-0-52` `ccp-1-0-37`

Which of these statements best describes a prospectus issued in connection with an IPO?

A. It is a disclosure document which contains all information that investors would reasonably require to make an informed assessment of the issuer and the securities being offered.
B. It is principally a legal and regulatory disclosure document which sets out the information prescribed by the Accounting and Regulatory Authority in its circulars.
C. It is principally a marketing document and sets out the information prescribed by the Accounting and Regulatory Authority in its circulars.
D. It is a disclosure document used by the issuer and the banks solely for marketing purposes.

**Answer: A.** The prospectus must contain all information investors and their advisers would reasonably require to make an informed assessment of the shares and the issuer. B and C: the regulator is MAS, not ACRA ("Accounting and Regulatory Authority"). C and D: it is principally a legal and disclosure document, not a marketing one.
*Cite: BF3 s14; BF2 s15; `ccp-1-0-52`, `ccp-1-0-37`*

### 0.IX.5 — IPO marketing: pre-IPO placements, cornerstone investors, roadshows, advertising

See Q23-17 under 0.IX.3 (no public marketing before lodgement).

**Q0-36** · `0.IX.5` · own question · `ccp-1-0-53`

An IPO issuer secures commitments from investors who will subscribe at the IPO price, concurrently with but separately from the IPO, giving the deal certainty. What are they?

A. Pre-IPO placees.
B. Cornerstone investors.
C. Underwriters.
D. Roadshow participants.

**Answer: B.** Cornerstone investors are placed concurrently with but separately from the IPO at the IPO price. A: pre-IPO placements come earlier, building credentials. D: roadshows market to institutional and accredited investors after lodgement.
*Cite: BF3 s15; RL-ECM p20; `ccp-1-0-53`*

### 0.IX.6 — Continuing obligations after listing; follow-on share issues

**Q23-18** · `0.IX.6` · 2023 CCP Paper 1 Q18 (no official answer) · `ccp-1-0-54`

When a company is listed on the SGX, it must [choose all that apply]:

I. Comply with all corporate governance practices in the Corporate Governance Code or explain any deviations.
II. Disclose such material information as is required in accordance with the SGX listing rules.
III. Make periodic disclosure of its financial statements.
IV. Subject interested person transactions which cross certain thresholds to shareholder approval.

A. I, II and III only.
B. All of them.
C. II only.
D. II and III only.

**Answer: B.** A listed issuer must disclose material information, report periodically, comply with the IPT rules (announcement at 3% of NTA, shareholders' approval at 5%) and comply or explain against the Code.
*Cite: BF3 s16; RL-ECM p13, p27–28; `ccp-1-0-54`*

**Q0-37** · `0.IX.6` · own question · `ccp-1-0-54`

A Mainboard issuer has a general share issue mandate. Up to what proportion of its issued shares may it issue under the mandate, and how much of that may be other than pro rata?

A. 100%, all of which may be non-pro rata.
B. Up to 50% of issued shares, of which no more than 20% other than pro rata to existing shareholders.
C. Up to 20%, all pro rata.
D. Up to 10%, all by placement.

**Answer: B.** Under Mainboard Rule 806(2) a general mandate allows up to 50% of issued shares, with no more than 20% other than on a pro rata basis.
*Cite: SGX Mainboard Rule 806(2) (current at 11 Nov 2026); RL-ECM p13; `ccp-1-0-54`*

## 1 · Corporate Governance

### 1.I Introduction to corporate governance

Sub-points 1.I.1–1.I.3. No real question; own questions Q1-1 to Q1-3.

### 1.I.1 — What corporate governance is; principles of good governance

**Q1-1** · `1.I.1` · own question · `ccp-1-1-1`

Which of the following is NOT one of the eight principles of good corporate governance the course lists?

A. Transparency.
B. Accountability.
C. Profit maximisation.
D. Sustainability.

**Answer: C.** The eight are transparency, accountability, integrity, fairness, sustainability, diversity, capability and leadership. The Code 2018 speaks of enhancing long-term shareholder value while taking into account other stakeholders' interests, not of maximising profit.
*Cite: CG1 s3–4; `ccp-1-1-1`*

### 1.I.2 — Who is responsible: regulators, CGAC, the board (s 157A CA) and its dual role

**Q1-2** · `1.I.2` · own question · `ccp-1-1-2`

Which statement about who is responsible for corporate governance in Singapore is CORRECT?

A. The Corporate Governance Advisory Committee enforces the Code against listed companies.
B. The business of a company is managed by, or under the direction or supervision of, its directors (s 157A CA), and the board's dual role is company performance and regulatory conformance.
C. The board's only role is regulatory conformance.
D. ACRA alone regulates listed companies' governance.

**Answer: B.** The board is central under s 157A CA and must deliver both performance (strategy and value creation) and conformance. A: the CGAC is industry-led; it monitors and advocates good practice and advises the regulators, leaving enforcement to SGX. C: understates the role. D: ACRA, MAS and SGX RegCo all regulate.
*Cite: CG1 s5–8; `ccp-1-1-2`*

### 1.I.3 — Why corporate governance: principal–agent problem; benefits

**Q1-3** · `1.I.3` · own question · `ccp-1-1-3`

In the agency theory the course uses, who is the agent of whom?

A. The shareholders are the agents of the board.
B. The board is the agent of the shareholders, and management is the agent of the board.
C. The regulators are the agents of the shareholders.
D. Management is the agent of the creditors.

**Answer: B.** Agency problems arise when the agent's interests conflict with the principal's; governance aligns the interests of board, shareholders and stakeholders, with benefits such as investor confidence, higher valuations and cheaper capital.
*Cite: CG1 s9–11; `ccp-1-1-3`*

### 1.II Disclosure-based regime and liability for failing to disclose

Sub-points 1.II.1–1.II.4. No real question; own questions Q1-4 to Q1-7.

### 1.II.1 — Shift from merit-based to disclosure-based regulation

**Q1-4** · `1.II.1` · own question · `ccp-1-1-4`

When did Singapore move from merit-based to disclosure-based regulation of its capital markets?

A. 1965–1967.
B. 1998–2000, with changes to the Companies Act, the SFA and the Listing Manual, and the first Code of Corporate Governance in 2001.
C. 2018, with the fourth Code.
D. It has always been disclosure-based.

**Answer: B.** Under the merit-based regime the regulator was gatekeeper; between 1998 and 2000 Singapore moved to a market-driven, disclosure-based regime, and MAS issued the first Code in 2001.
*Cite: CG1 s12; CG-LP p4; `ccp-1-1-4`*

### 1.II.2 — s 203 SFA continuous disclosure: offence (intentional/reckless) v civil (negligent); s 204 penalty

**Q1-5** · `1.II.2` · own question · `ccp-1-1-5`

A listed company negligently fails to announce information the Listing Rules require it to disclose. Under the SFA, which is CORRECT?

A. It commits an offence punishable by a fine of up to S$250,000.
B. The failure contravenes s 203 but is not an offence, because only an intentional or reckless failure is; it attracts civil penalty and civil liability.
C. It is not a contravention of the SFA at all, only of the Listing Rules.
D. It is an offence punishable by imprisonment of up to 10 years.

**Answer: B.** s 203(1) forbids intentional, reckless or negligent failures to notify SGX; s 203(3) makes only intentional or reckless failures offences. A: the S$250,000 fine (or up to 7 years' jail, or both, s 204(1)) applies to the offence. C: s 203 gives the disclosure rules the force of law. D: the maximum is 7 years.
*Cite: CG1 s13; SFA12 p9–10 (ss 203–204); `ccp-1-1-5`*

### 1.II.3 — s 331 SFA: officers liable (consent, connivance, neglect)

**Q1-6** · `1.II.3` · own question · `ccp-1-1-6`

A listed company recklessly fails to disclose material information, and the failure is attributable to the neglect of its CFO. Is the CFO personally liable?

A. No; only the company commits the offence.
B. Yes; under s 331 SFA an officer is guilty where the company's offence was committed with his consent or connivance or is attributable to his neglect.
C. Only if he personally profited.
D. Only if he is also a director.

**Answer: B.** s 331 SFA makes officers personally accountable for the company's offence on consent, connivance or neglect. C and D add requirements s 331 does not have.
*Cite: CG1 s14; Cyril-CG §2.1; `ccp-1-1-6`*

### 1.II.4 — Materiality: Madhavan Peter v PP; China Aviation Oil

**Q1-7** · `1.II.4` · own question · `ccp-1-1-7`

In *Madhavan Peter v PP* [2012] SGHC 153, how did the High Court read the Rule 703 materiality test?

A. Any information that could affect the share price at all.
B. Information "likely to effect a significant change in the price or value" of the issuer's securities.
C. Only information that has already moved the share price.
D. Only information concerning the company's financial results.

**Answer: B.** Chan Sek Keong CJ read the test as information likely to effect a significant change in price or value. In the China Aviation Oil case, three directors were fined S$150,000 each for failing to disclose oil-options losses in breach of Rule 703.
*Cite: CG2 s4; `ccp-1-1-7`*

### 1.III Immediate disclosure of material information (Rule 703, Appendix 7.1)

Sub-points 1.III.1–1.III.7. Real questions: Q23-19 (1.III.1, 1.III.4), QSQ-G7 (1.III.2), QSQ-G2, QSQ-G10 (1.III.5, 1.III.4). Own questions Q1-8 to Q1-10.

### 1.III.1 — Rule 703(1): false market / likely to materially affect price

**Q23-19** · `1.III.1` `1.III.4` · 2023 CCP Paper 1 Q19 (no official answer) · `ccp-1-1-8` `ccp-1-1-11`

Big Chicken Limited is listed on the Mainboard of the SGX-ST. Its unlisted subsidiary has entered into a joint venture under which the core business of Big Chicken Limited may be merged with another company. Due to the significance of this joint venture, the local press caught wind of it even before any formal agreement was signed and has published an article on it. Which of the following statements is true under Listing Rule 703?

A. As the joint venture is undertaken by its unlisted subsidiary, Big Chicken Limited is not required to announce the joint venture.
B. Big Chicken Limited can choose not to announce the joint venture immediately as it wishes to update shareholders in person at its annual general meeting next week.
C. As the joint venture was already reported on and became public information, Big Chicken Limited is not required to announce the joint venture.
D. Big Chicken Limited must make an immediate announcement on SGXNET of this joint venture.

**Answer: D.** Rule 703(1) covers information concerning the issuer or any of its subsidiaries or associated companies, and a JV or merger is a typical event needing immediate disclosure (App 7.1 para 8). A: subsidiaries are covered. B: the announcement must be immediate and through SGXNET. C: the information being generally available is no excuse, and a press leak also ends any confidentiality carve-out.
*Cite: LM r 703(1), (3); LM-App7.1 paras 5, 8; `ccp-1-1-8`, `ccp-1-1-11`*

### 1.III.2 — Examples of material information and events needing immediate disclosure

**QSQ-G7** · `1.III.2` · SQ p15 Q7 [Original], official key B · `ccp-1-1-9`

Sigma Ltd discovers that one of its major manufacturing plants has been destroyed by fire. The disruption is expected to significantly affect production and profitability. Which statement is the MOST ACCURATE with respect to the disclosure of such information under the listing rules?

A. Sigma Ltd may wait until its next financial statements are released.
B. Sigma Ltd should generally announce the information immediately.
C. Sigma Ltd only needs to notify its insurers.
D. Sigma Ltd need only disclose the information if shareholders request it.

**Answer: B.** Information likely to materially affect the share price must be announced immediately (Rule 703(1)). A, C and D postpone or avoid disclosure the rule requires.
*Cite: CG2 s5; LM-App7.1 paras 4, 8; SQ p114 (key B); `ccp-1-1-9`*

### 1.III.3 — Exceptions: breach of law (703(2)); the three conditions in 703(3)

**Q1-8** · `1.III.3` · own question · `ccp-1-1-10`

A listed company is negotiating a confidential acquisition; no agreement has been reached. When may it withhold disclosure under Rule 703(3)?

A. Whenever the board considers disclosure premature.
B. Only while a reasonable person would not expect disclosure, the information is confidential, and it concerns an incomplete proposal or negotiation (or another listed category); once any condition fails, it must announce immediately.
C. Until the deal completes, regardless of leaks.
D. Only if SGX grants a waiver.

**Answer: B.** All three conditions in Rule 703(3) must be met, and disclosure is due as soon as any ceases (e.g. a leak ends confidentiality). D: SGX will not waive Rule 703 (Rule 703(5)). Information whose disclosure would breach the law is separately excepted (Rule 703(2)).
*Cite: CG2 s6; LM r 703(2)–(3); `ccp-1-1-10`*

### 1.III.4 — How to announce: SGXNET first; no waiver; "already public" is no excuse

See Q23-19 under 1.III.1 and QSQ-G10 under 1.III.5.

### 1.III.5 — Personal matters of a director or CEO (investigation, accident, illness)

**QSQ-G2** · `1.III.5` `1.III.4` · SQ p13 Q2 [Part B 2024], official key D · `ccp-1-1-12` `ccp-1-1-11`

Fondue Limited is listed on the Mainboard. Mr Chocolate, its Chairman and CEO, is being investigated for intentionally making a false police report against his neighbour, including serious allegations under the Penal Code. Which statement(s) is/are TRUE under the Listing Rules?

I. As the investigation relates to the personal affairs of Mr Chocolate and has nothing to do with the company's business, Fondue Limited is not required to announce the investigation.
II. Fondue Limited can choose to publicise the investigation by way of an official statement to the local press instead of an announcement via SGXNET, as this would reach a larger number of people.
III. Fondue Limited can choose not to announce the investigation immediately as it wishes to wait to see if Mr Chocolate will be charged in court.

A. I only.
B. II and III.
C. I and III.
D. None of the statements is true.

**Answer: D.** Personal matters of a Chairman/CEO are not excluded if material; announcements go through SGXNET first, not the press; and the issuer cannot wait to see if he is charged.
*Cite: CG2 s3, s7; LM r 702, 703; SQ p114 (key D); `ccp-1-1-12`, `ccp-1-1-11`*

**QSQ-G10** · `1.III.5` `1.III.4` · SQ p17 Q10 [Original], official key D · `ccp-1-1-12` `ccp-1-1-11`

Unlucky Limited is listed on the Mainboard. Mr South, its Chairman and CEO, is in a coma after a serious traffic accident and will not be able to carry out his duties soon. A video of the accident has been widely circulated on social media. Which statement(s) is/are TRUE under the Listing Rules?

I. As the traffic accident relates to the personal affairs of Mr South and has nothing to do with the company's business, Unlucky Limited is not required to announce the traffic accident and hospitalisation of Mr South.
II. As the video has been widely circulated on social media and has become public information, Unlucky Limited is not required to announce the traffic accident and hospitalisation of Mr South.
III. Unlucky Limited may choose to disclose the traffic accident and hospitalisation of Mr South only after Mr South regains consciousness.

A. I only.
B. I and II only.
C. I, II and III.
D. None of the statements are true.

**Answer: D.** His incapacity as Chairman and CEO is material and must be announced immediately via SGXNET; that it is on social media is no excuse, and the issuer cannot wait for his recovery.
*Cite: CG2 s3, s7; LM-App7.1 para 5; SQ p114 (key D); `ccp-1-1-12`, `ccp-1-1-11`*

### 1.III.6 — Rumours, unusual trading and trading halts

**Q1-9** · `1.III.6` · own question · `ccp-1-1-13`

An unsubstantiated press rumour of a takeover bid causes unusual trading in a listed company's shares. What should the company do?

A. Ignore it, since it did not start the rumour.
B. Clarify, confirm or explain the rumour; if the information is materially price-sensitive, consider a trading halt so it can be disseminated before trading resumes.
C. Wait for SGX to suspend the shares.
D. Brief its largest shareholders privately.

**Answer: B.** Rumours causing unusual trading should be clarified, confirmed or explained, with a halt where needed. D would be selective disclosure.
*Cite: CG2 s8; `ccp-1-1-13`*

### 1.III.7 — No selective disclosure; profit guidance

**Q1-10** · `1.III.7` · own question · `ccp-1-1-14`

A listed company's CFO realises the company will miss the profit target it publicly announced. She wants to tell the analysts who cover the stock at a private briefing first. Which is CORRECT?

A. She may, as analysts help disseminate information.
B. She must not disclose selectively; the company should give profit guidance by announcement, since it is unlikely to meet its disclosed targets.
C. No disclosure is needed until the year-end results.
D. She may tell the largest institutional shareholders first.

**Answer: B.** Appendix 7.1 para 7 forbids divulging information so as to put anyone in a privileged dealing position, and profit guidance is required when publicly disclosed targets will not be met. A, C and D are wrong.
*Cite: CG2 s11; Cyril-CG §2.6; `ccp-1-1-14`*

### 1.IV Specific announcements (Rule 704)

Sub-points 1.IV.1–1.IV.2. Real questions: QSQ-G3, Q23-21 (1.IV.1). Own question Q1-11.

### 1.IV.1 — Appointment or cessation of directors, CEO, CFO and equivalent officers; AC appointments; relatives in managerial positions

**QSQ-G3** · `1.IV.1` · SQ p14 Q3 [Part B 2024], official key B · `ccp-1-1-15`

Sunshine Group Limited, listed on the Mainboard, appointed a new financial controller, Ray, on 20 October 2024. Ray will be the most senior financial officer since the company has no CFO, and will be responsible for the Group's overall financial reporting, management accounting and compliance matters. Which statement is TRUE?

A. The appointment of Ray as financial controller does not need to be announced to shareholders.
B. The appointment of Ray as financial controller must be announced immediately on 20 October 2024.
C. The appointment of Ray as financial controller must be announced within three (3) market days from 20 October 2024.
D. Ray's appointment must be disclosed in Sunshine Group Limited's annual report issued after the end of the current financial year.

**Answer: B.** Rule 704(7)(a) requires immediate announcement of the appointment of a CFO or other executive officer of equivalent authority; a financial controller who is the most senior finance officer is one.
*Cite: CG2 s9; LM r 704(7); SQ p114 (key B); `ccp-1-1-15`*

**Q23-21** · `1.IV.1` · 2023 CCP Paper 1 Q21 (no official answer) · `ccp-1-1-15`

Mooncake Group Limited, listed on the Mainboard, appointed a new financial controller, Mr Snow, on 2 October 2023. He will be the most senior financial officer since the company has no CFO, and will be responsible for the Group's overall financial reporting, management accounting and compliance matters. Which statement is true?

A. Mr Snow's appointment need only be disclosed in Mooncake Group Limited's annual report after the end of the current financial year.
B. The appointment of Mr Snow as financial controller does not need to be announced to shareholders.
C. The appointment of Mr Snow as financial controller must be announced immediately on 2 October 2023.
D. The appointment of Mr Snow as financial controller need only be announced within three (3) market days from 2 October 2023.

**Answer: C.** Same rule as QSQ-G3: an officer of equivalent authority to a CFO must be announced immediately (Rule 704(7)(a)).
*Cite: LM r 704(7); `ccp-1-1-15`*

### 1.IV.2 — Other specific events

**Q1-11** · `1.IV.2` · own question · `ccp-1-1-16`

Which of the following must a listed issuer announce immediately under Rule 704?

A. A creditor's application to court to wind up one of its subsidiaries.
B. A routine renewal of its office cleaning contract.
C. The hiring of a junior accounts clerk with no family links to directors.
D. A change in its office telephone number.

**Answer: A.** Rule 704(20) requires immediate announcement of any application to court to wind up the issuer or a subsidiary (or to place it under JM). B, C and D are not Rule 704 events and are not material.
*Cite: CG2 s9; LM r 704(20); `ccp-1-1-16`*

### 1.V Periodic reporting

Sub-points 1.V.1–1.V.2. Real questions: Q23-27 (1.V.1), Q23-25 (1.V.2, 1.V.1).

### 1.V.1 — Financial statements: half-yearly v quarterly (risk-based); 45 / 60 days; voluntary updates

**Q23-27** · `1.V.1` · 2023 CCP Paper 1 Q27 (no official answer) · `ccp-1-1-17`

Sun Limited is listed on the Mainboard. When will Sun Limited be required under the Listing Rules to announce its financial statements on a quarterly basis?

A. When its auditors have issued a disclaimer of opinion on its latest financial statements.
B. When its auditors have issued a qualified opinion on its latest financial statements.
C. All of the scenarios.
D. When its auditors have stated that a material uncertainty relating to going concern exists in its latest financial statements.

**Answer: C.** Quarterly reporting is required where the auditors issued an adverse opinion, qualified opinion or disclaimer, or stated a material uncertainty relating to going concern (Rule 705(2)); all three scenarios qualify.
*Cite: CG2 s10, s12–13; LM r 705(2); `ccp-1-1-17`*

### 1.V.2 — Annual report and AGM (Rule 707); chairman's statement

**Q23-25** · `1.V.2` `1.V.1` · 2023 CCP Paper 1 Q25 (no official answer) · `ccp-1-1-18` `ccp-1-1-17`

Sad Balloon Limited is listed on the Mainboard. Its most recent financial year ended on 31 March 2023. Which of the following actions would be in compliance with the Listing Rules?

I. Holding its annual general meeting on 14 July 2023.
II. Holding its annual general meeting on 1 August 2023.
III. Announcing its unaudited financial results for the full financial year on 10 May 2023.
IV. Announcing its unaudited financial results together with its annual report for the full financial year on 14 July 2023.

A. II and IV only.
B. II and III only.
C. I and III only.
D. I and IV only.

**Answer: C.** The AGM must be held within four months of the year end (Rule 707(1)), i.e. by 31 July 2023, so I complies and II does not. Full-year results must be announced within 60 days (Rule 705(1)), i.e. by 30 May 2023, so III complies and IV (14 July) is late. (The candidate's selection on the screenshot, D, is wrong.)
*Cite: LM r 705(1), 707(1); `ccp-1-1-18`, `ccp-1-1-17`*

### 1.VI Board diversity and sustainability reporting

Sub-points 1.VI.1–1.VI.2. No real question; own questions Q1-12, Q1-13.

### 1.VI.1 — Board diversity policy (Rule 710A)

**Q1-12** · `1.VI.1` · own question · `ccp-1-1-19`

Under Rule 710A, which is CORRECT?

A. A board diversity policy is recommended but optional.
B. Every issuer must maintain a board diversity policy addressing gender, skills and experience, and describe in its annual report its targets, plans and timelines, progress, and how the board's mix serves its needs.
C. The policy need cover only gender.
D. The policy must be approved by SGX before adoption.

**Answer: B.** Since 2022 the policy is mandatory (Rule 710A(1)) and its annual report description must cover the four items in Rule 710A(2).
*Cite: CG2 s14–15; LM r 710A; `ccp-1-1-19`*

### 1.VI.2 — Sustainability reporting (Rules 711A, 711B; PN 7.6)

**Q1-13** · `1.VI.2` · own question · `ccp-1-1-20`

For a financial year starting in 2026, which statement about a listed issuer's sustainability report is CORRECT?

A. It may omit climate-related disclosures if it explains why.
B. All primary components are mandatory; the report is issued together with the annual report (within 5 months of year end if externally assured), the board bears ultimate responsibility, and all directors must have one-time sustainability training.
C. External assurance is compulsory.
D. Only the CEO is responsible for it.

**Answer: B.** From 1 Jan 2026 all Rule 711B(1) components are mandatory and the report is issued with the annual report; the board is ultimately responsible; the process needs internal review, while external assurance is optional (C wrong). A: climate-related disclosures were never on a comply-or-explain basis.
*Cite: CG2 s10, s16–20; `ccp-1-1-20`*

### 1.VII Interested person transactions: scope (Chapter 9)

Sub-points 1.VII.1–1.VII.5. Real questions: QSQ-G5, Q23-30 (1.VII.3, 1.VII.4), Q23-32 (1.VII.5). Own questions Q1-14, Q1-15.

### 1.VII.1 — Objective of Chapter 9; substance over form

**Q1-14** · `1.VII.1` · own question · `ccp-1-1-21`

A transaction is structured through a chain of companies so that, on paper, the listed group does not deal directly with its controlling shareholder. How does Chapter 9 treat it?

A. Chapter 9 looks only at the legal form, so it does not apply.
B. Chapter 9 looks at the economic and commercial substance of the transaction, instead of legal form and technicality, having regard to its objective of guarding against conflicts of interest.
C. Chapter 9 applies only to transactions in the ordinary course of business.
D. Chapter 9 never applies to indirect transactions.

**Answer: B.** Rules 901–902 require regard to the objective and to substance over form; "transaction" includes those entered into directly or indirectly, e.g. through interposed entities (Rule 904(6)).
*Cite: CG3 s3, s6; LM r 901–902, 904(6); `ccp-1-1-21`*

### 1.VII.2 — Entity at risk

**Q1-15** · `1.VII.2` · own question · `ccp-1-1-22`

Which of these is NOT an "entity at risk" of a Mainboard issuer?

A. The issuer itself.
B. An unlisted subsidiary of the issuer.
C. An unlisted associated company over which the listed group has control.
D. A subsidiary of the issuer that is itself listed on SGX.

**Answer: D.** An entity at risk is the issuer, an unlisted subsidiary, or an unlisted associated company controlled by the listed group (Rule 904(2)); a listed subsidiary is outside the definition.
*Cite: CG3 s3; LM r 904(2); `ccp-1-1-22`*

### 1.VII.3 — Interested person: director, CEO, controlling shareholder and their associates

**QSQ-G5** · `1.VII.3` `1.VII.4` · SQ p15 Q5 [Part B 2024], official key D · `ccp-1-1-23` `ccp-1-1-24`

Swift Limited is listed on the Mainboard. Which statement is TRUE for the purposes of Chapter 9 of the Listing Rules?

A. The adopted child of the Chief Executive Officer of Swift Limited is not an interested person of Swift Limited.
B. The brother of a director of Swift Limited is not an interested person of Swift Limited.
C. Castle Pte Ltd, a company in which a director of Swift Limited directly holds 5% of its shares, and whose husband directly holds 30% of its shares, is not an interested person of Swift Limited.
D. Although the cousin of a director of Swift Limited does not fall strictly within the definition of "interested person", there is a possibility that the SGX may deem him an "interested person" of Swift Limited.

**Answer: D.** SGX may deem a person an interested person where it transacts with an entity at risk under an arrangement with an interested person (Rule 904(4A)). A and B: an adopted child and a sibling are immediate family, so associates. C: the director and her husband together hold 35%, over the 30% threshold, so Castle is an associate.
*Cite: CG3 s4–5; LM r 904(4), (4A); SQ p114 (key D); `ccp-1-1-23`, `ccp-1-1-24`*

**Q23-30** · `1.VII.3` `1.VII.4` · 2023 CCP Paper 1 Q30 (no official answer) · `ccp-1-1-23` `ccp-1-1-24`

Era Limited is listed on the Mainboard. Which statement is true for the purposes of Chapter 9 of the Listing Rules?

A. Although the cousin of a director of Era Limited does not fall strictly within the definition of "interested person", there is a possibility that the SGX may deem him an "interested person" of Era Limited.
B. The sister of a director of Era Limited is not an interested person of Era Limited.
C. The adopted child of the Chief Executive Officer of Era Limited is not an interested person of Era Limited.
D. Bejewel Pte Ltd, a company in which a director of Era Limited directly holds 5% of its shares, and whose husband directly holds 30% of its shares, is not an interested person of Era Limited.

**Answer: A.** Same analysis as QSQ-G5: only the Rule 904(4A) statement is true; the sister, adopted child and 35%-held company are associates and so interested persons.
*Cite: CG3 s4–5; LM r 904(4), (4A); `ccp-1-1-23`, `ccp-1-1-24`*

### 1.VII.4 — SGX's power to deem an interested person (Rule 904(4A))

See QSQ-G5 and Q23-30 under 1.VII.3.

### 1.VII.5 — What counts as a "transaction" (Rule 904(6))

**Q23-32** · `1.VII.5` `1.VIII.6` · 2023 CCP Paper 1 Q32 (no official answer) · `ccp-1-1-25` `ccp-1-1-31`

Which of the following actions of Golden Eggs Limited, listed on the Mainboard, is a "transaction" which would be subject to Listing Rules 905, 906 and 907?

A. A payment of directors' fees to the directors of Golden Eggs Limited.
B. A grant of options for shares in Golden Eggs Limited to an interested person not pursuant to an employees' share option scheme.
C. All of the actions would be subject to Listing Rules 905, 906 and 907.
D. A payment of dividends to an interested person.

**Answer: B.** Granting options is a "transaction" (Rule 904(6)(e)), and only grants under an SGX-approved employees' share option scheme are exempt (Rule 915(2)). A: directors' fees are exempt (Rule 915(8)). D: pro-rata dividends are exempt (Rule 915(1)). So C is wrong.
*Cite: LM r 904(6), 915(1), (2), (8); `ccp-1-1-25`, `ccp-1-1-31`*

### 1.VIII Interested person transactions: thresholds, approval, exceptions

Sub-points 1.VIII.1–1.VIII.8. Real questions: QSQ-G8 (1.VIII.1), Q23-32 (1.VIII.6, under 1.VII.5). Own questions Q1-16 to Q1-22.

### 1.VIII.1 — 3% announcement, 5% shareholder approval, aggregation, S$100,000 floor (Rules 905–906)

**QSQ-G8** · `1.VIII.1` · SQ p16 Q8 [Original], official key B · `ccp-1-1-26`

Sigma Ltd, a listed company, proposes to enter into an Interested Person Transaction. Its value exceeds 3%, but does not exceed 5%, of the group's latest audited net tangible assets. Which statement is the MOST ACCURATE?

A. Neither an announcement nor shareholders' approval is required.
B. The company must make an announcement but shareholders' approval is not required.
C. Shareholders' approval is required but no announcement is necessary.
D. Both an announcement and shareholders' approval are always required.

**Answer: B.** An IPT of 3% or more of latest audited NTA must be announced (Rule 905); shareholders' approval is needed at 5% or more (Rule 906).
*Cite: CG3 s7–8; LM r 905–906; SQ p114 (key B); `ccp-1-1-26`*

**Q1-16** · `1.VIII.1` · own question · `ccp-1-1-26`

During one financial year a listed issuer enters into three IPTs with its controlling shareholder worth 1.5%, 1.0% and 0.8% of latest audited NTA (each above S$100,000). Which is CORRECT?

A. None needs announcing, because each is below 3%.
B. When the aggregate reaches 3% (on the third transaction), that transaction and all future ones with the same interested person that year must be announced.
C. All three need shareholders' approval.
D. Aggregation applies only across different financial years.

**Answer: B.** IPTs with the same interested person in the same financial year are aggregated; once they reach 3% the latest and all future ones that year must be announced (Rule 905(2)). The total is 3.3%, below 5%, so no shareholders' approval.
*Cite: LM r 905(2), 906(1); `ccp-1-1-26`*

### 1.VIII.2 — Value of a transaction (Rule 909); "same interested person" (Rule 908); negative NTA

**Q1-17** · `1.VIII.2` · own question · `ccp-1-1-27`

A listed issuer lends money to its controlling shareholder. Under Rule 909, how is the value of the transaction measured?

A. The interest payable only.
B. The interest payable plus the amount of the loan.
C. The loan amount less interest.
D. Nil, since a loan is repaid.

**Answer: B.** Value is the amount at risk: for lending to an interested person, the interest payable plus the loan; for borrowing from one, the interest payable (A). If NTA is negative, the issuer consults SGX on another benchmark, such as market capitalisation.
*Cite: LM r 909; CG3 s7–8; `ccp-1-1-27`*

### 1.VIII.3 — Contents of the announcement; audit committee statement (Rule 917)

**Q1-18** · `1.VIII.3` · own question · `ccp-1-1-28`

Which must a Rule 905 IPT announcement include?

A. The CEO's personal view of the interested person.
B. A statement whether the audit committee considers the transaction on normal commercial terms and not prejudicial to the issuer and its minority shareholders (or that it is obtaining an independent financial adviser's opinion first).
C. The share price on the day of the announcement only.
D. Nothing beyond the parties' names.

**Answer: B.** Rule 917 requires details of the interested person and the transaction, the rationale and benefit, the audit committee statement (or IFA route), and year-to-date totals.
*Cite: LM r 917; `ccp-1-1-28`*

### 1.VIII.4 — Shareholder approval: timing (918); interested person abstains (919)

**Q1-19** · `1.VIII.4` · own question · `ccp-1-1-29`

A listed issuer needs shareholders' approval for an IPT with its controlling shareholder. Which is CORRECT?

A. Approval may be obtained after completion.
B. Approval must be obtained before the transaction is entered into or, if it is expressed to be conditional on approval, before completion; the interested person and associates must not vote, nor act as proxies without specific voting instructions.
C. The controlling shareholder may vote if it discloses its interest.
D. Approval is by the board alone.

**Answer: B.** Rules 918 and 919.
*Cite: LM r 918–919; `ccp-1-1-29`*

### 1.VIII.5 — Annual report disclosure of IPTs (Rule 907)

**Q1-20** · `1.VIII.5` · own question · `ccp-1-1-30`

What must a listed issuer's annual report disclose about IPTs under Rule 907?

A. Nothing, if each IPT was announced.
B. For each interested person: its name, the nature of the relationship, the aggregate value of IPTs in the year (excluding those under S$100,000 and those under a shareholders' mandate), and the aggregate value under a mandate.
C. Only IPTs that needed shareholders' approval.
D. Only IPTs under a general mandate.

**Answer: B.** Rule 907 requires the per-person aggregate disclosure described in B.
*Cite: CG3 s9; LM r 907; `ccp-1-1-30`*

### 1.VIII.6 — Exceptions from all requirements (Rule 915)

See Q23-32 under 1.VII.5 (options outside an ESOS are not exempt).

**Q1-21** · `1.VIII.6` · own question · `ccp-1-1-31`

Which of these IPTs is exempt from announcement, shareholders' approval AND annual report disclosure?

A. A one-off payment to a retiring director in excess of his contractual entitlement (a "golden parachute").
B. A loan on normal commercial terms in the ordinary course of business from an MAS-licensed bank in which the controlling shareholder has an interest.
C. A five-year lease of property from the CEO's wife.
D. A joint venture with the controlling shareholder.

**Answer: B.** Financial assistance from an MAS-licensed financial institution on normal commercial terms and in the ordinary course is exempt under Rule 915(6)–(7). A: golden parachutes are carved out of the remuneration exemption (Rule 915(8)). C: only leases of up to 3 years with a valuation are exempt, and then only from shareholders' approval (Rule 916(1)). D: a JV is at most exempt from approval under Rule 916(2) if its conditions are met.
*Cite: CG3 s10–13; LM r 915–916; `ccp-1-1-31`*

### 1.VIII.7 — Exceptions from shareholder approval only (Rule 916)

**Q1-22** · `1.VIII.7` · own question · `ccp-1-1-32`

A listed issuer's subsidiary will lease an office from its controlling shareholder for 2 years at a rent supported by a property valuer's valuation. The value exceeds 5% of NTA. Which is CORRECT?

A. No announcement and no approval are needed.
B. Shareholders' approval is not needed (Rule 916(1)), but the transaction must still be announced and disclosed in the annual report.
C. Shareholders' approval is needed because the value exceeds 5%.
D. The transaction is prohibited.

**Answer: B.** Rule 916 exempts only from Rule 906 (approval); Rules 905 and 907 still apply.
*Cite: CG3 s12–13; LM r 916(1); `ccp-1-1-32`*

### 1.VIII.8 — General mandate for recurrent transactions (Rule 920)

**Q1-23** · `1.VIII.8` · own question · `ccp-1-1-33`

A listed issuer buys raw materials every month from a company owned by its controlling shareholder. What can it do to avoid seeking approval for each purchase?

A. Nothing; each purchase over 5% needs separate approval.
B. Seek a general mandate from shareholders for recurrent transactions of a revenue or trading nature, renewed annually, with a circular that includes an IFA's opinion on the pricing methods.
C. Seek a general mandate covering the purchase of the supplier's factory as well.
D. Ask SGX for a waiver.

**Answer: B.** Rule 920 mandates cover recurrent revenue or trading transactions, not purchases of assets, undertakings or businesses (C wrong); transactions under a mandate are not separately subject to Rules 905 and 906.
*Cite: CG3 s14; LM r 920; `ccp-1-1-33`*

### 1.IX The Code of Corporate Governance and comply-or-explain

Sub-points 1.IX.1–1.IX.2. Real questions: QSQ-G9, Q23-29 (1.IX.1); Q23-22 (1.IX.1, under 1.X.3). Own question Q1-24.

### 1.IX.1 — Status of the Code; Rule 710; Principles, Provisions, Practice Guidance

**QSQ-G9** · `1.IX.1` · SQ p16 Q9 [Original], official key B · `ccp-1-1-34`

Mercury Ltd has not appointed a lead independent director, even though the Code recommends doing so in certain circumstances. The board believes its current governance arrangements adequately protect shareholders. Which statement is the MOST ACCURATE?

A. Mercury Ltd must appoint a lead independent director immediately, per the Code.
B. Mercury Ltd may maintain its current arrangement, provided it gives a meaningful explanation of the departure from the relevant provision of the Code.
C. Mercury Ltd should simply state that it has not complied with the Code.
D. Mercury Ltd need not mention the matter in its annual report and should only mention it as and when a lead independent director is appointed.

**Answer: B.** Provisions are comply-or-explain: the issuer must state the Provision departed from, explain why, and explain how its practice is consistent with the intent of the Principle (Rule 710). A: Provisions are not mandatory. C: a bare statement is not an explanation. D: the variation must be explained in the annual report.
*Cite: CG3 s15–19; LM r 710; SQ p114 (key B); `ccp-1-1-34`*

**Q23-29** · `1.IX.1` · 2023 CCP Paper 1 Q29 (no official answer) · `ccp-1-1-34`

Which of the following statements is false in respect of Echo Limited, listed on the Mainboard?

I. Echo Limited can choose not to adopt the practices set out in the Practice Guidance. It does not need to provide any explanation for not adopting the practices set out in the Practice Guidance.
II. Echo Limited can choose not to comply with the principles of the Code of Corporate Governance. However, it would have to explain the reason for any variation from the principles.

A. II only.
B. Both statements are false.
C. None of the statements is false.
D. I only.

**Answer: A.** Statement I is true: the Practice Guidance is voluntary. Statement II is false: issuers must comply with the Principles; comply-or-explain applies to the Provisions. (The candidate's selection on the screenshot, D, is wrong.)
*Cite: CG3 s18; LM r 710; `ccp-1-1-34`*

See also Q23-22 under 1.X.3 (Provision 2.2 variation explained).

### 1.IX.2 — Structure of the Code: the 13 Principles

**Q1-24** · `1.IX.2` · own question · `ccp-1-1-35`

Under which section of the Code do Principles 9 (risk management and internal controls) and 10 (Audit Committee) fall?

A. Board matters.
B. Remuneration matters.
C. Accountability and audit.
D. Managing stakeholder relationships.

**Answer: C.** The Code's five sections: board matters (1–5), remuneration matters (6–8), accountability and audit (9–10), shareholder rights and engagement (11–12), managing stakeholder relationships (13).
*Cite: CG4 s3; CODE pp4–18; `ccp-1-1-35`*

### 1.X Directors: independence and board composition

Sub-points 1.X.1–1.X.4. Real questions: QSQ-G4, QSQ-G6, Q23-24 (1.X.2), Q23-22, Q23-28, Q23-31 (1.X.3). Own questions Q1-25, Q1-26.

### 1.X.1 — Who is "independent" (Provision 2.1); substantial shareholder = 5%

**Q1-25** · `1.X.1` · own question · `ccp-1-1-36`

Under Provision 2.1 of the Code, a director is not independent if he has a relationship that could interfere with his independent business judgement with which of the following?

A. Only the company itself.
B. The company, its related corporations, its substantial shareholders (5% or more) or its officers.
C. Only shareholders holding 15% or more.
D. Any company in the same industry.

**Answer: B.** Provision 2.1 covers relationships with the company, related corporations, substantial shareholders (5%) and officers. The NC determines independence annually (Provision 4.4), and the Rule 210(5)(d) tests are mandatory on top.
*Cite: CG4 s4–5; CODE Provision 2.1; `ccp-1-1-36`*

### 1.X.2 — Rule 210(5)(d): employment (3 years), immediate family, 9-year rule

**QSQ-G4** · `1.X.2` · SQ p14 Q4 [Part B 2024], official key D · `ccp-1-1-37`

Lexus Limited, listed on the Mainboard, is considering appointing an independent director. Who is NOT DISQUALIFIED from being an independent director under the Listing Rules?

A. Ben, whose wife is the current CEO of Lexus Limited.
B. Sandy, who has just joined Lexus Limited as a marketing director.
C. Geraldine, a current employee of Lexus Limited's subsidiary since 2019. Geraldine has never been employed directly by Lexus Limited.
D. Linda, who was previously appointed as an independent director of Lexus Limited from 2015 to 2018.

**Answer: D.** Linda served 3 years in aggregate, well under nine, and none of the other Rule 210(5)(d) limbs applies. A: an immediate family member employed by the issuer whose pay the RC sets (the CEO). B: employed by the issuer now. C: employed by a related corporation in the current or past three years.
*Cite: CG4 s5; LM r 210(5)(d); SQ p114 (key D); `ccp-1-1-37`*

**QSQ-G6** · `1.X.2` · SQ p15 Q6 [Original], official key D · `ccp-1-1-37`

Sigma Ltd, listed on the Mainboard, is considering appointing an independent director. Who would be DISQUALIFIED from being independent under the listing rules?

A. John, who was previously employed as the head of Human Resources of Sigma Ltd from 2000 to 2010.
B. Lionel, who holds a shareholding interest in Sigma Ltd of 1%.
C. Anabelle, whose twin sister is currently an accounts manager working at Sigma Ltd.
D. Ronald, who is currently employed with Omega Pte Ltd, the most significant operating subsidiary of Sigma Ltd.

**Answer: D.** A current employee of a related corporation is disqualified (Rule 210(5)(d)(i)). A: employment ended more than three financial years ago. B: 1% is not a disqualification. C: the sister's remuneration as an accounts manager is not set by the RC, so limb (ii) does not bite.
*Cite: CG4 s5; LM r 210(5)(d); SQ p114 (key D); `ccp-1-1-37`*

**Q23-24** · `1.X.2` · 2023 CCP Paper 1 Q24 (no official answer) · `ccp-1-1-37`

Bravo Limited, listed on the Mainboard, is considering appointing an independent director. Of the following candidates, who is not disqualified from being independent under Listing Rule 210(5)(d)?

I. Mr Lim, whose father is the current CEO of Bravo Limited.
II. Ms Lau, who has been an employee of Bravo Limited since 2000.
III. Mr Koh, who was previously appointed as an independent director of Bravo Limited from 2012 to 2015.
IV. Ms Tan, who has been an employee of Bravo Limited's subsidiary since 2019. Ms Tan has never been employed directly by Bravo Limited.

A. Ms Lau.
B. Ms Tan.
C. Mr Koh.
D. Mr Lim.

**Answer: C.** Mr Koh served 3 years in aggregate. Mr Lim's father is the CEO (immediate family employed, pay set by the RC); Ms Lau is a current employee; Ms Tan is a current employee of a related corporation.
*Cite: LM r 210(5)(d); `ccp-1-1-37`*

### 1.X.3 — Board composition

**Q23-28** · `1.X.3` · 2023 CCP Paper 1 Q28 (no official answer) · `ccp-1-1-38`

The board of Charlie Limited, listed on the Mainboard, is: Alfred (executive director); Beatrice (independent non-executive director and Chairman of the board); Charlotte (executive director); Diane (independent non-executive director); Ernest (executive director); Fynn (independent non-executive director); Gloria (independent non-executive director). Gloria will soon retire. Which statement is true?

A. Charlie Limited must appoint an additional executive director to be in full compliance with the Code of Corporate Governance.
B. Charlie Limited will still be in full compliance with the Code of Corporate Governance even after Gloria steps down as a director.
C. Charlie Limited must appoint an additional, non-executive director to be in full compliance with the Code of Corporate Governance.
D. Charlie Limited must appoint a lead independent director from amongst the remaining independent directors to be in full compliance with the Code of Corporate Governance.

**Answer: C.** After Gloria leaves there are six directors: three executive and three non-executive. Provision 2.3 requires non-executive directors to be a majority, so another non-executive director is needed. The Chairman is independent, so no ID majority (Provision 2.2) or lead ID (Provision 3.3) is required (D wrong), and three IDs out of six meet Rule 210(5)(c). A makes things worse; B is wrong.
*Cite: CG4 s6; LM r 210(5)(c); CODE Provisions 2.2, 2.3, 3.3; `ccp-1-1-38`*

**Q23-22** · `1.X.3` `1.IX.1` · 2023 CCP Paper 1 Q22 (no official answer) · `ccp-1-1-38` `ccp-1-1-34` `ccp-1-1-37`

Mr Ho is the Chairman of the board of Alpha Limited, listed on the Mainboard. Mr Ho's son is currently employed as an executive director of Alpha Limited. Assuming compliance with other Listing Manual requirements, which statement is true for the purposes of the Code of Corporate Governance?

A. Since Mr Ho is not independent, the majority of the board must consist of independent directors. There must be no variation from this arrangement.
B. Since Mr Ho is not independent, the majority of the board should consist of independent directors under the Code. However, Alpha Limited can explain the reason for any variation from this Code requirement and explain how its practices are still consistent with the intent of the relevant principle.
C. Mr Ho's son's employment does not affect Mr Ho's independence. Mr Ho can, if the Nominating Committee agrees, be the independent Chairman of the board of directors of Alpha Limited.
D. Since Mr Ho is not independent, he cannot be the Chairman of the board of directors of Alpha Limited.

**Answer: B.** An immediate family member employed by the issuer whose remuneration the RC determines (an executive director's package is set on the RC's recommendation) makes Mr Ho not independent (Rule 210(5)(d)(ii)), and where the Chairman is not independent the IDs should be a majority (Provision 2.2) — a Provision, so comply or explain (Rule 710). A: Provisions allow explained variation. C: the mandatory Rule 210(5)(d) tests cannot be waived by the NC. D: the Code does not bar a non-independent Chairman; it calls for an ID majority and a lead ID.
*Cite: LM r 210(5)(d), 710; CODE Provisions 2.2, 3.3, 6.1; `ccp-1-1-38`, `ccp-1-1-34`, `ccp-1-1-37`*

**Q23-31** · `1.X.3` `1.XI.4` · 2023 CCP Paper 1 Q31 (no official answer) · `ccp-1-1-38` `ccp-1-1-43`

Which statement about the lead independent director ("Lead ID") of a listed company's board is false for the purposes of the Code of Corporate Governance?

A. The Lead ID should be the chairman of the Remuneration Committee.
B. The Lead ID should be a member of the Nominating Committee.
C. A Lead ID should be appointed where the Chairman of the board is not independent.
D. The Lead ID should not have an immediate family member similarly employed by the Company whose remuneration is determined by the Remuneration Committee.

**Answer: A.** The Code makes the lead ID a member of the NC (Provision 4.2) and calls for one where the Chairman is not independent (Provision 3.3); as an ID he must pass Rule 210(5)(d)(ii) (D true). Nothing requires him to chair the RC; the RC chairman need only be independent (Provision 6.2).
*Cite: CODE Provisions 3.3, 4.2, 6.2; LM r 210(5)(d); `ccp-1-1-38`, `ccp-1-1-43`*

### 1.X.4 — Director training (Rule 210(5)(a)); re-nomination every 3 years (Rule 720(5))

**Q1-26** · `1.X.4` · own question · `ccp-1-1-39`

A newly appointed director of a Mainboard issuer has never been a director of an SGX-listed company. Which is CORRECT?

A. Training is optional.
B. He must undergo the training prescribed in Practice Note 2.3, unless the NC considers it unnecessary because of other relevant experience and discloses the basis; all directors must also submit for re-nomination and re-appointment at least once every three years.
C. He must retire at the first AGM and may not stand again.
D. He need only attend sustainability training.

**Answer: B.** Rule 210(5)(a) (training) and Rule 720(5) (re-nomination every three years); one-time sustainability training is in addition, not instead (D).
*Cite: CG4 s7; LM r 210(5)(a), 720(5); `ccp-1-1-39`*

### 1.XI Board committees

Sub-points 1.XI.1–1.XI.5. Real questions: Q23-35, Q23-33 (1.XI.2), Q23-37 (1.XI.3), Q23-26, Q23-36 (1.XI.4). Own questions Q1-27, Q1-28.

### 1.XI.1 — Committees required (Rule 210(5)(e)); AC the only one required by statute (s 201B CA)

**Q1-27** · `1.XI.1` · own question · `ccp-1-1-40`

Which board committee of a listed company is prescribed by statute?

A. The Nominating Committee.
B. The Remuneration Committee.
C. The Audit Committee (s 201B CA); the Listing Rules (Rule 210(5)(e)) also require committees performing the functions of an AC, NC and RC, with written terms of reference.
D. The Board Risk Committee.

**Answer: C.** Only the AC is prescribed by law; the NC and RC are required by the Listing Rules. D: the board should consider a risk committee (Provision 9.1), but it is not compulsory.
*Cite: CG4 s8; LM r 210(5)(e); `ccp-1-1-40`*

### 1.XI.2 — Audit Committee: composition, duties, internal audit

**Q23-35** · `1.XI.2` · 2023 CCP Paper 1 Q35 (no official answer) · `ccp-1-1-41`

*Facts for Q23-35 to Q23-37:* Gamma Limited, listed on the Mainboard, asks for advice on which members should form the Audit Committee (AC), Remuneration Committee (RC) and Nominating Committee (NC). Its board: Albert, independent non-executive director with recent and relevant accounting expertise; Bruce, the CEO, with recent and relevant accounting expertise; Charles, non-independent non-executive director with recent and relevant accounting expertise; Darren, independent non-executive director with no recent and relevant accounting expertise and experience.

Which AC composition best complies with the Code of Corporate Governance?

A. AC comprises Darren as the Chairman, Albert and Charles as members.
B. AC comprises Albert as the Chairman, Bruce and Darren as members.
C. AC comprises Albert as the Chairman, Bruce and Charles as members.
D. AC comprises Albert as the Chairman, Darren and Charles as members.

**Answer: D.** The AC needs at least three directors, all non-executive, the majority (including the Chairman) independent, and at least two members, including the Chairman, with recent and relevant accounting expertise (Provision 10.2). D: Albert (ID, expertise) chairs; Darren (ID) gives an independent majority; Charles adds the second expert. A: the Chairman lacks accounting expertise. B and C: Bruce, the CEO, is executive.
*Cite: CG4 s9–10; CODE Provision 10.2; `ccp-1-1-41`*

**Q23-33** · `1.XI.2` `1.XI.3` `1.XI.4` · 2023 CCP Paper 1 Q33 (no official answer) · `ccp-1-1-41` `ccp-1-1-42` `ccp-1-1-43`

Which option correctly matches the duties of the Nominating Committee (NC), Remuneration Committee (RC) and Audit Committee (AC) of a listed company?

A. NC: reviewing whistle-blowing policy and arrangements. RC: reviewing succession plans for directors. AC: making recommendations to the Board on the specific remuneration packages for each director and key management personnel.
B. NC: reviewing succession plans for directors. RC: making recommendations to the Board on the specific remuneration packages for each director and key management personnel. AC: reviewing whistle-blowing policy and arrangements.
C. NC: reviewing succession plans for directors. RC: reviewing whistle-blowing policy and arrangements. AC: making recommendations to the Board on the specific remuneration packages for each director and key management personnel.
D. NC: making recommendations to the Board on the specific remuneration packages for each director and key management personnel. RC: reviewing whistle-blowing policy and arrangements. AC: reviewing succession plans for directors.

**Answer: B.** The NC reviews succession plans (Provision 4.1), the RC recommends specific remuneration packages (Provision 6.1), and the AC reviews the whistle-blowing policy (Provision 10.1).
*Cite: CODE Provisions 4.1, 6.1, 10.1; `ccp-1-1-41`, `ccp-1-1-42`, `ccp-1-1-43`*

### 1.XI.3 — Remuneration Committee

**Q23-37** · `1.XI.3` · 2023 CCP Paper 1 Q37 (no official answer) · `ccp-1-1-42`

Facts as for Q23-35 (Gamma Limited). Which RC composition best complies with the Code of Corporate Governance?

A. RC comprises Charles as the Chairman, Albert and Darren as members.
B. RC comprises Albert as the Chairman, Bruce and Darren as members.
C. RC comprises Darren as the Chairman, Albert and Charles as members.
D. RC comprises Albert as the Chairman, Bruce and Darren as members.

**Answer: C.** The RC needs at least three directors, all non-executive, the majority (including the Chairman) independent (Provision 6.2). C: Darren (ID) chairs, Albert (ID) and Charles (non-executive). A: Charles, the Chairman, is not independent. B and D (identical on the screen): Bruce, the CEO, is executive.
*Cite: CG4 s11; CODE Provision 6.2; `ccp-1-1-42`*

See also Q23-33 under 1.XI.2.

### 1.XI.4 — Nominating Committee

**Q23-36** · `1.XI.4` · 2023 CCP Paper 1 Q36 (no official answer) · `ccp-1-1-43`

Facts as for Q23-35 (Gamma Limited). Which NC composition best complies with the Code of Corporate Governance?

A. NC comprises Albert as the Chairman, Bruce and Charles as members.
B. NC comprises Albert as the Chairman, Bruce and Darren as members.
C. NC comprises Bruce as the Chairman, Albert and Darren as members.
D. NC comprises Charles as the Chairman, Albert and Darren as members.

**Answer: B.** The NC needs at least three directors, the majority (including the Chairman) independent, and unlike the AC and RC it may include the CEO (Provision 4.2). B: Albert (ID) chairs, Darren (ID) gives the majority, Bruce may sit. A: only one of three is independent. C and D: the Chairman is not independent.
*Cite: CG4 s12–13; CODE Provision 4.2; `ccp-1-1-43`*

**Q23-26** · `1.XI.4` · 2023 CCP Paper 1 Q26 (no official answer) · `ccp-1-1-43`

Which statement about the Nominating Committee of a Mainboard company under the Code of Corporate Governance is false?

A. The lead independent director should be a member of the Nominating Committee.
B. The majority of the Nominating Committee, including the Chairman of the Nominating Committee, should be independent.
C. An executive director can be a member of the Nominating Committee.
D. The Nominating Committee must not comprise more than 3 directors.

**Answer: D.** The NC has at least three directors, not at most three. A, B and C are true (Provision 4.2).
*Cite: CODE Provision 4.2; `ccp-1-1-43`*

See also Q23-31 under 1.X.3 and Q23-33 under 1.XI.2.

### 1.XI.5 — Board risk committee; board's comment on internal controls (Rule 1207(10))

**Q1-28** · `1.XI.5` · own question · `ccp-1-1-44`

What must the board of a listed issuer say in its annual report about internal controls?

A. Nothing; that is the external auditors' job.
B. It must comment on the adequacy and effectiveness of the internal controls (financial, operational, compliance and IT) and risk management systems, state whether the AC concurs, and disclose any material weaknesses and the steps taken (Rule 1207(10)).
C. Only that a board risk committee has been set up.
D. Only whether the CEO is satisfied with the controls.

**Answer: B.** Rule 1207(10) and PN 12.2. C: a board risk committee is something the board should consider (Provision 9.1), not the required statement.
*Cite: CG4 s14; LM r 1207(10); `ccp-1-1-44`*

### 1.XII Remuneration disclosure

Sub-points 1.XII.1–1.XII.2. Real questions: QSQ-G1, Q23-20 (1.XII.2). Own question Q1-29.

### 1.XII.1 — Principle 8; Provisions 8.1–8.3

**Q1-29** · `1.XII.1` · own question · `ccp-1-1-45`

Under Provision 8.1 of the Code, how is the remuneration of the top five key management personnel (who are not directors or the CEO) disclosed?

A. Exactly, to the dollar, mandatorily.
B. In bands no wider than S$250,000, with their aggregate total, on a comply-or-explain basis.
C. In bands no wider than S$100,000.
D. Not at all.

**Answer: B.** Provision 8.1. C: S$100,000 bands apply under Provision 8.2 to employees who are substantial shareholders or immediate family of a director, the CEO or a substantial shareholder and earn over S$100,000. A: exact, mandatory disclosure applies only to each director and the CEO (Rule 1207(10D)).
*Cite: CG4 s15; CODE Provisions 8.1–8.2; `ccp-1-1-45`*

### 1.XII.2 — Rule 1207(10D): mandatory disclosure for each director and the CEO

**QSQ-G1** · `1.XII.2` · SQ p13 Q1 [Part B 2024], official key A · `ccp-1-1-46`

Which statement(s) about remuneration disclosure in the annual report of a listed company is/are TRUE?

I. A listed company must disclose the amounts and breakdown of remuneration for each individual director.
II. A listed company can choose not to disclose the bonuses and share-based incentives and awards in the remuneration breakdown for each individual director, as long as it explains the reason for the variation.
III. A listed company can choose not to disclose the remuneration of its Chief Executive Officer as long as he is not also a director.

A. I only.
B. I and II.
C. II and III.
D. I, II and III.

**Answer: A.** Rule 1207(10D) requires names, amounts and a full percentage breakdown (including bonuses and share-based incentives) for each director and the CEO, whether or not the CEO is a director; as a Listing Rule it cannot be explained away.
*Cite: CG4 s16; LM r 1207(10D); SQ p114 (key A); `ccp-1-1-46`*

**Q23-20** · `1.XII.2` · 2023 CCP Paper 1 Q20 (no official answer) · `ccp-1-1-46`

Which statements about remuneration disclosure will be true for listed companies preparing annual reports for financial years ending on or after 31 December 2024?

I. A listed company must disclose the amounts and breakdown of remuneration for each individual director.
II. A listed company can choose not to disclose the bonuses and share-based incentives and awards in the remuneration breakdown for each individual director, as long as it explains the reason for the variation.
III. A listed company can choose not to disclose the remuneration of its Chief Executive Officer as long as it explains the reason for the variation.

A. I only.
B. I, II and III.
C. I and II only.
D. I and III only.

**Answer: A.** Same rule as QSQ-G1 (Rule 1207(10D), mandatory from FYs ending on or after 31 Dec 2024).
*Cite: LM r 1207(10D); `ccp-1-1-46`*

### 1.XIII Market conduct (SFA Part 12)

Sub-points 1.XIII.1–1.XIII.5. No real question; own questions Q1-30 to Q1-35.

### 1.XIII.1 — False trading, market rigging and market manipulation (ss 197–198)

**Q1-30** · `1.XIII.1` · own question · `ccp-1-1-47`

A trader places matched buy and sell orders in a thinly traded stock through two accounts he controls, to make the stock look actively traded. Which provision does this most directly contravene?

A. s 197 SFA (false trading and market rigging).
B. s 218 SFA (insider trading by a connected person).
C. s 203 SFA (continuous disclosure).
D. s 331 SFA (officers' liability).

**Answer: A.** s 197 prohibits conduct whose purpose (or one purpose) is, or which is likely, to create a false or misleading appearance of active trading. s 198 covers two or more transactions affecting the price with intent to induce others to deal. B, C and D deal with other matters.
*Cite: SFA12 p3–5 (ss 197–198); `ccp-1-1-47`*

### 1.XIII.2 — False or misleading statements, fraudulent inducement, deceptive devices (ss 199–201)

**Q1-31** · `1.XIII.2` · own question · `ccp-1-1-48`

A director posts online that his listed company has "secured a S$500m contract", not caring whether it is true; it is not. The share price jumps. Which provision applies?

A. s 199 SFA: a false or misleading statement in a material particular likely to induce dealing or affect the price, made by someone who does not care whether it is true or knows or ought reasonably to know it is false.
B. s 215 SFA, the definition of "generally available".
C. s 223 SFA, the underwriters' exception.
D. No provision; only the company's own announcements are regulated.

**Answer: A.** s 199 catches the statement; s 200 (inducing dealing by misleading statements, promises or forecasts) may also apply. B and C are a definition and a defence.
*Cite: SFA12 p6–7 (ss 199–201); `ccp-1-1-48`*

### 1.XIII.3 — Insider trading: connected and other persons; "generally available"; material effect (ss 215–220)

**Q1-32** · `1.XIII.3` · own question · `ccp-1-1-49`

An employee of a listed company learns of an unannounced takeover offer and buys shares. Which is CORRECT?

A. The prosecution must prove he intended to use the information.
B. As a connected person, once possession of the information and its non-availability are proved, he is presumed to know it was not generally available and price-sensitive (s 218(4)); intention to use it need not be proved (s 220).
C. He is liable only if he made a profit.
D. Employees are not connected persons.

**Answer: B.** An employee is an officer and so a connected person (s 218(5)); knowledge is presumed (s 218(4)) and intention need not be proved (s 220(1)). For a non-connected insider, the prosecution must prove knowledge (s 219).
*Cite: SFA12 p16–23 (ss 215–220); `ccp-1-1-49`*

**Q1-33** · `1.XIII.3` · own question · `ccp-1-1-49`

When is information "generally available" under s 215 SFA?

A. As soon as one newspaper journalist hears it.
B. When it is readily observable; or has been made known in a manner likely to bring it to the attention of persons who commonly invest in such securities and a reasonable period for dissemination has elapsed; or consists of deductions from such information.
C. Only after the next periodic report.
D. Only once SGX confirms it.

**Answer: B.** s 215(a)–(c).
*Cite: SFA12 p16–23 (s 215); `ccp-1-1-49`*

### 1.XIII.4 — Insider trading defences, incl. parity of information (s 231)

**Q1-34** · `1.XIII.4` · own question · `ccp-1-1-50`

A director sells shares in his listed company to a buyer who, he proves, already knew the same price-sensitive information before the deal. Which is CORRECT?

A. He has no defence because he is a connected person.
B. He has the s 231(1) defence that the other party knew, or ought reasonably to have known, the information before the transaction (parity of information).
C. He has a defence only if he made no profit.
D. He has the s 223 underwriters' defence.

**Answer: B.** s 231(1). C has no basis; D applies to underwriters.
*Cite: SFA12 p24–29 (ss 222–231); `ccp-1-1-50`*

### 1.XIII.5 — Sanctions: criminal (ss 204, 221), civil penalty (s 232), civil liability (s 234)

**Q1-35** · `1.XIII.5` · own question · `ccp-1-1-51`

In a civil penalty action by MAS for insider trading, what is the maximum penalty the court may order against an individual?

A. S$250,000 only.
B. The greater of 3 times the profit gained or loss avoided, or S$2 million (minimum S$50,000 for an individual, S$100,000 for a corporation).
C. 7 years' imprisonment.
D. Twice the profit gained.

**Answer: B.** s 232(1)–(3), on a balance of probabilities, brought with the Public Prosecutor's consent within 6 years (s 233). A and C are the criminal maxima (ss 204, 221). Contemporaneous traders may also claim compensation (s 234).
*Cite: SFA12 p29–32 (ss 232–234); `ccp-1-1-51`*

## 2 · Insolvency & Corporate Restructuring

### 2.I Liquidation: overview

Sub-points 2.I.1–2.I.2. Real question: Q21I-25 (2.I.2). Own question Q2-1. The 2021 INS screens begin: "Please select the most appropriate answer. The IRDA refers to the Insolvency, Restructuring and Dissolution Act 2018."

### 2.I.1 — What liquidation is; IRDA framework and transition; compulsory v voluntary (MVL / CVL)

**Q2-1** · `2.I.1` · own question · `ccp-1-2-1`

A winding-up application is filed against a company in 2026. Which statute governs, and which kind of winding up is it if ordered?

A. The Companies Act insolvency provisions; a creditors' voluntary winding up.
B. The IRDA, because the relevant event (the application) occurred after 30 July 2020; a compulsory winding up by the Court.
C. The Bankruptcy Act; a members' voluntary winding up.
D. The IRDA; a members' voluntary winding up.

**Answer: B.** The IRDA (in force 30 July 2020) applies where the relevant event occurs after that date. A winding up on an application to court is compulsory; members' voluntary winding up is for solvent companies and creditors' voluntary for insolvent ones that resolve to wind up. The Bankruptcy Act and the Companies Act's insolvency provisions were repealed.
*Cite: INS1 s2–5; INS-CS1 p4–5, p8; `ccp-1-2-1`*

### 2.I.2 — When winding up commences (ss 126, 161(6))

**Q21I-25** · `2.I.2` · 2021 INS Q25 (no official answer) · `ccp-1-2-2`

In a winding up by the court, the winding up is deemed to have commenced ____

A. at the time of the filing of the winding up application.
B. at the time of the making of the winding up order.
C. at the time a statutory demand is served on the debtor.
D. 3 weeks after a statutory demand is served on the debtor.

**Answer: A.** A winding up by the Court is deemed to commence when the application is made (s 126(2)); the order's effects relate back. A voluntary winding up commences on the resolution (s 161(6)).
*Cite: IRDA ss 126(2), 161(6); INS-CS1 p5, p16; `ccp-1-2-2`*

### 2.II Compulsory winding up: standing and grounds

Sub-points 2.II.1–2.II.7. Real questions: Q21I-26 (2.II.1), Q21I-3 (2.II.2), QSQ-I3, QSQ-I7, Q23-45, Q21I-17 (2.II.4), QSQ-I1, QSQ-I2, Q23-43 (2.II.6). Own questions Q2-2 to Q2-4.

### 2.II.1 — Who may apply (s 124(1)); contingent and prospective creditors

**Q21I-26** · `2.II.1` `2.XI.2` `2.X.1` · 2021 INS Q26 (no official answer) · `ccp-1-2-3` `ccp-1-2-55` `ccp-1-2-45`

Which of the following statements is/are wrong?

(I) A compulsory winding up by the court can only be obtained through an application by one of its creditors.
(II) After a company makes an application under section 64 of the IRDA, it enjoys an automatic interim moratorium of 90 days.
(III) A liquidator of a company can set aside a transaction as an unfair preference if it can be shown that the company received no consideration under the transaction.

A. (III) only.
B. All are wrong.
C. (I) and (III).
D. (I) only.

**Answer: B.** (I): the company, a contributory, a liquidator, a judicial manager, the Minister or MAS may also apply (s 124(1)). (II): the automatic interim moratorium is 30 days (s 64(14)). (III): receiving no consideration is the mark of a transaction at an undervalue (s 224), not an unfair preference (s 225).
*Cite: IRDA ss 64(14), 124(1), 224–225; `ccp-1-2-3`, `ccp-1-2-55`, `ccp-1-2-45`*

**Q2-2** · `2.II.1` · own question · `ccp-1-2-3`

A landlord's tenant company will owe rent under an existing lease for the next three years, but nothing is due yet. Can the landlord apply to wind up the company?

A. No; only creditors with debts presently due can apply.
B. Yes, as a contingent or prospective creditor: a person towards whom, under an existing obligation, the company may or will become subject to a present liability on a future event or date (s 124(1)(c); *Re People's Parkway Development*).
C. Only with the shareholders' consent.
D. Only if the company is in voluntary liquidation.

**Answer: B.** s 124(1) lets a creditor "including a contingent or prospective creditor" apply. C and D have no basis.
*Cite: INS1 s7–8; IRDA s 124(1); `ccp-1-2-3`*

### 2.II.2 — Procedure for a winding-up application

**Q21I-3** · `2.II.2` `2.V.1` · 2021 INS Q3 (no official answer) · `ccp-1-2-4` `ccp-1-2-17`

Tom wishes to apply to court to wind up a debtor company, but does not wish to nominate a private liquidator. Which statement is correct?

A. Tom can choose not to nominate a private liquidator and in the absence of such nomination, the Official Receiver must be appointed as the liquidator.
B. If Tom, as the creditor applying for the winding up order, nominates a private liquidator, no other party can object to such nomination.
C. Tom may nominate the Official Receiver to be appointed as liquidator only if Tom has taken reasonable steps but is unable to obtain the consent of a private liquidator to be appointed as liquidator, and the Official Receiver consents to being nominated.
D. If there is no agreement between the parties on who to appoint as the liquidator, the court hearing the winding up application will always appoint the Official Receiver as the liquidator.

**Answer: C.** The applicant must nominate a licensed insolvency practitioner and file his written consent (s 135(1)–(2)); he may nominate the Official Receiver only if he took reasonable steps but could not get a practitioner's consent and the OR consents (s 135(3)). A contradicts s 135(1); B and D have no basis.
*Cite: IRDA-2018 s 135(1)–(3); INS1 s21–25; `ccp-1-2-4`, `ccp-1-2-17`*

**Q2-3** · `2.II.2` · own question · `ccp-1-2-4`

Which of these is NOT a usual step in a creditor's winding-up application?

A. Filing an originating application supported by affidavit.
B. Advertising the application.
C. Paying a deposit to the Official Receiver.
D. Obtaining the shareholders' consent to the application.

**Answer: D.** The application is made by originating application with an affidavit, advertised, served on the company, and the applicant pays a deposit to the OR; persons intending to appear give notice. No shareholder consent is needed.
*Cite: INS1 s9–10; Cyril-INS §1.2.2; `ccp-1-2-4`*

### 2.II.3 — Inability to pay debts (s 125(1)(e)): the three routes in s 125(2)

**Q2-4** · `2.II.3` · own question · `ccp-1-2-5`

A creditor obtains judgment against a company and the sheriff's execution is returned unsatisfied. Which statement is CORRECT?

A. The creditor must still serve a statutory demand before applying.
B. The company is deemed unable to pay its debts under s 125(2)(b), one of three routes alongside an unpaid statutory demand (s 125(2)(a)) and proof to the Court's satisfaction, counting contingent and prospective liabilities (s 125(2)(c)).
C. Unsatisfied execution is irrelevant to a winding up.
D. Only the company itself can rely on s 125(2).

**Answer: B.** Each route is an alternative; inability to pay is the usual ground (s 125(1)(e)). A judgment is not itself a prerequisite to applying.
*Cite: INS1 s11–12; IRDA s 125(2); `ccp-1-2-5`*

### 2.II.4 — Statutory demand: over S$15,000, 3 weeks, pay / secure / compound

**QSQ-I3** · `2.II.4` · SQ p19 Q3 [Part B 2024], official key A · `ccp-1-2-6`

For the purposes of a winding up application against a debtor company, a debtor company is deemed to be unable to pay its debts if a statutory demand for a sum exceeding S$15,000 has been served on the company, and the company has for a period of ____ neglected to pay the sum, or to secure or compound the sum to the reasonable satisfaction of the creditor.

A. 3 weeks.
B. 2 weeks.
C. 6 months.
D. 1 month.

**Answer: A.** s 125(2)(a) IRDA: 3 weeks.
*Cite: IRDA s 125(2)(a); SQ p114 (key A); `ccp-1-2-6`*

**Q23-45** · `2.II.4` · 2023 CCP Paper 1 Q45 (no official answer) · `ccp-1-2-6`

Same stem as QSQ-I3. Options: A. 2 weeks. B. 3 weeks. C. 1 month. D. 6 months.

**Answer: B.** 3 weeks (s 125(2)(a)).
*Cite: IRDA s 125(2)(a); `ccp-1-2-6`*

**Q21I-17** · `2.II.4` · 2021 INS Q17 (no official answer) · `ccp-1-2-6`

Same stem as QSQ-I3. Options: A. 2 weeks. B. 1 month. C. 3 weeks. D. 6 months.

**Answer: C.** 3 weeks (s 125(2)(a)).
*Cite: IRDA s 125(2)(a); `ccp-1-2-6`*

**QSQ-I7** · `2.II.4` `2.II.3` · SQ p21 Q7 [Part B 2025 S1], official key D · `ccp-1-2-6` `ccp-1-2-5`

Luka Pte Ltd supplies basketball equipment monthly to Maverick Pte Ltd, which pays S$2,000 every month. Maverick failed to pay for December 2024's equipment. On 1 January 2025, Luka served a statutory demand on Maverick for the unpaid delivery. It is now 1 February 2025. Can Luka apply to wind up Maverick, and why?

A. Yes, Maverick is now deemed unable to pay its debts on the basis of the statutory demand.
B. Yes, because it is just and equitable for Maverick to be wound up.
C. No, because Luka has yet to commence legal proceedings and obtain judgment against Maverick.
D. No, Maverick is not deemed to be unable to pay its debt notwithstanding the statutory demand.

**Answer: D.** A statutory demand founds the presumption only for a debt exceeding S$15,000; S$2,000 does not, however long it is unpaid. B: no just-and-equitable facts. C: a judgment is not a prerequisite.
*Cite: IRDA s 125(2)(a); INS1 s13–14; SQ p114 (key D); `ccp-1-2-6`, `ccp-1-2-5`*

### 2.II.5 — Cash-flow test of insolvency (Sun Electric)

**Q2-5** · `2.II.5` · own question · `ccp-1-2-7`

Under *Sun Electric Power v RCMA Asia* [2021] SGCA 60, how does the Court decide whether a company is unable to pay its debts?

A. Balance-sheet test only: total assets against total liabilities.
B. Cash-flow test: whether its current assets exceed its current liabilities so that it can meet its debts as they fall due within a 12-month timeframe, looking at factors such as debts due, demands, payment history, liquid assets and financing.
C. Whether its share price has fallen.
D. Whether it has paid a dividend in the last year.

**Answer: B.** The Court of Appeal adopted the cash-flow test over a 12-month horizon.
*Cite: INS1 s17; INS-SYL p1; `ccp-1-2-7`*

### 2.II.6 — Disputed debt and cross-claim; abuse of process

**QSQ-I1** · `2.II.6` · SQ p18 Q1 [Part B 2024], official key C · `ccp-1-2-8`

Stoke Pte Ltd supplies raw materials monthly to United Pte Ltd. In 2022 United sued Stoke for damaging United's premises during a delivery and obtained judgment against Stoke; Stoke has not paid the judgment sum. The supply contract continued. United now says it cannot pay for the June–December 2024 deliveries, and does not dispute that debt. Can Stoke apply to wind up United, and why?

A. No, because Stoke has not obtained judgment against United and so the winding up application will fail as a result.
B. No, because a winding up application cannot be used as a means to coerce a debtor to make payment and Stoke's winding up application will be an abuse of process.
C. Yes, but only if Stoke's undisputed claim against United exceeds United's claim against it.
D. Yes, because United's claim against Stoke is irrelevant – as long as United is unable to pay the debt owed to Stoke under the supply contract Stoke is entitled to apply to wind up United.

**Answer: C.** United's unpaid judgment is a genuine cross-claim; it defeats the application if it equals or exceeds Stoke's debt. A: no judgment is needed. B: an undisputed debt is a proper basis. D: the cross-claim is relevant.
*Cite: INS1 s15–16; INS-CS1 p14–15; SQ p114 (key C); `ccp-1-2-8`*

**Q23-43** · `2.II.6` · 2023 CCP Paper 1 Q43 (no official answer) · `ccp-1-2-8`

Mr Broke, a sole proprietor, supplies raw materials monthly to Stonks Pte Ltd. In 2021 Stonks sued him for knocking over and injuring 5 of its employees while making a delivery. The supply contract continued. Stonks now says it cannot pay him for his June–December 2022 deliveries, and does not dispute that debt. Can he apply to wind up Stonks, and why?

A. No, because Mr Broke has not obtained judgment against Stonks and so his winding up application will fail as a result.
B. No, because a winding up application cannot be used as a means to coerce a debtor to make payment and Mr Broke's winding up application will be an abuse of process.
C. Yes, because Stonks is unable to pay the debt owed to Mr Broke as it fell due. The claim by Stonks is irrelevant.
D. Yes, but only if Mr Broke's undisputed claim against Stonks exceeds Stonks' claim against him.

**Answer: D.** Same rule as QSQ-I1: a genuine cross-claim equal to or exceeding the debt defeats the application. (The candidate's selection, D, is right.)
*Cite: INS1 s15–16; INS-CS1 p14–15; `ccp-1-2-8`*

**QSQ-I2** · `2.II.6` · SQ pp18–19 Q2 [Part B 2024], official key D · `ccp-1-2-8`

Mega Farmer Pte Ltd supplies fruit to Papaya Tree Pte Ltd and set up a S$2 million escrow account that Papaya Tree may draw on only if found to suffer loss from poor-quality fruit. In 2020 Mega Farmer lent Papaya Tree S$3 million interest-free, recallable on demand and secured by a personal guarantee from Papaya Tree's managing director, Mr Papy. After complaints of worms and a prohibited pesticide in fruit supplied by Mega Farmer, Papaya Tree sued Mega Farmer for S$3 million in losses. Mega Farmer then served a statutory demand for repayment of the S$3 million loan and, when it went unpaid, applied to wind up Papaya Tree. Can Papaya Tree successfully resist the winding up application?

A. No, because the escrow account monies represent a security which reduces the amount of Papaya Tree's claim against Mega Farmer such that Papaya Tree's claim is now lesser than Mega Farmer's claim.
B. Yes, because Mega Farmer cannot proceed with the winding up application without first claiming from Mr Papy pursuant to the personal guarantee.
C. No, because until the court grants an order in favour of Papaya Tree against Mega Farmer, Papaya Tree is not considered to have a genuine cross-claim on substantial grounds.
D. Yes, so long as Papaya Tree can satisfy the Court that it has a genuine cross-claim based on substantial grounds that is equal to or more than Mega Farmer's claim.

**Answer: D.** A genuine cross-claim on substantial grounds (a triable issue) that equals or exceeds the debt defeats the application. A: the escrow does not reduce the cross-claim. B: the creditor need not first call on the guarantee. C: no judgment is needed for a cross-claim to count.
*Cite: INS1 s15–16; INS-CS1 p14–15; SQ p114 (key D); `ccp-1-2-8`*

### 2.II.7 — Court's discretion not to wind up; public interest

**Q2-6** · `2.II.7` · own question · `ccp-1-2-9`

A company is temporarily unable to pay a large debt but is commercially viable, employs hundreds and has supportive creditors. Must the Court wind it up on a creditor's application?

A. Yes; once inability to pay is shown, a winding-up order is mandatory.
B. No; the Court has a discretion (s 128) and may consider public interest elements such as the effect on employees, creditors, suppliers and shareholders, and the wishes of creditors and contributories (s 201), and may adjourn.
C. No, because the company has employees.
D. Yes, unless the shareholders object.

**Answer: B.** *BNP Paribas v Jurong Shipyard* at [19]; C overstates it; D has no basis.
*Cite: INS1 s18; INS-CS1 p15; `ccp-1-2-9`*

### 2.III Voluntary winding up

Sub-points 2.III.1–2.III.3. Real question: Q21I-21 (2.III.2). Own questions Q2-7, Q2-8.

### 2.III.1 — When a company may wind up voluntarily (s 160); steps after the resolution

**Q2-7** · `2.III.1` · own question · `ccp-1-2-10`

How does a company resolve to wind itself up voluntarily when its constitution fixes no duration, and what must follow?

A. By ordinary resolution; no filings needed.
B. By special resolution (s 160(1)); within 7 days it lodges the resolution with the Registrar and gives notice in the Gazette and a local English daily.
C. By board resolution alone.
D. By application to court.

**Answer: B.** s 160(1)(b) requires a special resolution; (a) covers expiry of a constitution-fixed period or event plus a general meeting resolution.
*Cite: INS-SYL p2; Cyril-INS §1.3.1; `ccp-1-2-10`*

### 2.III.2 — Members' voluntary winding up: declaration of solvency

**Q21I-21** · `2.III.2` · 2021 INS Q21 (no official answer) · `ccp-1-2-11`

Tom, the sole shareholder of a company facing financial difficulty, asks whether the company can be placed in a members' voluntary liquidation. Which is correct?

A. Only solvent companies can be placed in a members' voluntary liquidation.
B. A company can be placed in a liquidation only by way of a court application.
C. A company cannot be placed in a liquidation if there is only one shareholder.
D. All companies can be placed in a members' voluntary liquidation so long as all the shareholders agree.

**Answer: A.** An MVL needs a directors' declaration that the company will pay its debts in full within 12 months (s 163); an insolvent company uses a creditors' voluntary winding up instead. B: voluntary winding up needs no court. C and D have no basis.
*Cite: IRDA s 163; INS-SYL p2; `ccp-1-2-11`*

**Q2-8** · `2.III.2` · own question · `ccp-1-2-11`

In a members' voluntary winding up, the liquidator forms the view that the company will not pay its debts in full within the period in the declaration of solvency. What must he do?

A. Continue the MVL regardless.
B. Summon a creditors' meeting (s 165); the winding up proceeds as a creditors' voluntary winding up.
C. Apply for the directors' imprisonment.
D. Apply to annul the winding up.

**Answer: B.** s 165. The declaration (majority of directors, 12 months, with a statement of affairs) must be lodged before the resolution (s 163).
*Cite: INS-SYL p2; Cyril-INS §1.3.2; `ccp-1-2-11`*

### 2.III.3 — Creditors' voluntary winding up: statutory declaration, creditors' meeting, liquidator

**Q2-9** · `2.III.3` · own question · `ccp-1-2-12`

In a creditors' voluntary winding up, the members nominate Ms A as liquidator and the creditors nominate Mr B. Who is liquidator?

A. Ms A, because the members passed the winding-up resolution.
B. Mr B, because where the two meetings nominate different persons the creditors' nominee is liquidator (s 167).
C. Both, jointly.
D. The Official Receiver.

**Answer: B.** If the creditors nominate no one, the company's nominee is liquidator. The process starts with the directors' statutory declaration that the company cannot by reason of its liabilities continue its business, and a provisional liquidator (s 161).
*Cite: INS-CS1 p9; INS-SYL p2; `ccp-1-2-12`*

### 2.IV Effect of winding up

Sub-points 2.IV.1–2.IV.4. Real questions: QSQ-I4, Q23-46, Q21I-18, Q21I-35 (2.IV.2). Own questions Q2-10 to Q2-12.

### 2.IV.1 — After the application: stay of proceedings (s 129)

**Q2-10** · `2.IV.1` · own question · `ccp-1-2-13`

A winding-up application has been filed but not yet heard. A supplier is suing the company in a separate action. What can the company or another creditor do?

A. Nothing until the order is made.
B. Apply to the Court to stay or restrain the action (s 129); the stay is discretionary and on terms.
C. The action is automatically stayed by the filing.
D. Ask the Official Receiver to strike it out.

**Answer: B.** Between application and order, s 129 gives a discretionary stay on application; the automatic stay comes with the order (s 133).
*Cite: INS1 s19; INS-CS1 p16; `ccp-1-2-13`*

### 2.IV.2 — After the order: no proceedings without leave (s 133)

**QSQ-I4** · `2.IV.2` · SQ p20 Q4 [Part B 2024], official key D · `ccp-1-2-14`

When a winding up order has been made against a company, no legal action or proceeding may be proceeded with or commenced against the company except: ____

A. in cases where such legal action or proceeding involves a claim exceeding S$15,000.
B. with the permission of all the shareholders of the company.
C. in cases where the directors of the company had breached their duties owed to the creditors.
D. with the permission of the court.

**Answer: D.** s 133(1): only with the leave of the Court.
*Cite: IRDA s 133(1); SQ p114 (key D); `ccp-1-2-14`*

**Q23-46** · `2.IV.2` · 2023 CCP Paper 1 Q46 (no official answer) · `ccp-1-2-14`

Same stem as QSQ-I4. Options: A. with the permission of all the shareholders of the company. B. in cases where such legal action or proceeding involves a claim exceeding S$15,000. C. in cases where the directors had breached their duties owed to the creditors. D. with the permission of the court.

**Answer: D.** s 133(1).
*Cite: IRDA s 133(1); `ccp-1-2-14`*

**Q21I-18** · `2.IV.2` · 2021 INS Q18 (no official answer) · `ccp-1-2-14`

Same stem as QSQ-I4. Options: A. with the permission of all the shareholders. B. claim exceeding S$15,000. C. directors breached duties owed to creditors. D. with the permission of the court.

**Answer: D.** s 133(1).
*Cite: IRDA s 133(1); `ccp-1-2-14`*

**Q21I-35** · `2.IV.2` `2.IX.6` `0.IV.8` · 2021 INS Q35 (no official answer) · `ccp-1-2-14` `ccp-1-2-43` `ccp-1-0-25`

Which statement correctly describes the similarities or differences between the rights of a secured creditor in a liquidation and in a judicial management?

A. A secured creditor can enforce its security rights in both a liquidation and a judicial management if the directors of the debtor company do not oppose such enforcement.
B. A secured creditor's ability to enforce its security rights is generally restrained in a liquidation but not in a judicial management.
C. In both a liquidation and a judicial management, a secured creditor may enforce its security rights with the permission of the court.
D. A secured creditor can never enforce its security rights so long as the company is in a liquidation or a judicial management.

**Answer: C.** It is the only statement true of both: in JM no step may be taken to enforce security without leave (ss 95–96); in a liquidation a secured creditor can generally stand outside it and enforce, and any proceedings against the company need leave (s 133). A: directors' views are irrelevant (and in JM their powers have passed to the judicial manager). B reverses the position. D: enforcement is possible with leave.
*Cite: IRDA ss 95, 96, 133; RL-Sec p6–7; `ccp-1-2-14`, `ccp-1-2-43`, `ccp-1-0-25`*

### 2.IV.3 — Void dispositions and executions; directors functus officio

**Q2-11** · `2.IV.3` · own question · `ccp-1-2-15`

A winding-up order is made on 1 June on an application filed on 1 April. On 15 May the directors transferred company shares held by a member to a buyer and sold a company van. What is the position?

A. Both are valid because they predate the order.
B. Both are void unless the Court orders otherwise, because they were made after the commencement of the winding up (the application date) (s 130(1)); on the order the directors became functus officio.
C. Only the van sale is void.
D. Both are voidable at the buyer's option.

**Answer: B.** s 130(1) covers dispositions of property and share transfers after commencement; executions put in force after commencement are also void (s 130(2)).
*Cite: INS1 s20–21; IRDA s 130; `ccp-1-2-15`*

### 2.IV.4 — Effect of voluntary winding up (ss 162, 170)

**Q2-12** · `2.IV.4` · own question · `ccp-1-2-16`

Which statement about a company in voluntary winding up is CORRECT?

A. Its corporate existence ends on the resolution.
B. Its corporate state and powers continue until dissolution, but it must cease business except as the liquidator considers necessary for its beneficial winding up; share transfers without the liquidator's sanction are void; and no action may be brought without leave of court (ss 162, 170).
C. It may carry on business as usual.
D. Creditors may levy execution freely.

**Answer: B.** ss 162 and 170.
*Cite: INS-SYL p3; IRDA ss 162, 170; `ccp-1-2-16`*

### 2.V The liquidator and the end of the liquidation

Sub-points 2.V.1–2.V.3. Real questions: Q21I-3 (2.V.1, under 2.II.2), Q21I-30 (2.V.1, under 2.IX.7). Own questions Q2-13 to Q2-15.

### 2.V.1 — Liquidator / Official Receiver: status, duties, powers, statement of affairs

See Q21I-3 under 2.II.2 and Q21I-30 under 2.IX.7.

**Q2-13** · `2.V.1` · own question · `ccp-1-2-17`

A liquidator sold an asset without the sanction s 144 required and now asks the Court to authorise the sale retrospectively. What is the likely result?

A. The Court will routinely ratify it.
B. The Court will not authorise acts retrospectively where sanction was required (*Re Kirkham* [2023] 5 SLR 635).
C. Sanction is never needed for sales.
D. The creditors can ratify it by simple majority without the Court.

**Answer: B.** The liquidator is an officer of the Court with fiduciary duties; his powers are in s 144 (s 177 in voluntary winding up).
*Cite: INS1 s21–25; INS-SYL p3; `ccp-1-2-17`*

### 2.V.2 — Estate costs rule

**Q2-14** · `2.V.2` · own question · `ccp-1-2-18`

A liquidator sues in the company's name and loses, with costs ordered against the company. How do those adverse costs rank?

A. As an unsecured debt, pari passu.
B. In priority over the other general expenses of the liquidation and the unsecured creditors (the estate costs rule); a liquidator who pays out in breach is personally liable.
C. Behind all creditors.
D. They cannot be recovered at all.

**Answer: B.** *Ho Wing On Christopher v ECRC Land* [2006] 4 SLR(R) 817.
*Cite: INS1 s35; `ccp-1-2-18`*

### 2.V.3 — Dissolution and release; declaring a dissolution void

**Q2-15** · `2.V.3` · own question · `ccp-1-2-19`

A company was dissolved after its liquidation 18 months ago. A creditor discovers an undisclosed asset. Can the dissolution be undone?

A. No; dissolution is final.
B. Yes; the Court may declare a dissolution void at any time within 2 years of the date of dissolution (s 208).
C. Only within 6 months.
D. Only by the Registrar, without the Court.

**Answer: B.** s 208; the liquidator's release and the dissolution itself are under ss 147–149.
*Cite: INS1 s36; INS-SYL p4–5; `ccp-1-2-19`*

### 2.VI Claims and distribution in liquidation

Sub-points 2.VI.1–2.VI.5. Real questions: Q21I-2 (2.VI.4), Q21I-27 (2.VI.5). Own questions Q2-16 to Q2-18.

### 2.VI.1 — Pari passu principle; no contracting out

**Q2-16** · `2.VI.1` · own question · `ccp-1-2-20`

A main contract provides that if the subcontractor (the company) is liquidated, the employer will pay the company's unsecured suppliers directly out of sums due to the company. Is the clause effective in the company's liquidation?

A. Yes; freedom of contract prevails.
B. No; parties cannot contract out of pari passu distribution (s 172), and such terms are struck down (*Joo Yee Construction v Diethelm Industries*).
C. Yes, if the suppliers are Singapore companies.
D. Only for debts under S$15,000.

**Answer: B.** Pari passu means like creditors are treated alike according to rank; it cannot be displaced by contract.
*Cite: INS1 s26–27; `ccp-1-2-20`*

### 2.VI.2 — Order of priority; preferential debts (s 203)

**Q2-17** · `2.VI.2` · own question · `ccp-1-2-21`

In a compulsory liquidation, which of these is paid first out of the free assets under s 203(1)?

A. Employees' unpaid wages.
B. Tax assessed before commencement.
C. The costs and expenses of the winding up incurred by the Official Receiver as liquidator.
D. The applicant's costs of the winding-up order.

**Answer: C.** s 203(1)(a) comes first, then other winding-up expenses (b), the applicant's costs (c), wages (d), retrenchment benefits (e), work injury compensation (f), CPF (g), vacation leave pay (h) and tax (i). Preferential debts are paid ahead of floating charge holders from floating-charge assets if free assets are insufficient.
*Cite: IRDA s 203(1); INS1 s26, s28; `ccp-1-2-21`*

### 2.VI.3 — Provable debts (s 218); liquidator's assessment of proofs

**Q2-18** · `2.VI.3` · own question · `ccp-1-2-22`

Which of these claims is NOT provable in the company's liquidation?

A. A debt payable in 6 months under a contract made before the winding up.
B. A contingent liability under a guarantee given before the winding up.
C. A claim for unliquidated damages in tort for negligence.
D. Pre-commencement interest on a debt.

**Answer: C.** Demands in unliquidated damages arising otherwise than by contract, promise or breach of trust are not provable (s 218(3)). A, B and D are provable (s 218(1)–(2)). The liquidator assesses each proof and is not bound by audited accounts, but needs some basis to query a facially genuine debt (*Fustar Chemicals*).
*Cite: INS1 s28–30; IRDA s 218; `ccp-1-2-22`*

### 2.VI.4 — Insolvency set-off (s 219)

**Q21I-2** · `2.VI.4` · 2021 INS Q2 (no official answer) · `ccp-1-2-23`

D Pte Ltd owes David S$100,000 for unpaid services. D Pte Ltd has a claim against David for S$70,000. D Pte Ltd was placed under judicial management. How much can David claim in his proof of debt lodged with the judicial manager?

A. S$30,000
B. S$70,000
C. 0
D. S$100,000

**Answer: A.** Mutual debts are set off and only the net balance is provable (s 219(2)): S$100,000 − S$70,000. Contractual set-off rights are also preserved in JM (s 96(5)).
*Cite: IRDA ss 96(5), 219; INS1 s31–34; `ccp-1-2-23`*

**Q2-19** · `2.VI.4` · own question · `ccp-1-2-23`

At what date is the account for insolvency set-off taken in a compulsory winding up?

A. The date of the winding-up order.
B. The commencement of the winding up, i.e. the date of the application (*Good Property Land v Société Générale*); insolvency set-off is mandatory and displaces contractual set-off (*Park Hotel CQ v Law Ching Hung*).
C. The date the creditor lodges its proof.
D. The date of dissolution.

**Answer: B.** Debts incurred after the creditor had notice of the pending application are excluded.
*Cite: INS1 s31–34; INS-CS1 p20–21; `ccp-1-2-23`*

### 2.VI.5 — Interest on debts (s 222); foreign currency claims

**Q21I-27** · `2.VI.5` · 2021 INS Q27 (no official answer) · `ccp-1-2-24`

In the insolvent winding up of a company, no secured creditor is entitled to any interest in respect of its debt after the commencement of the winding up, if it does not realise its security within ____ after the commencement.

A. 6 months
B. 24 months
C. 3 months
D. 12 months

**Answer: D.** 12 months, or such further period as the liquidator allows (s 223).
*Cite: IRDA s 223; RL-Sec p6; `ccp-1-2-24`*

### 2.VII Bankruptcy: application and administration

Sub-points 2.VII.1–2.VII.7. Real questions: Q21I-8 (2.VII.1), QSQ-I5, Q23-47, Q23-48, Q21I-9 (2.VII.2), Q21I-14, Q21I-24 (2.VII.4), Q21I-19 (2.VII.6). Own questions Q2-20 to Q2-22.

### 2.VII.1 — Court's jurisdiction over the debtor (s 310)

**Q21I-8** · `2.VII.1` `2.VII.2` · 2021 INS Q8 (no official answer) · `ccp-1-2-25` `ccp-1-2-26`

Which of the following statements is/are wrong?

(I) A bankruptcy application may be made against an individual debtor if the debtor has, at any time within 1 year immediately before the application, been ordinarily resident in Singapore.
(II) An individual debtor with no property in Singapore can never be made a bankrupt in Singapore.
(III) Only locally incorporated creditors can make a bankruptcy application in Singapore.

A. (II) and (III).
B. (III) only.
C. (I) and (III).
D. All the statements are wrong.

**Answer: A.** (I) is right (s 310(1)(c)). (II) is wrong: domicile, property and recent residence or business are alternatives. (III) is wrong: any creditor meeting s 311 may apply.
*Cite: IRDA ss 307, 310(1), 311; INS2 s4–6; `ccp-1-2-25`, `ccp-1-2-26`*

### 2.VII.2 — Who may apply; grounds (s 311): S$15,000, liquidated, unable to pay, foreign debts

**QSQ-I5** · `2.VII.2` · SQ p20 Q5 [Part B 2024], official key C · `ccp-1-2-26`

No bankruptcy application may be made to the court in respect of any debt unless, at the time of the application, the amount of the debt or the aggregate amount of the debts owed to the same creditor is not less than ____.

A. S$10,000.
B. S$12,000.
C. S$15,000.
D. S$100,000.

**Answer: C.** s 311(1)(a) IRDA.
*Cite: IRDA s 311(1)(a); SQ p114 (key C); `ccp-1-2-26`*

**Q23-47** · `2.VII.2` · 2023 CCP Paper 1 Q47 (no official answer) · `ccp-1-2-26`

Same stem as QSQ-I5. Options: A. S$10,000. B. S$15,000. C. S$100,000. D. S$12,000.

**Answer: B.** S$15,000 (s 311(1)(a)).
*Cite: IRDA s 311(1)(a); `ccp-1-2-26`*

**Q21I-9** · `2.VII.2` · 2021 INS Q9 (no official answer) · `ccp-1-2-26`

Same stem as QSQ-I5 (without "owed to the same creditor"). Options: A. S$15,000. B. S$12,000. C. S$10,000. D. S$100,000.

**Answer: A.** S$15,000 (s 311(1)(a)).
*Cite: IRDA s 311(1)(a); `ccp-1-2-26`*

**Q23-48** · `2.VII.2` · 2023 CCP Paper 1 Q48 (no official answer) · `ccp-1-2-26`

Who may make a bankruptcy application against an individual?

A. The individual himself or herself.
B. The nominee supervising the implementation of a voluntary arrangement proposed by the individual and approved under Part 14 of the IRDA.
C. One of the individual's creditors.
D. All of the statements are accurate.

**Answer: D.** A creditor's application may be made by one of the individual's creditors or by the nominee supervising an approved Part 14 voluntary arrangement (s 307(1)(a)(i)–(ii)); the debtor may make a debtor's application (s 308).
*Cite: IRDA-2018 ss 307(1)(a), 308; INS2 s5; `ccp-1-2-26`*

### 2.VII.3 — Statutory demand (s 312); expedited application (s 314)

**Q2-20** · `2.VII.3` · own question · `ccp-1-2-27`

A creditor serves a bankruptcy statutory demand on an individual in Singapore for a debt payable immediately. When is the debtor presumed unable to pay, and how long has he to apply to set the demand aside?

A. After 7 days; 3 days to set aside.
B. After 21 days without compliance or an application to set aside; the application to set aside is made within 14 days of service (21 days if served out of jurisdiction).
C. After 3 weeks; no right to set aside.
D. Immediately on service.

**Answer: B.** s 312 and the IRDA PI Rules. A creditor may apply before the 21 days expire if there is a serious possibility the debtor's property or its value will be significantly diminished (s 314).
*Cite: INS2 s7, s9; `ccp-1-2-27`*

### 2.VII.4 — Effect of a bankruptcy order; Official Assignee and private trustee

**Q21I-14** · `2.VII.4` · 2021 INS Q14 (no official answer) · `ccp-1-2-28`

A creditor served a statutory demand on X on 1 September 2021 and filed a bankruptcy application on 27 September 2021. The first hearing on 11 October 2021 was adjourned, and the bankruptcy order was made on 25 October 2021. When did the bankruptcy commence?

A. 27 September 2021.
B. 25 October 2021.
C. 1 September 2021.
D. 11 October 2021.

**Answer: B.** A bankruptcy commences on the date the order is made (s 326). (Contrast a company winding up, which relates back to the application.)
*Cite: IRDA s 326; INS2 s9–10; `ccp-1-2-28`*

**Q21I-24** · `2.VII.4` · 2021 INS Q24 (no official answer) · `ccp-1-2-28`

A Singapore bank wishes to make a bankruptcy application against a debtor and asks whether it can appoint the Official Assignee to be trustee of the bankrupt's estate. The Singapore bank ____

A. can do so if its claim against the debtor exceeds S$15,000.
B. cannot do so unless the debtor consents.
C. cannot do so and must appoint a private trustee, because the bank is an institutional creditor.
D. can do so as there are no restrictions on who it can appoint.

**Answer: C.** A creditor applying for a bankruptcy order must apply for a trustee other than the Official Assignee if it is an institutional creditor (s 36(2)(a)(i)). (The candidate's selection on the screenshot, A, is wrong; the candidate's own note cites s 36(2)(a)(i).)
*Cite: IRDA-2018 s 36(2); INS-SYL p6; `ccp-1-2-28`*

### 2.VII.5 — Duties of the bankrupt

**Q2-21** · `2.VII.5` · own question · `ccp-1-2-29`

Which of these is a duty of a bankrupt under the IRDA?

A. To find a buyer for his house within 30 days.
B. To assist the Official Assignee in identifying and recovering his estate's property (s 399), file a statement of affairs (s 332) and submit accounts when directed (s 333).
C. To pay all his creditors within a year.
D. To resign from all employment.

**Answer: B.** The general duty to assist includes disclosing property and proceedings, delivering documents and attending creditors' meetings.
*Cite: INS2 s11; `ccp-1-2-29`*

### 2.VII.6 — Restrictions on the bankrupt

**Q21I-19** · `2.VII.6` · 2021 INS Q19 (no official answer) · `ccp-1-2-30`

Which statement about a bankrupt person is correct?

A. A bankrupt person can continue being a director of a company so long as he owns all the shares in the company.
B. A bankrupt person is allowed to borrow any sum of money so long as he informs the Official Assignee after doing so.
C. A bankrupt person cannot travel overseas unless he has the permission of the Official Assignee.
D. If a bankrupt person had, before bankruptcy, commenced a legal proceeding, he can continue such proceeding in his discretion.

**Answer: C.** s 401(1)(b). A: acting as a director without the Court's or OA's permission is an offence (s 148(1) CA). B: obtaining credit of S$1,000 or more without disclosing his status is an offence (s 412). D: he needs the OA's sanction to continue proceedings, other than for personal injury or matrimonial proceedings (s 401(1)(a)).
*Cite: IRDA ss 401, 412; CA s 148(1); INS2 s12; `ccp-1-2-30`*

### 2.VII.7 — Distribution of dividends; trustee's remuneration

**Q2-22** · `2.VII.7` · own question · `ccp-1-2-31`

Which is NOT one of the four factors for fixing a bankruptcy trustee's remuneration under r 47 of the IRDA Personal Insolvency Rules?

A. The complexity of the case.
B. Any exceptional responsibility assumed.
C. The effectiveness of the trustee's performance.
D. The number of creditors who voted for the trustee.

**Answer: D.** The fourth factor is the value and nature of the estate's assets. The OA declares and distributes dividends whenever he has sufficient funds (s 385).
*Cite: INS2 s19, s21; `ccp-1-2-31`*

### 2.VIII Bankruptcy: annulment, discharge and alternatives

Sub-points 2.VIII.1–2.VIII.6. Real questions: Q23-49, Q21I-5 (2.VIII.6). Own questions Q2-23 to Q2-27.

### 2.VIII.1 — Annulment (ss 392–393); composition or scheme (s 357)

**Q2-23** · `2.VIII.1` · own question · `ccp-1-2-32`

A bankrupt's family pays off all the proved debts and the expenses of the bankruptcy. What can happen?

A. Nothing; bankruptcy lasts at least 3 years.
B. The bankruptcy can be annulled — by the Court if all debts and expenses have been paid or secured (s 392), or by the Official Assignee's certificate where all proved debts and expenses are paid (s 393).
C. Only discharge after 7 years.
D. The creditors must re-prove.

**Answer: B.** The Court may also annul an order that ought not to have been made; creditors may accept a composition or scheme (s 357).
*Cite: INS2 s22–23; `ccp-1-2-32`*

### 2.VIII.2 — Discharge by the Court (s 394)

**Q2-24** · `2.VIII.2` · own question · `ccp-1-2-33`

On a discharge application, which order may the Court make under s 394(3)?

A. Only an absolute discharge.
B. Refuse discharge, discharge absolutely, or discharge on conditions (e.g. as to future income or after-acquired property).
C. Only refuse discharge.
D. Order the creditors to pay the bankrupt's debts.

**Answer: B.** Where specified circumstances are proved (e.g. no books, rash speculation, undue preferences, assets under 20% of unsecured liabilities), the Court must refuse discharge or impose conditions (s 394(4)–(5)).
*Cite: INS2 s24; `ccp-1-2-33`*

### 2.VIII.3 — Discharge by certificate of the Official Assignee (s 395)

**Q2-25** · `2.VIII.3` · own question · `ccp-1-2-34`

A first-time bankrupt pays his target contribution and no relevant creditor objects. When may the OA issue a certificate of discharge?

A. After 1 year.
B. After 3 years from the administration date.
C. Only after 7 years.
D. Only after 9 years.

**Answer: B.** First-time bankrupts: 3 years with target contribution and no objection, or 5 years; in any case after 7 years. Repeat bankrupts: 5 or 7 years with target contribution, otherwise 9.
*Cite: INS2 s25–26; IRDA s 395(2); `ccp-1-2-34`*

### 2.VIII.4 — Effect of discharge

**Q2-26** · `2.VIII.4` · own question · `ccp-1-2-35`

Which debt is released by the bankrupt's discharge (without any special order)?

A. A fine for a criminal offence.
B. A debt arising from his fraud.
C. An ordinary unsecured trade debt provable in the bankruptcy.
D. Income tax owed to the Government.

**Answer: C.** Discharge releases provable debts (s 397), but not Government debts (unless the Minister agrees), fines, or fraud debts; personal-injury damages and family orders survive unless the Court orders otherwise.
*Cite: INS-SYL p7; IRDA s 397; `ccp-1-2-35`*

### 2.VIII.5 — Individual voluntary arrangement (Part 14)

**Q2-27** · `2.VIII.5` · own question · `ccp-1-2-36`

Which statement about an individual voluntary arrangement is CORRECT?

A. It is available to undischarged bankrupts.
B. The Court may make an interim order protecting the debtor while his proposal is considered, if he intends to propose an arrangement and his nominee is qualified and willing to act (ss 276–279).
C. It needs no creditors' meeting.
D. It is administered by the Official Assignee as a DRS.

**Answer: B.** An IVA is not available to an undischarged bankrupt (s 275); a creditors' meeting considers the proposal (ss 280–285).
*Cite: INS2 s13–15; `ccp-1-2-36`*

### 2.VIII.6 — Debt repayment scheme (Part 15)

**Q21I-5** · `2.VIII.6` · 2021 INS Q5 (no official answer) · `ccp-1-2-37`

An individual debtor wishes to be considered for a debt repayment scheme under section 289 of the IRDA. To be eligible, the total amount of his debt must not exceed ____.

A. S$250,000
B. S$15,000
C. S$200,000
D. S$150,000

**Answer: D.** S$150,000 (s 289(2)(a) and the DRS Regulations).
*Cite: INS2 s16–17; `ccp-1-2-37`*

**Q23-49** · `2.VIII.6` · 2023 CCP Paper 1 Q49 (no official answer) · `ccp-1-2-37`

A Bank has filed a bankruptcy application against Ms Chu, who wishes to be placed under the debt repayment scheme. Which statement(s) is/are correct?

I. Ms Chu is eligible for the debt repayment scheme so long as her debt to A Bank does not exceed S$150,000.
II. If Ms Chu is placed under the debt repayment scheme, she must enter into a debt repayment plan and repay her debts over a fixed period of no more than 3 years.
III. Ms Chu must be found suitable for the debt repayment scheme by the Official Assignee.
IV. To be eligible for the debt repayment scheme, Ms Chu's total debt owed to all her creditors, including her debt to A Bank, must not exceed S$150,000.

A. II and IV.
B. I and III.
C. II, III, and IV.
D. III and IV.

**Answer: D.** The OA reviews the debtor's suitability (s 289(1)) and must report unsuitability if the aggregate of her debts exceeds the prescribed amount (s 289(2)(a)), so the limit is on total debts (IV), not the debt to one creditor (I). II: the repayment plan may run up to 5 years, not 3 (s 290).
*Cite: IRDA-2018 ss 289(1)–(2), 290; INS2 s16–17; `ccp-1-2-37`*

### 2.IX Judicial management

Sub-points 2.IX.1–2.IX.7. Real questions: QSQ-I10, Q23-50 (2.IX.2), QSQ-I9, Q21I-22 (2.IX.3), Q21I-11 (2.IX.5), Q21I-10, Q23-52 (2.IX.6), Q21I-15, Q21I-16, Q23-51, Q21I-30 (2.IX.7). Own questions Q2-28, Q2-29.

### 2.IX.1 — Aims and features; which companies

**Q2-28** · `2.IX.1` · own question · `ccp-1-2-38`

Which statement about judicial management is CORRECT?

A. The directors stay in control (debtor in possession).
B. The directors are replaced by an independent judicial manager with all their powers, and a moratorium gives the company time to rehabilitate; any company liable to be wound up under the IRDA may use it, but not, e.g., banks or insurers.
C. It is available only to Singapore-incorporated companies.
D. It always ends in liquidation.

**Answer: B.** A describes a scheme. C: a foreign company with a substantial connection is liable to be wound up and so may use JM. D: survival or a scheme are statutory purposes.
*Cite: INS3 s2–5; INS-CS1 p36–38; `ccp-1-2-38`*

### 2.IX.2 — Threshold and test: the three purposes in s 89(1)

**QSQ-I10** · `2.IX.2` · SQ p22 Q10 [Part B 2025 S1], official key D · `ccp-1-2-39`

Which of the following is not a purpose of judicial management under the IRDA?

A. The survival of the company as a going concern.
B. The approval of a compromise or an arrangement under section 210 of the Companies Act 1967.
C. A more advantageous realisation of the company's assets than on winding up.
D. The assessment of whether there are grounds to wind up the company under section 124(1) of the IRDA.

**Answer: D.** A, B and C are the three purposes in s 89(1).
*Cite: IRDA s 89(1); SQ p114 (key D); `ccp-1-2-39`*

**Q23-50** · `2.IX.2` · 2023 CCP Paper 1 Q50 (no official answer) · `ccp-1-2-39`

Which of the following is a statutory aim of judicial management under the IRDA?

A. To distribute the company's assets in a fair and pari passu manner.
B. To prevent directors who have breached their duties from remaining in control of the company.
C. To get the company's books in order.
D. To ensure the survival of the company or its undertaking as a going concern.

**Answer: D.** s 89(1)(a). A is the aim of liquidation; B and C are not statutory purposes.
*Cite: IRDA s 89(1); `ccp-1-2-39`*

### 2.IX.3 — Who may apply (s 90); procedure; interim judicial manager

**QSQ-I9** · `2.IX.3` `2.IX.2` · SQ p22 Q9 [Part B 2025 S1], official key C · `ccp-1-2-40` `ccp-1-2-39`

Marina Pte Ltd is struggling to pay its debts. Mr Shenton, a creditor, is considering applying to place Marina under judicial management. Can he make the application?

A. No, as he does not have the requisite locus standi to make the application.
B. Yes, if the judicial management will result in a smoother transition to the eventual liquidation of Marina.
C. Yes, if there is reasonable prospect of selling off Marina's business as a going concern under judicial management.
D. Yes, if the judicial management will better serve the interests of Marina's shareholders as compared to a winding up.

**Answer: C.** Any creditor may apply (s 90), and the order must be likely to achieve a s 89(1) purpose, such as survival of the undertaking as a going concern. A: creditors have standing. B and D are not statutory purposes.
*Cite: IRDA ss 89–90; SQ p114 (key C); `ccp-1-2-40`, `ccp-1-2-39`*

**Q21I-22** · `2.IX.3` · 2021 INS Q22 (no official answer) · `ccp-1-2-40`

Which of the following has no legal standing to apply to place a company under judicial management?

A. The directors of the company acting pursuant to a shareholders' or directors' resolution.
B. A minority shareholder of the company.
C. The company.
D. Any creditor of the company.

**Answer: B.** s 90 lists the company, its directors and any creditor; shareholders as such are not listed.
*Cite: IRDA s 90; `ccp-1-2-40`*

### 2.IX.4 — Opposition by a floating charge holder (s 91(6)); public interest (s 91(10))

**Q2-29** · `2.IX.4` · own question · `ccp-1-2-41`

A bank holding a floating charge over substantially all of a company's property, with power to appoint a receiver and manager, opposes the company's JM application. When must the Court dismiss it?

A. Whenever any secured creditor opposes.
B. If the prejudice to the bank from the order would be disproportionately greater than the prejudice to the unsecured creditors if it were not made (s 91(6)) — unless the public interest requires the order (s 91(10)).
C. Never; the Court always has an unfettered discretion.
D. Only if the bank's debt exceeds S$15,000.

**Answer: B.** Under *Re Bintan Lagoon Resort* the question is whether the public interest requires the order, not merely whether JM would be in the public interest.
*Cite: INS3 s9–13; IRDA s 91(6), (10); `ccp-1-2-41`*

### 2.IX.5 — Judicial management by creditors' resolution (s 94)

**Q21I-11** · `2.IX.5` · 2021 INS Q11 (no official answer) · `ccp-1-2-42`

A client says an application to the court is the only way to commence a judicial management process. Is the client correct and why (or why not)?

A. No, because the IRDA allows all insolvency processes to be commenced out of court.
B. Yes, because a judicial management order can only be granted by the court.
C. No, because it is possible for the company to initiate a judicial management out of court.
D. Yes, because a judicial manager is an officer of the court.

**Answer: C.** Under s 94 the company may appoint an interim judicial manager and its creditors may resolve to place it in JM without a court order. A overstates it; B and D are wrong.
*Cite: IRDA s 94; INS3 s16; `ccp-1-2-42`*

### 2.IX.6 — Moratoria (ss 95, 96); contractual set-off

**Q21I-10** · `2.IX.6` · 2021 INS Q10 (no official answer) · `ccp-1-2-43`

Which of the following is a wrong statement of the effect of an application to place a company under judicial management?

A. No step may be taken to enforce any security over any property of the company.
B. No order may be made, and no resolution may be passed, for the winding up of the company.
C. No legal proceedings may be commenced against the company.
D. No contractual set-off rights may be exercised by any creditor of the company.

**Answer: D.** Contractual set-off is not affected (s 96(5); *Electro Magnetic v DBS*). A, B and C describe the s 95 moratorium (proceedings and enforcement are barred except with leave).
*Cite: IRDA ss 95, 96(5); INS3 s18–20; `ccp-1-2-43`*

**Q23-52** · `2.IX.6` `2.IX.7` · 2023 CCP Paper 1 Q52 (no official answer) · `ccp-1-2-43` `ccp-1-2-44`

By order of Court, John was appointed judicial manager of Happy Pte Ltd ("HPL") on 30 July 2023. Which statement(s) is/are correct?

I. While HPL is in judicial management, every website in which HPL's name appears must indicate that the company is under judicial management.
II. HPL's secured creditors may enforce their security over HPL's property.
III. Upon the application for judicial management being made, an automatic moratorium period of 30 days commences, during which no order may be made for the winding up of the company.
IV. John must lodge the judicial management order with the Official Receiver and publish his appointment in the Gazette by 30 August 2023.

A. II and III only.
B. I only.
C. IV only.
D. I and III only.

**Answer: B.** I is right: every website of the company on which its name appears must state that it is managed by the judicial manager (s 97(1)(b)). II is wrong: security cannot be enforced without leave (ss 95–96). III is wrong: the s 95 moratorium runs from the application until it is decided; the 30-day automatic moratorium belongs to scheme applications (s 64(14)). Statement IV does not appear in any option except C, which excludes the true statement I. (The candidate's selection on the screenshot, D, is wrong.)
*Cite: IRDA-2018 ss 95, 96, 97(1); `ccp-1-2-43`, `ccp-1-2-44`*

See also Q21I-35 under 2.IV.2.

### 2.IX.7 — The judicial manager: powers, proposals, duration, discharge, creditor protection

**Q21I-15** · `2.IX.7` · 2021 INS Q15 (no official answer) · `ccp-1-2-44`

Unless extended by the court, a judicial management order lasts for ____ days after the date of the making of the order.

A. 60
B. 180
C. 365
D. 90

**Answer: B.** 180 days, extendable by the Court or by creditors' approval (s 111). D: 90 days is the deadline for the statement of proposals (s 107).
*Cite: INS3 s21–26; `ccp-1-2-44`*

**Q21I-16** · `2.IX.7` · 2021 INS Q16 (no official answer) · `ccp-1-2-44`

David has just been appointed judicial manager of a company. To be approved at a meeting of creditors convened to consider it, a statement of proposals has to be approved by ____ of the creditors present and voting in person or by proxy.

A. a majority in number and value
B. three-fourths in number and value
C. a majority in number and three-fourths in value
D. all

**Answer: A.** A majority in number and value of the creditors present and voting whose claims the JM has accepted (s 108(3); the same majority approves substantial revisions, s 110(2)(b)). C is the scheme majority.
*Cite: IRDA-2018 ss 107–108, 110(2); `ccp-1-2-44`*

**Q23-51** · `2.IX.7` · 2023 CCP Paper 1 Q51 (no official answer) · `ccp-1-2-44`

James has been appointed judicial manager of Distress Pte Ltd. Its creditors want oversight of James' performance of his functions. Which of the following can they do under the IRDA?

A. Pass a creditors' resolution to compel James to undertake that he will comply with the creditors' directions.
B. Make an application to Court seeking the nomination of a committee of creditors.
C. Establish a committee of creditors that may require James to provide information regarding the discharge of his duties.
D. Appoint an independent assessor.

**Answer: C.** Where the creditors' meeting approves the proposals it may establish a committee, which may require the JM to attend and give it information about the carrying out of his functions (s 109). A, B and D have no basis in the Act.
*Cite: IRDA-2018 s 109; `ccp-1-2-44`*

**Q21I-30** · `2.IX.7` `2.V.1` `2.XIII.1` · 2021 INS Q30 (no official answer) · `ccp-1-2-44` `ccp-1-2-17` `ccp-1-2-64`

A liquidator's powers are different from those of a judicial manager in that:

A. a judicial manager has the power to carry on the business of the company under judicial management; a liquidator may only do so to the extent it is necessary for the beneficial winding up of the company.
B. a liquidator is able to set aside a transaction as an unfair preference or a transaction at an undervalue; a judicial manager has no such powers.
C. a liquidator can appoint solicitors to assist in the performance of his or her functions; a judicial manager cannot do so.
D. a liquidator can commence a legal proceeding on behalf of the company; a judicial manager cannot do so.

**Answer: A.** A JM has power to carry on the company's business (First Schedule); a liquidator may do so only so far as necessary for the beneficial winding up (s 144(1)(a)). B: the JM can also apply to set aside preferences and undervalues (ss 224–227). C and D: both officeholders have these powers.
*Cite: IRDA-2018 s 144(1)(a), First Schedule; INS3 s21; `ccp-1-2-44`, `ccp-1-2-17`, `ccp-1-2-64`*

### 2.X Avoidance of antecedent transactions; officers' liability

Sub-points 2.X.1–2.X.9. Real questions: Q21I-26 (2.X.1, under 2.II.1), Q21I-4 (2.X.2), Q23-55, Q21I-28 (2.X.4), Q21I-7 (2.X.5), Q23-57, Q21I-33 (2.X.6), Q21I-12 (2.X.9). Own questions Q2-30 to Q2-33.

### 2.X.1 — Unfair preference: elements (s 225)

See Q21I-26 under 2.II.1 (no consideration is an undervalue, not a preference).

**Q2-30** · `2.X.1` · own question · `ccp-1-2-45`

Two months before its liquidation, an insolvent company repays a bank loan that its director had personally guaranteed, while other creditors go unpaid. Which is CORRECT?

A. It cannot be a preference because the bank, not the director, was paid.
B. It may be an unfair preference of the director as surety: it puts him in a better position in the liquidation, and if the company was influenced by a desire to prefer him (presumed, as he is connected), the payment can be set aside.
C. It is a transaction at an undervalue.
D. It is valid because the company received value.

**Answer: B.** A surety or guarantor can be the person preferred (s 225); the connected-person presumption applies (s 225(5)). C: repaying a debt gives value.
*Cite: INS4 s5–6, s9–13; IRDA ss 225–226; `ccp-1-2-45`*

### 2.X.2 — Relevant time; connected persons and associates (ss 226, 217)

**Q21I-4** · `2.X.2` · 2021 INS Q4 (no official answer) · `ccp-1-2-46`

A creditor filed a winding up application on 20 October 2020. The company was wound up on 21 November 2020 and X was appointed liquidator. X wishes to set aside, as an unfair preference, a payment the company made to its subsidiary in January 2019. Which is correct?

A. X can do so as the payment was within the period starting 3 years before the commencement of the winding up.
B. X cannot do so as the correct ground for setting aside is that the payment was a transaction at an undervalue.
C. X cannot do so as the payment fell outside the period starting 6 months before the commencement of the winding up.
D. X can do so as the payment was within the period starting 2 years before the commencement of the winding up.

**Answer: D.** A subsidiary is a connected person (an associate of the company, s 217), so the look-back for a preference is 2 years before commencement (the application date, 20 October 2020) (s 226). January 2019 is within it. A: 3 years is the undervalue period. B: a payment of a debt is a preference question. C: 6 months is not the IRDA period.
*Cite: IRDA ss 126, 217, 226; INS4 s7–8; `ccp-1-2-46`*

### 2.X.3 — Desire to prefer: presumption, test, proper commercial consideration

**Q2-31** · `2.X.3` · own question · `ccp-1-2-47`

An insolvent company pays an unconnected supplier in full because the supplier threatened to stop deliveries essential to keep the factory running. Is the company "influenced by a desire to prefer"?

A. Yes, always, because the supplier was paid in full.
B. Not necessarily: the test is whether the decision was influenced by a desire to prefer (it need only be one factor); a transaction actuated by a proper commercial consideration, such as keeping essential supplies, is not a preference, though creditor pressure alone does not negate the desire.
C. Yes, because the desire is presumed for every creditor.
D. No, because pressure always negates the desire.

**Answer: B.** *DBS v Tam Chee Chong*; *Rabobank v Jurong Technologies*. C: the presumption applies only to connected persons (s 225(5); *Progen*). D overstates it.
*Cite: INS4 s9–13; `ccp-1-2-47`*

### 2.X.4 — Transaction at an undervalue (s 224): elements, 3 years, presumption, defence

**Q21I-28** · `2.X.4` · 2021 INS Q28 (no official answer) · `ccp-1-2-48`

Which of the following is a valid defence to a claim that a transaction was at an undervalue?

A. The transaction occurred more than 6 months before the commencement of the winding up.
B. The debtor company entered into the transaction in good faith and for the purpose of carrying on its business and the transaction benefited the company.
C. The debtor company was not associated with the other party to the transaction.
D. The debtor company was not influenced by the desire to prefer the other party to the transaction.

**Answer: B.** s 224(4): good faith, for the purposes of the business, with reasonable grounds for believing the transaction would benefit the company. A: the look-back is 3 years. C: connection only creates a presumption of insolvency. D: desire to prefer belongs to preferences.
*Cite: IRDA s 224(4); INS4 s14–20; `ccp-1-2-48`*

**Q23-55** · `2.X.4` · 2023 CCP Paper 1 Q55 (no official answer) · `ccp-1-2-48`

You act for the judicial managers of M Pte Ltd ("MPL"); the JM commenced in June 2023. In October 2020, at City Bank's request, MPL granted a registered charge over its share of a processing plant to secure bank loans made in early 2019 by City Bank to AA Pte Ltd ("AAPL"). MPL owns a minority of the shares in AAPL, and they share the same sole director, Naomi. AAPL is currently insolvent. The loans were essential for AAPL's semiconductor operations. Which statement is correct?

A. The charge granted to City Bank may be avoided as it was a transaction made at an undervalue. No valuable consideration was received by MPL in granting the charge.
B. The charge granted to City Bank cannot be avoided as AAPL was MPL's subsidiary and both companies share the same sole director.
C. The charge granted to City Bank can be avoided as it was an unfair preference. MPL chose to prefer City Bank on the ground that AAPL owed money to City Bank and that MPL has an interest in AAPL.
D. The charge granted to City Bank cannot be avoided as valuable consideration was received by AAPL and thus in turn MPL.

**Answer: A.** MPL gave security for another company's existing debt and received nothing itself: a transaction for no consideration (s 224(3)), within 3 years before the JM commenced (s 226(1)(a)). C: City Bank was not MPL's creditor, so there is no preference of a creditor of MPL. B: AAPL was not MPL's subsidiary (MPL holds a minority), and being related would not stop avoidance. D: consideration must move to the company itself. The s 224(4) defence would need MPL to show it acted in good faith for its own business with reasonable grounds to believe it would benefit; the facts show a benefit to AAPL only.
*Cite: IRDA ss 224, 226; INS4 s14–20; `ccp-1-2-48`*

### 2.X.5 — Void dispositions after commencement (s 130; s 328)

**Q21I-7** · `2.X.5` · 2021 INS Q7 (no official answer) · `ccp-1-2-49`

Following a winding up application filed on 2 September 2021, a winding up order was made against ABC Pte Ltd and a liquidator appointed on 24 September 2021. ABC Pte Ltd had made a payment to X on 7 September 2021. The liquidator may try to set aside the payment on the ground that:

A. it was an unfair preference under section 225 of the IRDA.
B. it was a disposition under section 130 of the IRDA.
C. it was a transaction at an undervalue under section 224 of the IRDA.
D. it was made without the approval of the board of directors of ABC Pte Ltd.

**Answer: B.** A disposition of property after the commencement of a winding up by the Court (the application date) is void unless the Court orders otherwise (s 130(1)). A and C deal with transactions before commencement.
*Cite: IRDA s 130; INS4 s21–23; `ccp-1-2-49`*

### 2.X.6 — Floating charges for no value (s 229)

**Q23-57** · `2.X.6` · 2023 CCP Paper 1 Q57 (no official answer) · `ccp-1-2-50`

Bank Y granted an unsecured loan to X in October 2020. In February 2021, X granted a floating charge in favour of Bank Y. A winding up application was filed against X in April 2022 and X was wound up by the court in June 2022. The floating charge granted to Bank Y:

A. may not be set aside because it fell outside the applicable claw-back period.
B. may be set aside so long as it fell within the applicable claw-back period.
C. may not be set aside only because there is no evidence of an intention to prefer.
D. may be set aside except to the extent of any new loan granted by Bank Y.

**Answer: A.** For an unconnected chargee the relevant time is 1 year before the commencement of the winding up (the April 2022 application) (s 229(2)); February 2021 is about 14 months earlier. D states the s 229(1) rule, which would apply only if the charge fell within the period. C: s 229 does not turn on desire to prefer.
*Cite: IRDA s 229(1)–(3); INS4 s24–25; `ccp-1-2-50`*

**Q21I-33** · `2.X.6` · 2021 INS Q33 (no official answer) · `ccp-1-2-50`

Bank Y granted an unsecured loan to X in September 2019. In January 2020, X granted a floating charge in favour of Bank Y. A winding up application was filed against X in March 2021 and X was wound up in May 2021. The floating charge granted to Bank Y [the screen says "Bank A"]:

A. may not be set aside only because there is no evidence of an intention to prefer.
B. may be set aside so long as it fell within the applicable claw-back period.
C. may not be set aside because it fell outside the applicable claw-back period.
D. may be set aside except to the extent of any new loan granted by Bank A.

**Answer: C.** Same rule as Q23-57: January 2020 is more than 1 year before the March 2021 application, and the bank is unconnected (s 229(2)). (The candidate's selection, D, overlooks the claw-back period.)
*Cite: IRDA s 229(1)–(3); `ccp-1-2-50`*

### 2.X.7 — Orders the Court may make (s 227)

**Q2-32** · `2.X.7` · own question · `ccp-1-2-51`

The Court finds a transaction at an undervalue. What orders may it make?

A. Only a declaration.
B. Any order it thinks fit to restore the position to what it would have been, e.g. re-vesting property, releasing security, ordering payment, reviving guarantees, while protecting third parties who acquired interests in good faith and for value (ss 224(2), 227).
C. Only damages against the directors.
D. Only an order dissolving the company.

**Answer: B.** s 227 gives examples of restorative orders.
*Cite: INS-SYL p9; IRDA s 227; `ccp-1-2-51`*

### 2.X.8 — Fraudulent trading (s 238)

**Q2-33** · `2.X.8` · own question · `ccp-1-2-52`

In a winding up, the liquidator alleges the directors knowingly carried on the business to defraud creditors. What must be shown for personal liability under s 238?

A. Mere negligence.
B. That the business was carried on with intent to defraud creditors or for a fraudulent purpose, involving actual dishonesty and real moral blame (*Tang Yoke Kheng v Lek Benedict*), and that the person was knowingly a party.
C. Only that the company became insolvent.
D. A prior criminal conviction.

**Answer: B.** Negligence-type conduct is addressed instead by wrongful trading (s 239).
*Cite: INS4 s26–27; IRDA s 238; `ccp-1-2-52`*

### 2.X.9 — Wrongful trading (s 239)

**Q21I-12** · `2.X.9` · 2021 INS Q12 (no official answer) · `ccp-1-2-53`

Y Pte Ltd cannot pay its debts as they fall due and seems unlikely to satisfy any future debt. Yaz, its sole director, continued the business and bought materials on credit, unsure whether Y Pte Ltd could pay for them. Which is correct?

A. Yaz may be liable for wrongful trading under section 239 of the IRDA because Y Pte Ltd was incurring debts without reasonable prospect of meeting them in full.
B. For Yaz to be found liable for wrongful trading, it is necessary to prove that she has been dishonest or fraudulent.
C. Yaz may be liable for wrongful trading under section 239 of the IRDA so long as she is a director of Y Pte Ltd at the time it is wound up.
D. Yaz will not be liable for wrongful trading under section 239 of the IRDA unless she is first convicted of a criminal offence.

**Answer: A.** An insolvent company that incurs debts without reasonable prospect of meeting them trades wrongfully, and a person knowingly party may be made personally liable (s 239). B: dishonesty is for fraudulent trading. C: liability attaches to being party to the trading, not to holding office at the winding up. D: no conviction is needed.
*Cite: IRDA s 239; INS4 s28–29; `ccp-1-2-53`*

### 2.XI Schemes of arrangement

Sub-points 2.XI.1–2.XI.8. Real questions: Q23-58, Q21I-23 (2.XI.2), Q23-59, QSQ-I8 (2.XI.5), Q21I-6 (2.XI.6), Q23-60 (2.XI.7, 2.XI.3), Q21I-20 (2.XI.8). Own questions Q2-34, Q2-35.

### 2.XI.1 — What a scheme is; which companies; key steps

**Q2-34** · `2.XI.1` · own question · `ccp-1-2-54`

Which is the correct order of the key steps in a scheme of arrangement?

A. Court sanction; creditors' meeting; leave to convene; lodgement.
B. Application for leave to convene the creditors' meeting(s) (s 210(1) CA); meetings and vote (s 210(3AB)); Court sanction (s 210(4)); lodgement of the order with the Registrar (s 210(5)).
C. Creditors' vote; lodgement; leave; sanction.
D. Lodgement; vote; sanction; leave.

**Answer: B.** Management stays in control throughout (debtor in possession), and a moratorium may be sought at any time before sanction (s 64).
*Cite: INS5 s2–3, s6–7; `ccp-1-2-54`*

### 2.XI.2 — Moratoria: automatic interim (s 64), court-ordered, related companies (s 65)

**Q23-58** · `2.XI.2` · 2023 CCP Paper 1 Q58 (no official answer) · `ccp-1-2-55`

Which of the following is true concerning an automatic interim moratorium under s 64 of the IRDA?

I. Such an automatic interim moratorium can take effect even if a resolution has been passed for the winding up of the company.
II. Creditors can continue with enforcement and/or repossession actions against the assets of the company while an automatic interim moratorium is in place, so long as such actions were commenced before it took effect.
III. An automatic moratorium arises upon the filing of an application for a stay under s 64 IRDA.
IV. The automatic interim moratorium will apply so long as the applicant company had not made an application under s 64 IRDA within the previous 12 months.

A. I and II only.
B. III and IV only.
C. II, III and IV only.
D. I, II and III only.
E. III only.

**Answer: B.** III: the moratorium arises on filing (s 64(14)). IV: it does not arise if the company made an earlier s 64(1) application attracting it within the previous 12 months (s 64(9)). II is false: enforcement and repossession cannot be continued without leave (s 64(8)(e)). Every option containing I also contains the false statement II, so B is the answer whatever the position on I.
*Cite: IRDA-2018 s 64(8)–(9), (14); `ccp-1-2-55`*

**Q21I-23** · `2.XI.2` · 2021 INS Q23 (no official answer) · `ccp-1-2-55`

Which of the following is not a requirement for an application for an automatic interim moratorium under section 64 of the IRDA?

A. Where the company has not proposed a compromise or arrangement, a brief description of the intended compromise or arrangement.
B. A list of all the employees of the company.
C. A list of every secured creditor of the company.
D. Evidence of support from the company's creditors for the intended or proposed compromise or arrangement.

**Answer: B.** s 64(4) requires evidence of creditor support, a brief description of an unproposed scheme, a list of every secured creditor and a list of unrelated unsecured creditors (or the 20 largest); not a list of employees.
*Cite: IRDA-2018 s 64(4); `ccp-1-2-55`*

See also Q21I-26 under 2.II.1 (30 days, not 90).

### 2.XI.3 — Application for leave to convene meetings (s 210(1) CA)

See Q23-60 under 2.XI.7 (option D: merits and fairness are not for the leave stage).

### 2.XI.4 — Notice and explanatory statement (s 211 CA)

**Q2-35** · `2.XI.4` · own question · `ccp-1-2-57`

What must the explanatory statement sent with the notice of a scheme meeting contain?

A. Only the date and place of the meeting.
B. An explanation of the effect of the scheme, any material interests of the directors (and how the scheme affects them differently), and full and fair disclosure of what creditors reasonably need to decide how to vote (s 211(1) CA).
C. The court's views on the scheme's fairness.
D. A valuation of each creditor's claim by the Official Receiver.

**Answer: B.** Proofs of debt are then adjudicated for voting (s 68 IRDA).
*Cite: INS5 s11; INS-CS1 p54, p57; `ccp-1-2-57`*

### 2.XI.5 — Classification of creditors

**QSQ-I8** · `2.XI.5` · SQ p21 Q8 [Part B 2025 S1], official key D · `ccp-1-2-58`

Which best describes the main purpose of classifying creditors for voting on a scheme of arrangement?

A. To ensure the ease of counting votes when creditors are organised in classes than counting the votes of individual creditors.
B. To ensure that groups of creditors are better able to assert their rights against a rival group of creditors.
C. To ensure that the company has an easier time explaining the different aspects of the proposed scheme to different groups of creditors.
D. To ensure that creditors with similar rights are in the same group such that they can consult together with a view to their common interests.

**Answer: D.** The dissimilarity principle (*TT International*): creditors whose rights are so dissimilar that they cannot sensibly consult together are put in separate classes.
*Cite: INS5 s12–14; SQ p114 (key D); `ccp-1-2-58`*

**Q23-59** · `2.XI.5` · 2023 CCP Paper 1 Q59 (no official answer) · `ccp-1-2-58`

Monarch Pte Ltd has convened creditors' meetings for a s 210 scheme. The classes are — Class 1: Mercury Pte Ltd, a wholly-owned subsidiary owed S$600,000 on an intercompany loan, and Mr May, owed S$500,000 on an unsecured loan. Class 2: Bulsara Bank, secured on machinery and expected to recover 100%, and Taylor Pte Ltd, an unsecured supplier expected to recover 40%. Class 3: Mr Deacon, an employee owed wages who will recover 100% as a preferential creditor. Which classes may be challenged as improper?

A. Only class 2.
B. Only classes 1 and 2.
C. None.
D. Only classes 2 and 3.

**Answer: B.** Class 2 puts a fully secured creditor with an unsecured one recovering 40%: their rights are too dissimilar to consult together. Class 1 mixes a related (wholly-owned subsidiary) creditor with an unrelated one, which raises class or vote-discounting issues and may be challenged. Class 3, a preferential creditor paid in full on its own, is unobjectionable.
*Cite: INS5 s12–14; `ccp-1-2-58`*

### 2.XI.6 — Voting: statutory majority (s 210(3AB) CA)

**Q21I-6** · `2.XI.6` · 2021 INS Q6 (no official answer) · `ccp-1-2-59`

Which correctly describes what must be satisfied for the approval of a scheme of arrangement?

A. Three-fourths in value of each class of creditors votes in favour of the scheme.
B. All creditors vote in favour of the scheme.
C. A majority in number representing three-fourths in value of each class of creditors votes in favour of the scheme.
D. A majority in number representing two-thirds in value of each class of creditors votes in favour of the scheme.

**Answer: C.** s 210(3AB) CA: a majority in number representing three-fourths in value of the creditors (or each class) present and voting.
*Cite: INS5 s6, s15; `ccp-1-2-59`*

### 2.XI.7 — Cram-down (s 70) and pre-pack schemes (s 71)

**Q23-60** · `2.XI.7` `2.XI.3` · 2023 CCP Paper 1 Q60 (no official answer) · `ccp-1-2-60` `ccp-1-2-56`

Which statement concerning a scheme of arrangement is correct?

A. A court can only exercise its power to cram down on a dissenting class of creditors if there is a majority in the number of creditors or creditors representing three-fourths of the value of creditors that approve the scheme.
B. Contingent creditors cannot take part in the scheme as their claims are for an unliquidated sum.
C. The court has the power to approve a scheme of arrangement without convening a creditors' meeting provided that certain preconditions are fulfilled.
D. In determining whether to grant leave to convene creditors' meetings, the court must consider the fairness and merits of the scheme.

**Answer: C.** The pre-pack (s 71): approval without a meeting if the conditions would have been met had one been summoned. A: cram-down needs a majority in number AND three-quarters in value of the creditors as a whole, plus other conditions (s 70). B: contingent creditors can be scheme creditors (contingent debts are provable, s 218). D: the leave stage is not the forum for merits and fairness (*TT International*).
*Cite: IRDA ss 70–71; INS5 s8–10, s16–17; `ccp-1-2-60`, `ccp-1-2-56`*

### 2.XI.8 — Court sanction; effect on creditors and third parties

**Q21I-20** · `2.XI.8` · 2021 INS Q20 (no official answer) · `ccp-1-2-61`

A scheme of arrangement duly approved by the requisite majority of creditors becomes effective once it has been sanctioned by the court and ____

A. lodged with the Registrar of Companies.
B. no further steps are required.
C. approved by the shareholders of the company.
D. approved by the directors of the company.

**Answer: A.** The order takes effect when a copy is lodged with the Registrar (or from an earlier date the Court specifies) (s 210(5) CA). (The candidate's selection, B, is wrong; the candidate's own note says "Needs to be lodged".)
*Cite: INS5 s18–22; `ccp-1-2-61`*

### 2.XII Rescue financing and ipso facto clauses

Sub-points 2.XII.1–2.XII.2. No real question kept (2021 INS Q34 is left out); own questions Q2-36, Q2-37.

### 2.XII.1 — Rescue financing and super priority (ss 67, 101)

**Q2-36** · `2.XII.1` · own question · `ccp-1-2-62`

A company under a s 64 moratorium can only get new money if the lender ranks ahead of an existing secured lender over the same asset. When may the Court grant that priority under s 67(1)(d)?

A. Whenever the company asks.
B. Only if the company would not otherwise have obtained the financing and the existing security holder is adequately protected (e.g. cash payments, replacement security, or the "indubitable equivalent").
C. Never; existing security can never be primed.
D. Only if the existing secured lender consents in writing.

**Answer: B.** s 67(1)(d), (6); in JM the judicial manager applies under s 101. Lesser orders: treatment as winding-up costs (a), super priority over preferential and unsecured debts (b), security on unencumbered property or subordinate security (c).
*Cite: IRDA ss 67, 101; `ccp-1-2-62`*

### 2.XII.2 — Ipso facto clauses (s 440)

**Q2-37** · `2.XII.2` · own question · `ccp-1-2-63`

A supplier's contract lets it terminate if the customer applies for a scheme moratorium. The customer applies under s 64 and keeps paying for supplies. Can the supplier terminate?

A. Yes; the clause is valid.
B. No; s 440 bars termination by reason only that restructuring proceedings have commenced, though the supplier may insist on cash for new supplies and need not extend further credit.
C. Yes, because s 440 applies only to winding up.
D. Yes, if it gives 30 days' notice.

**Answer: B.** s 440(1)–(3) covers scheme, moratorium and JM proceedings (not winding up, so C is wrong); the Court may disapply it for significant financial hardship (s 440(4)), and certain contracts and companies are excluded (s 440(5)).
*Cite: IRDA s 440; INS-CS1 p62; `ccp-1-2-63`*

### 2.XIII Choosing a procedure

Sub-point 2.XIII.1. Real question: Q21I-30 (under 2.IX.7). Own question Q2-38.

### 2.XIII.1 — Winding up v scheme of arrangement v judicial management

See Q21I-30 under 2.IX.7 (liquidator's v JM's powers).

**Q2-38** · `2.XIII.1` · own question · `ccp-1-2-64`

The founders of a distressed but viable company want to stay in control while restructuring its debts with creditor support. Which procedure fits best?

A. Compulsory winding up.
B. A scheme of arrangement: management stays in control (debtor in possession), with a s 64 moratorium and a binding compromise once approved by each class and sanctioned.
C. Judicial management, which keeps the directors in control.
D. A creditors' voluntary winding up.

**Answer: B.** In JM the directors are replaced by the judicial manager (C wrong); winding up is terminal (A, D).
*Cite: INS-LP p1; INS3 s3–5; INS5 s4–6; `ccp-1-2-64`*

### 2.XIV Cross-border insolvency

Sub-points 2.XIV.1–2.XIV.4. Real questions: Q21I-13, Q21I-29 (2.XIV.1), QSQ-I6 (2.XIV.2), Q21I-31 (2.XIV.4). Own question Q2-39.

### 2.XIV.1 — UNCITRAL Model Law: recognition, COMI, main and non-main proceedings, relief

**Q21I-13** · `2.XIV.1` · 2021 INS Q13 (no official answer) · `ccp-1-2-65`

Xandor Ltd, incorporated in Country X, commenced a debt reorganisation under Country X's laws. Country X has not adopted the UNCITRAL Model Law. The administrators appointed there ask whether they can seek recognition and a stay of creditor action from the Singapore High Court. Which is correct?

A. The administrators will not be recognised under Singapore law because Country X has not adopted the Model Law.
B. The Singapore High Court can grant recognition and assistance under the Model Law only if Xandor Ltd is also wound up in Singapore.
C. The administrators may apply for an order of recognition and assistance under the Model Law and the Singapore High Court may grant such order if the requirements under the Model Law are satisfied.
D. The Singapore High Court may grant assistance under the Model Law if it will not be contrary to the public policy of Country X.

**Answer: C.** Singapore adopted the Model Law (IRDA Third Schedule) without any reciprocity requirement. B: no Singapore winding up is needed. D: the public-policy question is Singapore's, not Country X's.
*Cite: INS6 s2–11; `ccp-1-2-65`*

**Q21I-29** · `2.XIV.1` · 2021 INS Q29 (no official answer) · `ccp-1-2-65`

Under the UNCITRAL Model Law on Cross-border Insolvency, a debtor's centre of main interests:

A. is defined to be the debtor's registered office.
B. is the place where most of the debtor's creditors are located.
C. is presumed to be the debtor's registered office unless there is evidence to the contrary.
D. is the debtor's registered office only if the debtor has publicised the address of such office.

**Answer: C.** Art 16(3); *Re Zetta Jet*.
*Cite: INS6 s2–11; `ccp-1-2-65`*

### 2.XIV.2 — Winding up foreign companies: substantial connection (s 246)

**QSQ-I6** · `2.XIV.2` · SQ p20 Q6 [Part B 2025 S1], official key A · `ccp-1-2-66`

Which statement is CORRECT with regard to the winding up of foreign companies?

A. A foreign company must have a substantial connection with Singapore before it can be wound up in Singapore.
B. Moratoriums are not available to foreign companies that are wound up in Singapore.
C. A foreign company can only be wound up in Singapore if it has property in Singapore.
D. Foreign companies cannot be wound up in Singapore.

**Answer: A.** s 246(1)(d) IRDA, with the s 246(3) factors (COMI, business or place of business here, registered foreign company, substantial assets, Singapore law or jurisdiction chosen). C: property alone is neither necessary nor enough. D is wrong.
*Cite: IRDA s 246(1)(d), (3); SQ p114 (key A); `ccp-1-2-66`*

### 2.XIV.3 — Liquidating a foreign company's Singapore assets; ring-fencing

**Q2-39** · `2.XIV.3` · own question · `ccp-1-2-67`

A foreign company in liquidation in its home country is also wound up in Singapore. Must the Singapore liquidator pay Singapore creditors first before sending assets to the home liquidation?

A. Yes, always.
B. Generally no — there is no general ring-fencing — except for certain "relevant companies", whose Singapore liquidator must first pay debts incurred in Singapore (s 250(3)(c)).
C. No; Singapore creditors are excluded altogether.
D. Only if the home country has adopted the Model Law.

**Answer: B.**
*Cite: INS6 s14; `ccp-1-2-67`*

### 2.XIV.4 — Foreign companies using Singapore schemes and judicial management

**Q21I-31** · `2.XIV.4` · 2021 INS Q31 (no official answer) · `ccp-1-2-68`

A foreign company can apply to the Singapore High Court to place itself under judicial management:

A. so long as there is no objection from its creditors.
B. only if Singapore is its centre of main interests.
C. only if its creditors are located in Singapore.
D. if it has chosen Singapore law to govern its loan agreements.

**Answer: D.** A foreign company may use JM if it is liable to be wound up in Singapore, i.e. has a substantial connection (s 88 IRDA "company"; s 246), and choosing Singapore law to govern a loan is a substantial-connection factor (s 246(3)(e)). B: COMI is one factor, not a requirement. A and C have no basis.
*Cite: IRDA ss 88, 246(3); INS6 s15–18; `ccp-1-2-68`*

## 3 · Admiralty

### 3.0 Facts used by the Admiralty questions

Four fact patterns recur below. Read them once here.

**Facts A — SQ Admiralty Qs 1–5 (MV SIRI AH).** MV EPL was sold by BLUES Ltd to GUNNERS Ltd on 1 June 2024 and renamed MV SIRI AH. On 21 August 2024 it was arrested in Singapore by its previous Master and crew, employed while BLUES Ltd owned the ship, for unpaid salary. FOOL-HUM Ltd, lawful holder of original bills of lading issued by GUNNERS Ltd, says the cargo was mis-delivered to another party on 1 July 2024.

**Facts B — SQ Admiralty Qs 6–10 (MT QUANZHEN).** The time charterer, YOUNG GOH, arrested MT QUANZHEN over a dispute under its time charter with the demise charterer, ZAO ZIJING. Unknown to YOUNG GOH, shortly before the in rem action was commenced ZAO ZIJING had terminated its demise charter with the registered owner, GO JING, for GO JING's alleged repudiatory breach. After the arrest, HOODOO Yard applied to intervene, claiming unpaid repair dues for repairs it understood were carried out at GO JING's request, and also claiming a possessory lien.

**Facts C — ADM2 sample questions (MT MANU).** After Glazer Shipping became insolvent, Bruno Bunkers began an in rem action and arrested MT MANU, owned by Ruben Tankers. The claim is on a bunker supply contract between Bruno Bunkers and Glazer Shipping, which Bruno Bunkers says Glazer entered into on behalf of Ruben Tankers. Omar Bank, MT MANU's mortgagee, applied to intervene.

**Facts D — ADM1 mock exam questions (MT KESPAR collision).** On 15 August 2023 the tanker MT KESPAR and the bulk carrier MV BERNT LEANO collided in the Singapore Straits, equally to blame; both were seriously damaged. MT KESPAR is owned by King Powder Inc (a one-ship company), bareboat chartered to Brendon Rodder SA, and part of a fleet managed by Foxes Shipmanagement Inc. MV BERNT LEANO, owned by Le Gooners Inc, carried soya bean meal ("Cargo"), damaged in the collision (claim US$5m). MT VARDEE, also managed by Foxes but owned by another one-ship company, will call at Singapore next week; so will MT MADDISSON, another tanker bareboat chartered by Brendon Rodder. Fillberth Side P&I Club, which is in financial difficulties and covers MT KESPAR, offers a Club letter of undertaking answering to a final judgment of the English courts.

### 3.I Admiralty jurisdiction (s 3 HCAJA)

Sub-points 3.I.1–3.I.2. Real questions: QSQ-A3, QSQ-A6, QSQ-A9, QADM-1, QADM-3, QADM1-1 (3.I.2). Own question Q3-1.

### 3.I.1 — Why use admiralty jurisdiction: action in rem, arrest for security

**Q3-1** · `3.I.1` · own question · `ccp-1-3-1`

Why would a claimant with a maritime claim against a foreign shipowner with no assets in Singapore use the admiralty jurisdiction?

A. To obtain judgment without proving its claim.
B. To bring an action in rem and arrest the ship, obtaining security for the claim before judgment; the ship stays detained until security is given, the claim settled or the ship sold.
C. Because in personam actions are not allowed in admiralty.
D. To avoid any need to satisfy s 3 or s 4 HCAJA.

**Answer: B.** C: the jurisdiction may always be invoked in personam (s 4(1)). D: the in rem route depends on a s 3(1) head and s 4(2), (3) or (4).
*Cite: ADM2 s2–3; HCAJA ss 3–4; `ccp-1-3-1`*

### 3.I.2 — Heads of claim in s 3(1)(a)–(r): finding the right head

**QSQ-A3** · `3.I.2` · SQ p44 Q3, official key D · `ccp-1-3-2`

Facts A. Which in rem claim may FOOL-HUM Ltd have against MV SIRI AH?

A. A claim for damage done by a ship under Section 3(1)(d) of the HCAJA.
B. Any claim for damage received by a ship under Section 3(1)(e) of the HCAJA.
C. A claim in respect of goods or materials supplied to a ship under Section 3(1)(l) of the HCAJA.
D. A claim for loss of or damage to goods carried in a ship under Section 3(1)(g) of the HCAJA.

**Answer: D.** Mis-delivery of cargo is a claim for loss of goods carried in a ship (s 3(1)(g)). A and B concern damage done or received by the ship; C concerns supplies to the ship.
*Cite: HCAJA s 3(1); SQ p116 (key D); `ccp-1-3-2`*

**QSQ-A6** · `3.I.2` · SQ p45 Q6, official key C · `ccp-1-3-2`

Facts B. Which s 3 HCAJA provision would YOUNG GOH have relied on to arrest the Vessel?

A. A claim in respect of goods or materials supplied to a ship for her operation or maintenance under Section 3(1)(l).
B. A claim for loss of or damage to goods carried in a ship under Section 3(1)(g).
C. A claim arising out of any agreement relating to the carriage of goods in a ship or the use or hire of a ship under Section 3(1)(h).
D. Any question arising between the co-owners of a ship as to possession, employment or earnings of that ship under Section 3(1)(b).

**Answer: C.** A time charter is an agreement for the use or hire of a ship (s 3(1)(h)).
*Cite: HCAJA s 3(1)(h); SQ p116 (key C); `ccp-1-3-2`*

**QSQ-A9** · `3.I.2` · SQ p47 Q9, official key B · `ccp-1-3-2`

Facts B. Which s 3 HCAJA provision could HOODOO Yard rely on to advance an in rem claim against the Vessel?

A. A claim arising out of the loss of or damage to goods carried in a ship, including circumstances connected with the handling or custody of such goods, under Section 3(1)(g).
B. A claim in respect of services rendered to a ship, including work done upon her, or charges arising therefrom under Section 3(1)(m).
C. A claim for damage caused by a ship, including damage occurring in the course of her operation or use, under Section 3(1)(d).
D. A claim in respect of goods or materials supplied to a ship for her operation, maintenance or upkeep, including items supplied in connection with works carried out on the vessel, under Section 3(1)(l).

**Answer: B.** Unpaid repair dues fall under s 3(1)(m) (construction, repair or equipment of a ship). D covers supplies such as bunkers, not repair work.
*Cite: HCAJA s 3(1)(m); SQ p116 (key B); `ccp-1-3-2`*

**QADM-1** · `3.I.2` · ADM2 s16 sample Q1 (no answer given) · `ccp-1-3-2`

Facts C. Which s 3 HCAJA provision would Bruno Bunkers have relied on to arrest MT MANU?

a) A claim for loss of or damage to goods carried in a ship under s 3(1)(g).
b) A claim in respect of a mortgage of or charge on a ship or any share therein under s 3(1)(c).
c) A claim for damage done by a ship under s 3(1)(d).
d) A claim in respect of goods or materials supplied to a ship for her operation or maintenance under s 3(1)(l).

**Answer: d.** Bunkers are goods or materials supplied to a ship for her operation (s 3(1)(l)).
*Cite: HCAJA s 3(1)(l); ADM2 s16; `ccp-1-3-2`*

**QADM-3** · `3.I.2` · ADM2 s18 sample Q3 (no answer given) · `ccp-1-3-2` `ccp-1-3-7`

Facts C. Which s 3 HCAJA provision could Omar Bank rely on to advance an in rem claim against MT MANU? (Options a–d as in QADM-1.)

**Answer: b.** A mortgagee's claim falls under s 3(1)(c).
*Cite: HCAJA s 3(1)(c); ADM2 s18; `ccp-1-3-2`, `ccp-1-3-7`*

**QADM1-1** · `3.I.2` `3.III.3` · ADM1 mock exam Q1 (no answer given) · `ccp-1-3-2` `ccp-1-3-9`

Facts D. Which statement about Cargo's claim against MV BERNT LEANO is false?

A) Cargo's claim satisfies Section 3(1)(g) of the HCAJA.
B) Cargo's claim does not arise in connection with a ship, BERNT LEANO, and therefore does not satisfy Section 4(4)(a) of the HCAJA.
C) Cargo's claim satisfies Section 4(4)(b) as the person who would be liable on the claim in an action in personam is Le Gooners, which is the owner of MV BERNT LEANO at the time the cause of action arose.
D) Cargo's claim satisfies Section 4(4)(c) as the person who would be liable in personam is Le Gooners, which is the owner of the ship at the time when the action is brought.

**Answer: B.** A claim for damage to cargo carried in BERNT LEANO plainly arises in connection with that ship. A, C and D correctly apply s 3(1)(g) and s 4(4)(a)–(c) to the carrying ship's owner.
*Cite: HCAJA ss 3(1)(g), 4(4); ADM1 mock Q1; `ccp-1-3-2`, `ccp-1-3-9`*

See also QSQ-A1 under 3.III.2 (crew wages, s 3(1)(n)).

### 3.II Liens and priorities

Sub-points 3.II.1–3.II.4. Real questions: QSQ-A2, QADM1-2 (3.II.2), QADM-8 (3.II.4). Own questions Q3-2, Q3-3.

### 3.II.1 — Statutory liens: how created, effect, time bar, change of ownership

**Q3-2** · `3.II.1` · own question · `ccp-1-3-3`

A bunker supplier has an unpaid claim against a ship's owner. When does its statutory lien arise, and what is its effect?

A. When the bunkers are delivered; it survives any later sale.
B. When it issues the originating claim in rem (the claim satisfying ss 3 and 4); from then it is protected against a later change of ownership and the time bar stops running, but a valid sale before the action is brought extinguishes the right in rem against that ship (*The Monica S*).
C. Only when the ship is arrested.
D. Never; bunker claims carry a maritime lien.

**Answer: B.** D: bunker supply claims carry no maritime lien.
*Cite: ADM1 s4; Cel-ADM; `ccp-1-3-3`*

### 3.II.2 — Maritime liens: which claims, how created, survive a sale

**QSQ-A2** · `3.II.2` `3.III.2` · SQ p44 Q2, official key D · `ccp-1-3-4` `ccp-1-3-8`

Facts A. Which statement about the previous Master's and crew's claim against MV SIRI AH is correct?

A. The previous Master and crew are not entitled to arrest MV SIRI AH because their claim does not fall within Section 3(1) of the HCAJA.
B. The previous Master and crew are not entitled to arrest MV SIRI AH because the party liable in personam is BLUES Ltd, which is not the relevant person at the time when the action is brought.
C. The previous Master and crew are entitled to arrest MV SIRI AH because BLUES Ltd is the party liable in personam, and it remains the beneficial owner of MV SIRI AH at the time the action is brought.
D. The claim of the previous Master and crew has a maritime lien, and they are entitled to arrest irrespective of whether BLUES Ltd remained the beneficial owner at the time when the action is brought.

**Answer: D.** Crew wages carry a maritime lien, which attaches to the ship and survives the sale, so they proceed under s 4(3) whoever owns the ship. A: wages are s 3(1)(n). B and C wrongly apply the s 4(4) ownership tests; C is also wrong on the facts (BLUES sold the ship).
*Cite: ADM1 s4; ADM2 s10; HCAJA s 4(3); SQ p116 (key D); `ccp-1-3-4`, `ccp-1-3-8`*

**QADM1-2** · `3.II.2` `3.III.2` `3.III.4` · ADM1 mock exam Q2 (no answer given) · `ccp-1-3-4` `ccp-1-3-8` `ccp-1-3-10`

Facts D. Which statement relating to BERNT LEANO's claim against KESPAR is true?

A) BERNT LEANO has a valid in rem claim, with a maritime lien, against KESPAR.
B) BERNT LEANO also has a valid in rem claim against MADDISSON because MADDISSON is bareboat chartered by Brendon Rodder.
C) BERNT LEANO does not have a valid in rem claim against KESPAR because it is unable to satisfy Section 3(1)(d) of the HCAJA.
D) BERNT LEANO does not have a valid in rem claim against KESPAR because it is not able to satisfy Section 4(4) of the HCAJA.

**Answer: A.** Collision damage is damage done by a ship (s 3(1)(d)) and carries a maritime lien, so the claim lies against KESPAR under s 4(3) (C and D wrong). B: a ship the relevant person only charters by demise is not a sister ship under s 4(4)(d).
*Cite: HCAJA ss 3(1)(d), 4(3), 4(4)(d); ADM1 s4–6; `ccp-1-3-4`, `ccp-1-3-8`, `ccp-1-3-10`*

### 3.II.3 — Possessory (repairer's) lien

**Q3-3** · `3.II.3` · own question · `ccp-1-3-5`

A shipyard repaired a vessel and has not been paid. While the vessel is still in its dock, what right does it have, and what does that right depend on?

A. A maritime lien, which survives any sale.
B. A possessory lien: it may keep the ship until paid, but only while it keeps possession; it may also bring an in rem claim under s 3(1)(m) read with s 4(4).
C. No right except an in personam claim.
D. A mortgage registered with the MPA.

**Answer: B.** Repairers' claims carry no maritime lien (A wrong); the possessory lien is lost with possession.
*Cite: ADM1 s4; ADM2 s10; `ccp-1-3-5`*

### 3.II.4 — Priorities of competing claims to the ship or its proceeds

**QADM-8** · `3.II.4` · ADM2 s23 sample Q8 (no answer given) · `ccp-1-3-6`

Facts C. MT MANU's value is insufficient to cover both Bruno Bunkers' and Omar Bank's claims. Which statement is true?

a) Both Bruno Bunkers and Omar Bank will share the sale proceeds proportionately to the size of their respective claims.
b) Bruno Bunkers' claim will be satisfied in full in advance of Omar Bank's because it commenced the action and arrested the vessel.
c) Omar Bank's claim will be satisfied ahead of Bruno Bunkers' claim because it has a maritime lien which ranks ahead of even the claim of the arresting party.
d) Omar Bank's claim will be satisfied ahead of Bruno Bunkers' claim because its mortgage claim ranks ahead of even the claim of the arresting party.

**Answer: d.** A mortgage ranks ahead of statutory liens such as a bunker claim, and arresting first gives no priority for the claim itself (only the arresting party's costs of arrest and sale rank early). a and b are wrong; c: a mortgage is not a maritime lien.
*Cite: ADM2 s10, s23; ADM-Guide paras 74–76; `ccp-1-3-6`*

### 3.III Invoking the jurisdiction in rem (s 4 HCAJA)

Sub-points 3.III.1–3.III.6. Real questions: QADM-4 (3.III.1), QSQ-A1 (3.III.2), QSQ-A7, QSQ-A10, QADM-2 (3.III.3), QSQ-A5, QADM1-5, QADM1-7, QADM1-M (3.III.4), QSQ-A8 (3.III.6). Own question Q3-4.

### 3.III.1 — s 4(2): claims in s 3(1)(a), (b), (c), (r) against the ship in question

**QADM-4** · `3.III.1` · ADM2 s19 sample Q4 (no answer given) · `ccp-1-3-7`

Facts C. Which s 4 HCAJA provision could Omar Bank rely on to advance an in rem claim against MT MANU?

a) Section 4(2), as Omar's claim falls within s 3(1)(a), (b), (c) or (r).
b) Section 4(3), as Omar's claim gives rise to a maritime lien.
c) Section 4(4)(a), (b) and (c), as the claim is in connection with a ship and the owner was the person liable in personam when the action arose and the beneficial owner when the action is brought.
d) Section 4(4)(d), as the claim is against any other ship of which, when the action is brought, the relevant person is the beneficial owner as respects all the shares.

**Answer: a.** A mortgage claim (s 3(1)(c)) proceeds against the ship in question under s 4(2), without the s 4(4) relevant-person tests. b: a mortgage is not a maritime lien.
*Cite: HCAJA s 4(2); ADM2 s18–19; `ccp-1-3-7`*

### 3.III.2 — s 4(3): maritime lien or other charge

**QSQ-A1** · `3.III.2` `3.I.2` · SQ p43 Q1, official key C · `ccp-1-3-8` `ccp-1-3-2`

Facts A. Which claim may the previous Master and crew have against MV SIRI AH?

A. A claim arising out of any agreement relating to the carriage of goods in a ship or the use or hire of a ship under Section 3(1)(h) read with Section 4(4) of the HCAJA.
B. A claim in respect of goods or materials supplied to a ship for her operation or maintenance under Section 3(1)(l) read with Section 4(4) of the HCAJA.
C. A claim by a master or a member of crew for wages under Section 3(1)(n) read with Section 4(3) of the HCAJA.
D. A claim by a master in respect of disbursements made on account of a ship under Section 3(1)(o) of the HCAJA.

**Answer: C.** Wages fall under s 3(1)(n), and as they carry a maritime lien the route is s 4(3). D: the claim is for salary, not disbursements.
*Cite: HCAJA ss 3(1)(n), 4(3); SQ p116 (key C); `ccp-1-3-8`, `ccp-1-3-2`*

See also QSQ-A2 and QADM1-2 under 3.II.2.

### 3.III.3 — s 4(4): claims in s 3(1)(d)–(q) — relevant person; arresting the ship itself

**QSQ-A7** · `3.III.3` · SQ p46 Q7, official key D · `ccp-1-3-9`

Facts B. Which s 4 HCAJA provision would YOUNG GOH have relied on to arrest the Vessel?

A. Section 4(2), as YOUNG GOH's claim falls within section 3(1)(a), (b), (c) or (r).
B. Section 4(3), as YOUNG GOH's claim gives rise to a maritime lien.
C. Sections 4(4)(a), (b) and (c), as the claim is in connection with a ship, the owner was the person liable in personam when the action arose, and when the action is brought the same person is the beneficial owner of that ship as respects all the shares in it.
D. Sections 4(4)(a), (b) and (c), as the claim is in connection with a ship, the demise charterer was the person liable in personam when the action arose, and when the action is brought the same person is the demise charterer of that ship.

**Answer: D.** YOUNG GOH's counterparty, and so the relevant person, is the demise charterer ZAO ZIJING; s 4(4)(c) allows arrest of the ship if the relevant person is its demise charterer when the action is brought. C: the owner GO JING is not liable on the time charter. A and B: a charter claim is s 3(1)(h) with no maritime lien.
*Cite: HCAJA s 4(4); SQ p116 (key D); `ccp-1-3-9`*

**QSQ-A10** · `3.III.3` · SQ p47 Q10, official key C · `ccp-1-3-9`

Facts B. Which s 4 HCAJA provision could HOODOO Yard have relied on in support of its in rem claim? (Options A–D as in QSQ-A7, with "HOODOO Yard's claim" in A and B.)

**Answer: C.** The repairs were done at the owner GO JING's request, so GO JING is the person liable in personam, owned the ship when the cause of action arose, and still owns it when the action is brought (s 4(4)(a)–(c)). D: the demise charterer did not order the repairs. A and B: a repair claim is s 3(1)(m) with no maritime lien.
*Cite: HCAJA s 4(4); SQ p116 (key C); `ccp-1-3-9`*

**QADM-2** · `3.III.3` · ADM2 s17 sample Q2 (no answer given) · `ccp-1-3-9`

Facts C. Which s 4 HCAJA provision would Bruno Bunkers have relied on to arrest MT MANU?

a) Section 4(2), as Bruno's claim falls within s 3(1)(a), (b), (c) or (r).
b) Section 4(3), as Bruno's claim gives rise to a maritime lien.
c) Section 4(4)(a), (b) and (c), as the claim is in connection with a ship, the owner was the person who would be liable in personam when the action arose, and when the action is brought the same person is the beneficial owner of that ship as respects all the shares in it.
d) Section 4(4)(d), as the claim is against any other ship of which, when the action is brought, the relevant person is the beneficial owner as respects all the shares in it.

**Answer: c.** A bunker claim (s 3(1)(l)) carries no maritime lien; Bruno says Ruben Tankers, the owner, is liable in personam (Glazer contracting on its behalf), and Ruben still owns MT MANU, so the ship itself is arrested under s 4(4)(c). d: MT MANU is the ship in question, not a sister ship.
*Cite: HCAJA s 4(4); ADM2 s17; `ccp-1-3-9`*

See also QADM1-1 under 3.I.2.

### 3.III.4 — Sister-ship arrest (s 4(4)(d)); one-ship companies

**QSQ-A5** · `3.III.4` · SQ p45 Q5, official key D · `ccp-1-3-10`

Facts A. Before starting an action against MV SIRI AH, FOOL-HUM Ltd learns that GUNNERS Ltd owns MV DEEVEESIE, which is expected in Singapore shortly. Which statement is correct?

A. FOOL-HUM Ltd should only pursue its claim against MV SIRI AH and not MV DEEVEESIE because its claim arises in connection with MV SIRI AH, and not MV DEEVEESIE.
B. FOOL-HUM Ltd cannot arrest MV DEEVEESIE because the party liable in personam for its claim is BLUES Ltd, and it is not the owner of MV DEEVEESIE.
C. FOOL-HUM Ltd cannot arrest MV DEEVEESIE because FOOL-HUM cannot satisfy Section 3(1) of the HCAJA.
D. FOOL-HUM Ltd can arrest MV DEEVEESIE because the party liable in personam for its claim is GUNNERS Ltd, and it is the beneficial owner of MV DEEVEESIE.

**Answer: D.** GUNNERS issued the bills of lading and owned the ship at the July mis-delivery, so it is the relevant person; it beneficially owns MV DEEVEESIE when the action is brought, so a sister-ship arrest lies (s 4(4)(d)). A: s 4(4)(d) exists for this. B: BLUES had sold the ship before the mis-delivery. C: the claim is s 3(1)(g).
*Cite: HCAJA s 4(4)(d); SQ p116 (key D); `ccp-1-3-10`*

**QADM1-M** · `3.III.4` `3.III.6` · ADM1 s6 mock question (scenarios only; options added here) · `ccp-1-3-10` `ccp-1-3-12`

Cargo carried on the ship MABEL, owned by Mabel Shipping Ltd, was damaged in January. The cargo owners wish to arrest in September. In which of these scenarios can they bring an in rem action as stated?

(a) In September MABEL is still owned by Mabel Shipping Ltd — arrest MABEL.
(b) MABEL was sold to Helen Shipping Ltd and renamed HELEN in July — arrest HELEN.
(c) As (b), but Mabel Shipping Ltd owns another ship, MANDY — arrest MANDY.
(d) As (b), but Mabel Shipping Ltd is the demise charterer of the ship MAGGIE — arrest MAGGIE.

A. (a) only.
B. (a) and (c) only.
C. (a), (b) and (c) only.
D. All four.

**Answer: B.** A cargo claim (s 3(1)(g)) carries no maritime lien, so it needs s 4(4). (a): the relevant person still owns the ship (s 4(4)(c)). (b): a valid sale before the action is brought defeats the claim against that ship (*The Monica S*). (c): MANDY is beneficially owned by the relevant person when the action is brought (s 4(4)(d)). (d): a ship the relevant person only charters by demise is not a sister ship.
*Cite: HCAJA s 4(4)(c)–(d); ADM1 s5–6; Cel-ADM; `ccp-1-3-10`, `ccp-1-3-12`*

**QADM1-5** · `3.III.4` · ADM1 mock exam Q5 (no answer given) · `ccp-1-3-10`

Facts D. Cargo now wants to arrest VARDEE. Which statement about Cargo's claim on VARDEE is true?

A) Cargo's claim satisfies Section 3(1)(d) of the HCAJA.
B) Cargo's claim satisfies Section 4(3) against VARDEE as there is a maritime lien against VARDEE.
C) Cargo's claim satisfies Section 4(4)(b) as the persons liable in personam are the managers, Foxes Shipmanagement.
D) Cargo's claim satisfies Sections 4(4)(b) and 4(4)(c) even though VARDEE is owned by another entity, not King Powder Inc.

**Answer: A.** Cargo's claim against the colliding ship KESPAR's interests is for damage done by a ship (s 3(1)(d)). B: any maritime lien attaches to KESPAR, not VARDEE. C: managers are not the persons liable. D: VARDEE belongs to a different one-ship company, so it is neither the ship in question nor a sister ship.
*Cite: HCAJA ss 3(1)(d), 4(4); ADM1 s5–6; `ccp-1-3-10`*

**QADM1-7** · `3.III.4` `3.III.3` · ADM1 mock exam Q7 (no answer given) · `ccp-1-3-10` `ccp-1-3-9`

Facts D. It turns out that Brendon Rodder owns MADDISSON, which is not under bareboat charter. Cargo now wants to pursue MADDISSON. Which statement is correct?

A) Cargo's claim does not satisfy Section 3(1)(d) of the HCAJA.
B) Cargo's claim against MADDISSON has a maritime lien.
C) Cargo's claim satisfies Section 4(4)(d) because MADDISSON is owned by Brendon Rodder.
D) Cargo's claim does not satisfy Section 4(4)(b) because KESPAR is not owned by Brendon Rodder.

**Answer: C.** Brendon Rodder, KESPAR's bareboat charterer, was its charterer and in possession and control when the collision occurred (s 4(4)(b)), and it beneficially owns MADDISSON when the action is brought, so MADDISSON can be arrested as a sister ship (s 4(4)(d)). D: s 4(4)(b) covers a charterer. B: a maritime lien attaches only to the colliding ship. A: collision damage is s 3(1)(d).
*Cite: HCAJA s 4(4)(b), (d); ADM1 s5–6; `ccp-1-3-10`, `ccp-1-3-9`*

### 3.III.5 — The Bunga Melati 5 five-step test

**Q3-4** · `3.III.5` · own question · `ccp-1-3-11`

Under *The Bunga Melati 5* [2012] 4 SLR 546, which step need NOT be proved on a balance of probabilities by a claimant invoking s 4(4)?

A. That the claim arises in connection with a ship.
B. The identity of the person who would be liable in personam, which need only be identified.
C. That the relevant person was the owner, charterer or in possession or control of the ship when the cause of action arose.
D. That the relevant person was the beneficial owner or demise charterer of the ship when the action was brought.

**Answer: B.** Step 3 requires only identification of the person liable in personam. Step 1 requires proof of the jurisdictional facts plus an arguable case on the type of claim; steps 2, 4 and 5 are proved on a balance of probabilities.
*Cite: ADM1 s7–8; ADM2 s8–9; `ccp-1-3-11`*

### 3.III.6 — Change of ownership or end of a demise charter before the action is brought

**QSQ-A8** · `3.III.6` · SQ p46 Q8, official key B · `ccp-1-3-12`

Facts B. Which statement relating to YOUNG GOH's claim is CORRECT?

A. YOUNG GOH can invoke the admiralty jurisdiction of the Singapore High Court as it has a maritime lien against the Vessel.
B. YOUNG GOH can invoke the admiralty jurisdiction of the Singapore High Court, even after the demise charter has been terminated.
C. YOUNG GOH cannot invoke the admiralty jurisdiction of the Singapore High Court as the demise charter has been terminated.
D. YOUNG GOH cannot invoke the admiralty jurisdiction of the Singapore High Court as it does not have a statutory lien against the Vessel.

**Answer: B (official key).** The key treats the purported termination for an alleged, unestablished repudiatory breach as not, by itself, ending the demise charter for s 4(4)(c), so ZAO ZIJING is still the demise charterer when the action is brought. This reason is inferred from the facts; the key gives none (see block 3-12). A: a charter claim carries no maritime lien. C is the opposite conclusion. D: a statutory lien arises by bringing the action.
*Cite: HCAJA s 4(4)(c); SQ p116 (key B); `ccp-1-3-12`*

See also QADM1-M under 3.III.4 (sale before action defeats a claim without a maritime lien) and QADM1-4 under 3.VII.2.

### 3.IV Before the arrest

Sub-points 3.IV.1–3.IV.3. No real question; own questions Q3-5 to Q3-7.

### 3.IV.1 — Strategic considerations: one ship one arrest, value of the vessel, costs, alternatives, arbitration

**Q3-5** · `3.IV.1` · own question · `ccp-1-3-13`

A claimant with a US$8m claim can arrest either the offending ship (value about US$3m, heavily mortgaged) or a sister ship (value about US$12m). Which consideration is CORRECT?

A. It may arrest both ships for the same claim to be safe.
B. It may arrest only one ship per cause of action (*The Banco*), and security is limited to the claim (with interest and costs) or the arrested ship's value, whichever is lower (*The Charlotte*), so the sister ship is the better choice.
C. Ship value is irrelevant to security.
D. An arrest can never support a foreign arbitration.

**Answer: B.** The claimant should also weigh port dues, Sheriff's expenses and cargo discharge costs, which its solicitors' undertaking may have to meet. D: an arrest may obtain security for a foreign arbitration (ss 6, 7, 12 IAA).
*Cite: Cel-ADM (lecture 2); ADM-Guide paras 4–10; `ccp-1-3-13`*

### 3.IV.2 — Duty of full and frank disclosure

**Q3-6** · `3.IV.2` · own question · `ccp-1-3-14`

At the ex parte arrest hearing, what must the claimant disclose?

A. Every possible defence the owner might raise on the merits.
B. All material facts, including disadvantageous ones such as a prior arrest or action for the same claim or doubts whether the defendant contracted as principal or agent — matters that could deliver a "knock-out blow" or show an abuse of process (*The Eagle Prestige*).
C. Nothing, because arrest is as of right.
D. Only the claim amount.

**Answer: B.** Given the low merits threshold, ordinary defences need not generally be disclosed (A wrong). Breach may lead to the warrant being set aside, and to damages if deliberate or malicious.
*Cite: ADM2 s11; ADM1 s12; `ccp-1-3-14`*

### 3.IV.3 — Pre-arrest preparation: searches, tracking, caveats against arrest

**Q3-7** · `3.IV.3` · own question · `ccp-1-3-15`

A shipowner expects creditors to try to arrest its ship when it calls at Singapore. What can it do beforehand?

A. Nothing; arrests cannot be pre-empted.
B. File a caveat against arrest, undertaking to provide security; the Duty Registrar is then unlikely to issue a warrant unless there are good reasons.
C. Ask the MPA to refuse entry to all arresting parties.
D. Obtain a Mareva injunction against all creditors.

**Answer: B.** On the claimant's side, preparation means ship tracking, ownership searches, checking the list of vessels already under arrest, and arranging funds for the Sheriff's expenses.
*Cite: Cel-ADM (lecture 2); ADM-Guide paras 9–10, 70; `ccp-1-3-15`*

### 3.V The arrest

Sub-points 3.V.1–3.V.2. No real question; own questions Q3-8, Q3-9.

### 3.V.1 — Arrest papers, solicitor's undertaking, Duty Registrar

**Q3-8** · `3.V.1` · own question · `ccp-1-3-16`

Which of these is NOT filed with a request for a warrant of arrest under Order 33 ROC 2021?

A. The admiralty originating claim in rem.
B. An affidavit leading to arrest, with full and frank disclosure.
C. The claimant's solicitors' undertaking to the Sheriff for the expenses of the arrest.
D. A court order for appraisement and sale.

**Answer: D.** Appraisement and sale come later, if the arrest continues. The claimant attends before the Duty Registrar after a caveat search made no more than 15 minutes before the hearing.
*Cite: ADM-Guide paras 11–16; `ccp-1-3-16`*

### 3.V.2 — Service of the arrest papers; port limits; after the arrest

**Q3-9** · `3.V.2` · own question · `ccp-1-3-17`

A claimant has a vessel arrested outside Singapore's port limits, though within territorial waters, without authority to do so. What is the likely result?

A. The arrest stands; territorial waters are enough.
B. The arrest may be set aside, with damages (*The Trade Resolve*).
C. The ship must be re-arrested in port within 7 days.
D. Only the Sheriff is liable.

**Answer: B.** Service is generally by fixing the papers to the windows in front of the wheelhouse (O 33 r 10); the Sheriff then notifies the MPA.
*Cite: ADM-Guide paras 24–26; Cel-ADM (lecture 2); `ccp-1-3-17`*

### 3.VI Security and release

Sub-points 3.VI.1–3.VI.4. Real questions: QADM-5, Q23-39, QADM1-3 (3.VI.1), QADM1-6 (3.VI.2), QSQ-A4 (3.VI.4). Own question Q3-10.

### 3.VI.1 — Security demand: quantum and justification

**QADM-5** · `3.VI.1` `3.VI.2` · ADM2 s20 sample Q5 (no answer given) · `ccp-1-3-18` `ccp-1-3-19`

Facts C. To release MT MANU, Ruben Tankers proposes a P&I Club letter of undertaking as security. Which statement about Bruno Bunkers' claim is correct?

a) Bruno Bunkers is entitled to reject the proposal because a P&I Club LOU is inadequate.
b) Bruno Bunkers is entitled to insist that the P&I Club LOU covers its principal claim, interest and costs, on its reasonably arguable best case.
c) Bruno Bunkers is only entitled to insist that the P&I Club LOU covers its principal claim.
d) Bruno Bunkers should apply to Court for a more favourable security.

**Answer: b.** Security may be demanded for the reasonably arguable best case: principal, interest (usually up to 3 years) and costs (*The Moschanthy*). a: a reputable Club LOU is acceptable. c: too little. d: no basis.
*Cite: ADM2 s12, s20; `ccp-1-3-18`, `ccp-1-3-19`*

**Q23-39** · `3.VI.1` `3.VI.2` · 2023 CCP Paper 1 Q39 (no official answer) · `ccp-1-3-18` `ccp-1-3-19`

*Facts for Q23-39 and Q23-40 (MV MOO):* ETH Pte Ltd demise-chartered MV MOO from its registered owner, Glazors Bhd, from 1 January to 1 December 2023. Glazors bought MV MOO from SAF Ltd on 1 December 2022. On 20 May 2023 Maclaren Pte Ltd, a bunker trader, ordered bunkers for MV MOO from Bunk-In Pte Ltd, allegedly "on behalf of MV MOO", cash on delivery; after delivery on 22 May, Bunk-In invoiced the "Owners". On 25 May 2023 Onan Ltd served a warrant of arrest on MV MOO for repairs carried out on 1 June 2022, quickly followed by a demand for security. ETH said the arrest was unlawful but could offer only a corporate guarantee from its parent, Ratcleve Pte Ltd (SGX-listed since 2010; profitable in its latest year after 2 years in the red, which ETH blamed on Covid). Onan rejected it and stopped negotiating; MV MOO remains under arrest and Onan is applying for a sale pendente lite.

Assuming that Onan has a valid in rem claim, which statement reflects a reasonable demand for security in exchange for the release of MV MOO?

A. A demand that security be provided to cover Onan Ltd's full claim, interest over 3 years and the costs of prosecuting the action.
B. A demand that security be provided strictly in the form of a bank guarantee.
C. A demand that an acceptable security be provided within 48 hours, failing which any further offers of security will not be considered.
D. A demand that security be provided for an amount that would cover only the quantum of Onan's reasonably best arguable case, in the form of a Club letter of undertaking that is answerable to a judgment of the English Courts.

**Answer: A.** The claim (on its reasonably arguable best case), 3 years' interest and costs is the usual measure. B: other forms (e.g. a reputable Club LOU, payment into court) are acceptable. C: an arbitrary deadline is oppressive. D: security must answer to a judgment of the competent court (Singapore), not a foreign one, and "only" the claim quantum leaves out interest and costs. (The candidate's selection, A, is right.)
*Cite: ADM1 s9–11; ADM2 s12; `ccp-1-3-18`, `ccp-1-3-19`*

**QADM1-3** · `3.VI.1` `3.VI.2` · ADM1 mock exam Q3 (no answer given) · `ccp-1-3-18` `ccp-1-3-19`

Facts D. Assuming BERNT LEANO has a valid in rem claim, which reflects a reasonable demand for security for KESPAR's release after her arrest by BERNT LEANO?

A) A demand that security be provided strictly in the form of a bail bond only.
B) A demand that security be provided strictly by a payment into court.
C) A demand that security be provided for an amount that would cover only the quantum of BERNT LEANO's reasonably best arguable case.
D) A demand that security be provided to cover BERNT LEANO's full claim, interest over 3 years and the costs of prosecuting the action.

**Answer: D.** Same measure as Q23-39. A and B insist on one form; C omits interest and costs.
*Cite: ADM1 s9–11; `ccp-1-3-18`, `ccp-1-3-19`*

### 3.VI.2 — Acceptable forms of security

**QADM1-6** · `3.VI.2` · ADM1 mock exam Q6 (no answer given) · `ccp-1-3-19`

Facts D. Regarding the proposal from Fillberth Side P&I Club, which statement is correct?

A) Cargo has received an acceptable proposal from the Club and should accept it promptly.
B) Cargo should reject the proposal because security should strictly be in the form of a payment into court.
C) Cargo should ask the Club for its financial information to verify its financial position and, if it is in fact in financial difficulties, request a bank guarantee.
D) Cargo should accept the proposal even though it answers to a final judgment of the English Courts.

**Answer: C.** Whether a club is reputable may require its financial information; if it is in difficulty, the claimant may ask for a bank guarantee. A and D: the club's position is doubtful and the wording must answer to the competent court's judgment, not the English courts'. B: payment into court is only one acceptable form.
*Cite: ADM1 s10–11, s15, s21; `ccp-1-3-19`*

See also QADM-5, Q23-39 and QADM1-3 under 3.VI.1.

### 3.VI.3 — Disputes over security; security under protest

**Q3-10** · `3.VI.3` · own question · `ccp-1-3-20`

The arresting party refuses a bank guarantee from a first-class Singapore bank for the full amount it demanded, insisting on cash. What can the owner do?

A. Nothing; the arresting party chooses the form.
B. Provide security under protest and apply for release and damages for wrongful continued detention (*The Evmar*); the Court can also moderate quantum and assess the wording.
C. Sail away, since the arrest lapses on refusal.
D. Only appeal to the MPA.

**Answer: B.** A first-class Singapore bank guarantee is always acceptable; unreasonable refusal exposes the claimant to damages for wrongful continuation of the arrest.
*Cite: ADM1 s11; Cyril-ADM §4.3; `ccp-1-3-20`*

### 3.VI.4 — Release from arrest; caveats against release; judicial sale

**QSQ-A4** · `3.VI.4` `3.VII.1` · SQ p44 Q4, official key A · `ccp-1-3-21` `ccp-1-3-22`

Facts A. GUNNERS Ltd wants MV SIRI AH released from arrest as expeditiously as possible. Which advice should NOT form part of your recommendation?

A. GUNNERS Ltd should apply to set aside the warrant of arrest on the ground that the admiralty jurisdiction of the Court has been wrongly invoked while the vessel continues to be under arrest.
B. GUNNERS Ltd should demand that BLUES Ltd provide acceptable security to fully secure the Master's and crew's claim, with interest over 3 years and the costs of prosecuting the action, and reserve GUNNERS's rights against BLUES Ltd for the arrest.
C. If BLUES Ltd refuses, GUNNERS Ltd should provide acceptable security to fully secure the Master's and crew's claim, with interest over 3 years and costs, while reserving its rights against BLUES Ltd.
D. GUNNERS Ltd should consider if the warrant of arrest may be set aside.

**Answer: A.** The crew's wage claim carries a maritime lien, so jurisdiction was properly invoked under s 4(3); a set-aside application would fail and keep the ship detained. B and C are the quick route to release (then an instrument of release under O 33 r 13); D, merely considering it, is sensible.
*Cite: ADM2 s13; ADM-Guide paras 40–43; SQ p116 (key A); `ccp-1-3-21`, `ccp-1-3-22`*

### 3.VII Challenging the arrest; wrongful arrest

Sub-points 3.VII.1–3.VII.2. Real questions: QADM-6 (3.VII.1), QSQ-A4 (3.VII.1, under 3.VI.4), QADM-7, Q23-40, QADM1-4 (3.VII.2).

### 3.VII.1 — Grounds to set aside the arrest or strike out the action

**QADM-6** · `3.VII.1` · ADM2 s21 sample Q6 (no answer given) · `ccp-1-3-22`

Facts C. Ruben Tankers wants to set aside Bruno Bunkers' arrest. Which statement is correct?

a) Ruben Tankers cannot set aside the arrest once the vessel has been released.
b) Ruben Tankers can set aside if it can show that it was only the demise charterer of MT MANU, and not the owner, at the time when Bruno Bunkers' cause of action accrued.
c) Ruben Tankers can set aside the arrest if it can show that it is not the party liable in personam for Bruno Bunkers' claim.
d) Ruben Tankers can set aside the arrest if it can show that it was only the demise charterer, and not the owner, at the time when the action was brought.

**Answer: c.** If Ruben Tankers is not the person liable in personam, s 4(4) is not satisfied and the jurisdiction was wrongly invoked (*The Bunga Melati 5*). a: release does not by itself prevent a challenge. b and d: s 4(4)(b) is satisfied by a charterer when the cause of action arose, and s 4(4)(c) by a demise charterer when the action is brought.
*Cite: ADM2 s14, s21; HCAJA s 4(4); `ccp-1-3-22`*

See also QSQ-A4 under 3.VI.4.

### 3.VII.2 — Damages for wrongful arrest and wrongful continuation of arrest

**QADM-7** · `3.VII.2` `3.IV.2` · ADM2 s22 sample Q7 (no answer given) · `ccp-1-3-23` `ccp-1-3-14`

Facts C. Ruben Tankers asks whether it can claim damages for wrongful arrest. Which statement is correct?

a) Every case of wrongful arrest will result in a claim for damages, subject only to proof of loss.
b) A claim for damages for wrongful arrest is likely to be awarded if Bruno Bunkers knew that the supply contract contained an arbitration agreement, but did not disclose it to the Court at the ex parte hearing.
c) An arrest that is set aside for failure to give full and frank disclosure must necessarily result in a claim for damages.
d) A claim for damages for wrongful arrest is likely to be awarded if Bruno Bunkers knew that it did not have a factual basis to assert that Glazer Shipping contracted on behalf of Ruben Tankers.

**Answer: d.** Damages need bad faith or gross negligence implying malice (*The Kiku Pacific*; *The Vasiliy Golovnin*), e.g. arresting knowing there is no factual basis. a and c: a set-aside, even for non-disclosure, does not automatically give damages. b: an arbitration clause does not bar an arrest for security (ss 6, 7, 12 IAA); its non-disclosure may risk the warrant being set aside, but without bad faith or gross negligence it does not make damages likely.
*Cite: ADM2 s14, s22; ADM1 s12; `ccp-1-3-23`, `ccp-1-3-14`*

**Q23-40** · `3.VII.2` · 2023 CCP Paper 1 Q40 (no official answer) · `ccp-1-3-23`

Facts as for Q23-39 (MV MOO). Having learnt that SAF (not Glazors) owned MV MOO when it was repaired and so is the party liable in personam for the repairs, ETH is considering a claim for damages for wrongful arrest. Which advice is incorrect?

A. Damages for wrongful arrest may be awarded even if the warrant of arrest is not set aside.
B. Onan's warrant of arrest may be set aside with damages if Onan knew that MV MOO was not owned by Glazors at the time of repairs on 1 June 2022, and did not disclose it when the warrant was applied for.
C. ETH will only be entitled to an award of damages for wrongful arrest if Onan's in rem claim is ultimately dismissed at trial for being unsustainable.
D. ETH will be entitled to damages for wrongful arrest if it can show that Onan acted with malice when it arrested MV MOO.

**Answer: C.** The test is bad faith or gross negligence implying malice, not the outcome at trial. D states the test. B: a deliberate non-disclosure of facts showing no jurisdiction may lead to set-aside and damages. A: damages for wrongful continuation of an arrest can follow from unreasonably rejecting acceptable security without the warrant being set aside (*The Evmar*). (The candidate's selection, A, is wrong.)
*Cite: ADM1 s12; Cyril-ADM §5; `ccp-1-3-23`*

**QADM1-4** · `3.VII.2` `3.III.6` · ADM1 mock exam Q4 (no answer given) · `ccp-1-3-23` `ccp-1-3-12`

Facts D. Cargo waited before acting against BERNT LEANO, which was meanwhile sold to Le Blues Inc (name unchanged). Cargo arrested BERNT LEANO, and Le Blues asks about damages for wrongful arrest. Which advice is correct?

A) Cargo's warrant of arrest may be set aside with damages for wrongful arrest if Cargo knew that BERNT LEANO was owned by Le Blues at the time of arrest, and did not disclose it when the warrant was applied for. (The slide notes that no maritime lien attaches to the carrying ship.)
B) Le Blues will not be entitled to damages for wrongful arrest even if it can show that Cargo acted with malice when it arrested BERNT LEANO.
C) Damages for wrongful arrest may be awarded as long as the warrant of arrest is set aside.
D) Le Blues will not be entitled to an award of damages for wrongful arrest because BERNT LEANO's name was not changed.

**Answer: A.** Cargo's claim against the carrying ship has no maritime lien, so after a sale before the action the s 4(4) route fails (*The Monica S*); arresting while knowing that, and concealing it, is the bad-faith case for damages. B: malice is exactly what founds damages. C: set-aside alone is not enough. D: the name is irrelevant.
*Cite: ADM1 s6, s12; `ccp-1-3-23`, `ccp-1-3-12`*

---

# Part 2 — Drills

Timed sets built only from Part 1 questions; find each by its ID (Ctrl-F the ID). Sit the set closed-book first, then check against the answer key and the explanation in Part 1, and log every miss in `weak-spots.md` under its Key. **Time limits** use the real exam's pace: the 2023 CCP Paper 1 instruction sheet gives 60 MCQs in two hours, so each Drill allows 2 minutes per question, rounded up to the next 5 minutes. Drills 1–10 run by Topic and together use every one of the 260 questions in Part 1 once. Drills 11–14 re-use them as mixed mocks: Drill 11 is the 40 Sample Questions with the official key; Drill 12 is the 51 held questions of the 2023 paper in their original order (its Subject split was Banking 18, Corporate Governance 19, Admiralty 5, Insolvency 18), the closest thing to a full sitting; Drill 13 is the 2021 Insolvency MCQs; Drill 14 samples the own questions across all four Subjects.

| Drill | Covers | Questions | Time |
|---|---|---|---|
| 1 | Banking & Fundraising: corporate finance, bank lending, facility agreement, security (0.I–0.IV) | 33 | 70 min |
| 2 | Banking & Fundraising: bonds, prospectus exemptions, private equity, IPO (0.V–0.IX) | 32 | 65 min |
| 3 | Corporate Governance: introduction, disclosure, announcements, reporting (1.I–1.VI) | 21 | 45 min |
| 4 | Corporate Governance: interested person transactions and the Code (1.VII–1.IX) | 17 | 35 min |
| 5 | Corporate Governance: directors, committees, remuneration, market conduct (1.X–1.XIII) | 24 | 50 min |
| 6 | Insolvency: liquidation, winding up, liquidator, distribution (2.I–2.VI) | 36 | 75 min |
| 7 | Insolvency: bankruptcy and its alternatives (2.VII–2.VIII) | 18 | 40 min |
| 8 | Insolvency: judicial management and avoidance (2.IX–2.X) | 24 | 50 min |
| 9 | Insolvency: schemes, rescue financing, ipso facto, choosing a procedure, cross-border (2.XI–2.XIV) | 17 | 35 min |
| 10 | Admiralty: all Topics (3.I–3.VII) | 38 | 80 min |
| 11 | Mixed mock: all 40 Sample Questions, official key | 40 | 80 min |
| 12 | Mixed mock: the 2023 CCP Paper 1 questions held, in paper order | 51 | 105 min |
| 13 | Insolvency mock: the 2021 INS MCQs held, in paper order | 32 | 65 min |
| 14 | Mixed mock: own questions across all four Subjects | 43 | 90 min |

### Drill 1 — Banking & Fundraising: corporate finance, bank lending, facility agreement, security (0.I–0.IV) · 33 questions · 70 minutes

**Questions:** Q0-1, Q0-2, QSQ-B1, QSQ-B6, Q23-1, Q23-2, Q0-3, QSQ-B2, Q23-3, Q23-4, Q0-4, QSQ-B10, Q23-7, Q0-5, Q0-6, QSQ-B3, Q0-7, Q0-8, Q0-9, QSQ-B4, Q23-5, Q0-10, Q0-11, QSQ-B8, Q0-12, QSQ-B9, Q0-13, Q23-6, Q0-14, Q0-15, Q0-16, Q0-17, Q0-18.

**Answer key:** Q0-1 D · Q0-2 B · QSQ-B1 A · QSQ-B6 A · Q23-1 A · Q23-2 C · Q0-3 B · QSQ-B2 A · Q23-3 C · Q23-4 C · Q0-4 B · QSQ-B10 A · Q23-7 D · Q0-5 C · Q0-6 C · QSQ-B3 A · Q0-7 B · Q0-8 B · Q0-9 B · QSQ-B4 A · Q23-5 C · Q0-10 B · Q0-11 B · QSQ-B8 D · Q0-12 B · QSQ-B9 A · Q0-13 B · Q23-6 D · Q0-14 B · Q0-15 B · Q0-16 B · Q0-17 B · Q0-18 B.

### Drill 2 — Banking & Fundraising: bonds, prospectus exemptions, private equity, IPO (0.V–0.IX) · 32 questions · 65 minutes

**Questions:** Q0-19, Q23-8, Q0-20, Q0-21, Q0-22, Q23-9, Q23-10, Q0-23, Q0-24, Q0-25, Q0-26, Q23-11, Q0-27, Q0-28, Q0-29, Q0-30, Q0-31, Q23-12, Q23-14, Q0-32, QSQ-B7, Q0-33, QSQ-B5, Q23-15, Q23-16, Q0-34, Q0-35, Q23-17, Q23-13, Q0-36, Q23-18, Q0-37.

**Answer key:** Q0-19 D · Q23-8 D · Q0-20 B · Q0-21 B · Q0-22 B · Q23-9 B · Q23-10 A · Q0-23 B · Q0-24 C · Q0-25 C · Q0-26 B · Q23-11 D · Q0-27 B · Q0-28 B · Q0-29 B · Q0-30 B · Q0-31 B · Q23-12 C · Q23-14 D · Q0-32 D · QSQ-B7 C · Q0-33 B · QSQ-B5 B · Q23-15 D · Q23-16 C · Q0-34 B · Q0-35 B · Q23-17 D · Q23-13 A · Q0-36 B · Q23-18 B · Q0-37 B.

### Drill 3 — Corporate Governance: introduction, disclosure, announcements, reporting (1.I–1.VI) · 21 questions · 45 minutes

**Questions:** Q1-1, Q1-2, Q1-3, Q1-4, Q1-5, Q1-6, Q1-7, Q23-19, QSQ-G7, Q1-8, QSQ-G2, QSQ-G10, Q1-9, Q1-10, QSQ-G3, Q23-21, Q1-11, Q23-27, Q23-25, Q1-12, Q1-13.

**Answer key:** Q1-1 C · Q1-2 B · Q1-3 B · Q1-4 B · Q1-5 B · Q1-6 B · Q1-7 B · Q23-19 D · QSQ-G7 B · Q1-8 B · QSQ-G2 D · QSQ-G10 D · Q1-9 B · Q1-10 B · QSQ-G3 B · Q23-21 C · Q1-11 A · Q23-27 C · Q23-25 C · Q1-12 B · Q1-13 B.

### Drill 4 — Corporate Governance: interested person transactions and the Code (1.VII–1.IX) · 17 questions · 35 minutes

**Questions:** Q1-14, Q1-15, QSQ-G5, Q23-30, Q23-32, QSQ-G8, Q1-16, Q1-17, Q1-18, Q1-19, Q1-20, Q1-21, Q1-22, Q1-23, QSQ-G9, Q23-29, Q1-24.

**Answer key:** Q1-14 B · Q1-15 D · QSQ-G5 D · Q23-30 A · Q23-32 B · QSQ-G8 B · Q1-16 B · Q1-17 B · Q1-18 B · Q1-19 B · Q1-20 B · Q1-21 B · Q1-22 B · Q1-23 B · QSQ-G9 B · Q23-29 A · Q1-24 C.

### Drill 5 — Corporate Governance: directors, committees, remuneration, market conduct (1.X–1.XIII) · 24 questions · 50 minutes

**Questions:** Q1-25, QSQ-G4, QSQ-G6, Q23-24, Q23-28, Q23-22, Q23-31, Q1-26, Q1-27, Q23-35, Q23-33, Q23-37, Q23-36, Q23-26, Q1-28, Q1-29, QSQ-G1, Q23-20, Q1-30, Q1-31, Q1-32, Q1-33, Q1-34, Q1-35.

**Answer key:** Q1-25 B · QSQ-G4 D · QSQ-G6 D · Q23-24 C · Q23-28 C · Q23-22 B · Q23-31 A · Q1-26 B · Q1-27 C · Q23-35 D · Q23-33 B · Q23-37 C · Q23-36 B · Q23-26 D · Q1-28 B · Q1-29 B · QSQ-G1 A · Q23-20 A · Q1-30 A · Q1-31 A · Q1-32 B · Q1-33 B · Q1-34 B · Q1-35 B.

### Drill 6 — Insolvency: liquidation, winding up, liquidator, distribution (2.I–2.VI) · 36 questions · 75 minutes

**Questions:** Q2-1, Q21I-25, Q21I-26, Q2-2, Q21I-3, Q2-3, Q2-4, QSQ-I3, Q23-45, Q21I-17, QSQ-I7, Q2-5, QSQ-I1, Q23-43, QSQ-I2, Q2-6, Q2-7, Q21I-21, Q2-8, Q2-9, Q2-10, QSQ-I4, Q23-46, Q21I-18, Q21I-35, Q2-11, Q2-12, Q2-13, Q2-14, Q2-15, Q2-16, Q2-17, Q2-18, Q21I-2, Q2-19, Q21I-27.

**Answer key:** Q2-1 B · Q21I-25 A · Q21I-26 B · Q2-2 B · Q21I-3 C · Q2-3 D · Q2-4 B · QSQ-I3 A · Q23-45 B · Q21I-17 C · QSQ-I7 D · Q2-5 B · QSQ-I1 C · Q23-43 D · QSQ-I2 D · Q2-6 B · Q2-7 B · Q21I-21 A · Q2-8 B · Q2-9 B · Q2-10 B · QSQ-I4 D · Q23-46 D · Q21I-18 D · Q21I-35 C · Q2-11 B · Q2-12 B · Q2-13 B · Q2-14 B · Q2-15 B · Q2-16 B · Q2-17 C · Q2-18 C · Q21I-2 A · Q2-19 B · Q21I-27 D.

### Drill 7 — Insolvency: bankruptcy and its alternatives (2.VII–2.VIII) · 18 questions · 40 minutes

**Questions:** Q21I-8, QSQ-I5, Q23-47, Q21I-9, Q23-48, Q2-20, Q21I-14, Q21I-24, Q2-21, Q21I-19, Q2-22, Q2-23, Q2-24, Q2-25, Q2-26, Q2-27, Q21I-5, Q23-49.

**Answer key:** Q21I-8 A · QSQ-I5 C · Q23-47 B · Q21I-9 A · Q23-48 D · Q2-20 B · Q21I-14 B · Q21I-24 C · Q2-21 B · Q21I-19 C · Q2-22 D · Q2-23 B · Q2-24 B · Q2-25 B · Q2-26 C · Q2-27 B · Q21I-5 D · Q23-49 D.

### Drill 8 — Insolvency: judicial management and avoidance (2.IX–2.X) · 24 questions · 50 minutes

**Questions:** Q2-28, QSQ-I10, Q23-50, QSQ-I9, Q21I-22, Q2-29, Q21I-11, Q21I-10, Q23-52, Q21I-15, Q21I-16, Q23-51, Q21I-30, Q2-30, Q21I-4, Q2-31, Q21I-28, Q23-55, Q21I-7, Q23-57, Q21I-33, Q2-32, Q2-33, Q21I-12.

**Answer key:** Q2-28 B · QSQ-I10 D · Q23-50 D · QSQ-I9 C · Q21I-22 B · Q2-29 B · Q21I-11 C · Q21I-10 D · Q23-52 B · Q21I-15 B · Q21I-16 A · Q23-51 C · Q21I-30 A · Q2-30 B · Q21I-4 D · Q2-31 B · Q21I-28 B · Q23-55 A · Q21I-7 B · Q23-57 A · Q21I-33 C · Q2-32 B · Q2-33 B · Q21I-12 A.

### Drill 9 — Insolvency: schemes, rescue financing, ipso facto, choosing a procedure, cross-border (2.XI–2.XIV) · 17 questions · 35 minutes

**Questions:** Q2-34, Q23-58, Q21I-23, Q2-35, QSQ-I8, Q23-59, Q21I-6, Q23-60, Q21I-20, Q2-36, Q2-37, Q2-38, Q21I-13, Q21I-29, QSQ-I6, Q2-39, Q21I-31.

**Answer key:** Q2-34 B · Q23-58 B · Q21I-23 B · Q2-35 B · QSQ-I8 D · Q23-59 B · Q21I-6 C · Q23-60 C · Q21I-20 A · Q2-36 B · Q2-37 B · Q2-38 B · Q21I-13 C · Q21I-29 C · QSQ-I6 A · Q2-39 B · Q21I-31 D.

### Drill 10 — Admiralty: all Topics (3.I–3.VII) · 38 questions · 80 minutes

**Questions:** Q3-1, QSQ-A3, QSQ-A6, QSQ-A9, QADM-1, QADM-3, QADM1-1, Q3-2, QSQ-A2, QADM1-2, Q3-3, QADM-8, QADM-4, QSQ-A1, QSQ-A7, QSQ-A10, QADM-2, QSQ-A5, QADM1-M, QADM1-5, QADM1-7, Q3-4, QSQ-A8, Q3-5, Q3-6, Q3-7, Q3-8, Q3-9, QADM-5, Q23-39, QADM1-3, QADM1-6, Q3-10, QSQ-A4, QADM-6, QADM-7, Q23-40, QADM1-4.

**Answer key:** Q3-1 B · QSQ-A3 D · QSQ-A6 C · QSQ-A9 B · QADM-1 d · QADM-3 b · QADM1-1 B · Q3-2 B · QSQ-A2 D · QADM1-2 A · Q3-3 B · QADM-8 d · QADM-4 a · QSQ-A1 C · QSQ-A7 D · QSQ-A10 C · QADM-2 c · QSQ-A5 D · QADM1-M B · QADM1-5 A · QADM1-7 C · Q3-4 B · QSQ-A8 B · Q3-5 B · Q3-6 B · Q3-7 B · Q3-8 D · Q3-9 B · QADM-5 b · Q23-39 A · QADM1-3 D · QADM1-6 C · Q3-10 B · QSQ-A4 A · QADM-6 c · QADM-7 d · Q23-40 C · QADM1-4 A.

### Drill 11 — Mixed mock: all 40 Sample Questions, official key · 40 questions · 80 minutes

**Questions:** QSQ-B1, QSQ-B6, QSQ-B2, QSQ-B10, QSQ-B3, QSQ-B4, QSQ-B8, QSQ-B9, QSQ-B7, QSQ-B5, QSQ-G7, QSQ-G2, QSQ-G10, QSQ-G3, QSQ-G5, QSQ-G8, QSQ-G9, QSQ-G4, QSQ-G6, QSQ-G1, QSQ-I3, QSQ-I7, QSQ-I1, QSQ-I2, QSQ-I4, QSQ-I5, QSQ-I10, QSQ-I9, QSQ-I8, QSQ-I6, QSQ-A3, QSQ-A6, QSQ-A9, QSQ-A2, QSQ-A1, QSQ-A7, QSQ-A10, QSQ-A5, QSQ-A8, QSQ-A4.

**Answer key:** QSQ-B1 A · QSQ-B6 A · QSQ-B2 A · QSQ-B10 A · QSQ-B3 A · QSQ-B4 A · QSQ-B8 D · QSQ-B9 A · QSQ-B7 C · QSQ-B5 B · QSQ-G7 B · QSQ-G2 D · QSQ-G10 D · QSQ-G3 B · QSQ-G5 D · QSQ-G8 B · QSQ-G9 B · QSQ-G4 D · QSQ-G6 D · QSQ-G1 A · QSQ-I3 A · QSQ-I7 D · QSQ-I1 C · QSQ-I2 D · QSQ-I4 D · QSQ-I5 C · QSQ-I10 D · QSQ-I9 C · QSQ-I8 D · QSQ-I6 A · QSQ-A3 D · QSQ-A6 C · QSQ-A9 B · QSQ-A2 D · QSQ-A1 C · QSQ-A7 D · QSQ-A10 C · QSQ-A5 D · QSQ-A8 B · QSQ-A4 A.

### Drill 12 — Mixed mock: the 2023 CCP Paper 1 questions held, in paper order · 51 questions · 105 minutes

**Questions:** Q23-1, Q23-2, Q23-3, Q23-4, Q23-5, Q23-6, Q23-7, Q23-8, Q23-9, Q23-10, Q23-11, Q23-12, Q23-13, Q23-14, Q23-15, Q23-16, Q23-17, Q23-18, Q23-19, Q23-20, Q23-21, Q23-22, Q23-24, Q23-25, Q23-26, Q23-27, Q23-28, Q23-29, Q23-30, Q23-31, Q23-32, Q23-33, Q23-35, Q23-36, Q23-37, Q23-39, Q23-40, Q23-43, Q23-45, Q23-46, Q23-47, Q23-48, Q23-49, Q23-50, Q23-51, Q23-52, Q23-55, Q23-57, Q23-58, Q23-59, Q23-60.

**Answer key:** Q23-1 A · Q23-2 C · Q23-3 C · Q23-4 C · Q23-5 C · Q23-6 D · Q23-7 D · Q23-8 D · Q23-9 B · Q23-10 A · Q23-11 D · Q23-12 C · Q23-13 A · Q23-14 D · Q23-15 D · Q23-16 C · Q23-17 D · Q23-18 B · Q23-19 D · Q23-20 A · Q23-21 C · Q23-22 B · Q23-24 C · Q23-25 C · Q23-26 D · Q23-27 C · Q23-28 C · Q23-29 A · Q23-30 A · Q23-31 A · Q23-32 B · Q23-33 B · Q23-35 D · Q23-36 B · Q23-37 C · Q23-39 A · Q23-40 C · Q23-43 D · Q23-45 B · Q23-46 D · Q23-47 B · Q23-48 D · Q23-49 D · Q23-50 D · Q23-51 C · Q23-52 B · Q23-55 A · Q23-57 A · Q23-58 B · Q23-59 B · Q23-60 C.

### Drill 13 — Insolvency mock: the 2021 INS MCQs held, in paper order · 32 questions · 65 minutes

**Questions:** Q21I-2, Q21I-3, Q21I-4, Q21I-5, Q21I-6, Q21I-7, Q21I-8, Q21I-9, Q21I-10, Q21I-11, Q21I-12, Q21I-13, Q21I-14, Q21I-15, Q21I-16, Q21I-17, Q21I-18, Q21I-19, Q21I-20, Q21I-21, Q21I-22, Q21I-23, Q21I-24, Q21I-25, Q21I-26, Q21I-27, Q21I-28, Q21I-29, Q21I-30, Q21I-31, Q21I-33, Q21I-35.

**Answer key:** Q21I-2 A · Q21I-3 C · Q21I-4 D · Q21I-5 D · Q21I-6 C · Q21I-7 B · Q21I-8 A · Q21I-9 A · Q21I-10 D · Q21I-11 C · Q21I-12 A · Q21I-13 C · Q21I-14 B · Q21I-15 B · Q21I-16 A · Q21I-17 C · Q21I-18 D · Q21I-19 C · Q21I-20 A · Q21I-21 A · Q21I-22 B · Q21I-23 B · Q21I-24 C · Q21I-25 A · Q21I-26 B · Q21I-27 D · Q21I-28 B · Q21I-29 C · Q21I-30 A · Q21I-31 D · Q21I-33 C · Q21I-35 C.

### Drill 14 — Mixed mock: own questions across all four Subjects · 43 questions · 90 minutes

**Questions:** Q0-1, Q0-4, Q0-7, Q0-10, Q0-13, Q0-16, Q0-19, Q0-22, Q0-25, Q0-28, Q0-31, Q0-34, Q0-37, Q1-1, Q1-4, Q1-7, Q1-10, Q1-13, Q1-16, Q1-19, Q1-22, Q1-25, Q1-28, Q1-31, Q1-34, Q2-1, Q2-4, Q2-7, Q2-10, Q2-13, Q2-16, Q2-19, Q2-22, Q2-25, Q2-28, Q2-31, Q2-34, Q2-37, Q3-1, Q3-3, Q3-5, Q3-7, Q3-9.

**Answer key:** Q0-1 D · Q0-4 B · Q0-7 B · Q0-10 B · Q0-13 B · Q0-16 B · Q0-19 D · Q0-22 B · Q0-25 C · Q0-28 B · Q0-31 B · Q0-34 B · Q0-37 B · Q1-1 C · Q1-4 B · Q1-7 B · Q1-10 B · Q1-13 B · Q1-16 B · Q1-19 B · Q1-22 B · Q1-25 B · Q1-28 B · Q1-31 A · Q1-34 B · Q2-1 B · Q2-4 B · Q2-7 B · Q2-10 B · Q2-13 B · Q2-16 B · Q2-19 B · Q2-22 D · Q2-25 B · Q2-28 B · Q2-31 B · Q2-34 B · Q2-37 B · Q3-1 B · Q3-3 B · Q3-5 B · Q3-7 B · Q3-9 B.

### Coverage check

Drills 1–10 together contain all 260 Part 1 questions, and every one of the 196 Sub-points has at least one tagged question, so every Sub-point is drilled at least once.
