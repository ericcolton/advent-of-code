#!/usr/bin/env python3

"""
Advent of Code 2022 Day 9: Rope Bridge

https://adventofcode.com/2022/day/9

Solution by Eric Colton
"""

import re
from typing import List, Tuple

class KnotMap:
    def __init__(self, length):
        self.roap = [(0, 0)] * length
        self.tail_visited = set([(0, 0)])

    def exec_instrs(self, instrs: List[Tuple[str, int]]):
        for i in instrs:
            dir, count = i
            for _ in range(count):
                self.move_head(dir)

    def recursive_move(self, node: int):
        py, px = self.roap[node - 1]
        ny, nx = self.roap[node]
        node_moved = True
        if py - ny == 2:
            self.roap[node] = ny + 1, px
        elif py - ny == -2:
            self.roap[node] = ny - 1, px
        elif px - nx == 2:
            self.roap[node] = py, nx + 1
        elif px - nx == -2:
            self.roap[node] = py, nx - 1
        else:
            return

        if node == len(self.roap) - 1:
            self.tail_visited.add(self.roap[node])
        else:
            self.recursive_move(node + 1)

    def move_head(self, dir: str):
        y, x = self.roap[0]
        if dir == 'U':
            self.roap[0] = y + 1, x
        elif dir == 'D':
            self.roap[0] = y - 1, x
        elif dir == 'R':
            self.roap[0] = y, x + 1
        elif dir == 'L':
            self.roap[0] = y, x - 1
        else:
            raise Exception("Unexpected direction")
        self.recursive_move(1)



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
        knot_map_2 = KnotMap(2)
        knot_map_2.exec_instrs(instrs)
        part_1 = find_tail_visited_count(knot_map_2)
        assert part_1 == 6090
        print(f"The solution to Part 1 is {part_1}")

        knot_map_10 = KnotMap(10)
        knot_map_10.exec_instrs(instrs)
        part_2 = find_tail_visited_count(knot_map_10)
        print(f"The solution to Part 2 is {part_2}")
        assert part_2 == 2320
