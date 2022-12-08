#!/usr/bin/env python3

"""
Advent of Code 2022 Day 7: No Space Left On Device

https://adventofcode.com/2022/day/7

Solution by Eric Colton
"""

import re
from typing import List, Tuple

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
    root = Dir(None, "/")
    working_dir = None
    l = 0
    while l < len(raw_lines):
        line = raw_lines[l].rstrip()
        match_cd = re.match(r'\$ cd (.+)', line)
        match_ls = re.match(r'\$ ls', line)
        if match_cd:
            dir_name = match_cd.group(1)
            if dir_name == '/':
                working_dir = root
            elif dir_name == '..':
                working_dir = working_dir.parent
            else:
                if dir_name not in working_dir.contents:
                    raise Exception("Cannot cd into an unknown directory")
                working_dir = working_dir.contents[dir_name]
            l += 1
        elif match_ls:
            l += 1
            while l < len(raw_lines) and not re.match(r'\$', raw_lines[l]):
                ls_line = raw_lines[l].rstrip()
                match_file = re.match(r'(\d+) (.+)', ls_line)
                match_dir = re.match(r'dir (\w+)', ls_line)
                if match_file:
                    size, name = int(match_file.group(1)), match_file.group(2)
                    if name in working_dir.contents:
                        raise Exception("Unexpected duplicate file")
                    file = File(name, size)
                    working_dir.add(name, file)
                elif match_dir:
                    name = match_dir.group(1)
                    if name in working_dir.contents:
                        raise Exception("Unexpected duplicate dir")
                    dir = Dir(working_dir, name)
                    working_dir.add(name, dir)
                else:
                    raise Exception ("Unexpected ls line")
                l += 1
        else:
            raise Exception("Unexpected line")
    return root

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
