#!/usr/bin/env python3

import re
from aoc_2023_04 import parse_input_data, count_total_points, count_cascading_scratchcards

TEST_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split("\n")

def test_count_total_points():
    data = parse_input_data(TEST_INPUT)
    part_1 = count_total_points(data)
    assert(part_1 == 13)

def test_count_cascading_scrathcards():
    data = parse_input_data(TEST_INPUT)
    part_2 = count_cascading_scratchcards(data)
    assert(part_2 == 30)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
