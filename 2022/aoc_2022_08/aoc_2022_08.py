#!/usr/bin/env python3

"""
Advent of Code 2022 Day 8: Treetop Tree House

https://adventofcode.com/2022/day/8

Solution by Eric Colton
"""

import re
from typing import List

class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.contents = {}
        self.name = name

    def add(self, name, item):
        self.contents[name] = item

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def parse_input_data(raw_lines: List[str]) -> Dir:
    return [c for c in line.rstrip() for line in raw_lines]

def find_dir_sizes(node: object) -> Tuple[int, List[int]]:
    if isinstance(node, File):
        return (node.size, [])
    elif isinstance(node, Dir):
        cum_size, sub_dirs = 0, []
        for c in node.contents.values():
            size, dir_list = find_dir_sizes(c)
            cum_size += size
            sub_dirs.extend(dir_list)
        sub_dirs.append(cum_size)
        return (cum_size, sub_dirs)
    else:
        raise Exception(f"unexpected content node: {node}")

def find_sum_small_dir_sizes(sizes: List[int]) -> int:
    return sum(filter(lambda x: x <= 100000, sizes))

def find_best_deletion_candidate_size(total_size: int, sizes: List[int]) -> int:
    target = total_size - 40000000
    if target < 0:
        return 0
    sizes = sorted(sizes)
    left, right = 0, len(sizes) - 1
    best = 0
    while left <= right:
        mid = left + (right - left) // 2
        if sizes[mid] == target:
            best = sizes[mid]
        if sizes[mid] < target:
            left = mid + 1
        elif sizes[mid] > target:
            right = mid - 1
            best = sizes[mid]
    return best

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
