#!/usr/bin/env python3

"""
Advent of Code 2022 Day 8: Treetop Tree House

https://adventofcode.com/2022/day/8

Solution by Eric Colton
"""

import re
from typing import List

def parse_input_data(raw_lines: List[str]) -> List[List[int]]:
    return [[int(i) for i in line.rstrip()] for line in raw_lines]

def iterate_x(data: List[List[int]], visible: List[List[bool]], y: int, end: int, backwards: bool) -> None:
    x_range = range(end - 1, -1, -1) if backwards else range(end)
    water_mark = -1
    for x in x_range:
        height = data[y][x]
        if height > water_mark:
            visible[y][x] = True
            water_mark = height

def iterate_y(data: List[List[int]], visible: List[List[bool]], x: int, end: int, backwards: bool) -> None:
    y_range = range(end - 1, -1, -1) if backwards else range(end)
    water_mark = -1
    for y in y_range:
        height = data[y][x]
        if height > water_mark:
            visible[y][x] = True
            water_mark = height

def find_visible(data: List[List[int]]) -> List[List[bool]]:
    len_row = len(data[0])
    visible = [[False] * len_row for _ in range(len(data))]
    for y in range(len(data)):
        iterate_x(data, visible, y, len_row, False)
        iterate_x(data, visible, y, len_row, True)
    for x in range(len_row):
        iterate_y(data, visible, x, len(data), False)
        iterate_y(data, visible, x, len(data), True)
    return visible

def find_visible_trees_count(visible: List[List[int]]):
    return sum([sum(map(lambda val: 1 if val else 0, row)) for row in visible])

def find_visible_distance(y: int, x: int, data: List[List[int]]) -> int:
    height = data[y][x]
    up = 0
    for yy in range(y + 1, len(data)):
        up += 1
        if data[yy][x] >= height:
            break
    down = 0
    for yy in range(y - 1, -1, -1):
        down += 1
        if data[yy][x] >= height:
            break
    right = 0
    for xx in range(x + 1, len(data[0])):
        right += 1
        if data[y][xx] >= height:
            break
    left = 0
    for xx in range(x - 1, -1, -1):
        left += 1
        if data[y][xx] >= height:
            break

    return up * down * right * left

def find_max_visible_distance(data: List[List[int]]) -> int:
    row_len = len(data[0])
    return max([max([find_visible_distance(y, x, data) for x in range(row_len)]) for y in range(len(data))])

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    print(input_filename)
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        visible = find_visible(data)
        part_1 = find_visible_trees_count(visible)
        assert part_1 == 1812
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_max_visible_distance(data)
        assert part_2 == 315495
        print(f"The solution to Part 2 is {part_2}")
