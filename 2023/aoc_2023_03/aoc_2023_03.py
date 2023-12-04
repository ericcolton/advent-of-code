#!/usr/bin/env python3

"""
Advent of Code 2023 Day 3: Gear Ratios

https://adventofcode.com/2023/day/3

Solution by Eric Colton
"""

from typing import Set, Dict, List

def find_neighbors(loc: tuple[int, int]) -> List[tuple[int, int]]:
    neighbors = []
    y, x = loc    
    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        dy, dx = delta
        neighbors.append((y + dy, x + dx))
    return neighbors

def count_sum_adjacent_parts(data: tuple[Dict[tuple[int, int], int], Set[tuple[int, int]]]):
    num_lookup, symbol_lookup = data
    adjacent = set()
    for loc, val in num_lookup.items():
        if val in adjacent:
            continue
        for n_loc in find_neighbors(loc):
            if n_loc in symbol_lookup:
                adjacent.add(val)
                break
    return sum(map(lambda x: x[1], adjacent))

def count_sum_gear_ratios(data: tuple[Dict[tuple[int, int], int], Set[tuple[int, int]]]):
    num_lookup, symbol_lookup = data
    gear_pairs, used = {}, set()
    for loc, val in num_lookup.items():
        if val in used:
            continue
        for n_loc in find_neighbors(loc):
            if n_loc in symbol_lookup and symbol_lookup[n_loc] == '*':
                if n_loc not in gear_pairs:
                    gear_pairs[n_loc] = []
                gear_pairs[n_loc].append(val)
                used.add(val)
                break
    total = 0
    for pair in gear_pairs.values():
        if len(pair) == 1:
            pass
        if len(pair) == 2:
            total += pair[0][1] * pair[1][1]
        elif len(pair) > 2:
            raise Exception('Gear contains more than 2 adjacent parts')
    return total

def parse_input_data(raw_lines: str) -> tuple[Dict[tuple[int, int], int], Set[tuple[int, int]]]:
    num_lookup, symbol_lookup = {}, {}
    for y in range(len(raw_lines)):
        line, x = raw_lines[y].rstrip(), 0
        while x < len(line):
            if line[x].isdigit():
                x_begin = x
                x += 1
                while x < len(line) and line[x].isdigit():
                    x += 1
                num = int(line[x_begin:x])
                for xx in range(x_begin, x):
                    num_lookup[y, xx] = (f"{y}, {x_begin}", num)
                continue
            elif line[x] != '.':
                symbol_lookup[(y, x)] = line[x]
            x += 1
    return num_lookup, symbol_lookup

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = count_sum_adjacent_parts(data)
        assert part_1 == 550934
        print(f"The solution to Part 1 is {part_1}")

        part_2 = count_sum_gear_ratios(data)
        assert part_2 == 81997870
        print(f"The solution to Part 2 is {part_2}")
