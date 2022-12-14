#!/usr/bin/env python3

"""
Advent of Code 2022 Day 13: Distress Signal

https://adventofcode.com/2022/day/13

Solution by Eric Colton
"""

import re
from typing import List, Tuple
from functools import cmp_to_key

DIVIDER_1 = [[2]]
DIVIDER_2 = [[6]]

def comparator(a: object, b: object) -> int:
    a_list, b_list = isinstance(a, list), isinstance(b, list)
    if a_list and b_list:
        for i in range(min(len(a), len(b))):
            result = comparator(a[i], b[i])
            if result != 0:
                return result
        if len(a) < len(b):
            return -1
        elif len(a) == len(b):
            return 0
        else:
            return 1
    elif a_list and not b_list:
        return comparator(a, [b])
    elif not a_list and b_list:
        return comparator([a], b)
    else:
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

def find_sum_ordered_indicies(data: List[Tuple[List, List]]) -> int:
    total = 0
    for i, pair in enumerate(data):
        if comparator(pair[0], pair[1]) == -1:
            total += i + 1
    return total

def flatten_pairs(data: List[Tuple]) -> List:
    output = []
    for pair in data:
        output.append(pair[0])
        output.append(pair[1])
    return output

def append_dividers(data: List) -> List:
    new_data = data[:]
    new_data.append(DIVIDER_1)
    new_data.append(DIVIDER_2)
    return new_data

def sort_packets_and_multiply_divider_placements(data: List):
    sorted_data = sorted(data, key=cmp_to_key(comparator))
    place_1, place_2 = None, None
    for i, packet in enumerate(sorted_data):
        if packet == DIVIDER_1:
            place_1 = i + 1
        elif packet == DIVIDER_2:
            place_2 = i + 1
        if place_1 != None and place_2 != None:
            return place_1 * place_2
    raise Exception("Cannot find dividers")
    
def parse_list(line: str, index: int) -> object:
    assert line[index] == '['
    content = []
    i = index + 1
    while line[i] != ']':
        if line[i] == '[':
            list_content, i = parse_list(line, i)
            content.append(list_content)
            continue
        if line[i] == ',':
            i += 1
            continue
        match = re.match(r'(\d+)', line[i:])
        if match:
            i += len(match.group(1))
            content.append(int(match.group(1)))
            continue
        raise Exception("Parse error")
    return content, i + 1

def parse_input_data(raw_lines: List[str]) -> List[Tuple[List, List]]:
    i = 0
    data = []
    while i < len(raw_lines):
        data.append((parse_list(raw_lines[i], 0)[0], parse_list(raw_lines[i+1], 0)[0]))
        i += 3
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_ordered_indicies(data)
        assert part_1 == 5366
        print(f"The solution to Part 1 is {part_1}")

        flat_list = flatten_pairs(data)
        flat_list = append_dividers(flat_list)
        part_2 = sort_packets_and_multiply_divider_placements(flat_list)
        assert part_2 == 23391
        print(f"The solution to Part 2 is {part_2}")
