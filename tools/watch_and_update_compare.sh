#!/bin/bash
filename=$1
filebase=${filename%.*}

python tools/vtt2compare.py $filename
while inotifywait -e modify $filebase.{raw,*.txt}; do \
    python tools/vtt2compare.py $filename
done
