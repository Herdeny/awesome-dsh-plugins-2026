#!/usr/bin/env python3
"""Idempotently sync QC color emoji + score distribution in awesome-dsh-2026 READMEs.

For every plugin line carrying a 🛡️QC:<score> mark, ensure the matching quality
level emoji (🟢 70-100 / 🟡 50-69 / 🟠 30-49 / 🔴 0-29) appears right after the
score. Then recompute the "质量评分分布 / Quality score distribution" block so
the four bucket counts always match the entries actually present.

Both README.md and README.en.md are updated in lockstep (CI sync_audit).

Usage:
    python3 scripts/update_qc_marks.py [--check]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from catalog import catalog_bounds, ENTRY_RE, qc_summary, replace_block

ROOT = Path(__file__).resolve().parent.parent
READMES = [ROOT / "README.md", ROOT / "README.en.md"]

QC_RE = re.compile(r"🛡️QC:(\d+)")
LEVELS = [
    (70, "🟢"),
    (50, "🟡"),
    (30, "🟠"),
    (0, "🔴"),
]
DIST_RE = re.compile(r"^(- )([🟢🟡🟠🔴])( \d+-\d+: )\d+")


def level_emoji(score: int) -> str:
    for lo, emoji in LEVELS:
        if score >= lo:
            return emoji
    return "🔴"


def add_emoji_to_line(line: str) -> str:
    m = QC_RE.search(line)
    if not m:
        return line
    emoji = level_emoji(int(m.group(1)))
    rest = line[m.end():]
    # strip any pre-existing level emoji (and whitespace) right after the score
    rest = re.sub(r"^\s*[🟢🟡🟠🔴]", "", rest)
    return line[: m.end()] + f" {emoji}" + rest


def process(text: str, lang: str = 'zh') -> str:
    start, end = catalog_bounds(text)
    lines = text[start:end].splitlines(keepends=True)
    for i, line in enumerate(lines):
        if ENTRY_RE.fullmatch(line.rstrip('\n')):
            lines[i] = add_emoji_to_line(line)
    text = text[:start]+''.join(lines)+text[end:]
    return replace_block(text, 'qc-summary', qc_summary(text, lang))


def main() -> int:
    changed = False
    check_only = "--check" in sys.argv
    for readme in READMES:
        original = readme.read_text(encoding="utf-8")
        updated = process(original, 'en' if readme.name == 'README.en.md' else 'zh')
        if updated != original:
            if not check_only:
                readme.write_text(updated, encoding="utf-8")
            changed = True
            print(f"{'needs update' if check_only else 'updated'} {readme.name}")
        else:
            print(f"unchanged {readme.name}")

    if "--check" in sys.argv:
        return 1 if changed else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
