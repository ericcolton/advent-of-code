#!/usr/bin/env python3

"""
Advent of Code 2021 Day 15: Chiton

https://adventofcode.com/2021/day/15

Solution by Eric Colton
"""

import re
from collections import namedtuple, deque
from typing import List, Dict, Tuple, Set, Optional

Point = namedtuple('Point', ['y', 'x'])

class Grid:
    def __init__(self, data: List[List[int]], expanded: bool):
        self.data = data
        self.expanded = expanded
    
    def length_x(self):
        length = len(self.data[0])
        return 5 * length if self.expanded else length
    
    def length_y(self):
        length = len(self.data)
        return 5 * length if self.expanded else length
    
    def get(self, point: Point) -> int:
        val = self.data[point.y % len(self.data)][point.x % len(self.data[0])]
        y_factor, x_factor = point.y // len(self.data), point.x // len(self.data[0])
        val += y_factor + x_factor
        return val if val < 10 else val % 10 + 1

def parse_input_data(raw_input: List[str]) -> List[List[int]]:
    return [list(map(lambda x: int(x), line.rstrip())) for line in raw_input]

def neighbors(grid: Grid, point: Point) -> List[Point]:
    neighbors = []
    for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        y, x = point.y + delta[0], point.x + delta[1]
        if y >= 0 and x >= 0 and y < grid.length_y() and x < grid.length_x():
            neighbors.append(Point(y, x))
    return neighbors

def find_length_min_path(grid: Grid) -> int:
    origin = Point(0, 0)
    queue = deque([origin])
    lengths = {origin: 0}
    while len(queue) > 0:
        point = queue.pop()
        for n in neighbors(grid, point):
            n_length = lengths[point] + grid.get(n)
            if n not in lengths or n_length < lengths[n]:
                lengths[n] = n_length
                queue.appendleft(n)
    return lengths[Point(grid.length_y() - 1, grid.length_x() - 1)]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        grid_data = parse_input_data(raw_input)
        grid = Grid(grid_data, False)
        part_1 = find_length_min_path(grid)
        assert part_1 == 583
        print(f"The solution to Part 1 is {part_1}")

        grid_expanded = Grid(grid_data, True)
        part_2 = find_length_min_path(grid_expanded)
        assert part_1 == 2927
        print(f"The solution to Part 2 is {part_2}")


