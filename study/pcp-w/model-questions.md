# PCP-W — Model Questions and Answers

Paper `pcp-w`, PCP written (PCP Paper 1), Mon 7 Dec 2026, 2:30–4:30pm, open book. Subject 0 Criminal Litigation Practice (Q1–Q2, about 60 marks), Subject 1 Family Law Practice (Q3–Q6, about 40 marks). Written 15 Nov 2026 as Markdown only, on Bennett's instruction of 14 Nov; no PDF is built until Phase 2 (`python3 tools/build_pack.py pcp-w --questions`).

**How the file runs.** *Part 1* holds the questions by Subject → Topic → Sub-point, in `coverage.md` order. Every past-paper question part held is placed under the Sub-point it mainly tests; a Sub-point it also tests carries a "see" line pointing to it. Where no past paper reaches a Sub-point, an own question ("own question", marked C or F) fills the gap. Every one of the 88 Sub-points has at least one question whose tag line names it. *Part 2* holds the Drills: timed sets built from Part 1 questions, each with a time limit and marking points.

**How to read a question.** The tag line gives the question ID · the Sub-point Keys it raises (`coverage.md`) · the source · marks · the Pre-writes (`prewrites.md`) or Templates (`templates.md`) that hold the rules. Cover the answer, answer it in I-CRUPAC prose, then check. Answers name the Pre-write they draw on as "(Pre-write 0-13)"; the law in every answer comes from those Pre-writes, which were checked against the course materials and the current statutes on 10 Nov 2026 (see `coverage.md`, Source key).

**Sources.** Question text is transcribed, or tightly summarised where the facts run to pages, from the papers in `Bar Exam/Seniors Notes/Nic_s Part B Package/3. PYP/` (2022, 2023 and 2025 are scans, read from the page images; earlier candidates' margin notes are left out) and from the 2026 Sample Questions (`Bar Exam/Sample Questions/20260806_Part_B_Course_Session_2_Sample_Questions.pdf`, "SQ"). Words in [square brackets] are not in the paper. The papers held:

- **PYP 2025** — `2025 PYP/PCP Paper 1 2025 (Crim & Fam).pdf`, Mon 8 Dec 2025: Crim Q1 (Mr Albert, 30 marks), Q2 (Ms Wing, 30 marks); Fam Q3–Q6 (40 marks).
- **PYP 2023** — `2023 PYP/PCP Paper 1 (Crim).pdf` and `(Fam).pdf`, Thu 7 Dec 2023: Crim Q1 (Mr ACC), Q2 (Ms Kew), 60 marks; Fam Q3–Q6, 40 marks.
- **PYP 2022** — `2022 PYP/Crim Lit 2022 PYP.pdf` (Wed 7 Dec 2022; Section B, Q1 Alex and Q2 Brian, 50 marks; the Section A MCQs were on Examplify and are not held) and `2022 PYP/Fam Lit 2022 PYP (pp 2-5 only, phone photos).pdf` (Cherry and Daniel; no marks printed; the cover is missing). The 2022 Crim Q1 is word for word the specimen question in `2022 PYP/Sample Question for Criminal Litigation Practice & Procedure.pdf` ("SQ22"), whose suggested answer is the only official key for it.
- **PYP 2021** — `2021 PYP/CRI 2021 Paper.pdf` (Tue 7 Dec 2021; Q1 Bill, 60 marks; Q2 seven short questions, 40 marks) and `2021 PYP/FAM 2021 Paper.pdf` (Thu 9 Dec 2021; Christine and Ken; no marks printed). Set under the CPC 2012 Rev Ed and old Women's Charter numbering; answers give the current law.
- **SQ** — the 2026 Sample Questions: Crim Q1 (Mr Loh Kee, "[Part B 2025S1]", 25 marks; answer guide SQ p123–125) and Fam Q (Celeste, "[Part B 2024]"; answer guide SQ p126–127). These guides, and SQ22, are the only official answers; every other answer is this project's own.

**Left out.** PYP 2021 Crim Q2.5 (whether three accused may be jointly tried) and Q2.7 (challenging a CCDC ruling in the General Division) test points that are not in the coverage list and have no source in the course materials or the pack (CL7 s9: criminal revision is not in the syllabus), so they are not answered here rather than answered by guesswork. No 2024 paper, and no 2018–2020 PCP paper, is held.

Self-study only — never use this file with a live quiz, the Mock Exam or another assessment (Handbook §7.11). The 2025 paper is the closest to 2026: if you mean to sit it unseen as a Practice Paper (Drill 10), skip the questions tagged `PYP 2025`.

---

# Part 1 — Questions by Topic and Sub-point

## 0 · Criminal Litigation Practice

### 0.I Taking instructions and preliminary advice

Sub-points 0.I.1–0.I.4. Tested: 0.I.1 (SQ), 0.I.3 (2023), 0.I.4 (2023, 2025). Own question C1 covers 0.I.2.

### 0.I.1 — Client seen before charge: statements, false information, destroying evidence

**SQ Crim Q1 facts.** Mr Loh Kee ("Mr Loh") has been called by Ang Mo Kio Police Division to attend an interview next week about a case of criminal intimidation at Shaw Theatres NEX (s 506 Penal Code 1871). An avid Marvel fan, he had queued overnight for an Avengers premiere. The person in front of him kept using his phone at full brightness and talking loudly about spoilers. After several failed attempts to stop him, Mr Loh leaned forward and whispered, "If you don't shut up, I'll make sure you never watch another Marvel movie again", and showed him a small penknife he was carrying. Mr Loh says: "The guy is overreacting! I wasn't really going to do anything – I just wanted to watch the movie in peace. Can I tell the police the penknife was just a fake cosplay prop? My friend who works at the cinema can delete the CCTV footage. Also, what will happen if they charge me?"

**QSQ-1-1** · `0.I.1` `0.I.4` · SQ Crim Q1.1; official guide SQ p123 · 5 marks · `pcp-w-0-1` `pcp-w-0-4`

Advise Mr Loh on his proposed course of action and what he should do during the police interview.

**Answer.**

The issue is whether Mr Loh may tell the police the penknife was a fake prop and have the CCTV deleted, and how he should approach the interview. He must do neither: each would be a further offence, and I cannot help him to do either. He should give a truthful account, knowing that what he says may be used to charge and convict him.

*Deleting the CCTV.* Concealing evidence or screening an offender is an offence under s 201 PC, and destroying evidence to obstruct the course of justice is an offence under s 204A PC. If Mr Loh's friend deletes the footage at his request, both would be exposed to charges more serious than the intimidation itself, and the deletion would destroy Mr Loh's credibility at any trial. I must advise him firmly against it.

*The "cosplay prop" story.* Giving false information to a public servant is an offence under s 182 PC (and a false declaration under s 200 PC). The penknife was real, so telling the police it was a prop would be false. A legal practitioner must not concoct any evidence or contrive any fact, whether or not it would advance the client's case (r 9(2)(g)–(h) Legal Profession (Professional Conduct) Rules 2015 ("PCR")), so I cannot help frame that account.

*The interview.* The investigating officer will record a statement under s 22 of the Criminal Procedure Code 2010 ("CPC"). Admissions in it may be relied on to charge him and later to convict him, and a later account that departs from it will damage his case. I would take his full instructions first, including what exactly he said and showed, and his connection (if any) with the complainant (CL1 s5–7). He should give a truthful account; his explanation that he meant only to stop the disturbance, not to carry out a threat, can be given honestly. Since a charge is possible, he should also line up a bailor (a Singapore citizen or PR above 21, not a bankrupt and not involved in the case) (Pre-write 0-1).

Therefore I would advise Mr Loh not to have the footage deleted and not to say the knife was a prop, to give a truthful s 22 statement understanding how it may be used, and to prepare a bailor in case he is charged. I would record this advice in an attendance note (r 5 PCR; Pre-write 0-4).

### 0.I.2 — Client seen after charge: statements, defences, alibi, advising on plea

**Own question C1 facts.** Daniel ("D"), 34, a Singapore citizen, was charged in the State Courts this morning with outraging the modesty of a woman on an MRT train on 3 March at about 8.15am (s 354(1) PC). When the charge was read to him at the police station he gave a cautioned statement saying only "I am innocent". He tells you that at 8.15am on 3 March he was at a café in Tampines with his colleague Farid, and he has a receipt timed 8.09am.

**Q0-C1-1** · `0.I.2` `0.I.4` `0.VI.2` · own question · 8 marks · `pcp-w-0-2` `pcp-w-0-4` `pcp-w-0-26`

Advise D on the steps you will take now that he has been charged, including how he can rely on his account of being at the café.

**Answer.**

The issue is what D needs, now that he is charged, before he decides how to plead, and how he may run his account that he was elsewhere. I would examine the charge against his instructions, explain his statements, give notice of alibi, and then advise him whether to plead guilty or claim trial; the decision is his.

*Charge and statements.* I would break the s 354(1) PC charge into its elements and take detailed instructions on each. I would explain the two investigation statements: the long statement recorded during investigations under s 22 CPC and the cautioned statement recorded when the charge was presented under s 23 CPC; admissions in either may found a conviction. D said only "I am innocent" when charged and did not mention the café. If he relies on it at trial, the court may draw an inference from his failure to mention, when charged, a fact he later relies on and could reasonably have been expected to mention (s 261(1) CPC) (Pre-write 0-26). He must be ready to explain why he did not.

*Alibi.* D's account is evidence that, being elsewhere at the time, he was not at the scene: "evidence in support of an alibi" (s 278(10) CPC). Without the court's permission he may not offer it unless he gives notice of its particulars, and may not call Farid unless the notice gives Farid's name and address (s 278(1)–(2)). Notice is given to the court when first charged, or in writing to the Public Prosecutor within 14 days of first being charged in court (s 278(5)). I would therefore give notice within 14 days, naming Farid and the café, and secure the receipt and any café CCTV at once.

*Advice on plea.* I must advise D whether to plead guilty or claim trial (r 14(5)(a)(i) PCR), and his choice governs. If the alibi checks out, claiming trial is realistic; I would also consider representations to the AGC, enclosing the receipt, seeking withdrawal on evidential grounds (Pre-write 0-8). I would record my advice and his instructions in an attendance note and make no promise of outcome (r 5 PCR; CL1 s15–17).

Therefore I would give notice of alibi under s 278 CPC within 14 days, gather the receipt, CCTV and Farid's evidence, consider representations to the AGC, and advise D in writing on plea, the decision being his (Pre-write 0-2).

### 0.I.3 — Getting seized evidence and the client's own statements

**PYP 2023 Crim Q1 facts.** Mr Ang Chiao Chin ("Mr ACC") comes to your office from Tanglin Police Station with a Notice of Summons to attend a Mention the next day (1 April 2023) in Magistrate Court 4B. A woman unknown to him, Miss Victoria Ong, claimed that he touched her 9-year-old son, Tim ("the Victim"), at Gardens by the Bay at about 2.15pm on 31 March 2023. The charge is for using criminal force on the Victim by touching his crotch over his shorts, punishable under s 354(2) PC. Mr ACC's response to the charge was "I am sorry. I plead for leniency." He now tells you: "I am innocent. I did not touch anyone. My hand may have accidentally come into contact with the Victim's crotch when I bent down near him to tie my shoelaces."

**Q2023-1-2** · `0.I.3` `0.V.1` `0.V.2` `0.V.4` · PYP 2023 Q1.2 · 12 marks · `pcp-w-0-3` `pcp-w-0-19` `pcp-w-0-20` `pcp-w-0-22`

Mr ACC says the police recorded a statement from him that took about 2 hours, in which he categorically denied any intention to use criminal force on the Victim. It is different from the documents he gave you. He was not given a copy. He wants to know whether you can obtain a copy, and if so when. Please advise him.

**Answer.**

The issue is whether and when Mr ACC can obtain a copy of his two-hour long statement. He has no right to an immediate copy. He will get it through the criminal case disclosure conference ("CCDC") procedure, in the Case for the Prosecution ("CFP") or the Prosecution's Supplementary Bundle ("PSB"); but because his case is in the Magistrate's Court the CCDC applies only if both sides opt in, which I would advise. Failing that, I would ask for it under the Prosecution's *Kadar* obligations.

*Which statements.* Mr ACC has given two statements: the s 22 CPC long statement recorded during investigations (the two-hour statement, a denial), and the s 23 CPC cautioned statement recorded when the charge was presented ("I am sorry. I plead for leniency"), which he has. The *Goldring* right of access covers documents he owned or controlled immediately before they were seized (*PP v Goldring Timothy Nicholas* [2014] 1 SLR 586), not a statement recorded by the police, so it does not help here.

*Under the CCDC.* The CFP must include any written statement of the accused recorded by a law enforcement officer that the Prosecution intends to adduce (s 162(1)(e) CPC); the PSB must include every other written statement of the accused relating to the charges proceeded with (s 166(1)(a)). The CFP is due within 2 weeks of the first CCDC (s 161(2)); the PSB within 2 weeks of service of the Case for the Defence ("CFD"), which is itself due within 2 weeks of the second CCDC (ss 163(1), 166(1)). So if the Prosecution relies on the long statement it comes with the CFP; if not, with the PSB.

*Does the CCDC apply?* It applies to offences in the Second Schedule to be tried in a District Court (s 159 CPC) and to all High Court cases (s 212). Mr ACC's case is fixed in the Magistrate's Court, so it applies only if both the Prosecution and the Defence consent (s 159(3)). Opting in gets him his statements, the Prosecution's summary of facts and its lists of witnesses and exhibits. The price is that he must file a CFD setting out his defence (accident) and the facts supporting it (s 165(1)); it can be used to cross-examine him if his evidence departs from it (s 258A), and departures can found adverse inferences (s 169) (Pre-write 0-21). Since his instructions are now firm, opting in is to his advantage. I would write to the Prosecution proposing to opt in under s 159(3).

*If the Prosecution will not opt in.* The long statement is a denial and so tends to strengthen the defence. Unused material that tends to undermine the Prosecution's case or strengthen the Defence, is likely to be admissible, and might reasonably be regarded as prima facie credible and relevant must be disclosed before trial at the latest (*Muhammad bin Kadar v PP* [2011] 3 SLR 1205 at [113]; ss 221A and 221D CPC) (Pre-write 0-22). I would request it on that basis.

*A caution.* The cautioned statement ("I am sorry. I plead for leniency") is an apparent admission. The long statement's denial will help him explain it, which is a further reason to get it before he decides on plea.

Therefore Mr ACC cannot have the statement now, but I would propose opting in to the CCDC under s 159(3) so that he receives it in the CFP (within 2 weeks of the first CCDC) or the PSB (within 2 weeks after his CFD), and in any event request it under *Kadar* before trial.

### 0.I.4 — Ethics with the client: confession, changing instructions, belief in guilt

**Q2023-1-1** · `0.I.4` `0.I.2` `0.IV.2` · PYP 2023 Q1.1 · 12 marks · `pcp-w-0-4` `pcp-w-0-2` `pcp-w-0-13`

*Facts: PYP 2023 Crim Q1, under 0.I.3 above.* You ask Mr ACC how his hand could have touched the Victim's crotch while he was tying his shoelaces. He hesitates for a few minutes and says, "I don't know. I think the Victim knocked into me. I did not even see him before he knocked into me." Mr ACC wants to know if you believe him enough to represent him. Please advise him.

**Answer.**

The issue is whether my view of Mr ACC's credibility affects whether, and how, I represent him, given that his account has shifted from "I am sorry, I plead for leniency" to "I did not touch anyone" to "the Victim knocked into me". My belief is not the test. I may and should represent him, take careful instructions on the inconsistencies, advise him on how his statements will be used and on plea, and act on his instructions so long as I put forward nothing I know to be false.

*My opinion of guilt is irrelevant.* A practitioner representing an accused must not express a personal opinion on whether the accused is guilty, nor allow that opinion to affect his professional assessment of the facts or law, his conduct of the proceedings, or his duty to the accused or the court (r 14(3)(b) PCR). I would tell Mr ACC that it is not my role to decide whether I believe him; my role is to advise him on the evidence and present his case. He has not confessed to me, so r 14(4) PCR (which forbids running anything inconsistent with a confession) is not engaged: his accounts are inconsistent, not an admission.

*My duties.* I must be honest with him and tell him everything that may reasonably affect his interests, act with reasonable diligence and competence, follow his lawful instructions, and keep contemporaneous records of his instructions and my advice (r 5 PCR). I must pursue every reasonable defence (r 14(2)) but must not concoct evidence or contrive facts (r 9(2)(g)–(h)), so I cannot suggest a version of events to him. I must make no promise about the outcome and should keep an attendance note (CL1 s15–17).

*The inconsistencies.* I would explain candidly how they will look. His cautioned statement under s 23 CPC ("I am sorry. I plead for leniency") reads as an admission and can be used against him; his long statement under s 22 denied any intention; and at trial the Prosecution will put each version to him. The accounts are not wholly irreconcilable (accidental contact in a crowd, whether he bent down or was knocked into), but he must settle on what actually happened. I would take a detailed account, test it against the location and any CCTV, and identify witnesses (to be interviewed separately, without him present). The fault element of s 354(2) is intention or knowledge that the touching would outrage modesty; accident denies it.

*Plea.* I must advise him whether to plead guilty or claim trial (r 14(5)(a)(i) PCR). If he maintains accident he cannot plead guilty, because saying in mitigation that the contact was accidental would qualify his plea and the court would have to reject it (s 228(4) CPC; *Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]) (Pre-write 0-13). If he decides to plead guilty after advice, he must accept every element. The decision is his.

Therefore I would tell Mr ACC that whether I believe him does not decide whether I act for him; I will represent him on his instructions, record those instructions and my advice, explain the risk his cautioned statement poses, and advise him on plea, but I will not present any account he tells me is untrue.

**PYP 2025 Crim Q1 facts.** On 1 June 2025 Mr Albert is charged under s 354(1) PC: "That you, on 1 January 2024 at about 1am, at the No Regrets Nightclub, did use criminal force on one Ms. Bebe, intending to outrage her modesty, to wit, by placing your hand on her right buttock". He swears he did no such thing. At the New Year celebration a woman turned around and accused him of molesting her; the police came at once and recorded a long statement from him in the wee hours. He was extremely tired and did not read it properly before signing it, and he can no longer recall what he said. His first Mention is tomorrow, 2 June 2025. [At trial (1.4) the Case for the Prosecution includes his long statement: "I did touch Ms. Bebe's buttock. However, I only did it in a moment of drunken impulse. I am sorry!"]

**Q2025-1-5** · `0.I.4` · PYP 2025 Q1.5 · 3 marks · `pcp-w-0-4`

During the trial, Mr Albert undergoes a rigorous cross-examination by the prosecutor. Afterwards he tells you in private: "Alright, I admit it, I did molest Ms. Bebe. But I want you to continue to defend me and tell the judge I am innocent." What do you do?

**Answer.**

The issue is whether I may continue to act for Mr Albert after his confession to me, and on what terms. I may continue, but I must not adduce any evidence or make any submission inconsistent with his confession, so I cannot tell the judge he is innocent.

Where an accused confesses to his legal practitioner, the practitioner may continue to represent him but must not adduce any evidence or make any submission inconsistent with the confession (r 14(4) PCR). A practitioner must not knowingly mislead the court (r 9(2)(a)) or knowingly assist or permit the client to do so (r 10(6)(a)). Where he knows the client has given false evidence, he must cease to act or, if he continues, conduct the case so as not to perpetuate the falsehood (r 10(4)), and he may withdraw where necessary to avoid breaching the Rules (r 26(5)(f)).

Mr Albert has already testified that he did not touch Ms Bebe, which he now says was false. I would explain to him that I cannot submit that he is innocent, call further evidence of his innocence, or rely on his denial in closing. I may still test whether the Prosecution has proved its case, without asserting a positive case inconsistent with his confession. Because his false evidence is already before the court, I must either cease to act or continue only on terms that do not perpetuate it; I would tell him so, and that if he insists I present him as innocent I will withdraw. I would also advise him on the option of changing his plea and on mitigation.

Therefore I would tell Mr Albert I cannot tell the judge he is innocent; I would continue only within r 14(4) and r 10(4) PCR, withdraw if he insists otherwise, and record his instructions and my advice in writing.

*See also:* QSQ-1-1 (under 0.I.1, no promises and attendance notes); Q0-C1-1 (under 0.I.2).

### 0.II Bail

Sub-points 0.II.1–0.II.4. Tested: 0.II.2 (SQ, 2025), 0.II.3 (2025), 0.II.4 (2021). Own question C2 covers 0.II.1.

### 0.II.1 — Agency and court bail; bailable offences

**Own question C2 facts.** Lee ("L"), a Malaysian national who lives in Johor Bahru and commutes to work in Singapore on a work permit, has been charged with an offence that the First Schedule to the CPC shows as bailable and punishable with imprisonment. The Prosecution tells you it will object to bail because L lives outside Singapore.

**Q0-C2-1** · `0.II.1` `0.II.4` · own question · 6 marks · `pcp-w-0-5` `pcp-w-0-7`

Advise L whether he will be released on bail.

**Answer.**

The issue is whether L, charged with a bailable offence, will be released on bail. He is prima facie entitled to bail as of right, but because the offence is punishable with imprisonment the court may refuse it on a prescribed ground; the realistic outcome is bail on conditions.

Agency (police) bail is usually granted before charge; after charge, bail is granted by the court. Whether an offence is bailable is shown in the fifth column of the First Schedule to the CPC. For a bailable offence the accused "must be released" on bail (s 92(1) CPC). But where the offence is punishable with imprisonment, the court may refuse bail if it believes, on the grounds prescribed in r 5 of the Criminal Procedure Rules 2018, that he will not attend court (s 92(3)). The prescribed grounds mix facts, such as the accused not being a citizen or permanent resident or not being domiciled in Singapore, with factors such as the seriousness of the offence and likely sentence, the strength of the evidence, and preparatory acts showing an intention not to surrender (CL1 s22).

L is a foreigner who lives in Johor, so the Prosecution has a prescribed ground to rely on. I would answer it with his ties and with conditions: his job here depends on his work permit, he travels here daily, and he has every reason to attend. I would offer the statutory conditions that he surrender his travel documents and attend court as appointed (s 94(1)), not leave Singapore without permission (s 99), and electronic tagging if needed (s 94(2)–(3)). A Singapore address for the period of bail would meet the practical problem that surrendering his passport stops him going home to Johor. The bailor must be a Singapore citizen or PR above 21, not a bankrupt and not involved in the case; the amount is set so that the bailor will not shirk his duties (*Ewe Pang Kooi v PP* [2015] 2 SLR 672). I may not stand bail myself (r 14(3)(a) PCR) (Pre-writes 0-5, 0-7).

Therefore L should be released on bail as of right unless the court accepts the prescribed ground; I would meet the Prosecution's objection with a Singapore address, surrender of his passport, a no-travel condition and a suitable bailor.

### 0.II.2 — Non-bailable offences: discretion, onus, Yang Yin factors

**QSQ-1-2** · `0.II.2` `0.II.4` · SQ Crim Q1.2; official guide SQ p123–124 · 5 marks · `pcp-w-0-6` `pcp-w-0-7`

*Facts: SQ Crim Q1, under 0.I.1 above.* Mr Loh asks: "If they charge me, will I be locked up immediately? I cannot go to prison – I am a secondary school teacher, and I will lose my job! I also have a mortgage to pay and elderly parents to support." Advise Mr Loh on the possibility of bail.

**Answer.**

The issue is whether Mr Loh, if charged with criminal intimidation (s 506 PC), a non-bailable offence, will be released on bail. Bail is at the court's discretion and the onus is on him; on the *Yang Yin* factors he is likely to be granted bail.

For a non-bailable offence the accused "may be released" on bail at the discretion of the police or the court (s 93(1) CPC), and the onus is on him to persuade the court to exercise its discretion in his favour (*S Selvamsylvester v PP* [2005] 4 SLR(R) 409). The court weighs the factors in *PP v Yang Yin* [2015] 2 SLR 78: whether there are reasonable grounds for believing the accused is guilty; the nature and gravity of the offence; the severity of the likely punishment; the danger of absconding; his character, means and standing; the danger of the offence being repeated; the danger of witnesses being tampered with; whether bail is needed to prepare the defence; and the length of detention. Bail must not be granted where the offence is punishable with death or life imprisonment (s 95(1)(a)), which is not this case.

*Application.* Gravity: a whispered threat about a film, with a small penknife shown, is serious (a weapon was involved) but not of the gravest kind. Absconding: Mr Loh is a secondary school teacher with a mortgage and elderly parents in Singapore; these ties make flight unlikely. Character: nothing suggests antecedents. Witnesses: the complainant is a stranger in a cinema, so there is little risk of interference. Repetition: the incident arose from a specific provocation. Each factor favours release, and any concern can be met by conditions such as surrender of his passport (s 94(1)) and a suitable bailor (Pre-write 0-7).

Therefore Mr Loh is unlikely to be kept in remand: although bail for s 506 PC is discretionary and the onus is on him, the *Yang Yin* factors favour release on standard conditions with a bailor.

### 0.II.3 — Exceptions to bail and carve-outs (s 95 CPC)

**Q2025-1-1** · `0.II.3` `0.II.2` `0.II.4` · PYP 2025 Q1.1 · 7 marks · `pcp-w-0-6` `pcp-w-0-7`

*Facts: PYP 2025 Crim Q1, under 0.I.4 above.* Mr Albert asks: "Will the Court allow me to go out on bail? I have a wife and kid in Thailand. I spend half of the year in Singapore and half of the year in Thailand with them. If I'm locked up in Singapore, I will not be able to communicate with them at all."

**Answer.**

The issue is whether Mr Albert, charged with outrage of modesty (s 354(1) PC), a non-bailable offence, will be released on bail. Bail is discretionary and he bears the onus; no statutory bar applies, and although his ties to Thailand point to a risk of flight, the court is likely to grant bail on conditions such as surrender of his passport and a higher amount.

*Non-bailable offence: discretion.* For a non-bailable offence the accused "may be released" on bail (s 93(1) CPC), and the onus is on him to persuade the court (*S Selvamsylvester v PP* [2005] 4 SLR(R) 409). The court weighs the *Yang Yin* factors, including the gravity of the offence and likely punishment, the danger of absconding, his character and standing, and the danger of interference with witnesses (*PP v Yang Yin* [2015] 2 SLR 78).

*No statutory bar.* Bail must not be granted where the offence is punishable with death or life imprisonment, or where the court believes on prescribed grounds that the accused will not attend (s 95(1) CPC), subject to carve-outs for, for example, juveniles and the sick or infirm (s 95(2)). Section 354(1) PC carries neither death nor life imprisonment, so s 95(1)(a) does not apply; the real question is attendance.

*Application of the factors.* Gravity: touching a stranger's buttock in a nightclub is serious but not of the gravest kind; s 354(1) carries up to 3 years' imprisonment. Absconding: this is the Prosecution's strongest point. Mr Albert spends half the year in Thailand, where his wife and child live, and his main family ties are abroad. But he has evidently lived in Singapore half the year, did not leave when the investigation was pending for six months, and attended when called. Character: no antecedents are mentioned. Witnesses: Ms Bebe is a stranger, so there is little risk of interference.

*Conditions and alternatives.* The flight risk is usually met by conditions and a higher amount rather than refusal (CL1 s24, s26). I would offer surrender of his passport, no leaving Singapore without permission, reporting, and electronic tagging if the court wants it (ss 94, 99 CPC), with a substantial sum from a bailor who is a Singapore citizen or PR above 21 and not a bankrupt; above $15,000 the bail must be in cash or cash equivalents (*Ewe Pang Kooi v PP* [2015] 2 SLR 672). Because s 354(1) carries not more than 7 years' imprisonment, I would also ask the Prosecution whether it will consent to his release on his own personal bond (s 93(1A)) (Pre-writes 0-6, 0-7). He can keep in touch with his family by phone and video while on bail; the condition he will feel is the bar on travelling to Thailand without permission.

Therefore Mr Albert is likely to be granted bail, but on conditions: he should expect to surrender his passport and be unable to travel to Thailand without the court's permission, and he should line up a bailor able to furnish a substantial sum.

### 0.II.4 — Bail conditions, breach, quantum, the bailor and the surety's duties

**Q2021-2-4** · `0.II.4` · PYP 2021 Q2.4 · 5 marks · `pcp-w-0-7`

An accused has been charged in court for an offence and is subsequently bailed out by a surety. What are the duties of the surety and what are the consequences if the accused does not turn up for court?

**Answer.**

The issue is what a surety must do and what follows if the accused fails to attend. The surety must ensure the accused attends, keep in contact with him, report loss of contact within 24 hours and ensure he stays in Singapore; if the accused fails to attend, he may be arrested without warrant, commits an offence by absconding, and the bond may be forfeited against the surety.

*Duties.* A surety must ensure that the released person attends court as required, keep in daily communication with him, lodge a police report within 24 hours of losing contact with him, and ensure he remains in Singapore unless permitted to leave (s 104 CPC). The surety is told of these duties on signing the bail bond. A surety who no longer wishes to stand may apply to be discharged from the bond (s 105), going through the court process and informing the Prosecution; a surety who believes the accused will not attend may tell the police and ask to be relieved, and the accused may then be arrested (s 103(3)(b)) (Cyril-Exam CS1).

*Consequences of non-attendance.* An accused who breaches a bail condition, including attending court, may be arrested without warrant, and the court then decides whether to grant bail again (s 103 CPC); absconding while on bail is itself an offence (s 103(5)). If the accused fails without reasonable excuse to attend, the court must forfeit the bond and may call on each surety to show cause why the bond should not be forfeited as against him (s 107A). The quantum of bail is set precisely so that the surety, whose money is at stake, will not shirk these duties (*Ewe Pang Kooi v PP* [2015] 2 SLR 672).

Therefore the surety's duties are to secure attendance, stay in contact, report loss of contact within 24 hours and keep the accused in Singapore; if the accused fails to turn up he faces arrest and a further charge, and the surety faces forfeiture of the bail sum (Pre-write 0-7).

*See also:* Q2025-1-1 (under 0.II.3, conditions for a flight risk); QSQ-1-2 (under 0.II.2); Q0-C2-1 (under 0.II.1).

### 0.III Pre-trial negotiations

Sub-points 0.III.1–0.III.4. Tested: 0.III.1–0.III.3 (2025 Q2.1). Own question C3 covers 0.III.4, which PYP 2025 Q2.2 (under 0.IV.5) also touches.

### 0.III.1 — Representations to the AGC and police; CCMS; without prejudice privilege

See Q2025-2-1 under 0.III.3 (representations as an option to avoid prosecution) and Q2025-1-3 under 0.V.4 (a CCMS discussion).

### 0.III.2 — Withdrawal of charges and warnings

See Q2025-2-1 under 0.III.3 (withdrawal with a stern or conditional warning).

### 0.III.3 — Composition of offences (s 241 CPC, Fourth Schedule)

**PYP 2025 Crim Q2 facts.** Ms Wing, 50, with no prior criminal record, has struggled with grief since her pet parrot died two years ago and appears to have developed an unusual attachment to birds. On nocturnal visits to Bird Paradise she allegedly "liberated" several macaws. She faces six charges: (1) criminal trespass into Bird Paradise, 4 April 2025, 3.52am (s 447 PC); (2) theft of a red macaw, 4 April 2025, 4.19am (s 380 PC); (3) criminal trespass, 11 April 2025, 11.42pm (s 447); (4) theft of a blue macaw, 11 April 2025, 11.58pm (s 380); (5) criminal trespass, 18 April 2025, 2.03am (s 447); (6) theft of a green macaw, 18 April 2025, 3.14am (s 380).

**Q2025-2-1** · `0.III.3` `0.III.1` `0.III.2` · PYP 2025 Q2.1 · 5 marks · `pcp-w-0-10` `pcp-w-0-8` `pcp-w-0-9`

Ms Wing tells you, "Look, I'm really sorry I took the birds. I won't ever do this again. Is there any way I can settle this privately with the park or avoid being prosecuted?" Advise Ms Wing on the available pre-trial options that might help her avoid formal prosecution.

**Answer.**

The issue is whether Ms Wing can settle with the park or avoid prosecution. She can compound the three trespass charges with the park, but not the thefts; for the thefts her route is representations to the AGC seeking withdrawal, ideally with a warning.

*Composition.* Offences listed in the Fourth Schedule to the CPC may be compounded, usually on payment of compensation, with the consent of the person entitled to compound and, once investigations have begun, of the Public Prosecutor (s 241(1) CPC). Once an offence is compounded no further proceedings may be taken and the court must order a discharge amounting to an acquittal (s 241(4)–(5)). Criminal trespass (s 447 PC) is listed, compoundable by the person in possession of the property; theft (ss 379, 380 PC) is not (CPC Fourth Schedule, Part 1). So Ms Wing may approach Bird Paradise, with the Public Prosecutor's consent, to compound Charges 1, 3 and 5, for example by compensating the park and returning or paying for the birds. She should know that a compounded offence is presumptive proof of an admission of guilt and may be a relevant factor if she is ever sentenced for a later offence (*Teo Seng Tiong v PP* [2021] 2 SLR 642 at [101]–[102]) (Pre-write 0-10).

*Representations.* For the theft charges she may make written representations to the AGC (or discuss the case with the prosecutor at the CCMS), seeking withdrawal on public-interest grounds: she is 50, has no record, is remorseful, the offences grew out of grief and possibly depression, and she will make restitution. Representations made in plea negotiations are without prejudice, with no express agreement needed (*PP v Knight Glenn Jeyasingam* [1999] 1 SLR(R) 1165 at [72]); they should be marked so, supported by documents (a psychiatric report, proof of restitution) and must state that her attention has been drawn to s 182 PC (at [49]) (Pre-write 0-8).

*Withdrawal and warnings.* Withdrawal may be unconditional or with a warning. A stern warning leads to a discharge amounting to an acquittal; a conditional warning (typically 12 or 24 months) leads to a discharge not amounting to an acquittal, and the charge may be revived if she re-offends within the period (CL2 s12). A warning is only the authority's opinion that an offence was committed, not a finding of guilt (*Wham Kwok Han Jolovan v A-G* [2016] 1 SLR 1370 at [34]), and cannot be treated as an aggravating factor later (*Teo Seng Tiong* at [88]; *GCO v PP* [2019] 3 SLR 1402 at [69]) (Pre-write 0-9). Three thefts on three separate nights make outright withdrawal hard to obtain, and no outcome can be promised.

Therefore Ms Wing should seek to compound the trespass charges with Bird Paradise, with the Public Prosecutor's consent, and make without prejudice representations to the AGC for withdrawal of the theft charges with a warning; if that fails, she should seek a favourable plea offer.

### 0.III.4 — Plea offers: proceeded and TIC charges, reduced charges, negotiating the SOF

**Own question C3 facts.** Wei ("W"), 23, faces five charges of theft in dwelling (s 380 PC) for taking items from the homes of five relatives over three months. The Prosecution offers that W plead guilty to three charges, with the other two taken into consideration. W wants the best deal you can get.

**Q0-C3-1** · `0.III.4` `0.IV.5` `0.VII.3` · own question · 8 marks · `pcp-w-0-11` `pcp-w-0-16` `pcp-w-0-36`

How would you respond to the Prosecution's offer?

**Answer.**

The issue is how to respond to the plea offer and what W can negotiate. I would ask the Prosecution to proceed on two charges rather than three, or to reduce the proceeded charges to theft under s 379 PC, and agree the Statement of Facts ("SOF") and its sentencing position before advising W.

In most cases the Prosecution offers a position on a plea of guilt, varying the number of charges proceeded with or reducing or amending charges (CL2 s17). Proceeded charges lead to conviction and sentence; the remaining charges are not convicted but, with the accused's consent, are taken into consideration ("TIC") in sentencing (s 148(1) CPC), which usually increases the sentence on the proceeded charges, though by less than convictions would (*Lim Hsien Hwei v PP* [2014] 3 SLR 15 at [22]) (Pre-write 0-16).

*Number of charges.* Where an accused is sentenced to imprisonment for at least three distinct offences, at least two terms must run consecutively (s 307(1) CPC). On three proceeded charges W faces at least two consecutive terms. If the Prosecution proceeds on two and takes three into consideration, s 307(1) is not engaged and the court has a free hand. The thefts were on separate occasions, so it may still order consecutive terms under the one-transaction rule (*Mohamed Shouffee bin Adam v PP* [2014] 2 SLR 998), but it is not compelled to. This is the illustration in CL2 s18.

*Reduced charges.* Alternatively I would ask for the proceeded charges to be reduced from s 380 to s 379 PC, which has no mandatory imprisonment.

*SOF and sentence.* I would ask for the draft SOF, go through it with W, and resolve any disputed facts that do not go to the elements; the elements themselves are not negotiable. I would ask for the Prosecution's sentencing position and try to persuade it lower, relying on W's youth, restitution and remorse (Cyril-Exam CS1–2). W must admit the TIC offences for them to be taken into consideration.

Therefore I would counter-propose two proceeded charges (or s 379 charges), agree the SOF and sentencing position, explain to W the effect of the TIC charges, and confirm his instructions to plead guilty in writing, promising no outcome (Pre-write 0-11).

### 0.IV Pleading guilty and the sentencing hearing

Sub-points 0.IV.1–0.IV.8. Tested: 0.IV.2 (2021, 2022, 2023, SQ), 0.IV.4 (2021, 2022, 2023, 2025, SQ), 0.IV.5 (2021, 2023, 2025), 0.IV.7 (2023, 2025). Own questions C4 (0.IV.1, 0.IV.8), C5 (0.IV.3) and C6 (0.IV.6).

### 0.IV.1 — The PG mention and a valid plea

**Own question C4 facts.** Ravi ("R"), 45, is charged with voluntarily causing hurt to his neighbour. He wants to plead guilty at the next mention "to get it over with". During your interview he says he has been treated for schizophrenia, stopped his medication a month ago, and at times does not seem to follow your questions.

**Q0-C4-1** · `0.IV.1` `0.IV.8` · own question · 8 marks · `pcp-w-0-12`

Advise R on what must happen for his plea of guilty to be validly recorded, and on what you should do about his mental state.

**Answer.**

The issue is whether R can validly plead guilty and whether his mental state prevents it. His plea will be valid only if he understands the nature and consequences of the plea and intends to admit the offence without qualification; given his history and present confusion, I should obtain a psychiatric assessment before he pleads, and the court may have to inquire into his fitness.

*A valid plea.* If the accused pleads guilty after the charge is read and explained, the plea is recorded and he may be convicted on it (s 227(1) CPC). Where he is represented, the court must record the advocate's confirmation that he understands the nature and consequences of the plea and intends to admit the offence without qualification (s 227(2)(b)). "Nature" means he knows exactly what he is charged with, in practice each element; "consequences" means he knows the punishment prescribed (*Balasubramanian Palaniappa Vaiyapuri v PP* [2002] 1 SLR(R) 138 at [25]). He must also understand that once convicted on his plea he cannot appeal against conviction, only sentence (s 375 CPC). I could not honestly give the s 227(2)(b) confirmation if I doubted that R understood these things.

*Fitness to plead.* Where the court has reason to suspect that the accused, through unsoundness of mind or any physical or mental condition, is incapable of making his defence, it must first investigate (s 247(1) CPC); it may receive a medical certificate or oral medical evidence (s 247(3)) and, if not satisfied that he is capable, must postpone and remand him for observation in a psychiatric institution for up to one month (s 247(4)). On the designated medical practitioner's certificate the court must, unless satisfied to the contrary, find him capable or incapable (s 248(1)–(2)); if capable it proceeds (s 248(2B)); if incapable, the proceedings are stayed once the court makes an order under s 249(2) or reports the case to the Minister (s 248(2A)).

