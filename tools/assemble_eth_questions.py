"""Assemble study/eth-w/model-questions.md from pyp-facts.md, drills.md and model-answers.md.

Usage: python3 tools/assemble_eth_questions.py [out-file]

model-answers.md stays the master copy of every answer: fix it there, re-run this, then
`python3 tools/build_pack.py eth-w --questions`. Question text lives in pyp-facts.md.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "study" / "eth-w"
MA = (ROOT / "model-answers.md").read_text().splitlines()
DR = (ROOT / "drills.md").read_text().splitlines()
COV = (ROOT / "coverage.md").read_text().splitlines()

# Key -> Pre-write IDs, and Key order
PW, ORDER = {}, []
for ln in COV:
    m = re.match(r"\| ([IV]+\.\d+) \| .*? \| .*? \| (.*?) \|$", ln)
    if m:
        ORDER.append(m.group(1))
        PW[m.group(1)] = re.findall(r"eth-w-0-\d+", m.group(2))

FACTS = {}
for f in ("pyp-facts.md",):
    cur = None
    for ln in (ROOT / f).read_text().splitlines():
        if ln.startswith("@@ "):
            cur = ln[3:].strip(); FACTS[cur] = []
        elif cur:
            FACTS[cur].append(ln)
FACTS = {k: "\n".join(v).strip() for k, v in FACTS.items()}


def section(heading, stop_extra=()):
    """Body of model-answers.md after the line equal to `heading`, up to the next ###/##/---/spoiler."""
    i = MA.index(heading) + 1
    out = []
    for ln in MA[i:]:
        if ln.startswith(("### ", "## ", "> **Spoiler")) or ln == "---" or ln in stop_extra:
            break
        out.append(ln)
    return "\n".join(out).strip()


def after_header(heading):
    """A '##' section's body after its 'Question: …' header paragraph."""
    body = section(heading)
    parts = body.split("\n\n", 1)
    return parts[1].strip() if parts[0].startswith("Question:") else body


def drill_block(start, stop_prefixes):
    i = DR.index(start) + 1
    out = []
    for ln in DR[i:]:
        if ln.startswith(stop_prefixes):
            break
        out.append(ln)
    return out


def split_calls(lines):
    """Bold call paragraphs ('**1.1 …**' or '**(a) …**', possibly over several lines) vs the facts."""
    facts, calls, cur = [], [], None
    for ln in lines:
        if cur is not None:
            if ln.strip():
                cur.append(ln.strip()); continue
            calls.append(" ".join(cur)); cur = None
        if re.match(r"\*\*(\d\.\d|\([ab]\))", ln):
            cur = [ln.strip()]
        else:
            facts.append(ln)
    if cur:
        calls.append(" ".join(cur))
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(facts)).strip()
    return text, calls


G = []  # (title, facts, [ (qid, keys, source, marks, call, answer) ])

def q(qid, keys, source, marks, call, answer):
    return dict(id=qid, keys=keys.split(), source=source, marks=marks, call=call, answer=answer)

H = lambda s: section(s)

