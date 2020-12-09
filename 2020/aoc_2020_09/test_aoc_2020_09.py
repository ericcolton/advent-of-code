#!/usr/bin/env python3

import re
from aoc_2020_09 import parse_input_data, find_first_invalid_index, find_range_that_sums_to_index, find_sum_max_and_min_in_range

TEST_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".split("\n")

def test_find_invalid_index():
    data = parse_input_data(TEST_INPUT)
    index = find_first_invalid_index(data, 5)
    assert data[index] == 127

def test_find_range_that_sums_to_index():
    data = parse_input_data(TEST_INPUT)
    index = find_first_invalid_index(data, 5)
    lower, upper = find_range_that_sums_to_index(index, data)
    rv = find_sum_max_and_min_in_range(lower, upper, data)
    assert rv == 62

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")