*Application.* R has stopped his medication and does not always follow questions. I would not let him plead at the next mention. I would obtain a psychiatric report on his present state, his fitness to plead and any link between his condition and the offence, and raise his condition with the court, which may then inquire under s 247. If he is fit, I would go through each element and the punishment with him, explain the bar on appealing conviction and the SOF, and record his instructions in writing. The report may also support mitigation (Pre-write 0-18).

Therefore R should not plead until his fitness is assessed; once fit, his plea is valid only if he admits each element, understands the punishment and the bar in s 375 CPC, and does not qualify it (Pre-write 0-12).

### 0.IV.2 — Qualified plea and retraction (s 228(4) CPC)

**PYP 2023 Crim Q2 facts.** Ms Kew is charged with theft (s 379 PC) of an egg mayonnaise sandwich from a 7-Eleven on 20 October 2023 and of a bottle of Coke Zero from a Cheers store on 25 October 2023. She has two psychiatric reports. The IMH report says she had no psychiatric condition at the time. Her private psychiatrist, Dr Psy Duck ("Dr PD"), says she suffered from Major Depressive Disorder ("MDD") at the time, which started around July 2023 after her husband's death and slightly impaired her ability to make rational decisions, so contributing to the offences. The Prosecution offers to proceed on the sandwich charge with the Coke Zero charge taken into consideration, and will ask for 5 days' imprisonment if she pleads guilty. She has one theft antecedent from 2000.

**Q2023-2-1** · `0.IV.2` `0.IV.7` · PYP 2023 Q2.1 · 10 marks · `pcp-w-0-13` `pcp-w-0-18`

Ms Kew says that she wants to plead guilty. She also tells you to raise in mitigation that she had forgotten to pay for the egg mayonnaise sandwich and promises to be more careful in future. Advise Ms Kew whether this is possible and what the consequences are.

**Answer.**

The issue is whether Ms Kew can plead guilty to theft and say in mitigation that she forgot to pay. She cannot: forgetting to pay denies dishonesty, the fault element of theft, so it qualifies her plea and the court must reject it under s 228(4) CPC. She must choose between an unqualified plea and claiming trial.

*Rule.* Where the court is satisfied that any matter raised in the plea in mitigation materially affects any legal condition required by law to constitute the offence charged, it must reject the plea of guilty (s 228(4) CPC). If mitigation indicates a lack of mens rea or actus reus, the accused has not admitted the offence without qualification and the plea must be rejected (*Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]). This codifies the earlier case law. The course example is exactly this case: theft requires dishonesty (ss 24, 378 PC), and "I forgot to pay" denies it (CL3 s11).

*Application.* If Ms Kew says she forgot to pay, she is saying she did not take the sandwich dishonestly. That goes to an element of s 379 PC, not to sentence. The court must reject her plea and, if she maintains the statement, the case goes to trial. The same would follow if she disputed dishonesty when the SOF was read. A plea that is accepted and later shown to be qualified cannot stand; she could seek to retract a plea only on valid and sufficient grounds showing it is proper and in the interests of justice (*Md Rafiqul*).

*My position.* I must advise her whether to plead guilty or claim trial (r 14(5)(a)(i) PCR), and I cannot help her plead guilty while asserting that she lacked dishonesty. If she genuinely forgot to pay, she has a defence and should claim trial. If she accepts she took it dishonestly, she may plead guilty and I would mitigate on proper grounds: her remorse, her husband's death and the MDD (if proved, see Q2023-2-2), the small value, and her long gap since the 2000 antecedent, which I must not contradict (r 14(8) PCR). A promise to be more careful in future is fine; it is the "forgot to pay" explanation that cannot be made (Pre-write 0-18).

Therefore Ms Kew must either drop the statement that she forgot to pay and plead guilty without qualification, or claim trial; if she pleads guilty and then says it in mitigation, the court must reject her plea under s 228(4) CPC (Pre-write 0-13).

**PYP 2022 Crim Q2 facts.** On Christmas Eve 2021 Brian went to a club with his girlfriend Alice; both drank heavily. Exhausted, Brian left Alice dancing and took a nap on a sofa. Dean, attracted to the inebriated Alice, slid his arm around her waist to steer her to a quieter part of the dance floor. Brian shouted, pulled Dean away, and smashed a glass bottle over his head; Dean lost consciousness. Brian is charged with voluntarily causing hurt with a dangerous weapon (s 324 PC). Dr Ben Tan, a private psychiatrist, reports that Brian had "a psychiatric condition known as morbid jealousy at the time of the offence", with a direct contributory link to the offence, but that it did not impair his awareness of the nature of his actions and he was fit to plead. The IMH psychiatrist, who assessed Brian immediately after arrest, reports no psychiatric disorder.

**Q2022-2-2** · `0.IV.2` `0.IV.1` · PYP 2022 Q2.2 · 5 marks · `pcp-w-0-13` `pcp-w-0-12`

At the Plead-Guilty Mention, Brian said he understood the nature and consequences of his plea and admitted the SOF without qualification, and the Judge convicted him under s 324 PC. After his lawyer read the plea in mitigation, Brian asked to speak and said: "Actually on that night, I had fallen asleep and I was suddenly woken up by a woman screaming. I thought it was Alice's voice, and when I found her, I thought I saw this man touching her breast with his hand. In my groggy state, I thought I was holding my phone in my hand when I used it to hit him on the head to stop him. I didn't know I was holding a bottle of beer!" Does Brian's statement affect his guilty plea?

**Answer.**

The issue is whether Brian's statement, made after conviction and during mitigation, qualifies his plea. It does: saying he thought he was holding his phone denies knowledge that he was using a dangerous weapon, an element of s 324 PC, so the court must reject the plea under s 228(4) CPC unless he withdraws the statement.

Section 228(4) CPC applies to "any matter raised in the plea in mitigation", which includes what Brian himself says to the court before sentence. Where the matter materially affects a legal condition of the offence, the court must reject the plea (*Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]). The offence under s 324 PC is voluntarily causing hurt by means of a dangerous weapon; Brian's statement that he did not know he was holding a bottle denies the knowledge and voluntariness relating to the weapon, which goes to the mental element.

The fact that he has already been convicted does not save the plea. The conviction rests on his unqualified admission of the SOF; once a qualification emerges in mitigation, the court must reject the plea and the matter goes to trial unless the qualification is withdrawn (CL3 s11; Pre-write 0-13). The court should ask Brian, through counsel, whether he maintains the statement. His lawyer should take instructions at once: if Brian accepts that he knew what he was holding and only wishes to explain his state of mind (his belief that Alice was being molested, his grogginess), that can be put as mitigation that does not deny an element; if he maintains that he did not know it was a bottle, he must claim trial. The other parts of his account (provocation, protecting Alice) go to sentence, not to guilt, and do not qualify the plea.

Therefore Brian's statement qualifies his plea; unless he withdraws the claim that he did not know he was holding a bottle, the court must reject the plea under s 228(4) CPC and fix the case for trial.

**QSQ-1-3** · `0.IV.2` `0.IV.4` `0.VII.1` · SQ Crim Q1.3; official guide SQ p124–125 · 7 marks · `pcp-w-0-13` `pcp-w-0-15` `pcp-w-0-34`

*Facts: SQ Crim Q1, under 0.I.1 above.* Mr Loh is charged with one count of criminal intimidation (s 506 PC) and one count of carrying an offensive weapon (s 6(1) Corrosive and Explosive Substances and Offensive Weapons Act 1958). He asks about a lenient sentence: "Look, I just wanted to watch the movie in peace. I wasn't trying to cause alarm or make him do anything – I was just venting my frustration! I happened to be holding my penknife in my hand, and I didn't mean to threaten him at all. Also, I have a private psychiatrist report saying I have obsessive-compulsive disorder that makes me extremely sensitive to disruptions, but the IMH doctor says I was just being unreasonable. How can I make sure the judge considers these points?" Advise Mr Loh.

**Answer.**

The issue is whether Mr Loh can plead guilty while saying he did not mean to threaten, and how he can rely on his OCD diagnosis when IMH disagrees. He cannot say he did not mean to threaten: that qualifies his plea. He can rely on the OCD as mitigation, but because the Prosecution disputes it there will likely be a Newton hearing, at which he must prove it on a balance of probabilities.

*Qualified plea.* "I wasn't trying to cause alarm … I didn't mean to threaten him" goes to the mental element of criminal intimidation, not to sentence; the official guide marks it as a statement that would qualify the plea because it qualifies the mental element (SQ p124). Where mitigation materially affects a legal condition of the offence, the court must reject the plea (s 228(4) CPC; *Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]). If Mr Loh pleads guilty he must accept that he meant to threaten; if he does not, he must claim trial (Pre-write 0-13).

*The OCD.* A mental condition that explains his conduct without denying an element (for example, that OCD made him extremely sensitive to disruption and lowered his self-control) is mitigation, not a qualification. The Prosecution relies on the IMH view, so this is a contested fact material to sentence. After hearing the mitigation the court may hear evidence to determine the truth of matters that may materially affect sentence (s 228(5) CPC): a Newton hearing, held when such a fact is contested (*Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). The burden lies on the party asserting the fact; a fact extraneous to the Prosecution's case and within the accused's knowledge must be proved by the Defence on a balance of probabilities (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]). Mr Loh must therefore call his psychiatrist to explain the diagnosis and its link to the offence, and his counsel will cross-examine the IMH psychiatrist (Pre-write 0-15).

*Why it matters.* If proved, a condition that contributed to the offence may reduce the weight of deterrence and shift the emphasis to rehabilitation (*Lim Ghim Peow v PP* [2014] 4 SLR 1287) (Pre-write 0-34); if not proved, the court sentences on the SOF.

Therefore Mr Loh must drop the claim that he did not mean to threaten if he pleads guilty, and can put the OCD forward as mitigation, which, if the Prosecution maintains its objection, will be tested at a Newton hearing where he bears the burden on a balance of probabilities (*Catherine Chan*).

### 0.IV.3 — The Statement of Facts and disputes about it

**Own question C5 facts.** Tom ("T") will plead guilty to theft in dwelling (s 380 PC) of his employer's watch. He disagrees with three statements in the draft Statement of Facts: (1) that he "took the watch intending to sell it" (he says he meant to borrow it and return it); (2) that he "had planned the theft for a week" (he says he took it on impulse); (3) that he was "wearing a red shirt" (it was blue).

**Q0-C5-1** · `0.IV.3` `0.IV.2` `0.IV.4` · own question · 9 marks · `pcp-w-0-14` `pcp-w-0-13` `pcp-w-0-15`

Advise T on each disputed statement.

**Answer.**

The issue is what T can do about the parts of the SOF he disputes when pleading guilty. The answer depends on whether each fact goes to an element, is material to sentence, or is immaterial.

There is no statutory requirement for an SOF; it helps the court to sentence and to ensure the accused understands his plea (*Mok Swee Kok v PP* [1994] 3 SLR(R) 134 at [14]; *Biplob Hossain Younus Akan v PP* [2011] 3 SLR 2 at [6]). It must contain every element of the charge and every fact material to sentence, aggravating or mitigating (*PP v Andrew Koh Weiwen* [2016] SGHC 103 at [16]). The accused need not admit every fact, so long as what he admits contains all the ingredients of the offence and what he disputes is immaterial (*Chota bin Abdul Razak v PP* [1991] 1 SLR(R) 501 at [16]). Disputes are raised with the Prosecution and ironed out before the hearing where possible (CL3 s17).

*(1) Intention to borrow.* Theft requires dishonesty. Saying he meant only to borrow and return the watch disputes dishonesty, which is an element. If he maintains it he cannot plead guilty: mitigation that denies an element qualifies the plea, which the court must reject (s 228(4) CPC; *Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]), and the case goes to trial. He must either accept the element or claim trial (Pre-write 0-13).

*(2) Planning for a week.* Premeditation is aggravating, so this fact is material to sentence but is not an element. I would ask the Prosecution to remove it, with any evidence of impulse. If it refuses, T may plead guilty with this fact disputed, and the court may hold a Newton hearing (s 228(5) CPC; *Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). Premeditation is part of the Prosecution's aggravating case, so it would bear the burden of proving it beyond reasonable doubt (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]) (Pre-write 0-15).

*(3) Shirt colour.* This is immaterial; the plea can be accepted even if T disputes it (*Chota*). I would still ask for it to be corrected.

Therefore T can plead guilty only if he accepts that he acted dishonestly; the premeditation dispute should be negotiated and, failing that, resolved at a Newton hearing; the shirt colour does not matter (Pre-write 0-14).

### 0.IV.4 — Newton hearing; competing psychiatric reports

**Q2023-2-2** · `0.IV.4` `0.IV.7` `0.VII.1` · PYP 2023 Q2.2 · 10 marks · `pcp-w-0-15` `pcp-w-0-18` `pcp-w-0-34`

*Facts: PYP 2023 Crim Q2, under 0.IV.2 above.* Ms Kew wants to avoid a jail term and to rely on Dr PD's report in mitigation; the Prosecution will rely on the IMH report. Advise her what is likely to happen at the plea of guilty hearing if she insists on relying on Dr PD's report.

**Answer.**

The issue is how the court will deal with Ms Kew's reliance on Dr PD's diagnosis of MDD when the Prosecution relies on the IMH report finding no condition. Because this is a dispute about a fact material to sentence that does not deny an element, the court is likely to hold a Newton hearing, at which Ms Kew must prove the MDD on a balance of probabilities.

*Not a qualified plea.* Dr PD says the MDD "slightly impaired" her ability to make rational decisions; it does not say she did not know what she was doing or lacked dishonesty. Relying on it as an explanation of why she offended is mitigation, not a denial of an element, so the plea stands (contrast Q2023-2-1).

*Newton hearing.* After the plea in mitigation the court may, of its own motion or on application, hear evidence to determine the truth of matters that may materially affect sentence, and attach such weight as it thinks fit (s 228(5) CPC). A Newton hearing is held when a fact material to sentence is contested; it is the exception, and the court may decline if the defence case is absurd or obviously untenable (*Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). A psychiatric condition that may displace imprisonment is plainly material. Where the Prosecution objects to unsubstantiated assertions in mitigation, the defence must withdraw them, prove them to the Prosecution's satisfaction, or call evidence (*PP v Aniza bte Essa* [2009] 3 SLR(R) 327 at [61]).

*Burden.* The party asserting the fact bears the burden. A fact extraneous to the Prosecution's case, which it would not have had to prove at trial, must be proved by the Defence on a balance of probabilities (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]). So Ms Kew must prove the MDD and its contributory link.

*Procedure and evidence.* The hearing runs like a trial: Dr PD and the IMH psychiatrist give evidence and are cross-examined. Dr PD's account has a clear timeline (onset in July 2023 after her husband's death, offences in October 2023) and a stated contributory link; I would test whether IMH took that history into account.

*Stakes.* If the MDD is proved, the court may give less weight to deterrence and more to rehabilitation, since deterrence is less effective where a psychiatric condition affected the offender's choices (*Lim Ghim Peow v PP* [2014] 4 SLR 1287) (Pre-write 0-34); that supports a non-custodial sentence instead of the 5 days sought. If it is not proved, the court sentences on the SOF with her 2000 antecedent in view.

Therefore, if Ms Kew insists on Dr PD's report and the Prosecution maintains its reliance on IMH, the court is likely to convene a Newton hearing under s 228(5) CPC, at which she must prove the MDD on a balance of probabilities; success would strengthen her case against imprisonment (Pre-write 0-15).

**Q2022-2-1** · `0.IV.4` `0.IV.1` · PYP 2022 Q2.1 · 5 marks · `pcp-w-0-15` `pcp-w-0-12`

*Facts: PYP 2022 Crim Q2, under 0.IV.2 above.* Brian intends to plead guilty but wants Dr Ben Tan's report "accepted by the Court" for his mitigation, since the IMH psychiatrist is "definitely biased in favour of the Prosecution". Advise Brian what will happen at the Plead-Guilty Mention if the Prosecution also insists that the IMH report be admitted, and what the Court will consider in deciding between the two reports. Assume Brian accepts the SOF without qualification.

**Answer.**

The issue is how the court will resolve the conflict between Dr Tan's report (morbid jealousy with a direct contributory link) and the IMH report (no disorder). Because the plea is unqualified and the dispute is about a fact material to sentence, the court will likely hold a Newton hearing, where Brian must prove the condition on a balance of probabilities.

Brian's plea is valid: Dr Tan himself says the condition did not impair Brian's awareness of the nature of his actions and that he was fit to plead, so relying on it does not deny an element (contrast Q2022-2-2). Whether he suffered morbid jealousy is a contested fact that may materially affect sentence. After the mitigation the court may hear evidence to determine its truth and attach such weight as it thinks fit (s 228(5) CPC); a Newton hearing is held where such a fact is contested, though not where the defence case is absurd or obviously untenable (*Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). The court will not simply "accept" one report: both psychiatrists give evidence and are cross-examined.

*Burden.* The condition is extraneous to the Prosecution's case and within Brian's knowledge, so he must prove it on a balance of probabilities (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]).

*What the court considers.* It weighs the two experts' evidence: what history each took, when each assessed Brian (IMH immediately after arrest; Dr Tan later), the reasoning for the diagnosis and for the contributory link, and how each stands up in cross-examination. Brian's belief that the IMH psychiatrist is biased is not evidence; any criticism must be put to the witness. If the condition and its link are proved, deterrence may weigh less and rehabilitation more (*Lim Ghim Peow v PP* [2014] 4 SLR 1287) (Pre-write 0-34).

Therefore the court is likely to hold a Newton hearing at which both psychiatrists testify, and Brian must prove his morbid jealousy and its contributory link on a balance of probabilities before it counts in mitigation (Pre-write 0-15).

**Q2021-2-2** · `0.IV.4` `0.IV.2` · PYP 2021 Q2.2 · 10 marks · `pcp-w-0-15` `pcp-w-0-13` `pcp-w-0-44`

You are a first-year associate assisting your partner. Your client is charged with three counts of theft in dwelling (s 380 PC): on three separate occasions, after trying on limited-edition sneakers at different stores, he ran out without paying and was caught nearby wearing them. He wishes to plead guilty to the three charges but to raise two issues in mitigation. First, he was just testing how the sneakers felt while running and always intended to come back and pay. Second, he believes he suffers from kleptomania and could not control himself, although the Prosecution's IMH report says he has no psychiatric condition. Write a short brief to your partner explaining the implications for the plea of guilt if each issue is raised in mitigation separately.

**Answer.**

*To: [Partner]. From: [Associate]. Re: [Client] — three charges under s 228(4) CPC.*

1. **Summary.** The first issue (testing the sneakers and intending to pay) would qualify his plea, and the court must reject it; he should not raise it unless he claims trial. The second (kleptomania) does not qualify the plea, but because IMH disputes it, the court will probably hold a Newton hearing at which he bears the burden on a balance of probabilities.

2. **Issue 1: "testing the sneakers, always intended to pay".** Theft in dwelling requires dishonesty (ss 24, 378, 380 PC). A statement that he always intended to return and pay denies dishonest intention. Where any matter in the plea in mitigation materially affects a legal condition of the offence, the court must reject the plea (s 228(4) CPC); mitigation indicating a lack of mens rea means he has not admitted the offence without qualification (*Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]). If he maintains it, all three charges go to trial. He must choose: accept dishonesty and drop this point, or claim trial. We must not help him plead guilty while denying an element (Pre-write 0-13).

3. **Issue 2: kleptomania.** Saying a condition made it hard for him to control himself, while accepting he knew he was taking the shoes without paying, explains the offence and goes to sentence, not guilt. It is not a qualification, provided it is not framed as "I did not know what I was doing". But it is a contested fact material to sentence: the court may hear evidence to determine it (s 228(5) CPC), in a Newton hearing (*Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). It is extraneous to the Prosecution's case, so he must prove it on a balance of probabilities (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]). We need a report from a private psychiatrist diagnosing kleptomania and linking it to the offences; at present we have only his own belief, and without evidence the Prosecution will object and the assertion must be withdrawn or proved (*PP v Aniza bte Essa* [2009] 3 SLR(R) 327 at [61]) (Pre-write 0-15).

4. **Recommendation.** Take his instructions on Issue 1 before the PG mention; if he insists he intended to pay, he should claim trial. If he pleads guilty, obtain a psychiatric report before relying on Issue 2 and prepare for a Newton hearing. The written mitigation should otherwise follow the usual structure, with nothing that denies an element (Template 0-44).

### 0.IV.5 — Charges taken into consideration (s 148 CPC)

**Q2025-2-2** · `0.IV.5` `0.III.4` `0.VII.3` · PYP 2025 Q2.2 · 4 marks · `pcp-w-0-16` `pcp-w-0-11` `pcp-w-0-36`

*Facts: PYP 2025 Crim Q2, under 0.III.3 above.* The prosecutor offers that if Ms Wing pleads guilty, they will proceed only on Charges 1–4 and apply for the remaining charges to be taken into consideration ("TIC") for sentencing. Explain to Ms Wing the legal implications of this arrangement and how it would affect her position.

**Answer.**

The issue is what it means for Charges 5 and 6 to be taken into consideration. With her consent, the court may take them into account in sentencing her on Charges 1–4; she will not be convicted of them, and while they will probably increase her sentence, the increase is less than separate convictions would bring.

If the accused is found guilty of an offence, the court may, with the consent of the Prosecution and the accused, take into consideration any other outstanding offences that the accused admits to having committed (s 148(1) CPC). The TIC must be recorded (s 148(4)), and once sentence is passed she cannot be charged or tried for a TIC offence unless her conviction on the proceeded charges is set aside (s 148(5)). TIC charges usually enhance the sentence, but whether to consider them is for the court (*PP v Mok Ping Wuen Maurice* [1998] 2 SLR(R) 439 at [19]); the accused can expect a more favourable overall sentence than if she had contested and been convicted of them (*Lim Hsien Hwei v PP* [2014] 3 SLR 15 at [22]). The court applies to the sentence for the proceeded charges an uplift reflecting a suitably discounted measure of what the TIC charges would have attracted (at [25]–[27]).

For Ms Wing: she must admit the third trespass and theft (18 April) and consent; she will have convictions only on Charges 1–4. The two TIC charges may lift her sentence on those four, but by less than two more convictions would. Only the four proceeded charges are sentenced, so only they count for s 307(1) CPC: with four terms of imprisonment, at least two must run consecutively (Pre-write 0-36). She might ask the Prosecution to proceed on fewer charges, for example one trespass and one theft, with the rest TIC, which would avoid s 307(1) altogether (Pre-write 0-11).

Therefore, by accepting the offer Ms Wing avoids convictions on Charges 5 and 6 and should receive a lower overall sentence than if convicted of all six, though higher than for Charges 1–4 alone; she should accept only if she admits the 18 April offences (Pre-write 0-16).

**Q2023-2-3** · `0.IV.5` `0.IV.6` · PYP 2023 Q2.3 · 10 marks · `pcp-w-0-16` `pcp-w-0-17`

*Facts: PYP 2023 Crim Q2, under 0.IV.2 above.* Ms Kew asks what it means when the Prosecution says the remaining charge (theft of the Coke Zero) is to be "taken into consideration", and how that would affect her eventual sentence. Please advise her.

**Answer.**

The issue is what it means for the Coke Zero charge to be taken into consideration and how that will affect her sentence on the sandwich charge. She will be convicted only of the sandwich theft; the Coke Zero theft, if she admits it and consents, may increase her sentence on that charge, but by less than a separate conviction would.

*What TIC means.* If the accused is found guilty of an offence, the court in passing sentence may, with the consent of the Prosecution and the accused, take into consideration any other outstanding offence that the accused admits to having committed (s 148(1) CPC). In practice, after she pleads guilty to the proceeded charge and admits the SOF, the Prosecution applies for the Coke Zero charge to be TIC, and her consent is sought and recorded (s 148(4)). She is not convicted of it, and once sentenced she cannot later be tried for it unless the conviction on the proceeded charge is set aside (s 148(5)). She must actually admit the Coke Zero theft; if she disputes it, she should not consent.

*Effect on sentence.* TIC charges usually enhance the sentence for the proceeded charge, though whether to take them into account is for the court (*PP v Mok Ping Wuen Maurice* [1998] 2 SLR(R) 439 at [19]). The accused can expect a more favourable overall result than if she had contested and been convicted of the TIC charge (*Lim Hsien Hwei v PP* [2014] 3 SLR 15 at [22]). The method is to compare the sentence for the proceeded charge alone with what she would have received had she been convicted of both, and apply to the former an uplift reflecting a suitably discounted measure of the latter (at [25]–[27]). A TIC offence cannot enhance a type of punishment it does not carry (at [26]–[27]).

*Her other past conduct.* Separately, her 2000 theft conviction is a criminal record that the Prosecution will tender (s 228(2)(a) CPC); I must not describe her as a first offender (r 14(8) PCR), though I can stress that it is 23 years old (*Teo Seng Tiong v PP* [2021] 2 SLR 642) (Pre-write 0-17).

*Application.* With two low-value thefts five days apart, the TIC charge may add a little to the sentence for the sandwich charge, for example making the Prosecution's 5 days harder to resist. Against that, she avoids a second conviction, and her mitigation (bereavement, MDD if proved, remorse, low value) still applies to the overall sentence.

Therefore consenting to the TIC means one conviction instead of two and a lower overall sentence than if convicted of both thefts, at the cost of a modest uplift on the sandwich charge (Pre-write 0-16).

**Q2021-2-1** · `0.IV.5` · PYP 2021 Q2.1 · 5 marks · `pcp-w-0-16`

An accused is charged with six counts of theft in dwelling (s 380 PC). If he pleads guilty at the pre-trial stage, the Prosecution will proceed on two charges and apply to have the remaining four taken into consideration for sentencing. On what basis can the court take the four charges into consideration, and what is the effect on his sentence for the two proceeded charges?

**Answer.**

The basis is s 148(1) CPC: having found the accused guilty of the two proceeded charges, the court in passing sentence may, with the consent of the Prosecution and the accused, take into consideration any other outstanding offences that the accused admits to having committed. So the four charges can be TIC only if he admits them and consents; the court then records them (s 148(4)), and after sentence he cannot be tried for them unless his conviction on the proceeded charges is set aside (s 148(5)).

The effect is that he is convicted and sentenced on two charges only. The TIC charges typically enhance the sentence for the proceeded charges, but whether and how much is for the court (*PP v Mok Ping Wuen Maurice* [1998] 2 SLR(R) 439 at [19]). He can expect a more favourable result than if he had contested and been convicted of all six (*Lim Hsien Hwei v PP* [2014] 3 SLR 15 at [22]): the court compares the sentence for the two proceeded charges alone with what all six convictions would have attracted, and applies to the former an uplift reflecting a suitably discounted measure of the latter (at [25]–[27]). A TIC charge cannot enhance a type of punishment it does not carry (at [26]–[27]). Only two charges are sentenced, so s 307(1) CPC (at least two consecutive terms where three or more imprisonment terms are imposed) is not engaged.

Therefore the four charges are TIC under s 148(1) CPC with his admission and consent, and their effect is a discounted uplift on the sentence for the two proceeded charges, not four further convictions (Pre-write 0-16).

### 0.IV.6 — Antecedents and past conduct relevant to sentence

**Own question C6 facts.** Sam ("S") has pleaded guilty to cheating. His record shows a 2012 conviction for theft; in 2019 he compounded a charge of voluntarily causing hurt by paying the victim $2,000; in 2022 he received a stern warning for a public-nuisance matter. S asks you to tell the judge in mitigation that he "has never been in trouble with the law".

**Q0-C6-1** · `0.IV.6` `0.IV.7` · own question · 7 marks · `pcp-w-0-17` `pcp-w-0-18`

Advise S on what the court may consider and what you may say.

**Answer.**

The issue is which parts of S's past the court may take into account, and what I may say in mitigation. The court will consider his 2012 conviction and, presumptively, the 2019 compounded offence, but not the 2022 warning; I may not tell the court he has never been in trouble.

The Prosecution's address on sentence may include the accused's criminal records and any relevant factors affecting sentence (s 228(2)(a), (c) CPC); a "criminal record" includes the record of any conviction (s 2 CPC). In *Teo Seng Tiong v PP* [2021] 2 SLR 642 at [79]–[108] the Court of Appeal held that criminal records and TIC charges count; compounded offences are presumptive proof of an admission of guilt and may be a relevant factor, though the offender may show he compounded for other reasons (at [101]–[102]); warnings do not count (at [88]). The prosecutor must inform the court of known antecedents (r 15(4) PCR). Defence counsel need not disclose antecedents, but must not adduce evidence or make submissions inconsistent with them (r 14(8) PCR).

*Application.* The 2012 theft is a criminal record and will be tendered. The 2019 composition presumptively counts; if S paid only to end the matter quickly while denying the assault, he may say so and the court may decide what weight to give it, if necessary after hearing evidence. The 2022 stern warning is irrelevant to sentence. I cannot say S "has never been in trouble with the law": that contradicts his record and would mislead the court (r 14(8); r 9(2)(a) PCR). I may argue that the conviction is 14 years old and of a different kind, so it deserves little weight, and press the genuine mitigating factors such as his early plea and remorse (r 14(2)). A clean record would have been only a neutral factor anyway (*Chew Soo Chun v PP* [2016] 2 SLR 78 at [30]) (Pre-write 0-18).

Therefore I would explain to S that the court will see the 2012 conviction and probably the composition, that I will not refer to the warning, and that I cannot make the statement he asks for; his mitigation will rest on the age and nature of the record and his remorse (Pre-write 0-17).

### 0.IV.7 — Address on sentence and plea in mitigation

**Q2025-2-3** · `0.IV.7` `0.IV.4` `0.VII.1` · PYP 2025 Q2.3 · 6 marks · `pcp-w-0-18` `pcp-w-0-15` `pcp-w-0-34`

*Facts: PYP 2025 Crim Q2, under 0.III.3 above.* Ms Wing decides to plead guilty. She confides: "I have been suffering from depression ever since my pet bird, Polly Wolly, died two years ago. I'm not saying I didn't know what I was doing, but I really think the loss of Polly Wolly affected my judgment. Is there any way this will help me get a lower sentence?" Advise Ms Wing on how this information might be presented, including the procedural consequences if the Prosecution disputes her claims.

**Answer.**

The issue is how Ms Wing's depression can be used in mitigation and what happens if the Prosecution disputes it. It can be put forward in her plea in mitigation, supported by a psychiatric report, as a factor that affected her judgment; it does not qualify her plea because she accepts she knew what she was doing. If the Prosecution disputes it, the court may hold a Newton hearing at which she must prove it on a balance of probabilities.

