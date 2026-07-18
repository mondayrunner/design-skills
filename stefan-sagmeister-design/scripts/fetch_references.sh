#!/usr/bin/env bash
# Genereert de references van de stefan-sagmeister-design skill lokaal.
#
# De skill leunt op twee bronnen die we niet herpubliceren op GitHub (copyright):
#   1. De Q&A's van https://sagmeister.com/answers/  -> references/answers-faq.md
#   2. YouTube-transcripts van zes talks             -> references/talks/*.md
# Dit script downloadt en parsed ze naar jouw lokale installatie.
#
# Vereist: curl, python3, yt-dlp (https://github.com/yt-dlp/yt-dlp)
set -euo pipefail
cd "$(dirname "$0")"

command -v yt-dlp >/dev/null || { echo "yt-dlp ontbreekt: brew install yt-dlp (of pip install yt-dlp)"; exit 1; }

echo "[1/3] FAQ ophalen van sagmeister.com..."
curl -sL "https://sagmeister.com/answers/" -o /tmp/sagmeister-answers.html
python3 parse_faq.py /tmp/sagmeister-answers.html ../references/answers-faq.md

echo "[2/3] YouTube-ondertitels downloaden (6 talks)..."
mkdir -p /tmp/sagmeister-subs
for id in H5oyGnzOLl4 yqQXFtSVEmA MNuOmTQdFjA pgOIAcZWS3s eMVWSUeeg8A VzPVe2D0kYM; do
  yt-dlp --skip-download --write-auto-sub --write-sub --sub-lang "en,en-orig" --sub-format vtt \
    -o "/tmp/sagmeister-subs/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >/dev/null 2>&1 || true
done

echo "[3/3] Transcripts opschonen..."
python3 vtt_to_md.py /tmp/sagmeister-subs ../references/talks

echo "Klaar. References staan in $(cd ../references && pwd)"
