#!/usr/bin/env python3

"""
Advent of Code 2022 Day 17: Pyroclastic Flow

https://adventofcode.com/2022/day/17

Solution by Eric Colton
"""

import re
from typing import List, Dict, Tuple
from math import inf
from collections import namedtuple

Node = namedtuple("Node", ['name', 'rate', 'edges'])
Point = namedtuple("Point", ['y', 'x'])

class Shape:
    def __init__(self, type):
        self.points = []        
        if type == 0:
            self.input = [Point(0, 0), Point(0, 1), Point(0, 2), Point(0, 3)]
        elif type == 1:
            self.input = [Point(0, 1), Point(1, 0), Point(1, 1), Point(1, 2), Point(2, 1)]
        elif type == 2:
            self.input = [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2), Point(2, 2)]
        elif type == 3:
            self.input = [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]
        elif type == 4:
            self.input = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]

    def apply_horizontal_shift(self, dir):
        for i in range(len(self.points)):
            point = self.points[i]
            candidate_x = point.x + (1 if dir else -1)
            self.points[i] = Point(point.y, candidate_x)

    def apply_downward_shift(self):
        for i in range(len(self.points)):
            point = self.points[i]
            self.points[i] = Point(point.y - 1, point.x)

class JetManager:
    def __init__(self, data: List[bool]):
        self.i = 0
        self.data = data
    
    def get_jet(self):
        rv = self.data[self.i]
        self.i += 1
        if self.i == len(self.data):
            self.i = 0
        return rv

class Tetris:
    def __init__(self):
        self.base_height = 0
        self.height = 0
        self.grid = [[True] * 7]
        self.active_shape = None

    def add_shape(self, shape: Shape):
        high_watermark = 0
        points = []
        for i_point in shape.input:
            y = i_point.y + self.height + 4
            high_watermark = max(high_watermark, y)
            points.append(Point(y, i_point.x + 2))
        shape.points = points
        while len(self.grid) <= high_watermark:
            self.grid.append([False] * 7)
        self.active_shape = shape
    
    def apply_jet(self, dir: bool) -> bool:
        assert self.active_shape != None
        move_ok = True
        for point in self.active_shape.points:
            candidate_x = point.x + (1 if dir else -1)
            if candidate_x < 0 or candidate_x > 6:
                move_ok = False
                break
            if self.grid[point.y][candidate_x]:
                move_ok = False
                break
        if move_ok:
            self.active_shape.apply_horizontal_shift(dir)

        for point in self.active_shape.points:
            candidate_y = point.y - 1
            if self.grid[candidate_y][point.x]:
                self.solidify_active_shape()
                return False
        self.active_shape.apply_downward_shift()
        return True

    def solidify_active_shape(self):
        assert self.active_shape != None
        for point in self.active_shape.points:
            self.grid[point.y][point.x] = True
            self.height = max(self.height, point.y)
        self.active_shape = None
        min_y = inf
        if len(self.grid) > 100:
            self.base_height += 50
            self.grid = self.grid[50:]
            self.height -= 50

    def get_height(self) -> int:
        return self.base_height + self.height

    def has_active_shape(self):
        return self.active_shape != None

def run_tetris(data: List[bool], count):
    tetris = Tetris()
    jet_manager = JetManager(data)
    for i in range(count):
        tetris.add_shape(Shape(i % 5))
        while tetris.has_active_shape():
            tetris.apply_jet(jet_manager.get_jet())
    return tetris.get_height()

def run_tetris_until_repeat(data: List[bool]):
    tetris = Tetris()
    jet_manager = JetManager(data)
    i = 0
    while True:
        if i % 10000 == 0:
            print(f"i = {i}")
        if jet_manager.i == 0 and i % 5 == 0:
            print(f"({i}) height: {tetris.get_height()}")
        tetris.add_shape(Shape(i % 5))
        while tetris.has_active_shape():
            tetris.apply_jet(jet_manager.get_jet())
        i += 1
    return tetris.get_height()

def parse_line(line: str) -> Tuple[str, Node]:
    match = re.match(r'Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)', line)
    if not match:
        raise Exception("Unexpected line")
    edges = match.group(3).split(", ")
    return Node(match.group(1), int(match.group(2)), edges)

def parse_input_data(raw_lines: List[str]) -> List[Dict[str, Node]]:
    return list(map(lambda x: 1 if x == '>' else 0, raw_lines[0].rstrip()))

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = run_tetris(data, 2022)
        print(part_1)

        part_2 = run_tetris_until_repeat(data)
        print(part_2)
        # part_1 = find_max_pressure(node_lookup, 'AA', 30, frozenset(), {})
        # assert part_1 == 2124
        # print(f"The solution to Part 1 is {part_1}")

        # part_2 = find_max_pressure_with_elephant(node_lookup, 'AA', 'AA', 0, 26, frozenset(), set(), set(), {})
        # print(f"The solution to Part 2 is {part_2}")
        # assert part_1 == 2124



        # part_2 = find_tuning_frequency(data, 4000000)
        # assert part_2 == 13213086906101
        #
