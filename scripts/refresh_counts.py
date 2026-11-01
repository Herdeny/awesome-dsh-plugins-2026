#!/usr/bin/env python3
"""Check canonical totals, QC coverage, badge alt text and paired update dates.

Recent highlights and official links are outside the canonical catalog.
--write repairs metadata and dates in both languages; default is read-only.
"""
import argparse
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from catalog import stats, summary, qc_summary, replace_block

ROOT = Path(__file__).resolve().parent.parent

def refresh(text,lang):
    total = stats(text)['projects']
    badge = f'![Projects: {total}](https://img.shields.io/badge/projects-{total}-orange.svg)'
    pattern = r'!\[Projects: \d+\]\(https://img\.shields\.io/badge/projects-\d+-orange\.svg\)'
    if len(re.findall(pattern,text)) != 1:
        raise ValueError('expected one numeric Projects badge')
    text = re.sub(pattern,lambda _:badge,text)
    text = replace_block(text,'catalog-summary',summary(text,lang))
    return replace_block(text,'qc-summary',qc_summary(text,lang))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true')
    args = ap.parse_args()
    drift,results,dates = False,[],[]
    for filename,lang in [('README.md','zh'),('README.en.md','en')]:
        p = ROOT/filename
        original = p.read_text()
        updated = refresh(original,lang)
        m = re.search(r'!\[Last updated: (\d{4}-\d{2}-\d{2})\]\(https://img\.shields\.io/badge/last--updated-(\d{4}--\d{2}--\d{2})-brightgreen\.svg\)',original)
        if not m or m.group(1) != m.group(2).replace('--','-'):
            drift = True
            print(f'✗ {filename}: update date alt text and URL disagree')
        dates.append(m.group(1) if m else None)
        if args.write:
            today = datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat()
            updated = re.sub(r'!\[Last updated:[^\]]*\]\([^\n]*\)',f'![Last updated: {today}](https://img.shields.io/badge/last--updated-{today.replace("-","--")}-brightgreen.svg)',updated)
        elif original != updated:
            drift = True
            print(f'✗ {filename}: catalog or QC metadata drift')
        results.append((p,updated))
        print(f'{filename}: {stats(original)}')
    if not args.write and dates[0] != dates[1]:
        drift = True
        print('✗ zh/en update dates differ')
    if args.write:
        for p,updated in results:
            if p.read_text() != updated:
                p.write_text(updated)
        return 0
    return int(drift)

if __name__ == '__main__':
    raise SystemExit(main())
