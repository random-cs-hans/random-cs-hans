#!/usr/bin/env python3

import itertools
import re
import sys
from contextlib import ExitStack
from pathlib import Path
from tempfile import TemporaryDirectory

WHITE_SPACE_REGEX = re.compile(r"^\s*$")


def create_compare_file(compare_file: Path, files: list[Path]):
    def iter_non_whitespace_paragraphs(file_path: Path):
        with open(file_path) as fd:
            for line in fd:
                if WHITE_SPACE_REGEX.match(line):
                    continue
                yield line

    with (
        TemporaryDirectory(dir=compare_file.parent) as tmp_dir_name,
        ExitStack() as exit_stack,
    ):
        tmp_file = Path(tmp_dir_name) / compare_file.name
        fout = exit_stack.enter_context(open(tmp_file, "w"))
        fout.write("\n".join([str(p) for p in files]))
        fout.write("\n---\n\n")

        for lines in itertools.zip_longest(
            *(iter_non_whitespace_paragraphs(p) for p in files),
            fillvalue="!!!EMPTY!!!\n",
        ):
            for idx, line in enumerate(lines):
                fout.write("@")
                fout.write(files[idx].stem.split(".", 1)[-1])
                fout.write("@")
                fout.write(line)
            fout.write("\n")
        tmp_file.rename(compare_file)


def main():
    vtt_file = Path(sys.argv[1])
    assert vtt_file.suffix == ".vtt"
    files = [
        vtt_file.with_suffix(".raw"),
        *vtt_file.parent.glob(vtt_file.with_suffix(".*.txt").name),
    ]
    compare_file = vtt_file.with_suffix(".cmp")
    create_compare_file(compare_file, files)


if __name__ == "__main__":
    main()
