#!/usr/bin/env python3

"""
Advent of Code 2022 Day 4: Camp Cleanup

https://adventofcode.com/2022/day/4

Solution by Eric Colton
"""

import re
from functools import reduce
from typing import List, Tuple, Set

def parse_input_data(raw_lines: List[str]) -> List[Tuple]:
    data = []
    for line in raw_lines:
        match = re.match(r'(\d+)\-(\d+),(\d+)\-(\d+)', line)
        if match:
            range_1 = (int(match.group(1)), int(match.group(2)))
            range_2 = (int(match.group(3)), int(match.group(4)))
            data.append((range_1, range_2))
        else:
            raise Exception("unexpected record format")
    return data

def fully_contained(record: Tuple) -> bool:
    return ((record[0][0] <= record[1][0] and record[0][1] >= record[1][1])
        or (record[1][0] <= record[0][0] and record[1][1] >= record[0][1]))

def partially_contained(record: Tuple) -> bool:
    return ((record[0][0] <= record[1][0] and record[0][1] >= record[1][0])
        or (record[1][0] <= record[0][0] and record[1][1] >= record[0][0]))

def count_matching(data, compare_func):
    return sum(map(lambda a: compare_func(a), data))

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = count_matching(data, fully_contained)
        assert part_1 == 534
        print(f"The solution to Part 1 is {part_1}")

        part_2 = count_matching(data, partially_contained)
        assert part_2 == 841
        print(f"The solution to Part 2 is {part_2}")
