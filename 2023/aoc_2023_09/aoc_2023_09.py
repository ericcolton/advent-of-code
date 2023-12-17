#!/usr/bin/env python3

"""
Advent of Code 2023 Day 9: Mirage Maintenance

https://adventofcode.com/2023/day/9

Solution by Eric Colton
"""

import re
from typing import List, Deque
from collections import deque

def is_all_zeros(row: Deque[int]) -> bool:
   return len(list(filter(lambda x: x != 0, row))) == 0

def extend_last_step(pyramid: List[Deque[int]]) -> int:
   pyramid[-1].append(0)
   for r in range(len(pyramid) - 2, -1, -1):
       row = pyramid[r]
       row.append(pyramid[r + 1][-1] + row[-1])
   return pyramid[0][-1]

def prepend_first_step(pyramid: List[Deque[int]]) -> int:
   pyramid[-1].appendleft(0)
   for r in range(len(pyramid) - 2, -1, -1):
       row = pyramid[r]
       row.appendleft(row[0] - pyramid[r + 1][0])
   return pyramid[0][0]

def sum_new_last_steps(pyramids: List[List[Deque[int]]]) -> int:
   return sum(list(map(extend_last_step, pyramids)))

def sum_new_first_steps(pyramids: List[List[Deque[int]]]) -> int:
   return sum(list(map(prepend_first_step, pyramids)))

def build_pyramid(data_row: List[int]) -> List[Deque[int]]:
   row = deque(data_row)
   pyramid = [row]
   while not is_all_zeros(row):
       next_row = deque()
       prev = None
       for val in row:
           if prev != None:
               next_row.append(val - prev)
           prev = val
       pyramid.append(next_row)
       row = next_row
   return pyramid

def build_pyramids(data: List[List[int]]) -> List[List[Deque[int]]]:
   return list(map(build_pyramid, data))

def parse_input_data(raw_lines: str) -> List[List[int]]:
   return [list(map(int, line.rstrip().split(' '))) for line in raw_lines]

if __name__ == '__main__':
  input_filename = __file__.rstrip('.py') + '_input.txt'
  with open(input_filename, 'r') as file:
       raw_input = file.readlines()
       data = parse_input_data(raw_input)
       pyramids = build_pyramids(data)
       
       part_1 = sum_new_last_steps(pyramids)
       assert part_1 == 2075724761
       print(f"The solution to Part 1 is {part_1}")

       part_2 = sum_new_first_steps(pyramids)
       assert part_1 == 2075724761
       print(f"The solution to Part 2 is {part_2}")