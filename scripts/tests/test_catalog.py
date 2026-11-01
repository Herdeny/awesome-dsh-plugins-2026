"""Regression checks for count inflation, metadata drift and read-only checks."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from catalog import parse_entries, stats
import format_catalog
import refresh_counts
import update_qc_marks
import sync_audit


def fixture(lang='zh'):
    plugin, resource = ('插件','资源') if lang=='zh' else ('Plugin','Resource')
    return f'''![Projects: 2](https://img.shields.io/badge/projects-2-orange.svg)
![Last updated: 2026-11-01](https://img.shields.io/badge/last--updated-2026--11--01-brightgreen.svg)
<!-- catalog-summary:start -->
stale
<!-- catalog-summary:end -->
<!-- recent-additions:start -->
stale
<!-- recent-additions:end -->
| [a/b](https://github.com/a/b) | duplicate highlight |
<!-- catalog:start -->

<a id="tools"></a>

## Tools

- [a/b](https://github.com/a/b) - A project (⭐3) 🛡️QC:72 🟢 · `{plugin}`

<a id="ecosystem"></a>

## Ecosystem

- [c/d](https://github.com/c/d) - A guide (⭐1) · `{resource}`

<!-- catalog:end -->
<!-- qc-summary:start -->
stale
<!-- qc-summary:end -->
- [Official](https://github.com/a/b)
'''


class CatalogTests(unittest.TestCase):
    def test_highlights_and_official_links_do_not_inflate_counts(self):
        self.assertEqual(stats(fixture()),dict(projects=2,main=1,ecosystem=1,scored=1,unscored=0))

    def test_missing_markers_fail_instead_of_counting_every_link(self):
        with self.assertRaises(ValueError):
            parse_entries(fixture().replace('<!-- catalog:end -->',''))

    def test_duplicate_repository_is_rejected(self):
        text=fixture().replace('https://github.com/c/d','https://github.com/A/B')
        with self.assertRaisesRegex(ValueError,'duplicate'):
            parse_entries(text)

    def test_out_of_range_scores_are_not_treated_as_valid(self):
        with self.assertRaisesRegex(ValueError,'between 0 and 100'):
            parse_entries(fixture().replace('QC:72','QC:172'))

    def test_unknown_type_requires_editorial_decision(self):
        text=fixture().replace('`插件`','`magic`')
        with self.assertRaisesRegex(ValueError,'unknown type'):
            format_catalog.format_text(text,'zh',[])

    def test_recent_records_require_catalog_membership_and_provenance(self):
        record=dict(repo='missing/project',added_on='2026-11-01',commit='a'*40,zh='x',en='x')
        with self.assertRaisesRegex(ValueError,'unlisted'):
            format_catalog.recent_table(fixture(),[record],'zh')
        record['repo']='a/b';record['commit']='latest'
        with self.assertRaisesRegex(ValueError,'source commit'):
            format_catalog.recent_table(fixture(),[record],'zh')

    def test_formatter_is_idempotent_and_preserves_scores_and_stars(self):
        original=fixture()
        formatted=format_catalog.format_text(original,'zh',[])
        self.assertEqual(format_catalog.format_text(formatted,'zh',[]),formatted)
        before=[(e.key,e.score,e.stars) for e in parse_entries(original)]
        after=[(e.key,e.score,e.stars) for e in parse_entries(formatted)]
        self.assertEqual(before,after)

    def test_read_only_format_check_does_not_fix_files(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'data/recent-additions.json').write_text('[]')
            for f,lang in [('README.md','zh'),('README.en.md','en')]:
                (root/f).write_text(fixture(lang))
            before={p:p.read_bytes() for p in root.glob('README*')}
            with patch.object(format_catalog,'ROOT',root),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(format_catalog.main([]),1)
            self.assertEqual(before,{p:p.read_bytes() for p in before})

    def test_qc_check_is_read_only_and_ignores_numeric_examples(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'README.md'
            text=fixture().replace('QC:72 🟢','QC:72 🔴')+'\nExample: 🛡️QC:99 🟢\n'
            p.write_text(text);before=p.read_bytes()
            with patch.object(update_qc_marks,'READMES',[p]),patch.object(sys,'argv',['update_qc_marks.py','--check']),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(update_qc_marks.main(),1)
            self.assertEqual(before,p.read_bytes())
            fixed=update_qc_marks.process(text)
            self.assertIn('QC:72 🟢',fixed)
            self.assertIn('🟢 70-100: 1',fixed)

    def test_badge_alt_text_and_url_are_both_repaired(self):
        text=fixture().replace('Projects: 2','Projects: 999').replace('projects-2-orange','projects-1-orange')
        result=refresh_counts.refresh(text,'zh')
        self.assertIn('Projects: 2](https://img.shields.io/badge/projects-2-orange.svg)',result)

    def test_translation_audit_catches_star_and_type_drift(self):
        for mutation in [lambda s:s.replace('(⭐3)','(⭐4)'),lambda s:s.replace('`Plugin`','`Skill`')]:
            with self.subTest(mutation=mutation),tempfile.TemporaryDirectory() as d:
                root=Path(d);zh=root/'README.md';en=root/'README.en.md'
                zh.write_text(fixture('zh'));en.write_text(mutation(fixture('en')))
                with patch.object(sync_audit,'FILES',dict(zh=zh,en=en)),patch.object(sys,'argv',['sync_audit.py','--summary']),contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(sync_audit.main(),1)


if __name__=='__main__':
    unittest.main()
