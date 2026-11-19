# ccp-2 — Progress (Phase 1)

Paper session `ccp-2`, 10–11 Nov 2026. Resume: read this file, then coverage.md and cheatsheets.md.

## Done
- coverage.md: Source key + Coverage List for all 4 Subjects (149 rows, 37 Topics), status table.
- cheatsheets.md: a Q&A Cheatsheet per Topic and an end-point block per Sub-point.
  - 0 IP: 0.I–0.XIII, blocks ccp-2-0-1..0-53 (56 rows).
  - 1 M&A: 1.I–1.X, blocks ccp-2-1-1..1-43 (46 rows).
  - 2 Competition: 2.I–2.VII, blocks ccp-2-2-1..2-25 (25 rows).
  - 3 Taxation: 3.I–3.VII, blocks ccp-2-3-1..3-22 (22 rows).
- Currency checks: statutes against course SSO copies (6 Jan 2025); tax rates and s 13W against IRAS;
  SIA/ANA, iNova/Mundipharma, Times/Penguin against the CCCS register (11 Nov 2026).
- Conflicts recorded in Source notes (e.g. CA s 308 numbering, s 13W sunset removed, Grab/Uber penalty,
  penalty duration rounding, SQ "global turnover" cap).

## Open verification flags
- none

## Known limits
- `Merger_Control_in_Singapore_(pages_69_to_97).pdf` (MCS) is scanned; read from rendered page images on 18 Nov 2026 and cited by page. Pp 69–97 cover thresholds and market definition only (new blocks `ccp-2-2-26`, `ccp-2-2-27`; Q2-21–Q2-23). The extract ends mid-sentence on p97 (captive sales).
- Taxation Learning Plan lists the exam as Wed 9 Dec 2026; SCHEMA puts Taxation in ccp-2 (Thu 10 Dec). Main session may want to confirm.

## Last --check
- 18 Nov 2026: passed; IP 56/56, M&A 46/46, Competition 27/27, Taxation 22/22; 145 blocks; 0 flags. PDFs not rebuilt (Bennett to review).
- 11 Nov 2026: passed; IP 56/56, M&A 46/46, Competition 25/25, Taxation 22/22; 143 blocks; 0 flags.

STATUS: DONE

## Model Q&A (Markdown only, 15 Nov 2026)
- `model-questions.md` built on Bennett's 14 Nov instruction. No PDF built (`--questions` waits for Phase 2).
- 207 questions: 94 real (40 SQ with the official key; 54 from the 2023 CCP Paper 2, transcribed from Examplify screenshots, with no key) and 113 own. 12 Drills: 9 by Topic, using all 207 once, and 3 mixed mocks. Timing is 2 min/Q.
- Sub-points: IP 62/62, M&A 49/49, Competition 35/35, Taxation 25/25 = 171/171. 0 TODO: verify (19 Nov 2026, after the audit fill).
- `check_model_qna.py ccp-2` exits 0, and `build_pack.py ccp-2 --check` passes. The builder's parse_questions finds 4 Subjects and 207 questions, every Key and end-point ID resolves, and every question has an Answer line.
- 2023 questions left out: Q22, Q33, Q37, Q48, Q53, Q54 (the reasons are in the file header).
- Three 2023 answers rest on the CCCS register rather than the course materials: Q41 Grab/Uber directions, Q42 LSEG/Refinitiv commitments, and Q36 (backed by the CL1 s6 slide). Two rest on elimination, where the sources contradict every other option: Q13 (I-Admin remedy) and Q28 (stamp duty paid upfront, per Cyril-TX §3.2.3).
- The earlier candidate's on-screen selections are wrong in places: Q3, Q8, Q27 (and others not flagged).
