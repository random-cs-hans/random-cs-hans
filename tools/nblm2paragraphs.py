#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

WRONG_SENTENCE_ENDINGS = frozenset([",", "，", "?", "!", "。", "？", "！", "…"])


def nblm_xml_to_txt(xml_file: Path, txt_file: Path):
    """Parse VTT file into structured segments"""

    root = ET.fromstring(xml_file.read_text())

    is_empty = True
    should_break = False

    def do_iter(node):
        nonlocal is_empty, should_break
        if node.tag == "button":
            should_break = True
        elif node.text:
            text = node.text
            if not text.isspace():
                if text[0] in WRONG_SENTENCE_ENDINGS:
                    txt_out.write(text[0])
                    text = text[1:]
                if should_break:
                    if not is_empty:
                        txt_out.write("\n")
                    is_empty = True
                    should_break = False
                if text:
                    txt_out.write(text)
                    is_empty = False
        else:
            for child in node:
                do_iter(child)

    with open(txt_file, "a") as txt_out:
        do_iter(root)


def main():
    xml_file = Path(sys.argv[1])
    assert xml_file.suffix == ".xml"
    txt_file = xml_file.with_suffix(".txt")
    nblm_xml_to_txt(xml_file, txt_file)


if __name__ == "__main__":
    main()
