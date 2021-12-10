#!/usr/bin/env python3

"""
Advent of Code 2021 Day 9: Smoke Basin

https://adventofcode.com/2021/day/9

Solution by Eric Colton
"""

import re
from collections import deque
from functools import reduce
from typing import List, Dict, Tuple

def parse_input_data(raw_input: List[str]) -> List[List[int]]:
    return [list(map(lambda c: int(c), row.rstrip())) for row in raw_input]

def neighbors(grid: List[List[int]], p: Tuple[int, int]) -> List[Tuple[int, int]]:
    candidates = []
    for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if (p[0] + delta[0] < len(grid) and
            p[0] + delta[0] >= 0 and
            p[1] + delta[1] < len(grid[0]) and
            p[1] + delta[1] >= 0):
            candidates.append((p[0] + delta[0], p[1] + delta[1]))
    return candidates

def find_basin_sizes(grid: List[List[int]], low_points: List[Tuple[int, int]]) -> List[int]:
    basin_sizes = []
    seen = set()
    for point in low_points:
        if point in seen:
            continue
        basin_size = 0
        queue = deque([point])
        seen.add(point)
        while len(queue) > 0:
            p = queue.pop()
            basin_size += 1
            for n in neighbors(grid, p):
                if n not in seen and grid[n[0]][n[1]] < 9:
                    seen.add(n)
                    queue.appendleft(n)
        basin_sizes.append(basin_size)
    return sorted(basin_sizes)

def find_low_points(grid: List[List[int]]) -> List[Tuple[int, int]]:
    low_points = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            is_min = True
            for n in neighbors(grid, (y, x)):
                if grid[n[0]][n[1]] <= grid[y][x]:
                    is_min = False
                    break
            if is_min:
                low_points.append((y, x))
    return low_points

def sum_risk_levels(grid: List[List[int]], low_points: List[Tuple[int, int]]) -> int:
    return sum(list(map(lambda p: grid[p[0]][p[1]] + 1, low_points)))

def product_three_largest_basins(basin_sizes):
    return reduce(lambda x, y: x * y, sorted(basin_sizes)[-3:], 1)

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        grid = parse_input_data(raw_input)
        low_points = find_low_points(grid)
        part_1 = sum_risk_levels(grid, low_points)
        assert part_1 == 448
        print(f"The solution to Part 1 is {part_1}")

        basin_sizes = find_basin_sizes(grid, low_points)
        part_2 = product_three_largest_basins(basin_sizes)
        assert part_2 == 1417248
        print(f"The solution to Part 2 is {part_2}")
