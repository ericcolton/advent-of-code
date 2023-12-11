#!/usr/bin/env python3

"""
 Advent of Code 2023 Day 8: Haunted Wasteland

https://adventofcode.com/2023/day/8

Solution by Eric Colton
"""

import re
import math
from typing import Dict

def count_simple_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        dir = 0 if instrs[count % len(instrs)] == 'L' else 1
        node = lookup[node][dir]
        count += 1
    return count

def count_simultaneous_steps_HACK(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    count = 0
    nodes = []
    for key in lookup.keys():
        if key[2] == 'A':
            nodes.append(key)
    memo = set()
    empty = False
    ends = []
    while not empty:
        empty = True
        for n in range(len(nodes)):
            node = nodes[n]
            if node == None:
                continue
            empty = False
            i = count % len(instrs)
            key = n, node, i
            if node[2] == 'Z':
                print(f"{n} {node} ({i}) found at {count}")        
            if key not in memo:
                dir = 0 if instrs[i] == 'L' else 1
                node = lookup[node][dir]
                nodes[n] = node
                memo.add(key)
            else:
                print(f"*** {n} exit {node} ({i}) found at {count}")
                ends.append(count)
                nodes[n] = None
        count += 1
    print(ends)
    print(math.lcm(*ends))
    return count

def count_simultaneous_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    count = 0
    nodes = []
    for key in lookup.keys():
        if key[2] == 'A':
            nodes.append(key)
    while not reached_end_state(nodes):
        dir = 0 if instrs[count % len(instrs)] == 'L' else 1
        for i in range(len(nodes)):
            nodes[i] = lookup[nodes[i]][dir]
        count += 1
    return count

def parse_input_data(raw_lines: str) -> tuple[str, Dict[str, tuple[str, str]]]:
    instrs = raw_lines[0].rstrip()
    lookup = {}
    for i in range(2, len(raw_lines)):
        match = re.match(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', raw_lines[i].rstrip())
        if match:
            lookup[match.group(1)] = (match.group(2), match.group(3))
        else:
            raise Exception("Unable to parse mapping")
    return (instrs, lookup)

if __name__ == '__main__':
   input_filename = __file__.strip('.py') + '_input.txt'
   with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = count_simple_steps(data)
        assert part_1 == 16579
        print(f"The solution to Part 1 is {part_1}")

        part_2 = count_simultaneous_steps_HACK(data)
        #assert part_2 == 16579
        print(f"The solution to Part 2 is {part_2}")