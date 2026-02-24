#!/usr/bin/env python3

import itertools
import json
import math
import sys
from pathlib import Path

import spacy

from utils import paragraph_to_tokens, tokens_to_lines


def compact_vtt(vtt_in, vtt_out):
    for line in vtt_in:
        vtt_out.write(line)
        if " --> " in line:
            break

    nlp = spacy.load("zh_core_web_sm")

    segments = []

    def flush_paragraph():
        nonlocal segments
        lines = tokens_to_lines(paragraph_to_tokens(" ".join(segments), nlp), [1])
        assert len(lines) == 1
        vtt_out.write(lines[0])
        vtt_out.write("\n\n")
        segments.clear()

    for line in vtt_in:
        if " --> " in line:
            flush_paragraph()
            vtt_out.write(line)
            continue
        line = line.strip()
        if line:
            segments.append(line)

    flush_paragraph()


def main():
    vtt_file = Path(sys.argv[1])
    assert vtt_file.suffix == ".vtt"
    compact_vtt_file = vtt_file.with_suffix(".compact.vtt")
    with (
        open(vtt_file) as vtt_in,
        open(compact_vtt_file, "w") as vtt_out,
    ):
        compact_vtt(vtt_in, vtt_out)


if __name__ == "__main__":
    main()
