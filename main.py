import os

LINE = "I'm out until Tuesday. Dave is covering for me: he's already replied to 14 of you and regrets 11 of them."

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-140 chars,
# not only whitespace, a single line. Fail loudly instead of shipping
# an invalid entry.
if not 1 <= len(LINE) <= 140 or not LINE.strip() or "\n" in LINE:
    raise SystemExit("entry line violates the 1-140 char single-line gate")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
entry_path = os.path.join(out_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

# Read-back verification: prove the file the grader reads is byte-identical
# to LINE. Fail loudly rather than ship a corrupted or truncated entry.
with open(entry_path, "r", encoding="utf-8", newline="") as f:
    written = f.read()
if written != LINE:
    raise SystemExit(
        f"entry.txt verification failed: read back {len(written)} chars, "
        f"expected {len(LINE)} chars identical to the entry line"
    )