# ---- 2025 ----
G.append(("2025 Q1 — Lumi, Kira and Hun Ter Law · PYP 2025 · 50 marks", FACTS["2025-1"], [
    q("Q2025-1-1", "II.1 II.2 II.3 II.10 II.15 II.17 II.18 II.7", "PYP 2025 Q1.1", "35 marks",
      "**1.1** Can K act for R and R's sister against B? Should K refrain from acting for R and R's sister against B? What are the relevant considerations? (35 marks)",
      H("### 1.1 Can K act for R and R's sister against B? Should K refrain? (35 marks)")),
    q("Q2025-1-2", "VI.1 VI.2 III.1 VII.3", "PYP 2025 Q1.2", "15 marks",
      "**1.2** Which or which portions, if any, of the proposed advertising statements can J use, and why or why not (15 marks)",
      H("### 1.2 Which of the proposed advertising statements can J use? (15 marks)")),
]))
G.append(("2025 Q2 — Skott, Xiao and Lone Wolf Law · PYP 2025 · 50 marks", FACTS["2025-2"], [
    q("Q2025-2-1", "V.1 II.8 II.9 II.6 II.7 III.2 IV.1", "PYP 2025 Q2.1", "25 marks",
      "**2.1** The conduct of S described at paragraphs 3–4 above (25 marks)",
      H("### 2.1 S's conduct at paragraphs 3–4 (25 marks)")),
    q("Q2025-2-2", "III.6 III.2 III.1 V.1 I.2", "PYP 2025 Q2.2", "25 marks",
      "**2.2** The conduct of S described at paragraphs 5–6 above (25 marks)",
      H("### 2.2 S's conduct at paragraphs 5–6 (25 marks)")),
]))
# ---- "2024" (practice sessions not matching any paper held) ----
G.append(("2024? PS1 Q2 — Seldon, Howwie and Emily · practice session 1; probably the 2024 paper", FACTS["ps1-2"], [
    q("QPS1-2", "II.1 II.14 II.15 II.17 II.18 II.19 II.26", "Practice Session 1 Q2 (course: all PS questions are past-year questions; no 2024 paper is held)", "not mark-weighted",
      "Critically evaluate all ethical issues arising from Seldon's and/or CT Law's proposed engagement to act for Lennard.",
      after_header("## PS1 Q2 — Seldon, Howwie and Emily")),
]))
G.append(("2024? PS2 Q1 — Zapp and Barbara's undertaking · practice session 2; probably the 2024 paper", FACTS["ps2-1"], [
    q("QPS2-1", "III.8 III.2 III.4 III.1 II.8 II.10 III.14", "Practice Session 2 Q1 (no 2024 paper is held)", "not mark-weighted",
      "Discuss and evaluate the following in relation to Zapp's ethical and professional obligations concerning Zapp's conduct in relation to Barbara's matter.",
      after_header("## PS2 Q1 — Zapp and Barbara's undertaking")),
]))
# ---- 2023 ----
CALL23 = ("Explain why or why not, and/or whether any additional safeguards or measures may be required on "
          "the part of TL and/or the legal practitioners involved.")
