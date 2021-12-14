#!/usr/bin/env python3

import re
from aoc_2021_14 import parse_input_data, execute_insertion_rounds, find_min_max_counts

TEST_INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")

def test_run_10_rounds():
    input, pairs = parse_input_data(TEST_INPUT)
    data = execute_insertion_rounds(input, pairs, 10)
    min_count, max_count = find_min_max_counts(data)
    diff = max_count - min_count
    assert diff == 1588

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
