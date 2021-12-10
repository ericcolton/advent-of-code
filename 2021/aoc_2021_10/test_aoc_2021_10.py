#!/usr/bin/env python3

import re
from aoc_2021_10 import parse_input_data, collect_first_corrupted, score_first_corrupted, collect_completions, score_completions

TEST_INPUT = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".split("\n")

def test_score_first_corrupted():
    records = parse_input_data(TEST_INPUT)
    first_corrupted = collect_first_corrupted(records)
    score = score_first_corrupted(first_corrupted)
    assert score == 26397

def test_score_completions():
    records = parse_input_data(TEST_INPUT)
    completions = collect_completions(records)
    score = score_completions(completions)
    assert score == 288957

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