G.append(("2023 Q1 — Archie, Betty, Cheryl and the RPL facility · PYP 2023 (= 2026 Sample Questions (a)–(c)) · 50 marks", FACTS["2023-1"], [
    q("Q2023-1-1", "II.17 II.15 II.18", "PYP 2023 Q1.1; official key SQ p109–113", "18 marks",
      f"**1.1** whether Archie can act for L. {CALL23} (18 marks)",
      H("### 1.1 Can Archie act for L? (18 marks)")),
    q("Q2023-1-2", "II.12 II.10 II.15", "PYP 2023 Q1.2; official key SQ p109–113", "18 marks",
      f"**1.2** whether it was acceptable for Betty to act for M, assuming Archie continues to act for L. {CALL23} (18 marks)",
      H("### 1.2 Was it acceptable for Betty to act for M? (18 marks)")),
    q("Q2023-1-3", "II.12 II.13", "PYP 2023 Q1.3; official key SQ p109–113", "14 marks",
      f"**1.3** whether Cheryl can act for the DSA, assuming Archie continues to act for L and Betty continues to act for M. {CALL23} (14 marks)",
      H("### 1.3 Can Cheryl act for the DSA? (14 marks)")),
]))
G.append(("2023 Q2 — Yeager, Shigan Partners and KP's website · PYP 2023 · 50 marks", FACTS["2023-2"], [
    q("Q2023-2-1", "III.11 IV.10 II.14 II.18 II.25 II.8", "PYP 2023 Q2.1", "18 marks",
      "**2.1** Should Y cease to act for B [R] in the proceedings? (18 marks)",
      H("### 2.1 Should Y cease to act for R? (18 marks)")),
    q("Q2023-2-2", "III.12 II.19", "PYP 2023 Q2.2", "18 marks",
      "**2.2** Assuming Y ceases to act for B [R] in the proceedings, can A take over conduct of the matter and act for B [R] in the proceedings? (18 marks)",
      H("### 2.2 Can A take over conduct and act for R? (18 marks)")),
    q("Q2023-2-3", "VI.1 VI.2", "PYP 2023 Q2.3", "14 marks",
      "**2.3** Whether the statements on KP's website are permissible (14 marks)",
      H("### 2.3 Are the statements on KP's website permissible? (14 marks)")),
]))
# ---- 2022 ----
G.append(("2022 Section B — Luna, Marci and the Settlement Agreement · PYP 2022 (= PS2 Q2) · 40 marks", FACTS["2022-B"], [
    q("Q2022-B-a", "III.11 IV.10 II.8 II.1 II.2", "PYP 2022 Sect B (a); = PS2 Q2(a)", "12 marks",
      "**(a)** Can Luna and Marci act for Davion in the New Suit? (12 marks)",
      H("### (a) Can Luna and Marci act for Davion in the New Suit? (12 marks)")),
    q("Q2022-B-b", "III.12 II.19 II.18", "PYP 2022 Sect B (b)", "14 marks",
      "**(b)** Assume that Luna proposes that another litigation partner from Mid Law, Chen, immediately takes over conduct of the matter, with Luna and Marci ceasing to have any involvement – can Mid Law continue to act for Davion in the New Suit under this proposed arrangement? (14 marks)",
      H("### (b) Can Mid Law continue through Chen? (14 marks)")),
    q("Q2022-B-c", "IV.4 II.26 II.7", "PYP 2022 Sect B (c)", "14 marks",
      "**(c)** Assume that Davion decides (regardless of Luna's, Marci's and Chen's views on the preceding questions) to instruct a different law practice, Dire Law LLC, to take over the matter, and Mid Law delivers the original signed Settlement Agreement to Dire Law (per Davion's request). A few days later, Mid Law receives an email from Top Law reminding them of the undertaking previously given by Luna and which states that the fees which Davion owes to Top Law remain unpaid. Please advise Luna on whether there has been any potential breach(es) of her professional and ethical obligations in relation to the above, and if so, what should Luna have done instead? (14 marks)",
      H("### (c) The original Settlement Agreement and Top Law's lien (14 marks)")),
]))
# ---- 2021 ----
G.append(("2021 Q1 — Andy, Beth, Clara, Xavier and Vega Bank · PYP 2021 (= PS1 Q1) · 40 marks", FACTS["2021-1"], [
    q("Q2021-1-1", "II.8 II.12 II.1", "PYP 2021 Q1.1; = PS1 Q1.1", "12 marks",
      "**1.1** Clara is concerned whether Andy or Beth may have already breached one or more professional conduct rules in relation to Beth advising Vega Bank on the loan agreement two years ago. Please evaluate Andy's and Beth's liability, if any, in relation to Vega Bank and Delta Tech entering into the loan agreement two years ago. (12 marks)",
      H("### Q1.1 Liability for the loan two years ago (12 marks)")),
    q("Q2021-1-2", "II.1 II.10 II.12 II.13 II.15 II.17 II.19", "PYP 2021 Q1.2", "18 marks",
      "**1.2** Andy tells Beth and Clara that they must immediately decline Vega Bank's instructions, in order to preserve Andy's and the firm's working relationship with Xavier, and so that Andy can continue advising Xavier on various matters as he has done for the past 5 years. Beth says that if she has to decline Vega Bank's instructions, she will need to provide them with a reason why. Alternatively, Beth suggests that it may be possible for Andy to continue acting for Xavier, while Beth and Clara can act for Vega Bank. Please evaluate the approaches proposed by Andy and Beth in relation to their proposed representation of Xavier and/or Vega Bank, respectively. (18 marks)",
      H("### Q1.2 Andy's and Beth's proposals (18 marks)")),
    q("Q2021-1-3", "II.6 II.20 II.5", "PYP 2021 Q1.3", "10 marks",
      "**1.3** Xavier subsequently instructs Andy to advise him on the loan agreement against Delta Tech. Andy is concerned that Xavier may be upset if he finds out that Vega Bank contacted the firm recently about the loan agreement. After the meeting, unknown to Beth and Clara, Andy prepares a draft deed to be signed by Xavier, which provides that Xavier waives and release any claims against the law practice and its lawyers, and confirms that Xavier has no cause for any complaint against Andy or the law practice. He tells Xavier's personal assistant that he needs this signed for purposes of required routine reporting to the law practice's insurers (no such requirement exists). Being extremely busy, Xavier signs the deed when his personal assistant places it before him, and the signed deed is returned to Andy. Please evaluate Andy's conduct in relation to the deed signed by Xavier. (10 marks)",
      H("### Q1.3 The deed signed by Xavier (10 marks)")),
]))
G.append(("2021 Q2 — Fiona and Gary's ex parte worldwide Mareva · PYP 2021 · 30 marks", FACTS["2021-2"], [
    q("Q2021-2", "I.4 II.7 III.1 III.2 III.3 III.8", "PYP 2021 Q2", "30 marks",
      "Please discuss and evaluate Fiona's conduct in relation to the ex parte application for a worldwide Mareva injunction on behalf of Gary against ICPL. (30 marks)",
      H("### Q2 Fiona and the ex parte worldwide Mareva (30 marks)")),
]))
G.append(("2021 Q3 — Terms of engagement · PYP 2021 (3.1, 3.3–3.5 = PS3 Q1) · 30 marks", FACTS["2021-3"], [
    q("Q2021-3", "VII.4 VII.5 II.25 II.4 II.5 VI.4 VI.2", "PYP 2021 Q3.1–3.5; = PS3 Q1(i)–(iv)", "5 × 6 marks",
      "Evaluate each of terms 3.1 to 3.5 above.",
      H("### Q3 Terms of engagement (5 × 6 marks)")),
]))
# ---- 2020 ----
G.append(("2020 Q1 — Caitlyn, Yasuo and Teemo · PYP 2020", FACTS["2020-1"], [
    q("Q2020-1-a", "II.12 II.13 II.17 II.19", "PYP 2020 Q1(a)", "20 minutes",
      "**(a)** Paragraphs 2 and 3 above (candidates should aim to spend not more than 20 minutes on this question)",
      H("### (a) Paragraphs 2 and 3: acting for both Yasuo and Teemo (20 minutes)")),
    q("Q2020-1-b", "II.19 III.8 III.15 VII.5", "PYP 2020 Q1(b)", "20 minutes",
      "**(b)** Paragraphs 4 and 5 above (candidates should aim to spend not more than 20 minutes on this question)",
      H("### (b) Paragraphs 4 and 5: the plan for Teemo, and the fee discount (20 minutes)")),
    q("Q2020-1-c", "III.13 III.2 III.8 III.15 V.1 I.2", "PYP 2020 Q1(c)", "20 minutes",
      "**(c)** Paragraph 6 above (candidates should aim to spend not more than 20 minutes on this question)",
      H("### (c) Paragraph 6: preparing Teemo's evidence (20 minutes)")),
]))
ps3q2 = after_header("## PS3 Q2 — Donnie, Melany and Mega Law")
G.append(("2020 Q2 — Donnie, Mega Law, MCP and Joey · PYP 2020 (paras 1, 3–4 = PS3 Q2)", FACTS["2020-2"], [
    q("Q2020-2-a", "VI.1 VI.2 V.4", "PYP 2020 Q2(a)", "22 minutes",
      "**(a)** Paragraph 2 above (candidates should aim not to spend more than 22 minutes on this question)",
      H("### (a) Paragraph 2: the Facebook statements (22 minutes)")),
    q("Q2020-2-b", "V.1 V.2 VII.6 VI.4 V.5 VI.6", "PYP 2020 Q2(b); = PS3 Q2", "14 minutes",
      "**(b)** Paragraph 3 above (candidates should aim not to spend more than 14 minutes on this question)",
      H("### (b) Paragraph 3: Melany's non-contentious work (14 minutes)")
      + "\n\n**The PS3 Q2 answer, which (b) builds on** (PS3 Q2 is paras 1, 3 and 4 of this question):\n\n" + ps3q2),
    q("Q2020-2-c", "V.5 II.19 II.21 II.23 IV.10 VII.5 V.2", "PYP 2020 Q2(c)", "24 minutes",
      "**(c)** Paragraphs 4 to 7 (candidates should aim not to spend more than 24 minutes on this question)",
      H("### (c) Paragraphs 4 to 7: MCP, the loan and Joey's shares (24 minutes)")),
]))
# ---- 2019 ----
q19_2 = section("## 2019 Q2 — Archie, Veronica and Cheryl (questions missing)")
q19_2 = re.sub(r"^- TODO: questions missing — ", "- ", q19_2, flags=re.M)
q19_2 = q19_2.split("\n\n", 1)[1]  # drop the 'Question: …' paragraph (repeated in the facts note)
G.append(("2019 Q1 — Buffy, Spike and Dru · PYP 2019", FACTS["2019-1"], [
    q("Q2019-1", "II.6 II.7 II.8 II.9 II.19 VII.3 VII.4 VII.5 III.8 III.9 III.10 IV.2 IV.11 IV.13 I.2", "PYP 2019 Q1", "60 minutes",
      "Discuss and evaluate Buffy's professional and ethical conduct in relation to the above matters (candidates should aim to spend not more than 60 minutes on this question).",
      H("### Q1 Buffy's conduct (60 minutes)")),
]))
G.append(("2019 Q2 — Archie, Veronica and Cheryl · PYP 2019 (questions missing)", FACTS["2019-2"], [
    q("Q2019-2", "II.17 II.18 II.10 II.12 II.19 IV.10 VI.4 II.3", "PYP 2019 Q2 (pp 5–6 missing)", "—",
      "*The questions asked are on the missing pages. The issues below are what the facts raise.*",
      "**Answer (issues only; no model answer, because the questions are missing):**\n\n" + q19_2),
]))
# ---- 2018 ----
ps3q3 = after_header("## PS3 Q3 — Brenner Law's proposed advertisements")
c18 = section("### (c) DPL's proposed advertising statements (24 minutes)")
c18_tail = c18[c18.index("In conclusion on Q1"):]
G.append(("2018 Q1 — Joyce, Duffer, Hawkins and Wheeler's Condition · PYP 2018 ((c) = PS3 Q3)", FACTS["2018-1"], [
    q("Q2018-1-a", "II.12 II.13 II.16 II.10 II.17", "PYP 2018 Q1(a)", "24 minutes",
      "**(a)** Joyce's conduct in relation to acting for Hawkins against Max and other creditors (it is recommended that candidates spend no more than 24 minutes on this part)",
      H("### (a) Joyce acting for Hawkins against Max and other creditors (24 minutes)")),
    q("Q2018-1-b", "VII.5 II.19", "PYP 2018 Q1(b)", "12 minutes",
      "**(b)** Whether BL can agree to Wheeler's Condition, and why or why not (it is recommended that candidates spend no more than 12 minutes on this part)",
      H("### (b) Can BL agree to Wheeler's Condition? (12 minutes)")),
    q("Q2018-1-c", "VI.1 VI.2", "PYP 2018 Q1(c); = PS3 Q3", "24 minutes",
      "**(c)** Which or which portions, if any, of DPL's proposed advertising statements can BL use, and why or why not (it is recommended that candidates spend no more than 24 minutes on this part)",
      ps3q3 + "\n\n" + c18_tail),
]))
CALL18 = ("Explain why or why not, and/or whether any additional safeguards or measures may be required on the "
          "part of PL and/or the legal practitioners involved")
