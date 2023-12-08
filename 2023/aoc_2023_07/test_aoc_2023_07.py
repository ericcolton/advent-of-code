#!/usr/bin/env python3

import re
from aoc_2023_07 import parse_input_data, find_sum_of_winnings

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")

def test_sum_of_winnings():
    data = parse_input_data(TEST_INPUT)
    part_1 = find_sum_of_winnings(data, False)
    assert(part_1 == 6440)

def test_sum_of_winnings_with_jokers():
    data = parse_input_data(TEST_INPUT)
    part_2 = find_sum_of_winnings(data, True)
    assert(part_2 == 5905)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
