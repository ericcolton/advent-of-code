#!/usr/bin/env python3

"""
 Advent of Code 2023 Day 5: If You Give A Seed A Fertilizer

https://adventofcode.com/2023/day/5

Solution by Eric Colton
"""

import re
from typing import Set, Dict, List
from math import inf
from collections import namedtuple

Mapping = namedtuple("Mapping", ["dest_start", "src_start", "range_len"])

def remap_with_mapping(target: int, mapping: List[List[int]]):
    left, right = 0, len(mapping) - 1
    match_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if mapping[mid].src_start == target:
            match_index = mid
            break
        elif mapping[mid].src_start < target:
            match_index = mid
            left = mid + 1
        else:
            right = mid - 1
    if match_index >= 0:
        match = mapping[match_index]
        offset = target - match.src_start
        assert offset >= 0
        if offset < match.range_len:
            next_change = match.range_len - offset
            return match.dest_start + offset, next_change
        elif match_index < len(mapping) - 1:
            return target, mapping[match_index + 1].src_start - target
        else:
            return target, inf
    return target, mapping[0].src_start - target

def find_location(seed: int, maps: List[List[List[int]]]):
    index, lowest_next_change = seed, inf
    for mapping in maps:
        index, next_change = remap_with_mapping(index, mapping)
        lowest_next_change = min(lowest_next_change, next_change)
    return index, lowest_next_change

def find_lowest_location_with_ranges(data: tuple[List[int], List[List[List[int]]]]) -> int:
    initial_seeds, maps = data
    lowest_location = inf
    index = 0
    for index in range(0, len(initial_seeds), 2):
        start, length = initial_seeds[index], initial_seeds[index + 1]
        seed = start
        while seed < start + length:
            location, lowest_next_change = find_location(seed, maps)
            lowest_location = min(lowest_location, location)
            seed += lowest_next_change
    return lowest_location

def find_lowest_location(data: tuple[List[int], List[List[List[int]]]]) -> int:
    initial_seeds, maps = data
    lowest = inf
    for seed in initial_seeds:
        location, _ = find_location(seed, maps)
        lowest = min(lowest, location)
    return lowest

def parse_input_data(raw_lines: str) -> tuple[List[int], List[List[List[int]]]]:
   i_match = re.match(r'seeds\:\s+(.*)\s*', raw_lines[0].rstrip())
   if i_match:
       initial_seeds = list(map(int, i_match.group(1).split(' ')))
   else:
       raise Exception('unable to parse initial seeds')

   maps = []
   line_num = 2
   while line_num < len(raw_lines):
       line_num += 1
       line_data = []
       while line_num < len(raw_lines) and raw_lines[line_num].rstrip() != '':
           entry = list(map(int, raw_lines[line_num].rstrip().split(" ")))
           line_data.append(Mapping(*entry))
           line_num += 1
       line_num += 1
       line_data.sort(key=lambda m: m.src_start)
       maps.append(line_data)
   return initial_seeds, maps


if __name__ == '__main__':
   input_filename = __file__.strip('.py') + '_input.txt'
   with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_lowest_location(data)
        assert part_1 == 226172555
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_lowest_location_with_ranges(data)
        assert part_2 == 47909639
        print(f"The solution to Part 2 is {part_2}")