#!/usr/bin/env python3

"""
Advent of Code 2021 Day 11: Smoke Basin

https://adventofcode.com/2021/day/11

Solution by Eric Colton
"""

from os import environ
import re
from collections import deque
from typing import List, Dict, Tuple, Optional

def parse_input_data(raw_input: List[str]) -> List[List[int]]:
    return [list(map(lambda x: int(x), list(row.rstrip()))) for row in raw_input]

def neighbors(grid: List[List[int]], location: Tuple[int, int]):
    neighbors = []
    for delta in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]:
        candidate = location[0] + delta[0], location[1] + delta[1]
        if (candidate[0] < len(grid) and
            candidate[1] < len(grid[0]) and
            candidate[0] >= 0 and
            candidate[1] >= 0):
            neighbors.append(candidate)
    return neighbors

def simulate_one_round(grid: List[List[int]]) -> int:

    def increment(location: Tuple[int, int]):
        y, x = location
        grid[y][x] += 1
        if grid[y][x] > 9 and location not in has_fired:
            has_fired.add(location)
            [increment(n) for n in neighbors(grid, location)]

    has_fired = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            increment((y, x))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] > 9:
                grid[y][x] = 0

    return len(has_fired)

def simulate_rounds(grid: List[List[int]], rounds: int) -> int:
    return sum([simulate_one_round(grid) for _ in range(rounds)])

def simulate_until_all_flash(grid):
    target = len(grid) * len(grid[0])
    count = 1
    while simulate_one_round(grid) < target:
        count += 1
    return count

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        grid = parse_input_data(raw_input)
        part_1 = simulate_rounds(grid, 100)
        assert part_1 == 1719
        print(f"The solution to Part 1 is {part_1}")

        grid = parse_input_data(raw_input)
        part_2 = simulate_until_all_flash(grid)
        assert part_2 == 232
        print(f"The solution to Part 2 is {part_2}")
