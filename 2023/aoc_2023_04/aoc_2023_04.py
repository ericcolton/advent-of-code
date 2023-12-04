#!/usr/bin/env python3

"""
Advent of Code 2023 Day 4: Scratchcards

https://adventofcode.com/2023/day/4

Solution by Eric Colton
"""

import re
from typing import Set, Dict, List

def parse_input_data(raw_lines: str) -> tuple[List[int], List[int]]:
    cards = []
    for line in raw_lines:
        match = re.match(r'Card\s+(\d+)\:\s+(.*?)\s+\|\s+(.*)\s*$', line.rstrip())
        if match:
            winners = list(map(int, re.split(r'\s+', match.group(2))))
            yours = list(map(int, re.split(r'\s+', match.group(3))))
            cards.append((winners, yours))
        else:
            raise Exception('invalid card syntax')
    return cards
        
if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        #part_1 = count_sum_adjacent_parts(data)
        #assert part_1 == 550934
        #print(f"The solution to Part 1 is {part_1}")

        # part_2 = count_sum_gear_ratios(data)
        # assert part_2 == 81997870
        # print(f"The solution to Part 2 is {part_2}")
