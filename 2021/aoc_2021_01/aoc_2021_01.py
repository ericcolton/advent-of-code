#!/usr/bin/env python3

"""
Advent of Code 2021 Day 1: Sonar Sweep

https://adventofcode.com/2021/day/1

Solution by Eric Colton
"""

from typing import List

def parse_input_data(raw_lines: List[str]) -> List[int]:
    return [int(line.rstrip()) for line in raw_lines]

def count_increasing_depths(data: List[int]) -> int:
    if len(data) == 0:
        return 0
    prev = data[0]
    count = 0
    for i in range(1, len(data)):
        if data[i] > prev:
            count += 1
        prev = data[i]
    return count

def count_increasing_depths_3_window(data: List[int]) -> int:
    if len(data) < 4:
        return 0
    prev_window = sum(data[:3])
    count = 0
    for i in range(3, len(data)):
        this_window = sum(data[i-2:i+1])
        if this_window > prev_window:
            count += 1
        prev_window = this_window
    return count

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = count_increasing_depths(data)
        assert part_1 == 1557
        print(f"The solution to Part 1 is {part_1}")

        part_2 = count_increasing_depths_3_window(data)
        #assert part_2 == 1557
        print(f"The solution to Part 1 is {part_2}")
