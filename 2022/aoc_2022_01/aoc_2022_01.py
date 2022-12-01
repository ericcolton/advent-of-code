#!/usr/bin/env python3

"""
Advent of Code 2022 Day 1: Calorie Counting

https://adventofcode.com/2022/day/1

Solution by Eric Colton
"""

from typing import List
import heapq

def parse_input_data(raw_lines: List[str]) -> List[List[int]]:
    elfs, current = [], []
    for line in raw_lines:
        val = line.rstrip()
        if val == '':
            elfs.append(current)
            current = []
        else:
            current.append(int(val))
    if len(current) > 0:
        elfs.append(current)
    return elfs

def find_sum_highest_calories(elfs: List[List[int]], k: int) -> int:
    heap = []
    for e in elfs:
        if len(heap) < k:
            heapq.heappush(heap, sum(e))
        else:
            heapq.heappushpop(heap, sum(e))
    return sum(heap)

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_highest_calories(data, 1)
        assert part_1 == 70116
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_highest_calories(data, 3)
        assert part_2 == 206582
        print(f"The solution to Part 1 is {part_2}")        
