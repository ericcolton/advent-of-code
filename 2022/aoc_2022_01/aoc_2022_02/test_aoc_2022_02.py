#!/usr/bin/env python3

import re
from aoc_2022_02 import parse_input_data, score_as_play, score_as_outcome, find_sum_scores

TEST_INPUT = """A Y
B X
C Z""".split("\n")

def test_score_as_play():
    data = parse_input_data(TEST_INPUT)
    assert score_as_play(data[0]) == 8
    assert score_as_play(data[1]) == 1
    assert score_as_play(data[2]) == 6
    assert find_sum_scores(data, False) == 15

def test_score_as_outcome():
    data = parse_input_data(TEST_INPUT)
    assert score_as_outcome(data[0]) == 4
    assert score_as_outcome(data[1]) == 1
    assert score_as_outcome(data[2]) == 7
    assert find_sum_scores(data, True) == 12

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
