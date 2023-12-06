#!/usr/bin/env python3

import re
from aoc_2023_05 import parse_input_data

TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n")

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
