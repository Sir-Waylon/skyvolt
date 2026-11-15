#!/bin/sh
# usage: ./ckpt.sh "what was done" "next step"
cd "$(dirname "$0")"
printf '{"done":"%s","next":"%s","resume":"unzip; python3 build.py events/<slug>/pack.json out/x.html; node chk4.js"}\n' "$1" "$2" > PROGRESS.json
rm -f ../kit_checkpoint.zip; zip -qr ../kit_checkpoint.zip . -x 'out/*' -x 'ck/*' && ls -la ../kit_checkpoint.zip
