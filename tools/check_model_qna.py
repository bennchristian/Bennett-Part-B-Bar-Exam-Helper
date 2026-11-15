"""Check a Paper's Model Q&A Markdown: every coverage Sub-point has a tagged question, no open TODO: verify.

    python3 tools/check_model_qna.py <pack folder>      e.g. pcp-w, ccp-1, drp-w-wa

Reads study/<pack>/coverage.md (rows `| <Key> | ...`) and study/<pack>/model-questions.md
(tag lines `**Q…** · `Key` · source · `end-point ID``). Exit 0 = done, 1 = gaps remain, 2 = no file.
Rows whose Covered-by cell starts `none` (deliberately uncovered) are reported but not counted as gaps.
"""
import re
import sys
from pathlib import Path

ROW = re.compile(r"^\|\s*`?((?:\d+\.)?[IVXLC]+\.\d+)`?\s*\|")
TAG = re.compile(r"^\*\*Q[\w-]+\*\*\s*·(.*)$")
KEY = re.compile(r"`((?:\d+\.)?[IVXLC]+\.\d+)`")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    d = Path(__file__).resolve().parent.parent / "study" / sys.argv[1]
    mq = d / "model-questions.md"
    if not mq.exists():
        print(f"{sys.argv[1]}: no model-questions.md")
        sys.exit(2)
    rows, none = [], []
    for line in (d / "coverage.md").read_text().splitlines():
        m = ROW.match(line)
        if m:
            (none if line.rstrip("| ").split("|")[-1].strip().startswith("none") else rows).append(m.group(1))
    text = mq.read_text()
    tagged = set()
    for line in text.splitlines():
        m = TAG.match(line.strip())
        if m:
            tagged.update(KEY.findall(m.group(1)))
    missing = [k for k in rows if k not in tagged]
    verify = [i + 1 for i, l in enumerate(text.splitlines()) if "TODO: verify" in l]
    print(f"{sys.argv[1]}: {len(rows) - len(missing)}/{len(rows)} Sub-points have a tagged question"
          + (f" ({len(none)} 'none' rows skipped)" if none else ""))
    if missing:
        print("  untagged:", ", ".join(missing))
    print(f"  TODO: verify in model-questions.md: {len(verify)}"
          + (f" (lines {', '.join(map(str, verify[:30]))}{' …' if len(verify) > 30 else ''})" if verify else ""))
    sys.exit(0 if not missing and not verify else 1)


if __name__ == "__main__":
    main()
