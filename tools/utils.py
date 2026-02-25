#!/usr/bin/env python3

import math
import re
from dataclasses import dataclass
from enum import Enum

SENTENCE_ENDINGS = frozenset([".", "?", "!", "。", "？", "！", "-", "—", "…", '"', "”"])

# Copied from
# https://github.com/EloiseSeverin/markdown_cjk_spacing/blob/master/markdown_cjk_spacing/cjk_spacing.py
# Also see
# https://steam.oxxostudio.tw/category/python/example/remove-blank.html
RANGE_CN = (
    ("\u3000", "\u303f"),  # CJK Symbols and Punctuation
    ("\u3400", "\u4db5"),  # CJK Unified Ideographs Extension A
    ("\u4e00", "\u9fef"),  # CJK Unified Ideographs
    ("\uf900", "\ufaff"),  # CJK Compatibility Ideographs
    ("\U00020000", "\U0002a6d6"),  # CJK Unified Ideographs Extension B
    ("\U0002a700", "\U0002b734"),  # CJK Unified Ideographs Extension C
    ("\U0002b740", "\U0002b81d"),  # CJK Unified Ideographs Extension D
    ("\U0002b820", "\U0002cea1"),  # CJK Unified Ideographs Extension E
    ("\U0002ceb0", "\U0002ebe0"),  # CJK Unified Ideographs Extension F
    ("\U0002f800", "\U0002fa1f"),  # CJK Compatibility Ideographs Supplement
    ("\uff00", "\uffee"),  # Halfwidth and Fullwidth Forms
)

WORD_REGEX = re.compile(
    "".join(
        [
            r"([a-zA-Z0-9]+)|([",
            *(f"{x}-{y}" for x, y in RANGE_CN),
            r"]+)|(\s+)",
        ]
    )
)


class TokenType(Enum):
    ALNUM = 0
    CN = 1
    WHITESPACE = 2
    OTHER = 3


@dataclass
class Token:
    t: TokenType
    val: str = ""


def paragraph_to_tokens(paragraph: str, nlp) -> list[Token]:
    tokens: list[Token] = []
    last_idx = 0
    for match in WORD_REGEX.finditer(paragraph):
        if match.start() != last_idx:
            tokens.append(Token(TokenType.OTHER, paragraph[last_idx : match.start()]))
        if match.group(1):
            if tokens and tokens[-1].t == TokenType.CN:
                tokens.append(Token(TokenType.WHITESPACE))
            tokens.append(Token(TokenType.ALNUM, match.group(1)))
        elif match.group(2):
            if tokens and tokens[-1].t == TokenType.ALNUM:
                tokens.append(Token(TokenType.WHITESPACE))
            elif (
                len(tokens) > 1
                and tokens[-2].t == TokenType.CN
                and tokens[-1].t == TokenType.WHITESPACE
            ):
                tokens.pop()
            doc = nlp(match.group(2))
            tokens.extend(Token(TokenType.CN, w.text) for w in doc)
        else:
            tokens.append(Token(TokenType.WHITESPACE))
        last_idx = match.end()
    if last_idx < len(paragraph):
        tokens.append(Token(TokenType.OTHER, paragraph[last_idx:]))
    return tokens


def tokens_to_lines(tokens: list[Token], raw_len_percents: list[float]) -> list[str]:
    lines: list[str] = []
    token_idx = 0
    for idx, raw_len_percent in enumerate(raw_len_percents):
        token_strs = []
        if idx + 1 < len(raw_len_percents):
            tokens_in_line = math.floor(raw_len_percent * len(tokens))
        else:
            tokens_in_line = len(tokens) - token_idx
        for i in range(token_idx, token_idx + tokens_in_line):
            if tokens[i].t == TokenType.WHITESPACE:
                if not token_strs or i + 1 == token_idx + tokens_in_line:
                    continue
                token_strs.append(" ")
            else:
                token_strs.append(tokens[i].val)
        token_idx += tokens_in_line
        while token_idx < len(tokens) and tokens[token_idx].t == TokenType.OTHER:
            token_strs.append(tokens[token_idx].val)
            token_idx += 1
        lines.append("".join(token_strs))
    return lines


def iter_vtt_paragraphs(vtt_in):
    indexes = {}
    segments = []
    prev_ts = ""
    prev_ts_chars = 0

    for line in vtt_in:
        line = line.strip()
        if " --> " in line:
            prev_ts = line
            break

    def flush_timestamp(line):
        nonlocal indexes, prev_ts, prev_ts_chars
        indexes[prev_ts] = prev_ts_chars
        prev_ts = line
        prev_ts_chars = 0

    def flush_paragraph():
        nonlocal indexes, segments
        indexes = {}
        segments = []

    for line in vtt_in:
        line = line.strip()
        if not line:
            continue
        if " --> " in line:
            flush_timestamp(line)
            if segments and segments[-1][-1] in SENTENCE_ENDINGS:
                yield indexes, segments
                flush_paragraph()
            continue
        prev_ts_chars += len(line)
        segments.append(line)

    if segments:
        flush_timestamp("")
        yield indexes, segments
        flush_paragraph()
