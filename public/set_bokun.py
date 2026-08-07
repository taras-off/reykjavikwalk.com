#!/usr/bin/env python3
"""Swap the Bokun placeholders across every file in public/ once the real IDs exist.
Usage:  python3 set_bokun.py <CHANNEL_UUID> <PRODUCT_ID>
"""
import sys, pathlib
if len(sys.argv) != 3:
    sys.exit(__doc__)
uuid, pid = sys.argv[1], sys.argv[2]
n = 0
for f in pathlib.Path('public').rglob('*.html'):
    t = f.read_text(encoding='utf8')
    if 'BOKUN_UUID' in t or 'BOKUN_PID' in t:
        f.write_text(t.replace('BOKUN_UUID', uuid).replace('BOKUN_PID', pid), encoding='utf8')
        n += 1
        print('patched', f)
print(f'{n} file(s) updated')
