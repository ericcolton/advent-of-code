#!/usr/bin/env python3

import re
from aoc_2023_03 import parse_input_data, count_sum_adjacent_parts, count_sum_gear_ratios

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")

def test_count_sum_adjacent_parts():
    data = parse_input_data(TEST_INPUT)
    part_1 = count_sum_adjacent_parts(data)
    assert(part_1 == 4361)

def test_count_sum_gear_ratios():
    data = parse_input_data(TEST_INPUT)
    part_2 = count_sum_gear_ratios(data)
    assert(part_2 == 467835)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
