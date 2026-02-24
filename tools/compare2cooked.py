#!/usr/bin/env python3

import itertools
import sys
from pathlib import Path


def compare_to_cooked(compare_file: Path, cooked_file: Path):
    with open(compare_file) as fin, open(cooked_file, "w") as fout:
        for line in fin:
            if line == "---\n":
                break

        last_line = ""
        for line in fin:
            if line.isspace():
                fout.write(last_line)
                last_line = ""
            else:
                last_line = line
        if last_line:
            fout.write(last_line)


def main():
    vtt_file = Path(sys.argv[1])
    assert vtt_file.suffix == ".vtt"
    compare_file = vtt_file.with_suffix(".cmp")
    cooked_file = vtt_file.with_suffix(".ckd")
    compare_to_cooked(compare_file, cooked_file)


if __name__ == "__main__":
    main()
