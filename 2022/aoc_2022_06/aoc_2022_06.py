#!/usr/bin/env python3

"""
Advent of Code 2022 Day 6: Tuning Trouble

https://adventofcode.com/2022/day/6

Solution by Eric Colton
"""

import re
from typing import List

def parse_input_data(raw_lines: List[str]) -> str:
    return raw_lines[0]

def find_start_marker(data: str, k: int) -> int:
    for i in range(len(data) - k - 1):
        s = set(data[i:i+k])
        if len(s) == k:
            return i + k
    raise Exception("start marker not found")

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_start_marker(data, 4)
        assert part_1 == 1093
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_start_marker(data, 14)
        assert part_2 == 3534
        print(f"The solution to Part 2 is {part_2}")
