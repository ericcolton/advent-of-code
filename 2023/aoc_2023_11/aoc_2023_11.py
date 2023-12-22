#!/usr/bin/env python3

"""
Advent of Code 2023 Day 11: Cosmic Expansion

https://adventofcode.com/2023/day/11

Solution by Eric Colton
"""

import re
from typing import Set, List

def count_total_lengths(expanded_stars: List[tuple[int, int]]):
    total_lengths = 0
    for i in range(len(expanded_stars)):
        i_star = expanded_stars[i]
        for j in range(i + 1, len(expanded_stars)):
            j_star = expanded_stars[j]
            total_lengths += abs(j_star[0] - i_star[0]) + abs(j_star[1] - i_star[1])
    return total_lengths

def expand_universe(data: tuple[Set[tuple[int, int]], int, int], expand_factor: int) -> List[tuple[int, int]]:
    stars, max_y, max_x = data
    translated_y_vals = [None] * (max_y + 1)
    translated_y = 0
    for y in range(max_y + 1):
        star_exists_on_y = False
        translated_y_vals[y] = translated_y
        for x in range(max_x + 1):
            if (y, x) in stars:
                star_exists_on_y = True
                break
        translated_y += 1 if star_exists_on_y else expand_factor
    
    translated_stars = []
    translated_x = 0
    for x in range(max_x + 1):
        star_exists_on_x = False
        for y in range(max_y + 1):
            if (y, x) in stars:
                star_exists_on_x = True
                translated_stars.append((translated_y_vals[y], translated_x))
        translated_x += 1 if star_exists_on_x else expand_factor
    return translated_stars

def parse_input_data(raw_input: str) -> tuple[Set[tuple[int, int]], int, int]:
    stars = set()
    max_y, max_x = 0, 0
    for y in range(len(raw_input)):
        for x in range(len(raw_input[y].rstrip())):
            if raw_input[y][x] == '#':
                stars.add((y, x))
                max_y, max_x = max(max_y, y), max(max_x, x)
    return (stars, max_y, max_x)

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        expanded_stars = expand_universe(data, 2)
        part_1 = count_total_lengths(expanded_stars)
        assert part_1 == 9418609
        print(f"The solution to Part 1 is {part_1}")
        
        expanded_stars = expand_universe(data, 1000000)
        part_2 = count_total_lengths(expanded_stars)
        assert part_2 == 593821230983
        print(f"The solution to Part 2 is {part_2}")
