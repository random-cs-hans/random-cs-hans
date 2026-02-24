#!/usr/bin/env python3

import itertools
import json
import math
import sys
from contextlib import ExitStack
from pathlib import Path

import spacy

from utils import iter_vtt_paragraphs, paragraph_to_tokens, tokens_to_lines


def vtts_to_blog(vtt_ins, blog_out):
    nlp = spacy.load("zh_core_web_sm")

    for g in zip(*[iter_vtt_paragraphs(vtt_in) for vtt_in in vtt_ins]):
        first_indexes = None
        for idx, (indexes, segments) in enumerate(g):
            if not first_indexes:
                first_indexes = indexes
                tokens = next(iter(indexes)).split(" --> ", maxsplit=2)
                assert len(tokens) == 2
                start = tokens[0].strip()
                end = tokens[1].strip()
                blog_out.write(
                    f'{{{{< track-segment start="{start}" end="{end}" >}}}}\n'
                )
            else:
                assert list(indexes.keys()) == list(first_indexes.keys()), (
                    f"{list(indexes.keys())}, {list(first_indexes.keys())}"
                )
            lang = vtt_ins[idx].name.rsplit(".", maxsplit=3)[-2]
            blog_out.write(f'{{{{< styled-paragraph class="lang-{lang}" >}}}}')
            lines = tokens_to_lines(paragraph_to_tokens(" ".join(segments), nlp), [1])
            assert len(lines) == 1
            blog_out.write(lines[0])
            blog_out.write("{{< /styled-paragraph >}}\n")
        blog_out.write("{{< /track-segment >}}\n\n")

    # for line in vtt_in:
    #     vtt_out.write(line)
    #     if " --> " in line:
    #         break
    #
    #
    # segments = []
    #
    # def flush_paragraph():
    #     nonlocal segments
    #     lines = tokens_to_lines(paragraph_to_tokens(" ".join(segments), nlp), [1])
    #     assert len(lines) == 1
    #     vtt_out.write(lines[0])
    #     vtt_out.write("\n\n")
    #     segments.clear()
    #
    # for line in vtt_in:
    #     if " --> " in line:
    #         flush_paragraph()
    #         vtt_out.write(line)
    #         continue
    #     line = line.strip()
    #     if line:
    #         segments.append(line)
    #
    # flush_paragraph()


def main():
    blog_file = Path(sys.argv[1])
    assert blog_file.suffix == ".md"
    vtt_files = reversed(
        sorted(list(blog_file.parent.glob(blog_file.with_suffix(".*.vtt").name)))
    )
    vtt_ins = []
    with (
        ExitStack() as exit_stack,
        open(blog_file, "w") as vtt_out,
    ):
        for vtt_file in vtt_files:
            vtt_ins.append(exit_stack.enter_context(open(vtt_file)))
        vtts_to_blog(vtt_ins, vtt_out)


if __name__ == "__main__":
    main()
