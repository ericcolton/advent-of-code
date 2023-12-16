#!/usr/bin/env python3

"""
Advent of Code 2023 Day 8: Haunted Wasteland

https://adventofcode.com/2023/day/8

Solution by Eric Colton
"""

import re
from typing import Dict
from math import gcd
from functools import reduce

def lcm(args):
   return reduce(lambda a, b: a * b // gcd(a, b), args)

def find_loop_length(node: str, data: tuple[str, Dict[str, tuple[str, str]]]):
   instrs, lookup = data
   start_node = node
   slow, fast = start_node, start_node
   slow_count, fast_count = 0, 0
   # find where slow and fast intersect
   while slow_count == 0 or slow != fast or (slow_count % len(instrs) != fast_count % len(instrs)):
        # advance slow
        dir = 0 if instrs[slow_count % len(instrs)] == 'L' else 1
        slow = lookup[slow][dir]
        slow_count += 1

        #advance fast
        for _ in range(2):
            dir = 0 if instrs[fast_count % len(instrs)] == 'L' else 1
            fast = lookup[fast][dir]
            fast_count += 1
   return slow_count

def count_simultaneous_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    return lcm(list(map(lambda n: find_loop_length(n, data), filter(lambda a: a[2] == 'A', lookup.keys()))))

def count_simple_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
   instrs, lookup = data
   count = 0
   node = 'AAA'
   while node != 'ZZZ':
       dir = 0 if instrs[count % len(instrs)] == 'L' else 1
       node = lookup[node][dir]
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
  input_filename = __file__.rstrip('.py') + '_input.txt'
  with open(input_filename, 'r') as file:
       raw_input = file.readlines()
       data = parse_input_data(raw_input)
       part_1 = count_simple_steps(data)
       assert part_1 == 16579
       print(f"The solution to Part 1 is {part_1}")

       part_2 = count_simultaneous_steps(data)
       assert part_2 == 12927600769609
       print(f"The solution to Part 2 is {part_2}")