G.append(("2018 Q2 — Pawnee LLP, the YPL bidders and Lex Sweetums · PYP 2018", FACTS["2018-2"], [
    q("Q2018-2-a", "II.12 II.10 II.15", "PYP 2018 Q2(a)", "20 minutes",
      f"**(a)** Whether Ben can act for E, assuming April continues to act for K. {CALL18} (it is recommended that candidates spend no more than 20 minutes on this part)",
      H("### (a) Can Ben act for E while April acts for K? (20 minutes)")),
    q("Q2018-2-b", "II.12 II.13 II.10", "PYP 2018 Q2(b)", "20 minutes",
      f"**(b)** Whether Chris can act for the PRA, assuming April continues to act for K, and taking into account the possibility of Ben acting for E. {CALL18} (it is recommended that candidates spend no more than 20 minutes on this part)",
      H("### (b) Can Chris act for the PRA? (20 minutes)")),
    q("Q2018-2-c", "VI.4 VI.3 VII.3 II.3", "PYP 2018 Q2(c)", "20 minutes",
      "**(c)** Which or which portions, if any, of LS' proposed clauses can PL agree to? Explain why or why not (it is recommended that candidates spend no more than 20 minutes on this part)",
      H("### (c) Which of LS's proposed clauses can PL agree to? (20 minutes)")),
]))
# ---- Drills ----
d1_lines = drill_block("### Question (30 marks, 36 minutes)", ("---", "### "))
d1_facts, d1_calls = split_calls(d1_lines)
d1_ans = section("### Model answer")
cut = d1_ans.index("**(b) ")
G.append(("Drill 1 — Priya Law · own question (QB-23) · 30 marks", d1_facts, [
    q("QD1-a", "II.24 II.19 II.10 IV.10", "Drill 1 (a); own, tier 3", "15 marks", d1_calls[0], d1_ans[:cut].strip()),
    q("QD1-b", "III.15 III.8 II.10", "Drill 1 (b); own, tier 3", "15 marks", d1_calls[1], d1_ans[cut:].strip()),
]))
DRILLS = [
    ("### Drill 2 (H1) — Marcus Lee and the Orchid suit (50 marks, 60 minutes)", "Drill 2 (H1) — Marcus Lee, the Orchid suit and DPP Nadia · own question (QB-38) · 50 marks",
     "QD2", [("III.5 III.7 III.14", "### 1.1 Marcus's conduct in chambers (15 marks)", "15 marks"),
             ("III.14 IV.9 III.2", "### 1.2 The undertaking, the email to the Judge and the LinkedIn post (20 marks)", "20 marks"),
             ("III.16", "### 1.3 Nadia's conduct as prosecutor (15 marks)", "15 marks")]),
    ("### Drill 3 (H2) — Daniel Koh, Rachel Ong and Crest Law (50 marks, 60 minutes)", "Drill 3 (H2) — Daniel Koh, Rachel Ong and Crest Law · own question (QB-39) · 50 marks",
     "QD3", [("IV.12 IV.7 IV.5 IV.6", "### 2.1 Daniel's conduct (30 marks)", "30 marks"),
             ("IV.8 IV.3", "### 2.2 Rachel's affidavit and Wei Ling's conduct (20 marks)", "20 marks")]),
    ("### Drill 4 (H3) — Benjamin Chua and Madam Lim (50 marks, 60 minutes)", "Drill 4 (H3) — Benjamin Chua and Madam Lim · own question (QB-40) · 50 marks",
     "QD4", [("I.3 II.22 II.19", "### 3.1 The lapsed practising certificate and the two loans (25 marks)", "25 marks"),
             ("II.11 II.10 II.7", "### 3.2 The requests for information and the will (25 marks)", "25 marks")]),
    ("### Drill 5 (H4) — Wendy Goh, Alvin and Homesmart (50 marks, 60 minutes)", "Drill 5 (H4) — Wendy Goh, Alvin and Homesmart · own question (QB-41) · 50 marks",
     "QD5", [("V.3 V.2 I.1", "### 4.1 Supervision of Alvin, and his admission application (15 marks)", "15 marks"),
             ("VI.5 VI.4", "### 4.2 The Homesmart arrangement (15 marks)", "15 marks"),
             ("VII.1 VII.2", "### 4.3 Mr Tan's settlement money and the Zenith purchase (20 marks)", "20 marks")]),
]
for start, title, pre, parts in DRILLS:
    facts, calls = split_calls(drill_block(start, ("### ",)))
    assert len(calls) == len(parts), (start, calls)
    qs = []
    for n, ((keys, head, marks), call) in enumerate(zip(parts, calls), 1):
        num = re.match(r"\*\*(\d\.\d)", call).group(1)
        qs.append(q(f"{pre}-{num.replace('.', '-')}", keys, f"{title.split(' · ')[0].split(' — ')[0]} {num}; own, tier 3", marks, call, H(head)))
    G.append((title, facts, qs))

