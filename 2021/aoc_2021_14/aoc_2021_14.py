#!/usr/bin/env python3

"""
Advent of Code 2021 Day 14: Extended Polymerization

https://adventofcode.com/2021/day/14

Solution by Eric Colton
"""

import re
from collections import defaultdict
from typing import List, Dict, Tuple, Set, Optional

def parse_input_data(raw_input: List[str]) -> Tuple[Dict[str, int], Dict[str, str], str]:
    data = defaultdict(int)
    data_line = raw_input[0].rstrip()
    for i in range(len(data_line) - 1):
        data[data_line[i:i+2]] += 1

    pairs = {}
    for line in raw_input[2:]:
        match = re.fullmatch(r'(\w\w) -> (\w)', line.rstrip())
        if match:
            pairs[match.group(1)] = match.group(2)
        else:
            raise Exception(f"Could not parse pair input line: '{line}'")
    return (data, pairs, data_line[-1])

def execute_insertion_round(data: Dict[str, int], pairs: Dict[str, str]) -> Dict[str, int]:
    new_data = defaultdict(int)
    for pair, count in data.items():
        if pair in pairs:
            new_char = pairs[pair]
            new_data[pair[0] + new_char] += count
            new_data[new_char + pair[1]] += count
        else:
            raise Exception(f"Unexpected pair: '{pair}'")
    return new_data

def execute_insertion_rounds(data: Dict[str, int], pairs: Dict[str, str], rounds: int) -> Dict[str, int]:
    for i in range(rounds):
        data = execute_insertion_round(data, pairs)
    return data

def find_min_max_counts(data: Dict[str, int], last_char: str) -> Tuple[int, int]:
    counts = defaultdict(int)
    for pair, count in data.items():
        counts[pair[0]] += count
    counts[last_char] += 1
    return min(counts.values()), max(counts.values())

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data, pairs, last_char = parse_input_data(raw_input)
        data = execute_insertion_rounds(data, pairs, 10)
        min_count, max_count = find_min_max_counts(data, last_char)
        part_1 = max_count - min_count
        assert part_1 == 2657
        print(f"The solution to Part 1 is {part_1}")

        data = execute_insertion_rounds(data, pairs, 30)
        min_count, max_count = find_min_max_counts(data, last_char)
        part_2 = max_count - min_count
        assert part_2 == 2911561572630
        print(f"The solution to Part 2 is {part_2}")

