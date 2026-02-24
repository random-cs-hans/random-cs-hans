#!/usr/bin/env python3

import itertools
import json
import sys
from pathlib import Path

import spacy

from utils import paragraph_to_tokens, tokens_to_lines


def cooked_to_vtt(vtt_in, idx_in, cooked_in, vtt_out):
    for line in vtt_in:
        if " --> " in line:
            break
        vtt_out.write(line)

    nlp = spacy.load("zh_core_web_sm")

    for index_json, paragraph in itertools.zip_longest(idx_in, cooked_in):
        paragraph = paragraph[:-1]
        tokens = paragraph_to_tokens(paragraph, nlp)
        index = json.loads(index_json)
        raw_lens = index.values()
        raw_total_len = sum(raw_lens)
        raw_len_percents = [float(raw_len) / raw_total_len for raw_len in raw_lens]
        assert len(raw_len_percents) == len(index)
        lines = tokens_to_lines(tokens, raw_len_percents)
        assert len(lines) == len(index)
        for timestamp, line in zip(index.keys(), lines):
            vtt_out.write(timestamp)
            vtt_out.write("\n")
            vtt_out.write(line)
            vtt_out.write("\n\n")


def main():
    vtt_file = Path(sys.argv[1])
    assert vtt_file.suffix == ".vtt"
    idx_file = vtt_file.with_suffix(".idx")
    cooked_file = vtt_file.with_suffix(".ckd")
    cooked_vtt_file = vtt_file.with_suffix(".cooked.vtt")
    with (
        open(vtt_file) as vtt_in,
        open(idx_file) as idx_in,
        open(cooked_file) as cooked_in,
        open(cooked_vtt_file, "w") as vtt_out,
    ):
        cooked_to_vtt(vtt_in, idx_in, cooked_in, vtt_out)


if __name__ == "__main__":
    main()
