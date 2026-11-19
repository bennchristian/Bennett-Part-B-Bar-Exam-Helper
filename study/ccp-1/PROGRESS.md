# ccp-1 — Progress

Phase 1 pack (Markdown only) for CCP MCQ 1, Wed 9 Dec 2026. Built 10–11 Nov 2026.

## Done
- coverage.md: Source key (shared + Subjects 0–3) and Coverage List — 0 Banking & Fundraising 9 Topics / 54 Sub-points;
  1 Corporate Governance 13 / 51; 2 Insolvency & Corporate Restructuring 14 / 68; 3 Admiralty 7 / 23. All 196 rows covered.
- cheatsheets.md: a Q&A Cheatsheet per Topic (43) and 196 end-point blocks (ccp-1-0-1…54, 1-1…51, 2-1…68, 3-1…23).
- All 2026 Sample Questions for CCP Paper 1 (Banking, CG, Insolvency, Admiralty; keys pp114, 116) are worked into the blocks.
- Statute/rule currency checked on SSO and the SGX Rulebook (11 Nov 2026): SFA, CA, IRDA, HCAJA, Listing Rules 210(2), 806.
  Corrections applied with `Conflict:` notes (CA s 131 period; SGX r 210(2)(a) S$10m; IRDA s 440 SDRP amendment).

## Notes for the main session
- The course's Listing Manual readings are image-only scans; rule text was read from Nic's Go Pack copy (Dec 2023) and
  updated from the 2026 slides (sustainability reporting, Rule 1207(10D)).
- Rescue financing (IRDA ss 67, 101) and ipso facto (s 440) are in the Learning Plan but not the slides; the blocks are
  taken from the statute.
- Admiralty SQ Q8 (key B) is explained by inference (alleged, unestablished termination of the demise charter); flagged
  in block 3-12's Source note; not an open item.

## Open items
- none

## Last --check
- 11 Nov 2026: `python3 tools/build_pack.py ccp-1 --check` — Check passed (196 rows, 196 blocks, zero open verify flags).

STATUS: DONE

## Model Q&A (Phase 2 item, Markdown only — Bennett, 14 Nov)
- 15 Nov 2026: model-questions.md built. 260 questions (139 real: SQ 40, 2023 CCP Paper 1 51, 2021 INS 32, ADM2 8, ADM1 8; 121 own), 14 Drills.
  196/196 Sub-points tagged; 0 TODO: verify. `check_model_qna.py ccp-1` exits 0; `build_pack.py ccp-1 --check` passes. No PDF built.
- Left out (see the file's "Left out" note): 2023 Q23, Q34, Q38, Q41, Q54, Q56 (Q42, Q44, Q53 not held); 2021 INS Q1, Q32, Q34, Q36.

## Audit fill (18–19 Nov 2026; Markdown only, no PDF — Bennett reviews first)
- From `audits/ccp-1-audit.md`. 16 new Sub-points and blocks: ccp-1-0-55 (cross-border loans); ccp-1-1-52…55 (new Topic 1.XIV,
  Listing Manual Chapter 12: Rules 1202–1206, 1207 incl. 1207(19), 1208–1212, read from page images of the scanned reading-list copy);
  ccp-1-1-56…59 (Code Principles 1, 5, 6–7, 11–13); ccp-1-2-69 (ss 315, 318, 323; Mohd Zain v Chimbusco); non-core blue Insolvency
  blocks ccp-1-2-70…75. Rothstar written into 2-48 (NIC-ANT), Mohd Zain into 2-8; s 440 block 2-63 sharpened (aircraft carve-out, winding up).
- Model Q&A: 277 questions (140 real, 137 own). Added 2021 INS Q34 (s 440, answer C from s 440(5)(e), (6); no official key) and own
  questions Q0-38, Q1-36…43, Q2-40…46 for the new Sub-points; Drills 1, 4–9 and 13 updated. No other real question exists for 1.I, 1.II,
  1.VI, 1.XIII or 3.V in any held source.
- About 33 blue Insolvency cases have no holding in any source and could not be read online; they are named, not stated, in the
  Source notes of 2-70…2-75 (syllabus: blue = not tested).
- 19 Nov 2026: `build_pack.py ccp-1 --check` passes (212 rows, 212 blocks); `check_model_qna.py ccp-1` 212/212; 0 TODO: verify.
