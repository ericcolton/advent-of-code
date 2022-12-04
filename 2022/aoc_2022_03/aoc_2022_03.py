#!/usr/bin/env python3

"""
Advent of Code 2022 Day 3: Rucksack Reorganization

https://adventofcode.com/2022/day/

Solution by Eric Colton
"""

from typing import List, Tuple, Set

def parse_input_data(raw_lines: List[str]) -> List[str]:
    return [line.rstrip() for line in raw_lines]

def find_priority(char: str) -> int:
    pri = ord(char.lower()) - ord('a') + 1
    if char.isupper():
        pri += 26
    return pri

def identify_outlier(line) -> int:
    half = len(line) // 2
    left, right = set(line[:half]), set(line[half:])
    outlier = list(left & right)[0]
    return find_priority(outlier)

def find_sum_outliers(data) -> int:
    return sum([identify_outlier(line) for line in data])

def find_3_intersection(a, b, c) -> int:
    badge = list(set(a) & set(b) & set(c))[0]
    return find_priority(badge)

def find_sum_3_intersections(data) -> int:
    total = 0
    for i in range(0, len(data), 3):
        total += find_3_intersection(data[i], data[i+1], data[i+2])
    return total

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_outliers(data)
        assert part_1 == 8072
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_3_intersections(data)
        assert part_2 == 2567
        print(f"The solution to Part 2 is {part_2}")
