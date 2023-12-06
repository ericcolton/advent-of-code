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

class Mapper:

    def __init__(self, maps):
        self._maps = maps
        self._memo = {}
        self._hits = 0
        self._misses = 0

    def _remap_with_mapping(self, target, mapping):
        left, right = 0, len(mapping) - 1
        match = None
        while left <= right:
            mid = left + (right - left) // 2
            if mapping[mid].src_start == target:
                match = mapping[mid]
                break
            elif mapping[mid].src_start < target:
                match = mapping[mid]
                left = mid + 1
            else:
                right = mid - 1
        if match:
            offset = target - match.src_start
            assert offset >= 0
            if offset < match.range_len:
                return match.dest_start + offset
        return target

    def find_location(self, seed):
        if self._hits + self._misses % 1000 == 0:
            print(f"hits = {self._hits}\tmisses = {self._misses}")
        if seed not in self._memo:
            index = seed
            for mapping in self._maps:
                index = self._remap_with_mapping(index, mapping)
            rv = index
            self._memo[seed] = rv
            self._misses += 1
        else:
            self._hits += 1
        return self._memo[seed]

def find_lowest_location_with_ranges(data):
    initial_seeds, maps = data
    mapper = Mapper(maps)
    lowest = inf
    for index in range(0, len(initial_seeds), 2):
        start, length = initial_seeds[index], initial_seeds[index + 1]
        for seed in range(start, start + length):
            lowest = min(lowest, mapper.find_location(seed))
    return lowest

def find_lowest_location(data):
    initial_seeds, maps = data
    mapper = Mapper(maps)
    lowest = inf
    for seed in initial_seeds:
        lowest = min(lowest, mapper.find_location(seed))
    return lowest

def parse_input_data(raw_lines: str) -> tuple[List[int], List[int]]:
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
        #assert part_2 == 226172555
        print(f"The solution to Part 2 is {part_2}")


       # part_2 = count_sum_gear_ratios(data)
       # assert part_2 == 81997870
       # print(f"The solution to Part 2 is {part_2}")
