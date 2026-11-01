#!/usr/bin/env python3
"""Format existing entries and recent highlights. Default: read-only check."""
import argparse
import json
import re
from datetime import date
from pathlib import Path
from catalog import ANCHOR_RE, ENTRY_RE, parse_entries, catalog_bounds, summary, qc_summary, replace_block

ROOT = Path(__file__).resolve().parent.parent

def recent_table(text, records, lang):
    by_repo = {e.name.lower():e for e in parse_entries(text)}
    seen = set()
    for record in records:
        repo = record['repo'].lower()
        date.fromisoformat(record['added_on'])
        if repo in seen or repo not in by_repo:
            raise ValueError(f'duplicate or unlisted recent addition: {repo}')
        if not re.fullmatch(r'[0-9a-f]{40}',record['commit']):
            raise ValueError(f'recent addition has no source commit: {repo}')
        seen.add(repo)
    rows = ['| 收录日期 | 项目 | 用途 |' if lang == 'zh' else '| Added | Project | Purpose |','| --- | --- | --- |']
    for r in sorted(records,key=lambda r:r['added_on'],reverse=True)[:6]:
        e = by_repo[r['repo'].lower()]
        url = 'https://github.com/Herdeny/awesome-dsh-plugins-2026/commit/'+r['commit']
        purpose = r['zh' if lang=='zh' else 'en']
        if any(c in purpose for c in ['|','\n']):
            raise ValueError('recent purpose must be plain table text')
        rows.append(f'| [{r["added_on"]}]({url}) | [{e.name}]({e.url}) | {purpose} |')
    return '\n'.join(rows)

def format_text(text, lang, records):
    entries = parse_entries(text)
    by_section = {}
    for e in entries:
        by_section.setdefault(e.section,[]).append(e)
    start,end = catalog_bounds(text)
    parts = re.split(r'(?=<a id="[\w-]+"></a>)',text[start:end])
    for i,part in enumerate(parts):
        if not part.strip():
            continue
        anchor = ANCHOR_RE.match(part)
        if not anchor:
            raise ValueError('unexpected text before catalog section')
        section = anchor.group(1)
        lines = part.splitlines()
        positions = [j for j,line in enumerate(lines) if ENTRY_RE.fullmatch(line)]
        if not positions:
            continue
        if any(line.strip() and not ENTRY_RE.fullmatch(line) for line in lines[positions[0]:positions[-1]+1]):
            raise ValueError(f'non-entry text between entries in {section}')
        formatted = [e.render(lang) for e in sorted(by_section[section],key=lambda e:e.name.casefold())]
        parts[i] = '\n'.join(lines[:positions[0]]+formatted+lines[positions[-1]+1:]).rstrip()+'\n\n'
    text = text[:start]+'\n\n'+''.join(parts).lstrip()+text[end:]
    text = replace_block(text,'catalog-summary',summary(text,lang))
    text = replace_block(text,'qc-summary',qc_summary(text,lang))
    text = replace_block(text,'recent-additions',recent_table(text,records,lang))
    text = re.sub(r'(?<=Projects: )\d+',str(len(entries)),text)
    return re.sub(r'(?<=projects-)\d+(?=-orange)',str(len(entries)),text)

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true')
    args = ap.parse_args(argv)
    records = json.loads((ROOT/'data/recent-additions.json').read_text())
    results = []
    for filename,lang in [('README.md','zh'),('README.en.md','en')]:
        p = ROOT/filename
        original = p.read_text()
        results.append((p,original,format_text(original,lang,records)))
    drift = False
    for p,original,updated in results:
        if original == updated:
            print(f'✓ {p.name}: catalog and highlights current')
        elif args.write:
            p.write_text(updated)
            print(f'updated {p.name}')
        else:
            drift = True
            print(f'✗ {p.name}: run python3 scripts/format_catalog.py --write')
    return int(drift)

if __name__ == '__main__':
    raise SystemExit(main())
