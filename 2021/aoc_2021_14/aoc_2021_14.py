#!/usr/bin/env python3

"""
Advent of Code 2021 Day 14: Extended Polymerization

https://adventofcode.com/2021/day/14

Solution by Eric Colton
"""

import re
from collections import Counter
from typing import List, Dict, Tuple, Set, Optional

def parse_input_data(raw_input: List[str]) -> Tuple[str, Dict[str, str]]:
    pairs = {}
    for line in raw_input[2:]:
        match = re.fullmatch(r'(\w\w) -> (\w)', line.rstrip())
        if match:
            pairs[match.group(1)] = match.group(2)
        else:
            raise Exception(f"Could not parse pair input line: '{line}'")
    return (raw_input[0].rstrip(), pairs)

def execute_insertion_round(input: str, pairs: Dict[str, str]) -> None:
    output = []
    for i in range(len(input) - 1):
        pair = input[i:i+2]
        if pair in pairs:
            output.append(input[i] + pairs[pair])
        else:
            raise Exception(f"Unexpected pair: '{pair}'")
    return ''.join(output) + input[-1]

def execute_insertion_rounds(data: str, pairs: Dict[str, str], rounds: int) -> None:
    for i in range(rounds):
        data = execute_insertion_round(data, pairs)
    return data

def find_min_max_counts(data: str) -> Dict[str, int]:
    min_seen, max_seen = None, None
    min_index, max_index = None, None
    for key, count in Counter(data).items():
        if min_seen == None or count < min_seen:
            min_seen = count
            min_index = key
        if max_seen == None or count > max_seen:
            max_seen = count
            max_index = key
    return min_seen, max_seen

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        input, pairs = parse_input_data(raw_input)
        data = execute_insertion_rounds(input, pairs, 10)
        min_count, max_count = find_min_max_counts(data)
        part_1 = max_count - min_count
        assert part_1 == 2657
        print(f"The solution to Part 1 is {part_1}")



