#!/usr/bin/env python3

"""
Advent of Code 2022 Day 9: Rope Bridge

https://adventofcode.com/2022/day/9

Solution by Eric Colton
"""

import re
from typing import List, Tuple

class KnotMap:
    def __init__(self):
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_visited = set([(0, 0)])
    
    def exec_instrs(self, instrs: List[Tuple[str, int]]):
        for i in instrs:
            dir, count = i
            for _ in range(count):
                self.move(dir)
    
    def move(self, dir: str):
        y, x = self.head
        if dir == 'U':
            self.head = y + 1, x
        elif dir == 'D':
            self.head = y - 1, x
        elif dir == 'R':
            self.head = y, x + 1
        elif dir == 'L':
            self.head = y, x - 1
        else:
            raise Exception("Unexpected direction")
        
        hy, hx = self.head
        ty, tx = self.tail
        
        if hy - ty == 2:
            self.tail = ty + 1, hx
        elif hy - ty == -2:
            self.tail = ty - 1, hx
        elif hx - tx == 2:
            self.tail = hy, tx + 1
        elif hx - tx == -2:
            self.tail = hy, tx - 1
        
        self.tail_visited.add(self.tail)

def parse_input_data(raw_lines: List[str]) -> List[Tuple[str, int]]:
    data = []
    for line in raw_lines:
        match = re.match(r'(\w) (\d+)', line.rstrip())
        if match:
            data.append((match.group(1), int(match.group(2))))
        else:
            raise Exception("Unexpected line")
    return data

def find_tail_visited_count(knot_map: KnotMap) -> int:
    return len(knot_map.tail_visited)

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        instrs = parse_input_data(raw_input)
        knot_map = KnotMap()
        knot_map.exec_instrs(instrs)
        part_1 = find_tail_visited_count(knot_map)
        assert part_1 == 6090
        print(f"The solution to Part 1 is {part_1}")

