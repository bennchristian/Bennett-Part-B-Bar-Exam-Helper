# CLK-M — Cheatsheets

Paper `clk-m`: Contemporary Legal Knowledge & Practice (MCQ), Fri 11 Dec 2026. Subjects
follow `SCHEMA.md`: 0 Data Protection & Cyber Regulation · 1 Law & Technology ·
2 Comparative Laws · 3 Conflict of Laws. Topic headings read `<subject>.<Topic>`.

**How to use in the exam.** Each Topic opens with a question-and-answer cheatsheet that runs
from broad to specific: the question a candidate would ask, then the answer and its limbs or
exceptions. Each line ends with a link such as `0-12`, which goes to the end-point block
`clk-m-0-12` below it. That block holds the full rule, a Rule in full box and the source. If
you know a keyword, search for it: every cheatsheet line, title and Keywords line is text.
Sections are written with a space (`s 48O`), so search for `48O` without the "s" if the
section-form search fails.

The cheatsheet gives short answers only. The rule in full and its sources are in the
end-point blocks, and the *Source note* is for checking only. Source aliases (DP-1, PDPA, LT-4, Cmp-2, CoL-3,
SampleQs, Cyril-Exam …) are defined in `outline.md` → "Source key". Page numbers are PDF
pages, which match the printed slide numbers. Where a secondary source disagrees with the
Course Materials, the block follows the Course Materials and the Source note records it in
a `Conflict:` sentence.

Not covered: topic 0.X (AI regulation), which is Non-Core and has no source; see `coverage.md`.

## 0.I PDPA scope and personal data

