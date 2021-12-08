#!/usr/bin/env python3

"""
Advent of Code 2021 Day 67: The Treachery of Whales

https://adventofcode.com/2021/day/7

Solution by Eric Colton
"""

import math
from typing import List

def parse_input_data(raw_input: List[str]) -> List[int]:
    return [int(i) for i in raw_input[0].rstrip().split(',')]

def find_median(positions: List[int]) -> int:
    spos = sorted(positions)
    mid = (len(spos) - 1) // 2
    return sum(spos[mid:mid+2]) // 2 if len(spos) % 2 == 0 else spos[mid]

def find_optimal_candidates(positions):
    floor = math.floor(sum(positions) / len(positions))
    ceil = math.ceil(sum(positions) / len(positions))
    return [floor] if floor == ceil else [floor, ceil]

def find_fuel_required_linear(positions: List[int], location: int) -> int:
    return sum(list(map(lambda p: abs(p - location), positions)))

def find_fuel_required_plustorial(positions, location: int) -> int:
    return sum(list(map(lambda p: abs(p - location) * (abs(p - location) + 1) // 2, positions)))

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        positions = parse_input_data(raw_input)
        location = find_median(positions)
        part_1 = find_fuel_required_linear(positions, location)
        assert part_1 == 328318
        print(f"The solution to Part 1 is {part_1}")

        candidates = find_optimal_candidates(positions)
        part_2 = min(list(map(lambda loc: find_fuel_required_plustorial(positions, loc), candidates)))
        assert part_2 == 89791146
        print(f"The solution to Part 2 is {part_2}")
