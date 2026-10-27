#!/usr/bin/env python3
"""Embed reproducible reference results in a single self-contained offline HTML file."""
import json
from pathlib import Path
from governance import experiment, ROOT

report=experiment()
template=(ROOT/'dashboard/template.html').read_text(encoding='utf-8')
payload=json.dumps(report,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
output=ROOT/'dashboard/index.html'
output.write_text(template.replace('__TODM_DATA__',payload),encoding='utf-8')
print('Offline dashboard:',output, 'bytes:',output.stat().st_size)