*Presenting it.* On conviction the Prosecution may address the court on sentence, the court must then hear the plea in mitigation, and the Prosecution may reply (s 228(1)–(3) CPC). Counsel must raise every favourable factor (r 14(2) PCR) but make no scandalous allegation (r 14(7)). Ms Wing needs a report from a psychiatrist diagnosing the depression, dating its onset (her parrot's death two years ago), and explaining its contributory link to the thefts; a bare assertion that is objected to must be withdrawn, proved or established by evidence (*PP v Aniza bte Essa* [2009] 3 SLR(R) 327 at [61]). The plea in mitigation would also rely on her age, lack of antecedents (neutral rather than mitigating: *Chew Soo Chun v PP* [2016] 2 SLR 78 at [30]), early plea and remorse, and restitution (Pre-write 0-18; Template 0-44).

*Not a qualification.* She must not say she did not know what she was doing or did not intend to take the birds; that would deny dishonesty and the court would have to reject her plea (s 228(4) CPC; *Md Rafiqul Islam Abdul Aziz v PP* [2017] 3 SLR 619 at [27]). Her actual words ("I'm not saying I didn't know what I was doing") are safe.

*Why it helps.* Where a mental condition contributed to the offence, deterrence may carry less weight and rehabilitation may take precedence (*Lim Ghim Peow v PP* [2014] 4 SLR 1287) (Pre-write 0-34). That supports a shorter term or, if it is not excluded, a community-based sentence such as a mandatory treatment order. Section 337(1) CPC bars community sentences for, among others, offences punishable with more than 3 years' imprisonment, though an MTO remains possible in some of those cases (s 337(2)); an MTO also needs an appointed psychiatrist's report that the condition is treatable, contributed to the offence, and that she is suitable (s 339(3)) (Pre-write 0-35).

*If the Prosecution disputes it.* The court may hear evidence to determine the truth of matters that may materially affect sentence (s 228(5) CPC) at a Newton hearing (*Ng Chun Hian v PP* [2014] 2 SLR 783 at [24]). As the fact is extraneous to the Prosecution's case, Ms Wing bears the burden on a balance of probabilities (*PP v Chan Yoke Ling Catherine* [2004] SGDC 108 at [47]–[52]); her psychiatrist and any Prosecution psychiatrist give evidence (Pre-write 0-15).

Therefore Ms Wing should obtain a psychiatric report and rely on her depression in her written mitigation as a contributory factor, without suggesting she did not know what she was doing; if the Prosecution disputes it, she must be ready to prove it at a Newton hearing.

*See also:* Q2023-1-3 (under 0.VII.2, avoiding caning); Q0-C6-1 (under 0.IV.6); Q2023-2-1 (under 0.IV.2).

### 0.IV.8 — Fitness to plead

See Q0-C4-1 under 0.IV.1 (a client with untreated schizophrenia who wants to plead guilty; ss 247–248 CPC).

### 0.V Trial I: disclosure

Sub-points 0.V.1–0.V.6. Tested: 0.V.1 (2025), 0.V.2 (2023, 2025), 0.V.3 (2021, 2022), 0.V.4 (2021, 2022, 2025), 0.V.5 (2021, 2022). Own question C7 covers 0.V.6.

### 0.V.1 — When the CCDC applies; opting in

**Q2025-1-2** · `0.V.1` `0.V.2` `0.V.3` `0.I.3` · PYP 2025 Q1.2 · 6 marks · `pcp-w-0-19` `pcp-w-0-20` `pcp-w-0-21` `pcp-w-0-3`

*Facts: PYP 2025 Crim Q1, under 0.I.4 above.* At the hearing on 2 June 2025 you tell the Court that Mr Albert claims trial. The Court fixes the matter for trial in the Magistrate's Court and, as the CCDC regime does not automatically apply there, asks whether the parties wish to opt in. Bearing in mind that Mr Albert cannot recall the contents of his long statement, advise him whether he should opt in to the CCDC, and why. Cite the relevant CPC provisions.

**Answer.**

The issue is whether Mr Albert should consent to the CCDC applying to his Magistrate's Court trial. He should: opting in obliges the Prosecution to disclose his long statement and its case before trial, which he badly needs; the cost, a Case for the Defence that can be used against him, is manageable because his defence (denial) is simple and firm.

*When the CCDC applies.* The CCDC applies to offences in the Second Schedule to the CPC that are to be tried in a District Court (s 159 CPC) and to every case tried in the High Court (s 212). A case outside s 159 may be dealt with under the CCDC if both the Prosecution and the Defence consent (s 159(3)). Mr Albert's case is in the Magistrate's Court, so it applies only if both consent. (The defence can no longer opt out of a case within s 159: the old s 159(2) was deleted with effect from 14 Feb 2025.)

*What he gains.* The Case for the Prosecution ("CFP") must contain the charge, a summary of the facts, lists of the Prosecution's witnesses and exhibits, and any written statement of the accused that the Prosecution intends to adduce (s 162(1)(a)–(e)); it is due within 2 weeks of the first CCDC (s 161(2)). Every other written statement of the accused relating to the charge must be served in the Prosecution's Supplementary Bundle ("PSB") within 2 weeks of service of the Case for the Defence (s 166(1)(a)). Either way Mr Albert will see his long statement before trial, which he cannot otherwise get as of right; the *Goldring* right of access covers only documents he owned or controlled before seizure, not a police-recorded statement (Pre-write 0-3). Knowing what he said, recorded when he was exhausted and in the early hours, is essential to deciding whether to challenge its admissibility or accuracy (Pre-write 0-32).

*What it costs.* He must serve a Case for the Defence ("CFD") within 2 weeks of the second CCDC (s 163(1)), stating a summary of his defence and the facts in support, his witnesses and exhibits, and any objection to the CFP with its factual and legal basis (s 165(1)). The court may draw inferences if his case at trial differs from the CFD (s 169(1)(c)), and the CFD may be used to cross-examine him and impeach his credit (s 258A) (Pre-write 0-21). His defence is a simple denial, so the risk is low, provided he approves the CFD in writing and raises any objection to the statement in it.

Therefore I would advise Mr Albert to opt in under s 159(3) CPC, so that he receives his long statement in the CFP or PSB well before trial, and to give me full instructions for a CFD that he must approve before it is filed (Pre-write 0-19).

*See also:* Q2023-1-2 (under 0.I.3, opting in to get the client's statement).

### 0.V.2 — CCDC documents and timelines

See Q2025-1-2 under 0.V.1 (CFP, PSB, CFD and their timelines) and Q2023-1-2 under 0.I.3.

### 0.V.3 — Non-compliance and inconsistency: inferences; leaving allegations out of the CFD

**PYP 2021 Crim Q1 facts.** Bill, 25, a Singaporean with no record, committed four robberies of lone petrol-kiosk attendants between 3am and 4am, wearing a balaclava and carrying a toy dagger. During a fifth robbery at a Shell kiosk in Mandai, a customer, Jerry, grabbed his shirt and pulled off the balaclava; Bill elbowed Jerry in the face several times, causing multiple facial fractures, and fled, leaving the balaclava and dagger. DNA on the balaclava and fingerprints on the dagger matched Bill. He is charged with five counts of robbery by night (s 392 PC) and one of voluntarily causing grievous hurt to Jerry (s 325 PC). He claims trial; in his initial s 22 CPC statement he denied the offences and said he was at home.

**Q2021-1-2** · `0.V.3` `0.VI.8` · PYP 2021 Q1.2 · 20 marks · `pcp-w-0-21` `pcp-w-0-32`

The CFP includes a detailed further s 22 statement in which Bill confesses that he premeditated the robberies, scouting for kiosks manned by lone elderly attendants, and admits striking Jerry because he panicked. Bill says the statement was improperly obtained: (a) Inspector Tom did not tell him he had the right to remain silent; (b) after his initial denial, two officers acting on Inspector Tom's directions handcuffed him to a bench in an air-conditioned holding area for over 8 hours, wearing only a T-shirt and shorts, with no proper break or refreshments before the further statement was recorded; (c) while recording it, Inspector Tom said: "I don't care about your future. If you are uncooperative, I am going to lock you up for however long it takes for you to properly reflect about whether you want to do the right thing." What procedures and principles govern whether the Prosecution can admit the confession? In particular, can Bill omit these allegations from his CFD so as to "take the Prosecution by surprise" at trial?

**Answer.**

The issue is whether the Prosecution can admit Bill's further statement, and whether he may hold back his allegations until trial. The statement is admissible unless made under threat, inducement, promise or oppression; because Bill alleges a threat and oppression the court must hold an ancillary hearing, at which the Prosecution must prove voluntariness beyond reasonable doubt. Bill should not omit the allegations from his CFD: the omission would invite adverse inferences and cross-examination, and gains him nothing.

*Admissibility and procedure.* The facts and allegations are the same as in PYP 2022 Q1.2 (Alex), whose official answer is worked through in Q2022-1-2 under 0.VI.8; the analysis applies to Bill. In short: (a) the failure to tell him of his right to silence does not by itself make the statement inadmissible (Explanation 2(d) to s 258 CPC; *PP v Mazlan bin Maidun* [1992] 3 SLR(R) 968), though it may be weighed with the other circumstances; (b) 8 hours handcuffed, cold and without refreshment goes to oppression (Explanation 1 to s 258), judged by whether the investigation by its nature, duration or circumstances affected his mind and will so that he spoke when he would otherwise have stayed silent (*Tey Tsun Hang v PP* [2014] 2 SLR 1189 at [113]); the threshold is high (*PP v Tan Boon Tat* [1990] 1 SLR(R) 287; *Fung Yuk Shing v PP* [1993] 2 SLR(R) 771); (c) Inspector Tom's words are a threat having reference to the charge, proceeding from a person in authority (s 258(3)); the test is partly objective (was there a threat?) and partly subjective (did it operate on Bill's mind?) (*Chia Chien Wei Kelvin v PP* [1998] 3 SLR(R) 619 at [53]). The court must convene an ancillary hearing (s 279 CPC), and the Prosecution must prove beyond reasonable doubt that the statement was voluntary (*Teo Yeow Chuah v PP* [2004] 2 SLR(R) 563 at [20]).

*Omitting the allegations from the CFD.* The CFD must state, where the Defence objects to any issue of fact or law in the CFP, the nature of the objection, the issue of fact on which evidence will be produced and the points of law relied on (s 165(1)(d) CPC); an objection to the voluntariness of a statement is exactly such an objection, so the allegations must be set out with their factual basis. If Bill's case at trial differs from or was omitted from his CFD, the court may draw such inference as it thinks fit (s 169(1)(c)); and the CFD is admissible and may be used to cross-examine him and impeach his credit (s 258A(1)). Allegations raised for the first time at the ancillary hearing would be attacked as an afterthought, weakening the very challenge he wants to make. The "surprise" gains nothing: once he raises voluntariness, the Prosecution must prove it beyond reasonable doubt anyway, and it will call Inspector Tom and the two officers whatever the CFD says.

Therefore the confession goes in only if the Prosecution proves at an ancillary hearing that it was voluntary; Bill should set out the three allegations fully in his CFD, because leaving them out invites an adverse inference under s 169(1) CPC and cross-examination under s 258A (Pre-writes 0-21, 0-32).

### 0.V.4 — Kadar disclosure of unused material

**Q2025-1-3** · `0.V.4` `0.III.1` `0.V.6` · PYP 2025 Q1.3 · 7 marks · `pcp-w-0-22` `pcp-w-0-8` `pcp-w-0-24`

*Facts: PYP 2025 Crim Q1, under 0.I.4 above.* Before trial you meet the Prosecutor for a CCMS discussion. He mentions that the Prosecution has CCTV footage of the incident but does not intend to use it at trial, and refuses your request for a copy. Mr Albert insists he must have it as it will surely exonerate him. Advise him how you can obtain a copy and the law you will rely on.

**Answer.**

The issue is whether the Prosecution must disclose CCTV footage that it holds but will not use. If the footage tends to undermine the Prosecution's case or strengthen Mr Albert's, it must be disclosed under *Kadar*, now codified in ss 221A and 221D CPC; I would request it in writing and, if refused, raise it with the court.

*The law.* The Prosecution must disclose unused material that tends to undermine its case or strengthen the defence, where the material is likely to be admissible and might reasonably be regarded as prima facie credible and relevant to guilt or innocence (*Muhammad bin Kadar v PP* [2011] 3 SLR 1205 at [113]), or, exceptionally, is likely inadmissible but would give a real chance of a line of inquiry leading to such material (at [117]). Material that is neutral or adverse to the accused need not be disclosed (at [113]). The duty covers material within the Prosecution's knowledge (*Kadar II* [2011] 4 SLR 791 at [14]). Where the CCDC applies, disclosure should be made with the CFP, within 2 weeks of the start of the CCDC; otherwise at the latest before trial; the duty continues until the case is disposed of, including on appeal (*Kadar I* at [113]). The obligations were codified in ss 221A and 221D CPC in 2025.

*Application.* CCTV of the incident is real evidence, likely admissible, and prima facie credible. If it shows Mr Albert's hands away from Ms Bebe, or someone else touching her, it strengthens his defence and must be disclosed. The Prosecution's decision not to use it, after watching it, suggests it does not clearly support the charge. If it is genuinely neutral or adverse, *Kadar* does not require disclosure; but the Prosecution is not the final judge, and in case of doubt the court can rule. Mr Albert's belief that it "will surely exonerate him" cannot be promised.

*Procedure.* The CCMS discussion itself is a without prejudice forum (*PP v Knight Glenn Jeyasingam* [1999] 1 SLR(R) 1165 at [72]), so I would follow it with an open letter requesting the footage under *Kadar* and ss 221A and 221D CPC, explaining how it bears on identification and the alleged touching. If the case has been opted into the CCDC (Q2025-1-2), it should come with the CFP. If the Prosecution still refuses, I would raise it with the court before trial. Non-disclosure that is later found to have been a breach may lead to an adjournment, an adverse inference, a retrial or, if the conviction is unsafe, an acquittal (*Lim Hong Liang v PP* [2021] 5 SLR 626) (Pre-write 0-24).

Therefore I would write to the Prosecution demanding the footage under *Kadar* and ss 221A and 221D CPC and, if it maintains its refusal, ask the court to direct disclosure before trial (Pre-write 0-22).

**Q2021-1-1** · `0.V.4` `0.V.5` · PYP 2021 Q1.1 · 10 marks · `pcp-w-0-22` `pcp-w-0-23`

*Facts: PYP 2021 Crim Q1, under 0.V.3 above.* The police recorded statements from (a) Kathy, the sole attendant at an Esso kiosk on Bukit Panjang Road during Bill's first robbery, who was petrified and could not identify the robber because of his "very scary" mask, but recalled that he did not sound local and seemed to speak with a heavy foreign accent; and (b) Max, Bill's father, who works irregular hours, usually sleeps soundly, and so could not confirm whether Bill was at home on the nights in question. Assuming the Prosecution will call neither, discuss whether it has any disclosure obligations in relation to these statements.

**Answer.**

The issue is whether the Prosecution must disclose the statements of Kathy and Max, neither of whom it will call. It must disclose both: Kathy's under *Kadar*, because it tends to undermine the identification of Bill; Max's under *Nabill*, because he is a material witness on Bill's alibi, even though his statement does not help Bill. The same analysis appears in the official answer to the near-identical PYP 2022 Q1.1 (Q2022-1-1 under 0.V.5).

*Kathy — Kadar.* The Prosecution must disclose unused material that tends to undermine its case or strengthen the defence, if likely admissible and prima facie credible and relevant to guilt (*Muhammad bin Kadar v PP* [2011] 3 SLR 1205 at [113]), or, exceptionally, if likely inadmissible but giving a real chance of a line of inquiry leading to such material (at [117]); neutral or adverse material need not be disclosed. Kathy's account that the robber spoke with a heavy foreign accent cuts against the case that the robber was Bill, a 25-year-old Singaporean. It tends to undermine the Prosecution's identification on the first robbery charge and strengthens Bill's alibi, so it must be disclosed (ss 221A, 221D CPC).

*Max — Nabill.* The Prosecution must disclose the statement of a material witness whom it does not call, that is, one who can be expected to confirm or contradict the accused's defence in material respects (*Muhammad Nabill bin Mohd Fuad v PP* [2020] 1 SLR 984 at [4]), whether the statement is favourable, neutral or adverse, and without any prior assessment of credibility (at [41]). The duty is triggered when the accused raises a defence and the Prosecution has such a statement (*Roshdi bin Abdullah Altway v PP* [2022] 1 SLR 535 at [155]); codified in ss 221A(2), 221B CPC. Bill's defence is alibi (at home); Max is the person who could confirm or contradict it. His statement (that he slept and cannot confirm) is neutral, but *Nabill* still requires disclosure so that Bill can make an informed decision whether to call him (at [44]–[45]).

*Timing.* Both statements should be disclosed with the CFP if the case proceeds under the CCDC (Bill is later tried by a District Judge, Q1.5), and otherwise before trial and before Bill testifies; the duty continues through any appeal (*Kadar I* at [113]; *Nabill* at [50]–[53]).

Therefore the Prosecution must disclose Kathy's statement under *Kadar* and Max's under *Nabill*, with the CFP (Pre-writes 0-22, 0-23).

### 0.V.5 — Material witnesses' statements (Nabill; Roshdi)

**PYP 2022 Crim Q1 facts (= SQ22).** One night at 10pm, Alex followed a lone woman from a bus stop, ran up to her at the void deck of a block of flats, groped her buttocks and ran away. A passer-by called the police. CCTV from nearby lift lobbies identified Alex, who was arrested at home in a nearby block; the police noted he had short hair and no tattoos on either calf. In his initial s 22 CPC statement he denied the offence and said he had been at home since returning from work at 6pm. He is charged under s 354(1) PC and claims trial.

**Q2022-1-1** · `0.V.5` `0.V.4` · PYP 2022 Q1.1 (= SQ22 1(a)); official suggested answer SQ22 · 10 marks · `pcp-w-0-23` `pcp-w-0-22`

The police recorded statements from (a) Kelly, who was at the void deck when she heard the victim scream behind her, saw her in distress, glimpsed a person running away, chased him, and from a distance saw that he had a ponytail and tattoos down one of his calves before losing sight of him; and (b) Michael, Alex's father, who works irregular hours, usually sleeps soundly, had been asleep since about 4pm, and so could not confirm whether Alex was home all night. Assuming the Prosecution will call neither, discuss whether it has any disclosure obligations in relation to their statements.

**Answer.**

The issue is whether the Prosecution must disclose the statements of Kelly and Michael. It must disclose Kelly's statement under the *Kadar* obligations and Michael's under the *Nabill* obligations.

*Kelly — Kadar.* The Prosecution must disclose unused material that tends to undermine its case or strengthen the defence, where it (a) is likely to be admissible and might reasonably be regarded as credible and relevant to guilt or innocence; or (b) is likely to be inadmissible but would provide a real (not fanciful) chance of pursuing a line of inquiry leading to material that is likely admissible and might reasonably be regarded as credible and relevant (*Muhammad bin Kadar v PP* [2011] 3 SLR 1205 at [113]–[121]). The obligation does not extend to material that is neutral or adverse to the accused. Kelly described the fleeing man as having a ponytail and calf tattoos; Alex has short hair and no tattoos. Her statement on its face undermines the Prosecution's identification, and at the least gives the defence a basis to show she cannot identify Alex and to call her. It must be disclosed (now ss 221A, 221D CPC) (Pre-write 0-22).

*Michael — Nabill.* The Prosecution must disclose the statement of a material witness whom it does not call. A material witness is one who can be expected to confirm or contradict the accused's defence in material respects; it does not matter whether the statement is favourable, neutral or adverse, because the object is to let the accused make an informed choice whether to call the witness (*Muhammad Nabill bin Mohd Fuad v PP* [2020] 1 SLR 984 at [39]–[50]). Alex's defence is an alibi (home since 6pm). Michael lives with him and is the obvious person to confirm or contradict it; his statement is neutral (he was asleep), but he is a material witness, so his statement must be disclosed and Alex can then decide whether to call him (ss 221A(2), 221B CPC). The Prosecution was not obliged to record statements from every material witness (*Roshdi bin Abdullah Altway v PP* [2022] 1 SLR 535 at [67], [166]), but having recorded this one it must disclose it.

*Timing.* Both statements should be disclosed when the CFP is served; the duty is continuing, extends to appeals, and ends only when the matter is completely disposed of (SQ22 suggested answer; *Kadar I* at [113]; *Nabill* at [50]–[53]).

Therefore the Prosecution must disclose Kelly's statement under *Kadar* and Michael's under *Nabill*, with the CFP (Pre-write 0-23).

### 0.V.6 — Consequences of a disclosure breach

**Own question C7 facts.** After a trial, Hana ("H") was convicted of voluntarily causing hurt to a shop assistant, Mei. The only eyewitness was Mei. Two weeks after conviction (and one week after sentence), H learns that the police held CCTV footage from the shop that shows Mei pushing H first. The Prosecution never disclosed it. Mei has since left Singapore permanently.

**Q0-C7-1** · `0.V.6` `0.V.4` `0.VIII.6` · own question · 10 marks · `pcp-w-0-24` `pcp-w-0-22` `pcp-w-0-43`

Advise H on the effect of the non-disclosure and how she can use the footage.

**Answer.**

The issue is whether the Prosecution's failure to disclose the footage entitles H to have her conviction overturned, and how she can put the footage before the appellate court. The non-disclosure breached the Prosecution's *Kadar* obligation; because the footage strongly supports self-defence and the prejudice cannot now be cured, H has a good argument that her conviction is unsafe.

*Breach.* The Prosecution must disclose unused material that tends to undermine its case or strengthen the defence, where it is likely to be admissible and might reasonably be regarded as prima facie credible and relevant to guilt or innocence (*Muhammad bin Kadar v PP* [2011] 3 SLR 1205 at [113]), now codified in ss 221A and 221D CPC. CCTV showing Mei pushing H first goes to self-defence, is likely admissible as real evidence, and was within the Prosecution's knowledge. It should have been disclosed before trial, and the duty continues through any appeal.

*Consequences.* A *Kadar* breach is not a "poison pill"; a conviction is overturned only if the non-disclosure caused a material irregularity occasioning a failure of justice (*Lim Hong Liang v PP* [2021] 5 SLR 626 at [21]). The court weighs the effect of the breach on the evidence, the prejudice to the accused, whether it can be remedied, its causes (including the Prosecution's conduct) and the wider interests of justice, including fairness to victims (at [22]). The conviction is unsafe where the evidence is clearly admissible and strongly points to acquittal (at [28], [30]); otherwise a retrial may be ordered (s 390(1)(b)(i) CPC). Here Mei was the only eyewitness and the footage contradicts her account on the central issue; H lost the chance to cross-examine her on it, and Mei has left Singapore, so a retrial cannot cure that loss (*Lim Hong Liang* at [32]). These factors point to an acquittal rather than a retrial (Pre-write 0-24).

*Getting the footage before the court.* H must file a Notice of Appeal within 14 days of sentence (s 377(2) CPC), which leaves her one week (Pre-write 0-39). With the appeal she should apply by criminal motion to adduce the footage as additional evidence (s 392(1) CPC). It must meet the cumulative *Ladd v Marshall* conditions: it could not have been obtained with reasonable diligence for the trial (the police held it and did not disclose it), it is relevant (self-defence), and it is reliable (timestamped CCTV) (Pre-write 0-43).

Therefore H should file a Notice of Appeal against conviction within the 14 days, apply under s 392 CPC to admit the footage, and argue that the *Kadar* breach makes her conviction unsafe, seeking an acquittal or, failing that, a retrial.

### 0.VI Trial II: the trial process

Sub-points 0.VI.1–0.VI.9. Tested: 0.VI.3 (2021), 0.VI.5 (2021), 0.VI.7 (2025), 0.VI.8 (2021, 2022, 2025). Own questions C8 (0.VI.1, 0.VI.2), C9 (0.VI.4, 0.VI.6) and C10 (0.VI.9).

### 0.VI.1 — Order of trial and the Prosecution's case; Browne v Dunn

**Own question C8 facts.** Ken ("K") is on trial for outraging the modesty of a passenger, Pei, at a bus interchange. His defence is that he brushed past her accidentally in a crowd. The Prosecution's case is Pei's evidence and that of the investigating officer. A cashier at a nearby kiosk, Ah Seng, who gave a police statement saying he saw the incident, is not on the Prosecution's witness list.

**Q0-C8-1** · `0.VI.1` `0.VI.2` `0.V.5` · own question · 9 marks · `pcp-w-0-25` `pcp-w-0-26` `pcp-w-0-23`

Advise K on how you will conduct the defence during the Prosecution's case, and on what can be made of the Prosecution's failure to call Ah Seng.

**Answer.**

The issue is what defence counsel must do during the Prosecution's case and whether the court may draw an inference from the Prosecution's decision not to call Ah Seng. I must cross-examine Pei and put K's case to her; the Prosecution must disclose Ah Seng's statement; and the court may presume his evidence would have been unfavourable to the Prosecution if he was available and central.

*Conduct during the Prosecution's case.* After the charge is read and K claims trial, the Prosecution may open and then calls its witnesses, each examined in chief, cross-examined and re-examined (s 230(1)(a)–(e) CPC); re-examination is confined to matters arising in cross-examination (s 140(3) EA). A party who intends to contradict a witness must put the substance of the contradiction to that witness in cross-examination (*Browne v Dunn* (1893) 6 R 67). I must therefore put to Pei that the contact was an accidental brush in the crowd, and test what she could see and feel. If I do not, K's account will be attacked as an afterthought when he testifies (CL5 s9, s18) (Pre-write 0-25).

*Ah Seng's statement.* Ah Seng can be expected to confirm or contradict K's defence in material respects, so he is a material witness. The Prosecution must disclose his statement whether it is favourable, neutral or adverse (*Muhammad Nabill bin Mohd Fuad v PP* [2020] 1 SLR 984 at [4], [41]; ss 221A(2), 221B CPC), at the latest before trial and before K testifies. After closing its case the Prosecution may also offer its remaining witnesses to the defence. I would demand the statement now and decide, once I have read it, whether to call him (Pre-write 0-23).

*Adverse inference.* The court may presume that evidence which could be and is not produced would, if produced, be unfavourable to the person who withholds it (s 116 illus (g) EA). No inference arises where the witness is not material or the case is proved by other independent evidence (*Satli bin Masot v PP*), but it is likely where the witness was readily available and central to the party's case (*Beh Chew Boo v PP*) (both from Cyril's notes, which give no citations). Ah Seng is the only independent eyewitness, so I would submit that the inference should be drawn; the Prosecution will reply that Pei's evidence suffices (Pre-write 0-26).

Therefore I would cross-examine Pei fully and put K's account to her, obtain Ah Seng's statement under *Nabill*, and, if the Prosecution does not call him, invite the court to draw an adverse inference under s 116 illus (g) EA.

### 0.VI.2 — Adverse inferences at trial

See Q0-C8-1 under 0.VI.1 (a witness the Prosecution does not call, s 116 illus (g) EA) and Q0-C1-1 under 0.I.2 (failure to mention an alibi when charged, s 261 CPC). The CCDC inferences (s 169 CPC) are in Q2021-1-2 under 0.V.3, and the accused's silence when called on (s 291(3)) in Q2021-1-3 under 0.VI.3.

### 0.VI.3 — Submission of no case to answer

**Q2021-1-3** · `0.VI.3` `0.VI.5` `0.VIII.1` `0.VI.2` · PYP 2021 Q1.3 · 10 marks · `pcp-w-0-27` `pcp-w-0-29` `pcp-w-0-38` `pcp-w-0-26`

*Facts: PYP 2021 Crim Q1, under 0.V.3 above.* After the ancillary hearing the court admits Bill's detailed confession, and the Prosecution closes its case. Bill wants his counsel to urge the court to "dismiss the charges" now. Is he likely to succeed, and what courses are open to him if he is not? Can he appeal now against the decision to admit his confession?

**Answer.**

The issue is whether Bill can obtain a dismissal at the close of the Prosecution's case, what he may do if the court calls on him, and whether the admissibility ruling can be appealed now. A submission of no case to answer is very unlikely to succeed; if called on, he may plead guilty or give his defence, testifying or staying silent; and he cannot appeal the ruling until after the trial.

*No case to answer.* At the close of the Prosecution's case the defence may submit that there is no case to answer (s 230(1)(f) CPC). The question is whether there is some evidence, not inherently incredible, which if accepted as accurate would establish each essential element of the offence (*Haw Tua Taw v PP* [1981–1982] SLR(R) 133 at [17]); evidence of primary fact is accepted unless inherently incredible (*Wong Wee Keong*, per Cyril-Exam §5.2). If there is no such evidence the court must order a discharge amounting to an acquittal (s 230(1)(k)); if there is, it must call on the accused to give his defence (s 230(1)(j)). A submission should not be made for its own sake (*Ong Lee Koon v PP* [1995] 1 SLR(R) 682 at [19]). Here the Prosecution has DNA on the balaclava, fingerprints on the toy dagger, Jerry's evidence and an admitted confession covering premeditation of the robberies and the blows to Jerry. Every element of each charge is supported by evidence that is not inherently incredible, so the threshold is met and the submission will fail (Pre-write 0-27).

*If called on.* Bill may plead guilty or give his defence (s 230(1)(n)). If he gives evidence he does so first, on oath, and is cross-examined (ss 230(1)(o), 291(1)); I must advise him whether to testify or remain silent, and the decision is his (r 14(5)(a)(ii) PCR) (Pre-write 0-29). If he refuses to testify once called on, the court may draw such inferences as appear proper (s 291(3)); he may also face an inference for relying on facts he failed to mention when charged (s 261) (Pre-write 0-26). Given the confession and forensic evidence, staying silent leaves the case unanswered; testifying exposes him to cross-examination on his inconsistent statements. A plea of guilty at this stage would still attract some credit for remorse.

*Appeal against the ruling.* An appeal lies only against a judgment, sentence or order as the CPC provides (s 374(1) CPC); an "order" means one that finally disposes of the parties' rights (*Ang Cheng Hai v PP* [1995] 3 SLR(R) 151), and there is no standalone appeal against an interlocutory ruling such as the admission of evidence after an ancillary hearing (*Knight Glenn Jeyasingam v PP* [1998] 3 SLR(R) 196). Bill must wait; if convicted, he can challenge the admission of the confession in an appeal against conviction (Pre-write 0-38).

Therefore Bill's submission of no case to answer is unlikely to succeed; he should prepare either to give evidence (with my advice on the risks) or to consider pleading guilty, and he cannot appeal the admissibility ruling until after verdict.

### 0.VI.4 — Altering or framing a new charge at trial

**Own question C9 facts.** Lina ("L") is on trial for voluntarily causing hurt by dangerous weapons (s 324 PC). At the close of the Prosecution's case the evidence that the object she swung was a knife is weak, and the judge says she is minded to alter the charge to voluntarily causing hurt (s 323 PC) before calling on L to give her defence. L's counsel wants to cross-examine the complainant again on the altered charge. Later, after the defence closes, the Prosecution wishes to call a new witness to rebut L's evidence.

**Q0-C9-1** · `0.VI.4` `0.VI.6` · own question · 8 marks · `pcp-w-0-28` `pcp-w-0-30`

Advise L on the alteration of the charge, the recall of the complainant and the Prosecution's rebuttal witness.

**Answer.**

The issue is whether the court may alter the charge at this stage, and what rights L has to recall witnesses and to meet rebuttal evidence. The court may alter the charge before calling on the defence; L is entitled to plead to it, to ask for time and to recall the complainant; and she may cross-examine any rebuttal witness.

*Alteration.* Before calling on the accused to give her defence, the court may alter the charge or frame a new charge, following ss 128–131 CPC (s 230(1)(g)). The altered charge must be explained to L and her plea taken (ss 128(2), 129(1)). If she says she is not ready, the court must consider her reasons, proceed only if that is unlikely to prejudice the defence or the Prosecution, and otherwise direct a new trial or adjourn (s 129(2)–(4)). Cyril's notes add that the power is used where the evidence obviously points to another offence (*Tan Khee Wan Iris*). Here the evidence supports hurt but not a dangerous weapon, so alteration to s 323 is appropriate, and it is in L's favour (Pre-write 0-28).

*Recall.* Where the charge is altered, the parties must on application be allowed to recall or re-summon and examine witnesses with reference to the altered charge only, unless the application is frivolous or vexatious or made to delay or frustrate justice (s 131). L's counsel should apply to recall the complainant and confine the questions to matters arising from the s 323 charge. Separately, the court may summon or recall any witness at any stage, and must do so if the evidence appears essential to a just decision (s 283(1)–(2)).

*Rebuttal.* At the close of the defence case the Prosecution may call or recall any person in rebuttal, and that person may be cross-examined by the defence (s 230(1)(t)). L's protection is the right to cross-examine the rebuttal witness (Pre-write 0-30).

Therefore L should plead to the altered s 323 charge and say whether she is ready, apply under s 131 CPC to recall the complainant, and cross-examine the Prosecution's rebuttal witness.

### 0.VI.5 — Case for the Defence: whether the accused should testify

See Q2021-1-3 under 0.VI.3 (options when called on; advising whether to testify, r 14(5)(a)(ii) PCR).

### 0.VI.6 — Recalling witnesses and rebuttal witnesses

See Q0-C9-1 under 0.VI.4 (recall on an altered charge, s 131; s 283; rebuttal, s 230(1)(t)).

### 0.VI.7 — Impeaching a witness by prior inconsistent statement

See Q2025-1-4 under 0.VI.8 (the accused confronted with his long statement; ss 147, 157(c) EA).

### 0.VI.8 — Challenging the accused's statement: TIPO and the ancillary hearing

**Q2022-1-2** · `0.VI.8` `0.V.3` · PYP 2022 Q1.2 (= SQ22 1(b)); official suggested answer SQ22 · 20 marks · `pcp-w-0-32` `pcp-w-0-21`

*Facts: PYP 2022 Crim Q1, under 0.V.5 above.* The CFP includes a detailed further s 22 CPC statement in which Alex confesses that he groped the victim because he found her attractive, and admits that his claim to have been home since 6pm was a lie. Alex says it was improperly obtained: (a) Inspector Tom did not tell him he had the right to remain silent; (b) after his initial denial, two officers acting on Inspector Tom's directions handcuffed him to a bench in an air-conditioned holding area for over 8 hours, wearing only a T-shirt and shorts, with no proper break or refreshments before the further statement was recorded; (c) while recording it, Inspector Tom said: "I don't care about your future. If you are uncooperative, I am going to lock you up for however long it takes for you to properly reflect about whether you want to do the right thing." What procedures and principles govern whether the Prosecution can admit the confession? Can Alex omit these allegations from his CFD so that he can "take the Prosecution by surprise" at trial?

**Answer.**

The issue is whether Alex's confession can be admitted given his three allegations, and whether he may leave them out of his CFD. The failure to warn him of his right to silence does not by itself exclude the statement; the other two allegations go to voluntariness, which the court must decide at an ancillary hearing where the Prosecution bears the burden beyond reasonable doubt. The threat in (c) gives Alex his best ground. He should not omit the allegations from his CFD.

*(a) No warning of the right to silence.* A witness examined under s 22 CPC may decline to say anything that might expose him to a criminal charge (s 22(2)), but an otherwise admissible statement is not inadmissible merely because the accused was not warned that he need not make it (Explanation 2(d) to s 258 CPC; *PP v Mazlan bin Maidun* [1992] 3 SLR(R) 968 at [13]–[19], [37]). This allegation alone does not exclude the statement, though it forms part of the circumstances.

*Starting point and procedure.* The accused's statement is admissible if the Prosecution relies on it (s 258(1) CPC), but the court must refuse to admit it if its making appears to have been caused by an inducement, threat or promise having reference to the charge, proceeding from a person in authority, and sufficient to give the accused reasonable grounds for supposing he would gain an advantage or avoid an evil of a temporal nature (s 258(3)). The Prosecution must prove voluntariness beyond reasonable doubt (*Chia Chien Wei Kelvin v PP* [1998] 3 SLR(R) 619 at [53]; *Teo Yeow Chuah v PP* [2004] 2 SLR(R) 563 at [20]). Because Alex alleges oppression and a threat, the court must hold an ancillary hearing (s 279(1)), at which the evidence is confined to the ancillary issue (s 279(2)).

*(b) Oppression.* Acts of a person in authority that tend to sap, and have in fact sapped, the maker's free will amount to a threat, inducement or promise (Explanation 1 to s 258). The test is whether the investigation was, by its nature, duration or other attendant circumstances, such as to affect the accused's mind and will so that he spoke when he would otherwise have stayed silent (*Tey Tsun Hang v PP* [2014] 2 SLR 1189 at [113]). The threshold is high. In *PP v Tan Boon Tat* [1990] 1 SLR(R) 287, an accused handcuffed by one hand to a chair for 9 hours without food or drink was treated in a "highly inconsiderate" way, but his statement was voluntary. In *Fung Yuk Shing v PP* [1993] 2 SLR(R) 771, a failure to offer food or drink for 7 hours did not make the statement involuntary. Alex's 8 hours in a T-shirt and shorts in an air-conditioned room is comparable, so this allegation on its own may well fail; a reasoned argument either way is acceptable, and it should be pressed together with (c).

*(c) Threat.* The test is partly objective (was there in fact a threat, inducement or promise?) and partly subjective (did it operate on the accused's mind through hope of escape or fear of punishment connected with the charge?) (*Kelvin Chia* at [53]). Inspector Tom's words threaten indefinite detention unless Alex is "cooperative", which refers to the charge and comes from a person in authority. On Alex's account both limbs are met, and the court must exclude the statement unless the Prosecution proves beyond reasonable doubt that the threat was not made or did not operate on his mind.

*Omitting the allegations from the CFD.* The CFD must specify the facts relied on to challenge voluntariness: it must state any objection to the CFP, with the issue of fact and the points of law (s 165(1)(d) CPC and Illustration 2 to s 165). If Alex omits them, the court may draw an adverse inference because his case at trial differs from his CFD (s 169(1)(c)); the omission damages his credibility and makes admission of the statement more likely; and the CFD itself can be used to cross-examine him (s 258A). The "surprise" gains nothing, because the Prosecution must prove voluntariness beyond reasonable doubt once he raises it (Pre-write 0-21).

Therefore the Prosecution can admit the confession only if, at an ancillary hearing under s 279 CPC, it proves beyond reasonable doubt that the statement was voluntary; the threat allegation is Alex's strongest point, and he should set out all three allegations in his CFD rather than risk an adverse inference under s 169(1)(c) (Pre-write 0-32).

**Q2025-1-4** · `0.VI.8` `0.VI.7` `0.V.3` · PYP 2025 Q1.4 · 7 marks · `pcp-w-0-32` `pcp-w-0-31` `pcp-w-0-21`

*Facts: PYP 2025 Crim Q1, under 0.I.4 above.* The CFP contains Mr Albert's long statement, including: "I did touch Ms. Bebe's buttock. However, I only did it in a moment of drunken impulse. I am sorry!" Mr Albert is horrified but assures you he will firmly deny the offence at trial. Advise him how his statement could be used against him at the trial, and the process involved.

**Answer.**

The issue is how the Prosecution can use Mr Albert's admission at trial. It can tender the statement as evidence of the facts in it, subject to any challenge to its voluntariness at an ancillary hearing; and if he testifies that he did not touch Ms Bebe, it can cross-examine him on the statement and seek to impeach his credit.

*Admission of the statement.* A statement made by the accused to a police officer (of at least sergeant's rank) is admissible (s 258(1)–(2) CPC), unless its making was caused by a threat, inducement or promise or by oppression (s 258(3), Explanation 1). If admitted, it is evidence of the facts it contains, and an admission like this one goes directly to the actus reus. Mr Albert says he was exhausted and signed without reading it in the early hours. If he alleges oppression, the court must hold an ancillary hearing (s 279), at which the Prosecution must prove voluntariness beyond reasonable doubt (*Teo Yeow Chuah v PP* [2004] 2 SLR(R) 563 at [20]). Tiredness alone is unlikely to amount to oppression, given the high threshold (*PP v Tan Boon Tat* [1990] 1 SLR(R) 287), and an otherwise admissible statement is not excluded merely because the accused was intoxicated or not warned that he need not speak (Explanation 2(b), (d)). But his account is still relevant to the weight the court gives the statement and to whether it was accurately recorded (Pre-write 0-32). Any such objection must be stated in his CFD (s 165(1)(d)), or the court may draw an inference (s 169(1)(c)) (Pre-write 0-21).

*Impeachment if he denies touching her.* If Mr Albert testifies that he never touched Ms Bebe, his evidence contradicts his statement. The Prosecution may cross-examine him on it (s 147(1) EA), following the *Muthusamy v PP* [1948] MLJ 57 steps: it identifies the inconsistent parts, the court decides whether the discrepancy is serious or material (*Kwang Boon Keong Peter v PP* [1998] 2 SLR(R) 211 at [21]), the statement is proved, and he is asked to explain; if the explanation is unsatisfactory, his credit may be impeached (s 157(c) EA). An outright admission against an outright denial is plainly material. Impeachment does not automatically mean the court rejects all his evidence (*Loganatha Venkatesan v PP* [2000] 2 SLR(R) 904 at [56]), but it will badly damage his credibility. His CFD, if it states his denial, can also be used in cross-examination (s 258A) (Pre-write 0-31).

*Advice.* Mr Albert must decide, with my advice, whether there is a genuine basis to challenge the statement (oppression, or inaccurate recording) and be ready to explain the inconsistency. A firm denial that ignores the statement will not work. I must also explain that if his instructions change, I cannot put forward a defence inconsistent with what he tells me (r 14(4) PCR).

Therefore the Prosecution will tender the statement as an admission, Mr Albert may challenge its voluntariness at an ancillary hearing where the Prosecution bears the burden, and if it is admitted and he denies the touching, he will be cross-examined on it under s 147 EA and his credit may be impeached under s 157(c) EA.

### 0.VI.9 — Closing submissions, judgment, proof beyond reasonable doubt; counsel's absence

**Own question C10 facts.** Jun ("J") is on trial for theft. The trial resumes next Monday for closing submissions. J's counsel has just been told that a High Court appeal in which he is lead counsel has been fixed for the same Monday.

**Q0-C10-1** · `0.VI.9` · own question · 7 marks · `pcp-w-0-33`

Advise J's counsel on what he must do about the clash, and outline the standard the court will apply in deciding J's guilt.

**Answer.**

The issue is whether counsel may be absent from J's trial and how the court will decide guilt. Counsel may be absent only on reasonable grounds, and must tell J beforehand and try to arrange another practitioner; the court will acquit unless the Prosecution has proved every element beyond reasonable doubt.

*Counsel's absence.* A practitioner must not be absent from a trial or hearing without reasonable grounds; if he is absent, he must inform the accused of the grounds beforehand and make reasonable efforts to arrange for another practitioner to act (r 14(3)(c)–(d) PCR). A clash with a fixed appeal may be a reasonable ground, but counsel's first step should be to ask one court or the other to refix the date. If that fails, he must tell J why he cannot attend and brief a colleague who knows the file; J may prefer to ask for an adjournment.

*Closing and judgment.* At the close of the defence case the defence may sum up and the Prosecution has the final right of reply (s 230(1)(u)–(v) CPC). The burden of proving guilt beyond reasonable doubt always lies on the Prosecution, and fanciful doubts do not suffice (*Jagatheesan s/o Krishnasamy v PP* [2006] 4 SLR(R) 45 at [61]). A doubt is reasonable if it is supported by reasons logically connected to the evidence, and it may arise within the Prosecution's own case or on the totality of the evidence (*PP v GCK* [2020] 1 SLR 486 at [131], [134]–[135]). If the court finds J not guilty it must order a discharge amounting to an acquittal; if guilty, it convicts and proceeds to sentence under s 228 (s 230(1)(w)–(x)). In closing, counsel should take each element of theft, especially dishonesty, and identify the reasoned doubts in the evidence, rather than asserting innocence.

Therefore counsel must try to resolve the clash, and if he cannot attend he must tell J the reason in advance and arrange a properly briefed colleague; the court will convict only if satisfied beyond reasonable doubt on each element (Pre-write 0-33).

### 0.VII Sentencing

Sub-points 0.VII.1–0.VII.4. Tested: 0.VII.2 (2021, 2023), 0.VII.3 (2021, 2022, 2025, SQ), 0.VII.4 (2021). Own question C11 covers 0.VII.1, which PYP 2023 Q2.2 and 2025 Q2.3 also touch.

### 0.VII.1 — Sentencing principles

**Own question C11 facts.** Priya ("P"), 19, a first-year polytechnic student with no antecedents, has pleaded guilty to theft (s 379 PC) of a $600 handbag from a department store. The Prosecution submits that a short imprisonment term is needed to deter shop theft, which it says is prevalent.

**Q0-C11-1** · `0.VII.1` `0.VII.2` · own question · 8 marks · `pcp-w-0-34` `pcp-w-0-35`

What sentencing principle should dominate, and what sentence would you ask for?

**Answer.**

The issue is which sentencing principle should carry most weight for P, and what sentence follows. Rehabilitation should be the dominant consideration because P is a young offender, so I would ask for probation.

*Principles.* The classical principles are retribution, deterrence, prevention and rehabilitation, and the judge must decide which carries most weight on the facts (*R v Sargeant* (1974) 60 Cr App R 74, approved in *PP v Law Aik Meng* [2007] 2 SLR(R) 814 at [24]–[29]). Deterrence is the "cornerstone" of Singapore sentencing, and general deterrence is engaged by a prevalent offence, which is the Prosecution's point. But rehabilitation is the presumptive dominant consideration for young offenders (*Praveen s/o Krishnan v PP* [2018] 3 SLR 1300), so for a 19-year-old first offender the starting point favours rehabilitation unless the offence is serious enough to displace it (Pre-write 0-34).

*Options.* Sentencing options include fines, imprisonment, caning, probation and community sentences (CL6 s12). Where a person is convicted of an offence whose sentence is not fixed by law, the court may make a probation order if it is expedient having regard to the circumstances, including the nature of the offence and the offender's character, with supervision for between 6 months and 3 years (s 5(1) Probation of Offenders Act 1951). Theft under s 379 PC has no mandatory minimum, so probation is available; the proviso confining probation to offenders aged 18 to 20 with no previous such conviction applies only where the offence carries a specified or mandatory minimum sentence. The court calibrates the sentence by aggravating, mitigating and neutral factors: P's lack of antecedents is neutral, while her youth and the remorse shown by her early plea are mitigating (*Chew Soo Chun v PP* [2016] 2 SLR 78 at [30]) (Pre-write 0-35).

*Application.* P is 19, a student with no record; the value is modest and the item was presumably recovered; nothing suggests premeditation or a syndicate. I would ask the court to call for a probation report and submit that probation, with requirements such as residence conditions or community service (s 5(2)–(5) POA), best serves rehabilitation while still marking the offence.

Therefore rehabilitation should dominate (*Praveen*), and I would ask for a probation order rather than imprisonment.

*See also:* Q2023-2-2 (under 0.IV.4) and Q2025-2-3 (under 0.IV.7): a mental condition shifting weight from deterrence to rehabilitation (*Lim Ghim Peow*).

### 0.VII.2 — Sentencing options and calibrating an individual sentence

**Q2023-1-3** · `0.VII.2` `0.IV.7` · PYP 2023 Q1.3 · 6 marks · `pcp-w-0-35` `pcp-w-0-18`

*Facts: PYP 2023 Crim Q1, under 0.I.3 above.* Mr ACC is concerned that s 354(2) PC carries a maximum of 5 years' imprisonment and the possibility of caning. He gives you a stack of testimonials from colleagues and employers, and says this is his first time in such a predicament. He wants to know what you can do to help him avoid caning altogether if he eventually decides to plead guilty. Please advise him.

**Answer.**

The issue is whether, on a plea of guilty, I can persuade the court not to impose caning for the s 354(2) PC charge. Caning is not mandatory for this offence, so I can ask the court to impose imprisonment (or a fine) without caning, relying on every favourable factor; but no outcome can be promised, and he must first decide, on my advice, that he genuinely admits the offence.

*Is caning mandatory?* Section 354(2) PC provides for imprisonment up to 5 years, or fine, or caning, or any combination. The court therefore has a discretion; caning is not compelled. The court calibrates the sentence from precedents or benchmarks, adjusting for aggravating, mitigating and neutral factors (*Chew Soo Chun v PP* [2016] 2 SLR 78 at [30]) (Pre-write 0-35).

*What I can put forward.* On conviction the court must hear the plea in mitigation (s 228(3) CPC), and I must raise every favourable factor (r 14(2) PCR), without scandalous allegations (r 14(7)). I would rely on: an early plea showing genuine remorse and sparing the 9-year-old victim from testifying; his good character, shown by the testimonials; the brief, over-the-clothes nature of the contact; and his personal circumstances. His lack of antecedents is a neutral factor, not a mitigating one (*Chew Soo Chun*), but it supports his character. I would distinguish precedents in which caning was imposed by the aggravating features they had and this case lacks, and submit for an imprisonment term without caning (Pre-write 0-18; Template 0-44). Certain persons cannot be caned at all: women, men over 50 at the time of caning, and men sentenced to death, though the court may then impose up to 12 months' imprisonment in lieu (s 325 CPC); if Mr ACC will be over 50, that matters.

*Two cautions.* First, his present instructions are that he is innocent and the contact was accidental. He may plead guilty only if he admits every element; if he pleads guilty and then says in mitigation that the contact was accidental, the court must reject the plea (s 228(4) CPC) (Pre-write 0-13). Second, I can promise nothing about the outcome (CL1 s15–17); the victim's age will weigh against him.

Therefore, if Mr ACC decides to plead guilty without qualification, I would submit a written mitigation stressing his remorse, character and the low-end nature of the contact, and ask for imprisonment without caning, which the court has power to order because caning under s 354(2) PC is discretionary.

**Q2021-1-4** · `0.VII.2` · PYP 2021 Q1.4 · 5 marks · `pcp-w-0-35`

*Facts: PYP 2021 Crim Q1, under 0.V.3 above. Robbery by night under s 392 PC carries a mandatory minimum of 3 years' imprisonment and 12 strokes of the cane (Q1.5). Bill was 25 at the time of the offences and 26 by conviction.* Given Bill's age and the prescribed punishment, would he be eligible for probation if convicted of all charges?

**Answer.**

The issue is whether probation is open to Bill. It is not, because robbery by night carries a mandatory minimum sentence and Bill is over 21 at conviction.

Where a person is convicted of an offence whose sentence is not fixed by law, the court may make a probation order instead of sentencing him if it is expedient to do so (s 5(1) Probation of Offenders Act 1951); there is no general age limit. But where the offence carries a specified minimum or mandatory minimum sentence of imprisonment, fine or caning, probation is available only if the offender (a) is at least 18 but under 21 at conviction, and (b) has no previous conviction for such an offence (s 5(1) proviso). Robbery by night carries a mandatory minimum of 3 years' imprisonment and 12 strokes. Bill has no previous conviction, so limb (b) is met, but he was 26 at conviction (and 25 even at the time of the offences), so limb (a) fails. The same mandatory minimum also rules out community sentences (s 337(1) CPC) (Pre-write 0-35).

Therefore Bill is not eligible for probation on the robbery charges; at least the mandatory minimum must be imposed for each.

### 0.VII.3 — Aggregate sentence: s 307(1), one-transaction rule, totality

**Q2025-2-4** · `0.VII.3` · PYP 2025 Q2.4 · 9 marks · `pcp-w-0-36`

*Facts: PYP 2025 Crim Q2, under 0.III.3 above.* Ms Wing pleads guilty to Charges 1–4 (trespass and theft on 4 April; trespass and theft on 11 April), with Charges 5–6 taken into consideration. Both parties agree that four weeks' imprisonment for each proceeded charge is appropriate, but the prosecutor argues that all four terms should run consecutively, for 16 weeks in total. As defence counsel, how would you respond?

**Answer.**

The issue is whether all four terms should run consecutively. They should not: s 307(1) CPC requires only two of the four to run consecutively; the trespass and theft on each night form one transaction and should run concurrently; and the totality principle points to an aggregate of 8 weeks, not 16.

*Section 307(1).* Where an accused is convicted and sentenced to imprisonment for at least three distinct offences, at least two terms must run consecutively (s 307(1) CPC). With four terms, the court must order at least two consecutively, but it is not required to order more. The Prosecution's 16 weeks is not compelled by statute.

*One-transaction rule.* Sentences for distinct offences committed on separate occasions should generally run consecutively, but sentences for offences forming a single transaction should run concurrently. A single transaction is a single invasion of the same legally protected interest, with proximity in time, place, continuity of action and continuity of purpose or design (*Mohamed Shouffee bin Adam v PP* [2014] 2 SLR 998 at [27]–[34]). On 4 April Ms Wing trespassed at 3.52am in order to take a macaw, which she did at 4.19am, in the same park; on 11 April the trespass (11.42pm) and theft (11.58pm) were 16 minutes apart. Each night's trespass and theft invaded the same interest (the park's property and premises), were close in time and place, and had one purpose: to take a bird. Each pair is one transaction, so Charges 1 and 2 should run concurrently, and Charges 3 and 4 likewise. The two nights a week apart are separate occasions, so one term from each night may run consecutively, which also satisfies s 307(1): for example Charge 2 consecutive with Charge 4, giving 8 weeks.

*Totality.* As a "last look", the aggregate should not be substantially above the normal level of sentences for the most serious individual offence, and its effect should not be crushing and out of keeping with the offender's record and prospects (*Shouffee*). Sixteen weeks is four times the agreed sentence for a single theft of one bird, and for a 50-year-old first offender acting out of grief and depression, with Charges 5–6 already reflected as TIC, it is disproportionate. Eight weeks is proportionate.

Therefore I would submit that only two terms (one from each night) should run consecutively, with each night's trespass and theft concurrent, for an aggregate of 8 weeks' imprisonment (Pre-write 0-36).

**QSQ-1-4** · `0.VII.3` · SQ Crim Q1.4; official guide SQ p125 · 8 marks · `pcp-w-0-36`

*Facts: SQ Crim Q1, under 0.I.1 above.* After Mr Loh pleads guilty to criminal intimidation (s 506 PC) and carrying an offensive weapon (s 6(1) Corrosive and Explosive Substances and Offensive Weapons Act 1958), the Prosecution asks for six months' imprisonment on each charge, to run consecutively for 12 months. Mr Loh asks: "How can they ask for six months for each of the charges? This was just one foolish incident!" Advise him whether the consecutive approach is appropriate.

**Answer.**

The issue is whether the two six-month terms should run consecutively. On the one-transaction rule and the totality principle they should run concurrently, for an aggregate of six months.

*The rules.* Section 307(1) CPC (at least two consecutive terms where three or more imprisonment terms are imposed) is not engaged by two terms, so the court has a free hand. Sentences for offences in a single transaction should run concurrently; for separate transactions, consecutively. A single transaction is a single invasion of the same legally protected interest, with proximity in time and place, continuity of action and continuity of purpose (*Mohamed Shouffee bin Adam v PP* [2014] 2 SLR 998 at [27]–[34]). The totality principle then requires a "last look": the aggregate should not be substantially above the normal level of sentence for the most serious individual offence (limb 1), and should not be crushing and out of keeping with the offender's record and prospects (limb 2).

*Application.* Both offences arose from one incident in one cinema seat in the course of one film: Mr Loh, with the penknife already on him, whispered the threat and showed the knife in the same moment, with the single purpose of making the person stop talking. They are proximate in time and place, with continuity of action and purpose. The Prosecution will argue that carrying an offensive weapon protects a different interest (public safety generally) from criminal intimidation (the person threatened), so that the interests are distinct and consecutive terms are justified. But here the knife was carried and used as the instrument of the threat to the same person, and the possession charge adds little beyond what the intimidation charge already captures. On totality, 12 months is double the normal sentence the Prosecution itself proposes for either offence (limb 1), and for a teacher of previously good character who will lose his job, it is crushing (limb 2). Even if the court considers the interests distinct, totality supports a substantial reduction in the aggregate.

Therefore I would submit that the two sentences should run concurrently for an aggregate of six months, as the offences form one transaction and 12 months offends both limbs of the totality principle (Pre-write 0-36).

**Q2022-2-3** · `0.VII.3` · PYP 2022 Q2.3 · 10 marks · `pcp-w-0-36`

*Facts: PYP 2022 Crim Q2, under 0.IV.2 above.* Brian's plea was rejected. While on bail he committed three more offences: theft (s 379 PC) of a $1,000 laptop from a Challenger outlet on 6 June 2022; outrage of modesty (s 354(1)) by touching Frieda Chan's buttocks on 7 June 2022; and voluntarily causing hurt (s 323) by punching the same Frieda Chan in the face on 7 June 2022. No plea offer is made; Brian pleads guilty to all four offences and the court imposes: s 324 — 1 year's imprisonment and 3 strokes; s 379 — 1 month; s 354(1) — 1 month; s 323 — 3 months. As the Judge, what global sentence would you impose, and which sentences run consecutively or concurrently?

**Answer.**

The issue is how the four imprisonment terms should be aggregated. At least two must run consecutively; the s 324 offence and the 7 June offences against Frieda Chan are separate transactions, and the laptop theft on 6 June is a further separate transaction; the two 7 June offences against Frieda form one transaction. I would run the s 324 term consecutively with the s 323 term and the theft term, with the s 354(1) term concurrent, for a global sentence of 1 year and 4 months' imprisonment and 3 strokes of the cane.

*Section 307(1).* Brian is sentenced to imprisonment for four distinct offences, so at least two terms must run consecutively (s 307(1) CPC); the cane is unaffected.

*One-transaction rule.* Offences on separate occasions generally run consecutively; offences in a single transaction (a single invasion of the same legally protected interest, proximate in time and place, with continuity of action and purpose) run concurrently (*Mohamed Shouffee bin Adam v PP* [2014] 2 SLR 998 at [27]–[34]). The s 324 offence (Christmas 2021, Dean) is wholly separate from the 2022 offences. The laptop theft (6 June, Challenger, property) is a separate occasion and interest from the 7 June offences. The touching and the punch of Frieda Chan on 7 June were committed against the same person, apparently in one encounter, and both invade her bodily integrity; they are best treated as one transaction, so the shorter s 354(1) term runs concurrently with the s 323 term. That leaves three transactions: s 324 (12 months), the laptop theft (1 month) and the Frieda Chan incident (3 months). Brian committed the 2022 offences while on bail for the s 324 charge, which supports marking each separate episode with a consecutive term.

*Totality.* An aggregate of 16 months (12 + 1 + 3) is a modest step above the 12 months for the most serious offence (limb 1) and is not crushing for a young man who re-offended three times while on bail (limb 2) (Pre-write 0-36). Running the s 354(1) term consecutively as well (17 months) would double-count the single incident with Frieda Chan; running the theft concurrently (15 months) would fail to reflect a distinct offence against a different victim committed on bail. Either 15 or 16 months is within the range of a reasoned answer; the key is to reason from s 307(1), the one-transaction rule and totality.

Therefore I would order the s 324, s 379 and s 323 terms to run consecutively and the s 354(1) term concurrently, for a global sentence of 16 months' imprisonment and 3 strokes of the cane.

**Q2021-1-5** · `0.VII.3` · PYP 2021 Q1.5 · 10 marks · `pcp-w-0-36`

*Facts: PYP 2021 Crim Q1, under 0.V.3 above.* The District Judge convicts Bill of all six charges, imposing the mandatory minimum of 3 years' imprisonment and 12 strokes for each robbery by night and 18 months for voluntarily causing grievous hurt to Jerry. He orders the sentences for the first and fifth robberies to run consecutively with the grievous hurt sentence: 7 years 6 months and 24 strokes in all. He notes the small sums taken (under $1,000 each time) and says he has balanced general deterrence against the need for a "proportionate" and "not crushing" sentence. Bill wanted all sentences concurrent so he could serve them "at one shot", and says the Judge failed to apply the one-transaction rule because his offences "were all so similar". Is the Judge justified, and does Bill have any basis for his complaint?

**Answer.**

The issue is whether three consecutive terms are justified, and whether the one-transaction rule required concurrent sentences. The Judge was justified: s 307(1) CPC forbids all-concurrent sentences, the five robberies were separate transactions, and the grievous hurt to Jerry invaded a different interest; Bill's complaint that the offences were "similar" misunderstands the rule.

*Section 307(1).* Bill was sentenced to imprisonment for six distinct offences, so at least two terms had to run consecutively (s 307(1) CPC). Serving everything "at one shot" was never open to him.

*One-transaction rule.* Offences committed on separate occasions should generally run consecutively; only offences that form a single transaction (a single invasion of the same legally protected interest, with proximity in time and place, continuity of action and continuity of purpose and design) run concurrently (*Mohamed Shouffee bin Adam v PP* [2014] 2 SLR 998 at [27]–[34]). The test is not whether offences are similar. Each robbery was against a different kiosk and attendant on a different night: separate occasions and separate invasions of different victims' interests. The grievous hurt to Jerry occurred during the fifth robbery, so it was proximate in time and place, but it invaded a different legally protected interest (Jerry's bodily integrity, not the kiosk's property) against a different victim, so it is not part of the same transaction as the robbery. Running it consecutively was open to the Judge.

*Totality.* As a last look, the aggregate should not be substantially above the normal level for the most serious offence, and should not be crushing (*Shouffee*); but totality cannot be used to minimise punishment where the facts warrant severity (*ADF v PP*, per Cyril-Exam §7.7.2), and it remains subject to s 307(1). The Judge chose three of six terms, explained that the small sums taken justified restraint, and expressly considered proportionality and whether the sentence was crushing. Five planned night-time robberies of lone elderly attendants with a weapon, and a violent assault causing multiple fractures, justify an aggregate well above the minimum for a single robbery. Seven years six months, out of a possible 16 years six months had every term run consecutively, is a measured result.

Therefore the Judge was justified in running three sentences consecutively, and Bill has no real basis to say the one-transaction rule was misapplied (Pre-write 0-36).

### 0.VII.4 — Other sentencing orders: deferment, backdating, fines, withdrawal, disposal of property

**Q2021-2-6** · `0.VII.4` · PYP 2021 Q2.6 · 5 marks · `pcp-w-0-37`

State the likely disposal orders under s 364(2) CPC for: (a) a wallet and its contents, stolen by the accused from the victim; (b) a Rolex watch that X stole from Y and pawned for cash, seized by the police from the pawnshop; (c) a knife with a 30-cm blade used by the accused in a robbery, which he says has sentimental value as a family heirloom; (d) the accused's laptop, seized in investigations into voyeurism offences, which contained no voyeuristic material or evidence of the offences; (e) $10,000 in the accused's account, admitted to be proceeds of illegal remote gambling.

**Answer.**

Under s 364(2) CPC, where property in respect of which an offence was committed, or which was used or intended for an offence, or which constitutes evidence, is produced before or in the custody of the court or the police, the court may order it forfeited, confiscated, destroyed or delivered to any person; property includes what it has been converted into (s 364(4)), and competing claims are decided at a disposal inquiry (Pre-write 0-37).

(a) **Wallet and contents:** delivered to the victim, the owner from whom it was stolen.

(b) **Rolex:** the owner (Y) and the pawnbroker, who paid X for it, have competing claims, so the court is likely to hold a disposal inquiry to decide which of them it should be delivered to.

(c) **Knife:** an instrument used to commit the robbery; it is likely to be forfeited or destroyed despite its claimed sentimental value, which does not outweigh the risk of returning a weapon used in a violent offence.

(d) **Laptop:** it contains no evidence of the offences and was not used for them, so it is likely to be returned to the accused.

(e) **$10,000:** admitted proceeds of illegal gambling, property in respect of which an offence was committed; likely to be forfeited.

Therefore the likely orders are: (a) return to the victim; (b) a disposal inquiry between Y and the pawnbroker; (c) forfeiture or destruction; (d) return to the accused; (e) forfeiture.

*See also:* Q2021-2-3 under 0.VIII.5 (a deferred sentence and a request for further deferment, s 318 CPC).

### 0.VIII Appeals and other applications

Sub-points 0.VIII.1–0.VIII.6. Tested: 0.VIII.1 (2021), 0.VIII.2 (2021, 2025), 0.VIII.3 (2021), 0.VIII.4 (2025), 0.VIII.5 (2021). Own question C7 (under 0.V.6) covers 0.VIII.6.

### 0.VIII.1 — What can be appealed, by whom, and to which court

See Q2021-1-3 under 0.VI.3 (no appeal against an interlocutory admissibility ruling, *Knight Glenn*) and Q2025-2-5 under 0.VIII.2 (no appeal against conviction after a plea of guilty, s 375 CPC).

### 0.VIII.2 — Appeal procedure and timelines

**Q2025-2-5** · `0.VIII.2` `0.VIII.1` `0.VIII.3` `0.VIII.4` · PYP 2025 Q2.5 · 6 marks · `pcp-w-0-39` `pcp-w-0-38` `pcp-w-0-40` `pcp-w-0-41`

*Facts: PYP 2025 Crim Q2, under 0.III.3 above.* The judge accepts the prosecutor's submission and imposes an aggregate sentence of 16 weeks' imprisonment. Ms Wing says: "This is outrageous, it's unfair! Surely there's something we can do about this?" Advise her on her appellate options, including the procedural timelines and the potential risks of an appeal.

**Answer.**

The issue is whether and how Ms Wing can challenge her 16-week aggregate sentence. She cannot appeal against conviction because she pleaded guilty, but she may appeal against sentence to the General Division of the High Court, filing a Notice of Appeal within 14 days and a Petition of Appeal within 14 days of receiving the grounds; she should also seek bail and a stay pending appeal. Her prospects are reasonable, but the court could dismiss the appeal or even increase the sentence.

*What she can appeal.* A convicted person may appeal against her sentence (s 374(4) CPC), but not against a conviction on her own plea of guilty (s 375). Only a party may appeal (s 377(1)). An appeal from the State Courts lies to the General Division of the High Court (s 19 SCJA), as a Magistrate's Appeal, usually before one judge (s 386(1)) (Pre-write 0-38).

*Timelines and documents.* She must file a Notice of Appeal (Form 66, Criminal Procedure Rules 2018) within 14 days of the sentence (s 377(2) CPC). The record of proceedings and the judge's grounds of decision are then prepared and served. She must file a Petition of Appeal (Form 67) within 14 days of receiving them (s 378(1)), setting out every ground, since she may not rely on grounds outside it without permission (s 378(6)); if no Petition is filed the appeal lapses (s 378(3)). The appeal may be summarily rejected if the grounds raise no question of law and there is nothing to suggest the sentence should be reduced (s 384) (Pre-write 0-39).

*Staying out of prison meanwhile.* An appeal does not stay execution, but she may apply for bail pending appeal (s 382) and a stay of execution (s 383). The court weighs the *PP v Adith s/o Sarvotham* [2014] 3 SLR 649 factors at [29], [32], including the risk of absconding, her record, the gravity of the offences, and the length of the sentence compared with the time the appeal will take. A 16-week sentence could be largely served before the appeal is heard, which would make the appeal nugatory; with no record and no flight risk, a stay is likely (Pre-write 0-40).

*Prospects and risks.* The appellate court will intervene only if the sentence is wrong in law or manifestly excessive (s 394 CPC), for example because the judge erred in principle or failed to appreciate the material (*PP v UI* [2008] 4 SLR(R) 500 at [12]), and only where substantial rather than minute alteration is needed (*PP v Siew Boon Loong* [2005] 1 SLR(R) 611 at [22]). Running the trespass and theft on each night consecutively ignores the one-transaction rule, an error of principle, and doubling the necessary 8 weeks is a substantial difference (Pre-write 0-36). The risks: the court may dismiss the appeal, the appeal may be summarily rejected, and on her own appeal the court may even enhance the sentence without a Prosecution cross-appeal (*Wong Tian Jun De Beers v PP* [2021] SGHC 273; s 390(1)(c)) (Pre-write 0-41).

Therefore Ms Wing should file a Notice of Appeal against sentence within 14 days, apply at once for bail and a stay pending appeal, and file her Petition within 14 days of receiving the grounds, arguing that 16 weeks is wrong in principle and manifestly excessive, understanding the risk that the sentence may be increased.

### 0.VIII.3 — Bail and stay of execution pending appeal

**Q2021-1-6** · `0.VIII.3` `0.VIII.2` · PYP 2021 Q1.6 · 5 marks · `pcp-w-0-40` `pcp-w-0-39`

*Facts: PYP 2021 Crim Q1, under 0.V.3 above; Bill was convicted after trial and sentenced to 7 years 6 months and 24 strokes (Q1.5).* If Bill remains dissatisfied with the verdict and his sentence, and is adamant about not wanting to spend a day in prison, what immediate steps should he take?

**Answer.**

The issue is how Bill can appeal and avoid starting his sentence meanwhile. He must file a Notice of Appeal within 14 days of sentence and apply at once for bail pending appeal and a stay of execution; but given the length of his sentence and the gravity of the offences, a stay is unlikely.

*Appeal.* Having claimed trial, Bill may appeal against both conviction and sentence (s 374(4) CPC) to the General Division. He must file a Notice of Appeal in Form 66 within 14 days; for an appeal against conviction, time runs from the date of sentence (s 377(2)(a)). He then files a Petition of Appeal within 14 days of receiving the record of proceedings and grounds of decision (s 378(1)), or the appeal lapses (s 378(3)). If he is already in prison, he may simply tell the prison authorities that he wishes to appeal (s 381) (Pre-write 0-39).

*Bail and stay.* An appeal does not stay execution; the court may grant bail pending appeal (s 382) and stay execution on reasonable terms (s 383). It weighs the *PP v Adith s/o Sarvotham* [2014] 3 SLR 649 factors at [29], [32]: the risk of absconding, criminal record, the risk of reoffending on bail, sufficiency of security, the interests of a fair prosecution, prejudice to the convicted person, the nature and gravity of the offence, the length of the sentence compared with the time the appeal will take, and whether prejudice can be met by other measures. In Bill's favour: no previous record. Against him: five robberies with a weapon and a violent assault, a long sentence (with caning) that he faces a strong incentive to avoid, and a 7½-year term that cannot be served before the appeal is heard, so refusing a stay will not make the appeal nugatory (Pre-write 0-40).

Therefore Bill should file his Notice of Appeal within 14 days of sentence and apply immediately for bail and a stay pending appeal, offering substantial security and conditions; but he should be told that, on the *Adith* factors, he is unlikely to avoid starting his sentence.

### 0.VIII.4 — Powers on appeal; enhancement; threshold

See Q2025-2-5 under 0.VIII.2 (the threshold under s 394 CPC and *PP v UI*; the risk of enhancement on the accused's own appeal, *Wong Tian Jun De Beers*).

### 0.VIII.5 — Criminal motion to extend time to appeal

**Q2021-2-3** · `0.VIII.5` `0.VII.4` `0.VIII.3` · PYP 2021 Q2.3 · 5 marks · `pcp-w-0-42` `pcp-w-0-37` `pcp-w-0-40`

A new client pleaded guilty three weeks ago to mischief (drawing graffiti at a void deck) and was sentenced to imprisonment. The court deferred the start of the sentence by four weeks, so he begins serving it a week from today. He thinks the sentence is too harsh and that he should only have been fined. He wants to appeal against sentence. Explain what needs to be done.

**Answer.**

The issue is how the client can appeal against sentence when the 14-day period has passed and his sentence starts in a week. He must apply by criminal motion for permission to appeal out of time, and at the same time seek a further deferment or stay so that the appeal is not overtaken by the sentence.

*Out of time.* A Notice of Appeal must be filed within 14 days of sentence (s 377(2) CPC); three weeks have passed, so he is out of time. He pleaded guilty, so he can appeal only against sentence, not conviction (s 375). The appellate court may, on the application of a person debarred from appealing for non-compliance with the CPC, permit him to appeal in the interests of justice, on such terms as it thinks fit (s 380(1)). The application is made by criminal motion, the vehicle for ancillary relief tied to an appeal (*Amarjeet Singh v PP* [2021] 4 SLR 841 at [27]–[28], [33]), supported by an affidavit. The court weighs (a) the length of the delay, (b) the explanation for it, and (c) whether the appeal has some prospect of success (*PP v Tan Peng Khoon* [2016] 1 SLR 713 at [38], [45]). Here the delay is about a week, which is short; he must explain why he did not file in time (for example, that he did not know of the 14-day limit or was unrepresented); and he must show the sentence is arguably manifestly excessive, the threshold for intervention (s 394; *PP v UI* [2008] 4 SLR(R) 500 at [12]) (Pre-write 0-42).

*The sentence starting in a week.* The court that sentenced him may defer a sentence for good reasons (s 318(1)–(2) CPC), and the appellate court may stay execution pending appeal (s 383) and grant bail (s 382). Since a short custodial sentence could be served before the appeal is heard, which would make the appeal pointless, I would apply for a stay (or further deferment) together with the criminal motion, relying on the *Adith* factor of sentence length against appeal time (Pre-writes 0-37, 0-40).

*Risks.* He should know the court may dismiss the appeal or even enhance the sentence on his own appeal (*Wong Tian Jun De Beers v PP* [2021] SGHC 273) (Pre-write 0-41).

Therefore I would file a criminal motion under s 380 CPC for permission to appeal against sentence out of time, with an affidavit explaining the short delay and the merits, and apply at once for a stay of execution or further deferment and bail pending the appeal.

### 0.VIII.6 — Fresh evidence on appeal

See Q0-C7-1 under 0.V.6 (undisclosed CCTV found after conviction; s 392 CPC and *Ladd v Marshall*).

## 1 · Family Law Practice

The 2021 and 2022 Family papers each set one long fact pattern with three questions: Q1 "advise on all issues pertaining to her intended divorce proceedings as well as the ancillary matters … [and] on [the] Personal Protection Order"; Q2 draft the Statement of Particulars; Q3 mediation. Q1 is split here by issue (Q2021F-1a to 1e, Q2022F-1a to 1g) and each part is placed under its Sub-point; in the exam it is one answer. Their facts are summarised once, under 1.I.2.

### 1.I Therapeutic justice, mediation and the family lawyer

Sub-points 1.I.1–1.I.3. Tested: 1.I.2 (2021, 2022). Own question F1 covers 1.I.1 and 1.I.3.

### 1.I.1 — Therapeutic justice and the lawyer's role

**Own question F1 facts.** Rachel ("R") has been married to Sam for 12 years; they have two sons, aged 8 and 11. She has just learnt that Sam has had a long affair. She wants to file for divorce at once, "make him pay", ask for sole custody so that he "loses the boys", and have you send Sam a letter "that tells him exactly what kind of man he is".

**Q1-F1-1** · `1.I.1` `1.I.3` `1.I.2` · own question · 8 marks · `pcp-w-1-1` `pcp-w-1-3` `pcp-w-1-2`

Advise R on how her case will be approached and what she must do before filing.

**Answer.**

The issue is how R's instructions fit the Family Justice Courts' approach and the steps required before filing. The court will take a non-adversarial, forward-looking approach focused on the boys' future; I will conduct the case collaboratively and cannot simply be her mouthpiece; and before filing she must make an offer of amicable resolution and complete the Co-Parenting Programme.

*Therapeutic justice.* Therapeutic justice is a non-adversarial, problem-solving approach that should allow healing and the recasting of a positive future; it is "a necessity", since damaged relationships cannot be repaired by material recompense (*VDZ v VEA* [2020] 2 SLR 858 at [75], [77]). Family practitioners must be aware of how they influence parenting disputes, including through the language of their correspondence, and work as a team to solve problems (*VDX v VDY* [2021] SGHCF 2 at [40]). Counsel are not mere mouthpieces of their clients and must counsel, and if necessary admonish, them (*BOI v BOJ* [2018] SGCA 61 at [139]). The FJC's TJ Model (2024) describes a judge-led process in which parties and lawyers work together towards timely and enduring solutions, and conduct inconsistent with it may attract costs orders (TJ Model para 19) (Pre-write 1-1).

*Application.* I would explain to R that the court looks forward, not back; that Sam's affair will not punish him on custody or division, since custody turns on the boys' welfare and division on contributions (Pre-writes 1-12, 1-18); and that an accusatory letter would inflame matters, hurt the boys and could count against her on costs. I would write to Sam in measured terms. I must tell her of all reasonably available dispute resolution options, advise her to consider resolving matters amicably, advise her to be constructive, and advise her to consider the boys' welfare and that the court decides on their welfare, not on her wishes (r 15A PCR) (Pre-write 1-2).

*Before filing.* Under the Family Justice (General) Rules 2024 ("FJ(G)R") a party must make an offer of amicable resolution before commencing proceedings unless there are reasonable grounds not to, and must not reject one without reasonable grounds (P 4 r 1(2)–(3)). Failing to make one may lead the court to disallow or reduce her costs or order her to pay costs (P 22 r 5(c)); an offering party who obtains a result no less favourable than her offer is, subject to the court's discretion, entitled to indemnity costs from the offer date (P 4 r 4(3)). Nothing here (such as family violence) gives her reasonable grounds not to make one. As the boys are under 21, she must also complete the Mandatory Co-Parenting Programme before filing (s 94A WC) (Pre-write 1-4). Once proceedings start, the case is judge-led: the court manages issues, evidence and timelines through case conferences, may order mediation and counselling, and things said without prejudice at a case conference remain inadmissible (P 8, including r 5 and r 7) (Pre-write 1-3).

Therefore I would advise R to put the boys' interests first, let me write to Sam in measured terms with an offer of amicable resolution, complete the Co-Parenting Programme, and approach the divorce as a judge-led, problem-solving process rather than a means of punishing Sam.

### 1.I.2 — PCR r 15A; reconciliation; mandatory mediation and counselling; FJC mediation

**PYP 2021 Family facts (summary).** Christine, 35, a Hong Kong citizen and Singapore PR, married Ken, 35, a Singaporean by birth, in 2015. She has not worked; she receives dividends of about HKD 1m (S$170,000) a year as a minority shareholder in her parents' business, which she has received since age 25. Ken earns over S$25,000 a month in HSBC private banking. After marriage they lived with Ken's parents in his River Valley condominium, bought before the marriage with his parents' money and in his sole name; it was later sold at a large profit, Ken repaid his parents and kept the profit. Her parents gave the couple a Grange Road bungalow as a wedding gift, in joint names and fully paid by them; the couple (and Ken's parents) moved in in 2016. From mid-2020 Ken "gambled" on stocks, lost heavily, borrowed from friends, lost his temper at Christine and, without her knowledge, withdrew over S$1m from their joint account (into which each had paid S$10,000 a month). Christine also owns two Hong Kong properties (gifts from her parents), a Bukit Timah Road property bought in 2017 for S$2.75m at Ken's urging (now worth S$3.5m), and a Hong Kong bank account holding the rest of her dividends. She knows nothing of Ken's assets. Their twins, Marcus and Charlotte, were born on 13 February 2017. In January 2021 Christine moved with the twins to the Bukit Timah property without Ken's consent; Ken confronted her there and slapped, punched and kicked her, and she was hospitalised; meanwhile the twins were kept by Ken's parents. She declined to pursue a police report and moved back, but was then kept from caring for the children. By April 2021 she had moved out of the master bedroom; Ken came home drunk in the mornings. On 29 June 2021 he physically abused her again while drunk; she fled to Bukit Timah with Marcus, leaving Charlotte. For 4 months Ken has refused her any contact with Charlotte, even by video, and has never asked for Marcus. Christine is tearful and depressed. She wants a divorce, Charlotte back immediately, and to return to Hong Kong with both children; in desperation she would leave Charlotte with Ken and go with Marcus. She asks about maintenance and division.

**PYP 2022 Family facts (summary).** Cherry, 42 (a Malaysian who became a Singapore citizen in 2006), married Daniel, 50, a Singapore citizen, in Singapore on 14 February 2002. They have twin daughters, Carissa and Calista, born 6 August 2010. Daniel also has a son, Raymond, now 16, from a 2006 affair; Raymond's mother abandoned him to Daniel at birth, Cherry forgave Daniel after counselling and raised Raymond as her own, and Raymond does not know she is not his mother; the three children are very close. Cherry gave up her S$2,000-a-month job as a gym instructor in 2006 to care for Raymond and then the twins; Daniel insisted she stay at home. Daniel rose to be a director earning over S$40,000 a month, invested heavily and profitably in shares, and retired about two years ago, refusing to share any details of his investments. The couple first lived with Daniel's parents in an Ang Mo Kio terrace house registered in the names of Daniel and his parents and fully paid before the marriage; Cherry paid S$30,000 towards renovating it. In 2012 they bought a Bukit Timah apartment for S$2m in joint names, Daniel paying the bulk and Cherry contributing CPF monies and S$20,000. Daniel's assets include his share of the Ang Mo Kio house, a Maserati, Citibank accounts and shares of unknown value, CPF monies, watches and wine, and a Singapore Island Country Club membership. Cherry has a BMW X5 paid for by Daniel, CPF monies, watches and handbags given by Daniel, and a POSB account holding about S$240,000, built up by transferring the unspent S$5,000 a month of the S$15,000 Daniel paid into their joint OCBC account for the household; Daniel does not know of it. After retiring, Daniel came home later and later; in early 2022 a private investigator found he frequented KTV lounges and massage parlours and had a relationship with a lounge hostess, checking into a nearby hotel with her at night. On 18 March 2022, in a quarrel over this, Cherry threw a chair in Daniel's direction; it hit Calista, who fell. Daniel left that night with Raymond and has not returned. The twins have not seen him for 8–9 months and miss him; Cherry accepts he has been a dutiful father but wants him to have no contact. He has stopped all financial support. Cherry wants a divorce. Daniel has applied for a Personal Protection Order for himself and Calista, and has sent Cherry threatening texts saying he will fight her "tooth and nail" over the children. Cherry would like to stay silent about her POSB account.

**Q2021F-3** · `1.I.2` · PYP 2021 FAM Q3 · not mark-weighted · `pcp-w-1-2`

*Facts: PYP 2021 Family, above.* Christine's parents do not want a protracted divorce. They understand the Family Justice Courts provide mediation and hope the matter can be resolved quickly, without fuss or media coverage. Christine would like to know the advantages of mediation, the process, and what she must do to prepare.

**Answer.**

The issue is what mediation offers Christine and how she should prepare. Because the twins are under 21, the court must in any event order mediation and/or counselling once proceedings begin; mediation at the FJC is confidential, keeps the outcome in the parties' hands and saves cost and acrimony, which meets her parents' concerns.

*My duties and the statutory framework.* I must tell Christine of all reasonably available dispute resolution options, including mediation and counselling; advise her to consider resolving matters amicably whenever reasonably possible; advise her to be constructive and reasonable; and advise her to consider the twins' welfare and the adverse impact of proceedings on them (r 15A PCR). The court must from time to time consider the possibility of reconciliation (s 139F WC). In divorce proceedings involving children below 21, the court must order the parties to attend mediation and/or counselling unless that is not in their or the children's interests (s 139I); non-compliance can lead to a stay or costs. Anything said or done in mediation or counselling is inadmissible (s 139B).

*Process at the FJC.* The case usually begins with a Family Dispute Resolution conference before a judge-mediator, with the parties, their solicitors and a court counsellor, to set the issues. There may be counselling or an intake session (parties alone) on the children's arrangements, then mediation sessions (judge-mediator, solicitors and clients) covering all issues with a focus on the children; high-conflict custody disputes may go to co-mediation. Any settlement is recorded in a draft consent order. The FJC does not mediate contested asset issues where gross known assets are $2 million or more and no child issue is contested; here the children's arrangements are hotly contested, so FJC mediation is available, though the parties could also use private mediation for the assets (FL8 s8–14, s22).

*Advantages.* It is non-adversarial; the parties decide and control the outcome rather than having one imposed; it allows practical solutions without blame; it saves time and costs; it avoids the trauma of contested hearings; and, important to her parents, what is said is confidential and inadmissible (s 139B), with no public hearing (FL8 s25–26).

*Preparation.* I would explain the process and its purpose; explore her options and advise whether her positions are reasonable (for instance that relocating the twins to Hong Kong needs Ken's consent or the court's leave, and that she should not offer to leave Charlotte behind as a bargaining chip); encourage an open mind and readiness to compromise; and prepare a written case summary. She should gather documents: her dividend records and Hong Kong bank statements, title and valuation documents for Grange Road, Bukit Timah and the Hong Kong properties, the joint account statements showing Ken's withdrawals, her renovation receipts, and a budget of her and the children's monthly expenses (FL8 s15–21). Her safety must also be considered: given Ken's violence, I would ask for arrangements so that she need not be alone with him, and pursue a protection order separately (Q2021F-1e).

Therefore mediation is likely to be ordered anyway, offers a confidential and quicker route to settlement, and Christine should come prepared with documents, a clear but realistic position on the children and finances, and an open mind (Pre-write 1-2).

**Q2022F-3** · `1.I.2` · PYP 2022 FAM Q3 · not mark-weighted · `pcp-w-1-2`

*Facts: PYP 2022 Family, above.* Cherry would like to know the advantages of mediation, the process of mediation and what she needs to do to prepare.

**Answer.**

The issue is what mediation offers Cherry and how she should prepare. As in Q2021F-3, the court must order mediation and/or counselling because the children are under 21 (s 139I WC); I must advise her on all dispute resolution options and amicable settlement and on the children's welfare (r 15A PCR); and things said in mediation are inadmissible (s 139B) (Pre-write 1-2).

*Process.* A Family Dispute Resolution conference before a judge-mediator sets the issues; counselling or an intake session addresses the children; mediation sessions with the judge-mediator, solicitors and parties cover all issues, focused on the children; a settlement is recorded as a draft consent order. With contested child issues (the twins, Raymond, Daniel's access), FJC mediation is available even though the assets may exceed $2 million.

*Advantages for Cherry.* She and Daniel decide the outcome; she avoids a contested hearing in which the children's loyalties are tested and in which her own conduct (the chair incident) would be aired; it is quicker and cheaper; it allows practical arrangements (such as how Raymond and the twins keep their bond, and how the children see their father) that a court order cannot fine-tune.

*Preparation.* Cherry should keep an open mind and be ready to compromise, especially on Daniel's contact with the children, since the court will not cut a dutiful father out (Pre-write 1-20). She should prepare a written summary and documents: CPF statements, Bukit Timah title and loan documents, valuations, the Ang Mo Kio renovation costs, the OCBC joint account statements, her POSB statements (which she must disclose, Q2022F-1f), car documents, and a budget of her and the children's monthly expenses. On Daniel's finances she should list what she knows and ask, through mediation or disclosure orders, for his investment and bank records (Pre-write 1-37).

Therefore Cherry should approach mediation prepared, with full disclosure of her own assets and a realistic position on the children, as it offers the best chance of a durable settlement.

### 1.I.3 — Offer of amicable resolution; judge-led approach

See Q1-F1-1 under 1.I.1 (offer of amicable resolution under FJ(G)R P 4 r 1 and costs; the judge-led approach and case conferences under P 8).

### 1.II Before filing: programmes, jurisdiction and procedure

Sub-points 1.II.1–1.II.5. Tested: 1.II.1 (2023, 2025, SQ), 1.II.2 (2021, 2023, 2025, SQ), 1.II.5 (2021, 2022). Own questions F2 (1.II.3) and F3 (1.II.4).

### 1.II.1 — Mandatory Co-Parenting Programme

**PYP 2023 Family Q3 facts.** Peter and Mary have been married for about 4 years and have one child, Paul, aged 8 months. Peter is a Singapore citizen; Mary remains a Malaysian citizen. Peter says the marriage has broken down and wants to commence divorce proceedings in Singapore; Mary is likely to contest.

**Q2023-3-2** · `1.II.1` · PYP 2023 Q3.2 · 2 marks · `pcp-w-1-4`

Discuss with Peter the requirement and purpose of his attending a Parenting Programme.

**Answer.**

Because Paul is below 21, Peter must complete the Mandatory Co-Parenting Programme before he can file for divorce. Every parent with a child below 21 must complete an approved parenting programme within the prescribed time (s 94A(1) WC), and no divorce application or cross-application may be filed by such a parent unless he has completed it, is an excluded party, or has the court's permission (s 94A(3)). The certificates of completion are filed with the divorce papers. Mary too must complete it before she can file any cross-application. If a party has not completed it the court may stay the proceedings until he does and order costs against him (s 94A(7)(b)), and it may order the parties to attend at any time (s 94A(5)). Anything said in the programme is inadmissible (s 94A(8)). Its purpose is to help parents understand the impact of divorce on their children and to plan co-parenting arrangements before proceedings begin; it is distinct from the mediation and counselling the court must order after filing under s 139I (Pre-write 1-4). Therefore Peter should complete the programme now and file his certificate with his divorce application.

**QSQ-3-1** · `1.II.1` `1.II.2` `1.IV.1` · SQ Fam Q3.1; official guide SQ p126 · not mark-weighted · `pcp-w-1-4` `pcp-w-1-5` `pcp-w-1-10`

Celeste and Colin, both Malaysian citizens, married in Kuala Lumpur in January 2020 and have been married about 3½ years; they have a daughter of about 9 months. They moved to Singapore for work in June 2020 and neither has returned to Malaysia since. Since June 2022, after quarrels, Celeste has slept in a separate bedroom with their daughter. She has evidence of Colin's adultery in a surveillance report obtained 4 weeks ago. Discuss whether the Family Justice Courts have jurisdiction over her intended divorce and, if so, what programmes she must attend before commencing proceedings.

**Answer.**

The issue is whether the Singapore court can hear Celeste's divorce and what she must do before filing. It can, on the basis of three years' habitual residence; the three-year bar has passed; and she must complete the Mandatory Co-Parenting Programme.

*Jurisdiction.* The court has jurisdiction in divorce only if either party is domiciled in Singapore at the commencement of proceedings, or habitually resident in Singapore for the three years immediately preceding commencement (s 93(1) WC). Neither is a Singapore citizen, so there is no deemed domicile under s 3(5). Habitual residence means residence that is normal apart from temporary absences, voluntarily adopted with a settled purpose, such as employment (*Lee Mei-Chih v Chang Kuo Yuan* [2012] SGHC 180). Both have lived and worked here since June 2020 without leaving, so by mid-2023 each has been habitually resident here for three years; either may therefore commence proceedings (Pre-write 1-5).

*Three-year bar.* No divorce application may be filed until three years have passed since the date of marriage (s 94(1) WC). They married in January 2020 and have been married about 3½ years, so the bar no longer applies (Pre-write 1-10).

*Programmes.* All parents with a child below 21 must complete the Mandatory Co-Parenting Programme, a one-to-one consultation for parents of minor children, before filing for divorce (s 94A WC); the certificate of completion is filed with the divorce papers, including any counterclaim, so Colin must complete it too before he can file one. The programme applies to divorces filed since 1 December 2016. It is distinct from the mediation and counselling the court must order after filing under s 139I (SQ guide p126) (Pre-write 1-4).

Therefore the court has jurisdiction under s 93(1)(b) WC on habitual residence, the three-year bar has passed, and Celeste must complete the Co-Parenting Programme before filing.

### 1.II.2 — Jurisdiction: domicile or three years' habitual residence

**Q2023-3-1** · `1.II.2` `1.IV.1` · PYP 2023 Q3.1 · 3 marks · `pcp-w-1-5` `pcp-w-1-10`

*Facts: PYP 2023 Family Q3, under 1.II.1 above.* Discuss and explain to Peter whether the Family Justice Courts have jurisdiction to deal with his intended divorce.

**Answer.**

The court has jurisdiction in divorce if either party is domiciled in Singapore at the commencement of proceedings, or habitually resident here for the three years immediately before (s 93(1) WC). A Singapore citizen is deemed domiciled in Singapore until the contrary is proved (s 3(5)). Peter is a Singapore citizen, so he is deemed domiciled here, and nothing suggests he has acquired a domicile elsewhere; the court therefore has jurisdiction under s 93(1)(a), whatever Mary's nationality (Pre-write 1-5). They have been married about 4 years, so the three-year bar on filing (s 94(1)) does not apply (Pre-write 1-10). Mary's intention to contest does not affect jurisdiction; it affects only the track the case takes (Pre-write 1-6). Therefore the Family Justice Courts have jurisdiction over Peter's divorce.

**PYP 2025 Family Q3 facts.** Bao Ho and his wife Linh Pham married in Vietnam about 10 years ago and have two children aged 7 and 9. All four are Vietnamese citizens. Linh was seconded to Singapore and the family moved here 5 years ago; both work here on Employment Passes. About 10 months ago Bao Ho discovered that Linh was having an affair with a male colleague; he has affectionate text messages and photographs of them holding hands and kissing. After a confrontation they had counselling and therapy, but he later learned the affair had continued despite her promise to end it. He wants to divorce citing adultery, believing it will give him an advantage on custody and a larger share of the matrimonial assets.

**Q2025-3-1** · `1.II.2` `1.II.1` · PYP 2025 Q3.1 · 2 marks · `pcp-w-1-5` `pcp-w-1-4`

Explain to Bao Ho whether the Family Justice Courts have jurisdiction over his intended divorce and, if so, what programmes he must attend before commencing proceedings.

**Answer.**

The court has jurisdiction in divorce if either party is domiciled in Singapore, or habitually resident here for the three years immediately before commencement (s 93(1) WC). Neither is a citizen, so there is no deemed domicile (s 3(5)). But both have lived and worked here for 5 years on Employment Passes: residence voluntarily adopted with a settled purpose (employment, the children's schooling), which is habitual residence unless long absences break the three years (*Lee Mei-Chih v Chang Kuo Yuan* [2012] SGHC 180, where 12 months' total absence did). I would check his travel; on the facts the court has jurisdiction under s 93(1)(b) (Pre-write 1-5). Because the children (7 and 9) are below 21, Bao Ho must complete the Mandatory Co-Parenting Programme before filing and file his certificate with the application; Linh must do so before any cross-application (s 94A WC) (Pre-write 1-4).

### 1.II.3 — Divorce procedure under the FJ(G)R 2024

**Own question F2 facts.** Tina has been served with her husband Victor's originating application for divorce, which relies on her alleged unreasonable behaviour and claims sole care and control of their daughter and division of the matrimonial flat. Tina denies the allegations and does not want a divorce on that basis; she also wants to claim maintenance for herself. She asks what happens next.

**Q1-F2-1** · `1.II.3` `1.I.2` · own question · 8 marks · `pcp-w-1-6` `pcp-w-1-2`

Advise Tina on the procedure and timelines from here to the resolution of the ancillary matters.

**Answer.**

The issue is how Tina responds and how the case proceeds under the Family Justice (General) Rules 2024, which apply to proceedings begun on or after 15 October 2024 and use "Applicant/Respondent" and "originating application" in place of "Plaintiff/Defendant" and "writ". Divorce runs in two stages: dissolution, then ancillary matters (custody, care and control, access, maintenance, division and costs).

*Responding.* Victor's application is in Form 2, stating the s 95A fact, brief particulars and his claims for ancillary relief (P 2 r 2). To contest, Tina must file a notice to contest in Form 4 within 14 days (P 2 r 4); by it she may object to the divorce or to the ancillary relief, make her own ancillary claims (such as maintenance for herself), file a cross-application or challenge jurisdiction. If she objects to the divorce itself, she must file a Reply (and any cross-application) within 28 days with brief particulars of her objections (P 2 r 5). If she cross-applies for divorce on her own fact, she must first have completed the Co-Parenting Programme (s 94A WC).

*Contested track.* The parties exchange affidavits of evidence-in-chief setting out all material facts and evidence; objections to an AEIC are made in Form 101 within 14 days (P 15 r 16). A request for trial is made in Form 6 (P 2 r 7), and the trial follows (order of trial, P 15 r 13). Throughout, the case is judge-led through case conferences (P 8), and because there is a child below 21 the court must order mediation and/or counselling (s 139I WC) (Pre-write 1-2). Many contested cases are resolved there: the parties may agree a different fact (such as mutual agreement) and proceed on the uncontested track.

*Ancillary matters.* After Interim Judgment, each party files a First Ancillary Affidavit in Form 15 within 28 days (P 2 r 16), with supporting documents; disclosure is sought under Part 9 by summons in Form 84, answered by an objection or a compliance affidavit; a Second Ancillary Affidavit follows (P 2 r 16(3)); then binding summaries in Form 17 (P 2 r 18), the hearing and orders. If ancillary matters are agreed, a draft order is filed by consent.

Therefore Tina should file her Form 4 notice to contest within 14 days, and a Reply within 28 days if she opposes the divorce itself, including her maintenance claim; she should then engage in the mediation the court will order, and prepare her Form 15 ancillary affidavit for filing within 28 days of any Interim Judgment (Pre-write 1-6).

### 1.II.4 — Relief without divorce

**Own question F3 facts.** Una married Wes 18 months ago; they have a son aged 1. Wes has stopped giving her any money, says he will "take the boy" to his parents' home, and has told her he is going to sell the condominium unit they bought together. Una does not want to wait. She asks whether she can divorce now and, if not, what she can do.

**Q1-F3-1** · `1.II.4` `1.IV.1` · own question · 8 marks · `pcp-w-1-7` `pcp-w-1-10` `pcp-w-1-25`

Advise Una.

**Answer.**

The issue is whether Una can divorce within three years of marriage and, if not, what relief she can obtain now. She is unlikely to be able to file for divorce yet, but she can obtain orders for her son, maintenance for herself and the child, and relief on the property without divorcing, and may seek judicial separation.

*The three-year bar.* No divorce application may be filed until three years have passed since the marriage (s 94(1) WC), unless the court gives permission on the ground of exceptional hardship suffered by the applicant or exceptional depravity on the part of the respondent (s 94(2)); the court considers the interests of any child and the chance of reconciliation (s 94(3)). Exceptional hardship is "something quite out of the ordinary and more than what an ordinary person should reasonably be asked to bear" (*Ng Kee Shee v Fu Gaofei* [2005] 4 SLR 762 at [23]); the purpose of the bar is to promote the sanctity of marriage (at [21]). Wes's withholding of money and threats are serious but are not, on their own, exceptional hardship or depravity (contrast the serial, filmed infidelity in *Tan Chew Kwee Jenn v Tan Chee Kiong John* [2006] SGDC 221). She will probably have to wait until 3 years from the marriage (Pre-write 1-10).

*Relief without divorce.* (1) *The child:* where there are no divorce proceedings (including where the parents are barred by s 94), custody, care and control and access may be decided under ss 3 and 5 of the Guardianship of Infants Act 1934, with the child's welfare the first and paramount consideration and neither parent having a superior right (s 3 GIA). Una can apply for care and control now, which answers the threat to "take the boy". (2) *Maintenance:* a wife may claim maintenance during the marriage on proof that the husband has neglected or refused to provide reasonable maintenance (s 69 WC), and both parents must maintain the child (ss 68–69). (3) *Property:* a dispute between spouses over property during the marriage may be brought to the court under s 59 WC, where general property law applies; she can use it if Wes tries to deal with the jointly owned unit. (4) *Protection:* if there is family violence, a protection order is available independently of divorce (Part 7 WC). (5) *Judicial separation:* either party may apply on the s 95A facts (s 101 WC); it releases her from the duty to cohabit and allows the court to make ancillary orders, and does not bar a later divorce (s 102) (Pre-write 1-7).

Therefore Una should apply under the GIA for care and control of her son, under s 69 WC for maintenance, and under s 59 WC if Wes tries to deal with the unit (or consider judicial separation), and file for divorce once three years have passed unless she can show exceptional hardship or depravity.

### 1.II.5 — Drafting the divorce application: brief particulars / Statement of Particulars

**Q2022F-2** · `1.II.5` `1.IV.3` · PYP 2022 FAM Q2 · not mark-weighted · `pcp-w-1-42` `pcp-w-1-12`

*Facts: PYP 2022 Family, under 1.I.2 above.* Draft the Statement of Particulars for Cherry. [Focus on content; formatting and professionalism will be considered but are not paramount.]

**Answer.**

*(Under the FJ(G)R 2024 the "Statement of Particulars" is the brief particulars in the originating application for divorce, Form 2. Cherry can rely on adultery: she learnt of the 2022 adultery in early 2022 and Daniel left on 18 March 2022, so they have not lived together for more than 6 months since she knew (s 95A(2)) (Pre-write 1-12). The 2006 affair cannot be relied on: she forgave him and they lived together for years after she knew. Template 1-42.)*

IN THE FAMILY JUSTICE COURTS OF THE REPUBLIC OF SINGAPORE — Originating Application for Divorce No. [ ] — Between [Cherry] (Applicant) and [Daniel] (Respondent)

**BRIEF PARTICULARS (STATEMENT OF PARTICULARS)**

1. The marriage has broken down irretrievably. The Applicant relies on the fact that the Respondent has committed adultery and the Applicant finds it intolerable to live with the Respondent (s 95A(1)(a) Women's Charter 1961).

2. *Particulars of adultery.*
   (a) From a date unknown to the Applicant, but at least from early 2022, the Respondent has had an intimate relationship with a woman working as a hostess at a KTV lounge, whose name is unknown to the Applicant.
   (b) On a number of nights in early 2022, the dates of which are set out in the surveillance report of [name of firm] dated [ ], the Respondent met the said woman at the said KTV lounge, checked into [name of hotel], a hotel near the lounge, with her, and stayed with her in a room there before taking her back to the lounge. The Respondent thereby had sexual intercourse with the said woman on those occasions.
   (c) The Applicant learnt of the matters in (a) and (b) from the said surveillance report in [month] 2022 and confronted the Respondent on 18 March 2022. The Respondent left the matrimonial home that night and the parties have not lived together since.

3. *Intolerability.* The Applicant finds it intolerable to live with the Respondent. The Respondent had previously been unfaithful, which the Applicant forgave after marital counselling, and the Respondent's further adultery has destroyed the Applicant's trust in him.

4. *Children and ancillary relief.* There are three children of the marriage: Carissa and Calista, born 6 August 2010, and Raymond, born [ ] 2006, who has been a member of the family since birth (s 92 WC). The Applicant claims joint custody of the children, care and control of the children to the Applicant with access to the Respondent, maintenance for the children and for herself, division of the matrimonial assets, and costs.

*Notes for the exam.* If the adultery is denied and the evidence of intercourse is thin, plead in the alternative the Respondent's unreasonable behaviour (s 95A(1)(b)): his unexplained absences until the early hours since retirement, his improper association with the hostess and his frequenting of KTV lounges and massage parlours, and his cutting off all financial support since March 2022 (Pre-write 1-13). Keep the language factual (no "philanderer"), give dates, and leave out the chair incident and the children's dispute, which belong to other proceedings and to the ancillary affidavit (Template 1-42).

**Q2021F-2** · `1.II.5` `1.IV.4` · PYP 2021 FAM Q2 · not mark-weighted · `pcp-w-1-42` `pcp-w-1-13`

*Facts: PYP 2021 Family, under 1.I.2 above.* Draft the Statement of Particulars for Christine. [Focus on content; formatting and professionalism will be considered but are not paramount.]

**Answer.**

*(Christine relies on unreasonable behaviour (s 95A(1)(b)); there is no evidence of adultery, no 2-year desertion and no long separation. She left on 29 June 2021 after the last incident and has not lived with Ken since, so s 95A(3) is no obstacle (Pre-write 1-13). Template 1-42.)*

IN THE FAMILY JUSTICE COURTS OF THE REPUBLIC OF SINGAPORE — Originating Application for Divorce No. [ ] — Between [Christine] (Applicant) and [Ken] (Respondent)

**BRIEF PARTICULARS (STATEMENT OF PARTICULARS)**

1. The marriage has broken down irretrievably. The Applicant relies on the fact that the Respondent has behaved in such a way that the Applicant cannot reasonably be expected to live with the Respondent (s 95A(1)(b) Women's Charter 1961).

2. *Particulars of behaviour.*
   (a) *Physical violence, January 2021.* In or about January 2021, at [address], Bukit Timah Road, the Respondent slapped, punched and kicked the Applicant. The Applicant was hospitalised for her injuries. The police were informed.
   (b) *Physical violence, 29 June 2021.* On the night of 29 June 2021, at the matrimonial home at Grange Road, the Respondent, while under the influence of alcohol, physically assaulted the Applicant, who fled the home that night.
   (c) *Financial irresponsibility and gambling.* From about mid-2020 the Respondent traded compulsively in shares, which he himself described as "gambling", sustained heavy losses, borrowed from friends to continue trading, and without the Applicant's knowledge or consent withdrew more than S$1 million from the parties' joint account.
   (d) *Verbal abuse.* When he lost money, the Respondent lost his temper and blamed the Applicant, accusing her of being wealthy and causing him stress; when confronted about the withdrawals he shouted at her and called her calculative.
   (e) *Neglect and drinking.* From mid-2020 the Respondent spent his nights trading, neglecting the Applicant; from about April 2021 he regularly returned home in the morning, drunk and smelling of alcohol and cigarette smoke.
   (f) *Exclusion from the children.* After January 2021 the Respondent prevented the Applicant from caring for the children, having them looked after by his parents at night; since 29 June 2021 he has refused the Applicant all contact with the child Charlotte, in person or by video call.

3. As a result the Applicant cannot reasonably be expected to live with the Respondent. The Applicant left the matrimonial home on 29 June 2021 and has not lived with the Respondent since.

4. *Children and ancillary relief.* There are two children of the marriage, Marcus and Charlotte, born 13 February 2017. The Applicant claims custody, care and control of both children with access to the Respondent, maintenance for the children, division of the matrimonial assets, and costs [and maintenance for herself, if instructed].

*Notes for the exam.* Number each incident with its date and effect; avoid labels ("abuser", "addict") in favour of facts; do not plead the Applicant's own conduct (taking the children in January 2021); and keep the detail of assets and the children's arrangements for the ancillary affidavit (Template 1-42).

### 1.III Nullity

Sub-points 1.III.1–1.III.3. None tested. Own question F4 covers all three; F14 (added 18 Nov) is a 7-mark question in the format of the short past-paper Q3 (marriage of convenience; wilful refusal and the s 107(1) bar; the three-year bar).

### 1.III.1 — Void and voidable marriages; void marriages

**Own question F4 facts.** Three clients ask about nullity. (a) Anna, a Singapore citizen, married Ben in Singapore in 2024; she has just learnt that Ben's earlier marriage in his home country was never dissolved. (b) Chen, a Singapore citizen, married Dora in Singapore in 2025; they agreed not to have sexual relations until a Chinese tea ceremony was held, but Dora has since refused to hold the ceremony and the marriage has never been consummated. (c) Eli married Fay in Singapore in 2021 because his family threatened to disown him and stop supporting his ailing mother unless he did; he wants an annulment now.

**Q1-F4-1** · `1.III.1` `1.III.2` `1.III.3` `1.II.2` · own question · 10 marks · `pcp-w-1-8` `pcp-w-1-9` `pcp-w-1-5`

Advise each client whether the marriage is void, voidable or valid, and whether a judgment of nullity can be obtained.

**Answer.**

The issue for each client is whether the marriage is void (void from the beginning) or voidable (valid until annulled), and whether any bar applies. Anna's marriage is void; Chen's is voidable for wilful refusal to consummate; Eli's claim of lack of consent is time-barred.

*Void and voidable.* A marriage is void if invalid under s 3(4) (both parties Muslim), ss 5 and 11 (a subsisting prior marriage), s 9 (a party under 18 without a special licence), s 10 (prohibited degrees), s 11A (marriage of convenience), s 12 (same sex) or s 13 (no valid licence or unauthorised solemniser) (s 105 WC). A void marriage is void whether or not a judgment is obtained, though either party may seek a judgment of nullity for certainty (s 104). A voidable marriage is valid until annulled, and a judgment annuls it only from when it is made final (s 110(2)); only the parties may seek it (*Tan Ah Thee v Lim Soo Foong* [2009] 3 SLR(R) 957). For nullity, the court also has jurisdiction if both parties reside in Singapore at commencement (s 93(2)) (Pre-writes 1-5, 1-8).

*(a) Anna.* Ben was still married when he married her, so the marriage is invalid under ss 5 and 11 and void under s 105. It never existed in law, but Anna should seek a judgment of nullity (s 104) for certainty; jurisdiction lies on her domicile as a citizen (s 93(1)(a), s 3(5)).

*(b) Chen.* A marriage is voidable only on the grounds in s 106 WC, including non-consummation owing to the respondent's wilful refusal (s 106(b)). Refusing to undergo an agreed pre-condition to consummation, such as Chinese customary rites, can amount to wilful refusal (*Kwong Sin Hwa v Lau Lee Yen* [1993] 1 SLR(R) 90). Dora's refusal to hold the tea ceremony that both agreed must come first is wilful refusal, so the marriage is voidable. Under s 107(1) relief is barred if the respondent shows that the applicant, knowing he could avoid the marriage, led her reasonably to believe he would not, and that a judgment would be unjust to her; nothing suggests that. The 3-year limit in s 107(2) applies only to grounds (c)–(f), not (b). Chen must be candid: non-consummation is easily alleged, and a judgment obtained by deceiving the court can be rescinded (*Heng Joo See v Ho Pol Ling* [1993] 2 SLR(R) 763).

*(c) Eli.* Lack of valid consent through duress is a ground (s 106(c)), but for grounds (c)–(f) proceedings must be instituted within 3 years of the marriage (s 107(2)). Eli married in 2021, so the 3 years have passed and the claim is barred, whatever the merits of the duress. An improper motive for marrying is not itself a ground (*Tan Ah Thee*). His remedy is divorce on a s 95A fact (Pre-write 1-9).

Therefore Anna's marriage is void and she should obtain a judgment of nullity; Chen may apply to annul his voidable marriage for wilful refusal; and Eli is out of time for nullity and should consider divorce.

**Own question F14 facts** (past-paper style, set in the format of the short Family Q3 of PYP 2023 and 2025; not from a past paper). Priya, a Singapore citizen, met Kenji, a foreign national on a short-term pass, through a dating agency, and they married at the Registry of Marriages in Singapore in January 2025. Kenji has refused all sexual relations since the wedding, saying he is "not ready". In February 2026 Priya overheard Kenji telling a friend that the agency had paid him S$8,000 to marry a Singaporean so that he could get a long-term visit pass, and that he "never meant it to be a real marriage". Priya had believed the marriage was genuine. She confronted him; he begged her to stay married until his pass was renewed, and she agreed, telling him in writing in March 2026 that she would "not do anything about the marriage" for now. Relying on that, Kenji turned down a job offer in his home country. Priya now wants to end the marriage as quickly as possible.

**Q1-F14-1** · `1.III.1` `1.III.2` `1.III.3` `1.IV.1` · own question, past-paper style (not from a past paper) · 3 marks · `pcp-w-1-8` `pcp-w-1-9` `pcp-w-1-10`

(a) Advise Priya whether her marriage is void. (3 marks)

**Answer.**

The issue is whether the marriage is void as a marriage of convenience. It is likely void under s 11A WC, so Priya does not need to wait for the three-year bar to pass; she should seek a judgment of nullity for certainty.

A marriage solemnised on or after 1 October 2016 is void if (a) a party enters it knowing or having reason to believe that its purpose is to assist a party to obtain an immigration advantage, and (b) any gratification is offered, given or received as an inducement or reward to a party for entering it (s 11A(1) WC); it is not void if both parties believed on reasonable grounds, when they married, that it would result in a genuine marital relationship (s 11A(2)). A marriage void under s 11A is void under s 105, whether or not a judgment is obtained, though either party may seek a judgment of nullity (s 104). An improper motive alone does not make a marriage void (*Tan Ah Thee v Lim Soo Foong* [2009] 3 SLR(R) 957); s 11A is the statutory exception (Pre-write 1-8).

The marriage was solemnised in January 2025. Kenji entered it knowing that its purpose was to obtain a long-term visit pass (an immigration advantage), and he received S$8,000 from the agency as a reward for marrying (gratification). The s 11A(2) exception needs *both* parties to have believed it would be genuine; Priya did, but Kenji admits he never meant it to be a real marriage, so the exception fails. Priya must prove the facts: she should record what she overheard and look for evidence of the payment (bank records, messages with the agency); if Kenji is convicted under s 57C(1) Immigration Act, the marriage is deemed void (s 11A(3)). Because a judgment of nullity is not a divorce, the three-year bar in s 94 does not apply (Pre-write 1-10). She should apply for a judgment of nullity under s 104; the court has jurisdiction on her domicile as a citizen (s 93(1)(a), s 3(5)) (Pre-write 1-5).

Therefore the marriage is likely void under s 11A read with s 105, and Priya should seek a judgment of nullity now.

**Q1-F14-2** · `1.III.2` `1.III.3` `1.IV.1` · own question, past-paper style (not from a past paper) · 4 marks · `pcp-w-1-9` `pcp-w-1-10`

(b) Assume Priya cannot prove the payment. Advise her whether she can have the marriage annulled on the ground of non-consummation, and what she can do if she cannot. (4 marks)

**Answer.**

The issue is whether the marriage is voidable for wilful refusal to consummate and whether a bar applies. It is voidable under s 106(b) WC, but Priya's written promise and Kenji's reliance on it may bar relief under s 107(1); if so, she cannot divorce until January 2028 unless she shows exceptional hardship or exceptional depravity.

*Ground.* A marriage is voidable if it has not been consummated owing to the respondent's wilful refusal (s 106(b) WC) (Pre-write 1-9). Kenji's refusal of all sexual relations for over a year, without any medical reason, is wilful refusal. Priya must be candid: non-consummation is easily alleged, and a judgment obtained by deceiving the court can be rescinded (*Heng Joo See v Ho Pol Ling* [1993] 2 SLR(R) 763).

*Bars.* The 3-year limit (s 107(2)) and the ignorance requirement (s 107(3)) do not apply to ground (b). But the court must not grant a judgment if the respondent satisfies it that (a) the applicant, knowing it was open to her to avoid the marriage, so conducted herself towards the respondent as to lead him reasonably to believe that she would not seek to do so, and (b) it would be unjust to the respondent to grant the judgment (s 107(1)). Priya knew of the refusal and the sham in March 2026 and told Kenji in writing that she would "not do anything about the marriage"; he relied on it by turning down a job. That satisfies limb (a). On limb (b), Priya can argue that it is not unjust to annul a marriage Kenji entered for money and an immigration advantage, and that her promise was "for now" and made under his pleading, so his reliance was unreasonable; the outcome is uncertain, and the burden is on Kenji.

*If nullity fails.* Divorce cannot be filed until three years from the marriage (January 2028) unless she shows exceptional hardship suffered by her or exceptional depravity on his part (s 94 WC) (Pre-write 1-10). Exceptional hardship is "something quite out of the ordinary" (*Ng Kee Shee v Fu Gaofei* [2005] 4 SLR 762 at [23]); in *Ng Kee Shee* a wife who entered an arranged marriage capriciously, with "absolutely no regard for the union", was held to justify early filing, since making the husband wait would visit her wrongs on him ([21]), which supports Priya. When she files, the fact will be unreasonable behaviour (s 95A(1)(b)) (Pre-write 1-13).

Therefore Priya should apply for nullity under s 106(b), expecting Kenji to raise the s 107(1) bar; in the alternative, she should seek permission to file for divorce within three years on the ground of exceptional hardship, relying on *Ng Kee Shee*.

### 1.III.2 — Voidable marriages

See Q1-F4-1 under 1.III.1 (part (b): wilful refusal to consummate, *Kwong Sin Hwa*; part (c): duress).

### 1.III.3 — Bars to relief for voidable marriages (s 107 WC)

See Q1-F4-1 under 1.III.1 (s 107(1) conduct bar; s 107(2) 3-year limit).

### 1.IV Divorce

Sub-points 1.IV.1–1.IV.7. Tested: 1.IV.1 (SQ), 1.IV.3 and 1.IV.4 (2021, 2022, 2023, 2025, SQ), 1.IV.6 (2023, 2025), 1.IV.7 (2025, SQ). Own question F5 covers 1.IV.2 and 1.IV.5.

### 1.IV.1 — Three-year bar and its exceptions

See QSQ-3-1 under 1.II.1 and Q2023-3-1 under 1.II.2 (bar passed), and Q1-F3-1 under 1.II.4 (exceptional hardship or depravity; alternatives within the 3 years).

### 1.IV.2 — Sole ground: irretrievable breakdown; just and reasonable

**Own question F5 facts.** Gina married Hal in 2010. In March 2023 Hal moved to Johor Bahru to live alone, telling Gina the marriage "is finished". She did not agree to his leaving; he had no job reason to go, and he has not returned or contacted her since, apart from a two-month stay in the flat in late 2023 when he was ill. Gina wants a divorce. Hal now says he still loves her, wants counselling, and will oppose the divorce because he would be left without the flat.

**Q1-F5-1** · `1.IV.2` `1.IV.5` · own question · 8 marks · `pcp-w-1-11` `pcp-w-1-14`

Advise Gina whether she can obtain a divorce.

**Answer.**

The issue is whether Gina can prove that the marriage has irretrievably broken down, on which fact, and whether Hal's wish to reconcile prevents a divorce. She can rely on desertion for at least two years, and Hal's one-sided wish to reconcile and his professions of love will not stop the divorce.

*The sole ground.* The sole ground for divorce is irretrievable breakdown (s 95 WC), proved by one of six facts in s 95A(1); the applicant may not rely on her own adultery, behaviour or desertion, and the court must be satisfied that it is just and reasonable to grant the divorce (s 95(2)). That proviso applies only in the most extreme cases where it would still be wrong to dissolve the marriage, considering the parties' conduct and the interests of any children; financial hardship alone is not enough unless grave, and a unilateral desire for reconciliation is meaningless without reciprocity (*William Cheng v Chai Mei Leng* [1999] SGCA 26). Once the fact is proved, professions of love and care do not rebut the breakdown (*Cheong Kim Seah v Lim Poh Choo* [1992] SGHC 231) (Pre-write 1-11).

*Desertion.* Desertion implies abandonment against the wish of the deserted spouse (s 92 WC). The applicant must show that the respondent deserted her for a continuous period of at least two years immediately before filing: physical separation, without her consent, with an intention to bring the marital union to an end (which may be inferred from conduct), by a spouse with capacity to form it, and without reasonable cause such as an overseas job (s 95A(1)(c); FL3 s20). Hal left in March 2023 against Gina's wishes, saying the marriage was finished, with no job reason, and has not returned. Desertion remains continuous even if the parties lived together for a total of 6 months or less during the period, but that time does not count towards the two years (s 95A(4)). His two-month stay in late 2023 therefore does not break the continuity, but it is added to the two years: by about May 2025 the desertion period was complete (Pre-write 1-14).

*Hal's opposition.* His wish for counselling is unilateral, and his assurances of love do not rebut breakdown (*William Cheng*; *Cheong Kim Seah*). His concern about the flat is a matter for the division of assets, not a reason to refuse a divorce; it is not the grave financial hardship that might engage the "just and reasonable" proviso. The court will consider reconciliation (s 139F WC) and, if there are children under 21, order mediation or counselling (s 139I), but cannot refuse a divorce because one party will not accept it.

Therefore Gina can file now on the fact of desertion for more than two years, and the court is likely to find irretrievable breakdown and grant the divorce despite Hal's opposition.

### 1.IV.3 — Adultery and the 6-month rule

**Q2025-3-2** · `1.IV.3` `1.IV.4` `1.IV.6` `1.IV.7` · PYP 2025 Q3.2 · 3 marks · `pcp-w-1-12` `pcp-w-1-13` `pcp-w-1-15` `pcp-w-1-16`

*Facts: PYP 2025 Family Q3, under 1.II.2 above.* Advise Bao Ho whether he can commence divorce proceedings on the fact of adultery and the likelihood of success; if not, whether there are alternative facts he can establish.

**Answer.**

The issue is whether Bao Ho can rely on Linh's adultery, and whether it will help him on the ancillary matters. He may rely on adultery if he can prove intercourse and finds it intolerable to live with her, but his evidence may not prove intercourse if she denies it, and it will not help him on custody or division; behaviour or mutual agreement are safer.

To establish adultery he must prove that Linh committed adultery (consensual sexual intercourse: *Tan Meng Hock v Tay Mui Keow* [1992] SGHC 218) and that he finds it intolerable to live with her (s 95A(1)(a) WC). Living together for up to 6 months in total after learning of the adultery is disregarded; if they lived together for more than 6 months after he knew of an act, he cannot rely on that act, but he can rely on later acts (s 95A(2)). He learnt of the affair 10 months ago and they stayed together for counselling, so he cannot rely on the adultery known then; he may rely on the continued affair he learnt of later, if within 6 months of cohabitation. Texts, hand-holding and kissing show inclination but not intercourse; if Linh admits it, the admission suffices, but if she contests he will need more, such as a private investigator's evidence of opportunity (FL3 s16–17) (Pre-write 1-12).

*Alternatives.* Her continued improper association after promising to end it is unreasonable behaviour (s 95A(1)(b); *Wong Siew Boey v Lee Boon Fatt* [1994] SGHC 35) (Pre-write 1-13); if Linh accepts the marriage is over, divorce by mutual agreement (s 95A(1)(f)) avoids a contested hearing (Pre-write 1-16). Separation (s 95A(1)(d)–(e)) is not available as they still live together (Pre-write 1-15).

*His misconception.* The fact relied on generally does not affect the ancillary matters: custody and care and control turn on the children's welfare, and division on contributions, with conduct relevant only if gross (Pre-writes 1-17, 1-33). Therefore Bao Ho can try adultery based on the later acts if Linh admits it, but behaviour or mutual agreement is the safer course, and neither will give him an advantage on custody or assets.

**Q2022F-1a** · `1.IV.3` `1.IV.4` `1.II.2` · PYP 2022 FAM Q1 (divorce) · not mark-weighted · `pcp-w-1-12` `pcp-w-1-13` `pcp-w-1-5`

*Facts: PYP 2022 Family, under 1.I.2 above.* Advise Cherry on her intended divorce proceedings.

**Answer.**

The issue is whether Cherry can divorce Daniel in Singapore and on which fact. She can: both are citizens, so the court has jurisdiction; the marriage is 20 years old; and she can rely on Daniel's adultery with the lounge hostess in 2022, or in the alternative his unreasonable behaviour.

*Jurisdiction and timing.* Both are Singapore citizens and so deemed domiciled here (s 3(5) WC); the court has jurisdiction under s 93(1)(a). They married in 2002, so the three-year bar (s 94) is long past (Pre-write 1-5).

*Adultery.* She must prove that Daniel committed adultery and that she finds it intolerable to live with him (s 95A(1)(a)). The 2006 affair cannot be relied on: she knew of it and they lived together for many years after (s 95A(2)(b)). The 2022 relationship can: the private investigator's report shows Daniel frequenting the lounge, forming a relationship with the hostess and checking into a hotel with her at night, which is evidence of inclination and opportunity from which intercourse may be inferred if contested (FL3 s16–17). She confronted him on 18 March 2022 and he left that night, so they have not lived together for more than 6 months since she knew (s 95A(2)). The hostess should be identified if her name is known (Pre-write 1-12).

*Unreasonable behaviour (alternative).* Daniel's unexplained absences until the early hours, the KTV lounges and massage parlours, his improper association with the hostess, and his cutting off all financial support since March 2022 together amount to behaviour such that Cherry cannot reasonably be expected to live with him, judged by the parties' personalities and the cumulative effect (s 95A(1)(b); *Wong Siew Boey v Lee Boon Fatt* [1994] SGHC 35) (Pre-write 1-13).

*General assessment.* Her chair-throwing on 18 March 2022 is relevant to Daniel's PPO application (Q2022F-1g) but does not prevent her divorce: she does not rely on her own conduct, and the fact relied on does not generally affect custody or division (Pre-write 1-12). Desertion is not available (Daniel left in March 2022, less than 2 years ago), and separation has not run long enough.

Therefore Cherry can file in Singapore on the fact of adultery (with behaviour as the fallback), after completing the Co-Parenting Programme (the twins are 12 and Raymond 16) (Pre-write 1-4); see the Statement of Particulars at Q2022F-2.

### 1.IV.4 — Unreasonable behaviour

**PYP 2023 Family Q4 facts.** Jenny and John, both Singapore citizens, have been married about 5 years with 2 young children. About 8 months ago Jenny discovered John's affair; she has a private investigator's surveillance report showing him checking into a hotel with a female colleague. She tried to forgive him and reconcile for the children's sake but could not. Quarrels followed; she kept accusing him of infidelity despite his assurance that he had cut off all ties. In frustration John threw a vase against a wall; a glass shard ricocheted and struck Jenny's face, leaving a 5cm permanent scar. John was extremely remorseful, saying it was an accident and he never meant to hurt her. Jenny wants to divorce on the fact of adultery.

**Q2023-4-1** · `1.IV.4` `1.IV.3` `1.IV.6` `1.IV.7` · PYP 2023 Q4.1 · 6 marks · `pcp-w-1-13` `pcp-w-1-12` `pcp-w-1-15` `pcp-w-1-16`

Advise Jenny whether this is possible and what other facts she can establish for the court to grant a judgment dissolving the marriage.

**Answer.**

The issue is whether Jenny can rely on adultery and, if not, what fact she should use. She probably cannot rely on adultery, because she has lived with John for about 8 months since she found out; she should rely on unreasonable behaviour, or on mutual agreement if John agrees.

*Adultery.* Jenny must prove John's adultery and that she finds it intolerable to live with him (s 95A(1)(a) WC). The PI report showing him checking into a hotel with a colleague is evidence of inclination and opportunity (FL3 s16–17). But if the parties lived together for more than 6 months after she knew of the adultery, she cannot rely on it, though she could rely on later acts (s 95A(2)(b)). She discovered it about 8 months ago and has lived with him since, trying to reconcile, so she cannot rely on that adultery, and John says the affair has ended (Pre-write 1-12).

*Unreasonable behaviour.* She must show that John has behaved in such a way that she cannot reasonably be expected to live with him (s 95A(1)(b)). Whether she finds it intolerable is subjective; whether she can reasonably be expected to live with him is objective but takes account of the parties' personalities and the cumulative effect of the conduct, active or passive (*Wong Siew Boey v Lee Boon Fatt* [1994] SGHC 35). The affair and improper association with his colleague, the quarrels and, above all, throwing a vase in anger so that she was permanently scarred, taken cumulatively, are capable of meeting the test even if he did not intend to injure her. Living together for up to 6 months after the last incident is disregarded (s 95A(3)), so she should file promptly or move out (Pre-write 1-13). John will point to her repeated accusations; but the question is his behaviour, not hers.

*Other facts.* If John accepts the marriage has broken down, divorce by mutual agreement (s 95A(1)(f)) avoids a contested hearing, with a written agreement setting out the reasons, reconciliation efforts and arrangements for finances and the children (s 95A(6)) (Pre-write 1-16). Separation (3 years with consent, 4 without) is not available, as they still live together as one household (Pre-write 1-15). Desertion does not arise.

Therefore Jenny should rely on unreasonable behaviour, or on mutual agreement if John consents, rather than adultery.

**Q2021F-1a** · `1.IV.4` `1.II.2` `1.IV.3` · PYP 2021 FAM Q1 (divorce) · not mark-weighted · `pcp-w-1-13` `pcp-w-1-5` `pcp-w-1-12`

*Facts: PYP 2021 Family, under 1.I.2 above.* Advise Christine on her intended divorce proceedings.

**Answer.**

The issue is whether Christine can divorce Ken in Singapore and on which fact. She can: Ken's domicile gives the court jurisdiction, and she can rely on his unreasonable behaviour.

*Jurisdiction and timing.* Ken is a Singapore citizen by birth and so deemed domiciled here (s 3(5) WC); the court has jurisdiction under s 93(1)(a). Christine, a PR who has lived here since 2015, is also likely to be habitually resident for the three years before filing (s 93(1)(b)). They married in 2015, so the three-year bar has passed (Pre-write 1-5).

*Unreasonable behaviour.* Christine must show that Ken has behaved such that she cannot reasonably be expected to live with him (s 95A(1)(b)), assessed with regard to the parties' personalities and the cumulative effect of conduct that may be active or passive (*Wong Siew Boey v Lee Boon Fatt* [1994] SGHC 35). Ken's violence in January 2021 (she was hospitalised) and on 29 June 2021 while drunk; his compulsive share "gambling", losses, borrowing, and secret withdrawal of over S$1 million from the joint account; his verbal abuse; his neglect and nights of drinking; and his exclusion of her from caring for the children amount, cumulatively and individually, to such behaviour. She left on 29 June 2021 and has not lived with him since, so s 95A(3) is no obstacle (Pre-write 1-13).

*Other facts.* There is no evidence of adultery (his late nights and drinking do not show it), so adultery is not available (Pre-write 1-12); desertion and separation have not run long enough. Christine's own taking of the twins in January 2021 does not bar her: she relies on Ken's behaviour, not her own.

Therefore Christine can file in Singapore on the fact of unreasonable behaviour, after both parents complete the Co-Parenting Programme (s 94A; the twins are 4) (Pre-write 1-4); see the Statement of Particulars at Q2021F-2.

### 1.IV.5 — Desertion for two years

See Q1-F5-1 under 1.IV.2 (desertion; s 95A(4) on periods of living together).

### 1.IV.6 — Separation: 3 years with consent or 4 years

See QSQ-3-2 under 1.IV.7 (separate bedrooms since June 2022; *Tan Lee Tiang*; s 95A(7)), Q2025-3-2 under 1.IV.3 and Q2023-4-1 under 1.IV.4.

### 1.IV.7 — Divorce by mutual agreement

**QSQ-3-2** · `1.IV.7` `1.IV.3` `1.IV.4` `1.IV.6` `1.IV.2` · SQ Fam Q3.2; official guide SQ p126–127 · not mark-weighted · `pcp-w-1-16` `pcp-w-1-12` `pcp-w-1-13` `pcp-w-1-15` `pcp-w-1-11`

*Facts: QSQ-3-1 under 1.II.1.* Celeste is adamant about divorcing on the fact of adultery, believing it will give her an advantage on the ancillary issues. Colin will consent to the marriage being dissolved, but denies adultery, saying the marriage had broken down before he met the third party. Advise Celeste whether she can secure a divorce on the fact of adultery and what other facts she can establish.

**Answer.**

The issue is which fact Celeste should rely on to prove irretrievable breakdown. She can rely on adultery, but since Colin denies it she would have to prove it at a contested hearing; as Colin consents to the divorce, mutual agreement (or behaviour) is the better course, and the fact chosen will not give her an advantage on the ancillary issues.

*The sole ground.* The sole ground for divorce is that the marriage has irretrievably broken down (s 95 WC), proved by one of the facts in s 95A(1): adultery, behaviour, desertion, separation for 3 years with consent or 4 years without, or mutual agreement (Pre-write 1-11).

*Adultery.* She must prove that Colin committed adultery and that she finds it intolerable to live with him (s 95A(1)(a)). The surveillance report, obtained 4 weeks ago, is evidence of inclination and opportunity, and the 6-month rule is not a problem because she learnt of it only 4 weeks ago (s 95A(2)). But Colin denies it, so in a contested hearing she must prove intercourse on the evidence (FL3 s16–17). Colin's point that the marriage broke down before the affair does not defeat adultery as a fact, but it signals a fight (Pre-write 1-12).

*Unreasonable behaviour.* The quarrels and fights that led her to move out of the master bedroom, and his improper association with another woman, can found behaviour such that she cannot reasonably be expected to live with him (s 95A(1)(b); *Wong Siew Boey v Lee Boon Fatt* [1994] SGHC 35) (Pre-write 1-13).

*Mutual agreement.* Because Colin consents to the divorce, they can agree in writing that the marriage has irretrievably broken down, stating the reasons, their efforts at reconciliation and the arrangements for their finances and daughter (s 95A(1)(f), (6)); the court will consider the possibility of reconciliation. This avoids proving adultery that Colin denies and suits the non-adversarial approach (Pre-write 1-16).

*Separation.* Since June 2022 she has slept in a separate bedroom, but living apart under the same roof requires separate households, not just separate rooms (*Tan Lee Tiang v Chia Thuan Hwa* [1993] SGHC 256; s 95A(7)), and in any case only about a year has passed, short of the 3 years needed even with Colin's consent (s 95A(1)(d)) (Pre-write 1-15).

*Her misconception.* The fact relied on does not generally affect the ancillary matters: care and control turns on the daughter's welfare, and division on contributions, with conduct relevant only if gross (Pre-writes 1-17, 1-33).

Therefore Celeste can file on adultery but should prefer divorce by mutual agreement, which Colin's consent makes available, with behaviour as the alternative; she gains nothing on the ancillary matters by insisting on adultery.

### 1.V Children

Sub-points 1.V.1–1.V.7. Tested: 1.V.1 (2022), 1.V.2 (2023, 2025), 1.V.3 (2021, 2023, 2025), 1.V.4 (2023), 1.V.6 (2021). Own question F7 covers 1.V.7 and F12 (added 18 Nov, non-core) 1.V.6; 1.V.5 is answered within PYP 2025 Q6 and 2022 Q1.

### 1.V.1 — Child of the marriage; welfare as paramount; wishes of parents and child

**Q2022F-1b** · `1.V.1` `1.V.2` `1.V.3` `1.V.4` `1.V.5` · PYP 2022 FAM Q1 (children) · not mark-weighted · `pcp-w-1-17` `pcp-w-1-18` `pcp-w-1-19` `pcp-w-1-20` `pcp-w-1-21`

*Facts: PYP 2022 Family, under 1.I.2 above.* Advise Cherry on the children's arrangements, including Raymond, and on her wish that Daniel have no contact with any of the children.

**Answer.**

The issue is what orders the court is likely to make for the twins and Raymond. The court will decide on the children's welfare: Raymond is a child of the marriage; joint custody is likely; Cherry is likely to keep care and control of the twins, with Raymond's arrangements turning on his welfare and his own views; and Daniel, a dutiful father, will have access, so Cherry's wish to cut him off will fail.

*Child of the marriage and the test.* The court may make orders on custody, care and control and access for any child of the marriage below 21 (ss 122, 124–126 WC). A child of the marriage includes, besides the children of both spouses, any other child who was a member of their family when they ceased to live together (s 92). Raymond, Daniel's son whom Cherry has raised as her own since infancy, was a member of the family until Daniel left with him in March 2022, so he is a child of the marriage. The welfare of each child is the paramount consideration; subject to it, the court has regard to the parents' wishes and to the child's wishes if he is of an age to express an independent opinion (s 125(2)). Welfare is taken in its widest sense: general well-being, happiness, security and all aspects of upbringing (*Tan Siew Kee v Chua Ah Boey* [1987] SGHC 52 at [12]) (Pre-write 1-17).

*Custody.* Custody concerns major long-term decisions (schooling, religion, major medical treatment) (s 126). Joint custody is the norm; sole custody is for exceptional cases such as abuse of the child, not mere acrimony (*CX v CY* [2005] 3 SLR(R) 690; *ZO v ZP* [2011] SGCA 25). Neither parent has abused the children; joint custody is likely, and Cherry's attempt to exclude Daniel would itself support a joint order as a reminder to consult (Pre-write 1-18).

*Care and control.* Relevant factors are continuity of care and the status quo, though not one created by a unilateral act (*Wong Phila Mae v Shaw Harold* [1991] 1 SLR(R) 680; *ABW v ABV* [2014] SGHC 29), and keeping siblings together (*Kim Chun Ahe v Ng Siew Kee* [2002] SGDC 276) (Pre-write 1-19). Cherry has been the twins' primary caregiver throughout and they live with her; she is likely to keep their care and control. Raymond has lived with Daniel since March 2022, a status quo created by Daniel's departure; but he is 16, so his wishes carry real weight, and the strong bond among the three children favours arrangements that keep them close. The court would also have to handle sensitively the fact that Raymond does not know Cherry is not his mother.

*Access.* Access lets the parent without care and control keep regular contact, and joint parenthood applies to access; extreme circumstances are needed before a parent has none (*BG v BF* [2007] 3 SLR(R) 233); supervised access is exceptional (*APE v APF* [2015] SGHC 17) (Pre-write 1-20). Cherry admits Daniel has been a dutiful father and the twins miss him; his infidelity is not a reason to deny access. He is likely to have liberal access to the twins, and Cherry access to Raymond.

*Evidence and the PPO.* The court must have regard to the advice of a person trained in child welfare (s 130 WC) and may call for a custody evaluation report and interview the children if mature enough (*ZO v ZP*; *AZB v AZC* [2016] SGHCF 1) (Pre-write 1-21). The chair incident and any protection order for Calista are relevant to welfare but not decisive; Cherry should show it was a single incident, out of character, and that she immediately attended to Calista (Q2022F-1g).

Therefore the likely outcome is joint custody, care and control of the twins to Cherry, Raymond's arrangements decided on his welfare with weight given to his own views, and liberal access to Daniel; I would advise Cherry that cutting Daniel off is neither achievable nor in the children's interests.

### 1.V.2 — Custody: joint, sole, no order

**PYP 2023 Family Q5 facts.** Jenny (see Q2023-4-1) has obtained Interim Judgment dissolving her marriage to John, and the ancillary matters are before the court. They have 4-year-old twins, Gillian and Jeremy. Jenny feels she is the more appropriate caregiver and wants sole custody, care and control because of John's infidelity. She is still upset and wants to cut off all contact between the children and John. John says Jenny cannot handle both twins and it would be fairer if each parent took one child. He has moved out and is demanding to see the children immediately.

**Q2023-5-1** · `1.V.2` · PYP 2023 Q5.1 · 3 marks · `pcp-w-1-18`

Advise Jenny on the possibility of securing an order for sole custody of the children.

**Answer.**

Jenny is unlikely to obtain sole custody. A custody order entitles the person given custody to decide questions on the children's upbringing and education (s 126 WC): major, long-term decisions, not day-to-day care. It is in a child's interest to have both parents in his life, so the court ordinarily makes a joint custody order (or no order where there is no dispute on serious matters); sole custody is reserved for exceptional circumstances such as physical, sexual or emotional abuse of the child, or non-cooperation so extreme that it harms the child, and acrimony between the parents is not enough (*CX v CY* [2005] 3 SLR(R) 690, affirmed in *ZO v ZP* [2011] SGCA 25). John's infidelity is a wrong against Jenny, not abuse of the twins, and nothing suggests he is a danger to them. Where one parent is inclined to exclude the other, as Jenny is, the court has used a joint custody order to remind her to consult him (*CX v CY*). Losing on sole custody does not mean losing the children: their day-to-day care is a matter of care and control (Q2023-5-2) (Pre-write 1-18). Therefore the court is likely to order joint custody.

### 1.V.3 — Care and control: sole, shared, split

**PYP 2025 Family Q6 facts.** Deborah, a US expatriate, has lived in Singapore with her husband Michael for 8 years. The court has just dissolved the marriage by mutual agreement. Financial matters are agreed, but custody, care and control remain unresolved despite mediation. They have two children, Joseph (7) and Joy (5), and now live apart. About five months ago, against Deborah's wishes, Michael forcibly took Joseph with him when he left the matrimonial home. Deborah says Michael is not a suitable carer because his job requires frequent travel, during which he leaves Joseph with neighbours, having no family support in Singapore. Joseph resists Deborah's attempts to spend time with him, which she attributes to Michael's influence and manipulation. Deborah seeks sole custody and sole care and control of both children. Michael proposes split care (Joseph with him, Joy with Deborah) or, alternatively, shared care and control of both.

**Q2025-6** · `1.V.3` `1.V.2` `1.V.4` `1.V.5` `1.V.1` · PYP 2025 Q6 · 15 marks · `pcp-w-1-19` `pcp-w-1-18` `pcp-w-1-20` `pcp-w-1-21` `pcp-w-1-17`

Explain to Deborah the difference between sole and joint custody, and the concepts of sole, split and shared care, and the orders the court might make.

**Answer.**

The issue is what orders the court is likely to make for Joseph and Joy. The court decides on the children's welfare as the paramount consideration. It is likely to order joint custody, not sole custody; and it is likely to give Deborah sole care and control of both children, with liberal access to Michael, rejecting both split care and shared care on these facts.

*The welfare principle.* The court may make orders on custody, care and control and access for children of the marriage below 21 (ss 122, 124–126 WC). Their welfare is paramount; subject to it, the court considers the parents' wishes and the wishes of a child old enough to express an independent opinion (s 125(2)). Welfare is taken in its widest sense, covering security, stability and the child's whole upbringing (*Tan Siew Kee v Chua Ah Boey* [1987] SGHC 52 at [12]) (Pre-write 1-17).

*Custody: sole and joint.* Custody gives the right to decide all questions on the child's upbringing and education (s 126): major, long-term matters such as schooling, religion and major medical treatment. A joint custody order requires the parents to make those decisions together; it is the norm, since a child's interest is to have both parents in his life. Sole custody gives one parent that power alone and is ordered only in exceptional circumstances, such as abuse of the child or non-cooperation so extreme that it harms the child; acrimony is not enough (*CX v CY* [2005] 3 SLR(R) 690; *ZO v ZP* [2011] SGCA 25). Michael's forcible removal of Joseph and his influence over him are serious, but he has not abused the children, and the court usually addresses such conduct through care and control and access rather than sole custody. Deborah should expect joint custody (Pre-write 1-18).

*Care and control: sole, shared and split.* Care and control gives a parent authority over day-to-day matters, and the child lives with that parent; the order may set conditions, including where the child lives and a prohibition on taking the child out of Singapore (s 126(2A)–(2B)). It may be:
- *sole*: one parent has care and control and the other has access;
- *shared*: the children spend roughly equal time in two homes, which suits parents who can cooperate and live close by (*TAT v TAU* [2018] SGHCF 11; *AQL v AQM* [2011] SGHC 264);
- *split*: the children are divided between the parents; uncommon, as in *AFK v AFM* [2010] SGDC 32, where a large age gap meant the teenagers had their own lives while the youngest had a settled routine with the mother.
The welfare factors include continuity and the status quo (*Wong Phila Mae v Shaw Harold* [1991] 1 SLR(R) 680; *ABW v ABV* [2014] SGHC 29), but not a status quo created by a unilateral act; a preference, all things being equal, for the mother of a young child (*Soon Peck Wah v Woon Che Chye* [1997] 3 SLR(R) 430); and keeping siblings together (*Kim Chun Ahe v Ng Siew Kee* [2002] SGDC 276) (Pre-write 1-19).

*Application.* Split care: Joseph (7) and Joy (5) are close in age; there is none of the age gap that justified *AFK v AFM*, and separating them would cut them off from each other. Michael's arrangement for Joseph was created five months ago by forcibly taking him against Deborah's wishes, a unilateral status quo that carries little weight. Shared care: it needs cooperation and practicality; the parents have failed to agree even after mediation, Michael's job takes him away frequently, and he leaves Joseph with neighbours because he has no family support here, so shared care is impractical. Sole care to Deborah: she has continuous care of Joy and, until Michael took him, of Joseph; they are young children; and keeping them together in one stable home serves their welfare.

*Joseph's resistance.* Joseph's reluctance to see Deborah needs careful handling. The court must have regard to the advice of a person trained in child welfare (s 130 WC; *WKM v WKN* [2024] SGCA 1 at [67]), and I would ask for a Custody Evaluation Report from the FJC's CAPS to assess both homes and whether Joseph's resistance reflects Michael's influence. At 7, Joseph may be too young for his views to carry much weight, but a judicial interview is possible if he is mature enough (*ZO v ZP*; *AZB v AZC* [2016] SGHCF 1) (Pre-write 1-21). Deborah should not arrange a private psychological assessment of Joseph without the court's leave.

*Access and conditions.* Michael should have liberal access (weekday, weekend, overnight and holiday) so that both children keep their relationship with him (*BG v BF* [2007] 3 SLR(R) 233); handovers could be arranged to ease Joseph's transition back to Deborah (Pre-write 1-20). As Deborah is an expatriate, she should know that once a custody or care and control order is in force she may not take the children out of Singapore for a month or more without Michael's written consent or the court's leave (s 126(3)–(4)) (Pre-write 1-22).

Therefore the court is likely to order joint custody, sole care and control of both children to Deborah, and liberal access to Michael, after a welfare report on Joseph; it is unlikely to split the siblings or to order shared care.

**PYP 2021 Family (children) — see Q2021F-1b under 1.V.6.**

### 1.V.4 — Access: types, supervised access, conditions

**Q2023-5-2** · `1.V.4` `1.V.3` · PYP 2023 Q5.2 · 7 marks · `pcp-w-1-20` `pcp-w-1-19`

*Facts: PYP 2023 Family Q5, under 1.V.2 above.* Discuss with Jenny the orders the court may make on care and control and on access, and the basis for them.

**Answer.**

The issue is who will have care and control of the twins and what access the other parent will have. The court is likely to give Jenny sole care and control of both twins, reject John's proposal to split them, and give John liberal access; Jenny's wish to cut off all contact will not be granted.

*Care and control.* The test is the twins' welfare (s 125(2) WC). Care and control may be sole, shared or (uncommonly) split (s 126(2A)–(2B); FL4 s8). Relevant factors are continuity and the status quo (*Wong Phila Mae v Shaw Harold* [1991] 1 SLR(R) 680; *ABW v ABV* [2014] SGHC 29); a preference, all things being equal, for the mother of young children (*Soon Peck Wah v Woon Che Chye* [1997] 3 SLR(R) 430); and keeping siblings together (*Kim Chun Ahe v Ng Siew Kee* [2002] SGDC 276). Split care is rare and has been ordered where a large age gap justified it (*AFK v AFM* [2010] SGDC 32) (Pre-write 1-19). The twins are 4, the same age, and have always lived together with Jenny, who remains in the home after John moved out. Dividing them would separate twins for the parents' convenience, not their welfare. John's concern that Jenny cannot cope with two is answered by support arrangements, not separation. Shared care requires a degree of cooperation that these parents do not presently have. Sole care and control to Jenny is the likely order.

*Access.* Access allows the non-resident parent to keep regular contact; it is the children's right as much as the parent's, and joint parenthood applies to access, so a parent is denied access only in extreme circumstances (*BG v BF* [2007] 3 SLR(R) 233). Supervised access is exceptional, ordered where there are serious welfare concerns, estrangement needing repair, or difficulty in implementing unsupervised access (*APE v APF* [2015] SGHC 17). Access may be reasonable or liberal, scheduled, weekday, weekend, overnight, holiday, or by video call, and conditions may be attached (s 126(2B)) (Pre-write 1-20). John's infidelity is not a ground to deny access, and there is no suggestion he poses a risk to the children; the vase incident was directed at a wall in a quarrel with Jenny, not at the twins, though it may justify conditions on handovers. Given John's demand to see the children now, I would advise Jenny to agree interim access, which also shows the court she supports the children's relationship with their father.

Therefore the likely orders are sole care and control of both twins to Jenny and liberal (probably unsupervised) access to John, with practical conditions; Jenny should not seek to cut him off, which the court will not order and which may count against her.

### 1.V.5 — Evidence in children's cases: welfare reports, the child's views

See Q2025-6 under 1.V.3 (a Custody Evaluation Report where a child resists one parent; judicial interview; no private assessment without leave) and Q2022F-1b under 1.V.1.

**Own question F15 facts** (past-paper style; not from a past paper). In contested divorce proceedings, Rachel and Sean each seek care and control of their daughter Mia (11). Mia has told her school counsellor that she wants to live with her father "because Mum is always angry". Rachel believes Sean has been coaching Mia. Sean wants to take Mia to a private child psychologist next week so that he can file a report showing that Mia is closely attached to him. Rachel asks what evidence the court will consider about Mia, whether Mia's wishes will decide the matter, and whether she can stop Sean's plan.

**Q1-F15-1** · `1.V.5` `1.V.1` · own question, past-paper style (not from a past paper) · 6 marks · `pcp-w-1-21` `pcp-w-1-17`

Advise Rachel.

**Answer.**

The issue is how the court will find out what is best for Mia and how much weight her wishes carry. Mia's welfare is paramount; her wishes are relevant because she is 11 but will not decide the case; the court will rely on a welfare report and may interview her; and Sean may not have her examined by a psychologist for expert evidence without the court's permission.

*Welfare and the child's wishes.* The welfare of the child is the paramount consideration; subject to it, the court has regard to the wishes of the child where the child is of an age to express an independent opinion (s 125(2)(b) WC) (Pre-write 1-17). Children should have a "voice", not necessarily a "choice"; the judge must be aware of the limitations of a child's expressed views, including coaching and loyalty conflicts, and give them appropriate weight (*AZB v AZC* [2016] SGHCF 1 at [11]–[12], [20], [25]). At 11, Mia can express a view, but if it reflects Sean's influence it will carry little weight.

*Reports and interviews.* The court must have regard to the advice of a person trained or experienced in child welfare, though it is not bound by it (s 130 WC; *WKM v WKN* [2024] SGCA 1 at [67]). Rachel should ask for a Custody Evaluation Report by the Court Family Specialists, which can assess both homes and whether Mia has been coached (Pre-write 1-21). The judge may also interview Mia; the discretion is exercised for her welfare, judges are not compelled to interview, and alternatives include a Child Representative (*AZB v AZC* at [21], [24]; *ZO v ZP* [2011] SGCA 25). Given the coaching allegation, a Child Representative or the report may be better than an interview alone.

*Sean's psychologist.* A party must not, without the court's permission, cause a child to be examined or assessed by a psychologist or other mental health professional to prepare expert evidence, and evidence from an unauthorised examination needs permission to be admitted (P 10 r 4 FJ(G)R 2024; previously r 35 FJR 2014); the application is made in Form 90 (FJC PD 2024 para 95). Subjecting a child to psychological assessment may not be in her best interests (*JAC v JAD* [2014] SGDC 379). Rachel's solicitors should write to Sean's solicitors objecting, and if he persists, raise it at the case conference; a report obtained without permission is unlikely to be admitted.

Therefore the court will decide on Mia's welfare, listening to but not bound by her wishes; Rachel should seek a custody evaluation report (and possibly a Child Representative) and object to Sean's private assessment, which needs the court's permission.

### 1.V.6 — Taking a child out of Singapore and relocation (non-core)

**Q2021F-1b** · `1.V.6` `1.V.3` `1.V.4` `1.V.2` · PYP 2021 FAM Q1 (children) · not mark-weighted · `pcp-w-1-22` `pcp-w-1-19` `pcp-w-1-20` `pcp-w-1-18`

*Facts: PYP 2021 Family, under 1.I.2 above.* Advise Christine on the children: getting Charlotte back, the likely orders, her wish to relocate to Hong Kong with both twins, and her alternative of leaving Charlotte with Ken and going to Hong Kong with Marcus.

**Answer.**

The issue is what orders the court is likely to make for the twins and whether Christine can take them to Hong Kong. The court will decide on the twins' welfare: it is likely to order joint custody and to give Christine care and control of both twins, keeping them together; she should apply at once for Charlotte's return and access in the meantime; and relocation is possible only with Ken's consent or the court's leave, decided on the twins' welfare with no presumption in her favour.

*The test and custody.* The twins' welfare is paramount; the parents' wishes come second (s 125(2) WC; *Tan Siew Kee v Chua Ah Boey* [1987] SGHC 52 at [12]) (Pre-write 1-17). Joint custody is the norm; sole custody is exceptional (*CX v CY* [2005] 3 SLR(R) 690). Ken's violence was directed at Christine, not the children, but his exclusion of her from Charlotte, his refusal of even video calls, and his drinking, if they persist, may show such non-cooperation as to harm the children, which is the narrow case for sole custody. Christine should expect joint custody but can argue for more (Pre-write 1-18).

*Care and control.* Relevant factors are continuity and the status quo, but not a status quo created by a unilateral act (*ABW v ABV* [2014] SGHC 29; *Wong Phila Mae v Shaw Harold* [1991] 1 SLR(R) 680); the preference, all things being equal, for the mother of young children (*Soon Peck Wah v Woon Che Chye* [1997] 3 SLR(R) 430); and keeping siblings together (*Kim Chun Ahe v Ng Siew Kee* [2002] SGDC 276) (Pre-write 1-19). Charlotte's present stay with Ken, and with his parents, results from Christine fleeing violence and Ken's refusal of contact, so it carries little weight. Christine has been the twins' mother at home, and Ken's drinking and violence weigh against him. The twins are 4 and should not be separated; split care is uncommon and reserved for cases like *AFK v AFM* [2010] SGDC 32 with a large age gap. Christine's suggestion of leaving Charlotte with Ken is understandable in her distress, but I must advise her that it is not in either twin's interest, would weaken her case, and the court decides on welfare, not on what the parents agree to trade (r 15A PCR). She should seek care and control of both.

*Immediate steps.* The court can make orders for a child's welfare summarily at case conferences (FJ(G)R P 8 r 5) (Pre-write 1-3); before divorce is filed, she may apply under the Guardianship of Infants Act 1934 (ss 3, 5) (Pre-write 1-7). She should apply now for interim care and control of Charlotte or, at least, interim access, including video calls. The court will call for a welfare report (s 130 WC) (Pre-write 1-21).

*Access for Ken.* Ken should have access, since joint parenthood applies to access and only extreme circumstances justify none (*BG v BF* [2007] 3 SLR(R) 233); given his violence and drinking, Christine can ask for conditions such as no alcohol before or during access and handovers at a neutral venue, or supervised access at first (*APE v APF* [2015] SGHC 17) (Pre-write 1-20).

*Relocation to Hong Kong.* While a custody or care and control order is in force, no one may take a child out of Singapore except with the written consent of both parents or the court's leave, save that the person with custody or care and control may do so for less than one month (s 126(3)–(4) WC); doing so otherwise is an offence (s 126(5)), and the court may restrain removal by injunction (s 131). On an application for leave to relocate, the welfare principle governs; the primary caregiver's reasonable wish to relocate is a factor, not a presumption, and the loss of the left-behind parent's relationship is important but not determinative (*BNS v BNT* [2015] SGCA 23). Christine's reasons are genuine (her family and support are in Hong Kong, her depression, the abuse here), but the twins have lived all their lives in Singapore, attend school here, and Ken's relationship with them would be greatly reduced. She would need a detailed plan for schooling, housing and Ken's continued contact (overseas and video access). She must not take the children to Hong Kong without consent or leave (Pre-write 1-22).

Therefore Christine should seek joint custody (or sole custody if Ken's obstruction continues), care and control of both twins with conditions on Ken's access, an immediate interim order for Charlotte, and, if she still wishes to relocate, Ken's written consent or the court's leave with a full plan; she should not leave Charlotte behind or remove either child without consent or leave.

**Own question F12 facts** (non-core; not from a past paper). Lena, an Australian, and Marc, a Singaporean, married in 2014 and moved to Singapore in 2016 for Marc's job; Lena gave up her teaching post in Melbourne. They have two children, Ella (9) and Sam (6). Interim judgment was granted last month; at the ancillary hearing Lena expects joint custody and care and control of both children, who have lived with her since the separation. Marc has had access every Wednesday evening and alternate weekends, which he has never missed, and he coaches Sam's football team. Lena has no family here, has been treated for depression since the separation, and has been offered a teaching job in Melbourne, where her parents will house them and the children have school places. She proposes that Marc have the children for most of the June and December school holidays and daily video calls, and offers to pay half the airfares. Lena asks: (a) whether she can take the children to Melbourne for two weeks over Christmas this year; and (b) whether she can move there with them for good, and what the court will consider.

**Q1-F12-1** · `1.V.6` `1.V.4` · own question, not from a past paper · 10 marks · `pcp-w-1-22` `pcp-w-1-20`

Advise Lena.

**Answer.**

The issue is whether Lena needs Marc's consent or the court's leave to take the children to Melbourne, first for a holiday and then for good. Once a care and control order is in force she may take them abroad for less than one month without anyone's consent, but a permanent move needs Marc's written consent or the court's leave; leave will be decided on the children's welfare with no presumption in her favour, and Marc's close, active bond with them is the main obstacle to her application.

*(a) The Christmas holiday.* Where an order for custody or care and control is in force, no person may take the child out of Singapore except with the written consent of both parents or the leave of the court (s 126(3) WC), but this does not prevent the person given care and control from taking the child out of Singapore for less than one month (s 126(4)). If Lena is given care and control, a two-week holiday is within s 126(4); she should still give Marc the itinerary and contact details, as overseas access orders often require (Pre-write 1-20). Until the order is made, she should obtain Marc's written consent, because he may otherwise apply for an injunction restraining removal (s 131) (Pre-write 1-22).

*(b) Relocation: the law.* A move to Melbourne needs Marc's written consent or the court's leave (s 126(3)); taking the children without either is an offence punishable with a fine of up to $5,000, imprisonment of up to 12 months, or both (s 126(5)), and, Australia being a Contracting State to the Hague Convention, could lead to an order for their return (Pre-write 1-23). On an application for leave, the welfare of the child is paramount and "ought to override any other consideration" (*BNS v BNT* [2015] SGCA 23 at [19]). There is no legal presumption in favour of relocation ([22]). The primary caregiver's reasonable wish to relocate is an important but not a singularly determinative factor, mattering chiefly where refusal would transfer her unhappiness and insecurity to the children ([20]–[21]); the loss of the children's relationship with the left-behind parent is an important consideration, not determinative, and "the stronger the bond, the larger the resultant void" ([25]–[26]). The court looks at the children's age, their attachment to each parent and their developmental needs, and relocation cases are very fact-specific (*UYK v UYJ* [2020] SGHCF 9 at [34], [37]) (Pre-write 1-22).

*Application.* In Lena's favour: she is the children's primary caregiver; her wish is genuine and reasonable, since she came to Singapore only for Marc's career, has no family here and has a job, housing and family support in Melbourne (compare the "trailing spouse" in *UYK v UYJ* at [33]–[34]); her depression is relevant if refusing the move would leave her isolated and unwell in a way that affects the children (*BNS v BNT* [20]–[21]); and her plan is detailed, with school places, generous holiday access, daily video calls and shared airfares. Against her: Marc has never missed access and coaches Sam's team, so the bond is strong and the void would be large ([25]–[26]); Ella and Sam have spent most of their lives in Singapore, and a move would replace weekly contact with two long holidays a year. In *BNS v BNT* a strong, active relationship with the father, together with a poorly conceived plan, led the Court of Appeal to refuse relocation ([32], [35]); Lena's plan is much better prepared, but Marc's bond is at least as strong. The court will call for a welfare report (s 130) and may hear the children's views, Ella's in particular, if she is mature enough (s 125(2)(b)) (Pre-write 1-21).

*Practical advice.* Lena should first ask Marc for his written consent, offering the contact plan in writing and through mediation; if he refuses, she should apply for leave with evidence of the job, school places, housing, her medical position and the proposed access, and keep facilitating his access meanwhile, since hostility to the other parent counts against her.

Therefore Lena may take the children on a two-week Christmas holiday once she has care and control (with Marc's written consent before then), but she can move them to Melbourne only with Marc's written consent or the court's leave; leave is possible but uncertain, because her strong plan and reasons must be weighed against the children's close bond with Marc, with no presumption in her favour.

### 1.V.7 — International child abduction (non-core)

**Own question F7 facts.** Ivy and Jon lived with their son Kai (6) in Country X, a Contracting State to the Hague Convention that has accepted Singapore's accession, where they had joint rights of custody. Eight months ago Ivy flew with Kai to Singapore for a holiday and did not return; Jon did not consent. Jon has applied in Singapore for Kai's return. Ivy says Jon was violent towards her in Country X and that Kai is now happily settled in a Singapore school.

**Q1-F7-1** · `1.V.7` · own question · 8 marks · `pcp-w-1-23`

Advise Ivy on Jon's application.

**Answer.**

The issue is whether the Singapore court must order Kai's return to Country X. Kai's retention here is wrongful, and because Jon applied within a year the court must order his return forthwith unless Ivy establishes one of the limited Article 13 defences; her allegation of violence is her only real argument.

*Framework.* The International Child Abduction Act 2010 implements the Hague Convention on the Civil Aspects of International Child Abduction, whose aim is the prompt return of children wrongfully removed to or retained in a Contracting State; it applies between Singapore and Contracting States that have accepted Singapore's accession. The primary issue is the child's habitual residence immediately before the removal or retention; once wrongful removal or retention is shown, a return order is made unless a limited Article 13 defence applies (*BDU v BDT* [2014] 2 SLR 725; *TUC v TUD* [2017] 4 SLR 877) (Pre-write 1-23).

*Wrongful retention.* Removal or retention is wrongful where it breaches rights of custody under the law of the State of habitual residence immediately before, and those rights were actually exercised (Art 3). Kai lived in Country X with both parents, who had joint rights of custody that Jon was exercising; Ivy's keeping him here after the holiday without Jon's consent is a wrongful retention.

*Time.* Where proceedings begin within one year of the wrongful removal or retention, the court shall order return forthwith (Art 12). Jon applied within eight months, so the "settled in its new environment" exception, which applies only after a year, is not open to Ivy; Kai's happiness at school does not answer the application.

*Defences (Ivy bears the burden).* The court may refuse return if (a) Jon was not actually exercising custody rights, or consented to or later acquiesced in the removal or retention; or (b) there is a grave risk that return would expose Kai to physical or psychological harm or otherwise place him in an intolerable situation; or if Kai objects and has reached an age and maturity at which his views should be taken into account (Art 13); or if return would breach fundamental principles of human rights (Art 20). Nothing suggests consent or acquiescence. Ivy's allegations of violence go to Art 13(b), but the defences are limited (FL4 s15): she must establish, with evidence, a grave risk that return would expose Kai to physical or psychological harm or place him in an intolerable situation; Jon's violence towards her helps only so far as it shows that risk to Kai. At 6, Kai is unlikely to be mature enough for his objections to be decisive. The FJC does not mediate ICAA applications, so any settlement would be through private mediation (FL8 s22).

Therefore a return order is likely; Ivy's only realistic defence is grave risk under Art 13(b), which needs strong evidence of risk to Kai, and she should also consider negotiating safe arrangements for Kai's return.

### 1.VI Maintenance

Sub-points 1.VI.1–1.VI.4. Tested: 1.VI.1 (2021, 2022), 1.VI.3 (2021, 2022). Own question F8 covers 1.VI.2 and 1.VI.4.

### 1.VI.1 — Child maintenance

**Q2022F-1c** · `1.VI.1` `1.VI.2` `1.VI.3` · PYP 2022 FAM Q1 (maintenance) · not mark-weighted · `pcp-w-1-24` `pcp-w-1-25` `pcp-w-1-26`

*Facts: PYP 2022 Family, under 1.I.2 above.* Advise Cherry on maintenance for herself and the children, given that Daniel has cut off all financial support since March 2022.

**Answer.**

The issue is what maintenance Cherry can obtain for the children and herself, and under which provision. Until she files for divorce she can claim now under s 69 WC for herself and the twins on proof of Daniel's neglect or refusal; once divorce is filed, maintenance is decided under ss 113 and 127. Daniel is likely to bear most of the children's needs, and Cherry, a homemaker for 16 years at his insistence, has a strong claim to maintenance for herself, though the amount will reflect what she receives on division.

*Children.* A parent must maintain or contribute to the maintenance of his children, whether legitimate or not (s 68 WC). On proof that a parent has neglected or refused to provide reasonable maintenance for a child, the court may order monthly or lump sum payments (s 69(2)); the applicant bears the burden (*UHA v UHB* [2019] SGHCF 12). The court considers the s 69(4) factors, chiefly the child's needs and each parent's means and earning capacity; the equal duty does not mean equal shares, and apportionment may follow the income ratio (*WBU v WBT* [2023] SGHCF 3). Extravagant items are not reasonable needs (*APE v APF*, per Cyril). Maintenance runs to 21, or beyond for a child in full-time education or national service (s 69(5)). In divorce, child maintenance is ordered under s 127 on the same principles (Pre-write 1-24). Daniel's stopping all deposits since March 2022 is plain neglect or refusal. Though retired, he has substantial investment income and assets; Cherry has no income. He should bear almost all of the twins' reasonable expenses (schooling, food, transport, activities) and he must maintain Raymond, his own son, who lives with him. Cherry's duty to Raymond as a non-parent who accepted him into the family (s 70) ends once he is taken away on the breakdown of the marriage (*EB v EC* [2006] 2 SLR(R) 475; *TDT v TDS* [2016] 4 SLR 145).

*Cherry's own maintenance: which provision.* While the marriage subsists and no divorce is filed, a wife may claim under s 69 on proof that her husband has neglected or refused to maintain her; once divorce proceedings are filed, the claim lies under s 113 (*Foo Ah Yan v Chiam Heng Chow* [2012] SGCA 15). Because she intends to divorce soon, a s 69 order would be overtaken; she can seek interim maintenance after filing (Pre-write 1-25).

*Quantum on divorce.* Under s 113, the court considers the s 114(1) factors: income, earning capacity and resources; needs; the standard of living before breakdown; age and duration of the marriage; contributions to the family including homemaking and caring; and any lost benefits. It tries, so far as practicable and just, to place the parties in the financial position they would have been in had the marriage not broken down (s 114(2)). Maintenance supplements the division of assets (*ATE v ATD* [2016] SGCA 2) (Pre-write 1-26). Cherry is 42, gave up her career in 2006 at Daniel's insistence, has been out of work for 16 years and earned only S$2,000 a month when she stopped; the family lived well on Daniel's income of over S$40,000 a month. Her need is real, and Daniel can pay; but if she receives a substantial share of a large pool (Q2022F-1e), her maintenance may be reduced. She must disclose her POSB account, which is part of her resources (Q2022F-1f).

Therefore Cherry should claim maintenance for the twins (and interim maintenance for herself) at once, under s 69 now or within the divorce once filed, with Daniel bearing the bulk of the children's needs and a substantial sum for her under ss 113–114, adjusted for what she receives on division.

### 1.VI.2 — Maintenance during marriage (s 69) and after divorce is filed (s 113)

**Own question F8 facts.** Lily and Max are married with no divorce proceedings. Three months ago Max stopped paying the household bills and has given Lily nothing since. Lily works part-time. She asks whether she can claim maintenance now, what happens if she later divorces, how long any order will last, and whether she should ask for maintenance if she does not need much now.

**Q1-F8-1** · `1.VI.2` `1.VI.4` `1.VI.3` · own question · 8 marks · `pcp-w-1-25` `pcp-w-1-27` `pcp-w-1-26`

Advise Lily.

**Answer.**

The issue is which provision governs Lily's claim at each stage, how long an order lasts, and whether she should seek an order now to preserve her position. She may claim now under s 69 WC; once divorce is filed the claim lies under s 113; an order lasts until either party dies or she remarries unless it says otherwise; and since variation needs a subsisting order, she should consider seeking one.

*Now: s 69.* Section 69 WC provides temporary relief for a wife (or incapacitated husband) during a subsisting marriage, on proof that the husband has neglected or refused to provide reasonable maintenance; it is not an ancillary matter. It covers a "married woman", including Muslim and foreign wives in Singapore and a party to a voidable marriage until annulment, but not a party to a void marriage. Max's stopping all support for three months is neglect or refusal, so Lily can apply. Her right to maintenance does not depend on fault, though conduct may affect the amount (Pre-write 1-25).

*After divorce is filed: s 113.* Once proceedings are filed or the marriage ends, she is no longer claiming as a wife during marriage; the claim lies under s 113, with interim maintenance pending the ancillary hearing. The two regimes have different considerations and goals (*Foo Ah Yan v Chiam Heng Chow* [2012] SGCA 15). If divorce is imminent, a s 69 application may be overtaken (Cyril-Exam §5.2.2). On divorce the amount is assessed under the s 114 factors, mainly her needs and Max's ability to pay, and supplements the division of assets (*ATE v ATD* [2016] SGCA 2) (Pre-write 1-26).

*Duration and variation.* Unless the order is expressed for a shorter period or rescinded, an unsecured maintenance order expires on the death of either party, or on the remarriage of the former wife receiving it (s 117 WC). The court may vary or rescind a subsisting maintenance order on either party's application where it was based on a misrepresentation or mistake of fact or there has been a material change in circumstances (s 118). But variation requires a subsisting order (*Tan Bee Giok v Loh Kum Yong* [1996] SGCA 69): if no order is made on divorce, she may be unable to claim later (Pre-write 1-27).

*Preserving the claim.* The courts sometimes preserved a wife's right by a nominal order (*APE v APF* [2015] SGCA 47), but following *ATE v ATD* a nominal order is not made as a matter of course; "something more" must be shown, and the former husband is not a "general insurer". If Lily expects her needs may grow (her part-time income, health or the children's needs), she should seek a modest order on divorce based on her actual needs, rather than rely on a nominal one.

Therefore Lily should apply under s 69 now for her reasonable needs; if she files for divorce, claim under s 113 instead; and, because variation needs a subsisting order, seek a real (if modest) order on divorce rather than none.

### 1.VI.3 — Maintenance of a wife or incapacitated husband on divorce

**Q2021F-1c** · `1.VI.3` `1.VI.1` `1.VI.4` · PYP 2021 FAM Q1 (maintenance) · not mark-weighted · `pcp-w-1-26` `pcp-w-1-24` `pcp-w-1-27`

*Facts: PYP 2021 Family, under 1.I.2 above.* Christine wants to know Ken's obligations to her in terms of maintenance.

**Answer.**

The issue is whether Christine can obtain maintenance for herself and the twins. Her own claim is weak, because her dividends of about S$170,000 a year meet her needs; but both parents must maintain the twins, and Ken, who earns more, should bear the larger share.

*Christine.* On divorce the court may order a husband to pay maintenance to his wife or former wife (s 113 WC), considering the s 114(1) factors: each party's income, earning capacity, property and resources; their needs; the standard of living before breakdown; their ages and the length of the marriage; and contributions to the family. The aim, so far as practicable and just, is to place them in the position they would have been in had the marriage not broken down (s 114(2)). The basis is financial preservation or evening out inequities (*BG v BF* [2007] 3 SLR(R) 233; *Foo Ah Yan v Chiam Heng Chow* [2012] SGCA 15), and maintenance supplements the division of assets; a nominal order to preserve a future claim is not made as a matter of course, since the former husband is not a "general insurer" (*ATE v ATD* [2016] SGCA 2) (Pre-write 1-26). Christine has an independent income of about S$170,000 a year, never needed to work, and will also receive a share of the assets. Her needs are largely met, so substantial maintenance is unlikely, and she would need to show "something more" to justify even a nominal order. Without a subsisting order she cannot later apply to vary (*Tan Bee Giok v Loh Kum Yong* [1996] SGCA 69) (Pre-write 1-27).

*The twins.* Both parents must maintain their children (s 68 WC). In divorce, the court orders child maintenance under s 127 on the principles in ss 68–69: the children's reasonable needs against each parent's means and earning capacity (s 69(4)), with apportionment that may follow the income ratio (*WBU v WBT* [2023] SGHCF 3); extravagant items are excluded (*APE v APF*, per Cyril) (Pre-write 1-24). Ken earns over S$25,000 a month (about S$300,000 a year), against her S$170,000, so he should bear the larger share of the twins' reasonable expenses (pre-school, care, food, medical), assessed on their actual needs. If the twins are in Christine's care, Ken will pay a monthly sum to her for them.

Therefore Christine should not expect significant maintenance for herself, but should claim child maintenance for the twins, with Ken bearing the larger part in proportion to his higher income.

### 1.VI.4 — Duration and variation of maintenance orders

See Q1-F8-1 under 1.VI.2 (s 117; s 118; *Tan Bee Giok*; nominal orders after *ATE v ATD*) and Q2021F-1c under 1.VI.3.

### 1.VII Division of matrimonial assets

Sub-points 1.VII.1–1.VII.10. Tested: 1.VII.1 (2021, 2022, 2023, 2025), 1.VII.2 (2021, 2022, 2025), 1.VII.3 (2021, 2022), 1.VII.6 (2023, 2025), 1.VII.7 (2022, 2025), 1.VII.9 (2022), 1.VII.10 (2021, 2022). Own questions F9 (1.VII.4, 1.VII.5), F10 (1.VII.8) and F13 (added 18 Nov, non-core: 1.VII.1 after a foreign divorce, 1.VII.8).

### 1.VII.1 — The power to divide: just and equitable; equal partnership

**PYP 2023 Family Q6 facts.** Amanda and her husband have been married about 15 years and have one child, aged 18, about to enlist for National Service. Both have worked throughout the marriage: Amanda is a nurse earning about $4,500 a month; her husband is a private banker earning about $20,000 a month. Both salaries are paid into their joint DBS account. They own a terrace house on East Coast Road in joint names; both contributed to the downpayment, and both service the mortgage from their CPF accounts and from cash in the joint DBS account. The other assets are their CPF monies, a car in [the husband's] name and separate OCBC accounts in each of their sole names.

**Q2023-6** · `1.VII.1` `1.VII.2` `1.VII.4` `1.VII.5` `1.VII.6` · PYP 2023 Q6 · 15 marks · `pcp-w-1-28` `pcp-w-1-29` `pcp-w-1-31` `pcp-w-1-32` `pcp-w-1-33`

Advise and discuss with Amanda how the court would approach the division of their matrimonial assets.

**Answer.**

The issue is how the court will divide the assets of this 15-year dual-income marriage. It will identify the pool, value it, and divide it justly and equitably using the *ANJ* structured approach: a ratio of direct contributions (which will favour her husband, the far higher earner), a ratio of indirect contributions, an average, and adjustments. Amanda can expect a share well above her share of the income, probably in the region of 35–45%, depending on her indirect contributions.

*The power and its basis.* On or after granting a divorce the court may divide the matrimonial assets in such proportions as it thinks just and equitable (s 112(1) WC). Marriage is treated as an equal co-operative partnership of efforts in which financial and homemaking contributions are both recognised (*NK v NL* [2007] 3 SLR(R) 743), but there is no presumption of equal contribution or norm of equal division (*Lim Choon Lai v Chew Kim Heng* [2001] 2 SLR(R) 260; *Lock Yeng Fun v Chua Hock Chye* [2007] 3 SLR(R) 520). The approach is broad brush (*UYQ v UYP* [2020] 1 SLR 551) (Pre-write 1-28).

*Step 1: the pool.* Matrimonial assets include every asset acquired during the marriage by one or both parties, whatever its name (s 112(10)(b)), and pre-marital assets that were ordinarily used by the family or substantially improved during the marriage (s 112(10)(a)); *USB v USA* [2020] 2 SLR 588 groups them into four categories (Pre-write 1-29). The pool here is: the East Coast terrace house (the matrimonial home, entire value); CPF balances accumulated during the marriage (pre-marital balances are excluded unless used for the home); the joint DBS account; each party's OCBC account; and the car. Each party must make full and frank disclosure (Pre-write 1-37). The assets are identified as at the date of Interim Judgment and valued as at the ancillary matters hearing, save that bank and CPF balances are taken at the Interim Judgment date (*ARY v ARX* [2016] SGCA 13; *BPC v BPB* [2019] SGCA 3) (Pre-write 1-31).

*Methodology.* All the assets are the product of the parties' pooled efforts, so the court will use the global assessment methodology rather than classify assets (*NK v NL*; *UTQ v UTR* [2019] SGHCF 13) (Pre-write 1-32).

*Step 2: ANJ.* The court (1) expresses as a ratio each party's direct financial contributions to acquiring or improving the assets; (2) expresses as a ratio their indirect contributions, financial and non-financial, to the family's welfare; (3) averages them, giving more weight to one where the circumstances warrant; and (4) adjusts for the s 112(2) factors (*ANJ v ANK* [2015] 4 SLR 1043) (Pre-write 1-33).

- *Direct.* Both salaries went into the joint account, which paid the mortgage with their CPF. The money in that account, and so the cash payments on the house, came about 80% from the husband ($20,000 of $24,500 a month), and his CPF contributions were also far larger. Unless Amanda can trace larger contributions of her own (for example to the downpayment), the direct ratio will favour him substantially.
- *Indirect.* Both worked full-time. The question is who carried the homemaking and the care of their child; a nurse working shifts may still have done much of it. If she was the main carer, her indirect ratio may well exceed 50%; if the burden was shared or a helper was employed, it will be closer to equal. The husband's financial support of the household counts as an indirect financial contribution.
- *Average and weight.* In a 15-year marriage indirect contributions are significant, so the two ratios are likely to be given equal weight.
- *Adjustments.* The child is 18 and about to start National Service; the court considers the needs of children (s 112(2)(c)), and child maintenance may extend beyond 21 during National Service or education (s 69(5)) (Pre-write 1-24).

*Outcome.* For example, a direct ratio of 75:25 (husband:Amanda) and an indirect ratio of 45:55 averaged equally gives 60:40. Amanda should gather the downpayment records, CPF statements and evidence of her role in raising their child.

Therefore the court will pool the house, CPF, bank accounts and car, apply the *ANJ* approach, and is likely to give Amanda a share well above the proportion of her income, around 35–45% depending on her indirect contributions.

### 1.VII.2 — Identifying matrimonial assets (s 112(10); USB v USA)

See Q2025-5 under 1.VII.6 (a pre-marital apartment used as the family home and renovated by the wife), Q2022F-1d under 1.VII.9 and Q2021F-1d under 1.VII.3.

### 1.VII.3 — Gifts, inheritance, inter-spousal gifts and windfalls (non-core)

**Q2021F-1d** · `1.VII.3` `1.VII.2` `1.VII.10` `1.VII.1` · PYP 2021 FAM Q1 (division) · not mark-weighted · `pcp-w-1-30` `pcp-w-1-29` `pcp-w-1-37` `pcp-w-1-28`

*Facts: PYP 2021 Family, under 1.I.2 above.* Advise Christine on Ken's obligations to her in terms of division of assets.

**Answer.**

The issue is which assets fall into the pool and how Ken's undisclosed dealings will be treated. The Grange Road bungalow is in the pool despite being her parents' gift, because it was the matrimonial home; her Hong Kong properties, also gifts but never used by the family, are out; the Bukit Timah property, bought during the marriage, is in; and Ken must account for the River Valley profits and the S$1m he withdrew, failing which the court is likely to draw an adverse inference against him.

*Framework.* The court divides the matrimonial assets justly and equitably (s 112(1) WC; *NK v NL* [2007] 3 SLR(R) 743) (Pre-write 1-28). Matrimonial assets are all assets acquired during the marriage, and pre-marital assets ordinarily used by the family or substantially improved during the marriage (s 112(10)) (*USB v USA* [2020] 2 SLR 588) (Pre-write 1-29). Gifts and inheritances from third parties are excluded unless they are the matrimonial home or have been substantially improved during the marriage by the other party or both (s 112(10); *Chen Siew Hwee v Low Kee Guan* [2006] 4 SLR(R) 605); the donee's intention may also bring a gift into or out of the pool (*CLC v CLB* [2023] 1 SLR 1260) (Pre-write 1-30).

*The assets.*
- *Grange Road bungalow:* a wedding gift from her parents, but the family lived there from 2016 as the matrimonial home, and it is in joint names. It is a matrimonial asset, entire value.
- *Hong Kong properties:* gifts from her parents, never used by the family or improved by Ken: excluded.
- *Bukit Timah Road property:* bought in 2017 during the marriage, in her sole name: a matrimonial asset, entire value (S$3.5m), regardless of title; her funding and her S$100,000 renovation count as her direct contributions.
- *River Valley condominium:* Ken's pre-marital asset, but the couple lived there after the marriage, so it became a matrimonial asset through ordinary use as the family home (s 112(10)(a)(i)). It has been sold; after the share repaid to his parents, Ken's share of the proceeds, including the profit he kept, should be accounted for in the pool.
- *Joint account:* the deposits made during the marriage are matrimonial. Ken withdrew over S$1m without her knowledge to fund trading and losses.
- *Her Hong Kong bank account:* dividends received during the marriage are assets acquired during the marriage, so in the pool. Her minority shareholding itself predates the marriage and, if it was a gift from her parents, is excluded; if not, only any part acquired during the marriage counts.
- *Ken's other assets:* his bank accounts, CPF accumulated during the marriage, investments and cars (the Bentley and the Mercedes) are all matrimonial assets, but Christine knows nothing of them.

*Disclosure and adverse inference.* Both parties must make full and frank disclosure (*USB v USA*). Christine should seek disclosure orders under Part 9 FJ(G)R (Pre-write 1-6). An adverse inference may be drawn where there is a substratum of evidence establishing a prima facie case of concealment and the party had particular access to the information (*BPC v BPB* [2019] 1 SLR 608 at [60]). Ken earns over S$25,000 a month, sold River Valley at a large profit and withdrew over S$1m, yet she does not know where any of it went: a strong prima facie case, with the information in his hands. The court may quantify identified sums and add them back to the pool (for example the S$1m and the River Valley profit), or award her a higher share of the known assets (uplift) (*UZN v UZM* [2021] 1 SLR 426) (Pre-write 1-37).

*Division.* The court will apply the *ANJ* structured approach (Pre-write 1-33). This is a marriage of about six years with young twins; both direct and indirect contributions matter. Christine's direct contributions are substantial (Bukit Timah, her share of the joint account deposits), and her indirect contributions include caring for the twins; Ken's direct contributions depend on what he discloses.

Therefore the pool comprises Grange Road, Bukit Timah, the joint account (with the S$1m added back), the River Valley proceeds, her Hong Kong account and all of Ken's assets, but not her Hong Kong properties; she should seek disclosure orders now and ask the court to draw an adverse inference against Ken if he cannot account for the money.

### 1.VII.4 — Dates for identifying and valuing the pool

**Own question F9 facts.** Interim Judgment was granted to Oscar and Pam on 2 March 2026; the ancillary matters hearing is in November 2026. Since Interim Judgment, Oscar has bought a new car with his bonus, and the value of the flat has risen. In January 2026, a month before Interim Judgment, Pam withdrew $80,000 from her savings account to pay her brother's gambling debts. Oscar also has a share portfolio built entirely from an inheritance he received during the marriage and his own trading, which he has never disclosed in full.

**Q1-F9-1** · `1.VII.4` `1.VII.5` `1.VII.10` · own question · 8 marks · `pcp-w-1-31` `pcp-w-1-32` `pcp-w-1-37`

At what dates will the pool be identified and valued, and should the court use the global or the classification methodology?

**Answer.**

The issue is which dates fix the pool and the values, and how the court will treat assets of different kinds. By default the pool is identified at Interim Judgment and valued at the ancillary hearing, save that bank and CPF balances are taken at Interim Judgment; the court can depart from this, for example to add back Pam's withdrawal. The global methodology is usual, but classification may be justified for Oscar's portfolio.

*Dates.* There are four candidate dates: separation, filing, Interim Judgment and the ancillary matters hearing. The default is that matrimonial assets are identified as at the date of Interim Judgment and valued as at the ancillary matters hearing, except that monies in bank and CPF accounts are taken at their Interim Judgment values; the court may depart from the default where the circumstances justify it (*ARY v ARX* [2016] SGCA 13; *BPC v BPB* [2019] SGCA 3) (Pre-write 1-31). So Oscar's new car, bought after 2 March 2026, is not in the pool unless the court departs from the default (for example if bought with matrimonial money); the flat is valued at its November 2026 value, so both share in the rise; and bank and CPF balances are taken at 2 March 2026. Pam's $80,000 was withdrawn before Interim Judgment, so it is not in her account at that date; Oscar will ask the court to add it back as a dissipation of matrimonial funds, which the court may do in substance as an adjustment or by drawing an inference if she cannot account for it (Pre-write 1-37).

*Methodology.* The global assessment methodology takes the net value of all matrimonial assets and divides it justly and equitably; the classification methodology splits the assets into classes with separate apportionments, keeping indirect contributions constant across classes (*NK v NL* [2007] 3 SLR(R) 743). Classification is used only where there are distinct classes of assets to which the parties contributed differently or some assets are not wholly the gains of the marital partnership (*UTQ v UTR* [2019] SGHCF 13), and *NK v NL* applied it where an adverse inference was drawn about one class of assets (per Cyril) (Pre-write 1-32). Oscar's portfolio is built from an inheritance received during the marriage: a gift or inheritance is excluded from the pool unless it is the matrimonial home or has been substantially improved by the other party or both (s 112(10)) (Pre-write 1-30). So far as the portfolio is traceable to the inheritance and Pam did not help to improve it, it stays out; so far as Oscar added money earned during the marriage, that part is a matrimonial asset (s 112(10)(b)), but one to which Pam contributed little directly. And because he has not disclosed it fully, an adverse inference may attach to that class (*BPC v BPB* [2019] 1 SLR 608 at [60]). Both points support classifying the portfolio separately; the rest of the pool (flat, CPF, accounts) would be assessed globally.

Therefore the pool is identified at 2 March 2026 and valued in November 2026 (bank and CPF at 2 March 2026), with Pam's withdrawal likely to be added back; and the court may treat Oscar's portfolio as a separate class while dealing with the other assets globally.

### 1.VII.5 — Global assessment and classification methodologies

See Q1-F9-1 under 1.VII.4 (when classification is justified, *UTQ v UTR*) and Q2023-6 under 1.VII.1 (global assessment for a dual-income couple).

**Own question F16 facts** (past-paper style; not from a past paper). Ahmad and Lina were married for 18 years; both worked throughout. The pool comprises their HDB flat and CPF, built up jointly, worth S$900,000, and a trading portfolio worth S$2 million that Ahmad built during the marriage from a S$300,000 inheritance and his own trading on weekends, which Lina never contributed to. Ahmad also failed to explain withdrawals of S$400,000 from his bank accounts in the year before he filed for divorce.

**Q1-F16-1** · `1.VII.5` `1.VII.10` `1.VII.6` · own question, past-paper style (not from a past paper) · 5 marks · `pcp-w-1-32` `pcp-w-1-37` `pcp-w-1-33`

Advise Lina on how the court is likely to approach the division methodologically.

**Answer.**

The issue is whether the court will assess contributions across the whole pool (global assessment) or class by class (classification). Because the trading portfolio is a distinct class to which the parties contributed very differently, and there is a possible adverse inference about Ahmad's withdrawals, classification is likely to be considered, with the ANJ approach applied within each class.

The global assessment methodology takes the net value of all the matrimonial assets and divides it justly and equitably; the classification methodology separates the assets into classes with individual apportionments, keeping indirect contributions constant across classes (*NK v NL* [2007] 3 SLR(R) 743) (Pre-write 1-32). Classification is appropriate where there are multiple classes of assets and some are not wholly the gains of the parties' cooperative partnership (*UTQ v UTR* [2019] SGHCF 13). The ANJ structured approach then applies, broad brush rather than arithmetically (*ANJ v ANK* [2015] 4 SLR 1043; *UYQ v UYP* [2020] SGCA 3 at [3]) (Pre-write 1-33).

The flat and CPF are jointly funded and suit a single ratio. The portfolio was built from an inheritance and Ahmad's own efforts; the original S$300,000 is an excluded inheritance unless transformed (s 112(10)) (Pre-write 1-30), but its growth through his trading during the marriage is a matrimonial asset to which Lina's direct contribution is nil, so a separate class reflects that difference. Ahmad's unexplained withdrawals may justify an adverse inference, by adding the sum back or by an uplift in Lina's share (*UZN v UZM* [2021] 1 SLR 426) (Pre-write 1-37); an inference affecting one class also points to classification (*NK v NL*).

Therefore Lina should expect the court to consider classification, with a lower share for her in the portfolio class but her indirect contributions held constant, and should press for an adverse inference over the S$400,000; if the court prefers a global assessment, she should argue that her indirect contributions over 18 years justify a substantial share of the whole pool.

### 1.VII.6 — The ANJ structured approach and the s 112(2) factors

**PYP 2025 Family Q5 facts.** Vikram and Mira, both Singapore citizens, have been married about 15 years and have two sons aged 10 and 3; the younger has cerebral palsy, with severe movement limitations, needs a wheelchair and substantial support. Mira divorced Vikram on his alleged behaviour; Interim Judgment was granted by consent in July 2025, ancillary matters adjourned to chambers. Joint custody, care and control to Mira, liberal access to Vikram, and child and spousal maintenance are agreed. Division is unresolved. Vikram is a supervisor earning $12,000 a month gross. Mira was a teacher (Head of Department) earning $8,000 a month but stopped work 3 years ago to look after the younger child after his diagnosis. They live in a 5-room HDB flat in joint names (minimum occupation period fulfilled); both used CPF monies for the purchase, with a bank loan for the balance; they paid the initial capital payment equally and shared the mortgage equally from CPF until Mira stopped work, since when Vikram has paid it all by CPF and cash. Vikram owns an Aljunied apartment in his sole name, bought before the marriage, with no mortgage; the family lived there for about 2 years while awaiting the HDB keys, and Mira spent $20,000 of her savings renovating it for the family. It is now rented out; part of the rent services the HDB loan and Vikram keeps the rest. The other assets are their CPF accounts, a car in Mira's name and separate OCBC accounts in each of their sole names; there are no joint accounts. You act for Vikram.

**Q2025-5** · `1.VII.6` `1.VII.2` `1.VII.1` `1.VII.4` `1.VII.7` · PYP 2025 Q5 · 15 marks · `pcp-w-1-33` `pcp-w-1-29` `pcp-w-1-28` `pcp-w-1-31` `pcp-w-1-34`

Advise and discuss with Vikram how the court would approach the division of their matrimonial assets.

**Answer.**

The issue is how the court will divide the assets after this 15-year marriage. It will identify the pool, which includes the Aljunied apartment at its full value because the family lived in it; value it; and apply the *ANJ* structured approach, since this was a dual-income marriage for most of its length. Vikram's larger direct contributions will be balanced by Mira's indirect contributions, especially her sacrifice of her career to care for their disabled son, and he should expect a division close to equal, perhaps slightly in his favour.

*The power.* The court may divide matrimonial assets in such proportions as it thinks just and equitable (s 112(1) WC), treating marriage as an equal co-operative partnership of efforts (*NK v NL* [2007] 3 SLR(R) 743), with no presumption of equal division (*Lock Yeng Fun v Chua Hock Chye* [2007] 3 SLR(R) 520) (Pre-write 1-28).

*Step 1: the pool.* Matrimonial assets are (a) pre-marital assets ordinarily used by both parties or their children for shelter, transport, household or similar purposes, or substantially improved during the marriage by the other party or both, and (b) all other assets acquired during the marriage (s 112(10)). *USB v USA* [2020] 2 SLR 588 sets out four categories: quintessential matrimonial assets and the matrimonial home (entire value); transformed pre-marital assets (entire value); pre-marital assets that are neither (only the part paid during the marriage); and transformed gifts or inheritances (entire value) (Pre-write 1-29).
- *HDB flat:* bought during the marriage in joint names; entire value.
- *Aljunied apartment:* Vikram's pre-marital asset, but the family lived in it for about 2 years as their home, so it was ordinarily used for shelter and became a matrimonial asset; Mira's $20,000 renovation may also be substantial improvement. Its entire value goes into the pool, and its later letting does not undo that. This is the most important point against Vikram; he may argue for a discount given that he alone bought it before the marriage (the court raised the possibility of discounting in *TNC v TND* [2017] SGCA 34), but the default is full inclusion.
- *CPF accounts:* balances accumulated during the marriage (pre-marital balances are excluded unless used for matrimonial assets).
- *Car in Mira's name and each party's OCBC account* (including the rent Vikram kept): acquired during the marriage, so in the pool whatever the name; a spouse's belief that a sole-name asset is "his own" is a common mistake (FL6 s13).
- *Dates:* assets are identified at Interim Judgment (July 2025) and valued at the ancillary hearing, with bank and CPF balances at the Interim Judgment date (*ARY v ARX* [2016] SGCA 13; *BPC v BPB* [2019] SGCA 3) (Pre-write 1-31). Both must make full and frank disclosure (Pre-write 1-37).

*Which approach.* The parties both worked for about 12 of the 15 years, so this is a dual-income marriage, and the *ANJ* approach applies, not the equal-division approach for long single-income marriages in *TNL v TNK* [2017] 1 SLR 609 (Pre-write 1-34). The global methodology is appropriate (Pre-write 1-32).

*Step 2: ANJ.* (1) Direct contributions: equal for the HDB capital payment and for the mortgage over 12 years, then Vikram alone for 3 years; Vikram's Aljunied apartment at its full value, less credit to Mira for her $20,000 renovation; CPF and bank balances according to each party's own accounts; the car's purchase as evidenced. Because Aljunied is unencumbered and wholly his, the direct ratio will be well in Vikram's favour, say about 65:35. (2) Indirect contributions: for 12 years both worked and shared the household; for the last 3 years Mira has given up an $8,000-a-month HOD career to care full-time for a severely disabled child, while Vikram's support continued. Courts lean towards a homemaker who sacrificed her career to raise the children, as opposed to engaging a helper (FL6 s20), so the indirect ratio is likely to favour Mira, say 35:65. (3) Average: in a 15-year marriage with young children, equal weight is reasonable: about 50:50. (4) Adjustments under s 112(2): the needs of the minor children, especially the younger child's lifelong needs, who will live with Mira (s 112(2)(c)); Vikram's sole servicing of the mortgage since Mira stopped work (s 112(2)(a)); the use of rent from his apartment to service the HDB loan (s 112(2)(a)). Conduct is irrelevant unless gross (s 112(2)(h)) (Pre-write 1-33). The approach is applied with a broad brush (*UYQ v UYP* [2020] 1 SLR 551).

*Practical outcome.* Mira, with care and control of a child in a wheelchair, may wish to keep the HDB flat, which already houses the family; Vikram may prefer to keep Aljunied and its rental income. The court will consider who can afford to keep the flat and the CPF refund and HDB eligibility consequences (FL6 s39–40).

Therefore Vikram should expect the pool to include the Aljunied apartment at full value, and an overall division close to 50:50 (perhaps slightly in his favour on direct contributions), with Mira likely to keep the HDB flat and Vikram possibly the Aljunied apartment, balanced by cash or CPF.

### 1.VII.7 — Long single-income marriages; trends in proportions

**Q2022F-1e** · `1.VII.7` `1.VII.6` `1.VII.10` · PYP 2022 FAM Q1 (division: proportions) · not mark-weighted · `pcp-w-1-34` `pcp-w-1-33` `pcp-w-1-37`

*Facts: PYP 2022 Family, under 1.I.2 above.* Cherry fears that her lack of employment and her lack of knowledge of Daniel's finances will put her at a disadvantage. Advise her on the likely division.

**Answer.**

The issue is how the pool will be divided between Cherry, a homemaker for 16 of 20 years, and Daniel, the sole breadwinner. This is a long, essentially single-income marriage, in which the courts do not apply the *ANJ* approach but incline towards equal division (*TNL v TNK*); and Daniel's refusal to disclose his investments exposes him to an adverse inference. Her unemployment is not a disadvantage in this framework.

*Long single-income marriages.* In long single-income marriages the *ANJ* approach tends to favour the earning spouse, so the courts look instead to precedent, which inclines towards equal division (*TNL v TNK* [2017] 1 SLR 609). Court of Appeal decisions on long marriages hover around equal division or within about 10% of it (*Lock Yeng Fun v Chua Hock Chye* [2007] 3 SLR(R) 520; *BOR v BOS* [2018] SGCA 78), and homemakers in long marriages often receive 40–50%. "Single-income" includes cases where the homemaker made some financial contribution (*UBM v UBN* [2017] SGHCF 13, per Cyril), so Cherry's work from 2002 to 2006 and her S$20,000 towards Bukit Timah do not change the classification. The exception is an extraordinarily large pool built by one spouse's exceptional efforts (*Yeo Chong Lin v Tay Ang Choo Nancy* [2011] 2 SLR 1157, 65% to the husband of a 49-year marriage with a S$69m pool) (Pre-write 1-34). Daniel's investments may be substantial, but they were built during a marriage in which Cherry gave up her career at his insistence to raise three children, including his son; this is not *Yeo Chong Lin*.

*Daniel's non-disclosure.* Both parties must make full and frank disclosure (*USB v USA* [2020] 2 SLR 588). An adverse inference may be drawn where there is a substratum of evidence establishing a prima facie case and the person had particular access to the information (*BPC v BPB* [2019] 1 SLR 608 at [60]). Daniel earned over S$40,000 a month, invested heavily and profitably, says he has enough for the family "for many more years", and refuses to give any details: a clear prima facie case, with the information in his hands alone. Cherry should first seek disclosure orders (Part 9 FJ(G)R); if he still fails to disclose, the court may quantify the hidden assets and add them to the pool, or award her a higher share of the known assets (uplift) (*UZN v UZM* [2021] 1 SLR 426) (Pre-write 1-37).

*Her own disclosure.* Her position depends on her being candid: if she conceals the POSB account, she invites the same inference against herself (Q2022F-1f).

*Conduct.* Daniel's affairs do not affect division unless they amount to gross misconduct (s 112(2)(h)); neither does her chair incident (Pre-write 1-33).

Therefore Cherry can expect close to an equal share of the pool (around 45–50%), possibly more if the court draws an adverse inference against Daniel, provided she fully discloses her own assets.

### 1.VII.8 — Pre- and post-nuptial agreements; consent orders (non-core)

**Own question F10 facts.** Quinn and Ray married in Country Z in 2012 after signing a pre-nuptial agreement, each with independent legal advice, that each would keep the assets in his or her own name on divorce. They moved to Singapore in 2014. Since then they have had three children, and Quinn gave up her career in 2016 to look after them; most assets acquired since are in Ray's name. Ray says the agreement means Quinn gets nothing.

**Q1-F10-1** · `1.VII.8` `1.VII.6` · own question · 6 marks · `pcp-w-1-35` `pcp-w-1-33`

Advise Quinn on the effect of the pre-nuptial agreement.

**Answer.**

The issue is whether the pre-nuptial agreement binds the court in dividing the assets. It does not: it is not void, but it is not enforceable in itself; it is a relevant factor under s 112(2)(e) WC that may carry significant weight, and here its weight is reduced because the circumstances have changed fundamentally since it was signed.

The court must have regard to any agreement between the parties on the ownership and division of matrimonial assets made in contemplation of divorce (s 112(2)(e) WC). Pre-nuptial agreements are not void and can carry significant, even critical, weight, but they are relevant factors, not enforceable on their own terms; they may be given effect by incorporating them into a consent order, and the court retains its discretion under s 112 (*TQ v TR* [2009] 2 SLR(R) 961) (Pre-write 1-35).

In Ray's favour, both had independent legal advice and the agreement is clear. In Quinn's favour, it was made in 2012, before the move to Singapore, before three children were born, and before she gave up her career; since 2016 her contribution has been as a homemaker, and nearly all the assets acquired since are in Ray's name only because he was the earner. Applying the agreement literally would ignore her indirect contributions, which the *ANJ* framework (or, in a long single-income marriage, the equal-division approach) requires the court to recognise (Pre-write 1-33). The court is therefore likely to give the agreement limited weight.

If the parties settle, the agreed division can be recorded in a consent order; consent orders are encouraged, and are varied or set aside only in limited circumstances (*Surindar Singh v Sita Jaswant Kaur* [2014] 3 SLR 1284; *AYM v AYL* [2013] 1 SLR 924; *AOO v AON* [2011] 4 SLR 1169; *BMI v BMJ* [2018] 1 SLR 43).

Therefore Ray is wrong that Quinn gets nothing: the agreement is one factor under s 112(2)(e), weakened by the change in their circumstances, and the court will divide the assets justly and equitably in light of her contributions as homemaker.

**Own question F13 facts** (non-core; not from a past paper). Hana (Japanese) and Tom (Singaporean) married in Tokyo in 2010 after signing, each with independent Japanese lawyers, a pre-nuptial agreement under Japanese law that on divorce each keeps the property in his or her own name and that the children will live with Tom. They lived in Singapore from 2011 to 2024; Hana gave up her career in 2013 to raise their two children, and Tom bought a condominium in his sole name in 2015, which they lived in, and built up his CPF and bank savings here. In 2024 Hana returned to Tokyo with the children with Tom's agreement. In March 2026 a Tokyo court granted a divorce, recognised in Singapore, but made no order on the Singapore property; Japanese law gave Hana a right to claim a division of property, but its limitation period expired while she was ill. Tom, still living in Singapore, relies on the agreement.

**Q1-F13-1** · `1.VII.1` `1.VII.8` `1.VII.2` · own question, not from a past paper · 10 marks · `pcp-w-1-28` `pcp-w-1-35` `pcp-w-1-29`

Advise Hana whether she can claim a share of the Singapore assets and what effect the pre-nuptial agreement will have.

**Answer.**

The issue is whether Hana can obtain a division of the Singapore assets after a Japanese divorce, and whether the pre-nuptial agreement prevents it. She may apply under Chapter 4A of the Women's Charter with the court's permission; she is likely to show substantial ground and that Singapore is the appropriate forum. The agreement is not enforceable in itself; it is a factor that may carry significant weight, but its weight is reduced here by the change in the parties' circumstances, and its term on the children is presumed unenforceable.

*Chapter 4A.* Where a marriage has been dissolved by proceedings in a foreign country and the divorce is entitled to recognition in Singapore, either party may apply for an order for financial relief (s 121B WC). The court has jurisdiction if one party was domiciled in Singapore, or habitually resident here for a continuous year, on the date of the application for permission or of the foreign divorce (s 121C): Tom, a Singaporean living here since 2011, satisfies this. No application may be made without the court's permission, which is not granted unless there is "substantial ground" for it (s 121D(1)–(2)). Before making an order the court must be satisfied that Singapore is an appropriate forum, having regard in particular to the parties' connection with Singapore and with Japan, any financial benefit Hana has received, any foreign order, any right she had to apply abroad and why she did not use it, the availability of assets here, enforceability and the time elapsed (s 121F(2)). If so, the court may make any order it could make under s 112 as if the divorce had been granted here (s 121G(1)) (*UFN v UFM* [2019] 2 SLR 650) (Pre-write 1-28).

Hana has a strong case for permission and forum: the family lived in Singapore for 13 years; the condominium, CPF and savings are all here, so an order is enforceable; the Tokyo court made no order on them; she has received nothing; and she can explain why her Japanese claim lapsed (her illness). She applied within months of the divorce. Japan's connection, and her lapsed right there, are the points Tom will raise (s 121F(2)(b), (f)).

*The pool.* The condominium, bought during the marriage and used as the family home, and Tom's CPF and savings acquired during the marriage, are matrimonial assets regardless of whose name they are in (s 112(10)(b); *USB v USA* [2020] 2 SLR 588) (Pre-write 1-29).

*The pre-nuptial agreement.* The court has regard to any agreement on ownership and division made in contemplation of divorce (s 112(2)(e), applied by s 121G(2)). A valid foreign pre-nuptial agreement is not void, and its validity is governed by its proper law (*TQ v TR* [2009] SGCA 6 at [32]); here, Japanese law, under which Hana should check with Japanese counsel that it is valid. But it "cannot be enforced, in and of itself" ([77]), it cannot detract from the court's ultimate power under s 112 ([73]), and there is "no blanket rule" that it must be enforced to the exclusion of other circumstances ([80]); depending on the circumstances it may carry significant or even critical weight (*TQ v TR*). In Tom's favour, both had independent legal advice and the agreement is clear. In Hana's favour, it was made before the move to Singapore and before the children were born, she then gave up her career for 11 years, and the assets in Tom's name reflect his earnings while she kept the home; applying it literally would ignore her indirect contributions, which the court must recognise (Pre-write 1-33). The court is therefore likely to give it some, but reduced, weight. The term that the children live with Tom is presumed unenforceable unless clearly shown to be in their interests; their welfare decides (*TQ v TR* at [70]) (Pre-writes 1-35, 1-17).

Therefore Hana should apply for permission under s 121D, showing substantial ground and addressing the s 121F factors, and then seek a just and equitable division of the condominium, CPF and savings under s 121G; the pre-nuptial agreement will be a factor against her but is not binding, and its weight is reduced by the children, her career sacrifice and the 16 years since it was signed.

### 1.VII.9 — Third-party interests in alleged matrimonial assets (non-core)

**Q2022F-1d** · `1.VII.9` `1.VII.2` `1.VII.3` · PYP 2022 FAM Q1 (division: the pool) · not mark-weighted · `pcp-w-1-36` `pcp-w-1-29` `pcp-w-1-30`

*Facts: PYP 2022 Family, under 1.I.2 above.* Advise Cherry which assets will form the pool of matrimonial assets, including the Ang Mo Kio house registered in the names of Daniel and his parents.

**Answer.**

The issue is which assets are matrimonial. Every asset acquired by either of them during the marriage is in the pool, regardless of name; Daniel's interest in the Ang Mo Kio house is also in, because it was their home, but his parents' interest is not, and the court cannot decide their rights; and Daniel's gifts to Cherry need separate treatment.

*Assets acquired during the marriage.* All assets acquired during the marriage by one or both parties are matrimonial (s 112(10)(b) WC; *USB v USA* [2020] 2 SLR 588) (Pre-write 1-29): the Bukit Timah apartment (joint names, 2012); the Maserati; Daniel's Citibank accounts, shares and CPF accumulated during the marriage; his watches, wine and country club membership (so far as acquired during the marriage and of value); Cherry's POSB account and CPF; the BMW; and the joint OCBC account.

*The Ang Mo Kio house.* It was registered in the names of Daniel and his parents and fully paid before the marriage, but the couple lived there as their home after the marriage, and Cherry spent S$30,000 renovating it. Daniel's interest is a pre-marital asset ordinarily used by the family for shelter, so it is a matrimonial asset at its full value (s 112(10)(a)). His parents' interest is not. The Family Justice Courts can divide only as between the spouses; s 112 does not allow them to determine a third party's rights or to order the sale or transfer of a third party's interest (*UDA v UDB* [2018] 1 SLR 1015). If the size of Daniel's share is disputed, the options are to obtain his parents' confirmation of their share and an undertaking, to have the dispute resolved in separate proceedings (with the s 112 proceedings stayed), or, if both spouses agree and the house is not the main asset, to ask the court to decide only Daniel's share, which would not bind his parents (Pre-write 1-36).

*Gifts from Daniel.* Gifts and inheritances are excluded from the pool unless they are the matrimonial home or substantially improved (s 112(10)) (Pre-write 1-30). But the watches, handbags and possibly the BMW were gifts from Daniel to Cherry, and pure inter-spousal gifts are treated differently from gifts by third parties (*Wan Lai Cheng v Quek Seow Kee* [2012] 4 SLR 405), while small gifts may be disregarded as de minimis (*Yeo Gim Tong Michael v Tianzon Lolita* [1996] SGCA 14). Cherry should list them with values and expect Daniel to argue they remain in the pool. These are non-core points.

*Disclosure.* She must disclose her POSB account (Q2022F-1f), and seek disclosure of Daniel's investments (Q2022F-1e) (Pre-write 1-37).

Therefore the pool includes Bukit Timah, Daniel's share of the Ang Mo Kio house, the cars, all bank and investment accounts and CPF accumulated during the marriage, and Daniel's collections, with the parents' share of Ang Mo Kio left out and the inter-spousal gifts open to argument.

### 1.VII.10 — Full and frank disclosure and adverse inferences

**Q2022F-1f** · `1.VII.10` · PYP 2022 FAM Q1 (Cherry's POSB account) · not mark-weighted · `pcp-w-1-37`

*Facts: PYP 2022 Family, under 1.I.2 above.* Cherry would like, if possible, to stay silent about her POSB account, which holds about S$240,000 that Daniel does not know of. Advise her.

**Answer.**

The issue is whether Cherry may keep the POSB account out of the proceedings. She may not: she must disclose it, I cannot help her conceal it, and concealment would harm her case far more than disclosure.

*Her duty.* Both parties must make full and frank disclosure of their means and assets (*USB v USA* [2020] 2 SLR 588). The account was built from household money Daniel provided during the marriage, so it is a matrimonial asset that must be listed in her ancillary affidavit (Pre-write 1-6).

*The risk of concealment.* An adverse inference may be drawn where there is a substratum of evidence of non-disclosure and the party had particular access to the information (*BPC v BPB* [2019] 1 SLR 608 at [60]). The transfers came from the joint OCBC account, whose statements Daniel can obtain; once discovered, the court may quantify the concealed sum and add it to the pool, or give Daniel a higher share of the known assets (*UZN v UZM* [2021] 1 SLR 426). It would also destroy her credibility, and with it her strongest argument: that Daniel is the one hiding assets (Q2022F-1e).

*My position.* I must inform her of her duty to be truthful to the court and to comply with legal requirements (r 10(2) PCR); I must, so far as I can, prevent her from suppressing evidence and not assist in it (r 10(3)(a)); and I must not knowingly assist or permit her to mislead the court (r 10(6)(a)). If she insisted on omitting the account from a sworn affidavit, I could not act on that instruction, and if she gave false evidence I would have to cease to act or not perpetuate it (r 10(4)) (Pre-write 1-37).

Therefore I would advise Cherry that the POSB account must be disclosed; she can explain that it came from careful household budgeting, but hiding it would expose her to an adverse inference and would end my ability to act for her.

### 1.VIII Protection against family violence

Sub-points 1.VIII.1–1.VIII.4. Tested: 1.VIII.1 and 1.VIII.2 (2021, 2022, 2023, 2025), 1.VIII.3 (2025, and 2021 below). Own question F11 covers 1.VIII.4. Past papers before 2025 refer to the old s 65 WC; answers apply the new Part 7 (in force 2 January 2025).

### 1.VIII.1 — Scope of Part 7; family member; who may apply

**Q2023-4-2** · `1.VIII.1` `1.VIII.2` `1.VIII.3` · PYP 2023 Q4.2 · 4 marks · `pcp-w-1-38` `pcp-w-1-39` `pcp-w-1-40`

*Facts: PYP 2023 Family Q4, under 1.IV.4 above.* Jenny wants to know how she can protect herself against future violence from John. Advise her on an application for a Personal Protection Order and its likelihood of success.

**Answer.**

The issue is whether Jenny can obtain a protection order against John. She has standing, the vase incident is likely to be family violence, and the order is likely to be granted if she shows it is necessary, which turns on whether she and John still live together and whether their conflict is unresolved.

*Standing.* John is her spouse, a "family member" (s 58A(a) WC), and as an adult she applies for herself (s 60(2)(c)). Part 7 (in force 2 January 2025) replaced the old s 65 (Pre-write 1-38).

*The test.* The court may make a protection order if satisfied on a balance of probabilities that family violence has been committed or is likely to be committed against her, and that the order is necessary for her protection (s 60A). Family violence includes physical abuse (conduct causing or threatening personal injury or physical pain) and emotional or psychological abuse (conduct that torments, intimidates or distresses); a single instance suffices (s 58B(1), (4)–(5)) (Pre-write 1-39).

*Family violence.* John threw a vase against the wall during a quarrel, and a shard scarred Jenny's face permanently. He says it was an accident and he never meant to hurt her. But throwing a vase in anger in her presence was his deliberate act, it caused her personal injury, and it was intimidating; it is likely to be physical and emotional abuse. It was not self-defence.

*Necessity.* The court considers whether the parties still live together or will be in contact, whether the cause of the conflict is resolved, the severity of the incident, and the respondent's attitude (FL7 s10). For Jenny: they still live together, the quarrels over the affair continue, and the injury was serious and permanent. For John: a single incident, not aimed at her, followed by genuine remorse. On balance an order is likely, especially while they share a home.

*Other orders.* If there is a danger of violence while the application is pending, she may seek an expedited order (s 61), and with it a domestic exclusion order excluding John from the home regardless of title (ss 60B(2)(a), 61A); a counselling order for both is also possible (s 60E) (Pre-write 1-40).

Therefore Jenny is likely to succeed, particularly if they continue to live together; she should apply for a protection order and consider an expedited order and a domestic exclusion order.

### 1.VIII.2 — The two-stage test: family violence and necessity

**PYP 2025 Family Q4 facts.** Your new client, Chun Li, has just been served with an application for a Protection Order filed by her husband, Ryu, for himself and their 6-year-old child. About a week ago, after she discovered Ryu had been unfaithful with a mutual friend, a quarrel erupted; in anger she slapped Ryu twice on the face and threw various cutlery at him. One spoon ricocheted off the table and accidentally struck their child, causing a minor bruise on the cheek. Chun Li says this was not typical of her and she was emotionally triggered by the discovery. She is concerned that a Protection Order may be made, especially for her child, and how it might affect her intended divorce and the custody, care and control of the child.

**Q2025-4** · `1.VIII.2` `1.VIII.1` `1.V.3` · PYP 2025 Q4 · 5 marks · `pcp-w-1-39` `pcp-w-1-38` `pcp-w-1-19`

Advise Chun Li on Ryu's application for a Protection Order for himself and their child, and its likelihood of success.

**Answer.**

The issue is whether Ryu is likely to obtain protection orders for himself and the child. He has standing for both. The slaps are physical abuse of Ryu, and the child was injured during violence the child perceived, so the first stage is likely met for both; the real contest is necessity, where the isolated, provoked and out-of-character nature of the incident gives Chun Li a reasonable argument, stronger for the child than for Ryu.

*Standing.* Chun Li is Ryu's spouse and the child's mother, a family member of both (s 58A(a), (c) WC). Ryu applies for himself (s 60(2)(c)) and, as a family member of a child below 18, for the child (s 60(2)(a)(i)) (Pre-write 1-38).

*Stage 1: family violence.* The court must be satisfied on a balance of probabilities that family violence has been committed or is likely to be committed (s 60A). Physical abuse is conduct that causes or threatens personal injury or physical pain; a single instance suffices; and violence need not be directed at the family member if it can be perceived by him (s 58B(1), (5)–(6)). Force lawfully used in self-defence or in correcting a child is excluded (s 58B(2)(c); *TCV v TCU* [2015] SGFC 3). Slapping Ryu twice and throwing cutlery at him is physical abuse of Ryu; provocation by his infidelity does not make it self-defence. The spoon that struck the child was not aimed at the child, but throwing cutlery caused the child a bruise, and the quarrel was capable of being perceived by the child, so the court may well find family violence against the child too.

*Stage 2: necessity.* The order must be necessary for the family member's protection (s 60A). The court considers whether the parties still live together or are likely to be in contact, whether the original cause of conflict has been resolved, the severity of the incident, and the respondent's attitude to the violence (FL7 s10). In Chun Li's favour: a single incident a week ago, out of character, provoked by the discovery of the affair, with minor injuries and genuine remorse. Against her: the cause (the affair) is unresolved, divorce proceedings are imminent, and the parties will remain in contact over the child. On balance, Ryu's application for himself may succeed if they still live together; the child's is weaker, given that the injury was accidental and the child was not the target.

*Effect on divorce and custody.* A protection order is relevant to the child's welfare but not decisive on care and control, which is decided on the child's welfare as a whole (Pre-write 1-19). The fact relied on for divorce is unaffected.

*Advice.* Chun Li should show her remorse and the isolated nature of the incident, consider offering an undertaking not to use violence, and attend counselling (the court can order counselling under s 60E in any event) (Pre-write 1-40). Therefore Ryu's application has a reasonable chance for himself, and a weaker one for the child; Chun Li's best response is to demonstrate that an order is not necessary.

**Q2022F-1g** · `1.VIII.2` `1.VIII.1` `1.V.3` · PYP 2022 FAM Q1 (Daniel's PPO application) · not mark-weighted · `pcp-w-1-39` `pcp-w-1-38` `pcp-w-1-19`

*Facts: PYP 2022 Family, under 1.I.2 above.* Advise Cherry on Daniel's application for a Personal Protection Order for himself and Calista, and whether it will affect her rights to the children, especially Calista.

**Answer.**

The issue is whether Daniel is likely to obtain protection orders for himself and Calista, and how that affects the children's arrangements. The chair incident is likely to be family violence against both, but Cherry has a real argument that an order is not necessary now that Daniel has lived apart for 8–9 months; an order would be relevant to, but not decisive of, Calista's care and control.

*Standing.* Cherry is Daniel's spouse and Calista's mother, a family member of both (s 58A WC). Daniel applies for himself (s 60(2)(c)) and, as a family member of a child below 18, for Calista (s 60(2)(a)) (Pre-write 1-38).

*Family violence.* Throwing a chair in Daniel's direction threatened him with injury and is physical abuse; it struck Calista, causing her to fall, and the violence was perceived by both twins, who were crying (s 58B(1), (5)–(6)). It was not self-defence or lawful correction (s 58B(2)(c)). The first stage is likely met for both (Pre-write 1-39).

*Necessity.* The court considers whether the parties still live together or will be in contact, whether the cause of conflict is resolved, its severity, and the respondent's attitude (FL7 s10). In Cherry's favour: it was one incident, in anger at discovering Daniel's second betrayal; she immediately went to Calista's aid; Daniel left that night and the parties have not lived together for 8–9 months; and there has been no further incident. Against her: the conflict is unresolved, Daniel's own threatening texts show continuing hostility, and the parties will be in contact over the children. Evidence of incidents after the application was filed is not considered at its trial (*Teng Cheng Sin v Law Fay Yuen* [2003] 3 SLR(R) 356) (Pre-write 1-41). An order for Daniel himself is unlikely to be necessary given the separation; for Calista, who lives with Cherry, the court will look closely at whether there is any continuing risk.

*Effect on the children.* An order would be relevant to the children's welfare but not decisive on care and control (Pre-write 1-19). Cherry has been the twins' primary carer; she should show remorse, offer an undertaking and attend counselling, which helps both the PPO and the children's case. Daniel's application may be tactical, given his texts about fighting her over the children; but Cherry should respond calmly, in keeping with the therapeutic justice approach (Pre-write 1-1).

Therefore Daniel's application may well fail on necessity, particularly for himself; for Calista the court will weigh the risk carefully, and Cherry should demonstrate that the incident was isolated, which also protects her position on care and control.

### 1.VIII.3 — Other orders: expedited, exclusion, stay away, no contact, counselling, MTO, monitoring, removal

**Q2021F-1e** · `1.VIII.3` `1.VIII.1` `1.VIII.2` · PYP 2021 FAM Q1 (PPO) · not mark-weighted · `pcp-w-1-40` `pcp-w-1-38` `pcp-w-1-39`

*Facts: PYP 2021 Family, under 1.I.2 above.* Advise Christine on the possibility and likelihood of success of an application for a Personal Protection Order.

**Answer.**

The issue is whether Christine can obtain a protection order against Ken and what other orders she can seek. Her application is strong: two serious assaults, one causing hospitalisation, and continuing contact over the children make an order necessary; she can also seek stay away and no contact orders, an expedited order if there is danger pending the hearing, and counselling.

*Standing.* Ken is her spouse, a family member (s 58A(a) WC), and she applies for herself (s 60(2)(c)) (Pre-write 1-38).

*Family violence.* In January 2021 Ken slapped, punched and kicked her, putting her in hospital; on 29 June 2021, drunk, he physically abused her again. Each is physical abuse (s 58B(1)); his verbal abuse and his exclusion of her from her daughter may also be emotional or psychological abuse, conduct that torments or distresses (s 58B(4)). That she did not pursue a police report in January does not prevent her relying on the incident now (Pre-write 1-39).

*Necessity.* The violence is repeated, severe, and linked to drinking and his losses, none of which is resolved; Ken once tracked her down at Bukit Timah, and the parties will be in contact over the twins. An order is plainly necessary (s 60A).

*Other orders.* (1) An expedited order, made while the application is pending if there is a danger of family violence in the meantime; it takes effect on service and lasts 28 days unless extended (s 61(2)). (2) A stay away order (for example from the Bukit Timah property and her place of work) and a no contact order (s 60B), which may accompany an expedited order (s 61A); a domestic exclusion order is not needed since she lives apart. (3) A counselling order for Ken, or both, for up to 36 months (s 60E). (4) If his drinking reflects a psychiatric condition contributing to the violence, the court could consider a mandatory treatment order after assessment (s 60F). Electronic monitoring and removal orders need a protector's application and are for exceptional cases (ss 60C, 60D) (Pre-write 1-40).

*Procedure and breach.* She files a complaint in the prescribed form (online through iFAMS or at the Family Protection Centre), meets a Court Family Specialist, and a duty judge confirms her account and may issue a summons and make an expedited order. A knowing breach of an order is a family violence offence punishable with a fine of up to $10,000 and imprisonment of up to 12 months (18 months if aggravated) (s 63C), and is arrestable (s 63D) (Pre-write 1-41).

Therefore Christine's application is likely to succeed; she should file now, seeking an expedited order with stay away and no contact orders and a counselling order for Ken.

### 1.VIII.4 — Breach, variation and revocation; procedure and trial

**Own question F11 facts.** In 2025 Mia obtained a protection order and a no contact order against her husband Ned. Last week Ned phoned her repeatedly and waited outside her office. Separately, Mia's sister Sue wants to apply for a protection order against her own husband, and asks how to go about it. Mia also asks whether, if she and Ned reconcile next year after counselling, her order can be lifted.

**Q1-F11-1** · `1.VIII.4` `1.VIII.3` · own question · 8 marks · `pcp-w-1-41` `pcp-w-1-40`

Advise Mia and Sue.

**Answer.**

The issue is what follows Ned's breach, how a protection order application is made and tried, and whether an order can later be lifted. Ned's conduct is a family violence offence for which he may be arrested; Sue applies by complaint in the prescribed form in quasi-criminal proceedings; and Mia may apply to vary or revoke her order if circumstances change.

*Breach.* A person who knowingly contravenes a protection order, expedited order, exclusion, stay away, no contact or electronic monitoring order commits a family violence offence (ss 60A(6), 60B(9), 60C(9), 61(11), 61A(10) read with s 63C WC), punishable with a fine of up to $10,000 or imprisonment of up to 12 months or both, or up to 18 months if aggravated (s 63C(1)). It must be proved beyond reasonable doubt and is an arrestable offence (s 63D). Ned's repeated calls and waiting at her office breach the no contact order; Mia should make a police report. Unreasonable breach of a counselling order or mandatory treatment order is a separate offence with a fine of up to $2,000 (ss 60E(8), (10), 60F(30)) (Pre-write 1-41).

*Procedure (Sue).* Applications are quasi-criminal and made in the same manner as a summons under the CPC (s 179A(4) WC; FJ(G)R). Sue files a written complaint in the prescribed form online (iFAMS), or at the Family Protection Centre, a Protection Specialist Centre or in person, giving particulars of the parties and of the latest and past incidents. She meets a Court Family Specialist; a duty judge confirms the truth of the contents and may dismiss the complaint, issue a summons, or make an expedited order if there is danger while it is pending (s 61). Both parties attend mentions: if the complainant is absent the case is struck off; if the respondent is absent it may proceed in his absence or a warrant of arrest may issue. The trial is in camera, the complainant and her witnesses first; disputed incidents after the application was filed are not considered at its trial (*Teng Cheng Sin v Law Fay Yuen* [2003] 3 SLR(R) 356), and children's evidence is treated with care (*QU v QV* [2008] SGDC 364) (Pre-write 1-41).

*Variation (Mia).* The court may vary, suspend or revoke a protection order and the related orders (s 60A(4); ss 60B(7), 60E(6), 61(7)), considering any change of circumstances and any counsellor's or psychiatrist's report, and whether the order is still necessary (s 60A(5)). If Mia and Ned reconcile and complete counselling without further incident, she can apply to vary or revoke the order; a counselling order survives revocation of the protection order (s 60E).

Therefore Mia should report Ned's breach to the police now; Sue should file a complaint in the prescribed form and ask the duty judge for an expedited order if she is in danger; and Mia may apply under s 60A(4)–(5) to lift her order if they genuinely reconcile.

---

# Part 2 — Drills

Timed practice sets built from the Part 1 questions. Each Drill lists its questions (answer them from the question text in Part 1, with the answer covered), a time limit and the marking points. **Timing:** the paper gives 120 minutes for 100 marks, so the limits allow about 1.2 minutes per mark; reading time is included. **Marking:** score yourself against the marking points (one tick per point made with its authority and applied to the facts), then read the model answer. Points marked *(official)* come from the SQ or SQ22 answer guides; the rest are this project's own, drawn from the Pre-writes. Note each miss as a Weak Spot for Phase 2.

| Drill | Focus | Questions | Marks | Time |
|---|---|---|---|---|
| 1 | Crim: before charge, bail, pre-trial negotiations | QSQ-1-1, QSQ-1-2, Q2025-2-1, Q0-C3-1 | 23 | 28 min |
| 2 | Crim: pleading guilty, Newton hearing, TIC | Q2023-2-1, Q2023-2-2, Q2023-2-3 | 30 | 36 min |
| 3 | Crim: disclosure and admissibility | Q2022-1-1, Q2022-1-2 | 30 | 36 min |
| 4 | Crim: sentencing and appeals | Q2025-2-4, Q2021-1-5, Q2025-2-5, Q2021-2-3 | 30 | 36 min |
| 5 | Crim: untested Sub-points (own questions) | Q0-C4-1, Q0-C5-1, Q0-C7-1, Q0-C9-1, Q0-C10-1 | 42 | 50 min |
| 6 | Fam: jurisdiction, divorce facts, PPO | Q2023-3-1, Q2023-3-2, Q2023-4-1, Q2023-4-2, Q2025-4 | 20 | 24 min |
| 7 | Fam: children | Q2023-5-1, Q2023-5-2, Q2025-6 | 25 | 30 min |
| 8 | Fam: division of matrimonial assets | Q2023-6, Q2025-5 | 30 | 36 min |
| 9 | Fam: untested Sub-points (own questions) | Q1-F2-1, Q1-F4-1, Q1-F5-1, Q1-F8-1, Q1-F11-1 | 42 | 50 min |
| 10 | Full paper: PYP 2025 | all 2025 questions | 100 | 120 min |
| 11 | Full paper: PYP 2023 | all 2023 questions | 100 | 120 min |
| 12 | Long-form family advice (2021/2022 style) | Q2022F-1a to 1g | — | 60 min |

### Drill 1 — Before charge, bail and pre-trial negotiations · 23 marks · 28 minutes

**Questions:** QSQ-1-1 (5), QSQ-1-2 (5), Q2025-2-1 (5), Q0-C3-1 (8).

**Marking points.**

- **QSQ-1-1** *(official, 5)*: cannot advise destroying evidence, an offence under ss 204/204A PC [2]; a false statement to police is an offence under s 182 PC [1]; r 9(2)(g)–(h) PCR, no concocting evidence or contriving facts [1]; explain the s 22 CPC long statement and its use [1].
- **QSQ-1-2** *(official, 5)*: non-bailable, so bail is discretionary [1]; onus on Mr Loh (*Selvamsylvester*) [1]; considerations such as gravity of the offence and danger of absconding (*Yang Yin*) [2]; applying them to his job, mortgage and parents [1].
- **Q2025-2-1** (5): trespass (s 447) compoundable with the park, theft not; PP's consent after investigations; effect s 241(4)–(5) and *Teo Seng Tiong* [2]; without prejudice representations, *Glenn Knight*, s 182 statement [1.5]; withdrawal with stern (DAA) or conditional (DNAA) warning; warning not aggravating [1.5].
- **Q0-C3-1** (8): what a plea offer is; proceeded vs TIC charges, s 148 [2]; s 307(1) and asking to proceed on two charges [2]; reduction from s 380 to s 379 [1]; negotiating the SOF (elements not negotiable) and the sentencing position [2]; written instructions, no promises [1].

### Drill 2 — Pleading guilty, Newton hearing and TIC · 30 marks · 36 minutes

**Questions:** Q2023-2-1 (10), Q2023-2-2 (10), Q2023-2-3 (10). This is the whole of PYP 2023 Crim Q2.

**Marking points.**

- **Q2023-2-1** (10): "forgot to pay" denies dishonesty, the fault element of theft [2]; s 228(4) CPC, court must reject the plea [2]; *Md Rafiqul* [27] [2]; consequence: trial unless withdrawn; retraction needs valid and sufficient grounds [2]; r 14(5)(a)(i) advice; proper mitigation instead (and r 14(8) for the 2000 antecedent) [2].
- **Q2023-2-2** (10): relying on MDD is not a qualification [1]; contested fact material to sentence, s 228(5), Newton hearing (*Ng Chun Hian* [24]) [2]; burden on the Defence on a balance of probabilities (*Catherine Chan*) [2]; *Aniza* (withdraw, prove or call evidence) [1]; procedure: both psychiatrists testify [2]; effect if proved: deterrence reduced, rehabilitation (*Lim Ghim Peow*) [2].
- **Q2023-2-3** (10): s 148(1): consent of both sides, admission, no conviction [2]; s 148(4)–(5) record and bar on later trial [1]; usually enhances (*Mok Ping Wuen* [19]) [2]; less than conviction (*Lim Hsien Hwei* [22]) and the uplift method [25]–[27] [3]; application to the Coke Zero charge and the 5-day position [2].

### Drill 3 — Disclosure and admissibility of statements · 30 marks · 36 minutes

**Questions:** Q2022-1-1 (10), Q2022-1-2 (20). Same facts as SQ22, which has the only official key.

**Marking points.**

- **Q2022-1-1** *(official, 10)*: identifies *Kadar* and *Nabill* [1]; *Kadar* test, limbs (a) and (b) [2]; neutral or adverse material excluded [1]; Kelly's statement undermines identification (ponytail, tattoos), so disclose [2]; *Nabill*: material witness, disclose whether favourable, neutral or adverse [2]; Michael relevant to the alibi, so disclose [1]; timing with the CFP, continuing duty including appeals [1].
- **Q2022-1-2** *(official, 20)*: no warning of right to silence is not fatal (Explanation 2(d) s 258; *Mazlan*) [3]; s 258(1) starting point; Prosecution proves voluntariness beyond reasonable doubt (*Kelvin Chia* [53]) [3]; ancillary hearing, s 279 [2]; oppression, Explanation 1, *Tey Tsun Hang* [113] [3]; high threshold, *Tan Boon Tat*, *Fung Yuk Shing*, reasoned conclusion [3]; threat: objective and subjective limbs, likely exclusion [3]; CFD must state the objection (s 165(1)(d), Illustration 2); omission invites s 169(1)(c) inference; s 258A [3].

### Drill 4 — Sentencing and appeals · 30 marks · 36 minutes

**Questions:** Q2025-2-4 (9), Q2021-1-5 (10), Q2025-2-5 (6), Q2021-2-3 (5).

**Marking points.**

- **Q2025-2-4** (9): s 307(1): four terms, at least two consecutive, not all [2]; one-transaction rule and its test (*Shouffee* [27]–[34]) [2]; each night's trespass and theft one transaction, concurrent; nights separate [2]; totality, both limbs [2]; conclusion of 8 weeks [1].
- **Q2021-1-5** (10): s 307(1) forbids all-concurrent [2]; one-transaction test, similarity is not the test [2]; robberies on separate occasions, consecutive [2]; grievous hurt to Jerry: different interest and victim [2]; totality applied, *ADF* (not to minimise), judge justified [2].
- **Q2025-2-5** (6): no appeal against conviction after a plea (s 375); sentence appeal (s 374(4)) to the General Division [1]; NOA 14 days Form 66; Petition 14 days after GD, Form 67; lapse; s 378(6) [2]; bail and stay, ss 382–383, *Adith* (short sentence) [1]; threshold s 394, *PP v UI*, *Siew Boon Loong* [1]; risks: summary rejection (s 384), enhancement (*Wong Tian Jun De Beers*) [1].
- **Q2021-2-3** (5): out of time, s 377(2); sentence only (s 375) [1]; criminal motion under s 380, *Amarjeet Singh* [1]; *Tan Peng Khoon* factors applied [2]; stay or further deferment pending the motion (ss 318, 383) [1].

### Drill 5 — Untested Criminal Sub-points · 42 marks · 50 minutes

**Questions:** Q0-C4-1 (8), Q0-C5-1 (9), Q0-C7-1 (10), Q0-C9-1 (8), Q0-C10-1 (7). Own questions; no past paper has tested these points, so they are where an examiner could surprise you.

**Marking points.**

- **Q0-C4-1** (8): s 227(1)–(2)(b), advocate's confirmation [2]; *Balasubramanian* [25] nature and consequences [1]; s 375 no appeal against conviction [1]; fitness: s 247(1), (3), (4) [2]; s 248 findings and stay [1]; practical steps (psychiatric report, do not plead yet) [1].
- **Q0-C5-1** (9): SOF purpose and content (*Mok Swee Kok*, *Biplob*, *Andrew Koh*) [2]; element dispute → qualified plea, trial (s 228(4), *Md Rafiqul*) [2]; material fact → negotiate, Newton (s 228(5), *Ng Chun Hian*), burden on Prosecution for an aggravating fact (*Catherine Chan*) [3]; immaterial fact → plea stands (*Chota*) [2].
- **Q0-C7-1** (10): *Kadar* breach identified [2]; not a "poison pill"; *Lim Hong Liang* [21]–[22] factors [3]; unsafe conviction vs retrial (s 390(1)(b)(i)); irremediable prejudice [2]; NOA within 14 days; s 392 and *Ladd v Marshall* limbs [3].
- **Q0-C9-1** (8): s 230(1)(g) power to alter before calling on defence [2]; ss 128–129: explain, plea, readiness, adjournment or new trial [2]; s 131 recall on altered charge [2]; s 283; rebuttal s 230(1)(t) with cross-examination [2].
- **Q0-C10-1** (7): r 14(3)(c)–(d): reasonable grounds, inform client, arrange another practitioner [3]; s 230(1)(u)–(x) [1]; *Jagatheesan* [61], *GCK* [131], [134]–[135] [2]; application in closing [1].

### Drill 6 — Jurisdiction, divorce facts and protection orders · 20 marks · 24 minutes

**Questions:** Q2023-3-1 (3), Q2023-3-2 (2), Q2023-4-1 (6), Q2023-4-2 (4), Q2025-4 (5).

**Marking points.**

- **Q2023-3-1** (3): s 93(1) both limbs [1]; s 3(5) citizen deemed domiciled [1]; three-year bar passed; Mary's nationality and contest irrelevant [1].
- **Q2023-3-2** (2): s 94A: child below 21, completion before filing, certificate, applies to cross-application [1]; purpose; distinct from s 139I [1].
- **Q2023-4-1** (6): adultery elements, PI evidence [1]; s 95A(2): over 6 months living together, cannot rely [2]; behaviour, *Wong Siew Boey*, the vase and cumulative effect; s 95A(3) [2]; mutual agreement as alternative; separation not available [1].
- **Q2023-4-2** (4): standing ss 58A, 60(2)(c) [1]; s 60A two-stage test; s 58B physical and emotional abuse; single instance [1]; necessity factors applied [1]; other orders (expedited, DEO, counselling) [1].
- **Q2025-4** (5): standing for Ryu and the child [1]; family violence against Ryu (slaps) and child (s 58B(6) perceived; not self-defence) [1.5]; necessity factors both ways [1.5]; effect on custody: relevant, not decisive; advice (remorse, undertaking, counselling) [1].

### Drill 7 — Children · 25 marks · 30 minutes

**Questions:** Q2023-5-1 (3), Q2023-5-2 (7), Q2025-6 (15).

**Marking points.**

- **Q2023-5-1** (3): custody = major decisions (s 126) [1]; *CX v CY* / *ZO v ZP*: joint the norm, sole only exceptionally, acrimony not enough [1]; infidelity not abuse; likely joint [1].
- **Q2023-5-2** (7): welfare paramount (s 125(2)) [1]; sole, shared and split explained [1]; factors: status quo, young children and mother (*Soon Peck Wah*), siblings together; split rejected for twins (*AFK v AFM* contrast) [2]; access: *BG v BF* joint parenthood; supervised only exceptionally (*APE v APF*) [2]; Jenny cannot cut John off; interim access [1].
- **Q2025-6** (15): welfare test and *Tan Siew Kee* [1]; sole vs joint custody with *CX v CY* [3]; sole, shared and split care explained with *TAT v TAU*/*AQL v AQM* and *AFK v AFM* [3]; factors: unilateral status quo, siblings, young children, Michael's travel [3]; Joseph's resistance: s 130 report, judicial interview (*ZO v ZP*), no private assessment [2]; access for Michael (*BG v BF*) [1]; likely orders stated (joint custody, sole care to Deborah, liberal access) [2].

### Drill 8 — Division of matrimonial assets · 30 marks · 36 minutes

**Questions:** Q2023-6 (15), Q2025-5 (15).

**Marking points (each question).**

- s 112(1) power; *NK v NL* equal partnership; no presumption of equality (*Lock Yeng Fun*) [2].
- Identifying the pool: s 112(10), *USB v USA* categories, each asset classified; for Q2025-5 this includes the Aljunied apartment as a transformed pre-marital asset at full value, with the *TNC v TND* discount argument [3].
- Dates: Interim Judgment and AM hearing, bank and CPF at IJ (*ARY v ARX*; *BPC v BPB*) [1].
- Methodology: global, with reason [1].
- Which approach: dual-income → *ANJ* (not *TNL v TNK*), with reason [1].
- *ANJ* steps 1–3 applied with figures: direct, indirect, average and weighting [4].
- s 112(2) adjustments (children's needs, mortgage payments, rental) [2].
- Realistic outcome and practical points (who keeps the flat; disclosure) [1].

### Drill 9 — Untested Family Sub-points · 42 marks · 50 minutes

**Questions:** Q1-F2-1 (8), Q1-F4-1 (10), Q1-F5-1 (8), Q1-F8-1 (8), Q1-F11-1 (8).

**Marking points.**

- **Q1-F2-1** (8): FJ(G)R 2024 terminology; two stages [1]; Form 4 within 14 days and its uses [2]; Reply within 28 days [1]; AEICs, Form 101, Form 6, trial [1]; s 139I mediation; uncontested track possible [1]; Form 15 within 28 days of IJ; Part 9 disclosure; Form 17 [2].
- **Q1-F4-1** (10): void vs voidable; s 105 grounds; s 104; s 110(2) [2]; Anna: s 11, void; seek judgment; jurisdiction [2]; Chen: s 106(b), *Kwong Sin Hwa*; s 107(1) and (2) do not bar; *Heng Joo See* candour [3]; Eli: s 106(c) duress but s 107(2) 3-year limit; *Tan Ah Thee*; divorce instead [3].
- **Q1-F5-1** (8): s 95(2) three requirements; six facts [1]; desertion elements (s 92; FL3 s20) applied [3]; s 95A(4) two-month return: continuity kept, time not counted [2]; *William Cheng* and *Cheong Kim Seah*; flat concern not grave hardship [2].
- **Q1-F8-1** (8): s 69: married woman, neglect or refusal, not ancillary [2]; s 113 once filed; *Foo Ah Yan* [2]; s 117 duration and s 118 variation [2]; *Tan Bee Giok*; nominal orders after *ATE v ATD* [2].
- **Q1-F11-1** (8): breach is a family violence offence, s 63C penalties, arrestable s 63D, BRD [3]; procedure: complaint in prescribed form, CFS, duty judge, expedited order, mentions, trial in camera, *Teng Cheng Sin* [3]; variation or revocation s 60A(4)–(5); counselling order survives [2].

### Drill 10 — Full paper: PYP 2025 · 100 marks · 120 minutes

Sit it as the exam, in the order printed: Crim Q1 (Q2025-1-1 to 1-5, 30 marks), Crim Q2 (Q2025-2-1 to 2-5, 30 marks), Fam Q3 (Q2025-3-1, 3-2, 5 marks), Q4 (Q2025-4, 5 marks), Q5 (Q2025-5, 15 marks), Q6 (Q2025-6, 15 marks). Use only the Reference Pack; keep Part 1 of this file closed. This is the paper closest to 2026; if you want it unseen as a Practice Paper, do it before reading its Part 1 answers.

**Marking points** (Drills 1, 4, 6, 7 and 8 above give the points for Q2025-2-1, 2-4, 2-5, Q2025-4, Q2025-6 and Q2025-5; the rest are below).

- **Q2025-1-1** (7): s 354(1) non-bailable; s 93(1) discretion; onus (*Selvamsylvester*) [2]; s 95(1) no bar (not death or life) [1]; *Yang Yin* factors applied: Thailand ties as flight risk vs his conduct [2]; conditions: passport, no travel, tagging, higher sum, bailor; s 93(1A) personal bond [2].
- **Q2025-1-2** (6): s 159 and s 212; Magistrate's Court needs consent, s 159(3) [2]; gain: statement in CFP (s 162(1)(e)) or PSB (s 166(1)(a)), timelines [2]; cost: CFD (s 165), ss 169, 258A; advise opting in [2].
- **Q2025-1-3** (7): *Kadar* test [113], [117]; neutral/adverse excluded [2]; *Kadar II* knowledge; codified ss 221A, 221D [1]; application to CCTV (undermines or strengthens) [2]; timing and continuing duty; letter after the WP CCMS; ask the court; consequences of breach [2].
- **Q2025-1-4** (7): s 258 admissibility; TIPO; ancillary hearing s 279; burden BRD (*Teo Yeow Chuah*) [3]; tiredness and oppression threshold [1]; impeachment ss 147, 157(c) EA; *Muthusamy* steps; material discrepancy; *Loganatha* [3].
- **Q2025-1-5** (3): r 14(4): may continue, nothing inconsistent [1]; cannot say he is innocent; r 10(4) and r 26(5)(f) [1]; advise and record [1].
- **Q2025-2-2** (4): s 148(1) consent, admission, no conviction [1]; enhancement but less than conviction (*Mok Ping Wuen*, *Lim Hsien Hwei*) [2]; s 307 counts only proceeded charges [1].
- **Q2025-2-3** (6): presenting depression in mitigation with a report; s 228(1)–(3); r 14(2) [1]; not a qualification (she knew what she was doing) [1]; *Lim Ghim Peow* [1]; Newton hearing s 228(5) [1]; burden on Defence, balance of probabilities (*Catherine Chan*) [2].
- **Q2025-3-1** (2): s 93(1)(b) habitual residence, *Lee Mei-Chih* [1]; s 94A Co-Parenting Programme [1].
- **Q2025-3-2** (3): adultery elements and s 95A(2) applied to the 10 months and later acts [1]; alternatives: behaviour, mutual agreement [1]; fact does not affect custody or division [1].

### Drill 11 — Full paper: PYP 2023 · 100 marks · 120 minutes

Crim Q1 (Q2023-1-1, 1-2, 1-3: 30 marks), Crim Q2 (Q2023-2-1, 2-2, 2-3: 30 marks), Fam Q3 (Q2023-3-1, 3-2: 5 marks), Q4 (Q2023-4-1, 4-2: 10 marks), Q5 (Q2023-5-1, 5-2: 10 marks), Q6 (Q2023-6: 15 marks). Drills 2, 6, 7 and 8 give the points for Crim Q2 and all the Family questions.

**Marking points** for Crim Q1:

- **Q2023-1-1** (12): r 14(3)(b): opinion of guilt irrelevant, may act [3]; r 14(4) not engaged (no confession) [1]; r 5 duties, r 9(2)(g)–(h), no promises, attendance notes, separate witness interviews [3]; inconsistent accounts and the s 23 cautioned statement; how they will be used [2]; s 354(2) mental element; accident means he cannot plead guilty (s 228(4), *Md Rafiqul*) [2]; r 14(5)(a)(i) advice on plea, his decision [1].
- **Q2023-1-2** (12): statements distinguished (s 22, s 23); *Goldring* does not cover police statements [2]; s 162(1)(e) CFP and s 166(1)(a) PSB [3]; timelines ss 161(2), 163(1), 166(1) [2]; s 159, s 212; Magistrate's Court → opt in s 159(3); CFD cost (ss 165, 169, 258A) [3]; *Kadar* fallback [2].
- **Q2023-1-3** (6): caning under s 354(2) discretionary [1]; mitigation: remorse, testimonials, r 14(2) [2]; lack of antecedents neutral (*Chew Soo Chun*) [1]; s 325 CPC exemptions [1]; cautions: must not qualify the plea; no promises [1].

### Drill 12 — Long-form family advice (2021/2022 format) · 60 minutes

The 2021 and 2022 Family papers asked one question: advise on all issues in the divorce, the ancillary matters and the PPO. The 2026 paper splits these into short parts, but this drill trains the order of a full advice. Answer PYP 2022 Family Q1 as one advice, then check against Q2022F-1a to 1g; optionally add Q2022F-2 (Statement of Particulars, +20 min) and Q2022F-3 (mediation, +10 min).

**Marking points** (one or two marks each; aim to hit all):

- Jurisdiction (s 93(1)(a), s 3(5)); three-year bar passed; Co-Parenting Programme.
- Fact: 2006 adultery barred by s 95A(2); 2022 adultery available on PI evidence; behaviour as fallback.
- Children: Raymond a child of the marriage (s 92); welfare test; joint custody; twins' care to Cherry; Raymond's views at 16; siblings; access to Daniel (*BG v BF*); welfare report (s 130).
- Maintenance: s 69 now vs s 113 after filing (*Foo Ah Yan*); children's maintenance (ss 68, 69, 127; *WBU v WBT*); Raymond and s 70; Cherry's own claim (s 114; *ATE v ATD*).
- Pool: s 112(10); Ang Mo Kio (Daniel's share only; *UDA v UDB*); inter-spousal gifts (*Wan Lai Cheng*).
- Proportions: long single-income marriage (*TNL v TNK*); trends; adverse inference against Daniel (*BPC v BPB*; *UZN v UZM*).
- POSB: duty to disclose; PCR r 10; adverse inference risk.
- PPO: standing; family violence (chair; Calista perceived and injured); necessity after 8–9 months apart; effect on care and control.
- Therapeutic justice framing; r 15A; mediation.
