#!/usr/bin/env python3

"""
Advent of Code 2022 Day 12: Hill Climbing Algorithm

https://adventofcode.com/2022/day/12

Solution by Eric Colton
"""

import re
from typing import List, Dict
from collections import deque

start_loc = None
dest_loc = None

def find_efficient_path(data: List[List[int]], start_end_nodes: Dict) -> int:
    start_node = start_end_nodes['start']
    queue = deque([None, start_node])
    count = 0
    seen = set([start_node])
    while len(queue) > 1:
        current = queue.pop()
        if current == None:
            count += 1
            queue.appendleft(None)
            continue
        if 
        neighbors()

        
        



def record_node(y: int, x: int, char: str) -> int:
    if char == 'S':
        start_end_nodes['start'] = (y, x)
        return 0
    elif char == 'E':
        start_end_nodes['end'] = (y, x)
        return 0
    else:
        return ord(char) - ord('a')

def parse_input_data(raw_lines: List[str], start_end_nodes: Dict) -> List[List[int]]:
    return [[record_node(y, x, c, start_end_nodes) for x, c in enumerate(line.rstrip())] for y, line in enumerate(raw_lines)]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        start_end_nodes = {}
        data = parse_input_data(raw_input, start_end_nodes)
        print(start_loc)
        find_efficient_path(data, start_end_nodes)

        print(Node.start_node)
        # exec_rounds(data, router, True, 20)
        # part_1 = find_product_two_most_active(data)
        # assert part_1 == 50172
        # print(f"The solution to Part 1 is {part_1}")

