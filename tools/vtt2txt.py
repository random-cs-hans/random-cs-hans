#!/usr/bin/env python3

import json
import sys
from pathlib import Path

from utils import iter_vtt_paragraphs


def vtt_to_paragraphs(vtt_in, idx_out, raw_out):
    """Parse VTT file into structured segments"""

    for indexes, segments in iter_vtt_paragraphs(vtt_in):
        json.dump(indexes, idx_out)
        idx_out.write("\n")
        raw_out.write(" ".join(segments))
        raw_out.write("\n")


def main():
    vtt_file = Path(sys.argv[1])
    assert vtt_file.suffix == ".vtt"
    idx_file = vtt_file.with_suffix(".idx")
    raw_file = vtt_file.with_suffix(".raw")
    with (
        open(vtt_file) as vtt_in,
        open(idx_file, "w") as idx_out,
        open(raw_file, "w") as raw_out,
    ):
        vtt_to_paragraphs(vtt_in, idx_out, raw_out)


if __name__ == "__main__":
    main()
