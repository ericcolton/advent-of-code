#!/usr/bin/env python3

"""
Advent of Code 2022 Day 16: Proboscidea Volcanium

https://adventofcode.com/2022/day/15

Solution by Eric Colton
"""

import re
import heapq
from typing import List, Dict, Tuple
from collections import namedtuple

Node = namedtuple("Node", ['name', 'rate', 'edges'])

def parse_line(line: str) -> Tuple[str, Node]:
    match = re.match(r'Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)', line)
    if not match:
        raise Exception("Unexpected line")
    edges = match.group(3).split(", ")
    return Node(match.group(1), int(match.group(2)), edges)

def parse_input_data(raw_lines: List[str]) -> List[Dict[str, Node]]:
    node_lookup = {}
    for line in raw_lines:
        node = parse_line(line.rstrip())
        node_lookup[node.name] = node
    return node_lookup

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        print(data)

        # part_2 = find_tuning_frequency(data, 4000000)
        # assert part_2 == 13213086906101
        # print(f"The solution to Part 2 is {part_2}")
