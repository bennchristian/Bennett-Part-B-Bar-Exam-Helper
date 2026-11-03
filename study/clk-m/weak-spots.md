# CLK-M — Weak Spots

A Weak Spot is a Sub-point where a Drill or the Practice Paper showed a gap, or where a lookup
in the Reference Pack failed (PRD FR-10).

Each one is fixed in the pack: a Flowchart end point, the contents page, or the keyword index.
The **Fix** column names the content ID that was changed. Recurring items go into the tracker's `notes` for `clk-m`
— the main session records them, on Bennett's word.

Built 2 Nov 2026, before any drill or Practice Paper had been sat.

## Log

Kinds: `wrong law`, `missed issue` or `failed lookup`. Fix: the content ID, plus what changed
(`keywords` / `title` / `body` / `chart` / `new block`).

| ID | Date | From | Coverage Key | Kind | Fix | Status |
|---|---|---|---|---|---|---|
| — | — | — | — | nothing sat yet | — | — |

## Source gaps — fix before exam week

1. **The DPCR AI-regulation topic (topic 0.X; coverage rows 0.X.1–3 are `TODO`) has no source in the library.** The learning plan lists the
   Model AI Governance Framework and the PDPA applied to AI [DP-Plan p4], but there is no deck
   for it. Download the slides from the 2 Nov DPCR Contact Session II from Campus (still not
   in the library on 3 Nov), and don't learn this topic from memory or seniors' notes.
2. **Law & Tech Contact Session 2 deck** (15 Oct) is missing from the folder; only the CS2
   lecture notes are there [LT-Plan p4].
3. **Statute currency.** The Go Pack copies (PDPA as at 1/10/2022, CYSA as at 11/4/2022, POHA
   as at 1/5/2023, ETA 2011 Rev Ed) may predate amendments. On 3 Nov 2026 the CYSA and the ETA
   were checked against Singapore Statutes Online (SSO-CYSA, SSO-ETA; approved by Bennett):
   - **CYSA: fixed.** Act 19 of 2024 (in force 31 Oct 2025) changed the Act in five ways:
     - it inserted Parts 3A–3C;
     - s 16A now covers third-party-owned CII (new block clk-m-0-69);
     - s 17 now covers systems of temporary cybersecurity concern (new block clk-m-0-70);
     - appeals moved to s 35B (clk-m-0-50 fixed);
     - s 7(1A) now reaches CII wholly outside Singapore, and s 14 reporting is wider
       (clk-m-0-46 and 0-48 updated, with `Conflict:` notes against DP-2).

     The Part 3 duties (ss 10, 13, 15, 16) and the Part 4 section numbers are unchanged.
   - **ETA: fixed.** Act 5 of 2021 removed negotiable instruments and documents of title from
     the First Schedule; they now fall under Part 2A on electronic transferable records. Act 16
     of 2021 excluded lasting powers of attorney from the trusts and powers-of-attorney item,
     with effect from 14 Nov 2022 (clk-m-1-24). The other ETA section numbers the pack cites
     are unchanged.
   - **PDPA: no block changes needed.** The only amendments since the Go Pack copy are s 48C
     (public-agency data sharing, 16 Oct 2026) and the deletion of Second Sch Part 3 para 3(a).
     Portability (Part 6B) is still not in force.
   - **POHA: fixed.** Act 23 of 2025 (29 Jun 2026) and Act 21 of 2025 (17 Aug 2026) changed
     clk-m-0-55 to 0-62 and 0-67, and added new block clk-m-0-71 (administrator orders), each
     with a `Conflict:` note against DP-3 and the Go Pack copy. The penalties and the names of
     the s 15A–15E orders are unchanged, so no Drill or mock-1 answer changes.
4. **Thai in-house privilege (clk-m-2-44): resolved 3 Nov 2026.** The slides [Cmp-4 p9], the
   official key [SampleQs p98 Q3, key p130] and Cyril [Cyril-Exam CMP §4.4.2] all say in-house
   lawyers are generally not protected. The 2019 Guide is more nuanced [Guide p10 Q13, p11 Q16].
   The conflict is recorded in the block; follow the slides and the key.