# ---- write ----
out = ["# ETH-W — Model Questions and Answers", "",
       "Paper `eth-w`. Every ETH hypothetical held, with its model answer: the past-year papers newest first, "
       "then the practice-session questions that match no paper held (probably 2024), then Drills 1–5. "
       "Built 5 Nov 2026 for `python3 tools/build_pack.py eth-w --questions`.", "",
       "**Sources.** Question text is transcribed from the past papers in `Bar Exam/Seniors Notes/Nic_s Part B Package/3. PYP/` "
       "(the 2018–2020, 2022, 2023 and 2025 papers are scans, read by OCR, cleaned up by hand and spot-checked against the page images; margin notes "
       "by earlier candidates are left out) and the practice-session papers in `Bar Exam/Modules/Ethics & Professional Responsibility/3. Practice Sessions - Question Papers/`. "
       "Words in [square brackets] are not in the paper. The transcribed question text is in `pyp-facts.md`; drill questions are from `drills.md`. "
       "Answers are copied from `model-answers.md`, which stays the master copy: fix an answer (or a transcription in `pyp-facts.md`) there, "
       "then run `python3 tools/assemble_eth_questions.py` and `python3 tools/build_pack.py eth-w --questions`; never edit this file by hand. Only 2023 Q1 has an official answer (SQ p109–113); every other answer is this project's own.", "",
       "**How to read a question:** the tag line gives the question ID · the Sub-point Keys it raises (from `coverage.md`) · "
       "the source · marks or time · the Pre-writes in the Reference Pack that hold the rules. Cover the answer, answer it, then check.",
       "Self-study only — never use this file with a live quiz, the Mock Exam or another assessment (Handbook §7.11). "
       "The 2025 paper comes first: if you mean to sit it unseen as a Practice Paper, skip it.", "",
       "## 0 · Ethics & Professional Responsibility", ""]
seen = set()
for title, facts, qs in G:
    out += [f"### {title}", "", facts, ""]
    for x in qs:
        assert x["id"] not in seen, x["id"]; seen.add(x["id"])
        for k in x["keys"]:
            assert k in PW, (x["id"], k)
        keys = sorted(dict.fromkeys(x["keys"]), key=ORDER.index)
        ids = list(dict.fromkeys(i for k in keys for i in PW[k]))
        tag = (f"**{x['id']}** · " + " ".join(f"`{k}`" for k in keys) + f" · {x['source']} · {x['marks']} · "
               + " ".join(f"`{i}`" for i in ids))
        ans = x["answer"]
        if not ans.startswith("**Answer"):
            ans = "**Answer.**\n\n" + ans
        out += [tag, "", x["call"], "", ans, ""]
text = "\n".join(out).rstrip() + "\n"
(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "model-questions.md").write_text(text)
print(len(seen), "questions in", len(G), "groups;", len(text.split()), "words")
