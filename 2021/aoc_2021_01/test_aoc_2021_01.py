#!/usr/bin/env python3

import re
from aoc_2021_01 import parse_input_data, count_increasing_depths, count_increasing_depths_3_window

TEST_INPUT = """199
200
208
210
200
207
240
269
260
263""".split("\n")

def test_count_increasing_depths():
    data = parse_input_data(TEST_INPUT)
    result = count_increasing_depths(data)
    assert result == 7

def test_count_increasing_depths_3_window():
    data = parse_input_data(TEST_INPUT)
    result = count_increasing_depths_3_window(data)
    assert result == 5

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