5. **FLPA ss 3–4 (clk-m-3-13): resolved 3 Nov 2026.** No library source goes beyond "limitation
   now mostly governed by the lex causae" [CoL-2 p22; CoL-Plan p4]. The official key applies
   the foreign period under s 3 [SampleQs p103 Q4, key p131]. The block now says exactly that
   and nothing more.
6. **Official sample-paper errata to be aware of** (the material on the slides is unaffected):
   - Conflicts Q1 is keyed D ("express governing law clause"), but the question mentions no
     clause. On the slides, Q1 would be decided by place of performance [SampleQs p102, key
     p131; CoL-2 p11].
   - Conflicts Q5's stem is mis-pasted from the Comparative section [SampleQs p103].

## High-risk traps (precise distinctions likely to become distractors)

**DPCR**
- The breach clock runs **3 calendar days from the assessment**, not from discovery.
- **Scale-only** breaches (≥500 individuals) go to the PDPC only, not to individuals.
- Individuals are notified **on or after** the PDPC, never before [PDPA s 26D].
- The penalty cap is 10% of Singapore turnover if turnover > $10m, otherwise $1m. It applies
  only to intentional or negligent breaches [PDPA s 48J].
- s 48O covers Parts 4–6B, **not Part 3**. Distress counts; loss of control alone does not
  (Reed).
- Legitimate interests, business improvement and deemed consent by notification **can't be
  used for marketing**.
- **Not** CII-owner duties: running the essential service. **Not** PDPA rights: erasure.
  **Not** POHA orders: a "specific correction order".
- CYSA **s 17 is now temporary-concern designation**, not appeals; appeals are **s 35B**
  (30 days). A third-party-owned CII designation (s 16A) falls on the **essential-service
  provider**, not the owner. Temporary designations last **at most 1 year**; CII designations
  last **5 years**.
- POHA since 29 Jun 2026: **"humiliation"** and **sexual or indecent** conduct count (ss 3, 4,
  6, 7). Sexual or indecent material with a **legitimate science, medicine, education or art
  purpose** is outside s 4. Penalties are unchanged: s 4 is still **fine only**.
- POHA orders can now be made against the **administrator** of a chat group, forum or page
  (ss 15CA, 15CB), but an administrator is **not** an internet intermediary.

**Law & Tech**
- Lessig's four modalities are law, norms, markets and architecture. "Regulations" is not one
  of them.
- Easterbrook says study general rules; he does not say cyberlaw is desirable.
- Collingridge is the author of the Collingridge dilemma — not Bennett Moses.
- B2C2: the **programmer's** knowledge counts, from programming to formation. The "reasonable
  trader" test is the dissent.
- Voller: **Fairfax, not Facebook**, was the publisher.
- PWA s 6 needs **all** limbs, and platform workers are **not** employees.
- ETA First Schedule: **bills of lading and negotiable instruments are no longer excluded**
  (since 2021, Part 2A electronic transferable records). A **lasting power of attorney** is
  outside the powers-of-attorney exclusion.

**Comparative**
- Indonesia's code has 4 books; Thailand's CCC has 6, with torts inside Book 2.
- Art 1342 is the clear-words rule; Art 1349 construes ambiguity against the party who
  requested the agreement.
- Thai CCC: s 14 makes the Thai text prevail; s 12 makes words beat figures; s 13 takes the
  lowest amount.
- Thai tort prescription (s 448): 1 year from knowledge, 10 years from the act.
- Relative competence is raised by exception and decided first. Absolute competence can be
  raised at any time.
- Ex aequo et bono **cannot override mandatory law**.

**Conflicts**
- The **burden flips**: on service in, D shows Singapore is not the natural forum; on service
  out, C shows Singapore is.
- Lex loci delicti for negligence is where the conduct happened, not where damage was
  suffered. For service-out damage, a company suffers loss at its **place of incorporation**.
- Exclusive clause → strong cause. Non-exclusive foreign clause → ordinary natural-forum test.
  Non-exclusive Singapore clause → strong cause.
- A foreign court's international jurisdiction rests only on the defendant having been the
  claimant, present, submitted, or bound by a clause. A PD 63-type nexus is not enough.
- Intrinsic fraud is a defence only on evidence the foreign court did not consider; extrinsic
  fraud is a defence even if it did.