- **Is it personal data? (PDPA s 2(1))**
  - Data, true or not, about an individual who can be identified from it alone or with other information the organisation has or is likely to access; facts and opinions → [0-1](#clk-m-0-1)
  - Business contact information not given solely for personal purposes: outside Parts 3–6A → [0-2](#clk-m-0-2)
  - Deceased: dead 10 years or less, only disclosure and s 24 apply; more than 10 years, none; records 100+ years old are out → [0-3](#clk-m-0-3)
- **Who must comply?**
  - Any organisation, including foreign companies and unincorporated associations → [0-5](#clk-m-0-5)
  - Excluded: individual in a personal or domestic capacity, employee in the course of employment, public agency → [0-4](#clk-m-0-4)
  - Data intermediary (DI): owes only protection, retention and telling the organisation of a breach; the organisation keeps everything else → [0-6](#clk-m-0-6)
- **Does a contract, another law or a guideline change things?**
  - A contract is no excuse; other written law prevails where inconsistent; PDPC guidelines do not bind → [0-7](#clk-m-0-7)

### clk-m-0-1 — What counts as personal data
*Keywords: personal data, identifiable individual, true or not, opinion, PDPA s 2(1)*

**End point:** Personal data is data, whether true or not, about an individual who can be identified from that data alone or with other information the organisation has or is likely to have access to; it covers facts and opinions.

*Source note: PDPA p11 (s 2(1)); DP-1 p17; SampleQs p89 Q1, key p130*

### clk-m-0-2 — Business contact information
*Keywords: business contact information, BCI, PDPA s 4(5)*

**End point:** Business contact information (name, title, business phone, address, email) not provided solely for personal purposes falls outside Parts 3 to 6A.

*Source note: PDPA p8 (s 2(1)), p14 (s 4(5))*

### clk-m-0-3 — Deceased individuals
*Keywords: deceased individual, 10 years, 100 years, PDPA s 4(4)*

**End point:** For a person dead 10 years or less, only the disclosure provisions and s 24 (protection) apply; dead more than 10 years, the Act does not apply; records 100 years or older are out of scope.

*Source note: PDPA p10 (s 2(1) individual), p14 (s 4(4))*

### clk-m-0-4 — Excluded persons — domestic, employee, public agency
*Keywords: personal or domestic capacity, employee, course of employment, public agency, Reed v Bellingham, PDPA s 4(1)*

**End point:** Parts 3 to 6B impose no obligation on an individual acting in a personal or domestic capacity, an employee acting in the course of employment, or a public agency; an employee relying on the exclusion must prove both limbs (Reed).

*Source note: PDPA p13 (s 4(1)); Reed p21*

### clk-m-0-5 — Organisations bound, including foreign ones
*Keywords: organisation, foreign company, partnership, unincorporated association, PDPA s 2(1)*

**End point:** An "organisation" is any individual, company, association or body of persons, whether or not formed or resident in Singapore, so foreign companies and unincorporated associations are bound.

*Source note: PDPA p11 (s 2(1)); SampleQs p91 Q7, key p130*

### clk-m-0-6 — Data intermediaries — what a DI owes
*Keywords: data intermediary, DI, DI obligations, data intermediary obligations, processor, processing on behalf, written contract, data controller, protection, retention, DI notifies the organisation, PDPA s 4(2), s 4(3), s 24, s 25, s 26C(3)(a), s 26E*

**End point:** A data intermediary (DI) processing personal data for another organisation under a written contract owes only three things. It must protect the data (s 24), stop retaining it once it is no longer needed (s 25), and tell the organisation, not the PDPC, of a data breach without undue delay (s 26C(3)(a)). The organisation keeps every obligation as if it processed the data itself (s 4(3)), so it assesses the breach and notifies the PDPC.

> **PDPA s 4(2)–(3): what a data intermediary owes**
> - Applies to a DI processing personal data on behalf of and for the purposes of another organisation, under a contract evidenced or made in writing (s 4(2)).
> - The DI owes only:
>   - the Protection Obligation (s 24);
>   - the Retention Limitation Obligation (s 25);
>   - on reason to believe a data breach has occurred, notifying the organisation it processes for, without undue delay (s 26C(3)(a));
>   - if it processes for a public agency, notifying that public agency instead, without undue delay (s 26E).
> - The DI does not owe:
>   - accountability (Part 3);
>   - consent, purpose limitation or notification (Part 4);
>   - access or correction (Part 5);
>   - accuracy (s 23) or transfer limitation (s 26);
>   - assessing the breach or notifying the PDPC or individuals (ss 26C–26D, apart from s 26C(3)(a));
>   - portability (Part 6B).
> - The organisation has the same obligations for data its DI processes as if it processed the data itself (s 4(3)). It assesses the breach (clk-m-0-43) and notifies the PDPC (clk-m-0-44).
> - Appointing a DI does not pass on responsibility. In SingHealth, both SingHealth and its DI, IHiS, were fined (clk-m-0-39).

*Source note: PDPA p12-13 (s 4(2)-(3)), p35-37 (ss 26C(3), 26E); DP-1 p18; Drill 1 DP3. Conflict: DP-1 p18 also lists Part 6B; PDPA s 4(2) excludes it, and the statute is followed.*

### clk-m-0-7 — Contracts, other laws and PDPC guidelines
*Keywords: contractual obligation, other written law, inconsistency, advisory guidelines, PDPA s 4(6), s 49*

**End point:** A contractual obligation is no excuse for breaching the PDPA; other written law prevails where inconsistent; PDPC advisory guidelines are not binding.

*Source note: PDPA p14 (s 4(6)), p78 (s 49); DP-1 p13*

## 0.II Consent and legal bases

- **Is the purpose sending marketing messages?**
  - Consent is needed; legitimate interests, business improvement and deemed consent by notification cannot be used → [0-8](#clk-m-0-8)
- **Is there valid consent?**
  - Express consent: purposes notified first; invalid if beyond what is reasonable or obtained by deception → [0-9](#clk-m-0-9)
  - Deemed by conduct: data volunteered for a purpose → [0-10](#clk-m-0-10)
  - Deemed by contractual necessity: reasonably necessary to conclude or perform a contract → [0-11](#clk-m-0-11)
  - Deemed by notification: assess no adverse effect, notify, give a reasonable opt-out period; not for marketing → [0-12](#clk-m-0-12)
  - Consent withdrawn: reasonable notice; organisation must explain the consequences and stop → [0-13](#clk-m-0-13)
  - Notifying purposes alone is not a legal basis → [0-14](#clk-m-0-14)
- **No consent: which exception?**
  - Individual's vital interests, emergency, next of kin → [0-15](#clk-m-0-15)
  - Publicly available, national interest, news, artistic, archival → [0-16](#clk-m-0-16)
  - Legitimate interests: must outweigh adverse effects, after an assessment; never for marketing → [0-17](#clk-m-0-17)
  - Business asset transaction (merger, acquisition) → [0-18](#clk-m-0-18)
  - Business improvement within related corporations; not for marketing → [0-19](#clk-m-0-19)
  - Research: public benefit, identifiable form needed, no decisions about the individual → [0-20](#clk-m-0-20)

### clk-m-0-8 — Marketing messages
*Keywords: marketing, direct marketing, legitimate interests, business improvement, deemed consent by notification, PDPR reg 13*

**End point:** Legitimate interests, business improvement and deemed consent by notification cannot be used to send marketing messages, so consent (or another basis) is needed; it is false that marketing never needs consent.

*Source note: PDPA p98 (First Sch Pt 3 para 1(4)), p103-105 (Pt 5); PDPR p15 (reg 13); SampleQs p90 Q5, key p130*

### clk-m-0-9 — Valid consent
*Keywords: consent, validity, false or misleading, beyond reasonable, PDPA s 13, s 14*

**End point:** Consent is valid only if the s 20 purposes were notified first; it is invalid if required beyond what is reasonable to supply the product or service or obtained by deceptive practices, and may be given by an authorised person.

*Source note: PDPA p20-21 (ss 13-14)*

### clk-m-0-10 — Deemed consent by conduct
*Keywords: deemed consent, conduct, voluntarily provides, onward disclosure, PDPA s 15(1), s 15(2)*

**End point:** Consent is deemed where an individual voluntarily provides data for a purpose and it is reasonable that they would; it extends to onward disclosure for that purpose.

*Source note: PDPA p21 (s 15(1)-(2))*

### clk-m-0-11 — Deemed consent by contractual necessity
*Keywords: deemed consent, contractual necessity, conclusion of contract, performance of contract, PDPA s 15(3)-(8)*

**End point:** Data given with a view to a contract is deemed consented to for disclosure and use reasonably necessary to conclude or perform it, including onward to third parties.

*Source note: PDPA p21-23 (s 15(3)-(8))*

### clk-m-0-12 — Deemed consent by notification
*Keywords: deemed consent by notification, opt-out, adverse effect assessment, PDPA s 15A, PDPR reg 14*

**End point:** Before relying on it, the organisation must assess that there is no likely adverse effect, notify the individual of the purpose with a reasonable opt-out period, and keep the assessment; not available for marketing messages.

*Source note: PDPA p24-25 (s 15A); PDPR p15-16 (regs 13-14)*

### clk-m-0-13 — Withdrawal of consent
*Keywords: withdraw consent, reasonable notice, consequences, PDPA s 16*

**End point:** An individual may withdraw consent on reasonable notice; the organisation must explain the likely consequences, cannot prohibit withdrawal, and must stop (and make its intermediaries and agents stop) unless the law requires otherwise.

*Source note: PDPA p25-26 (s 16)*

### clk-m-0-14 — Notification of purposes is not a legal basis
*Keywords: notification of purposes, legal basis, PDPA s 20*

**End point:** Notifying purposes is a separate obligation, not a legal basis for collection, use or disclosure.

*Source note: SampleQs p92 Q8, key p130; DP-1 p26*

### clk-m-0-15 — Vital interests
*Keywords: vital interests, emergency, next of kin, clearly in the individual's interests, First Schedule Part 1*

**End point:** No consent is needed where processing is clearly in the individual's interests and consent cannot be obtained in time or would not reasonably be withheld (notify as soon as practicable), in emergencies threatening life or health, or to contact next of kin.

*Source note: PDPA p95-96 (First Sch Pt 1)*

### clk-m-0-16 — Matters affecting the public
*Keywords: publicly available, national interest, news activity, artistic, archival, historical, First Schedule Part 2*

**End point:** Publicly available data, the national interest, solely artistic or literary purposes, archival or historical purposes (unless too sensitive) and news activity by a news organisation are exceptions.

*Source note: PDPA p96-97 (First Sch Pt 2)*

### clk-m-0-17 — Legitimate interests — must outweigh adverse effects; never for marketing
*Keywords: legitimate interests, legitimate interests exception, outweigh, adverse effect, balancing, assessment, mitigation, marketing carve-out, not for marketing, applicable purpose, investigation, debt recovery, legal services, evaluative purpose, credit bureau, First Schedule Part 3, para 1(4), PDPR reg 15*

**End point:** No consent is needed where the organisation's (or another person's) legitimate interests outweigh any adverse effect on the individual. The organisation must assess this beforehand, mitigate the adverse effects, and give the individual reasonable access to information about it. The exception never covers sending marketing messages, which need consent or another basis (para 1(4); clk-m-0-8).

> **PDPA First Schedule Part 3 para 1: the legitimate interests exception**
> - Both must hold (para 1(1)):
>   - (a) the collection, use or disclosure is in the legitimate interests of the organisation or another person; and
>   - (b) those legitimate interests outweigh any adverse effect on the individual.
> - Before relying on it, the organisation must (para 1(2)):
>   - (a) assess, before collecting, using or disclosing, whether para 1(1) is satisfied; and
>   - (b) give the individual reasonable access to information about the collection, use or disclosure.
> - In that assessment it must (para 1(3)):
>   - (a) identify any likely adverse effect on the individual;
>   - (b) identify and implement reasonable measures to eliminate the adverse effect, reduce its likelihood, or mitigate it;
>   - (c) comply with any prescribed requirements (PDPR reg 15).
> - **Not for marketing.** Para 1(1) does not apply to sending a message for an "applicable purpose" (s 37(6), Tenth Schedule), i.e. marketing (para 1(4)).
> - The other Part 3 grounds need no balancing:
>   - evaluative purposes (para 2);
>   - investigations or proceedings (para 3);
>   - recovering or paying a debt (para 4);
>   - legal services (para 5);
>   - credit bureau reports (para 6).

*Source note: PDPA p98-100 (First Sch Pt 3 paras 1-6), p42 (s 37(6)); PDPR p16-17 (reg 15); Drill 1 DP5; SampleQs p90 Q5, key p130*

### clk-m-0-18 — Business asset transactions
*Keywords: business asset transaction, merger, acquisition, First Schedule Part 4*

**End point:** Data may be processed without consent in a business asset transaction, subject to conditions such as limiting it to necessary data and destroying or returning it if the deal fails.

*Source note: PDPA p100-102 (First Sch Pt 4)*

### clk-m-0-19 — Business improvement
*Keywords: business improvement, related corporation, personalise, First Schedule Part 5, Second Schedule Part 2 Division 2*

**End point:** Data may be used, or shared within related corporations, without consent to improve goods, services or methods, or to understand or personalise for customers, if identifiable form is needed and a reasonable person would find it appropriate; not for marketing.

*Source note: PDPA p103-105 (First Sch Pt 5), p106 (Second Sch Pt 2 Div 2)*

### clk-m-0-20 — Research
*Keywords: research, public benefit, impracticable to seek consent, Second Schedule*

**End point:** Use for research needs identifiable form to be necessary, a clear public benefit, no decisions about the individual, and no identification in published results; disclosure for research also needs consent to be impracticable.

*Source note: PDPA p106-108 (Second Sch)*

## 0.III Other organisational obligations

- **Governance: what must every organisation have? (Accountability, ss 11–12)**
  - A DPO with published contact details, policies and practices, and a complaints process; a data inventory or DPIA is not required → [0-21](#clk-m-0-21)
  - Not actionable under s 48O → [0-33](#clk-m-0-33)
- **Collection and purpose**
  - Purpose limitation: only purposes a reasonable person would consider appropriate and that were notified → [0-22](#clk-m-0-22)
  - Notification: tell purposes on or before collection and before any new use → [0-23](#clk-m-0-23)
- **Holding and sending data**
  - Accuracy: only if the data is used for a decision about the individual or disclosed → [0-24](#clk-m-0-24)
  - Retention: stop or anonymise once the purpose and legal or business need have both gone → [0-25](#clk-m-0-25)
  - Transfer overseas: comparable-standard obligations (law, contract, BCRs, CBPR), or consent or contractual necessity → [0-26](#clk-m-0-26)
  - Marketing calls or texts: Do Not Call register checks (non-core) → [0-27](#clk-m-0-27)

### clk-m-0-21 — Accountability obligations
*Keywords: accountability, data protection officer, DPO, policies and practices, complaints process, data inventory, DPIA, PDPA s 11, s 12*

**End point:** An organisation must designate a DPO and publish their business contact details, develop and communicate policies and practices, set up a complaints process, and make information available on request; a data inventory or DPIA is not an express requirement.

*Source note: PDPA p19-20 (ss 11-12); SampleQs p90 Q4, key p130; DP-1 p28 (lists a data inventory only as a measure that may be taken)*

### clk-m-0-22 — Purpose limitation
*Keywords: purpose limitation, reasonable person, appropriate, PDPA s 18*

**End point:** Data may be collected, used or disclosed only for purposes a reasonable person would consider appropriate in the circumstances and that the individual has been informed of.

*Source note: PDPA p27 (s 18); DP-1 p26*

### clk-m-0-23 — Notification obligation
*Keywords: notification, purposes, before collection, new purpose, PDPA s 20*

**End point:** The organisation must tell the individual its purposes on or before collection and before any new use, and give a contact on request; this is not needed for deemed consent or s 17 exceptions, but is still needed for employment purposes.

*Source note: PDPA p27-29 (s 20)*

### clk-m-0-24 — Accuracy obligation
*Keywords: accuracy, complete, decision affecting the individual, PDPA s 23*

**End point:** Reasonable effort to ensure accuracy and completeness is required only if the data is likely to be used to make a decision affecting the individual or disclosed to another organisation.

*Source note: PDPA p32-33 (s 23)*

### clk-m-0-25 — Retention limitation
*Keywords: retention, cease to retain, anonymise, legal or business purposes, PDPA s 25*

**End point:** An organisation must stop retaining data, or anonymise it, once both the purpose is no longer served and retention is no longer necessary for legal or business purposes.

*Source note: PDPA p33 (s 25)*

### clk-m-0-26 — Transfer limitation
*Keywords: transfer limitation, overseas transfer, comparable standard, contract, binding corporate rules, APEC CBPR, PDPA s 26, PDPR reg 10*

**End point:** Data may go overseas only if the recipient is bound by legally enforceable obligations of a comparable standard (law, contract, binding corporate rules, CBPR or PRP certification), or on valid consent, contractual necessity or in transit.

*Source note: PDPA p33-34 (s 26); PDPR p10-14 (Part 3, regs 10-12). Conflict: Cyril-Exam DP §1.2.2 cites "s 10 PDPR"; it is reg 10.*

### clk-m-0-27 — Do Not Call (non-core)
*Keywords: Do Not Call, DNC register, specified message, calling line identity, PDPA s 43, s 44, s 45*

**End point:** Before sending specified marketing messages the sender must check the DNC register (s 43), identify itself with contact details valid for 30 days (s 44), and not conceal its calling line identity (s 45); Part 9 is outside the core reading list.

*Source note: DP-1 p28; PDPA p44-47 (ss 43-45); DP-Plan p5*

## 0.IV Individual rights and private action

- **What can the individual ask for?**
  - Access: data and how it was used or disclosed in the past year; 30 days or a written timeline; a reasonable fee → [0-28](#clk-m-0-28)
  - Access refused: Fifth Schedule items, safety, another individual's data → [0-29](#clk-m-0-29)
  - Correction: correct or annotate; tell recipients from the past year; no fee → [0-30](#clk-m-0-30)
  - Deletion: no right to erasure; withdraw consent, and retention limitation applies → [0-31](#clk-m-0-31)
  - Portability: legislated, not in force → [0-32](#clk-m-0-32)
- **Can the individual sue? (s48O / s 48O)**
  - Which breaches: Parts 4, 5, 6, 6A, 6B and Do Not Call; not Part 3 (Accountability, ss 11–12); wait for any PDPC decision to be final → [0-33](#clk-m-0-33)
  - Is emotional distress loss? Yes. Is loss of control of data loss? No (*Reed v Bellingham*) → [0-34](#clk-m-0-34)

### clk-m-0-28 — Access requests — duty and timing
*Keywords: access request, past year, 30 days, fee, written estimate, PDPA s 21, PDPR reg 5, reg 7*

**End point:** On request the organisation must provide the data and how it was used or disclosed in the past year as soon as reasonably possible; if it cannot respond within 30 days it must say in writing when it will, and it may charge a reasonable fee after a written estimate.

*Source note: PDPA p29-31 (s 21); PDPR p5 (reg 5), p6-8 (reg 7)*

### clk-m-0-29 — Access requests — refusal grounds
*Keywords: Fifth Schedule, opinion data, examination, privileged, confidential commercial information, safety, another individual, PDPA s 21(3), s 21(4), s 22A*

**End point:** Fifth Schedule items (e.g. evaluative opinions, exam scripts, privileged material, confidential commercial information) need not be provided; data must not be provided if it threatens safety or health, causes grave harm, reveals another individual's data or harms the national interest; keep a copy after refusing.

*Source note: PDPA p29-30 (s 21(3)-(4)), p32 (s 22A), p108-109 (Fifth Sch)*

### clk-m-0-30 — Correction requests
*Keywords: correction, error or omission, annotate, opinion, no fee, PDPA s 22*

**End point:** The organisation must correct an error or omission and send the correction to organisations it disclosed to in the past year, or annotate the data if it decides not to; opinions need not be altered, and no fee may be charged.

*Source note: PDPA p31-32 (s 22), p109-110 (Sixth Sch); PDPR p6-8 (reg 7)*

### clk-m-0-31 — No right to erasure
*Keywords: erasure, deletion, right to be forgotten, withdraw consent, retention*

**End point:** The PDPA gives no right to deletion; the individual can withdraw consent (s 16) and the organisation must stop retaining data under s 25.

*Source note: DP-1 p31-32; SampleQs p92 Q9, key p130. Conflict: Cyril-Exam DP §1.3 and Nic-DP p4 list a right to erasure; the module and official key say there is none.*

### clk-m-0-32 — Data portability
*Keywords: data portability, porting, not in force*

**End point:** Data portability is legislated but not yet in force.

*Source note: DP-1 p32*

### clk-m-0-33 — Private action under s 48O — which breaches
*Keywords: s48O, s 48O, section 48O, right of private action, private action, sue the organisation, civil action, Part 4, Part 5, Part 6, Part 6A, Part 6B, not Part 3, Accountability Obligation, ss 11-12, Do Not Call, injunction, declaration, damages, PDPC decision final*

**End point:** Under s 48O, a person who suffers loss or damage directly from an organisation's breach of Parts 4, 5, 6, 6A or 6B (or from a person's breach of the Do Not Call provisions or s 48B(1)) may sue for an injunction, declaration or damages. Part 3, the Accountability Obligation (ss 11–12), is not listed, so a s 48O claim cannot rest on a breach of the accountability obligations. If the PDPC has decided on the breach, the claim must wait until that decision is final.

> **PDPA s 48O: right of private action**
> - Who can sue (s 48O(1)): a person who suffers loss or damage directly as a result of a contravention —
>   - (a) by an organisation of any provision of Part 4 (collection, use, disclosure), 5 (access, correction), 6 (care of data), 6A (data breach notification) or 6B (portability); or
>   - (b) by a person of Division 3 of Part 9 (Do Not Call: specified messages to Singapore numbers) or s 48B(1).
> - Not covered: Part 3, ss 11–12, the Accountability Obligation (DPO, policies, complaints process).
> - Timing (s 48O(2)): if the PDPC has made a decision on the contravention, no action until the decision is final, with no further right of appeal.
> - Relief (s 48O(3)):
>   - (a) an injunction or declaration;
>   - (b) damages;
>   - (c) any other relief the court thinks fit.
> - What counts as "loss or damage", and whether emotional distress does: clk-m-0-34.

*Source note: PDPA p73 (s 48O), p19-20 (ss 11-12, Part 3), p44 (Part 9 Div 3); Drill 1 DP8*

### clk-m-0-34 — Private action — is emotional distress loss? (Reed v Bellingham)
*Keywords: Reed v Bellingham, s48O, s 48O, loss or damage, emotional distress, is emotional distress loss, loss of control, loss of control of personal data, anxiety, ordinary vicissitudes of life, s 32(1)*

**End point:** Yes: emotional distress is "loss or damage" under s 48O (*Reed v Bellingham* [107]). Loss of control of personal data on its own is not ([108]). Every breach of Parts 4–6 involves some loss of control, so counting it would make the "loss or damage" requirement meaningless ([109]–[110]). The claimant must prove they actually suffered distress, and ordinary negative emotions that are part of life do not count ([114], [116]).

> **Reed v Bellingham [2022] SGCA 60: "loss or damage" under the private action (then s 32(1), now s 48O)**
> - Emotional distress is "loss or damage" ([107]).
> - Loss of control of personal data, by itself, is not ([108]–[110]).
> - Whether the claimant suffered distress ([114]):
>   - the test is subjective: did this claimant suffer it?
>   - how a reasonable person would react is only an evidential tool;
>   - objective signs of distress weigh more than bare assertions in an affidavit.
> - Non-exhaustive factors ([115]):
>   - (a) the nature of the personal data, e.g. financial data is sensitive;
>   - (b) the nature of the breach;
>   - (c) the nature of the defendant's conduct;
>   - (d) the risk of future breaches causing distress;
>   - (e) the actual impact of the breach on the claimant.
> - Negative emotions that are part of the ordinary vicissitudes of life are not emotional distress ([116]).
> - Applied to DP8: anxiety over loss of control, pleaded on a breach of ss 11–12, fails twice over. Part 3 is outside s 48O (clk-m-0-33), and loss of control is not loss.

*Source note: Reed p47-51 ([107]-[116]); PDPA p73 (s 48O, inserted by Act 40 of 2020, replacing s 32); Drill 1 DP8*

## 0.V PDPC enforcement and offences

- **What can the PDPC do to an organisation?**
  - Investigate, refer to mediation, give directions, impose penalties, accept voluntary undertakings → [0-35](#clk-m-0-35)
  - Maximum financial penalty: 10% of Singapore turnover if over $10m, otherwise $1m; intentional or negligent breaches only → [0-36](#clk-m-0-36)
  - Challenge: reconsideration, then Appeal Panel, then High Court → [0-37](#clk-m-0-37)
- **What offences does an individual commit? (Part 9B)**
  - Unauthorised disclosure, improper use, re-identification; $5,000 and/or 2 years → [0-38](#clk-m-0-38)
- **Case example**
  - SingHealth fined $250,000 and its DI IHiS $750,000; responsibility is not delegated → [0-39](#clk-m-0-39)
- **Who is the PDPC and what does it do? (Part 2)**
  - IMDA is designated as the PDPC (s 5); functions (s 6); advisory committees (s 7); Commissioner and delegation (s 8); PDPC officers prosecute with the PP's authorisation (s 9); cooperation agreements with other regulators (s 10) → [0-76](#clk-m-0-76)
- **How does the PDPC give a direction or penalty, and how is it enforced?**
  - Written notice first; at least 14 days to make representations before a penalty; takes effect on service; pay within at least 28 days (s 48K) → [0-77](#clk-m-0-77)
  - Register the direction or penalty notice in a District Court, then enforce it like a court order (s 48M) → [0-77](#clk-m-0-77)
- **Part 10 offences: what else is a crime under the PDPA?**
  - Access, correction or porting request about another person without authority; destroying records to evade a request; obstructing the PDPC; false statements to it (s 51) → [0-78](#clk-m-0-78)
  - No penalty stated: up to $10,000 and/or 3 years (s 56); District Court jurisdiction (s 54); composition (s 55) → [0-78](#clk-m-0-78)
- **Is the employer or a director liable for what an employee did?**
  - The employee's act in the course of employment is the employer's act too, with or without its knowledge (s 53(1)); for an offence, the employer has a "practicable steps" defence (s 53(2)) → [0-79](#clk-m-0-79)
  - Officers who consented, connived or failed to take reasonable steps are guilty of the company's offence (s 52; s 52A for partnerships and associations) → [0-79](#clk-m-0-79)
- **Re-identifying anonymised data: is testing a defence?**
  - Yes, if the accused reasonably believed it was for a specified purpose (Eleventh Schedule: testing anonymisation or the security of anonymised data) and notified the PDPC or the organisation as soon as practicable (s 48F(2)(c)) → [0-80](#clk-m-0-80)
- **How does the PDPC choose its enforcement outcome? (Guide on Active Enforcement)**
  - Suspend or discontinue; voluntary undertaking; breach findings (no breach, warning, directions, penalty); expedited decision procedure on an upfront admission → [0-81](#clk-m-0-81)
- **Optional reading: decisions**
  - Spize Concepts: no DPO or policies, overseas vendor with no transfer safeguards; $20,000 → [0-82](#clk-m-0-82)
  - RedMart [2023]: NRIC photos of suppliers; no valid consent, but legitimate interests later met → [0-83](#clk-m-0-83)

### clk-m-0-35 — PDPC investigation and enforcement powers
*Keywords: PDPC, investigation, mediation, directions, voluntary undertaking, PDPA s 50, s 48G, s 48H, s 48I, s 48L*

**End point:** The PDPC investigates under s 50 (and may suspend or discontinue it, e.g. on settlement or an accepted undertaking) and may refer to mediation, review access or correction responses, issue directions, impose penalties and accept voluntary undertakings.

*Source note: PDPA p61-70 (ss 48G-48L), p77 (s 50); DP-1 p35*

### clk-m-0-36 — Financial penalty cap
*Keywords: financial penalty, 10% of turnover, $1 million, intentional or negligent, PDPA s 48J*

**End point:** The maximum is 10% of annual Singapore turnover if turnover exceeds $10 million, otherwise $1 million, and only for intentional or negligent breaches that are not themselves offences.

*Source note: PDPA p64-65 (s 48J(3)); DP-1 p35. Conflict: DP-1 p35 and Cyril-Exam DP §1.4 say "10% or $1 million, whichever is higher"; same result, statute wording followed.*

### clk-m-0-37 — Reconsideration and appeals
*Keywords: reconsideration, Data Protection Appeal Panel, Appeal Committee, High Court, PDPA s 48N, s 48Q, s 48R*

**End point:** A PDPC decision may be reconsidered (s 48N), then appealed to the Data Protection Appeal Panel (s 48Q) and on to the High Court (s 48R).

*Source note: PDPA p71-75 (ss 48N-48R)*

### clk-m-0-38 — Offences by individuals (Part 9B)
*Keywords: unauthorised disclosure, improper use, re-identification, anonymised, $5,000, 2 years, PDPA s 48D, s 48E, s 48F*

**End point:** An individual commits an offence by knowing or reckless unauthorised disclosure (s 48D), improper use for gain or to cause harm or loss (s 48E), or unauthorised re-identification of anonymised data (s 48F); fine up to $5,000 and/or up to 2 years, with defences including prior public availability, legal permission and consent.

*Source note: PDPA p54-61 (ss 48C-48F); PDPR p17 (regs 15A-15B)*

### clk-m-0-39 — SingHealth case study
*Keywords: SingHealth, IHiS, cyber attack, $250,000, $750,000, data intermediary*

**End point:** SingHealth was fined $250,000 and its data intermediary IHiS $750,000 after 1.5 million patients' data was taken; the controller's protection duty is not delegated away by using an intermediary.

*Source note: SingH p7, p49; Nic-DP p7-8*

### clk-m-0-76 — PDPC and administration (PDPA Part 2)
*Keywords: Personal Data Protection Commission, PDPC, IMDA, Info-communications Media Development Authority, designated, functions of the Commission, advisory committee, Commissioner for Personal Data Protection, delegation, conduct of proceedings, cooperation agreement, foreign data protection body, PDPA s 5, s 6, s 7, s 8, s 9, s 10*

**End point:** IMDA is designated as the PDPC, which administers the PDPA (s 5). Its functions include promoting awareness, advising the Government, representing Singapore internationally, and administering and enforcing the Act (s 6). It may appoint a Commissioner and other officers and delegate to them (s 8), conduct prosecutions with the Public Prosecutor's authorisation (s 9), and make cooperation agreements with other regulators (s 10).

> **PDPA Part 2**
> - s 5: IMDA is designated as the PDPC (s 5(1)); the PDPC administers the Act (s 5(2)).
> - s 6: functions, including:
>   - (a) promote awareness of data protection;
>   - (b) provide consultancy and advisory services;
>   - (c) advise the Government;
>   - (d) represent the Government internationally;
>   - (e) research and education;
>   - (f) technical cooperation with foreign data protection authorities;
>   - (g) administer and enforce the Act.
> - s 7: the Minister may appoint advisory committees; the PDPC may consult them but is not bound.
> - s 8: the PDPC may appoint the Commissioner, Deputy and Assistant Commissioners and inspectors. A delegated function is exercised in the Commissioner's name, and the PDPC may not exercise it while the delegation is in force (s 8(2)). An authorised officer must produce their authority on demand (s 8(3)).
> - s 9: an authorised officer may conduct proceedings for a PDPA offence with the Public Prosecutor's authorisation; the PDPC's legal counsel may appear in civil proceedings.
> - s 10: cooperation agreements with other regulators to share information, assist each other and avoid duplication. Information goes to a foreign data protection body only against its written undertaking on confidentiality (s 10(3)).

*Source note: PDPA p14-17 (ss 5-10); DP-Plan p5 (Part 2 is core reading).*

### clk-m-0-77 — Directions and penalties: procedure and enforcement (ss 48K, 48M)
*Keywords: written notice, proposed direction, preliminary decision, written representations, 14 days, 28 days, instalments, interest, takes effect on service, registration in District Court, enforce direction, enforce financial penalty, PDPA s 48K, s 48M*

**End point:** Before giving a direction or imposing a financial penalty, the PDPC must give written notice of the proposed action and allow written representations; for a penalty the window is at least 14 days (s 48K(1)-(2)). The decision takes effect only when served (s 48K(7)), and a penalty is payable by a date at least 28 days after the notice (s 48K(8)). To enforce a direction or penalty notice, the PDPC registers it in a District Court, after which it is enforceable as a District Court order (s 48M).

> **PDPA s 48K: procedure**
> - (1) Written notice first, stating:
>   - (a) the intended action under s 48I or s 48J(1);
>   - (b) the proposed direction;
>   - (c) each instance of non-compliance or the reasons;
>   - (d) the time for written representations.
> - (2) Penalty: at least 14 days after service for representations. (3) Extension on written application, for exceptional circumstances.
> - (4) Decide after considering representations, or when time expires with none.
> - (5) No notice needed if the organisation or person has died, is bankrupt or has ceased to exist.
> - (6) Notice of the decision goes to the organisation and to any complainant; (7) it takes effect only on service on the organisation.
> - (8) Penalty due by a date not earlier than 28 days after the notice; (9) time may be extended or instalments allowed; (10) interest capped at the Rules of Court judgment-debt rate.
>
> **PDPA s 48M: enforcement**
> - (1)-(2) The PDPC may apply to register in a District Court a direction under s 48H(2), 48I or 48L(4), or a written notice for a financial penalty (and interest).
> - (3) From registration it has the same force as a District Court order.

*Source note: PDPA p67-70 (ss 48K, 48M). Reconsideration and appeals: clk-m-0-37.*

### clk-m-0-78 — Part 10 offences and penalties (ss 51, 54-56)
*Keywords: offence, access request without authority, correction request without authority, data porting request without authority, evade a request, destroy records, falsify, obstruct the Commission, refuse to provide information, false or misleading statement, general penalty, $10,000, 3 years, District Court jurisdiction, composition, PDPA s 51, s 54, s 55, s 56*

**End point:** Section 51 makes it an offence to make an access, correction or porting request about someone else without their authority, to dispose of or falsify records to evade an access or correction request, to obstruct the PDPC, to refuse without reasonable excuse to give it information or attend, or to give it false or misleading information. Where no penalty is stated, the general penalty is a fine up to $10,000 and/or up to 3 years' imprisonment (s 56). These are distinct from the Part 9B offences by individuals (clk-m-0-38).

> **PDPA s 51 and Part 10 general provisions**
> - s 51(1)-(2): requests without the other individual's authority, max $5,000 and/or 12 months:
>   - (a) access request (s 21(1));
>   - (b) correction request (s 22(1));
>   - (c) data porting request (s 26H(1)), except an individual porting their own user activity or user-provided data that includes another person's data (s 51(1A)).
> - s 51(3) offences by an organisation or person:
>   - (a) with intent to evade an access or correction request, disposing of, altering, falsifying, concealing or destroying a record: individual $5,000 and/or 12 months; otherwise $50,000 (s 51(4));
>   - (b) obstructing the PDPC, an inspector or authorised officer; (c) false or misleading statement or information: individual $10,000 and/or 12 months; otherwise $100,000 (s 51(5));
>   - (ba) refusing without reasonable excuse to provide information or documents; (bb) refusing to attend: individual $5,000 and/or 6 months; otherwise $10,000 (s 51(6)).
> - s 54: a District Court may try any PDPA offence and impose the full penalty.
> - s 55: the PDPC may compound prescribed offences for up to the lower of half the maximum fine or $5,000 (Part 9 offences: up to $1,000).
> - s 56: general penalty where none is stated: fine up to $10,000 and/or up to 3 years; continuing offence, up to $1,000 a day.

*Source note: PDPA p78-80 (s 51), p85-86 (ss 54-56); DP-Plan p5 (Part 10 is core reading).*

### clk-m-0-79 — Corporate officers and employer liability (ss 52, 52A, 53)
*Keywords: employer liable for employee, vicarious liability, course of employment, with or without knowledge or approval, practicable steps defence, officer of the corporation, director, consented, connived, knowingly concerned, failed to take reasonable steps, state of mind of a corporation, partnership, unincorporated association, PDPA s 52, s 52A, s 53*

**End point:** Anything an employee does in the course of employment is treated, for the PDPA, as done by the employer as well, whether or not the employer knew or approved (s 53(1)). For an offence, the employer has a defence if it proves it took such steps as were practicable to prevent the conduct (s 53(2)). When a corporation commits an offence, an officer or manager who consented, connived, was knowingly concerned, or knew or ought to have known and failed to take all reasonable steps to stop it, is guilty of the same offence (s 52(2)).

> **PDPA ss 52-53**
> - s 52(1): a corporation's state of mind is shown by an officer, employee or agent acting within actual or apparent authority with that state of mind.
> - s 52(2): an officer, or an individual in management able to influence the conduct, who:
>   - (i) consented or connived, or conspired, to effect the offence;
>   - (ii) was knowingly concerned in or party to it; or
>   - (iii) knew or ought reasonably to have known it would be or was being committed and failed to take all reasonable steps to prevent or stop it,
> - is guilty of the same offence. The officer may rely on the corporation's defences (s 52(3)); the corporation's own liability is unaffected, and s 52(2) applies whether or not it is convicted (s 52(5)).
> - s 52A: the same rules for unincorporated associations and partnerships (officers, committee members, partners).
> - s 53(1): an act or conduct of an employee in the course of employment is treated as done by the employer as well as the employee, whether or not with the employer's knowledge or approval.
> - s 53(2): in proceedings for an offence, the employer's defence is to prove it took such steps as were practicable to prevent the employee doing that act, or acts of that description.
> - Contrast the employee's own position: an employee acting in the course of employment is not an "organisation" bound by Parts 3-6 (s 4(1)(b); clk-m-0-4).

*Source note: PDPA p80-85 (ss 52, 52A, 53); DP-Plan p5.*

### clk-m-0-80 — Re-identification defence: specified purposes (s 48F(2)(c), Eleventh Schedule)
*Keywords: re-identification, anonymised information, specified purpose, Eleventh Schedule, testing anonymisation, testing integrity and confidentiality, security testing, notify the Commission, defence, balance of probabilities, PDPA s 48F*

**End point:** Unauthorised re-identification of anonymised information is an offence (s 48F(1); clk-m-0-38). It is a defence, proved on a balance of probabilities, that the accused reasonably believed the re-identification was for a specified purpose and notified the PDPC or the organisation as soon as practicable (s 48F(2)(c)). The specified purposes in the Eleventh Schedule are all about testing anonymisation and the security of anonymised information.

> **PDPA s 48F(2) defences and the Eleventh Schedule**
> - s 48F(2), any of:
>   - (a) the identity information was publicly available (and, if only because of an applicable contravention, the accused did not know and was not reckless as to that);
>   - (b) the re-identification was permitted or required by another law, or authorised or required by a court order;
>   - (c) the accused reasonably believed it was for a **specified purpose** and notified the PDPC or the organisation or public agency as soon as practicable;
>   - (d) the accused reasonably believed, and was not reckless as to whether, they had a legal right to do it (other than for a specified purpose);
>   - (e) other prescribed circumstances.
> - Eleventh Schedule specified purposes (s 48F(4)):
>   - 1. testing the effectiveness of the anonymisation of personal data held by an organisation or public agency;
>   - 2. testing the integrity and confidentiality of anonymised information it holds;
>   - 3. assessing, testing or evaluating its systems and processes for safeguarding the integrity and confidentiality of anonymised information it holds, sends or receives.

*Source note: PDPA p58-60 (s 48F), p121 (Eleventh Sch); DP-Plan p5 (Eleventh Schedule is core reading).*

### clk-m-0-81 — PDPC Guide on Active Enforcement (optional reading)
*Keywords: Guide on Active Enforcement, enforcement outcomes, suspension, discontinuation, advisory notice, voluntary undertaking, remediation plan, breach findings, no breach, warning, directions, financial penalty, expedited decision procedure, EDP, upfront admission of liability, harm, culpability, aggravating, mitigating, first-time offender, cooperation*

**End point:** After an investigation the PDPC may (1) suspend or discontinue it, usually where the impact is low, (2) accept a voluntary undertaking backed by a remediation plan, or (3) make breach findings: no breach, a warning, directions, a financial penalty, or both. Under the expedited decision procedure the organisation admits liability upfront, which shortens the process and counts in its favour on penalty. Penalties are assessed on harm and culpability, then adjusted for mitigation, past breaches, admission, cooperation and proportionality.

> **Guide on Active Enforcement (revised 1 Oct 2022)**
> - Enforcement outcomes (p13):
>   - 1. suspension or discontinuation of the investigation (s 50(3)), often with an advisory notice, where impact is low or limited;
>   - 2. voluntary undertaking (s 48L): possible where the organisation shows accountable policies and practices and has a remediation plan ready to implement at once. Acceptance is at the PDPC's discretion, and the undertaking is published (p18-20);
>   - 3. breach findings: (i) no breach; (ii) warning; (iii) directions; (iv) financial penalties; (v) directions and financial penalties.
> - Expedited decision procedure (p23-24), requiring early on:
>   - an upfront voluntary admission of liability;
>   - the relevant facts (e.g. forensic reports, remediation);
>   - written confirmation of willingness to comply with directions or a penalty.
>   - The admission is a favourable factor on penalty, except for a repeat offender.
> - Financial penalties (p27-28): directions without a penalty are considered first; a penalty is imposed where needed to reflect seriousness. Cap: $1 million or 10% of Singapore turnover if it exceeds $10 million, from 1 Oct 2022 (clk-m-0-36). The method:
>   - 1. assess harm (number affected, categories of data, duration) and culpability (nature of the breach, overall compliance);
>   - 2. adjust for mitigation and its timeliness, previous non-compliance, voluntary admission (including under the EDP), cooperation, and first-time offending;
>   - 3. check the likely impact on the organisation, proportionality and deterrence.

*Source note: Outside the library. PDPC, Guide on Active Enforcement (revised 1 Oct 2022), pdpc.gov.sg, read 19 Nov 2026: p13-14, p18-20, p22-24, p27-28. Listed as optional reading [DP-Plan p6].*

### clk-m-0-82 — Re Spize Concepts [2019] SGPDPC 22 (optional reading)
*Keywords: Spize Concepts, Spize, online ordering, Call Center link, administrator account, password management, data protection officer, DPO, no policies, openness obligation, data intermediary overseas, Novadine, transfer limitation, comparable protection, contractual necessity, financial penalty $20,000, PDPA s 11(3), s 12, s 24, s 26*

**End point:** A food-delivery business's online portal exposed about 148 customers' names, contact details and addresses because someone used the managing director's shared administrator account to make an internal link public. The Commissioner found breaches of the Protection Obligation (poor password and administrator-account controls), the then Openness Obligation (no DPO, no data protection policies), s 12(d)(i) (no information on how its US vendor processed data) and the Transfer Limitation Obligation (no assessment of comparable protection or contractual necessity before using a US data intermediary). Penalty: $20,000.

> **Key points**
> - s 24: password policies and control of administrator accounts are part of reasonable security arrangements ([15]-[17]).
> - ss 11(3), 12(a): no DPO (appointed only after the PDPC's notice) and no policies = breach ([18]).
> - s 26: using an overseas data intermediary is a transfer. The organisation must ensure comparable protection by assessing the foreign law or by contract, or document that a deeming provision (e.g. transfer necessary to perform the contract with the individual) applies ([25]-[27]).
> - Directions: financial penalty of $20,000 within 30 days ([30]).

*Source note: Outside the library. Re Spize Concepts Pte Ltd [2019] SGPDPC 22 (Tan Kiat How, Commissioner, 4 Jul 2019), pdpc.gov.sg, read 19 Nov 2026: [2], [4], [15]-[18], [25]-[27], [29]-[30]. The decision cites the old PDPR 2014 and s 29 numbering; the transfer rules are now in PDPR 2021 Part 3 and directions in s 48I. Listed as optional reading [DP-Plan p6].*

### clk-m-0-83 — Re RedMart [2023] SGPDPC 1 (optional reading)
*Keywords: RedMart, NRIC photographs, ID photographs, suppliers, visitors, warehouse, food safety, consent not appropriate, condition of entry, notification, deemed consent, national interest exception, investigations exception, legitimate interests exception, LIE assessment, no direction, PDPA s 13, s 14, s 15, s 18, s 20, First Schedule Part 3 para 1*

**End point:** RedMart photographed suppliers' NRICs at its warehouses for food-safety reasons without notifying them of the purpose. Consent was not valid: the purpose was not notified, and photographing IDs as a condition of making deliveries for work was not consent to a product or service they chose. Deemed consent, the national interest exception and the investigations exception (which needs an ongoing, not a future, investigation) were all rejected. Legitimate interests could apply, and once RedMart did and documented a proper assessment with mitigating controls, no direction was needed.

> **Key points**
> - Consent failed: no notice of purpose (ss 14(1)(a), 18(b), 20); and consent is not the right basis for a condition of entry imposed on workers making deliveries ([5]).
> - Legitimate interests exception (First Sch Pt 3 para 1, from 1 Feb 2021): before collecting, assess and document whether the interests outweigh any adverse effect, implement mitigating measures, and give reasonable access to information, e.g. in the public data protection policy ([6]-[7]).
> - Rejected bases ([11]): national interest (food security at one's own warehouses is not national defence or security); investigations (must be an ongoing investigation, not a hypothetical future one); deemed consent (no real choice, and not obvious that ID images would be taken and stored).
> - Outcome: RedMart's later assessment and controls (limited collection, restricted devices and access, one-year retention, notices at the security posts) satisfied the exception, so the proposed direction was not issued ([13]-[18]).
> - Do not confuse with RedMart [2022] SGPDPC 8 (API key leak; $72,000 penalty under s 24).

*Source note: Outside the library. Re RedMart Ltd [2023] SGPDPC 1 (Yeong Zee Kin, Deputy Commissioner, 18 Jan 2023), pdpc.gov.sg, read 19 Nov 2026: [1]-[18]. Legitimate interests rule: clk-m-0-17. Listed as optional reading [DP-Plan p7].*

## 0.VI Protection obligation and data breach notification

- **What security must an organisation have? (s 24)**
  - Reasonable security arrangements, including against loss of storage media; no one-size-fits-all, no mandatory ISO 27001 → [0-40](#clk-m-0-40)
- **Is the data breach notifiable?**
  - Significant harm, or 500 or more individuals → [0-42](#clk-m-0-42)
  - Exception: unauthorised access only within the organisation is deemed not notifiable → [0-41](#clk-m-0-41)
- **What must happen after a breach, and who does it?**
  - The organisation assesses reasonably and expeditiously; a DI tells the organisation without undue delay → [0-43](#clk-m-0-43)
  - The organisation notifies the PDPC within 3 calendar days of assessing the breach as notifiable, not of discovering it → [0-44](#clk-m-0-44)
  - The organisation notifies individuals on or after notifying the PDPC; harm-type breaches only, with exceptions → [0-45](#clk-m-0-45)
  - The DI does not notify the PDPC → [0-6](#clk-m-0-6)
- **How should an organisation respond to a breach? (PDPC data breach guide)**
  - C.A.R.E.: Contain, Assess, Report, Evaluate; assess whether notifiable within 30 calendar days of credible grounds → [0-86](#clk-m-0-86)
- **Optional reading: decisions**
  - Singtel (DP-2102-B7878): zero-day in a third-party file transfer appliance; patched within 5 days; no breach of s 24 → [0-84](#clk-m-0-84)
  - Marina Bay Sands [2025]: API identifier dropped in a software migration, 665,495 patrons exposed; negligent breach; $315,000 → [0-85](#clk-m-0-85)

### clk-m-0-40 — The Protection Obligation
*Keywords: protection obligation, reasonable security arrangements, storage medium, ISO 27001, administrative, technical, physical, PDPA s 24*

**End point:** An organisation (controller or intermediary) must make reasonable security arrangements against unauthorised access, collection, use, disclosure, copying, modification or disposal, and loss of storage media; there is no one-size-fits-all and no mandated standard such as ISO 27001.

*Source note: PDPA p33 (s 24); DP-2 p40-44; SampleQs p91-92 Q6, Q10, key p130*

### clk-m-0-41 — Breach within the organisation
*Keywords: data breach, within an organisation, not notifiable, PDPA s 26B(4)*

**End point:** A breach that relates only to unauthorised access within the organisation is deemed not notifiable.

*Source note: PDPA p35 (s 26B(4))*

### clk-m-0-42 — When a breach is notifiable
*Keywords: notifiable data breach, significant harm, significant scale, 500 individuals, account identifier, password, PDPA s 26B, DBNR reg 3, reg 4*

**End point:** A breach is notifiable if it causes or is likely to cause significant harm, or affects 500 or more individuals; harm is deemed for a name or ID number plus prescribed data, or an account identifier plus password.

*Source note: PDPA p34-35 (s 26B); DBNR p2 (regs 3-4). Conflict: Cyril-Exam DP §2.1.2 lists name, account identifier and credentials separately; DBNR reg 3 requires the combinations.*

### clk-m-0-43 — Assessing a suspected breach
*Keywords: assessment, reasonable and expeditious, 30 days, data intermediary, without undue delay, PDPA s 26C*

**End point:** The organisation must assess a suspected breach reasonably and expeditiously (PDPC guidance: generally within 30 days, not in the statute); a data intermediary must tell the controller without undue delay.

*Source note: PDPA p35-36 (s 26C); KC p130*

### clk-m-0-44 — Notifying the PDPC — 3 calendar days
*Keywords: notify PDPC, 3 calendar days, after assessment, late notification, PDPA s 26D(1), DBNR reg 5*

**End point:** The PDPC must be notified as soon as practicable and no later than 3 calendar days after the day the organisation assesses the breach as notifiable (not from discovery); late notices must give reasons.

*Source note: PDPA p36 (s 26D(1)); DBNR p3-4 (reg 5)*

### clk-m-0-45 — Notifying affected individuals
*Keywords: notify individuals, on or after, scale-only, remedial action, waiver, law enforcement, PDPA s 26D(2), s 26D(5)-(7)*

**End point:** Individuals must be notified on or after notifying the PDPC, and only for harm-type breaches (not scale-only ones), unless remedial action or prior technological protection makes harm unlikely, the PDPC or a law-enforcement agency directs otherwise, or the PDPC waives it.

*Source note: PDPA p36-37 (s 26D(2), (5)-(7)); DP-2 p49-50. Conflict: Nic-DP p6 says "concurrently"; the Act says on or after.*

### clk-m-0-84 — Singtel, PDPC Case DP-2102-B7878: no breach (optional reading)
*Keywords: Singtel, Singapore Telecommunications, no breach, zero-day vulnerability, third-party file transfer appliance, FTA, Accellion, vendor-controlled source code, patching within five days, reasonable security arrangements, Protection Obligation, PDPA s 24*

**End point:** Threat actors exploited two zero-day vulnerabilities in a third-party file transfer appliance that Singtel licensed, exfiltrating personal data of 163,370 individuals. Only the developer (Accellion) had the source code and could find and fix the flaws, and Singtel patched the appliance within five days of each update. The Deputy Commissioner held Singtel had made reasonable security arrangements and could not be liable for zero-day vulnerabilities in a third party's system: no breach of s 24, no enforcement action.

*Source note: Outside the library. PDPC, Summary of the Decision, Case No DP-2102-B7878, Singapore Telecommunications Ltd (published 19 May 2022), pdpc.gov.sg, read 19 Nov 2026: paras 1-7. Listed as optional reading [DP-Plan p7]. Compare SingHealth (clk-m-0-39), where the organisation's own measures fell short.*

### clk-m-0-85 — Re Marina Bay Sands [2025] SGPDPC 6 (optional reading)
*Keywords: Marina Bay Sands, MBS, software migration, API identifier omitted, single employee, no second-layer check, six months undetected, 665,495 patrons, dark web, negligent breach, standard of negligence, reasonably foreseeable risk, recklessness distinguished, revised penalty cap 10% of turnover, financial penalty $315,000, PDPA s 24, s 48J*

**End point:** During a large software migration, one API identifier was left out, so a webpage lost its security policies and 665,495 patrons' data was exfiltrated and offered for sale. One employee had compiled the API list manually with no second check, and the gap went unnoticed for six months. The Commissioner held this a negligent breach of the Protection Obligation and imposed $315,000, crediting MBS's voluntary admission and immediate remediation. Negligence under s 48J is objective: if the risk was reasonably foreseeable and the arrangements fell below what a reasonable organisation would have done, the breach is negligent; it need not be reckless.

> **Key points**
> - Standard ([44]-[47]): negligence is not limited to conduct that would necessarily cause the harm. That conflates it with recklessness (failing to address blatant or obvious risks). Ask objectively (a) what risks to the data were reasonably foreseeable, and (b) what security arrangements the organisation should reasonably have had.
> - Risk factors ([46]): volume, type and nature of the data; how it is processed; the form in which it is held; impact on data subjects of unauthorised access.
> - Penalty: $315,000 under the revised framework (cap 10% of Singapore turnover above $10 million from 1 Oct 2022) ([120], [123]).

*Source note: Outside the library. Re Marina Bay Sands Pte Ltd [2025] SGPDPC 6 (Lew Chuen Hong, Commissioner, 28 Oct 2025) and PDPC executive summary, pdpc.gov.sg, read 19 Nov 2026: [44]-[47], [120], [123]. Listed as optional reading [DP-Plan p7].*

### clk-m-0-86 — PDPC Guide on Managing and Notifying Data Breaches (optional reading)
*Keywords: Guide on Managing and Notifying Data Breaches, data breach management plan, C.A.R.E., CARE, contain, assess, report, evaluate, root cause, 30 calendar days to assess, reasonable and expeditious steps, document the assessment, data intermediary notifies the organisation, significant harm, significant scale, 500 individuals, 3 calendar days*

**End point:** The PDPC's guide frames breach response as C.A.R.E.: Contain the breach and mitigate harm, Assess its cause and effect, Report to the PDPC (mandatory if notifiable) and affected individuals, and Evaluate the response to prevent recurrence. Once it has credible grounds to believe a breach occurred, the organisation must take reasonable and expeditious steps to assess whether it is notifiable, normally within 30 calendar days, and document those steps. A notifiable breach must then be reported to the PDPC within 3 calendar days (clk-m-0-44).

> **Guide (revised 15 Mar 2021)**
> - C.A.R.E. (p5, p13):
>   - **Contain**: stop further compromise; mitigate harm after an initial appraisal;
>   - **Assess**: root cause and effectiveness of containment;
>   - **Report**: to the PDPC (mandatory if notifiable; voluntary otherwise) and to affected individuals if required;
>   - **Evaluate**: review the response and prevent future breaches.
> - Assessment (p21-22): starts when the organisation has credible grounds to believe a breach occurred (self-discovery, public alert, or a data intermediary's notice). It must take reasonable and expeditious steps to assess within 30 calendar days, and be ready to explain any longer time; unreasonable delay is itself a breach of the DBN Obligation. All steps must be documented.
> - Data intermediaries notify the organisation they act for, which assesses and notifies (p21; clk-m-0-6).
> - Notifiable: likely significant harm, or significant scale, i.e. 500 or more individuals (p23-24; clk-m-0-42).

*Source note: Outside the library. PDPC, Guide on Managing and Notifying Data Breaches under the PDPA (revised 15 Mar 2021), pdpc.gov.sg, read 19 Nov 2026: p5, p13, p21-24. Listed as optional reading [DP-Plan p6].*

## 0.VII Cybersecurity Act — critical information infrastructure

- **What is a "computer" or "computer system"?**
  - CYSA s 2 definitions → [0-72](#clk-m-0-72)
- **Is it CII, or another designated system?**
  - Owned by the essential-service provider: necessary for an essential service, loss debilitating, located wholly or partly in Singapore (s 7); ownership is not a criterion → [0-46](#clk-m-0-46)
  - Owned by a third party: the provider is designated responsible (s 16A) → [0-69](#clk-m-0-69)
  - Any owner, short-term high risk: system of temporary cybersecurity concern, up to 1 year (s 17) → [0-70](#clk-m-0-70)
- **What must a CII owner do?**
  - Report material changes within 30 days, and ownership changes within 7 days → [0-47](#clk-m-0-47)
  - Report prescribed cybersecurity incidents → [0-48](#clk-m-0-48)
  - Comply with the cybersecurity code of practice (no legislative effect, but binding unless waived) and with directions → [0-49](#clk-m-0-49)
  - Take part in exercises; appeal to the Minister within 30 days → [0-50](#clk-m-0-50)
  - Audit every 2 years; risk assessment every year → [0-51](#clk-m-0-51)
  - Not a duty: actually providing the essential service → [0-52](#clk-m-0-52)
- **What does the CII Code of Practice require on governance?**
  - Board expertise, a risk register, policies reviewed every 12 months, owner responsible despite outsourcing → [0-53](#clk-m-0-53)
- **What can the Commissioner do in an incident?**
  - s 19 investigation powers; s 20 serious-incident powers → [0-54](#clk-m-0-54)
- **Emergency cybersecurity measures (s 23), technical experts (s 22), ID cards (s 21)** → [0-87](#clk-m-0-87)
  - The Minister, by certificate, may direct any person to take measures against a serious and imminent threat; non-compliance or obstruction: up to $50,000 and/or 10 years → [0-87](#clk-m-0-87)
- **Which services are "essential services"? (First Schedule)** → [0-88](#clk-m-0-88)
  - 11 sectors: energy, info-communications, water, healthcare, banking and finance, security and emergency services, aviation, land transport, maritime, functioning of Government, media → [0-88](#clk-m-0-88)
- **Optional reading: CSA reports**
  - Singapore Cybersecurity Strategy 2021: three pillars and two enablers → [0-89](#clk-m-0-89)
  - Singapore Cyber Landscape 2021: ransomware 137 cases (+54%), 55,000 phishing URLs → [0-90](#clk-m-0-90)

### clk-m-0-46 — Designation of CII
*Keywords: critical information infrastructure, CII, provider-owned CII, designation, essential service, 5 years, outside Singapore, Cybersecurity Act s 7, s 7(1A), First Schedule*

**End point:** A computer system is designated CII (called "provider-owned CII" since 31 Oct 2025) if two conditions are met (s 7(1)):
- it is necessary for the continuous delivery of an essential service, and its loss would be debilitating; and
- it is located wholly or partly in Singapore.

A system wholly outside Singapore can also be designated if it would otherwise have qualified (s 7(1A)). Designation lasts 5 years, and ownership or place of incorporation is not a criterion. If the essential-service provider does not own the system, see clk-m-0-69.

*Source note: SSO-CYSA s 7; CYSA p13-15 (s 7), p69-71 (First Sch); DP-2 p18-21. Conflict: DP-2 p20 says "located in Singapore"; the Act says wholly or partly, and since 31 Oct 2025 s 7(1A) also reaches systems wholly outside Singapore.*

### clk-m-0-69 — Third-party-owned CII — designated provider (s 16A)
*Keywords: third-party-owned critical information infrastructure, designated provider, provider of essential service, not owned by the provider, outside Singapore, 5 years, Cybersecurity Act s 16A, Part 3A*

**End point:** A system may be necessary for an essential service (its loss would be debilitating) but not owned by the essential-service provider. The Commissioner may then designate the provider as responsible for that system's cybersecurity, whether the system is in or outside Singapore (s 16A(1)). The designation lasts 5 years (s 16A(3)). The provider then has duties that mirror a CII owner's (ss 16E-16L):
- furnishing information;
- meeting prescribed standards;
- following directions;
- reporting ownership changes and incidents;
- audits and risk assessments;
- notifying material changes to its legally binding commitment;
- taking part in exercises.

*Source note: SSO-CYSA ss 16A, 16E-16L (Part 3A, inserted by Act 19 of 2024, in force 31 Oct 2025); DP-Plan p5. The library's CYSA (2022) and the DPCR slides do not cover Part 3A.*

### clk-m-0-70 — System of temporary cybersecurity concern (s 17)
*Keywords: system of temporary cybersecurity concern, temporary, high risk, limited period, one year, national security, Cybersecurity Act s 17, Part 3B*

**End point:** The Commissioner may designate a system that is located wholly or partly in Singapore as a system of temporary cybersecurity concern if, for a limited period, both of these hold (s 17(1)):
- there is a high risk of a cybersecurity threat or incident against the system; and
- its loss or compromise would seriously harm Singapore's national security, defence, foreign relations, economy, public health, public safety or public order.

The designation lasts at most one year (s 17(2)(d)). The owner must then furnish information, comply with written directions and report incidents (ss 17D-17F).

*Source note: SSO-CYSA ss 17, 17D-17F (Part 3B, inserted by Act 19 of 2024, in force 31 Oct 2025); DP-Plan p5. The library's CYSA (2022) and the DPCR slides do not cover Part 3B; in the 2022 text s 17 was the appeal section.*

### clk-m-0-72 — What is a "computer" and a "computer system" (CYSA s 2)
*Keywords: computer, definition of computer, meaning of computer, computer system, Computer Misuse Act, data processing device, storage facility, communications facility, interconnected computers, information technology system, operational technology system, industrial control system, SCADA, virtual computer, Cybersecurity Act s 2*

**End point:** CII and the other CYSA designations attach to a "computer" or "computer system". A computer is any electronic, magnetic, optical, electrochemical or other data-processing device performing logical, arithmetic or storage functions, together with its directly related storage and communications facilities. A computer system is an arrangement of interconnected computers designed for one or more specific functions, and includes IT and OT systems.

> **Cybersecurity Act s 2: definitions**
> - "computer": an electronic, magnetic, optical, electrochemical, or other data processing device performing logical, arithmetic, or storage functions —
>   - including any data storage facility or communications facility directly related to or operating in conjunction with it;
>   - excluding any device the Minister prescribes by Gazette notification.
> - "computer system": an arrangement of interconnected computers designed to perform one or more specific functions, including —
>   - (a) an information technology system; and
>   - (b) an operational technology system, e.g. an industrial control system, programmable logic controller, SCADA system or distributed control system.
> - For most of the Act, including Part 3 (other than s 7(1A)) and Parts 3A–3B, "computer" and "computer system" include virtual ones (s 2).
> - The CII designation criteria are in clk-m-0-46.
> - Computer Misuse Act 1993 s 2(1) (not on the CLK reading list) is wider in one way and narrower in another. It also covers "a group of such interconnected or related devices", and it expressly excludes automated typewriters or typesetters, portable hand-held calculators and similar non-programmable devices or devices with no data storage. The CYSA definition leaves out both and excludes only devices the Minister prescribes. For a CYSA question, use the CYSA definition.

*Source note: SSO-CYSA s 2 ("computer", "computer system", virtual computers); Drill 1 DP15. CMA comparison: Computer Misuse Act 1993 s 2(1), SSO current version (sso.agc.gov.sg/Act/CMA1993), read 19 Nov 2026; outside the library.*

### clk-m-0-47 — Reporting changes — 30 days and 7 days
*Keywords: material change, change in ownership, 30 days, 7 days, Cybersecurity Act s 10, s 13*

**End point:** A CII owner must furnish information on request and report material changes within 30 days (s 10), and report a change in beneficial or legal ownership within 7 days (s 13).

*Source note: SSO-CYSA ss 10(5), 13; CYSA p17-18 (s 10), p20 (s 13)*

### clk-m-0-48 — Reporting cybersecurity incidents
*Keywords: cybersecurity incident, prescribed incident, interconnected system, supplier, detection mechanisms, Cybersecurity Act s 14*

**End point:** Within the prescribed period, the owner must report prescribed cybersecurity incidents affecting any of these (s 14(1)):
- the CII;
- any system under the owner's control, whether or not it is interconnected with the CII;
- a supplier's system that is interconnected with the CII.

The owner must also report any other incident the Commissioner specifies, and keep mechanisms to detect incidents (s 14(2)).

*Source note: SSO-CYSA s 14; CYSA p20-21 (s 14); DP-2 p25. Conflict: DP-2 p25 (the 2022 text) covers only the CII and interconnected systems under the owner's control; since 31 Oct 2025, s 14(1)(ba)-(bb) add the owner's other systems and suppliers' interconnected systems.*

### clk-m-0-49 — Cybersecurity code of practice and directions
*Keywords: cybersecurity code of practice, Cybersecurity Code of Practice for CII, code of practice, standards of performance, legislative effect, no legislative effect, must comply, waiver, Commissioner waives, written directions, Cybersecurity Act s 35A, s 12, s 11 (repealed)*

**End point:** A cybersecurity code of practice (or standard of performance) has no legislative effect, but a CII owner must comply with it unless the Commissioner waives it. Owners must also comply with the Commissioner's written directions (s 12). Since 31 Oct 2025 the code-of-practice rule is in s 35A; it was formerly s 11.

> **Cybersecurity Act s 35A: codes of practice and standards of performance**
> - The Commissioner may issue or approve codes of practice or standards of performance for the cybersecurity of (s 35A(1)(a)):
>   - provider-owned CII (its owners);
>   - third-party-owned CII (designated providers, s 16A);
>   - systems of temporary cybersecurity concern (owners, s 17);
>   - other designated systems and providers.
> - A code provision inconsistent with the Act has no effect, to the extent of the inconsistency (s 35A(2)).
> - A code has no effect until notice of it is published (s 35A(3)–(4)).
> - **No legislative effect** (s 35A(5)).
> - **The persons it applies to must comply** (s 35A(6)).
> - **The Commissioner may waive it**, generally or for a specified time, in whole or in part (s 35A(7)).
> - A code provision can be appealed to the Minister within 30 days (s 35B; clk-m-0-50).
> - What the CII Code of Practice requires on governance: clk-m-0-53.

*Source note: SSO-CYSA ss 12, 35A, 35B; CYSA p19-20 (ss 11-12); DP-2 p24; Drill 1 DP11. Conflict: CYSA p19 and DP-2 p24 (the 2022 text) put this rule in s 11. Act 19 of 2024 deleted s 11 with effect from 31 Oct 2025 and moved the rule, unchanged in substance, to s 35A.*

### clk-m-0-50 — Cybersecurity exercises and appeals
*Keywords: cybersecurity exercise, appeal to Minister, 30 days, Cybersecurity Act s 16, s 35B*

**End point:** A CII owner must take part in a cybersecurity exercise when directed (s 16). Designations (including under ss 16A and 17), written directions and codes of practice can be appealed to the Minister within 30 days (s 35B).

*Source note: SSO-CYSA ss 16, 35B; CYSA p24-25 (ss 16-17). Conflict: DP-2 p27 and Cyril-Exam DP §2.2.1 cite s 15(7)-(8) for the exercise offence; it is s 16(3). The library's 2022 CYSA puts appeals in s 17; since 31 Oct 2025 they are in s 35B, and s 17 designates systems of temporary cybersecurity concern.*

### clk-m-0-51 — Audits and risk assessments
*Keywords: audit, risk assessment, once every 2 years, once a year, 30 days, Cybersecurity Act s 15*

**End point:** A CII owner must have an audit at least once every 2 years and a risk assessment at least once a year, and give the reports to the Commissioner within 30 days of completion.

*Source note: SSO-CYSA s 15; CYSA p22 (s 15); DP-2 p26*

### clk-m-0-52 — Running the essential service is not a duty
*Keywords: essential service, not an obligation, CII owner*

**End point:** Providing the essential service using the CII is not one of a CII owner's obligations under the Act.

*Source note: SampleQs p89 Q2, key p130*

### clk-m-0-53 — Code of Practice — governance
*Keywords: Cybersecurity Code of Practice, governance, board, risk register, 12 months, cloud, outsourcing*

**End point:** The board and senior management must include a member with cybersecurity knowledge; there must be a risk framework and a risk register for each CII, policies reviewed every 12 months, and the owner stays responsible when outsourcing or using the cloud.

*Source note: CoP p17-24 (section 3); DP-2 p35-36*

### clk-m-0-54 — Investigation and serious-incident powers (Part 4)
*Keywords: investigation powers, serious cybersecurity incident, severity threshold, privilege, Cybersecurity Act s 19, s 20*

**End point:** Under s 19 the Commissioner may require anyone to attend, answer and produce records (privilege respected, contracts no excuse); for serious incidents meeting the severity threshold, s 20 adds remedial directions, entry, scanning and seizure.

*Source note: CYSA p28-34 (ss 19-20); DP-2 p29-31*

### clk-m-0-87 — Emergency measures, technical experts and ID cards (CYSA ss 21-23)
*Keywords: emergency cybersecurity measures, certificate under the Minister's hand, serious and imminent threat, essential service, national security, specified person, real-time information, overrides contract and professional rules, legal privilege, $50,000, 10 years, immunity for good faith, cybersecurity technical expert, identification card, incident response officer, Cybersecurity Act s 21, s 22, s 23*

**End point:** If satisfied it is necessary to prevent, detect or counter a serious and imminent threat to an essential service or to Singapore's national security, defence, foreign relations, economy, public health, safety or order, the Minister may by certificate authorise or direct any specified person or organisation to take measures or meet requirements (s 23(1)). These include providing information, including real-time information, and override contract and professional confidentiality, but not legal privilege (s 23(2)-(3)). Failing to comply or obstructing is an offence (up to $50,000 and/or 10 years), and good-faith compliance carries immunity (s 23(4)-(6)). The Commissioner may appoint cybersecurity technical experts to advise incident response officers in ss 19-20 investigations (s 22), and officers must declare their office and show ID on demand (s 21).

> **Cybersecurity Act ss 21-23**
> - s 21: an incident response officer exercising Part 4 powers must declare their office and produce an ID card on demand.
> - s 22: the Commissioner may appoint as a cybersecurity technical expert, for a specified period, (a) a public officer or statutory-board employee, (b) a suitably qualified individual, or (c) a full-time national serviceman. They give technical advice in ss 19-20 investigations and must carry an ID card.
> - s 23(1): threat to (a) the provision of an essential service, or (b) national security, defence, foreign relations, economy, public health, public safety or public order. The Minister's certificate may authorise or direct a specified person to take measures or comply with requirements.
> - s 23(2) measures include: Criminal Procedure Code powers; requiring others to give information on the design, configuration, operation or cybersecurity of computers; giving the Minister or Commissioner information (including real-time); reporting breaches or attempted breaches.
> - s 23(3): no right to legally privileged information; otherwise it overrides any law, contract or professional conduct rule.
> - s 23(4)-(5): failure without reasonable excuse, or obstruction, is an offence: up to $50,000 and/or 10 years.
> - s 23(6): no civil or criminal liability for acts done in good faith in compliance.

*Source note: SSO-CYSA ss 21-23; `study/clk-m/authorities/0 Data Protection/Cybersecurity Act 2018 (SSO current).pdf` p76-79. Part 4 is core reading [DP-Plan p5]. Investigation powers in ss 19-20: clk-m-0-54.*

### clk-m-0-88 — Essential services (CYSA First Schedule)
*Keywords: essential services, First Schedule, sectors, energy, electricity, gas, info-communications, telephony, broadband, domain name registry, water, healthcare, acute hospital, banking, payments, securities, currency issuance, civil defence, police, immigration, prison, aviation, air navigation, airport, land transport, MRT, bus, road traffic, maritime, port, bunker, pilotage, Government services, media, broadcasting, newspapers, security printing*

**End point:** CII must be necessary for the continuous delivery of an "essential service", meaning a service listed in the First Schedule (s 2(1); clk-m-0-46). The Schedule lists 46 services in 11 sectors: energy, info-communications, water, healthcare, banking and finance, security and emergency services, aviation, land transport, maritime, functioning of Government, and media.

> **CYSA First Schedule (by sector, items)**
> - Energy (1-2): electricity generation, transmission or distribution; natural gas supply for electricity generation.
> - Info-communications (3-6): fixed and mobile telephony; broadband internet access; national domain name registry.
> - Water (7-9): water supply; used water collection and treatment; stormwater management.
> - Healthcare (10-11): acute hospital care; disease surveillance and response.
> - Banking and finance (12-18): banking; payments clearing and settlement; securities; derivatives; monetary and financial stability; currency issuance; Government cash management and payments.
> - Security and emergency services (19-23): civil defence; police and security; immigration; national registration; prisons.
> - Aviation (24-28): air navigation; airport passenger control; baggage and cargo handling; aerodrome operations; flight operations.
> - Land transport (29-33): licensed rapid transit and bus services, and their monitoring and management; road traffic management.
> - Maritime (34-41): shipping traffic management; container, general and bulk cargo and cruise or ferry terminals; pilotage, towage and water supply; bunker supply; salvage; passenger ferries.
> - Functioning of Government (42-43): electronic delivery of Government services; electronic processing of internal Government functions.
> - Media (44-46): free-to-air broadcasting; newspaper publication; security printing.

*Source note: SSO-CYSA First Sch; `study/clk-m/authorities/0 Data Protection/Cybersecurity Act 2018 (SSO current).pdf` p118-121. The First Schedule is core reading [DP-Plan p5].*

### clk-m-0-89 — The Singapore Cybersecurity Strategy 2021 (optional reading)
*Keywords: Singapore Cybersecurity Strategy 2021, CSA, strategic pillars, foundational enablers, build resilient infrastructure, enable a safer cyberspace, enhance international cyber cooperation, vibrant cybersecurity ecosystem, robust cyber talent pipeline, beyond CII, voluntary non-binding norms*

**End point:** CSA's Strategy 2021 (5 Oct 2021, refreshing the 2016 strategy) has three strategic pillars: build resilient infrastructure, enable a safer cyberspace, and enhance international cyber cooperation. It has two foundational enablers: a vibrant cybersecurity ecosystem and a robust cyber talent pipeline. It flagged expanding the Cybersecurity Act beyond CII, which the 2024 amendments did (clk-m-0-69, clk-m-0-70).

> **Strategy 2021**
> - Pillar 1, build resilient infrastructure: a coordinated national approach with CII at its core; secure Government systems; safeguard important entities and systems beyond CII; regulation remains a key lever, alongside a risk-management mindset.
> - Pillar 2, enable a safer cyberspace: secure digital infrastructure, devices and applications; safeguard cyberspace activities; a cyber-savvy population.
> - Pillar 3, enhance international cyber cooperation: voluntary, non-binding norms alongside international law; capacity-building and interoperable standards; fight cross-border threats.
> - Enablers: develop a vibrant cybersecurity ecosystem (research, innovation, market); grow a robust cyber talent pipeline (youths, women, mid-career).
> - A later Strategy 2026 (13 Oct 2026) has replaced it; the reading list names the 2021 version.

*Source note: Outside the library. CSA, The Singapore Cybersecurity Strategy 2021 (5 Oct 2021), csa.gov.sg, read 19 Nov 2026: p1-3 (overview, pillars and enablers). Listed as optional reading [DP-Plan p6].*

### clk-m-0-90 — Singapore Cyber Landscape 2021 (optional reading)
*Keywords: Singapore Cyber Landscape 2021, SCL, CSA, SingCERT, ransomware, phishing URLs, command and control servers, botnet drones, website defacements, cybercrime, online cheating, Computer Misuse Act cases, spoofed brands*

**End point:** CSA's review of 2021 (published 29 Aug 2022) reported rising threats: 137 ransomware cases reported to SingCERT (up 54% from 89), about 55,000 Singapore-linked phishing URLs (up from 47,000), and 3,300 unique C&C servers (more than triple 2020's 1,026). Cybercrime was 48% of all crime, mainly online cheating (18,068 cases).

> **Headline figures (2021)**
> - Ransomware: 137 cases reported to SingCERT (2020: 89).
> - Phishing: ~55,000 Singapore-linked phishing URLs (2020: 47,000); social networking the most spoofed sector, then financial, then online/cloud services.
> - C&C servers: 3,300 unique (2020: 1,026); botnet drones: ~4,800 a day (2020: 6,600).
> - Website defacements: 419 (2020: 495).
> - Cybercrime: 48% of overall crime; online cheating 18,068 (2020: 12,242); Computer Misuse Act cases 3,731 (2020: 3,482).
> - Cases handled by SingCERT: 7,342 (2020: 9,080).

*Source note: Outside the library. CSA, Singapore Cyber Landscape 2021 (29 Aug 2022), csa.gov.sg, read 19 Nov 2026: p4 (key figures). Listed as optional reading [DP-Plan p6].*

## 0.VIII POHA — offences and civil remedies

- **Which harassment offence?**
  - Intended to cause, and caused, harassment, alarm, distress or humiliation (s 3) → [0-55](#clk-m-0-55)
  - Likely to be caused: fine only (s 4) → [0-56](#clk-m-0-56)
  - Fear or provocation of violence (s 5) → [0-57](#clk-m-0-57)
  - Towards a public servant, including doxxing (s 6) → [0-58](#clk-m-0-58)
  - A course of conduct: unlawful stalking (s 7) → [0-59](#clk-m-0-59)
- **What civil remedy?**
  - Damages under the s 11 statutory tort, and s 11A enhanced damages; the common-law tort is abolished → [0-60](#clk-m-0-60)
  - Protection order: contravention, likely to continue, just and equitable → [0-61](#clk-m-0-61)
- **Protection order refused because the harassment has stopped? (*Lai Kwok Kin v Teo Zien Jackson*)**
  - All three s 12(2) limbs must be met; no presumption once a contravention is shown; the court may weigh conduct after filing, giving less weight to de-escalation that only "games the system" → [0-91](#clk-m-0-91)
- **Who can never get a protection order made against them? (Exempt Class of Persons Order)**
  - Network access, data transmission and search-index providers acting automatically, not originating or selecting the audience, not modifying the content → [0-92](#clk-m-0-92)

### clk-m-0-55 — Intentionally causing harassment, alarm or distress (s 3)
*Keywords: intentional harassment, humiliation, sexual or indecent, doxxing, identity information, related person, POHA s 3*

**End point:** It is an offence to cause harassment, alarm, distress or humiliation, intending to do so, by any of these:
- threatening, abusive, insulting, sexual or indecent words, behaviour or communication;
- publishing identity information of the target or a related person.

The penalty is a fine up to $5,000 and/or up to 6 months. Reasonable conduct is a defence.

*Source note: SSO-POHA s 3; POHA p8-9 (s 3); DP-3 p8-9. Conflict: DP-3 and the Go Pack copy predate Act 23 of 2025 (in force 29 Jun 2026), which added "humiliation" and sexual or indecent conduct; the penalty is unchanged.*

### clk-m-0-56 — Harassment likely to be caused (s 4) — fine only
*Keywords: harassment, likely to cause, humiliation, sexual or indecent, legitimate purpose, science, medicine, education, art, fine only, entity, POHA s 4*

**End point:** Threatening, abusive, insulting, sexual or indecent words, behaviour or communication is an offence if perceived by a person likely to be caused harassment, alarm, distress or humiliation.
- The penalty is a fine up to $5,000 only.
- It binds individuals and entities.
- Sexual or indecent material with a legitimate purpose related to science, medicine, education or art is excluded (s 4(1A)).
- Defences: the accused had no reason to believe it would be perceived, or the conduct was reasonable.

*Source note: SSO-POHA s 4; POHA p10 (s 4); DP-3 p10. Conflict: Cyril-Exam DP §3.2.2 and Nic-DP p11 add up to 6 months' imprisonment; the Act provides a fine only. DP-3 and the Go Pack copy predate Act 23 of 2025 (in force 29 Jun 2026), which added "humiliation", sexual or indecent conduct and the s 4(1A) exception.*

### clk-m-0-57 — Fear or provocation of violence (s 5)
*Keywords: fear of violence, provocation, POHA s 5*

**End point:** Causing fear of, or provoking or facilitating, unlawful violence is punishable by a fine up to $5,000 and/or up to 12 months; the "no reason to believe it would be seen" defence applies only to s 5(1)(b).

*Source note: POHA p11-12 (s 5). Conflict: Cyril-Exam DP §3.2.3 applies that defence to all of s 5.*

### clk-m-0-58 — Conduct towards public servants (s 6)
*Keywords: public servant, public service worker, sexual or indecent, doxxing, identity information, deter from duty, POHA s 6, s 6(1A)*

**End point:** There are two offences, both punishable by a fine up to $5,000 and/or up to 12 months:
- threatening, abusive, insulting, sexual or indecent conduct towards a public servant or public service worker in relation to their duties (s 6(1));
- since 17 Aug 2026, publishing identity information of a public servant or worker (or a related person) with intent to cause harassment, alarm, distress or humiliation, and either to deter them from their duty or because of their lawful discharge of it (s 6(1A)).

For both, the accused must know or ought reasonably to know the victim's capacity.

*Source note: SSO-POHA s 6; POHA p13 (s 6). Conflict: the Go Pack copy predates Act 23 of 2025 (sexual or indecent conduct, 29 Jun 2026) and Act 21 of 2025 (s 6(1A), 17 Aug 2026).*

### clk-m-0-59 — Unlawful stalking (s 7)
*Keywords: unlawful stalking, course of conduct, online stalking, online location, humiliation, POHA s 7*

**End point:** Unlawful stalking is a course of conduct associated with stalking that both:
- causes harassment, alarm, distress or humiliation; and
- is intended to, or the accused knows or ought reasonably to know is likely to, have that effect.

Since 29 Jun 2026 the examples include online activity in places the victim visits, and making a presence felt online (s 7(3)(ca)-(cb)). The penalty is a fine up to $5,000 and/or up to 12 months; reasonable conduct is a defence.

*Source note: SSO-POHA s 7; POHA p15-17 (s 7); DP-Plan p5. Conflict: Cyril-Exam DP omits s 7; it is core. The Go Pack copy predates Act 23 of 2025, which added "humiliation" and the online examples.*

### clk-m-0-60 — Statutory tort and abolition of the common-law tort
*Keywords: statutory tort, damages, enhanced damages, online activity, written request, common-law tort of harassment abolished, POHA s 11, s 11A, s 14*

**End point:** A victim of ss 3, 4, 5 or 7 may sue for damages under the s 11 statutory tort; the common-law tort of harassment is abolished (s 14). Since 29 Jun 2026 the court may also award enhanced damages under s 11A when all three of these hold:
- the conduct is wholly or partly online;
- the victim made a reasonable written request to address it;
- the respondent, without reasonable excuse, failed to do so within a reasonable time.

Enhanced damages are separate from punitive and aggravated damages.

*Source note: SSO-POHA ss 11, 11A, 14; POHA p23 (s 11), p36 (s 14); DP-3 p16. s 11A was inserted by Act 23 of 2025 and is not listed in DP-Plan p5.*

### clk-m-0-61 — Protection orders
*Keywords: protection order, likely to continue, just and equitable, Exempt Class of Persons Order, POHA s 12*

**End point:** The court may grant a protection order if satisfied of a contravention of ss 3 to 7, that it is likely to continue or be repeated, and that an order is just and equitable (deemed on conviction or voluntarily causing hurt); none lies against passive network or search providers (non-core Order).

*Source note: SSO-POHA s 12; POHA p24-26 (s 12); DP-3 p17, p24. Since 29 Jun 2026 a protection order can also require the respondent to stop publishing an offending communication (s 12(2B)(b)).*

### clk-m-0-91 — Lai Kwok Kin v Teo Zien Jackson [2020] SGHC 95 (optional reading)
*Keywords: Lai Kwok Kin, Teo Zien Jackson, WeR1, protection order, likely to continue, just and equitable, conjunctive requirements, pre-emptive approach rejected, conduct after filing, expedited protection order, de-escalation, genuine contrition, game the system, without prejudice, POHA s 12(2)*

**End point:** A former employee harassed his ex-employer's managing director by email and online posts, but the conduct stopped and the posts were taken down. The High Court (See Kee Oon J) upheld the refusal of a protection order. The three s 12(2) requirements (a contravention; likely to continue or recur; just and equitable) are conjunctive, and there is no "starting position" that an order follows once a contravention is shown. The court may consider the respondent's conduct after the application is filed: escalation supports an order, while de-escalation gets weight only if it reflects genuine contrition rather than an attempt to "game the system".

> **Key points**
> - s 12(2)(a)-(c) are cumulative; a "pre-emptive" approach would shift the burden to the respondent and make s 12(2)(b) otiose ([26], [49]).
> - Conduct during the proceedings or while an expedited protection order is in force is relevant to whether a contravention is likely to continue ([56]-[57]).
> - Weight depends on the facts; less weight to de-escalating acts without genuine contrition or done under an EPO ([61]).
> - "Without prejudice" correspondence was privileged and could not be waived unilaterally ([82]-[84]).
> - Appeal dismissed ([85]).

*Source note: Outside the library. Lai Kwok Kin v Teo Zien Jackson [2020] SGHC 95 (See Kee Oon J, 12 May 2020), elitigation.sg, read 19 Nov 2026: [1]-[4], [26], [49], [56]-[57], [61], [82]-[85]. Listed as optional reading under DPCR [DP-Plan p7]; it is a POHA case, not a PDPA one. Protection order rule: clk-m-0-61.*

### clk-m-0-92 — POHA (Exempt Class of Persons) Order 2014 (non-core)
*Keywords: Exempt Class of Persons Order, exempt class, no protection order, no expedited protection order, network access, transmission or routing of data, search engine, index of search results, automatic manner, technical input only, not the originator, does not select recipients, does not modify content, POHA s 21(2)*

**End point:** No protection order or expedited protection order may be made against a person who provides network access, data transmission or routing, or a search-results index, and who publishes the offending communication only in the course of that service, automatically and with technical input only, without originating it, selecting its audience or modifying it.

> **Order para 2: all of these must apply**
> - (a) in the business of providing: (i) network access facilities; (ii) transmission or routing of data or connections for it; or (iii) an index of search results linking to content stored elsewhere;
> - (b) publishes the offending communication or statement electronically in the course of that service;
> - (c) is not its originator;
> - (d) does not select who may perceive it; and
> - (e) performs the service automatically (technical input only) without modifying the content.

*Source note: POHA (Exempt Class of Persons) Order 2014 (S 751/2014, as amended by S 219/2020 wef 1 Apr 2020) para 2; `study/clk-m/authorities/0 Data Protection/POHA (Exempt Class of Persons) Order.pdf` p1-2. Non-core [DP-Plan p6].*

## 0.IX False statements — POHA orders and POFMA

- **Is it POHA or POFMA?**
  - The victim applies to court for an *order*: POHA ss 15–15E
  - A Minister issues a *direction* (correction direction, stop communication direction, access blocking): POFMA, non-core → [0-68](#clk-m-0-68)
- **What must the applicant prove for any POHA false-statement order?** → [0-67](#clk-m-0-67)
  - A false statement of fact about the applicant, on the balance of probabilities
  - The respondent published or carried it (not needed for s 15E)
  - An order is just and equitable
  - Not needed: that the respondent knew it was false, or that the statement is still up
- **Which order? Ask who the respondent is, then what the applicant wants.**
  - Publisher, take it down: stop publication order (s 15A) → [0-62](#clk-m-0-62)
  - Publisher, publish a correction: correction order (s 15B) → [0-63](#clk-m-0-63)
  - Internet intermediary (e.g. Facebook, Google), block Singapore users: disabling order (s 15C) → [0-64](#clk-m-0-64)
  - Internet intermediary, notify the Singapore users who saw it: targeted correction order (s 15D) → [0-65](#clk-m-0-65)
  - Prescribed respondent and serious harm: general correction order (s 15E) → [0-66](#clk-m-0-66)
  - Administrator of a chat group, channel, forum or page (since 29 Jun 2026): ss 15CA (stop) and 15CB (correct) → [0-71](#clk-m-0-71)
- **When does a general correction order apply? (s 15E)** → [0-66](#clk-m-0-66)
  - The respondent is prescribed: a prescribed newspaper, broadcaster, telco or internet intermediary (POHA Regs reg 4). An ordinary blogger never is.
  - The statement has caused, or is likely to cause, serious harm to the subject's reputation. No other order has this requirement.
  - The respondent need not have published the statement.
  - Serious harm: the Act gives no test, only two illustrations (a lawyer losing clients; a widely shared adultery allegation). No reported judgment applies s 15E (eLitigation search, 19 Nov 2026), so argue from the illustrations.
- **Trap words**
  - "Specific correction order": there is no such order. The intermediary order is the *targeted* correction order → [0-65](#clk-m-0-65), [0-67](#clk-m-0-67)
  - The slides label s 15B "(SPO)" and s 15C "correction order (DO)". Use the statute's names → [0-63](#clk-m-0-63), [0-64](#clk-m-0-64)
  - "Direction" means POFMA, not POHA → [0-68](#clk-m-0-68)
- **Which intermediaries are prescribed? (POHA Prescribed Internet Intermediaries Regulations, non-core)**
  - Disabling and targeted correction orders: Facebook, Instagram, Twitter, HardwareZone, WeChat, YouTube; general correction order: SPH, Mediacorp and others, telcos, and Facebook, Instagram, Twitter, HardwareZone, Google Search, Baidu → [0-93](#clk-m-0-93)
- **POFMA in detail (non-core)**
  - Offence of communicating a known falsehood (s 7: up to $50,000 and/or 5 years); Part 3 directions to the communicator: correction and stop communication (ss 10-16) → [0-94](#clk-m-0-94)
  - Part 4 directions to intermediaries and mass media: targeted correction, disabling, general correction (ss 20-28) → [0-95](#clk-m-0-95)
  - Declared online locations (3 or more directed statements, at least 3 within 6 months) and account restriction directions (ss 32-34, 40-43) → [0-96](#clk-m-0-96)
  - Codes of practice; the Prominence Code (s 48) → [0-97](#clk-m-0-97)
  - POFMA Regulations regs 3-8: who is prescribed; what a direction must contain → [0-98](#clk-m-0-98)
- **The Online Safety (Relief and Accountability) Act 2025 (non-core)**
  - Commissioner of Online Safety; victim reports; Part 5 directions; new statutory torts; in force in part from 29 Jun 2026 → [0-99](#clk-m-0-99)

### clk-m-0-62 — Stop publication order (s 15A)
*Keywords: stop publication order, publisher, POHA s 15A*

**End point:** The court may order the respondent publisher, or any other individual or entity, to stop publishing the false statement and not to publish any similar (including identical) statement, by a specified time. "Publishing" excludes intermediary, telco, internet-access and computing resource services.

*Source note: SSO-POHA s 15A; POHA p38-40 (s 15A); DP-3 p19-20. Conflict: the Go Pack copy and DP-3 predate Act 23 of 2025 (in force 29 Jun 2026), which widened s 15A(3) from "substantially similar" to "similar" statements, including identical ones (s 15A(5)).*

### clk-m-0-71 — Administrator orders (ss 15CA, 15CB)
*Keywords: administrator, online location, chat group, channel, forum, social media page, group admin, stop publication (administrator) order, correction (administrator) order, POHA s 15CA, s 15CB*

**End point:** Since 29 Jun 2026 the court may make two kinds of order against the administrator of an online location (a website, chat group, channel, forum, social media page, etc.) where the false statement has been published:
- stop its publication in Singapore, including similar copies (s 15CA);
- publish a correction notice (s 15CB).

An administrator is whoever develops, maintains or manages the location, controls membership or access, or has editorial control. It does not include an internet intermediary or an internet-access provider (s 2). The usual requirements apply (clk-m-0-67).

*Source note: SSO-POHA ss 2, 15, 15CA, 15CB (inserted by Act 23 of 2025, in force 29 Jun 2026). Not in DP-3 or the Go Pack copy.*

### clk-m-0-63 — Correction order (s 15B)
*Keywords: correction order, correction notice, POHA s 15B*

**End point:** The court may order the publisher to publish a correction notice.

*Source note: POHA p39 (s 15B); DP-3 p21. Conflict: DP-3 p21 and Cyril-Exam DP §4.1.2 label it "(SPO)"; the statute name is correction order.*

### clk-m-0-64 — Disabling order (s 15C)
*Keywords: disabling order, internet intermediary, end-users in Singapore, POHA s 15C*

**End point:** The court may order an internet intermediary to disable access by end-users in Singapore to the false statement (and identical copies, for prescribed intermediaries).

*Source note: POHA p40-41 (s 15C); DP-3 p22. Conflict: DP-3 p22 labels it "correction order (DO)"; the statute name is disabling order.*

### clk-m-0-65 — Targeted correction order (s 15D) — not a "specific" correction order
*Keywords: targeted correction order, TCO, internet intermediary, notify users who saw it, end-users in Singapore, specific correction order (no such order), POHA s 15D*

**End point:** The court may order an internet intermediary to send a correction notice to the end-users in Singapore who accessed the false statement on its service. This is the only correction order aimed at an intermediary's users. There is no "specific correction order" (clk-m-0-67).

> **POHA s 15D: targeted correction order**
> - Against an internet intermediary, on the application of the subject of the statement (s 15D(1)).
> - The court must be satisfied, on the balance of probabilities, that (s 15D(1)(a)):
>   - (i) material containing the statement has been or is being published by means of the respondent's internet intermediary service; and
>   - (ii) the statement is a false statement of fact;
> - and (b) an order is just and equitable.
> - The notice goes to (s 15D(2)):
>   - (a) all end-users in Singapore who access the specified material on the service from a specified time; and
>   - (b) for a prescribed internet intermediary, also all end-users in Singapore it knows had accessed the material, or identical copies, on the service.

*Source note: SSO-POHA s 15D (unchanged by Acts 21 and 23 of 2025); POHA p41-42 (s 15D); SampleQs p89 Q3, key p130. Conflict: Cyril-Exam DP §4.1.4 calls it a "direction"; under POHA it is an order (directions are POFMA).*

### clk-m-0-66 — General correction order (s 15E) — prescribed respondent and serious harm
*Keywords: general correction order, GCO, prescribed respondent, prescribed individual or entity, serious harm, serious harm to reputation, when to use a general correction order, newspaper, broadcaster, telco, prescribed internet intermediary, POHA s 15E, POHA Regs reg 4*

**End point:** Use a general correction order when two things are present. The respondent must be *prescribed* (a prescribed newspaper, broadcaster, telco or internet intermediary), and the false statement must have caused, or be likely to cause, serious harm to the subject's reputation. The respondent need not have published the statement; it is made to carry a correction notice to its own readers or users.

> **POHA s 15E: general correction order**
> - Against a prescribed individual or entity (s 15E(1); POHA Regs reg 4).
> - The court must be satisfied, on the balance of probabilities, that (s 15E(1)(a)):
>   - (i) the statement is a false statement of fact; and
>   - (ii) its publication has caused or is likely to cause serious harm to the reputation of the subject;
> - and (b) an order is just and equitable.
> - Unlike ss 15A–15D, the respondent need not have published or carried the statement.
> - Where the notice is published (s 15E(2)):
>   - (a) a prescribed newspaper permit-holder: in its newspaper or printed publication;
>   - (b) a prescribed broadcaster: on its broadcasting service;
>   - (c) a prescribed telecommunications licensee: on its system or service;
>   - (d) a prescribed internet intermediary: on its service, or to all or a class of its end-users in Singapore;
>   - (e) anyone else: by any means within its control.
> - **How "serious harm" is assessed.** The Act gives no test, only two illustrations of serious harm:
>   - (a) X falsely says Y, a lawyer, misappropriated client money, and Y's clients end their contracts;
>   - (b) a false allegation that Y committed adultery is widely published on social media.
> - **No case-law test.** Neither the course materials nor any reported judgment sets one: an eLitigation search on 19 Nov 2026 for "general correction order" and "targeted correction order" found 0 judgments. Best-supported position: "serious" means more than ordinary reputational harm, judged on the facts, by analogy with the two illustrations (actual loss of business; wide circulation of a grave allegation).

*Source note: SSO-POHA s 15E and illustrations (unchanged by Acts 21 and 23 of 2025); POHA p42-43 (s 15E); POHA Regs p3 (reg 4(4)); Drill 1 DP14. Conflict: Cyril-Exam DP §4.1.5 lists WeChat and YouTube as prescribed for s 15E; reg 4(4) lists Facebook/Instagram, Twitter, HardwareZone, Google Search and Baidu. WeChat and YouTube are prescribed only for disabling and targeted correction orders (regs 2-3; clk-m-0-93). No reported case applies s 15E (eLitigation search, 19 Nov 2026).*

### clk-m-0-67 — Requirements common to the false-statement orders
*Keywords: false statement of fact, balance of probabilities, just and equitable, does not know it is false, specific correction order, POHA s 15*

**End point:** The applicant must show on a balance of probabilities a false statement of fact about them, published by the respondent, and that an order is just and equitable; the respondent need not know it is false, and orders may issue even if it was amended or taken down. There is no "specific correction order".

*Source note: SSO-POHA ss 15, 15A(2); POHA p37-38 (ss 15, 15A(2)); SampleQs p89 Q3, key p130. Since 29 Jun 2026, s 15(1) also applies these rules to the two administrator orders (clk-m-0-71).*

### clk-m-0-68 — POFMA (non-core)
*Keywords: POFMA, ministerial direction, correction direction, stop communication direction, access blocking order, declared online location*

**End point:** POFMA works through ministerial directions (correction, stop communication, access blocking, directions to intermediaries) rather than court orders; s 7 makes it an offence to communicate a known falsehood likely to cause specified harms.

*Source note: DP-3 p27; POFMA p13-15; DP-Plan p6*

### clk-m-0-93 — POHA (Prescribed Internet Intermediaries and Others) Regulations 2020 (non-core)
*Keywords: prescribed internet intermediary, prescribed respondent, disabling order identical copies, targeted correction order, general correction order, Facebook, Instagram, Twitter, HardwareZone, WeChat, YouTube, Google Search, Baidu, Singapore Press Holdings, Mediacorp, StarHub Cable Vision, SingNet, Singtel Mobile, StarHub Mobile, M1, POHA Regs reg 2, reg 3, reg 4*

**End point:** The Regulations name the intermediaries and others that are "prescribed" for the POHA false-statement orders. For a disabling order (identical copies) and a targeted correction order (notifying past viewers) these are Facebook, Instagram, Twitter, HardwareZone, WeChat and YouTube (regs 2-3). For a general correction order they are SPH, four broadcasters, three telcos, and Facebook, Instagram, Twitter, HardwareZone, Google Search and Baidu (reg 4). WeChat and YouTube are not prescribed for s 15E.

> **POHA Regs (S 217/2020; current version on SSO as at 18 Nov 2026)**
> - reg 2 (s 15C(2)(b), disabling order, identical copies): Facebook and Instagram (Facebook, Inc.); Twitter; HardwareZone.com (SPH Magazines); WeChat; YouTube (Google LLC).
> - reg 3 (s 15D(2)(b), targeted correction order to past viewers): the same five.
> - reg 4 (s 15E, general correction order):
>   - (1) newspaper permit-holder: Singapore Press Holdings Ltd;
>   - (2) broadcasting licensees: Mediacorp Pte Ltd; Mediacorp TV Singapore; StarHub Cable Vision; SingNet;
>   - (3) telecommunications licensees: Singtel Mobile; StarHub Mobile; M1;
>   - (4) internet intermediaries: Facebook and Instagram; Twitter; HardwareZone.com; Google Search; Baidu.

*Source note: POHA (Prescribed Internet Intermediaries and Others) Regulations 2020 (S 217/2020) regs 2-4; `study/clk-m/authorities/0 Data Protection/POHA (Prescribed Internet Intermediary) Regulations.pdf` p1-3; checked against SSO (sso.agc.gov.sg/SL/PHA2014-S217-2020) on 19 Nov 2026, unchanged. Non-core [DP-Plan p6]. This explains the clk-m-0-66 conflict: WeChat and YouTube are prescribed only for regs 2-3.*

### clk-m-0-94 — POFMA offences and Part 3 directions (ss 7-16) (non-core)
*Keywords: POFMA s 7, communication of false statement of fact, knowing or having reason to believe, public interest, security, public health, public tranquillity, friendly relations, election, enmity, public confidence in Government, bots s 8, services s 9, Part 3 Direction, Correction Direction, Stop Communication Direction, Minister, Competent Authority, amended or ceased, non-compliance offence, access blocking order, POFMA s 10, s 11, s 12, s 15, s 16*

**End point:** It is an offence to communicate in Singapore a statement knowing or having reason to believe it is a false statement of fact likely to harm specified public interests (s 7: individual up to $50,000 and/or 5 years; otherwise up to $500,000). Separately, any Minister may instruct the Competent Authority to issue a Part 3 Direction to the person who communicated a false statement of fact, if the Minister thinks it in the public interest (s 10). This can be a Correction Direction (publish a correction notice, s 11) or a Stop Communication Direction (s 12). Non-compliance is an offence (s 15), and the IMDA may be directed to order access blocking (s 16).

> **POFMA ss 7-16**
> - s 7(1): communicating in Singapore a statement known or believed to be false that is likely to: (i) prejudice security; (ii) prejudice public health, safety, tranquillity or finances; (iii) prejudice friendly relations; (iv) influence an election or referendum; (v) incite enmity between groups; or (vi) diminish public confidence in the Government or a statutory board.
> - ss 8-9: offences of making or altering bots, and providing services, for communicating false statements.
> - s 10: conditions for a Part 3 Direction: (a) a false statement of fact has been or is being communicated in Singapore; (b) a Minister thinks it in the public interest. It may issue even if the statement was amended or has ceased (s 10(2)).
> - s 11: Correction Direction: publish a correction notice, including in a specified online location or next to every copy.
> - s 12: Stop Communication Direction: stop communicating it, and substantially similar statements; may also require a correction notice.
> - s 15: non-compliance without reasonable excuse: individual up to $20,000 and/or 12 months; otherwise up to $500,000. Another legal duty or a pending variation application or appeal is no defence.
> - s 16: if a Part 3 Direction is not complied with, the Minister may direct the IMDA to order internet access providers to block the online location.
> - Appeals lie to the High Court (s 17) after an application to the Minister to vary or cancel (s 19).

*Source note: POFMA p13-22 (ss 7-16); DP-3 p27; DP-Plan p6 (POFMA ss 7-16 are non-core reading).*

### clk-m-0-95 — POFMA Part 4 directions to intermediaries and mass media (ss 20-28) (non-core)
*Keywords: Part 4 Direction, internet intermediary, mass media, Targeted Correction Direction, Disabling Direction, General Correction Direction, prescribed internet intermediary, identical copies, newspaper, broadcaster, telecommunications licensee, correction notice easily perceived, remedial order, non-compliance $1 million, $100,000 a day, access blocking, POFMA s 20, s 21, s 22, s 23, s 24, s 27, s 28*

**End point:** If a Minister thinks it in the public interest that material containing a false statement of fact communicated in Singapore be dealt with, Part 4 Directions may go to intermediaries and the mass media (s 20). There are three kinds: a Targeted Correction Direction (an internet intermediary notifies its Singapore users who accessed the material, s 21), a Disabling Direction (disable Singapore users' access, s 22), and a General Correction Direction to prescribed intermediaries, newspapers, broadcasters or telcos (s 23). Non-compliance: individual up to $20,000 and/or 12 months; otherwise up to $1 million plus $100,000 a day (s 27). An access blocking order may follow (s 28).

> **POFMA ss 20-28**
> - s 20: conditions: (a) subject material containing a false statement of fact has been or is being communicated in Singapore; (b) public interest. Also available after amendment or removal (s 20(2)).
> - s 21: Targeted Correction Direction to the intermediary whose service carried it, to notify all Singapore end-users who access it after a specified time; prescribed intermediaries may be required to do more.
> - s 22: Disabling Direction to disable Singapore end-users' access; prescribed intermediaries may also have to disable identical copies and send correction notices.
> - s 23: General Correction Direction to (a) a prescribed internet intermediary, (b) a prescribed newspaper permit-holder, (c) a prescribed broadcaster, (d) a prescribed telecoms licensee, or (e) another prescribed person, to publish a correction notice to its users or audience (who is prescribed: clk-m-0-98).
> - s 24: correction notices must be easily perceived.
> - s 27: non-compliance offence (as above); failing only s 24 is not non-compliance.
> - s 28: access blocking order where a Part 4 Direction is not complied with.

*Source note: POFMA p25-31 (ss 20-28); DP-Plan p6.*

### clk-m-0-96 — POFMA declared online locations and account restriction (ss 32-34, 40-43) (non-core)
*Keywords: declared online location, Declaration, 3 or more statements, active directions, 6 months, 2 years, access blocking, internet intermediary disable access, Account Restriction Direction, inauthentic online account, bot, coordinated inauthentic behaviour, POFMA s 32, s 33, s 34, s 40, s 42, s 43*

**End point:** The Minister may declare an online location if three or more different statements subject to active Part 3 or 4 Directions have been communicated on it, at least three of them first communicated there within the previous six months (s 32(1)). A Declaration lasts at most two years and may require the operator to tell users (s 32(3)). Access may then be blocked, and intermediaries ordered to disable access (ss 33-34). Separately, a prescribed intermediary may be directed to restrict specified accounts used for a false statement or coordinated inauthentic behaviour, where the account is inauthentic or bot-controlled (s 40). Non-compliance is an offence (s 42) and access blocking may follow (s 43).

> **POFMA ss 32-43**
> - s 32(1): (a) 3 or more different statements subject to active Part 3 and/or Part 4 Directions communicated on the location; (b) at least 3 first communicated there within 6 months before the Declaration.
> - s 32(3): the Declaration must give the URL or identifier, reproduce the Directions, state its start and expiry (not later than 2 years), and may require the operator to notify users.
> - ss 33-34: access blocking orders, and orders to internet intermediaries to disable access to the declared location. ss 36-38: no deriving benefit, paid content or financial support for declared locations.
> - s 40: Account Restriction Direction to a prescribed internet intermediary to (a) stop the service being used to communicate through specified accounts, or (b) stop those accounts interacting with Singapore users. Conditions: the account is with that intermediary; a false statement of fact or coordinated inauthentic behaviour was carried out with it; the Minister has determined it is inauthentic or bot-controlled; and it is in the public interest.
> - ss 42-43: non-compliance offence; access blocking.

*Source note: POFMA p36-50 (ss 32-43); DP-Plan p6.*

### clk-m-0-97 — POFMA codes of practice and the Prominence Code (s 48) (non-core)
*Keywords: code of practice, POFMA s 48, Competent Authority, POFMA Office, IMDA, political paid content, sponsor disclosure, coordinated inauthentic behaviour, give prominence to credible sources, Code of Practice for Giving Prominence to Credible Online Sources of Information, Prominence Code, due diligence, annual report*

**End point:** The Competent Authority (the POFMA Office in IMDA) may issue codes of practice to prescribed intermediaries on disclosing political paid content, countering inauthentic behaviour, giving prominence to credible sources, and not giving prominence to declared locations or directed material (s 48). Under the Prominence Code (in force 2 Oct 2019), prescribed intermediaries must have reasonable due diligence measures that prioritise authoritative information, give contextual information, keep declared and directed material out of promotional sections, and provide Government reporting channels. They must report annually to the POFMA Office.

> **Prominence Code**
> - Applies to prescribed internet intermediaries (para 4): give prominence to credible online sources, and not give prominence to declared online locations or material subject to a Part 3 or Part 4 Direction.
> - Due diligence measures must include (para 5):
>   - (a) prioritising relevant and authoritative information, or reducing the visibility of directed material, in automatically ranked channels;
>   - (b) contextual information on sources (trustworthiness indicators, media ownership, verified identity);
>   - (c) keeping declared locations and directed material out of sections meant to promote viewership;
>   - (d) Government reporting channels, acted on as soon as practicable.
> - Annual report to the POFMA Office (para 6).

*Source note: POFMA p55 (s 48); POFMA Office, Code of Practice for Giving Prominence to Credible Online Sources of Information (2 Oct 2019) paras 2-6, `Seniors Notes/Nic_s Part B Package/4. Nic Exam Go Pack/5. CLK/PDPA/2. PDPA Statutes/POFMA_Office,_Code_of_Practice_for_Giving_Prominence_to_Credible.pdf` p1-2. Non-core [DP-Plan p6].*

### clk-m-0-98 — POFMA Regulations 2019, regs 3-8 (non-core)
*Keywords: POFMA Regulations, prescribed internet intermediaries, Google Search, Facebook, Instagram, Messenger, WhatsApp, X, Twitter, HardwareZone, Baidu, TikTok, YouTube, WeChat, SPH Media, Mediacorp, StarHub, SingNet, Singtel Mobile, M1, digital advertising intermediaries, Google Ads, Audience Network, contents of a direction, public interest statement, basis of falsity, regs 3-8*

**End point:** The Regulations name the prescribed intermediaries and media for POFMA directions and set what a direction must contain. Targeted correction, disabling and general correction directions: Google Search, Facebook, Instagram, X, HardwareZone, Baidu and TikTok, plus YouTube and WeChat for ss 21-22 (reg 3(1)-(2)). Account restriction directions also cover Messenger and WhatsApp (reg 3(3)). Prescribed media for general correction directions are SPH Media, four broadcasters and three telcos (reg 4). Every Part 3 or 4 Direction must state the online location, the basis on which the statement is false, and that the Minister thinks it in the public interest (reg 6).

> **POFMA Regulations 2019 (version in force from 24 Aug 2023)**
> - reg 3(1) (ss 21(2), 22(2), 23(1)(a)): Google Search; Facebook and Instagram (Meta); X; HardwareZone.com (SPH Media); Baidu; TikTok.
> - reg 3(2) (ss 21(2), 22(2) only): YouTube; WeChat.
> - reg 3(3) (s 40, account restriction): YouTube; Facebook, Messenger and Instagram; WhatsApp; X; HardwareZone.com; WeChat; TikTok.
> - reg 4: newspaper permit-holder SPH Media; broadcasters Mediacorp Pte Ltd, Mediacorp TV Singapore, StarHub Cable Vision, SingNet; telcos Singtel Mobile, StarHub Mobile, M1.
> - reg 5: digital advertising intermediaries: Google Ads; Meta's Audience Network.
> - reg 6: a Part 3 or Part 4 Direction must contain (a) the online location; (b) the basis on which the statement is false; (c) a statement that the Minister thinks it is in the public interest; (d)-(e) how and where to apply to the Minister to vary or cancel it.
> - reg 7: a Declaration must state how to apply to suspend, vary or cancel it.
> - reg 8: an Account Restriction Direction must give the account details, the basis of falsity or coordinated inauthentic behaviour, the basis for finding the account inauthentic or a bot, and the public interest statement.

*Source note: POFMA Regulations 2019 (S 662/2019, version in force from 24/8/2023) regs 3-8; `study/clk-m/authorities/0 Data Protection/POFMA Regulations.pdf` p2-7. Non-core [DP-Plan p6].*

### clk-m-0-99 — Online Safety (Relief and Accountability) Act 2025 (non-core)
*Keywords: Online Safety (Relief and Accountability) Act, OSRAA, Online Safety (Relief and Accountability) Bill 2025, Act 23 of 2025, Commissioner of Online Safety, Online Safety Commission, OSC, online harmful activity, online harassment, doxxing, online stalking, intimate image abuse, image-based child abuse, online impersonation, inauthentic material abuse, false material, statement harmful to reputation, incitement of enmity, incitement of violence, report, Part 5 direction, stop communication direction, access disabling direction, right-of-reply direction, labelling direction, account restriction direction, engagement reduction direction, access blocking order, app removal order, statutory torts, administrators, online service providers, online harm notice*

**End point:** Passed on 5 Nov 2025, the Act (No 23 of 2025) commenced in part on 29 Jun 2026. It creates a Commissioner of Online Safety to whom a victim (a citizen, PR or person with a prescribed connection; a parent for a child) may report online harmful activity. On "reason to suspect" such activity, even from the report alone, the Commissioner may give Part 5 directions to anyone, in or outside Singapore: stop communication, restraining, access disabling, right-of-reply, labelling, account restriction and engagement reduction directions. Non-compliance can lead to access blocking or app removal orders and is an offence. The Act also creates statutory torts against perpetrators, administrators and online service providers that fail to respond reasonably to an online harm notice. It also made the POHA amendments now in force (e.g. administrator orders, clk-m-0-71).

> **OSRAA 2025**
> - Online harmful activities (Part 3; s 3(1)): online harassment (s 9), doxxing (s 10), non-consensual disclosure of private information (s 11), online stalking (s 12), intimate image abuse (s 13), image-based child abuse (s 14), online impersonation (s 15), inauthentic material abuse (s 16), publication of false material (s 17), statement harmful to reputation (s 18), online instigation of disproportionate harm (s 19), incitement of enmity (s 20), incitement of violence (s 21). Only those brought into operation count; from 29 Jun 2026 these include ss 9, 10, 12, 13 and 14.
> - Online harassment (s 9): online material a reasonable person would conclude is threatening, abusive, insulting, sexual or indecent, and likely to cause harassment, alarm, distress or humiliation (excluding material with a legitimate scientific, medical, educational or artistic purpose).
> - Reports (Part 4): eligible victims (s 22) report to the Commissioner, subject to prescribed preconditions (s 23).
> - Directions (Part 5): given on reason to suspect, possibly on the report alone (s 26(1)-(2)), to any individual or entity in or outside Singapore (s 26(3)). For false material, only right-of-reply directions, unless the falsehood ties the victim to a trade, investment or fundraising (s 26(5)). On non-compliance: access blocking order (s 44) or app removal order (s 45) (s 43).
> - Reconsideration and appeal to the Online Safety Appeal Panel (Part 7); offences of non-compliance (ss 71-72).
> - Torts (Parts 10-12): e.g. intimate image abuse (s 83), image-based child abuse (s 84), online impersonation (s 85); administrators facilitating harm or failing to respond reasonably to an online harm notice (ss 90-91); online service providers failing to respond reasonably (s 94). Remedies include damages, enhanced damages and orders (Part 13).

*Source note: Outside the library. Online Safety (Relief and Accountability) Act 2025 (No 23 of 2025), SSO current version as at 18 Nov 2026 (sso.agc.gov.sg/Act/OSRAA2025), read 19 Nov 2026: commencement note, ss 2, 3, 9, 22, 26, 43-45, 83-94. The reading list names the Bill [DP-Plan p6]; it has since been enacted. Non-core.*

## 0.X AI regulation

- **Non-core; outside course materials.** The learning plan lists this topic "in brief" only, and the library has no slides for it. These blocks use the PDPC's own published guidance → [0-73](#clk-m-0-73)
- **What is the Model AI Governance Framework? Is it binding?** → [0-73](#clk-m-0-73)
  - Voluntary, not law: PDPC/IMDA guidance, 2nd ed 21 Jan 2020 (1st ed 23 Jan 2019)
  - Two guiding principles: AI decision-making should be explainable, transparent and fair; AI solutions should be human-centric
  - Four areas: internal governance structures and measures; level of human involvement in AI-augmented decision-making; operations management; stakeholder interaction and communication
  - Algorithm-, technology-, sector-, scale- and business-model-agnostic. Not aimed at off-the-shelf software that happens to include AI
- **How much human oversight should the AI decision have?** → [0-73](#clk-m-0-73)
  - Human-in-the-loop: the human keeps full control and the AI only recommends (doctor choosing a diagnosis)
  - Human-out-of-the-loop: no human oversight and no override (product recommendations, airline scheduling)
  - Human-over-the-loop (human-on-the-loop): the human monitors and can take over (GPS route the driver can change)
  - Choose using the probability-severity of harm matrix, plus nature and reversibility of harm and operational feasibility
- **Does the PDPA apply when an organisation trains or deploys an AI system?** Yes → [0-74](#clk-m-0-74)
  - Training or testing a model on customer data without consent: Business Improvement Exception (improve a product, recommendation engine, HR shortlisting, job assignment to platform workers, bias assessment) → [0-74](#clk-m-0-74), [0-19](#clk-m-0-19)
  - Commercial research with no product roadmap, clear public benefit, joint research with an unrelated company: Research Exception → [0-74](#clk-m-0-74), [0-20](#clk-m-0-20)
  - Deployed AI making recommendations, predictions or decisions about users: consent and notification, unless deemed consent or an exception applies → [0-74](#clk-m-0-74)
  - AI used to detect fraud or illegal activity without consent: legitimate interests exception → [0-74](#clk-m-0-74), [0-17](#clk-m-0-17)
  - What to tell users: the feature, the types of data, why the data is relevant, which data most influences the output → [0-74](#clk-m-0-74)
  - Written policies on AI safeguards (Accountability, s 12) → [0-74](#clk-m-0-74)
  - A vendor or systems integrator building a bespoke AI system with the client's data is a data intermediary → [0-74](#clk-m-0-74), [0-6](#clk-m-0-6)
- **AI ethics and data governance: what good practice looks like** → [0-75](#clk-m-0-75)
  - Data minimisation; pseudonymise or anonymise; anonymised data is outside the PDPA but can be re-identified
  - Data lineage and provenance record; data quality; selection and measurement bias; separate training, testing and validation datasets
  - Explainability, or repeatability where explainability is impracticable; robustness; traceability; reproducibility; auditability
  - Tell stakeholders: general disclosure, opt-out option, feedback channels and review of decisions

### clk-m-0-73 — Model AI Governance Framework (non-core; outside course materials)
*Keywords: Model AI Governance Framework, Model Framework, MAIGF, PDPC, IMDA, voluntary, not binding, guiding principles, explainable, transparent, fair, human-centric, human-in-the-loop, human-out-of-the-loop, human-over-the-loop, human-on-the-loop, probability-severity of harm matrix, internal governance, operations management, stakeholder interaction, ISAGO, Compendium of Use Cases, AI governance, artificial intelligence*

**End point:** The Model AI Governance Framework is voluntary PDPC/IMDA guidance, not law (2nd ed, 21 Jan 2020). It rests on two principles: AI decision-making should be explainable, transparent and fair, and AI solutions should be human-centric. It turns them into practices in four areas. The level of human oversight (in, out of, or over the loop) is chosen mainly by the probability and severity of harm.

> **Model AI Governance Framework (2nd ed)**
> - Nature (paras 1.1, 2.2–2.3):
>   - voluntary and "living"; adopting it does not absolve an organisation from complying with current laws, but helps show accountability-based practices (para 2.12);
>   - algorithm-, technology-, sector-, scale- and business-model-agnostic;
>   - aimed at organisations deploying AI at scale, not at those buying off-the-shelf software that now includes AI.
> - Two guiding principles (para 2.7):
>   - (a) organisations using AI in decision-making should ensure the process is explainable, transparent and fair;
>   - (b) AI solutions should be human-centric: human well-being and safety are the primary considerations.
> - Four areas (Part 3):
>   - internal governance structures and measures: clear roles, risk management and internal controls, ethics review boards, board-level sponsorship (paras 3.5–3.7);
>   - determining the level of human involvement in AI-augmented decision-making (paras 3.14–3.18);
>   - operations management: data for model development, and explainability, repeatability, robustness, traceability, reproducibility and auditability (paras 3.19–3.44; clk-m-0-75);
>   - stakeholder interaction and communication: general disclosure, opt-out, feedback channels (paras 3.45–3.62; clk-m-0-75).
> - Three approaches to human involvement (para 3.14):
>   - (a) human-in-the-loop: active human oversight; the human keeps full control and the AI only recommends (a doctor deciding the diagnosis);
>   - (b) human-out-of-the-loop: no human oversight over executing the decision; the AI has full control with no human override (product recommendations; airline scheduling);
>   - (c) human-over-the-loop (human-on-the-loop): the human monitors or supervises and can take over when the model meets unexpected events (a GPS route the driver can alter).
> - Choosing the approach (paras 3.15–3.18):
>   - a matrix of the probability of harm against the severity of harm to the individual or organisation;
>   - not the only factors: also the nature and reversibility of harm and operational feasibility;
>   - for safety-critical systems, a person should be able to assume control or safely shut the system down.
> - Companion documents: the Implementation and Self-Assessment Guide for Organisations (ISAGO) and a Compendium of Use Cases (para 2.4).

*Source note: Outside the library. PDPC/IMDA, Model Artificial Intelligence Governance Framework, 2nd ed (21 Jan 2020), pdpc.gov.sg, read 18 Nov 2026: Summary of updates p4; paras 1.1 (p10-11), 2.2-2.4 (p13-14), 2.7 (p15), 2.12, 3.5-3.7 (p21-22), 3.14-3.18 (p30-31). The course library only names the topic and the Framework [DP-Plan p4 (S/N 5), p6 (reading list); `Seniors Notes/Cyril - Part B/Stuff/5. Contemporary Legal Knowledge and Practice (CLK)/1. Data Protection and Cyber Regulation/Slides/1. Introduction.pdf` p4].*

### clk-m-0-74 — Application of the PDPA to AI systems (non-core; outside course materials)
*Keywords: AI system, machine learning, training data, train a model, develop, test, monitor, deploy, recommendation, prediction, decision, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems, 1 Mar 2024, not legally binding, Business Improvement Exception, Research Exception, bias assessment, consent, notification, meaningful consent, legitimate interests, fraud detection, Accountability Obligation, written policies, model card, system card, service provider, systems integrator, bespoke AI, data intermediary, data mapping, labelling, provenance record, First Schedule Part 5, Second Schedule Part 2, s 12, s 20, s 24, s 25, s 26C*

**End point:** The PDPA applies to all collection and use of personal data to develop, test, monitor and deploy AI systems. Training needs consent unless an exception applies, usually Business Improvement (improving an existing product or service) or Research (no product roadmap, clear public benefit). A deployed system needs consent and notification unless deemed consent or an exception (e.g. legitimate interests for fraud detection) applies. A vendor building a bespoke system on the client's data is a data intermediary, and the client stays primarily responsible.

> **PDPC Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (1 Mar 2024)**
> - Status: advisory, not legally binding on the PDPC or anyone; the PDPA prevails on any inconsistency (para 2.2).
> - The PDPA applies to all collection and use of personal data, including to develop, test and monitor AI systems and to deploy them (para 2.1).
> - **Development, testing, monitoring.** Consent, or one of two exceptions (paras 4.2, 5–6):
>   - Business Improvement Exception (First Sch Pt 5; Second Sch Pt 2 Div 2 for sharing within a group): use without consent, of data collected in accordance with the PDPA, for (para 5.1):
>     - (a) improving or enhancing goods or services, or developing new ones;
>     - (b) improving or developing methods or processes for business operations;
>     - (c) learning or understanding individuals' behaviour and preferences;
>     - (d) identifying suitable goods or services, or personalising them;
>     - provided (para 5.2): (a) the purpose cannot reasonably be achieved without identifiable data; and (b) a reasonable person would consider the use appropriate.
>     - Examples (para 5.4): social media recommendation engines; job assignment to platform workers; HR systems giving a first cut of candidates. It also covers testing (para 5.6) and bias assessment (paras 5.8–5.10).
>   - Research Exception (Second Sch Pt 2 Div 3): broader R&D with no immediate product application (para 6.1), if (para 6.2):
>     - (a) identifiable data is needed for the research;
>     - (b) there is a clear public benefit;
>     - (c) the results will not be used to make decisions affecting the individual; and
>     - (d) published results do not identify the individual.
>     - Disclosure to another company for joint research also needs consent to be impracticable (para 6.3).
> - **Deployment (B2C).** Consent is needed unless deemed consent or an exception applies (para 9.1):
>   - Notification (s 20) supports meaningful consent; it should be proportionate to the risk and the AI's autonomy (paras 9.2–9.4). Tell users, as far as practicable (para 9.5):
>     - (a) the product function that needs the data;
>     - (b) the types of data;
>     - (c) how the data is relevant to the feature;
>     - (d) which data features most influence the output.
>   - Layered notices, pop-ups, model cards and system cards may be used; commercially sensitive detail may be withheld if the decision is justified and documented internally (paras 9.6–9.8).
>   - Legitimate interests exception: e.g. AI used to detect or prevent illegal activity. The interests must outweigh any adverse effect, and the organisation must tell individuals it relies on the exception (paras 9.9–9.11; clk-m-0-17).
>   - Accountability (ss 11–12): written policies on the practices and safeguards for fairness and reasonableness, proportionate to the risk, available on request (s 12(d)) and ideally published (paras 10.2–10.8). Re HSBC [2021] SGPDPC 3: HSBC met its obligations by explaining how it used personal data and AI in credit assessments (para 10.3 n 18).
> - **Procurement (B2B).** A service provider (e.g. a systems integrator) developing a bespoke AI system with the client's personal data is a data intermediary (paras 11.1–11.2):
>   - it owes the Protection (s 24) and Retention (s 25) Obligations, and must notify the client of a breach (s 26C);
>   - good practice: data mapping and labelling, and a provenance record of the training data's lineage (paras 11.2–11.3);
>   - it should help the client meet its consent, notification and accountability obligations, but the client bears primary responsibility (paras 11.4–11.8).
>   - Not relevant to in-house development or to off-the-shelf products that use AI (para 11.1).

*Source note: Outside the library. PDPC, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (1 Mar 2024), pdpc.gov.sg, read 18 Nov 2026: paras 1.3-1.5 (p3), 2.1-2.2 (p4), 4.2 (p5-6), 5.1-5.10 (p6-8), 6.1-6.3 (p9), 9.1-9.11 (p12-16), 10.1-10.8 (p16-18), 11.1-11.8 (p19-21). Exception wording in the PDPA itself: clk-m-0-19, clk-m-0-20 [PDPA p103-108]. Topic listed only [DP-Plan p4 (S/N 5)].*

### clk-m-0-75 — AI ethics and data governance (non-core; outside course materials)
*Keywords: AI ethics, data governance, data accountability, data minimisation, pseudonymise, de-identify, anonymise, anonymised data, re-identification, model inversion attack, privacy by design, data protection impact assessment, DPIA, data lineage, data provenance, data quality, bias, selection bias, measurement bias, omission bias, stereotype bias, training testing validation datasets, explainability, repeatability, robustness, traceability, reproducibility, auditability, algorithm audit, general disclosure, opt-out, feedback channel, AI Verify*

**End point:** Good AI data governance means using as little personal data as possible: minimise it, and pseudonymise or anonymise it where possible. Anonymised data is outside the PDPA but still carries re-identification risk. Organisations should also know where the data came from (lineage and provenance), check its quality and bias, and make models explainable, or at least repeatable, traceable and auditable. They should tell stakeholders how AI is used and give them channels to give feedback or ask for a review.

> **Data protection in development** (AI Guidelines paras 7.1–7.12):
> - data minimisation: use only the attributes and volume needed (para 7.1);
> - pseudonymise or de-identify as a basic control; if raw data must be used (e.g. facial images), the Protection Obligation (s 24) applies to the development environment, and a DPIA is encouraged (paras 7.2–7.3);
> - privacy by design against privacy attacks such as model inversion (para 7.6);
> - anonymise as far as possible. Anonymised data is outside the PDPA but can be re-identified, so controls are still needed. Where personal data is used instead, document why and decide at senior level (paras 7.8–7.9);
> - data is effectively anonymised when there is no serious possibility of re-identification (para 7.10).
>
> **Data accountability for model development** (Model Framework paras 3.22–3.24):
> - biased, inaccurate or non-representative data raises the risk of discriminatory decisions (para 3.22);
> - practices (para 3.23):
>   - (a) understand data lineage and keep a data provenance record;
>   - (b) ensure data quality: accuracy, completeness, veracity, recency, relevance, integrity, usability, human interventions;
>   - (c) minimise inherent bias: selection bias (including omission and stereotype bias) and measurement bias;
>   - (d) use different datasets for training, testing and validation;
>   - (e) periodically review and update datasets;
> - the same practices apply even if only non-personal or anonymised data is used (para 3.24).
>
> **Algorithm and model** (Model Framework paras 3.25–3.44):
> - explainability: explain how the model's algorithms work and how they reach a decision (paras 3.26–3.29);
> - repeatability: where explainability is impracticable, show the model consistently gives the same result in the same scenario (para 3.30);
> - robustness: the system copes with errors during execution and with erroneous input (paras 3.31–3.35);
> - traceability: decisions and the data and processes behind them are documented (paras 3.36–3.38);
> - reproducibility: an independent party can obtain the same results (paras 3.39–3.40);
> - auditability: the system is ready for an assessment of its algorithms, data and design processes by internal or external auditors (paras 3.41–3.44; Annex B algorithm audits).
>
> **Stakeholder interaction** (Model Framework paras 3.45–3.62):
> - general disclosure of whether and how AI is used (para 3.46);
> - consider whether to offer an option to opt out (paras 3.52–3.53);
> - feedback channels, and a way to ask for a review of material AI decisions; where a fully autonomous decision materially affects a consumer, a human review is reasonable (para 3.54).
>
> **Tools:** AI Verify can test explainability, fairness, robustness and other claims made in notices (AI Guidelines para 10.10).

*Source note: Outside the library. PDPC, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (1 Mar 2024) paras 7.1-7.12 (p10-12), 10.10 (p18-19); PDPC/IMDA, Model AI Governance Framework, 2nd ed (21 Jan 2020) paras 3.22-3.24 (p36-40), 3.25-3.44 (p43-51), 3.45-3.54 (p53-57), Annex B (p67); both read 18 Nov 2026 on pdpc.gov.sg. Cyril's 2025 slides name the topic "Data ethics and future regulatory models / issues" but give no content [`Seniors Notes/Cyril - Part B/Stuff/5. Contemporary Legal Knowledge and Practice (CLK)/1. Data Protection and Cyber Regulation/Slides/1. Introduction.pdf` p4].*

## 1.I What law and technology is

- **What is the framing question?**
  - Does the problem lie with the law, the technology, or both? → [1-1](#clk-m-1-1)
- **Is "cyberlaw" a field of its own?**
  - Easterbrook, the Law of the Horse: no; it is shallow and misses unifying principles, so study general rules → [1-2](#clk-m-1-2)
  - Lessig: specialised study is useful, because cyberspace's architecture regulates → [1-4](#clk-m-1-4)
- **How is behaviour regulated, and how does code differ from law?**
  - Four constraints: law, norms, markets and architecture (code). Law threatens a sanction after the act; code makes behaviour possible or impossible in advance. "Code is law" → [1-3](#clk-m-1-3)
- **Is law a technology?**
  - Elliot: the common law as cybernetic AI; it depends on how "law" and "technology" are defined → [1-5](#clk-m-1-5)

### clk-m-1-1 — The Big Question
*Keywords: Big Question, issue with the law, issue with the technology*

**End point:** Ask whether the problem lies with the law (fix the law), the technology (fix the technology), or both.

*Source note: LT-1 p16*

### clk-m-1-2 — Easterbrook — the Law of the Horse
*Keywords: Easterbrook, Law of the Horse, cyberlaw, unifying principles, Chicago School, property rights, bargaining*

**End point:** Grouping law around one technology is "doomed to be shallow and to miss unifying principles", so study general rules and keep doing what you have been doing; his prescriptions are clear rules, property rights and bargaining institutions.

*Source note: LT-1 p19-21; SampleQs p94 Q6, key p130*

### clk-m-1-3 — Lessig — the four constraints; code versus law
*Keywords: Lessig, four constraints, four modalities, law, norms, markets, architecture, code, code is law, code versus law, difference between code and law, direct regulation, indirect regulation, plastic, ex post sanction*

**End point:** Behaviour is regulated by four constraints: law, social norms, markets and architecture, which in cyberspace is code. Law acts directly, or indirectly by changing the other three. Code and law constrain in different ways. Law tells people how to behave and threatens punishment if they deviate. Code sets the conditions of access in advance, making some behaviour possible and other behaviour impossible, and it is plastic: chosen by those who write it.

> **Code versus law (Lessig, "What Cyberlaw Might Teach")**
> - **Law acting directly** tells individuals how they ought to behave and threatens punishment if they deviate (an ex post sanction) [LT-1 p23; LT-2 p7].
> - **Law acting indirectly** changes one of the other constraints: norms, markets or architecture [LT-1 p23; LT-2 p8].
> - **Code** is the software, architecture or protocols of cyberspace [LT-1 p24]:
>   - it is experienced as conditions of access;
>   - it makes some behaviour possible and other behaviour impossible;
>   - it is chosen by code writers, so it too regulates.
> - **Code is plastic,** so it can regulate more, and more subtly, and can substitute for law or norms [LT-1 p24].
> - The same constraint can be reached by different means at different cost; changing code may be cheaper than changing law (the car radio) [LT-2 p7].
> - **"Code is law."** Because code regulates, law must regulate code if public values, especially constitutional values, are to be preserved [LT-1 p25].

*Source note: LT-1 p23-25; LT-2 p6-8; Drill 2 LT1*

### clk-m-1-4 — Lessig — why cyberspace is special
*Keywords: Lessig, What Cyberlaw Might Teach, specialised study, constitutional values*

**End point:** Cyberspace is special enough that specialised study is useful and possible — because its architecture regulates behaviour, not merely because it is new — and law must regulate code to preserve constitutional values.

*Source note: LT-1 p25-26; SampleQs p95 Q7, key p130. Conflict: Cyril-Exam LT §1.2 and Nic-LT p2 say Lessig wanted "a new field of law"; the slide says only that specialised study is useful.*

### clk-m-1-5 — Is law a technology?
*Keywords: Elliot, Holmes, common law as artificial intelligence, cybernetic feedback*

**End point:** Elliot (1984) described Holmes's common law as a system of artificial intelligence learning by cybernetic feedback; whether law is a technology depends on how "law" and "technology" are defined.

*Source note: LT-1 p14-15. Conflict: Cyril-Exam LT §1.1 says Holmes himself called the common law AI; the slide quotes Elliot writing about Holmes.*

## 1.II Regulation theory

- **When is behaviour controlled?**
  - Ex ante regulation, before harm (speed limits); ex post liability, after harm (tort) → [1-6](#clk-m-1-6)
- **Who makes the rules?**
  - Formal regulation, then quasi-regulation (state-backed codes), then self-regulation → [1-7](#clk-m-1-7)
- **What constrains behaviour? Do regulations count as law?**
  - Market, architecture (code), law, norms. Regulations are part of law, not a fifth modality; "codes" is architecture → [1-8](#clk-m-1-8)
- **Which thinker said what?**
  - Bennett Moses: protect values and minimise harm; rules can be technology-specific, risk-specific or technology-neutral → [1-9](#clk-m-1-9)
  - Yeong Zee Kin: law regulates how technology is applied and supplied; "technology regulation" is a misnomer → [1-10](#clk-m-1-10)
  - Collingridge: too early, too little information; too late, the technology is entrenched → [1-11](#clk-m-1-11)
  - Is law always the slow tortoise to technology's hare? → [1-12](#clk-m-1-12)

### clk-m-1-6 — Ex ante regulation and ex post liability
*Keywords: ex ante, ex post, regulation, liability, Shavell*

**End point:** Regulation controls conduct before harm (e.g. speed limits); liability responds after it (e.g. tort).

*Source note: LT-2 p3*

### clk-m-1-7 — The regulation spectrum
*Keywords: formal regulation, quasi-regulation, self-regulation, codes of practice, soft law, Moran*

**End point:** Rules run from formal regulation (legislation) through quasi-regulation (state-backed soft law such as codes of practice) to self-regulation by industry.

*Source note: LT-2 p3*

### clk-m-1-8 — The four modalities (the pathetic dot) — regulations count as law
*Keywords: pathetic dot, four modalities, market, architecture, code, codes, law, norms, regulations, do regulations count as law, regulations are law, regulation in Lessig's sense, car radio, choice architecture*

**End point:** The four modalities are market, architecture (including code), law and norms. Regulations do count as law: the slide lists "(formal) regulations" under law, beside liability rules and other legal rules. So "regulations" is not a fifth modality, and it is the right answer to "which is NOT one of the four modalities?" ("codes" is architecture). In Lessig's general sense, "regulation" is what all four constraints do. The same constraint can be imposed through different modalities at different cost.

> **The four modalities (LT-2 p6)**
> - **Market:** supply, demand, price.
> - **Architecture:** physical space; code.
> - **Law:** (formal) regulations; liability rules; other legal types (property rules, inalienability rules).
> - **Norms:** culture, custom, "soft" law.

*Source note: LT-2 p6-8; LT-1 p23 (Lessig's general sense of "regulation"); SampleQs p94 Q5, key p130*

### clk-m-1-9 — Bennett Moses
*Keywords: Bennett Moses, technology regulation, socio-technical landscape, technology-neutral, risk-specific*

**End point:** The useful question is not "technology regulation" but how to protect values and minimise harm in an evolving socio-technical landscape; rules may be technology-specific, risk-specific or technology-neutral.

*Source note: LT-2 p10-12*

### clk-m-1-10 — Yeong Zee Kin
*Keywords: Yeong Zee Kin, misnomer, applied and supplied, laws ex post, regulations ex ante*

**End point:** "Technology regulation" is a misnomer: law regulates how technology is applied and supplied; laws are overarching and enforced after the event, regulations are role-specific and set standards in advance.

*Source note: LT-2 p13-14. Conflict: Cyril-Exam LT §2.2.2 attributes the laws/regulations distinction to Bennett Moses; the slide gives it to Yeong.*

### clk-m-1-11 — The Collingridge dilemma
*Keywords: Collingridge dilemma, David Collingridge, uncertainty, entrenchment*

**End point:** Early on there is too little information to regulate well; later the technology is entrenched and costly to change. It was coined by David Collingridge, not Bennett Moses.

*Source note: LT-2 p17; LT-CS1 p68*

### clk-m-1-12 — The legal tortoise and the technological hare
*Keywords: tortoise and hare, law lags technology, stifle innovation*

**End point:** The lecture asks whether law always crawls while technology leaps, framing the debate between waiting to avoid stifling innovation and regulating before risks materialise.

*Source note: LT-2 p18*

## 1.III Automobiles case study

- **What was the first legal response to cars?**
  - Courts applied horse-carriage negligence rules ("the law of the metal horse") → [1-13](#clk-m-1-13)
- **Why did regulation follow?**
  - Liability failed (many accidents, defendants who could not pay), so compulsory insurance followed → [1-14](#clk-m-1-14)
- **What else changed?**
  - Norms (jaywalking stigma), architecture (roads) and law all shifted; a US account → [1-15](#clk-m-1-15)
- **What is the lesson?**
  - Lessig's theory "nearly note for note": ask who has power over code → [1-16](#clk-m-1-16)
- **Who is liable when an automated vehicle crashes? (Soh, control-centric account)**
  - Control means influence over risk, not physical driving, so AVs are legally controllable; manufacturers, software developers, fleet operators and users all share in creating the risk; existing tort principles can cope → [1-62](#clk-m-1-62)

### clk-m-1-13 — The law of the metal horse
*Keywords: law of the metal horse, horse-carriage cases, negligence, driver, Model T*

**End point:** Courts first applied existing horse-carriage negligence rules to cars, extending "driver" to motorists.

*Source note: LT-3 p5-6*

### clk-m-1-14 — Liability failed, so compulsory insurance followed
*Keywords: judgment-proof defendants, compulsory insurance, Road Traffic Acts, 1930s*

**End point:** Liability alone was insufficient (many accidents, judgment-proof defendants), so the UK Road Traffic Acts of the 1930s brought compulsory insurance; compensation still depended on proving negligence.

*Source note: LT-3 p6*

### clk-m-1-15 — Norms, architecture and law all shifted
*Keywords: jaywalking, accidents, roads, sidewalks, US*

**End point:** Norms (the jaywalking stigma, calling collisions "accidents"), architecture (roads, sidewalks) and law (jaywalking offences) all shifted — a US-specific account.

*Source note: LT-3 p7*

### clk-m-1-16 — Lessig's theory plays out
*Keywords: Lessig, power map, corporations, government, communities, who controls code*

**End point:** The history follows Lessig "nearly note for note": markets are held by corporations, law by governments and norms by communities — so ask who has power over code, and look for "we've handled this before".

*Source note: LT-3 p9*

### clk-m-1-62 — Soh: a control-centric account of tort liability for automated vehicles
*Keywords: Jerrold Soh, Towards a Control-Centric Account of Tort Liability for Automated Vehicles, Torts Law Journal 2021, automated vehicle, AV, self-driving car, driver-centric, control, metaphysical risk, risk creation, manufacturer, software developer, fleet operator, consumer, machine learning, existing tort principles*

**End point:** Motor accident law is "driver-centric", which seems to suggest it cannot apply to automated vehicles. Soh argues the tort concept of control should be understood as influence over risk, not over a physical object. On that view AVs are legally controllable in theory despite having no human driver, and legally controlled in practice despite machine learning. Manufacturers, software developers, fleet operators and consumers all participate in creating vehicular risk, so existing tort principles are better equipped to allocate AV liability than they first appear.

*Source note: Jerrold Soh, "Towards a Control-Centric Account of Tort Liability for Automated Vehicles" (2021) Torts Law Journal, abstract at ink.library.smu.edu.sg/sol_research/3217, read 19 Nov 2026. LT-Plan p5 (reading list); the CS1 notes set "my Automated Vehicles piece, p 9–11 only" as a starred reading [`Bar Exam/Modules/Contemporary Legal Knowledge & Practice/2. Law and Technology/Video Lecture & Slides/Compiled_Lecture_Notes_CS 1_(B26S2).pdf` p4]. The full text (SSRN and the SMU repository) sits behind bot checks, so this block follows the author's abstract, not pp 9-11. The course's own automobiles content is clk-m-1-13 to 1-16.*

## 1.IV Electronic transactions

- **Why was the ETA passed, and what do the cases say?**
  - To confirm that familiar contract rules apply online, not to rewrite them; based on the UN Model Law → [1-17](#clk-m-1-17)
  - *Chwee Kin Keong v Digilandmall*: ordinary formation principles apply online; the ETA was not referred to → [1-18](#clk-m-1-18)
  - *SM Integrated Transware v Schenker*: email can be "in writing" for Civil Law Act s 6(d) → [1-19](#clk-m-1-19)
- **How is an e-contract formed?**
  - A website listing is an invitation to make offers (s 14) → [1-20](#clk-m-1-20)
  - Time of receipt: when retrievable at the designated address (s 13) → [1-21](#clk-m-1-21)
  - No human review is no bar (s 15); an input error can be withdrawn if notified promptly and no benefit received (s 16) → [1-22](#clk-m-1-22)
- **Writing, signatures, exclusions and ISPs**
  - Electronic records and signatures count as writing and signatures (ss 6–8) → [1-23](#clk-m-1-23)
  - Excluded: wills, trusts and powers of attorney, sale of immovable property (First Schedule) → [1-24](#clk-m-1-24)
  - Network service providers are not liable for third-party material they merely give access to → [1-25](#clk-m-1-25)

### clk-m-1-17 — Why the ETA was passed
*Keywords: Electronic Transactions Act, ETA, UN Model Law, functional equivalence, technology neutrality, non-discrimination*

**End point:** The rules were clear offline but uncertain in application online, so the ETA clarified and reaffirmed that familiar contract rules apply; it was not a reaction to a court ruling and did not rewrite offer and acceptance. It derives from the 1996 UN Model Law.

*Source note: LT-4 p5, p9, p13; LT-CS1 p67; LT-CS1n p5; SampleQs p93 Q1, key p130*

### clk-m-1-18 — Chwee Kin Keong v Digilandmall
*Keywords: Chwee Kin Keong v Digilandmall, pricing error, unilateral mistake, common ground*

**End point:** It was common ground that ordinary formation principles apply to internet contracts ([29]); the court did not refer to the ETA, which may have played a background role.

*Source note: LT-4 p10-11; SampleQs p95 Q8, key p130; Nic-LT Cases p2-3*

### clk-m-1-19 — SM Integrated Transware v Schenker
*Keywords: SM Integrated Transware v Schenker, Civil Law Act s 6(d), email, writing, land contract*

**End point:** The ETA's carve-out of Civil Law Act s 6 matters does not stop email satisfying s 6(d); construing s 6(d) itself, the emails were "in writing" ([85]).

*Source note: LT-4 p12*

### clk-m-1-20 — Website listings are invitations to offer (s 14)
*Keywords: invitation to make offers, website, interactive application, ETA s 14*

**End point:** A proposal generally accessible to the public, including through interactive ordering, is an invitation to make offers unless it clearly shows an intention to be bound.

*Source note: Nic-ETA p15 (s 14)*

### clk-m-1-21 — Time of receipt (s 13)
*Keywords: time of receipt, designated address, capable of being retrieved, aware, despatch, ETA s 13*

**End point:** A message is received when capable of being retrieved at a designated address; at an undesignated address, when retrievable and the addressee is aware it was sent there; despatch is when it leaves the originator's system.

*Source note: Nic-ETA p14-15 (s 13)*

### clk-m-1-22 — Automated systems and input errors (ss 15–16)
*Keywords: automated message system, input error, withdraw, ETA s 15, s 16*

**End point:** A contract is not invalid merely because no person reviewed an automated system's actions (s 15); a person who makes an input error with no chance to correct it may withdraw that portion if they notify promptly and received no material benefit (s 16).

*Source note: Nic-ETA p15-16 (ss 15-16); LT-4 p4*

### clk-m-1-23 — Writing and electronic signatures
*Keywords: functional equivalence, electronic record, writing, electronic signature, digital signature, ETA ss 6-8*

**End point:** Electronic records, writing and signatures are treated like their paper equivalents (ss 6-8); digital signatures show no tampering and identify the signer, which justifies evidential presumptions.

*Source note: LT-4 p4, p6; Nic-ETA p10-11*

### clk-m-1-24 — Excluded matters
*Keywords: wills, trusts, power of attorney, lasting power of attorney, immovable property, negotiable instruments, bills of lading, First Schedule, ETA s 4, electronic transferable records, Part 2A*

**End point:** The ETA's Part 2 rules on electronic records and signatures do not apply to the First Schedule matters (s 4):
- making a will;
- indentures, declarations of trust and powers of attorney, but not implied, constructive or resulting trusts, or a lasting power of attorney;
- the sale or conveyance of immovable property.

The slides summarise this as wills, trusts and real property. Negotiable instruments and bills of lading are no longer excluded. Since the 2021 amendments that adopted the Model Law on Electronic Transferable Records, they can exist as electronic transferable records under Part 2A.

*Source note: SSO-ETA s 4, First Sch, s 16A; LT-4 p4, p9; Nic-ETA p9, p32-33 (2011 Rev Ed); Cyril-Exam LT §2.4. The Go Pack's 2011 text still lists negotiable instruments and documents of title. Act 5 of 2021 removed them, and Act 16 of 2021 added the lasting power of attorney exception from 14 Nov 2022.*

### clk-m-1-25 — Network service providers
*Keywords: network service provider, third-party material, adopt, ETA s 26*

**End point:** A network service provider is not liable for third-party material it merely provides access to, but remains liable for content it adopts; contractual duties and court orders to remove content are unaffected.

*Source note: LT-4 p7; Nic-ETA p24-25 (s 26)*

## 1.V Algorithmic contracting — B2C2 v Quoine

- **What happened?**
  - A failed platform update led to trades at 10 BTC per ETH; Quoine reversed them → [1-26](#clk-m-1-26)
- **Unilateral mistake with algorithms: whose knowledge, of what, and when?**
  - Whose: the programmer's, for deterministic algorithms → [1-27](#clk-m-1-27)
  - What: actual or constructive knowledge that the offer would only be accepted under a mistake, and acting to take advantage → [1-28](#clk-m-1-28)
  - When: from programming up to formation → [1-29](#clk-m-1-29)
  - Result: no operative mistake; the algorithms worked as meant → [1-30](#clk-m-1-30)
- **Other views**
  - Lord Mance (dissent): what would a reasonable trader have thought? → [1-31](#clk-m-1-31)
  - Vincent Ooi: is software a tool or an electronic agent? → [1-32](#clk-m-1-32)

### clk-m-1-26 — Facts of B2C2 v Quoine
*Keywords: B2C2 v Quoine, Quoine, margin call, 10 BTC to 1 ETH, reversed trades*

**End point:** After Quoine's failed update thinned the market, forced margin-call buys hit B2C2's hard-coded orders at 10 BTC per ETH (against about 0.04), and Quoine reversed the trades.

*Source note: LT-1 p29-31*

### clk-m-1-27 — The programmer's knowledge counts
*Keywords: deterministic algorithm, programmer's knowledge, B2C2 v Quoine*

**End point:** For deterministic algorithms, which do only what they were programmed to do, the relevant knowledge is that of the programmer ([98]).

*Source note: LT-1 p32*

### clk-m-1-28 — The test for unilateral mistake
*Keywords: actual or constructive knowledge, take advantage of a mistake, B2C2 v Quoine*

**End point:** The question is whether, when programming, the programmer had actual or constructive knowledge that the offer would only ever be accepted by a party under a mistake, and was acting to take advantage of it ([103]).

*Source note: LT-1 p33*

### clk-m-1-29 — Time of assessment
*Keywords: point of programming, contract formation, hypothetical trading floor, B2C2 v Quoine*

**End point:** Knowledge is assessed from the time of programming up to formation; Quoine's "hypothetical meeting on the trading floor" approach was rejected ([104]).

*Source note: LT-1 p34*

### clk-m-1-30 — No operative mistake
*Keywords: no mistake, operated as meant to, platform failure, B2C2 v Quoine*

**End point:** There was no mistake in law or equity: the algorithms "operated as they were meant to" ([115]); the counterparties' mistake was about the platform's reliability, not a term.

*Source note: LT-1 p35*

### clk-m-1-31 — Lord Mance's dissent
*Keywords: Mance IJ, dissent, reasonable trader, B2C2 v Quoine*

**End point:** Lord Mance IJ would have asked what a reasonable trader, knowing the circumstances, would have thought ([200]).

*Source note: LT-1 p35*

### clk-m-1-32 — Vincent Ooi — tools or agents
*Keywords: Vincent Ooi, mere tool, electronic agent, objective theory of contract*

**End point:** Ooi asks whether software is a mere tool or an electronic agent, and argues for extending the objective theory of contract.

*Source note: LT-1 p36*

## 1.VI Platform economics

- **Why do platforms win?**
  - They cut transaction costs (concentration, scale, predictability, network externalities) → [1-33](#clk-m-1-33)
- **Which network effect?**
  - Cross-side: more on one side helps the other side → [1-34](#clk-m-1-34)
  - Same-side: users on the same side help or hurt each other (Tinder) → [1-35](#clk-m-1-35)
  - Critical mass: must be reached and kept (Grab) → [1-36](#clk-m-1-36)
- **How do platforms steer behaviour?**
  - Fees, terms, norms and code → [1-37](#clk-m-1-37)
- **Is harm to non-users a network externality?**
  - No (e.g. smoking) → [1-38](#clk-m-1-38)

### clk-m-1-33 — Why platforms win — transaction costs
*Keywords: transaction costs, middleman, economies of concentration, economies of scale, predictability, network externalities*

**End point:** Platforms cut transaction costs as middlemen through economies of concentration and scale, predictability, and network externalities.

*Source note: LT-5 p3-5*

### clk-m-1-34 — Cross-side network effects
*Keywords: network externalities, cross-side network effect, two-sided market*

**End point:** More participants on one side make the platform more valuable to the other side (more riders help drivers), raising its value for everyone.

*Source note: LT-5 p5-6; SampleQs p93 Q2, key p130*

### clk-m-1-35 — Same-side network effects
*Keywords: same-side network effect, Tinder, negative network effect*

**End point:** Participants on the same side can help or hurt each other; Tinder shows positive cross-side but negative same-side effects.

*Source note: LT-5 p8*

### clk-m-1-36 — Critical mass
*Keywords: critical mass, negative feedback loop, Grab*

**End point:** A new platform faces an initial negative loop (no drivers, so no riders, and vice versa); critical mass must be reached and kept — Grab lost half its drivers overnight.

*Source note: LT-5 p6*

### clk-m-1-37 — Platform levers
*Keywords: membership fees, transaction fees, terms, norms, code*

**End point:** Platforms steer behaviour with membership and transaction fees, terms, norms and code; each platform is its own "cyberspace".

*Source note: LT-5 p7-8*

### clk-m-1-38 — What network externalities are not
*Keywords: externality, smoking, harm to others*

**End point:** Harm imposed on non-users (as with smoking) is not a network externality.

*Source note: SampleQs p93 Q2, key p130*

## 1.VII Platform workers

- **UK: is a ride-hailing driver a worker? (Uber v Aslam)**
  - The written contract is not the starting point; control shows subordination → [1-39](#clk-m-1-39)
  - Five findings of control, so drivers were workers → [1-40](#clk-m-1-40)
- **Singapore: what is the policy?**
  - Platform workers are not employees, but get basic protections → [1-41](#clk-m-1-41)
- **Is the worker covered by the Platform Workers Act 2024?**
  - Platform worker: agreement, management control, payment, in Singapore (s 5) → [1-42](#clk-m-1-42)
  - Management control needs all three limbs: data used for a specified purpose, no routine human intervention, a Second Schedule restriction (s 6(1)) → [1-43](#clk-m-1-43)
  - Second Schedule restrictions, and the presumption of control (s 6(3)–(4)) → [1-44](#clk-m-1-44)
  - Escaping the Act: only by disproving a limb → [1-45](#clk-m-1-45)

### clk-m-1-39 — Uber v Aslam — how control is judged
*Keywords: Uber v Aslam, worker, written contract, subordination, control, log on*

**End point:** Because the statute protects vulnerable workers, the written contract is not the starting point ([76]-[77]); control shows subordination and dependence ([87]); freedom to choose when to log on did not prevent worker status ([90]).

*Source note: LT-5 p13-18. UK law itself is not examined (LT-5 p10)*

### clk-m-1-40 — Uber v Aslam — the five findings
*Keywords: Uber v Aslam, five findings, fixes pay, ratings, acceptance rate, workers not employees*

**End point:** Uber fixed pay, dictated terms, constrained ride acceptance, controlled delivery (vetting, ratings) and restricted driver-passenger contact ([93]), so drivers were workers; employee status was left open. Platforms "always cry no control", but code-as-law reveals it.

*Source note: LT-5 p19-20; LT-CS2n p2*

### clk-m-1-41 — The Singapore policy — not employees
*Keywords: Tripartite Workgroup, Platform Workers Act 2024, not employees, work injury compensation, WICA*

**End point:** The Tripartite Workgroup recommended that platform workers not be classed as employees, but that platforms with management control give basic protections such as work-injury compensation; the government accepted all 12 recommendations and passed the PWA.

*Source note: LT-5 p21; LT-CS2n p2*

### clk-m-1-42 — Who is a platform worker (s 5)
*Keywords: platform worker, platform operator, PWA s 5*

**End point:** A platform worker has an agreement with a platform operator, is subject to its management control, is paid or benefits, and is in Singapore.

*Source note: LT-5 p22*

### clk-m-1-43 — Management control — all three limbs (s 6(1))
*Keywords: management control, specified purpose, human intervention, Second Schedule, PWA s 6(1)*

**End point:** Management control needs all three: (a) data on users and non-employee workers used for a specified purpose (eligibility, task allocation, payment, or a prescribed purpose); (b) no regular or routine human intervention; (c) a Second Schedule requirement or restriction.

*Source note: LT-5 p23. Conflict: Cyril-Exam LT §3.2 gives the pre-statute three factors; the PWA test is followed.*

### clk-m-1-44 — Second Schedule and the presumption (s 6(3)–(4))
*Keywords: Second Schedule, price negotiation, own clientele, incentives, penalties, presumption, app or website, PWA s 6(3), s 6(4)*

**End point:** Second Schedule restrictions cover how, when or how well work is done, price negotiation, building one's own clientele, hours or number of tasks, and systematic incentives or penalties; requirements under written law don't count, and control is presumed from a platform work agreement plus tasks accessed through the operator's app or website.

*Source note: LT-5 p24-25*

### clk-m-1-45 — Escaping the Act
*Keywords: rebut presumption, ride-hailing, delivery*

**End point:** The Act mainly targets ride-hailing and delivery; a platform escapes only by showing no data use, regular human intervention, or no Second Schedule restriction — "surprising if it happens in practice".

*Source note: LT-5 p26*

## 1.VIII Platform defamation

- **Who published the defamatory material?**
  - Sharing a link without comment is publication (*Lee Hsien Loong v Leong Sze Hian*) → [1-46](#clk-m-1-46)
  - The page owner publishes users' comments (*Fairfax Media v Voller*) → [1-47](#clk-m-1-47)
  - Businesses running pages risk liability → [1-48](#clk-m-1-48)
- **Is the platform itself liable?**
  - Open: adoption, acquiescence once notified, architecture; Singapore has no s 230 equivalent → [1-49](#clk-m-1-49)
- **Online defamation across borders: where is it published, and whose law applies? (*Dow Jones v Gutnick*)**
  - Published where downloaded and read, so in Victoria; Victoria not a clearly inappropriate forum; Gary Chan proposes tiered connecting factors → [1-63](#clk-m-1-63)

### clk-m-1-46 — Lee Hsien Loong v Leong Sze Hian
*Keywords: Lee Hsien Loong v Leong Sze Hian, sharing a link, publication, Facebook*

**End point:** Sharing a link to a defamatory article on Facebook, without comment, was publication of the article; platform liability was not in issue.

*Source note: LT-5 p29-30*

### clk-m-1-47 — Fairfax Media v Voller
*Keywords: Fairfax v Voller, page owner, publisher, intentional participation, comments*

**End point:** Fairfax, the page owner — not Facebook — published users' defamatory comments: intentional participation means voluntary and active, regardless of knowledge of the content ([62], [66]); publication occurred when comments were accessed ([98]).

*Source note: LT-5 p31-35. Conflict: Cyril-Exam LT §3.3 says "platforms (or business users)" can be liable; the slide says Fairfax, not Facebook.*

### clk-m-1-48 — Liability of business users
*Keywords: business users, commercial purpose, page operators*

**End point:** Businesses that run pages on platforms for commercial readership can be liable for others' posts.

*Source note: LT-5 p35-36*

### clk-m-1-49 — Is the platform liable?
*Keywords: platform liability, adoption, acquiescence, section 230, no Singapore case*

**End point:** Open questions are adoption, acquiescence once notified, and how far the architecture facilitates the defamatory meaning; Singapore has no s 230 equivalent and no platform-defamation case.

*Source note: LT-5 p30; LT-CS2n p2-3*

### clk-m-1-63 — Dow Jones v Gutnick: where online defamation happens
*Keywords: Dow Jones v Gutnick, Gutnick v Jones, Barron's Online, internet defamation, place of publication, downloaded, comprehended by the reader, server in New Jersey, single publication rule rejected, multiple publication, lex loci delicti, choice of law, forum non conveniens, Victoria, Gary Chan, habitual residence, connecting factors*

**End point:** A Barron's Online article written in New York and hosted on New Jersey servers defamed a Victorian resident who sued in Victoria only for his reputation there. The High Court of Australia held that defamation occurs where the material is downloaded and comprehended, so it was published in Victoria. Victoria was not a clearly inappropriate forum and its law applied. The US single publication rule (publication at the server) was rejected. Gary Chan notes that the place of publication can produce several applicable laws, and proposes tiered choice-of-law rules built on the convergence of the place of publication, the place of damage to reputation and the plaintiff's habitual residence.

*Source note: Gary Chan Kok Yew, "Internet Defamation and Choice of Law in Dow Jones & Company Inc v Gutnick" [2003] Sing JLS 483, `Bar Exam/Modules/Contemporary Legal Knowledge & Practice/2. Law and Technology/Reading List/Internet_Defamation_and_Choice_of_Law in_Dow_Jones_and_Company_Inc. v Gutnick.pdf` p3-7 (facts, jurisdiction), p19-21 (place of publication), p35-37 (recommended rules); LT-1 (teaser slide "Gutnick v Jones"). The CS1 notes make Chan an "optional skim". For Singapore choice of law in tort see clk-m-3-6 to 3-11.*

## 1.IX Blockchain and crypto assets

- **What was blockchain designed for?**
  - To solve double-spending without a trusted third party ("trust in code") → [1-50](#clk-m-1-50)
- **How does it work?**
  - Hash-chained blocks, proof of work, the longest chain wins; transactions are public → [1-51](#clk-m-1-51)
  - Is it tamper-proof? No, only probabilistically: a 51% attack can succeed → [1-52](#clk-m-1-52)
  - Uses (tokens, NFTs, smart contracts) and proof of stake → [1-53](#clk-m-1-53)
- **Are crypto assets property?**
  - Yes: a thing in action (*ByBit Fintech v Ho Kai Xin*) → [1-54](#clk-m-1-54)

### clk-m-1-50 — What blockchain was designed for
*Keywords: blockchain, double-spending problem, peer-to-peer, timestamp server, trust in code, trusted third party*

**End point:** Its original purpose was to solve double-spending with a peer-to-peer distributed timestamp server — storing data securely without trusted third parties, replacing trust in banks with "trust in code".

*Source note: LT-6 p4, p9-10, p24; SampleQs p95 Q9, key p130*

### clk-m-1-51 — Hashing and proof of work
*Keywords: hash, SHA-256, proof of work, consensus mechanism, longest chain*

**End point:** Blocks are hash-chained and agreed by consensus; under proof of work miners find a hash meeting a target, altering a block means redoing it and all later blocks, and the longest chain wins. Transactions are public — hashing is not for secrecy.

*Source note: LT-6 p16-19*

### clk-m-1-52 — Tamper-resistance is probabilistic
*Keywords: tamper-proof, probabilistic, 51% attack, Ethereum Classic*

**End point:** Tamper-resistance is probabilistic, not absolute: 50%+ of computing power, an easy puzzle, few blocks or luck can let an attacker win (Ethereum Classic suffered a 51% attack).

*Source note: LT-6 p23*

### clk-m-1-53 — Uses and other consensus methods
*Keywords: tokens, NFTs, land registers, smart contracts, proof of stake, slashing*

**End point:** Uses include tokens, NFTs, land registers and smart contracts — Bitcoin is one "app"; other consensus methods include proof of stake (deposit and slashing).

*Source note: LT-6 p21, p24-25*

### clk-m-1-54 — ByBit Fintech v Ho Kai Xin
*Keywords: ByBit v Ho Kai Xin, crypto asset, thing in action, property, Ainsworth*

**End point:** Crypto assets satisfy the Ainsworth criteria and are a thing in action — an incorporeal right of property enforceable in court ([31]-[36]).

*Source note: LT-6 p25-26*

## 1.X Artificial intelligence

- **How does AI work?**
  - Defining AI: Turing, Russell and Norvig → [1-55](#clk-m-1-55)
  - Symbolic (explicit rules) versus statistical (patterns in data) → [1-56](#clk-m-1-56)
  - "Learning" means adjusting weights → [1-57](#clk-m-1-57)
  - Language models predict words; generative AI is a subset of predictive AI → [1-58](#clk-m-1-58)
- **Can AI be responsible?**
  - Attributing intent to AI is the Fundamental Attribution Error; look to the people → [1-59](#clk-m-1-59)
  - DABUS as inventor failed everywhere; "neurons" and "learning" are metaphors → [1-60](#clk-m-1-60)
  - "It is just maths", but that does not mean it is harmless → [1-61](#clk-m-1-61)

### clk-m-1-55 — Defining AI
*Keywords: Turing test, imitation game, Russell and Norvig, thinking humanly, acting rationally*

**End point:** Turing replaced "can machines think?" with the imitation game; Russell and Norvig classify AI as thinking or acting, humanly or rationally.

*Source note: LT-7 p5-6*

### clk-m-1-56 — Symbolic versus statistical AI
*Keywords: symbolic AI, statistical AI, rules-based, machine learning, expert system, Susskind*

**End point:** Symbolic AI specifies explicit rules and knowledge bases (e.g. Susskind's divorce expert system); statistical AI (machine learning) finds implicit patterns in data, because writing every rule is too costly.

*Source note: LT-7 p7-12; SampleQs p93 Q3, key p130*

### clk-m-1-57 — What learning means
*Keywords: machine learning, learning, coefficients, weights, explainable, regression, Vasentha*

**End point:** "Learning" is adjusting numerical coefficients (weights) in a model until the fit stabilises; simple models are "very explainable" (e.g. a sentencing regression on Vasentha).

*Source note: LT-7 p13-19; SampleQs p96 Q10, key p130*

### clk-m-1-58 — Language models and generative AI
*Keywords: language model, large language model, LLM, parameters, generative AI, predictive AI, GPT*

**End point:** A language model is trained to predict deleted words from a text corpus; "large" means a large number of parameters (GPT-3.5: 175 billion); generative AI is a subset of predictive AI and is not new.

*Source note: LT-7 p22-25; SampleQs p94 Q4, key p130. Conflict: Cyril-Exam LT §5.2.3 gives a different timeline (GPT-3 in 2020, GPT-5); the slide's timeline is followed.*

### clk-m-1-59 — Legal dispositionism
*Keywords: legal dispositionism, Soh, Fundamental Attribution Error, situation, missing person problem*

**End point:** Attributing intentions to AI is the Fundamental Attribution Error (Ross 1977): look to the situation — regulators, makers, programmers, operators and users; the law's "missing person problem" is that it assumes a person acts.

*Source note: LT-7 p29-31; LT-Plan p5 (author: Soh)*

### clk-m-1-60 — DABUS and metaphors
*Keywords: DABUS, Thaler, AI inventor, Thaler v Perlmutter, android fallacy, anthropomorphic bias*

**End point:** Claims that the AI DABUS should be named inventor (and the related copyright claim in Thaler v Perlmutter) failed everywhere; words like "neurons" and "learning" are metaphors, and anthropomorphism misleads.

*Source note: LT-7 p32-33*

### clk-m-1-61 — It is just maths
*Keywords: matrix multiplication, just maths*

**End point:** All of these systems are matrix maths, but "it is just maths" does not mean there is nothing to worry about.

*Source note: LT-7 p26*

## 2.I Civil law system and sources

- **What are the sources of law in a civil law system?**
  - Codes: the main source and first port of call → [2-1](#clk-m-2-1)
  - Judicial decisions: no stare decisis; uniform case law is persuasive (jurisprudence constante) → [2-2](#clk-m-2-2)
  - Doctrine (academic writing): a formally recognised source → [2-3](#clk-m-2-3)
- **Which code?**
  - Indonesia: the 1847 Dutch Civil Code, four books; overridden by new statutes rather than amended → [2-4](#clk-m-2-4)
  - Indonesia: "Law No x of year"; implementing regulations; contracts without an Indonesian version (Language Law) → [2-5](#clk-m-2-5)
  - Thailand: the CCC, on a German model, six books → [2-6](#clk-m-2-6)
  - What the Obligations book covers → [2-7](#clk-m-2-7)

### clk-m-2-1 — Codification
*Keywords: civil law, codified, civil code, first port of call, comprehensive*

**End point:** Civil law systems are codified: the code is the main source and the first port of call, and codes are intended to be comprehensive; case law does not carry the same weight as at common law.

*Source note: Cmp-1 p3; Cmp-1T p2-4*

### clk-m-2-2 — Judicial decisions — no stare decisis
*Keywords: stare decisis, precedent, jurisprudence constante, persuasive*

**End point:** There is no stare decisis and no single decision binds; once case law is uniform it is persuasive (jurisprudence constante), and conflicting decisions carry no weight.

*Source note: Cmp-1 p15; Cmp-1T p9; SampleQs p99 Q6, key p130*

### clk-m-2-3 — Doctrine (academic writing)
*Keywords: doctrine, academic writing, legal scholarship, Dutch scholars*

**End point:** Academic writing ("doctrine") is a significant, formally recognised source that shapes how codes are read; in Indonesia, Dutch scholars' readings of the 1847 Code are a source of law.

*Source note: Cmp-1T p4; SampleQs p99 Q5, key p130*

### clk-m-2-4 — The Indonesian Civil Code
*Keywords: Indonesian Civil Code, KUHPerdata, 1847, Dutch, four books, Arts 1233-1456*

**End point:** The Dutch Civil Code has applied in Indonesia since 1847; its authoritative text is Dutch, so it is rarely amended and is overridden instead by new statutes (1960 agrarian, 1974 marriage law). It has four books: persons; goods; obligations and contracts (Arts 1233-1456); evidence and prescription.

*Source note: Cmp-1 p6; Cmp-1T p3-4*

### clk-m-2-5 — Indonesian statutes and implementing regulations
*Keywords: implementing regulation, Law No, toll road law, Language Law 24/2009, bad faith, Supreme Court circular*

**End point:** Laws are cited "Law No x of year" and need implementing regulations, which may come late. Under the Language Law (24/2009) and a 2023 Supreme Court circular, a contract without an Indonesian version is annullable only if the omission was not in good faith.

*Source note: Cmp-1 p7-9; Cmp-1T p4-6. Conflict: Cyril-Exam CMP §1.2.2 states the bad-faith rule the other way round; the transcript is followed.*

### clk-m-2-6 — The Thai Civil and Commercial Code
*Keywords: Thai Civil and Commercial Code, CCC, six books, German model, 2017 Constitution*

**End point:** The 2017 Constitution is supreme and statute is the main source; the CCC combines civil and commercial law on a German model in six books: general principles; obligations (torts in Title 5); specific contracts; property; family; succession.

*Source note: Cmp-1 p11-12; Cmp-1T p6-8*

### clk-m-2-7 — What the Obligations book covers
*Keywords: obligations, book of obligations, contract, tort, statutory claims*

**End point:** The Obligations book covers obligations from contract, obligations arising from law and relationships, and statutory and tort claims.

*Source note: Cmp-1 p11; SampleQs p98 Q4, key p130*

## 2.II Contract formation and interpretation

- **Is there a valid contract?**
  - Consent, capacity, lawful and certain content; no consideration needed → [2-8](#clk-m-2-8)
- **Indonesia: how is a contract interpreted?**
  - Clear wording: no departing from it (Art 1342) → [2-9](#clk-m-2-9)
  - Unclear wording: parties' intent, enforceable meaning, custom, the whole agreement (Arts 1343–1351) → [2-10](#clk-m-2-10)
  - In doubt: against the party who requested it (Art 1349) → [2-11](#clk-m-2-11)
- **Thailand: how is a contract interpreted?**
  - Real intention over literal words (s 171); good faith and custom (s 368) → [2-12](#clk-m-2-12)
  - Gap-fillers: words over figures, lowest amount, the Thai text prevails (ss 10–14) → [2-13](#clk-m-2-13)
  - Unexpressed intention does not count; implied terms do → [2-14](#clk-m-2-14)
  - Pre-contract negotiations: admitted much more readily than at common law → [2-15](#clk-m-2-15)
- **Can SMM invalidate the contract? Defects of consent (fact pattern Q1(b))**
  - Indonesia: error as to the substance, duress, or fraud (Arts 1321-1328); the claim to nullify lies for 5 years (Arts 1449, 1454) → [2-46](#clk-m-2-46)
  - Thailand: mistake (ss 156-158), fraud (s 159), and intentional silence deemed fraud (s 162); avoid within 1 year of when ratification became possible (s 181); exclusion of liability for fraud is void (s 373) → [2-47](#clk-m-2-47)

### clk-m-2-8 — Formation — no consideration
*Keywords: formation, consent, capacity, lawful and certain content, consideration, public order*

**End point:** A civil-law contract needs consent, capacity (for juristic persons, limited to acts useful for their purpose) and lawful, certain content not contrary to public order; consideration is not required.

*Source note: Cmp-2 p2; Cmp-2T p1; SampleQs p100 Q9, key p130*

### clk-m-2-9 — Clear wording — Art 1342
*Keywords: Article 1342, clear wording, plain meaning, Indonesian Civil Code*

**End point:** If the wording of an agreement is clear, one may not deviate from it by interpretation.

*Source note: Cmp-2 p3*

### clk-m-2-10 — Canons for unclear wording — Arts 1343–1351
*Keywords: Article 1343, intent of the parties, enforceable meaning, local custom, read as a whole, Articles 1344-1351*

**End point:** Only where wording is unclear: seek the parties' intent over the literal sense (1343), prefer the enforceable meaning (1344), the meaning suiting the agreement's nature (1345), local custom (1346), implied customary terms (1347), and read the agreement as a whole (1348); general words cover what was intended (1350) and an example does not restrict (1351).

*Source note: Cmp-2 p3; Cmp-2T p2. Conflict: the transcript applies Art 1343 to clear words; the slide says it applies where wording is open to several interpretations, and the slide is followed.*

### clk-m-2-11 — In doubt, against the requester — Art 1349
*Keywords: Article 1349, contra proferentem, party requesting the agreement*

**End point:** In doubt, the agreement is interpreted against the party who requested it and in favour of the party who bound himself.

*Source note: Cmp-2 p3*

### clk-m-2-12 — Real intention and custom — ss 171 and 368
*Keywords: Thai CCC s 171, s 368, real intention, good faith, custom, clear terms*

**End point:** Seek the real intention rather than the literal words (s 171: "investment" contracts that were really loans, SC 11107/2555), and interpret as good faith requires, considering custom (s 368: jute packing, SC 1375/2505); a clear written term needs no outside evidence (SC 2210/2526).

*Source note: Cmp-2 p4; Cmp-2T p2-3*

### clk-m-2-13 — Thai gap-fillers — ss 10–14
*Keywords: Thai CCC s 10, s 11, s 12, s 13, s 14, words over figures, lowest amount, Thai text prevails*

**End point:** Prefer the meaning that gives effect (s 10); in doubt, for the obligor (s 11); words prevail over figures (s 12); the lowest amount governs (s 13); if language versions differ and intent is unclear, the Thai text prevails (s 14).

*Source note: Cmp-2 p5*

### clk-m-2-14 — Unexpressed intention and implied terms
*Keywords: unexpressed intention, implied terms, subjective, objective*

**End point:** An unexpressed intention cannot form a contract or part of one, but terms implied in fact and in law are recognised.

*Source note: Cmp-2T p4*

### clk-m-2-15 — Pre-contract negotiations
*Keywords: pre-contract negotiations, subjective intention, exclusionary rule*

**End point:** Civil law is much more expansive in admitting negotiations to interpret a contract (though not conclusive), moving towards the parties' subjective intention; common law generally excludes them.

*Source note: Cmp-2 p6; Cmp-2T p5*

### clk-m-2-46 — Indonesia: defects of consent (Arts 1321-1328, 1449-1454)
*Keywords: defects of consent, wilsgebreken, error, mistake, dwaling, duress, dwang, fraud, bedrog, nullification, voidable, substance of the subject matter, identity of the person, fraud must be proven, five years, restitution, Indonesian Civil Code Art 1320, Art 1321, Art 1322, Art 1323, Art 1328, Art 1449, Art 1452, Art 1454*

**End point:** Consent is defective if given by mistake or obtained by duress or fraud (Art 1321). Mistake counts only if it goes to the substance of the subject matter, or to the identity of the other party where the contract was made for that person (Art 1322). Fraud must be such that the other party would never have contracted without it, and it must be proved, not presumed (Art 1328). The contract is not void automatically: the affected party must claim nullification (Art 1449), generally within five years (Art 1454), and the parties are restored to their prior position (Art 1452).

> **Indonesian Civil Code**
> - Art 1321: no valid consent if given by mistake or obtained by duress or fraud.
> - Art 1322: mistake invalidates only if it concerns the substance of the subject matter; a mistake as to the person invalidates only if the contract was concluded for that specific person.
> - Arts 1323-1327: duress (including by a third party, or against a spouse or relatives) is a ground for nullification; it is lost if the contract is affirmed after the duress ends.
> - Art 1328: fraud is a ground only if, without the deceit, the other party would clearly never have contracted; fraud is not presumed and must be proven.
> - Art 1449: a contract made under duress, error or fraud gives a legal claim to nullify it.
> - Art 1452: nullification restores the parties to their pre-contract position; Art 1453: costs, damages and interest may also be awarded.
> - Art 1454: the claim must be brought within five years, unless a shorter period applies.
> - Apply (fact pattern): mere silence about Ms Moreau's plans would have to amount to deceit without which SMM would never have contracted, proved by SMM (Art 1328); the contract here is governed by Thai law (cl 17.1), so see clk-m-2-47.

*Source note: Indonesian Civil Code (trilingual), `study/clk-m/authorities/2 Comparative/Indonesian Civil Code (trilingual).pdf` p291-292 (Arts 1321-1328), p315 (Arts 1449-1454). The course slides do not cover defects of consent [Cmp-2]; the fact pattern raises the issue [Fact p3 Q1(b)]. Outside the slides.*

### clk-m-2-47 — Thailand: mistake, fraud and intentional silence (CCC ss 156-163, 181, 373)
*Keywords: mistake as to an essential element, void, mistake as to quality of the person, voidable, gross negligence, fraud, voidable, incidental fraud, compensation only, intentional silence, non-disclosure, bilateral juristic act, deemed fraud, ratification, one year, ten years, exclusion of liability for fraud void, entire agreement, non-reliance clause, clause 15, Thai Civil and Commercial Code s 156, s 157, s 158, s 159, s 161, s 162, s 163, s 181, s 373*

**End point:** Under Thai law a declaration made under a mistake as to an essential element is void (s 156), and one made under a mistake as to an essential quality of the person is voidable (s 157), unless the mistaken party was grossly negligent (s 158). A declaration induced by fraud is voidable only if, without the fraud, the act would not have been made (s 159); incidental fraud gives only compensation (s 161). In a bilateral act, intentional silence about a fact the other party does not know is deemed fraud if, without it, the act would not have been made (s 162). A voidable act must be avoided within one year of when it could be ratified and within ten years of the act (s 181). An advance agreement excluding liability for one's own fraud or gross negligence is void (s 373).

> **Thai CCC**
> - s 156: mistake as to an essential element (the character of the act, the person who is party, the property) makes the declaration void.
> - s 157: mistake as to a quality of the person, essential in ordinary dealings and without which the act would not have been made: voidable.
> - s 158: no reliance on ss 156-157 if the mistake was due to one's own gross negligence.
> - s 159: fraud makes the declaration voidable only if, without it, the act would not have been made; third-party fraud only if the other party knew or ought to have known.
> - s 161: incidental fraud (only more onerous terms): compensation only.
> - s 162: intentional silence by one party about a fact or quality the other does not know is deemed fraud, if it is proved that without it the act would not have been made.
> - s 163: if both acted fraudulently, neither can rely on it.
> - s 181: a voidable act cannot be avoided later than one year from when ratification could have been made, or ten years from the act.
> - s 373: an agreement made in advance exempting a debtor from liability for its own fraud or gross negligence is void.
> - Apply (fact pattern, Thai law under cl 17.1): SP's intentional silence about Ms Moreau's planned departure is deemed fraud under s 162 only if SMM proves it would not have contracted without it; Ms Ahmad's evidence that Moreau was not "essential" goes to that. If it was incidental, SMM gets compensation only (s 161). On the best reading of s 373, the cl 15.2-15.3 non-reliance and exclusion wording cannot protect SP against liability for its own fraud.

*Source note: Thai Civil and Commercial Code Book 1 (English translation, ThaiLaws.com 2008 edition) ss 156-163 p23-25, s 181 p26; s 373 from thailawonline.com/thai-civil-code/section-373 (unofficial plain-English summary), both read 19 Nov 2026. Outside the course slides and library; the fact pattern raises the issue [Fact p3 Q1(b)]. Applying s 373 to cl 15 is this pack's reading; the course materials do not decide it. Good faith and abuse of rights: clk-m-2-16 to 2-19.*

## 2.III Good faith (Thailand)

- **What role does good faith play?**
  - Presumed (s 6) → [2-16](#clk-m-2-16)
  - Interpreting terms (s 368) → [2-17](#clk-m-2-17)
  - Pervasive: performance too, and can override express terms → [2-18](#clk-m-2-18)
  - Exercising a right only to injure another is a wrongful act (abuse of rights, s 421) → [2-19](#clk-m-2-19)

### clk-m-2-16 — Good faith is presumed — s 6
*Keywords: Thai CCC s 6, presumption of good faith*

**End point:** A person is presumed to act in good faith (SC 9158/2539).

*Source note: Cmp-2 p7*

### clk-m-2-17 — Interpreting by good faith — s 368
*Keywords: Thai CCC s 368, good faith, custom, ordinary prudence*

**End point:** Contracts are interpreted as good faith requires, considering custom; absent custom, as a person of ordinary prudence in good faith would (SC 478/2544: a right to "use the path" includes vehicles).

*Source note: Cmp-2 p7; Cmp-2T p6*

### clk-m-2-18 — Good faith is pervasive
*Keywords: good faith, performance, override express terms, implied duty, Thai CCC s 5*

**End point:** Good faith governs both interpretation and performance, in contract and tort, and can override express terms or imply a duty; s 5 (good faith in exercising rights) appears only in the optional Pongsapan reading.

*Source note: Cmp-2T p6-7; Pongsapan p17*

### clk-m-2-19 — Abuse of rights — s 421
*Keywords: Thai CCC s 421, abuse of rights, solely to injure, wrongful act*

**End point:** Exercising a right whose only purpose is to injure another is a wrongful act (supermarket coupons, SC 6599/2559); the actor must aim to cause unilateral injury (SC 1992/2538).

*Source note: Cmp-2 p8; Cmp-3 p4; SampleQs p100 Q8, key p130*

## 2.IV Contract remedies and election

- **Which remedy?**
  - Performance: specific performance is preferred → [2-20](#clk-m-2-20)
  - Termination: needs a material breach → [2-21](#clk-m-2-21)
  - Damages: any breach; no punitive damages in most systems → [2-22](#clk-m-2-22)
- **What conditions and limits apply?**
  - Contributory fault versus mitigation; no general duty to mitigate in France → [2-23](#clk-m-2-23)
  - Notice of default and a last chance first → [2-24](#clk-m-2-24)
  - Election: renounce performance to claim damages; silence means insisting on performance → [2-25](#clk-m-2-25)
- **Can SMM simply terminate on its own? Indonesia (fact pattern Q1(a))**
  - No: a breach is an implied dissolving condition, but dissolution must be requested from the court (Art 1266) → [2-48](#clk-m-2-48)

### clk-m-2-20 — Specific performance is preferred
*Keywords: specific performance, impossible, damages adequate*

**End point:** Civil law prefers specific performance (France, Germany and French-influenced systems refuse it only if performance is impossible); common law makes damages the rule and specific performance the exception.

*Source note: Cmp-2 p9; Cmp-2T p8*

### clk-m-2-21 — Termination needs a material breach
*Keywords: termination, material breach, fundamental breach*

**End point:** Most civil-law systems require a material or fundamental breach to terminate.

*Source note: Cmp-2T p9. Conflict: Cyril-Exam CMP §2.5 says a fundamental breach is needed for damages too; the transcript limits it to termination (and damages in lieu of performance).*

### clk-m-2-22 — Damages
*Keywords: damages, damages in lieu of performance, punitive damages, lost profits, consequential loss*

**End point:** Damages are available for any breach, except damages in lieu of performance, which are tantamount to termination (Germany); punitive damages are absent in most civil-law systems; lost profits are recoverable; common law recovers indirect loss only if both parties contemplated it.

*Source note: Cmp-2T p7-9*

### clk-m-2-23 — Reducing damages — contributory fault and mitigation
*Keywords: contributory fault, mitigation, benefits from breach, France*

**End point:** Contributory fault (conduct before or at the damage) differs from mitigation (conduct after awareness), and benefits from the breach reduce recovery; France has no general duty to mitigate in tort and only exceptionally in contract, whereas common law requires mitigation.

*Source note: Cmp-2T p9*

### clk-m-2-24 — Notice and a last chance
*Keywords: notice of default, last chance, formal notice, France*

**End point:** Civil law commonly requires notifying the breach or requesting performance to give a last chance; in France there are no damages until the defaulting party is put on formal notice, even with a fixed deadline.

*Source note: Cmp-2T p10*

### clk-m-2-25 — Election of remedies
*Keywords: election of remedies, renounce performance, positive damages, negative damages, Turkish Code of Obligations*

**End point:** The code prescribes the relief after termination, and the obligee must immediately renounce performance to claim positive damages (as if performed) or negative damages (as if never made); staying silent means being deemed to insist on performance, with only delay damages (Turkish case study; Indonesian and Thai codes are "similar").

*Source note: Cmp-2 p9-11; Cmp-2T p10-11; SampleQs p101 Q10, key p130*

### clk-m-2-48 — Indonesia: termination must be requested from the court (Art 1266)
*Keywords: termination, dissolution, unilateral termination, implied dissolving condition, reciprocal agreement, non-performance, court, judge, grace period, one month, Indonesian Civil Code Art 1266*

**End point:** In a reciprocal contract, non-performance is deemed a dissolving condition, but the contract is not void by law: dissolution must be requested from the court, even if the contract expressly provides for termination on non-performance (Art 1266). If the contract has no termination clause, the judge may give the defendant up to one month to perform. So under Indonesian law SMM cannot terminate unilaterally; it must go to court (or, with an arbitration clause, the tribunal; clk-m-2-49).

> **Indonesian Civil Code Art 1266**
> - A dissolving condition is deemed included in reciprocal agreements where one party fails to perform.
> - The agreement is not void by law; dissolution must be requested from the court.
> - The request is needed even if the agreement states the conditions of dissolution on non-performance.
> - If it does not, the judge may, at the defendant's request, fix a period of at most one month to perform.

*Source note: Indonesian Civil Code (trilingual), `study/clk-m/authorities/2 Comparative/Indonesian Civil Code (trilingual).pdf` p281 (Art 1266). Outside the course slides; the fact pattern asks it [Fact p3 Q1(a)]. Material breach generally: clk-m-2-21.*

## 2.V Delict (non-contractual claims)

- **Indonesia: what is an unlawful act? (Art 1365)**
  - Elements: unlawful act, fault, damage, causation → [2-26](#clk-m-2-26)
  - Heads of compensation → [2-27](#clk-m-2-27)
- **Thailand: what is a wrongful act?**
  - Wilful or negligent unlawful injury (s 420) → [2-28](#clk-m-2-28)
  - Liability for others: employer, principal, vehicle owner (ss 425–437) → [2-29](#clk-m-2-29)
  - Compensation: fixed by the court (s 438) → [2-30](#clk-m-2-30)
  - Time limit: 1 year from knowledge or 10 years from the act (s 448) → [2-31](#clk-m-2-31)

### clk-m-2-26 — Article 1365 — the rule and its elements
*Keywords: Article 1365, unlawful act, fault, damage, causation, immaterial damage*

**End point:** Every unlawful act causing damage obliges the wrongdoer to compensate; the elements are an unlawful act, fault (intent or negligence), damage (material or immaterial) and causation.

*Source note: Cmp-3 p2*

### clk-m-2-27 — Article 1365 — heads of compensation
*Keywords: compensation, repair, restoration costs, suffering, reputation*

**End point:** Compensation can be money for lost assets, repair, restoration costs, and compensation for suffering or harm to reputation.

*Source note: Cmp-3 p3; SampleQs p100 Q7, key p130*

### clk-m-2-28 — Wrongful act — s 420
*Keywords: Thai CCC s 420, wrongful act, wilfully or negligently, life, body, health, liberty, property*

**End point:** A person who wilfully or negligently and unlawfully injures the life, body, health, liberty, property or any right of another commits a wrongful act and must compensate.

*Source note: Cmp-3 p4; Cmp-1 p13*

### clk-m-2-29 — Vicarious liability — ss 425–437
*Keywords: Thai CCC s 425, s 427, s 428, s 437, employer, agent, vehicles*

**End point:** An employer is jointly liable for an employee's acts in the course of employment (s 425); ss 427-428 cover principals and contractors; s 437 makes vehicle owners or controllers liable unless force majeure or the victim's fault.

*Source note: Cmp-1 p13*

### clk-m-2-30 — Compensation — s 438
*Keywords: Thai CCC s 438, compensation, restitution, exhaustive*

**End point:** The court fixes the manner and extent of compensation, including restitution of property or its value; the forms of compensation are exhaustively set out in the CCC.

*Source note: Cmp-1 p13; Cmp-1T p8. Conflict: Cyril-Exam CMP §3.3 says the CCC gives only broad principles; the lecturer says compensation is exhaustively set out.*

### clk-m-2-31 — Prescription — s 448
*Keywords: Thai CCC s 448, prescription, limitation, 1 year, 10 years, knowledge*

**End point:** A tort claim prescribes 1 year from when the injured person knew of the act and of the person liable, or 10 years from the act, whichever is first; a longer criminal prescription applies if the act is also a crime.

*Source note: Cmp-1 p13; Cmp-1T p8-9. Conflict: Cyril-Exam CMP §3.3 runs the year from the act; the module runs it from knowledge.*

## 2.VI Civil court jurisdiction (competence)

- **Indonesia: which court?**
  - Relative competence: geographical; the defendant's domicile; raised by exception → [2-32](#clk-m-2-32)
  - Absolute competence: subject matter; can be raised any time → [2-33](#clk-m-2-33)
  - International arbitral awards: district courts register, set aside and enforce only → [2-34](#clk-m-2-34)
- **Thailand: which court?**
  - Where the cause arose or the defendant is domiciled (CPC s 4); the specialised courts → [2-35](#clk-m-2-35)
- **The contract has an arbitration clause: can the Jakarta court hear the claim, or SP's counterclaim? (fact pattern Q4(a)-(b))**
  - No: the District Court has no jurisdiction over disputes between parties bound by an arbitration agreement (Arbitration Law Arts 3, 11) → [2-49](#clk-m-2-49)
- **The claim names the wrong party: what should the defendant do? (Q4(a))**
  - Raise an exception (error in persona) asking the court to declare the claim inadmissible, alongside the competence exception → [2-50](#clk-m-2-50)
- **Can SP recover its legal costs? (Q4(d))**
  - Court costs follow the event; lawyers' fees are generally not recoverable in Indonesian courts → [2-51](#clk-m-2-51)

### clk-m-2-32 — Relative competence and the exception
*Keywords: relative competence, domicile, HIR Art 118(1), exception, decided before the merits*

**End point:** Relative competence is geographical: sue in the district court of the defendant's domicile, or actual residence if unknown (Art 118(1) HIR); the defendant may file an exception to this competence, which must be decided before the merits.

*Source note: Cmp-4 p2-4. Conflict: Cyril-Exam CMP §4.1.3 ties "decided first" to the absolute-competence exception (Art 134 HIR); the slide follows the relative-competence rule.*

### clk-m-2-33 — Absolute competence
*Keywords: absolute competence, subject matter, any time, own motion*

**End point:** Absolute competence is subject-matter jurisdiction; its absence can be raised at any time and the court must recognise it of its own motion.

*Source note: Cmp-4 p2, p4*

### clk-m-2-34 — District courts and international arbitral awards
*Keywords: Arbitration Law, international arbitral award, registration, setting aside, enforcement*

**End point:** Indonesian district courts may only register, set aside and enforce international arbitral awards.

*Source note: Cmp-4 p4. Conflict: Cyril-Exam CMP §4.1.3 says the court can only enforce or refuse enforcement; the slide includes setting aside.*

### clk-m-2-35 — Thai courts — s 4 and the specialised courts
*Keywords: Thai Civil Procedure Code s 4, specialised courts, Central Labour Court, IP and International Trade Court, Tax Court, Bankruptcy Court*

**End point:** Sue where the cause of action arose or the defendant is domiciled (CPC s 4); four specialised first-instance courts have nationwide jurisdiction (Labour, with 8 regional branches; IP and International Trade; Tax; Bankruptcy), with most appeals going straight to the Supreme Court.

*Source note: Cmp-4 p5*

### clk-m-2-49 — Indonesia: an arbitration clause ousts the District Court (Arbitration Law Arts 3, 11)
*Keywords: arbitration agreement, arbitration clause, District Court has no jurisdiction, absolute competence, eliminate the right to go to court, refuse and not interfere, counterclaim, exception, Law No 30 of 1999, Arbitration Law Art 3, Art 11, HK-seated ICC arbitration*

**End point:** The District Court has no jurisdiction to try disputes between parties bound by an arbitration agreement (Art 3), and a written arbitration agreement removes the parties' right to take the dispute to the District Court, which must refuse to intervene (Art 11). On the fact pattern, cl 18 (HK-seated ICC arbitration) means the Central Jakarta District Court should decline the claim. SP should raise the arbitration clause as an absolute-competence exception (clk-m-2-33) rather than counterclaim for the fees there. A counterclaim also falls within cl 18, so the court can refuse to award it even if the contract is valid; SP should claim the fees in the arbitration.

> **Law No 30 of 1999 on Arbitration and ADR**
> - Art 3: the District Court has no jurisdiction to try disputes between parties bound by an arbitration agreement.
> - Art 11(1): a written arbitration agreement eliminates the parties' right to resolve the dispute through the District Court.
> - Art 11(2): the District Court must refuse, and not interfere in, a dispute that has been determined by arbitration, except where the Act provides.
> - The courts' role is limited to registering, setting aside and enforcing awards (clk-m-2-34).

*Source note: Law No 30 of 1999 on Arbitration and Alternative Dispute Resolution, Arts 3, 11 (English translation, acerislaw.com copy; official translation also at peraturan.go.id), read 19 Nov 2026. Outside the course slides; Cmp-4 p4 states only the courts' limited role over awards. Applying it to the fact pattern [Fact p3 Q4(a)-(b), cl 18] is this pack's reading; another basis for refusing the fees would be good faith or abuse of rights (clk-m-2-18, 2-19).*

### clk-m-2-50 — Indonesia: the wrong party named in the claim (error in persona)
*Keywords: wrong party, wrongly identified defendant, error in persona, exceptio in persona, exception, eksepsi, claim inadmissible, niet ontvankelijk verklaard, tidak dapat diterima, HIR Art 136, decided with the merits*

**End point:** A claim that names the wrong defendant is defective in form. The defendant raises an error in persona exception, asking the court to declare the claim inadmissible (niet ontvankelijk verklaard), which ends the case without deciding the merits. Exceptions other than competence are decided together with the merits (HIR Art 136), whereas a competence exception is decided first (clk-m-2-32, 2-33). On the fact pattern SP should raise both the arbitration clause (absolute competence; clk-m-2-49) and the error in persona. The wrong naming alone does not make the court lack jurisdiction.

*Source note: Outside the course materials. Hukumonline, "Tentang Error in Persona dan Error in Objecto" (klinik, read 19 Nov 2026), citing M Yahya Harahap; Leks & Co blog on formal exceptions and HIR Art 136 (read 19 Nov 2026). These are secondary sources: no statute or Supreme Court decision was located. Best-supported position, to be weighed accordingly. The fact pattern asks it [Fact p3 Q4(a)].*

### clk-m-2-51 — Indonesia: costs (court costs versus lawyers' fees)
*Keywords: legal costs, lawyers' fees, attorney fees, court costs, court fees, losing party pays, costs follow the event, not recoverable, each party bears its own fees, HIR Art 181*

**End point:** In Indonesian civil litigation the losing party is ordered to pay the court costs (court fees, operational costs, stamp duty), set by the judges in the judgment (HIR Art 181). Each party generally bears its own lawyers' fees: there is no general rule shifting them, and recovery is rare. On the fact pattern, SP can expect court costs if it wins but should not expect to recover its legal fees in the Jakarta proceedings. In the ICC arbitration, the tribunal can award costs, including legal fees.

*Source note: Outside the course materials. Secondary practice guides read 19 Nov 2026: Chambers Global Practice Guides, Litigation 2026 (Indonesia) and Litigation 2025 (Indonesia); Makarim & Taira S, Litigation & Dispute Resolution 2019 (Global Legal Insights); Mulawarman Law Review article on recovery of lawyers' fees. HIR Art 181 itself was not read; it is cited as these guides describe the rule. The ICC point relies on the ICC Rules (not read here). The fact pattern asks it [Fact p3 Q4(d)].*

## 2.VII Ex aequo et bono

- **Can a court decide on fairness?**
  - Indonesia: judges must explore society's sense of justice and cannot refuse a case for lack of law → [2-36](#clk-m-2-36)
- **Can an arbitrator?**
  - With the mandate: may depart from the law, but not from mandatory provisions → [2-37](#clk-m-2-37)
  - Without the mandate: decides on the law only → [2-38](#clk-m-2-38)

### clk-m-2-36 — In the Indonesian courts
*Keywords: ex aequo et bono, justice, Pancasila, cannot refuse a case, sense of justice*

**End point:** A party may ask for relief on justice and fairness; judges must explore society's sense of justice (Art 5(1)) and may not refuse a case because the law is absent or unclear (Art 10(1)); justice is based on Pancasila (Art 2(2)).

*Source note: Cmp-4 p6. Conflict: Cyril-Exam CMP §4.3.1 says it must be requested in writing under Art 2; the slide shows no such rule.*

### clk-m-2-37 — Arbitrators with an ex aequo et bono mandate
*Keywords: arbitration, ex aequo et bono, mandatory law, dwingende regels, Arbitration Law Art 56(1)*

**End point:** Arbitrators given the mandate may depart from the law, but not from mandatory provisions (dwingende regels).

*Source note: Cmp-4 p7*

### clk-m-2-38 — Arbitrators without the mandate
*Keywords: arbitration, legal norms, like a judge*

**End point:** Without the mandate, the arbitrator decides only on the law, like a judge.

*Source note: Cmp-4 p7*

## 2.VIII Discovery and privilege

- **Can a party get documents from the other side?**
  - Civil law generally: very limited disclosure → [2-39](#clk-m-2-39)
  - Indonesia: no compulsory disclosure → [2-40](#clk-m-2-40)
  - Thailand: no duty to disclose; list relied-on documents 7 days before the hearing → [2-41](#clk-m-2-41)
- **Can documents be withheld? (privilege)**
  - Generally: confidentiality, not privilege; in-house counsel usually not covered → [2-42](#clk-m-2-42)
  - Indonesia: licensed advocates only; the KPK can seize → [2-43](#clk-m-2-43)
  - Thailand: no privilege; the lawyer may refuse; in-house not covered → [2-44](#clk-m-2-44)
  - Grounds to withhold (official key): attorney-client privilege, trade secrets, irrelevance → [2-45](#clk-m-2-45)

### clk-m-2-39 — Civil-law discovery generally
*Keywords: discovery, disclosure, document production, no general right to request*

**End point:** Parties gather evidence before filing and present their own documents; disclosure is very limited and there is no general right to request documents from the other side.

*Source note: Cmp-4 p8-9; SampleQs p97 Q1, key p130*

### clk-m-2-40 — Discovery in Indonesia
*Keywords: Indonesia, no compulsory disclosure, specific documents*

**End point:** There is no compulsory disclosure; the court may order specific documents but very rarely does.

*Source note: Guide p6*

### clk-m-2-41 — Discovery in Thailand
*Keywords: Thailand, no duty to disclose, list of documents, 7 days, originals*

**End point:** There is no duty to disclose; a party lists the documents it relies on at least 7 days before the hearing, originals only, and a request for the other side's document succeeds only if you hold a copy or a reference to it.

*Source note: Guide p9*

### clk-m-2-42 — Confidentiality, not privilege
*Keywords: privilege, confidentiality, lawyer's duty, in-house counsel, APAC privilege table*

**End point:** Civil-law systems impose a lawyer's duty of confidentiality (state secrets, trade secrets, client's private information) rather than client privilege, and in-house lawyers are generally not covered; Singapore protects advice, litigation and in-house communications, China none.

*Source note: Cmp-4 p9-10; Guide p3*

### clk-m-2-43 — Indonesia — advocates' confidentiality and the KPK
*Keywords: Indonesia, licensed advocate, Advocates Law 18/2003, KPK, sans prejudice, in-house*

**End point:** Confidentiality attaches to communications with licensed Indonesian advocates (in-house lawyers only if licensed); there is no partial waiver, regulators such as the KPK can seize documents with no right to withhold, and "sans prejudice" letters between lawyers are inadmissible.

*Source note: Guide p5-7*

### clk-m-2-44 — Thailand — the lawyer may refuse
*Keywords: Thailand, no legal professional privilege, lawyer may refuse, court can compel, in-house counsel, police*

**End point:** There is no legal professional privilege. The lawyer (not the client) may refuse to disclose a confidential document or fact, but the court can compel disclosure if the refusal is unreasonable. In-house lawyers are generally not bound by the confidentiality obligation. So in the exam, a Thai in-house counsel cannot claim privilege, and the police can access the documents (official key).

*Source note: Cmp-4 p9; Guide p8-11; SampleQs p98 Q3, key p130; Cyril-Exam CMP §4.4.2. Conflict: the 2019 Guide says that only a court can compel disclosure to enforcement authorities (p10 Q13), and that licensed in-house lawyers may arguably be protected (p11 Q16). The slides and the official key say in-house lawyers are generally not protected and the police can access the documents, so follow the slides and the key.*

### clk-m-2-45 — Grounds for withholding documents
*Keywords: withhold documents, external counsel, trade secrets, relevance*

**End point:** Per the official key, documents can be withheld on attorney-client privilege (typically external lawyers only), trade secrets or proprietary information, or irrelevance as ruled by the judge.

*Source note: SampleQs p97 Q2, key p130*

## 3.I Choice of law — contract

- **Was a state's law chosen?**
  - Only a state's law counts; not non-state rules or soft law → [3-1](#clk-m-3-1)
- **Is the issue formation, agency or capacity?**
  - A similar 3-stage rule; capacity can also follow the defendant's domicile → [3-2](#clk-m-3-2)
- **Which law governs the contract? (3 stages)**
  - Stage 1, express choice: applies if bona fide and legal (fails only if made solely to evade a foreign law) → [3-3](#clk-m-3-3)
  - Stage 2, implied choice: inferred from factors such as the jurisdiction clause, language and currency → [3-4](#clk-m-3-4)
  - Stage 3, objective choice: the place of performance and related transactions weigh most → [3-5](#clk-m-3-5)

### clk-m-3-1 — A choice of law must be a state's law
*Keywords: lex causae, governing law, state law, soft law, model law*

**End point:** Choice of law rules select the law of a state; non-state model laws and soft law do not count.

*Source note: CoL-2 p5*

### clk-m-3-2 — Formation, agency and capacity
*Keywords: formation, agency, capacity, Solomon Lew, domicile*

**End point:** Formation and agency follow a similar 3-stage rule (Solomon Lew); capacity follows the 3-stage rule or the law of the defendant's domicile.

*Source note: CoL-2 p12*

### clk-m-3-3 — Stage 1 — express choice and bona fides
*Keywords: express choice, bona fide and legal, no connection, evasion, Peh Teck Quee, Pacific Recreation*

**End point:** An express choice governs even if the chosen law has no connection to the dispute; the only limit is that it be bona fide and legal — it fails only if the sole purpose was to evade the operation of a foreign law (Peh Teck Quee).

*Source note: CoL-2 p8-9; SampleQs p102 Q2, key p131*

### clk-m-3-4 — Stage 2 — implied choice
*Keywords: implied choice, jurisdiction clause, arbitration clause, related transaction*

**End point:** Where there is no express choice, ask what law the parties actually but impliedly chose, using factors such as a jurisdiction or arbitration clause, language, form, related transactions, currency, residence and place of performance.

*Source note: CoL-2 p10*

### clk-m-3-5 — Stage 3 — objective choice and weight of factors
*Keywords: objective choice, reasonable businesspeople, place of performance, First Laser, currency, language*

**End point:** Failing that, apply the law reasonable businesspeople would have chosen: the same factors with different weight — place of performance and the law of related transactions are very important (First Laser), internationalised language, forms and currencies are not.

*Source note: CoL-2 p10-11. Conflict: Cyril-Exam CoL §2.2.1 says equal weight is placed on all factors at stage 3; the slide says different weight.*

## 3.II Choice of law — tort

- **What is the basic rule?**
  - Double actionability: actionable under both Singapore law and the lex loci delicti → [3-6](#clk-m-3-6)
- **Where is the lex loci delicti?**
  - Negligence: where the conduct occurred → [3-7](#clk-m-3-7)
  - Misrepresentation: where it was received and acted on → [3-8](#clk-m-3-8)
  - Conspiracy: the most-connected place → [3-9](#clk-m-3-9)
  - Other torts: where in substance the cause of action arose → [3-10](#clk-m-3-10)
- **Can either law be disapplied?**
  - Flexible exception: only if that law is purely fortuitous → [3-11](#clk-m-3-11)

### clk-m-3-6 — Double actionability
*Keywords: double actionability, lex fori, lex loci delicti, Rickshaw*

**End point:** A tort claim succeeds only if it would succeed under both Singapore law (lex fori) and the lex loci delicti — "double or nothing" (Rickshaw).

*Source note: CoL-2 p14*

### clk-m-3-7 — Negligence — where the conduct occurred
*Keywords: negligence, lex loci delicti, negligent conduct, Man Diesel*

**End point:** For negligence, the lex loci delicti is where the defendant's allegedly negligent conduct occurred, not where the claimant suffered damage (Man Diesel).

*Source note: CoL-2 p15-16*

### clk-m-3-8 — Misrepresentation — where received and acted on
*Keywords: misrepresentation, received and acted upon, JIO Minerals*

**End point:** For misrepresentation, it is where the statement was received and acted upon (JIO Minerals).

*Source note: CoL-2 p16*

### clk-m-3-9 — Conspiracy — the most-connected place
*Keywords: conspiracy, most connected, EFT Holdings, five factors*

**End point:** For conspiracy, it is the place most connected with the conspiracy, weighing the conspirators' identity and location, where agreements were made, where concerted acts were done, the claimant's location and where losses were suffered (EFT Holdings).

*Source note: CoL-2 p16*

### clk-m-3-10 — The general rule
*Keywords: lex loci delicti, substance of the tort, Man Diesel*

**End point:** Otherwise, ask where in substance the cause of action arose, looking back over the events once the tort is complete (Man Diesel).

*Source note: CoL-2 p15*

### clk-m-3-11 — The flexible exception
*Keywords: flexible exception, purely fortuitous, third state law, Rickshaw*

**End point:** The court may disapply the lex fori, the lex loci delicti or both (applying a more connected third law), but only where the disapplied law is purely fortuitous; the exception is rare and strictly applied.

*Source note: CoL-2 p17-18; SampleQs p102 Q3, key p131*

## 3.III Limits on choice of law

- **Is the issue procedural?**
  - Evidence and remedies: the lex fori → [3-12](#clk-m-3-12)
  - Limitation: the lex causae (Foreign Limitation Periods Act ss 3–4) → [3-13](#clk-m-3-13)
- **Is there a substantive override?**
  - A Singapore statute, expressly or impliedly (forum mandatory rules) → [3-14](#clk-m-3-14)
  - A foreign rule that offends fundamental public policy → [3-15](#clk-m-3-15)

### clk-m-3-12 — Procedure is for the lex fori
*Keywords: procedure, substance, evidence, presumptions, remedies, lex fori, Goh Suan Hee*

**End point:** Procedural issues are governed only by Singapore law, including evidence (admissibility, weight, presumptions) and the availability of certain remedies (Goh Suan Hee).

*Source note: CoL-2 p21-22. Conflict: Cyril-Exam CoL §2.4.1 says Goh Suan Hee suggests remedies are for the lex causae; the slide lists remedies as procedural.*

### clk-m-3-13 — Limitation — Foreign Limitation Periods Act
*Keywords: limitation, Foreign Limitation Periods Act 2012, FLPA s 3, s 4, lex causae*

**End point:** Limitation is an exception to the procedure rule: it is now mostly governed by the lex causae (FLPA ss 3-4). Where foreign law governs the claim, its limitation period applies under s 3. In the official sample, a 2-year foreign period bars a contract claim brought in Singapore after 3 years, even though Singapore's period is 6 years.

*Source note: CoL-2 p22; CoL-Plan p4; SampleQs p103 Q4, key p131; Isabel p5. The library gives no FLPA detail beyond this pointer to ss 3-4 and the sample key, so do not go further than they do.*

### clk-m-3-14 — Forum mandatory rules
*Keywords: forum mandatory rule, overriding statute, regulatory, protective, JIO Minerals*

**End point:** Choice of law rules are common-law rules, so a Singapore statute can override them — expressly (rare) or impliedly where it is regulatory or protective rather than merely supplementing private rights (JIO Minerals); the test is "ambiguous".

*Source note: CoL-2 p23*

### clk-m-3-15 — Public policy
*Keywords: public policy, fundamental, Burswood, Oppenheimer v Cattermole, separate legal personality, Desert Palace, gambling*

**End point:** A specific foreign rule is disapplied only if enforcing it offends Singapore's fundamental public policy (Burswood) — e.g. race discrimination (Oppenheimer) or separate legal personality; statutory policy such as on gambling (Desert Palace) is an open question; the rest of the foreign law still applies.

*Source note: CoL-2 p24-25; SampleQs p102 Q2. Conflict: Cyril-Exam CoL §2.4.3 says Desert Palace held statutory policy ranks higher; the slide marks it with a question mark.*

## 3.IV Jurisdiction — service in Singapore

- **Does jurisdiction exist? Who was served in Singapore?**
  - An individual: present even fleetingly → [3-16](#clk-m-3-16)
  - A company: Singapore-incorporated, or foreign with a place of business here → [3-17](#clk-m-3-17)
- **Should Singapore hear it? (Spiliada)**
  - Stage 1: the defendant shows another forum is more appropriate → [3-18](#clk-m-3-18)
  - Stage 2: the claimant shows a real risk of injustice abroad → [3-19](#clk-m-3-19)

### clk-m-3-16 — Individuals — present even fleetingly
*Keywords: service in Singapore, presence, fleeting presence, Burgundy, SCJA s 16(1)(a)(i)*

**End point:** Jurisdiction exists if the defendant is served in Singapore (SCJA s 16(1)(a)(i)); an individual is present even if only fleetingly (Burgundy).

*Source note: CoL-3 p8-9*

### clk-m-3-17 — Companies — incorporated or carrying on business
*Keywords: company presence, Companies Act s 387, s 368, s 376, carrying on business, Adams v Cape*

**End point:** A company is present if Singapore-incorporated (CA s 387), or if foreign with a place of business or carrying on business here (CA ss 368, 376) — an agent doing its business from a fixed place for a sufficient period (Adams v Cape).

*Source note: CoL-3 p9*

### clk-m-3-18 — Spiliada stage 1 — D shows another forum is more appropriate
*Keywords: forum non conveniens, natural forum, Spiliada, Lakshmi, burden on defendant, connecting factors*

**End point:** In service-in cases the defendant must show Singapore is not the natural forum, weighing party connections, witnesses and evidence, governing law and other proceedings — not mechanically (Lakshmi).

*Source note: CoL-3 p10-12*

### clk-m-3-19 — Spiliada stage 2 — real risk of injustice abroad
*Keywords: real and material risk of injustice, burden on claimant, limitation, delay, breakdown of law and order*

**End point:** Even if another forum is more appropriate, Singapore keeps the case if the claimant shows a real and material risk of injustice abroad — e.g. very short limitation, severe delay, blatantly unfair evidence rules, threats to safety or a breakdown of law and order.

*Source note: CoL-3 p13-14*

## 3.V Jurisdiction — service out of Singapore

- **What is the test for service out?**
  - Court approval (O 8 r 1): good arguable case of nexus, forum conveniens, serious question on the merits; the burden is on the claimant → [3-20](#clk-m-3-20)
- **Which nexus head (PD 63(3))?**
  - Contract made, through an agent, governed by Singapore law, or with a Singapore clause ((d)) → [3-21](#clk-m-3-21)
  - Breach in Singapore ((e)) → [3-22](#clk-m-3-22)
  - Tort act in Singapore, or Singapore as the lex loci delicti ((f)(i), (p)) → [3-23](#clk-m-3-23)
  - Damage suffered in Singapore ((f)(ii)) → [3-24](#clk-m-3-24)

### clk-m-3-20 — The O 8 r 1 test and the burden on C
*Keywords: service out, O 8 r 1(1), PD 63(2), good arguable case, sufficient nexus, forum conveniens, serious question, Spiliada*

**End point:** Service out needs the Court's approval (ROC 2021 O 8 r 1(1)) on a showing of a good arguable case of sufficient nexus, that Singapore is the forum conveniens, and a serious question on the merits (PD 63(2)); the claimant bears the burden on natural forum (Spiliada). More than one state may have a nexus.

*Source note: CoL-3 p16-17, p20*

### clk-m-3-21 — Contract heads — PD 63(3)(d)
*Keywords: PD 63(3)(d)(i), (d)(ii), (d)(iii), (d)(iv), contract made in Singapore, essential step, DJS Solutions, governing law, jurisdiction clause*

**End point:** A contract claim has a nexus if the contract was made in Singapore or an essential step was taken here (d)(i) (DJS Solutions), made through an agent here (d)(ii), governed by Singapore law (d)(iii), or contains a Singapore jurisdiction clause (d)(iv).

*Source note: CoL-3 p17-18*

### clk-m-3-22 — Breach in Singapore — PD 63(3)(e)
*Keywords: PD 63(3)(e), breach in Singapore, performance impossible, Recovery Vehicle 1*

**End point:** A claim for breach committed in Singapore, or abroad making performance in Singapore (the only place of performance) impossible, has a nexus (Recovery Vehicle 1).

*Source note: CoL-3 p18*

### clk-m-3-23 — Tort act or Singapore law of the tort — PD 63(3)(f)(i), (p)
*Keywords: PD 63(3)(f)(i), PD 63(3)(p), act or omission in Singapore, cause of action arising in Singapore*

**End point:** A tort claim has a nexus if an act or omission in Singapore is an element of it ((f)(i)), or if the cause of action arose in Singapore, i.e. Singapore is the lex loci delicti ((p)).

*Source note: CoL-3 p19*

### clk-m-3-24 — Damage suffered in Singapore — PD 63(3)(f)(ii)
*Keywords: PD 63(3)(f)(ii), damage suffered in Singapore, place of incorporation, bank account, MAN Diesel*

**End point:** A claim founded on damage suffered here (for torts where damage is part of the claim, e.g. negligence, conspiracy) or for damages for damage suffered here has a nexus; a company suffers damage at its place of incorporation, not where its bank account is (MAN Diesel).

*Source note: CoL-3 p19*

## 3.VI Jurisdiction clauses

- **Is the clause exclusive?**
  - Exclusive, naming Singapore: no stay without strong cause → [3-25](#clk-m-3-25)
  - Exclusive, naming a foreign court: stay unless strong cause → [3-26](#clk-m-3-26)
- **Is it non-exclusive?**
  - Naming Singapore: strong cause → [3-27](#clk-m-3-27)
  - Naming a foreign court: the natural forum test; the clause is only a factor → [3-28](#clk-m-3-28)
- **Does the clause provide for service out?**
  - A clause providing for service out: no Court approval needed (O 8 r 1(3)) → [3-29](#clk-m-3-29)
- **Hague Choice of Court Agreements Act 2016 (COCAA): not covered in the course, "good to know in practice"** → [3-30](#clk-m-3-30)
  - Does COCAA apply? International case, exclusive choice of court agreement, civil or commercial matter; not consumers, employment, arbitration or the s 9(2) list → [3-30](#clk-m-3-30)
  - A clause naming the courts of one Contracting State is deemed exclusive unless the parties expressly say otherwise → [3-30](#clk-m-3-30)
  - Singapore is the chosen court: it must hear the case and cannot decline on forum non conveniens → [3-30](#clk-m-3-30)
  - Singapore is not the chosen court: it must stay or dismiss, unless one of five exceptions applies (s 12(1)) → [3-30](#clk-m-3-30)
  - Enforcing a judgment of a chosen foreign court: the High Court must recognise it with no review of the merits; mandatory and discretionary refusal grounds (ss 13–16) → [3-30](#clk-m-3-30)

### clk-m-3-25 — Exclusive Singapore clause — strong cause
*Keywords: exclusive jurisdiction clause, strong cause, Vinmar, abuse of process, party autonomy*

**End point:** Singapore will not stay unless there is strong cause (Vinmar): the forum non conveniens factors plus substantial justice and abuse of process, with only factors unforeseeable when contracting carrying real weight — stricter than natural forum.

*Source note: CoL-3 p25-26*

### clk-m-3-26 — Exclusive foreign clause — stay unless strong cause
*Keywords: exclusive foreign jurisdiction clause, stay, strong cause*

**End point:** The strong cause test works in reverse: Singapore will generally stay its proceedings to give effect to an exclusive foreign clause unless there is strong cause not to.

*Source note: CoL-3 p26; SampleQs p104 Q6, key p131*

### clk-m-3-27 — Non-exclusive Singapore clause — strong cause
*Keywords: non-exclusive jurisdiction clause, Singapore, strong cause, Shanghai Turbo, forum bias*

**End point:** Where parties submitted to the non-exclusive jurisdiction of Singapore, proceedings will not be stayed unless there is strong cause — a forum bias for Singapore (Shanghai Turbo).

*Source note: CoL-3 p27*

### clk-m-3-28 — Non-exclusive foreign clause — natural forum
*Keywords: non-exclusive foreign jurisdiction clause, natural forum, Shanghai Turbo*

**End point:** A non-exclusive foreign clause does not by itself require Singapore to decline: no stay unless Singapore is not the natural forum, the clause being only a factor (Shanghai Turbo).

*Source note: CoL-3 p27; SampleQs p104 Q7, key p131*

### clk-m-3-29 — Clause providing for service out
*Keywords: O 8 r 1(3), service out under contract, no approval, invariably exercise*

**End point:** Where a contract provides for service out in a particular manner, no Court approval is needed (O 8 r 1(3)) and the court will invariably exercise jurisdiction; the clause also supplies a nexus under PD 63(3)(d)(iv) and (r).

*Source note: CoL-3 p23-24*

### clk-m-3-30 — Hague Choice of Court (COCAA) — not covered
*Keywords: Choice of Court Agreements Act 2016, COCAA, Hague Convention on Choice of Court Agreements 2005, Hague Convention 2005, Contracting State, exclusive choice of court agreement, deemed exclusive, unless expressly provided otherwise, international case, civil or commercial matter, consumer, employment, chosen court, must exercise jurisdiction, cannot decline, forum non conveniens, non-chosen court, must stay or dismiss, null and void, capacity, manifest injustice, public policy, cannot reasonably be performed, chosen court decided not to hear, recognition and enforcement, foreign judgment, no review of merits, refuse recognition, fraud in connection with procedure, inconsistent judgment, punitive damages, non-compensatory damages, judicial settlement, interim measures, severability, COCAA s 3, s 8, s 9, s 11, s 12, s 13, s 14, s 15, s 16*

**End point:** The slide flags COCAA as not covered in the course but "good to know in practice". It applies to an exclusive choice of court agreement in an international civil or commercial case. A clause naming the courts of one Contracting State is deemed exclusive unless the parties expressly say otherwise. A chosen Singapore court must hear the case unless the agreement is null and void under Singapore law, and cannot decline on forum non conveniens. A non-chosen Singapore court must stay or dismiss unless one of five exceptions applies. The High Court must recognise and enforce a chosen foreign court's judgment without reviewing the merits, subject to the refusal grounds in ss 14–16.

> **Choice of Court Agreements Act 2016 (gives effect to the Hague Convention of 30 Jun 2005; in force 1 Oct 2016)**
> - **Scope (s 8):** every international case where there is an exclusive choice of court agreement concluded in a civil or commercial matter, subject to ss 9, 10 and 22.
>   - "International case" for jurisdiction (s 4(1)): unless the parties reside in the same Contracting State and everything except the chosen court's location is connected only with that State. For recognition, any foreign judgment case is international (s 4(2)).
>   - Excluded agreements (s 9(1)): (a) a party is an individual acting primarily as a consumer; (b) employment contracts and collective agreements.
>   - Excluded matters (s 9(2)), e.g. status and capacity of individuals, family law, succession, insolvency, carriage of passengers and goods, competition, personal injury or death, non-contractual tort claims for damage to tangible property, rights in rem in immovables, validity of legal persons, validity and (non-contractual) infringement of IP other than copyright, public registers. A matter raised only as a preliminary question does not take the case outside the Act (s 9(5)).
>   - Arbitration and related proceedings are excluded (s 9(3)); so are interim measures, which a Singapore court may still grant (s 10).
>   - Not retrospective: no application to a Singapore-court agreement concluded before 1 Oct 2016, or to a foreign-court agreement concluded before the Convention entered into force for that State (s 24).
> - **Exclusivity (s 3):**
>   - (1) exclusive agreement: in writing or another accessible form, designating the courts (or specific courts) of one Contracting State to the exclusion of all others;
>   - (2) deemed exclusive: a written agreement designating the courts of one Contracting State is deemed exclusive unless the parties expressly provide otherwise;
>   - a clause in a contract is independent of the contract, so the contract's invalidity alone does not invalidate it (s 5).
> - **Singapore is the chosen court (s 11):**
>   - (1) it has jurisdiction unless the agreement is null and void under Singapore law;
>   - (2) it cannot decline on the ground that the dispute should be decided in another State's court (no forum non conveniens stay);
>   - (3) except in circumstances prescribed by regulations.
>   - A designation of the High Court includes the SICC unless a contrary intention appears (s 2(2)–(3)).
> - **Singapore is not the chosen court (s 12(1)):** it must stay or dismiss, unless it determines that:
>   - (a) the agreement is null and void under the law of the chosen court's State;
>   - (b) a party lacked capacity under Singapore law;
>   - (c) giving effect to it would lead to manifest injustice or be manifestly contrary to Singapore public policy;
>   - (d) it cannot reasonably be performed for exceptional reasons beyond the parties' control; or
>   - (e) the chosen court has decided not to hear the case.
>   - The court may still stay or dismiss on other grounds (s 12(2)).
> - **Recognition and enforcement (s 13):** apply to the General Division of the High Court.
>   - The judgment is recognised only if it has effect, and enforced only if it is enforceable, in the State of origin (s 13(2)).
>   - No review of the merits; the court is bound by the origin court's jurisdictional findings of fact unless the judgment was by default (s 13(3)).
>   - The court must recognise and enforce, except on the refusal grounds below (s 13(4)).
>   - "Judgment" covers final decisions on the merits, consent and default judgments, and costs (s 2(1)); a severable part may be enforced (s 19).
> - **Must refuse (s 14):**
>   - (a) the defendant was not notified of the originating document in time to defend, unless the defendant appeared and argued the case without challenging notification where the origin State's law allowed a challenge;
>   - (b) the judgment was obtained by fraud in connection with a matter of procedure;
>   - (c) recognition would be manifestly incompatible with Singapore public policy, including fundamental principles of procedural fairness.
> - **May refuse (s 15(1)):**
>   - (a) the agreement is null and void under the chosen court's law, unless the chosen court held it valid;
>   - (b) a party lacked capacity under Singapore law;
>   - (c) notification was incompatible with Singapore's fundamental principles on service;
>   - (d) the judgment is inconsistent with a Singapore judgment between the same parties;
>   - (e) it is inconsistent with an earlier recognisable judgment of another State between the same parties on the same cause of action;
>   - (f) other prescribed circumstances.
> - **Other grounds:**
>   - refuse or postpone while the judgment is under review or appeal, or the time for one has not expired (s 15(2));
>   - refuse against a party that objected in time to a transfer by the chosen court (s 15(4));
>   - refuse to the extent the damages, including exemplary or punitive damages, exceed compensation for actual loss (s 16).
> - Judicial settlements are enforced like judgments, on the same refusal grounds (s 20). Where the Act does not apply, the common law rules continue (s 21).

*Source note: CoL-3 p28 (slide: "not covered in this course, but good to know in practice"; deemed exclusive; chosen court must exercise jurisdiction; non-chosen court must not, "unless the clause is invalid"). Statute: Choice of Court Agreements Act 2016 (2020 Rev Ed, operative 31 Dec 2021), `study/clk-m/authorities/3 Conflicts/Choice of Court Agreements Act 2016 (SSO current).pdf`, ss 2-5, 8-16, 19-21, 24. CoL-3 p28 shortens the s 12(1) exceptions to "unless the clause is invalid"; the Act lists five. The library does not list the Contracting States; the pack states no list, so check the HCCH status table if a question turns on it.*

## 3.VII Submission by conduct

- **What is the test?**
  - A clear and unequivocal step inconsistent with objecting to jurisdiction → [3-31](#clk-m-3-31)
- **Does this step submit?**
  - Yes: a defence on the merits, contesting summary judgment, seeking status-quo injunctions → [3-32](#clk-m-3-32)
  - No: a notice to contest, or challenging jurisdiction or the natural forum → [3-33](#clk-m-3-33)

### clk-m-3-31 — The test for submission
*Keywords: submission by conduct, SCJA s 16(1)(b), clear and unequivocal step, Reputation Administration v Spamhaus*

**End point:** Submission is its own head of jurisdiction (SCJA s 16(1)(b)) and cures defective service; it requires a clear and unequivocal step inconsistent with objecting to jurisdiction (Reputation Administration), and is distinct from submission by agreement.

*Source note: CoL-3 p30-31*

### clk-m-3-32 — Steps that submit
*Keywords: defence on the merits, summary judgment, interim injunction, Reputation Administration, Shanghai Turbo*

**End point:** Filing a defence on the merits or contesting summary judgment on the merits (Reputation Administration), seeking status-quo interim injunctions (Shanghai Turbo), and contesting interim injunctions that D could not avoid by challenging jurisdiction all submit.

*Source note: CoL-3 p32. Conflict: Isabel p14 says contesting an interim injunction never submits; the slide follows the "could not avoid" test.*

### clk-m-3-33 — Steps that do not submit
*Keywords: notice of intention to contest, challenge jurisdiction, natural forum, O 6 r 6(4), O 6 r 7(6)*

**End point:** Filing a notice to contest (O 6 r 6(4)), or challenging the existence of jurisdiction or Singapore as natural forum (O 6 r 7(6)), does not submit.

*Source note: CoL-3 p32*

## 3.VIII Anti-suit injunctions

- **Is the respondent amenable to Singapore jurisdiction?**
  - It must be; this is a prerequisite → [3-34](#clk-m-3-34)
- **Is there a jurisdiction clause?**
  - A Singapore clause: readily granted, absent strong cause or delay → [3-35](#clk-m-3-35)
  - A foreign-court clause: no ASI (*Akai*) → [3-36](#clk-m-3-36)
  - No clause: Singapore is the natural forum, and the foreign suit is vexatious or oppressive → [3-37](#clk-m-3-37)

### clk-m-3-34 — Jurisdiction over the respondent is a prerequisite
*Keywords: anti-suit injunction, ASI, Lakshmi factors, amenable to jurisdiction*

**End point:** An ASI restrains foreign proceedings to prevent fragmentation and outflanking; the Lakshmi factors are not a test, and jurisdiction over the respondent is a prerequisite for any interim injunction.

*Source note: CoL-4 p3-5*

### clk-m-3-35 — Contractual ASIs — readily granted
*Keywords: contractual anti-suit injunction, Singapore jurisdiction clause, Sun Travels, strong cause, delay*

**End point:** Where foreign proceedings breach a Singapore jurisdiction clause, an ASI is readily granted (Sun Travels) unless there is strong cause, or unreasonable delay with the foreign case advanced (delay is excused only if spent contesting the foreign court's jurisdiction).

*Source note: CoL-4 p6-7; SampleQs p104 Q8, key p131*

### clk-m-3-36 — Foreign-court clause — no ASI
*Keywords: foreign jurisdiction clause, international busybody, Akai*

**End point:** Where the parties chose a foreign court, Singapore will not generally grant an ASI, even to restrain proceedings in another foreign state — it is not an "international busybody" (Akai).

*Source note: CoL-4 p6. Conflict: Cyril-Exam CoL §4.3 says "will not grant"; the slide says "will not generally grant".*

### clk-m-3-37 — Non-contractual ASIs — vexation or oppression
*Keywords: non-contractual anti-suit injunction, natural forum, vexatious, oppressive, unconscionable, Kirkham v Trane, Lakshmi, comity*

**End point:** Without a Singapore clause courts are generally reluctant (comity): an ASI needs Singapore to be the natural forum and the foreign suit to be vexatious or oppressive — i.e. unconscionable, such as oppressive procedure, extreme inconvenience or bad faith (Kirkham v Trane; Lakshmi); delay is relevant.

*Source note: CoL-4 p8-10*

## 3.IX Foreign judgments — recognition

- **Did the foreign court have international jurisdiction?**
  - Four bases only: the debtor was the claimant, was present, submitted, or agreed a clause → [3-38](#clk-m-3-38)
- **Is the judgment final and conclusive?**
  - A final judgment: cannot be varied by the court that gave it, even if appealable → [3-39](#clk-m-3-39)
  - An interim or interlocutory order: final only on the issues it had to decide → [3-40](#clk-m-3-40)

### clk-m-3-38 — International jurisdiction — four bases only
*Keywords: international jurisdiction, Giant Light, claimant, presence, submission, jurisdiction clause, Pemberton v Hughes*

**End point:** The foreign court must have had jurisdiction over the debtor because the debtor was the claimant, was present, submitted by conduct, or agreed a clause choosing that court (Giant Light); service is not required (Pemberton v Hughes), and a mere nexus such as governing law is not enough.

*Source note: CoL-5 p6-8. Conflict: Cyril-Exam CoL §5.2.1 lists five bases, including a prior agreement to submit; the slide lists four.*

### clk-m-3-39 — Final and conclusive judgments
*Keywords: final and conclusive, Bunga Melati 5, res judicata, first-instance judgment*

**End point:** A judgment is final and conclusive if the court that gave it cannot vary, reopen or set it aside (Bunga Melati 5); a first-instance judgment is final even if appealable.

*Source note: CoL-5 p9-10*

### clk-m-3-40 — Interim and interlocutory orders
*Keywords: interlocutory order, interim order, good arguable case, strike-out, Lakshmi*

**End point:** Interim status-quo orders and findings of a good arguable case are not final; an interlocutory order is final only on the issues it had to finally decide (Lakshmi).

*Source note: CoL-5 p9-10; SampleQs p105 Q9, key p131*

## 3.X Foreign judgments — defences and consequences

- **Which defence?**
  - No notice or no hearing: breach of natural justice → [3-41](#clk-m-3-41)
  - Fraud from within the trial: only on evidence the foreign court did not consider → [3-42](#clk-m-3-42)
  - Fraud from outside the trial: a defence even if the evidence was considered → [3-43](#clk-m-3-43)
  - Fundamental public policy, including an egregious error of Singapore law → [3-44](#clk-m-3-44)
- **What follows recognition?**
  - Enforce a money judgment by an action for the debt → [3-45](#clk-m-3-45)
  - Issue estoppel and Henderson estoppel → [3-46](#clk-m-3-46)

### clk-m-3-41 — Breach of natural justice
*Keywords: natural justice, notice, opportunity to be heard, Paulus Tannos, summary judgment without notice*

**End point:** Recognition can be refused if the debtor lacked notice (service or actual knowledge) or a meaningful opportunity to be heard (Paulus Tannos).

*Source note: CoL-5 p12-13; SampleQs p105 Q10, key p131*

### clk-m-3-42 — Intrinsic fraud
*Keywords: intrinsic fraud, forged evidence, concocted testimony, Les Placements, Hong Pian Tee*

**End point:** Fraud from within the trial (forged evidence, concocted testimony) is a defence only if based on evidence the foreign court did not consider (Les Placements).

*Source note: CoL-5 p14*

### clk-m-3-43 — Extrinsic fraud
*Keywords: extrinsic fraud, bribing witnesses, tricked into settling, full and frank disclosure*

**End point:** Fraud from outside the trial (bribing witnesses, tricking the debtor into settling, default judgment without full and frank disclosure) is a defence even if based on evidence the foreign court considered.

*Source note: CoL-5 p14*

### clk-m-3-44 — Public policy
*Keywords: public policy, Burswood, Merck, manifest error of Singapore law, WSG Nimbus, anti-suit injunction*

**End point:** Recognition is refused if contrary to fundamental public policy (Burswood), including a judgment based on a manifest, patent or egregious error of Singapore law (Merck) or obtained in breach of a Singapore ASI (WSG Nimbus).

*Source note: CoL-5 p15*

### clk-m-3-45 — Enforcing money judgments
*Keywords: enforcement, action on the judgment debt, summary judgment, definite sum, PD 63(3)(m), Desert Palace*

**End point:** A recognised money judgment is enforced by an action for the debt, usually by summary judgment (nexus PD 63(3)(m); Singapore is the natural forum if the debtor has assets here); only definite-sum judgments qualify, not liability findings, injunctions, specific performance or proprietary relief (Desert Palace).

*Source note: CoL-5 p17-18*

### clk-m-3-46 — Estoppel — issue and Henderson
*Keywords: issue estoppel, Henderson, extended res judicata, Merck, Humpuss*

**End point:** Issue estoppel needs the same parties and the same issue finally decided (Merck); Henderson estoppel covers an issue that should have been raised (Merck) or a party who should have been joined (Humpuss), absent fresh evidence or a good reason.

*Source note: CoL-5 p19-21*
