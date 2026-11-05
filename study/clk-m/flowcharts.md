# CLK-M — Flowcharts

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
> - The Computer Misuse Act is not on the CLK reading list and is not in the library. `TODO: verify` whether its definition of "computer" is the same.

*Source note: SSO-CYSA s 2 ("computer", "computer system", virtual computers); Drill 1 DP15*

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
  - Serious harm: the Act gives no test, only two illustrations (a lawyer losing clients; a widely shared adultery allegation). `TODO: verify` any case-law test.
- **Trap words**
  - "Specific correction order": there is no such order. The intermediary order is the *targeted* correction order → [0-65](#clk-m-0-65), [0-67](#clk-m-0-67)
  - The slides label s 15B "(SPO)" and s 15C "correction order (DO)". Use the statute's names → [0-63](#clk-m-0-63), [0-64](#clk-m-0-64)
  - "Direction" means POFMA, not POHA → [0-68](#clk-m-0-68)

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
> - `TODO: verify` whether any case or the course materials set a test for serious harm.

*Source note: SSO-POHA s 15E and illustrations (unchanged by Acts 21 and 23 of 2025); POHA p42-43 (s 15E); POHA Regs p3 (reg 4(4)); Drill 1 DP14. Conflict: Cyril-Exam DP §4.1.5 lists WeChat and YouTube as prescribed for s 15E; reg 4(4) lists Facebook/Instagram, Twitter, HardwareZone, Google Search and Baidu.*

### clk-m-0-67 — Requirements common to the false-statement orders
*Keywords: false statement of fact, balance of probabilities, just and equitable, does not know it is false, specific correction order, POHA s 15*

**End point:** The applicant must show on a balance of probabilities a false statement of fact about them, published by the respondent, and that an order is just and equitable; the respondent need not know it is false, and orders may issue even if it was amended or taken down. There is no "specific correction order".

*Source note: SSO-POHA ss 15, 15A(2); POHA p37-38 (ss 15, 15A(2)); SampleQs p89 Q3, key p130. Since 29 Jun 2026, s 15(1) also applies these rules to the two administrator orders (clk-m-0-71).*

### clk-m-0-68 — POFMA (non-core)
*Keywords: POFMA, ministerial direction, correction direction, stop communication direction, access blocking order, declared online location*

**End point:** POFMA works through ministerial directions (correction, stop communication, access blocking, directions to intermediaries) rather than court orders; s 7 makes it an offence to communicate a known falsehood likely to cause specified harms.

*Source note: DP-3 p27; POFMA p13-15; DP-Plan p6*

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
- **Service and treaties**
  - A clause providing for service out: no Court approval needed (O 8 r 1(3)) → [3-29](#clk-m-3-29)
  - Hague Choice of Court (COCAA): not covered → [3-30](#clk-m-3-30)

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
*Keywords: Choice of Court Agreements Act 2016, COCAA, Hague Convention 2005*

**End point:** Under COCAA a clause choosing one Convention state is deemed exclusive and the chosen court must hear the case; the slide flags this as not covered in the course.

*Source note: CoL-3 p28*

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
