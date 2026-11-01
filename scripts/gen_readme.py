#!/usr/bin/env python3
"""Compatibility wrapper: maintain the current catalog, never old /tmp seeds.

Use `python3 scripts/format_catalog.py --write` to format or omit --write
for a read-only check. This legacy name retains the same safe default.
"""
from format_catalog import main

if __name__ == '__main__':
    raise SystemExit(main())
