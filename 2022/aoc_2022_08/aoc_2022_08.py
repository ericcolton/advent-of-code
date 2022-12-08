#!/usr/bin/env python3

"""
Advent of Code 2022 Day 8: Treetop Tree House

https://adventofcode.com/2022/day/8

Solution by Eric Colton
"""

import re
from typing import List

def parse_input_data(raw_lines: List[str]) -> List[List[str]]:
    return [line.rstrip() for line in raw_lines]

def find_visible(data: List[str]) -> List[List[bool]]:
    len_row = len(data[0])
    visible = [[False] * len_row for _ in range(len(data))]
    for y in range(len(data)):
        water_mark = 0
        for x in range(len_row):
            



    return visible

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        root = parse_input_data(raw_input)
        total_size, dir_sizes = find_dir_sizes(root)
        part_1 = find_sum_small_dir_sizes(dir_sizes)
        assert part_1 == 1454188
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_best_deletion_candidate_size(total_size, dir_sizes)
        assert part_2 == 4183246
        print(f"The solution to Part 2 is {part_2}")
