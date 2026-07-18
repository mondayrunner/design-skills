#!/usr/bin/env python3
"""Parse sagmeister.com/answers/ HTML into a clean markdown FAQ reference."""
import re
from html.parser import HTMLParser
from html import unescape

import sys
html = open(sys.argv[1]).read()

# Each category block: <div ... id="slug"> ... <h2><span>Title</span></h2> ... qa items
sections = re.split(r'<div class="paginatable[^"]*block subanchor" id="([^"]+)">', html)
# sections[0] = preamble, then pairs of (slug, content)

out = ["# Stefan Sagmeister — Answers (FAQ from sagmeister.com)\n",
       "Source: https://sagmeister.com/answers/ — Sagmeister's own written answers to interview questions, in his own voice.\n"]

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n\s*', '\n\n', s)
    return s.strip()

total_q = 0
for i in range(1, len(sections), 2):
    slug, content = sections[i], sections[i+1]
    m = re.search(r'<h2\s*><span>(.*?)</span></h2>', content)
    title = strip_tags(m.group(1)) if m else slug
    out.append(f"\n## {title}\n")
    qas = re.findall(r'<div class="question _pkedit-noblock">(.*?)</div>\s*<div class="answer">\s*<span class="_pkedit">(.*?)</span>\s*</div>', content, re.S)
    for q, a in qas:
        q, a = strip_tags(q), strip_tags(a)
        if not a:
            continue
        total_q += 1
        out.append(f"**Q: {q}**\n\n{a}\n")

open(sys.argv[2], "w").write("\n".join(out))
print(f"Wrote {total_q} Q&As across {len(sections)//2} categories")
