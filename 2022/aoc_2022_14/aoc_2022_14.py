#!/usr/bin/env python3

"""
Advent of Code 2022 Day 14: Regolith Reservoir

https://adventofcode.com/2022/day/14

Solution by Eric Colton
"""

import re
from typing import List, Tuple
from collections import namedtuple
from math import inf

Point = namedtuple("Point", ["x", "y"])

class Reservoir:

    def __init__(self):
        self.filled = set()
        self.min_y = inf
        self.max_y = -inf

    def fill(self, p: Point) -> None:
        self.filled.add(p)
        self.max_y = max(self.max_y, p.y)
        self.min_y = min(self.min_y, p.y)

    def add_sand(self) -> bool:
        loc = Point(500, 0)
        while loc.y < self.max_y:
            if Point(loc.x, loc.y + 1) not in self.filled:
                loc = Point(loc.x, loc.y + 1)
                continue
            if Point(loc.x - 1, loc.y + 1) not in self.filled:
                loc = Point(loc.x - 1, loc.y + 1)
                continue
            if Point(loc.x + 1, loc.y + 1) not in self.filled:
                loc = Point(loc.x + 1, loc.y + 1)
                continue
            self.fill(loc)
            return True
        self.fill(loc)
        return False

def parse_line(line: str) -> List[Point]:
    coords = line.split(" -> ")
    pairs = []
    for c in coords:
        x, y = c.split(",")
        pairs.append(Point(int(x), int(y)))
    return pairs

def parse_input_data(raw_lines: List[str]) -> List[List[Point]]:
    return [parse_line(line.rstrip()) for line in raw_lines]

def draw_line(r: Reservoir, a: Point, b: Point) -> None:
    if a.x == b.x:
        low, hi = min(a.y, b.y), max(a.y, b.y)
        for iy in range(low, hi + 1):
            r.fill(Point(a.x, iy))
    elif a.y == b.y:
        low, hi = min(a.x, b.x), max(a.x, b.x)
        for ix in range(low, hi + 1):
            r.fill(Point(ix, a.y))
    else:
        raise Exception("Inconsistent line")

def draw_rock_lines(r: Reservoir, data: List[List[Point]]) -> None:
    for line in data:
        last_point = line[0]
        for i in range(1,len(line)):
            next_point = line[i]
            draw_line(r, last_point, next_point)
            last_point = next_point

def add_sand_until_overflow(r: Reservoir) -> int:
    count = 0
    while r.add_sand():
        count += 1
    return count

def add_sand_until_full(r: Reservoir) -> int:
    count = 0
    while r.min_y > 0:
        r.add_sand()
        count += 1
    return count

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        r = Reservoir()
        draw_rock_lines(r, data)
        part_1 = add_sand_until_overflow(r)
        assert part_1 == 1298
        print(f"The solution to Part 1 is {part_1}")

        r = Reservoir()
        draw_rock_lines(r, data)
        r.max_y += 1
        part_2 = add_sand_until_full(r)
        assert part_2 == 25585        
        print(f"The solution to Part 2 is {part_2}")
