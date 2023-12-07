#!/usr/bin/env python3

import re
from aoc_2023_06 import parse_input_data, product_of_ways_to_win

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200""".split("\n")

def test_product_of_ways_to_win():
    data = parse_input_data(TEST_INPUT)
    part_1 = product_of_ways_to_win(data[0])
    assert(part_1 == 288)

def test_ways_to_win():
    data = parse_input_data(TEST_INPUT)
    part_2 = product_of_ways_to_win(data[1])
    assert(part_2 == 71503)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
