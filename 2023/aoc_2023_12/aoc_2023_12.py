#!/usr/bin/env python3

"""
Advent of Code 2023 Day 12: Hot Springs

https://adventofcode.com/2023/day/12

Solution by Eric Colton
"""

import re
from typing import Dict, List

def undamaged_logic(entry: tuple[str, List[int]], index_s: int, index_g: int, current_g_len: int, memo: Dict[tuple[int, int, int], int]):
    groupings = entry[1]
    if current_g_len > 0:
        if current_g_len == groupings[index_g]:
            # end a damaged grouping of correct length
            return recurse(entry, index_s + 1, index_g + 1, 0, memo)
        else:
            return 0
    else:
        # extend an undamaged grouping
        return recurse(entry, index_s + 1, index_g, 0, memo)

def damaged_logic(entry: tuple[str, List[int]], index_s: int, index_g: int, current_g_len: int, memo: Dict[tuple[int, int, int], int]):
    groupings = entry[1]
    if index_g < len(groupings) and current_g_len < groupings[index_g]:
        # start or extend a damaged grouping
         return recurse(entry, index_s + 1, index_g, current_g_len + 1, memo)
    else:
        return 0

def recurse(entry: tuple[str, List[int]], index_s: int, index_g: int, current_g_len: int, memo: Dict[tuple[int, int, int], int]):
    springs, groupings = entry
    if index_s == len(springs):
        if index_g == len(groupings) - 1 and current_g_len == groupings[-1]:
            return 1
        elif index_g == len(groupings):
            return 1
        else:
            return 0
    elif index_g < len(groupings) and current_g_len > groupings[index_g]:
        return 0

    key = index_s, index_g, current_g_len
    if key not in memo:
        undamaged, damaged = 0, 0
        c = springs[index_s]
        if c == '.' or c == '?':
            undamaged = undamaged_logic(entry, index_s, index_g, current_g_len, memo)
        if c == '#' or c == '?':
            damaged = damaged_logic(entry, index_s, index_g, current_g_len, memo)
        memo[key] = undamaged + damaged
    return memo[key]

def count_arrangements(entry: tuple[str, List[int]]) -> int:
    return recurse(entry, 0, 0, 0, {})

def sum_all_arrangements(data: List[tuple[str, List[int]]]) -> int:
    return sum(list(map(count_arrangements, data)))

def expand_record(record: tuple[str, List[int]]) -> tuple[str, List[int]]:
    springs, groupings = record
    return ("?".join([springs] * 5), groupings * 5)

def expand_data(data: List[tuple[str, List[int]]]) -> List[tuple[str, List[int]]]:
    return list(map(expand_record, data))

def parse_input_data(raw_input: str) -> List[tuple[str, List[int]]]:
    data = []
    for line in raw_input:
        match = re.match(r'([\?\.\#]+)\s(.+)', line.rstrip())
        if match:
            data.append((match.group(1), list(map(int, match.group(2).split(",")))))
        else:
            raise Exception(f"unexpected line: {line.rstrip()}")
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = sum_all_arrangements(data)
        assert part_1 == 7118
        print(f"The solution to Part 1 is {part_1}")

        expanded_data = expand_data(data)
        part_2 = sum_all_arrangements(expanded_data)
        assert part_2 == 7030194981795
        print(f"The solution to Part 2 is {part_2}")
