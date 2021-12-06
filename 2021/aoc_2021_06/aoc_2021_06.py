#!/usr/bin/env python3

"""
Advent of Code 2021 Day 6: Lanternfish

https://adventofcode.com/2021/day/6

Solution by Eric Colton
"""

from typing import List, Dict
from collections import namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['point_a', 'point_b'])

def parse_input_data(raw_input: List[str]) -> List[int]:
    return [int(i) for i in raw_input[0].rstrip().split(',')]

def consolidate_by_age(ages: List[int]) -> Dict[int, int]:
    count_by_age = defaultdict(int)
    for age in ages:
        count_by_age[age] += 1
    return count_by_age

def iterate_days(count_by_age: Dict[int, int], days: int) -> None:
    for _ in range(days):
        old_0 = count_by_age[0]
        for i in range(8):
            count_by_age[i] = count_by_age[i + 1]
        count_by_age[6] += old_0                
        count_by_age[8] = old_0            

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        ages = parse_input_data(raw_input)
        count_by_age = consolidate_by_age(ages)
        iterate_days(count_by_age, 80)
        part_1 = sum(count_by_age.values())
        assert part_1 == 362639
        print(f"The solution to Part 1 is {part_1}")

        iterate_days(count_by_age, 256-80)
        part_2 = sum(count_by_age.values())
        assert part_2 == 1639854996917
        print(f"The solution to Part 1 is {part_2}")
