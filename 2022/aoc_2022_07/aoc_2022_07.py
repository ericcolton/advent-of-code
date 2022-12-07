#!/usr/bin/env python3

"""
Advent of Code 2022 Day 7: No Space Left On Device

https://adventofcode.com/2022/day/7

Solution by Eric Colton
"""

import re
from typing import List

class Dir:
    def __init__(self, name):
        self.contents = {}
        self.name = name

    def add(self, name, item):
        self.contents[name] = item

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def parse_input_data(raw_lines: List[str]) -> Dir:
    path_components, path, working_dir = [], "", None
    l = 0
    while l < len(raw_lines):
        line = raw_lines[l].rstrip()
        match_cd = re.match(r'\$ cd (.+)', line)
        match_ls = re.match(r'\$ ls', line)
        if match_cd:
            dir_name = match_cd.group(1)
            if dir == '/':
                path_components.clear()
            elif dir == '..':
                path_components.pop()
            else:
                path_components.append(dir_name)
            path = "/".join(path_components)
            l += 1
        elif match_ls:
            l += 1
            while l < len(raw_lines) and not re.match(r'\$', raw_lines[l]):
                ls_line = raw_lines[l].rstrip()
                match_file = re.match(r'(\d+) (.+)', ls_line)
                match_dir = re.match(r'dir (\w+)', ls_line)
                if match_file:
                    size, name = match_file.group(1), match_file.group(2)
                    if name in dir_at_path[path].contents:
                        raise Exception("Unexpected duplicate file")
                    file = File(name, size)
                    dir_at_path[path].add(name, file)
                elif match_dir:
                    name = match_dir.group(1)
                    if name in dir_at_path[path].contents:
                        raise Exception("Unexpected duplicate dir")
                    dir_path = current + name
                    dir = Dir(name)
                    if dir_at_path[path]
                    dir_at_path[path].add(name, dir)
                else:
                    raise Exception ("Unexpected ls line")
                l += 1
        else:
            raise Exception("Unexpected line")
    return dir_at_path[""]

        
                    






    

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
