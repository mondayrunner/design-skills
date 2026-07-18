#!/usr/bin/env python3
"""Convert YouTube VTT subtitles to clean transcript markdown files."""
import re, os, textwrap

VIDEOS = {
    "H5oyGnzOLl4": ("how-to-create-original-ideas", "How to Create Original Ideas — Stefan Sagmeister (talk, 1h08)"),
    "yqQXFtSVEmA": ("now-is-better", "Stefan Sagmeister: Finally, Something Good / Now Is Better (talk, 1h09)"),
    "MNuOmTQdFjA": ("the-power-of-time-off", "Stefan Sagmeister: The Power of Time Off (TED talk, 17m)"),
    "pgOIAcZWS3s": ("why-designers-should-open-their-own-studio", "Why Graphic Designers Should Open Their Own Studio — Twos Talks with Stefan Sagmeister (interview, 1h)"),
    "eMVWSUeeg8A": ("7-rules-for-more-happiness", "Stefan Sagmeister: 7 Rules for Making More Happiness (TED talk, 9m)"),
    "VzPVe2D0kYM": ("design-and-happiness", "Stefan Sagmeister: Design and Happiness (talk, 1h08)"),
}

import sys
SUBS = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def parse_vtt(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    cues, seen_tail = [], ""
    for line in lines:
        if "-->" in line or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")) or not line.strip():
            continue
        text = re.sub(r'<[^>]+>', '', line).strip()
        text = text.replace("&nbsp;", " ").replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<")
        if not text or text == seen_tail:
            continue
        # rolling captions repeat the previous line; skip exact dupes of last cue
        if cues and (text == cues[-1] or cues[-1].endswith(text)):
            continue
        cues.append(text)
        seen_tail = text
    return " ".join(cues)

for vid, (slug, title) in VIDEOS.items():
    src = f"{SUBS}/{vid}.en.vtt"
    if not os.path.exists(src):
        src = f"{SUBS}/{vid}.en-orig.vtt"
    body = parse_vtt(src)
    body = re.sub(r'\s+', ' ', body).strip()
    wrapped = "\n".join(textwrap.wrap(body, width=110))
    words = len(body.split())
    with open(f"{OUT}/{slug}.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\nSource: https://www.youtube.com/watch?v={vid}\n"
                f"Auto-generated transcript (unedited captions), ~{words} words.\n\n{wrapped}\n")
    print(f"{slug}.md: {words} words")
