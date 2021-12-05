#!/usr/bin/env python3

"""
Advent of Code 2021 Day 5: Hydrothermal Venture

https://adventofcode.com/2021/day/5

Solution by Eric Colton
"""

import re
from typing import List, Dict, Set, Tuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['point_a', 'point_b'])

def parse_input_data(raw_input: List[str]) -> List[Line]:
    results = []
    for line in raw_input:
        match = re.fullmatch(r'(\d+),(\d+)\s+\-\>\s+(\d+),(\d+)', line.rstrip())
        if match:
            point_a = Point(int(match.group(1)), int(match.group(2)))
            point_b = Point(int(match.group(3)), int(match.group(4)))
            results.append(Line(point_a, point_b))
    return results

def determine_step(line: Line) -> Tuple[int, int]:
    a_x, a_y = line.point_a
    b_x, b_y = line.point_b
    if a_x == b_x:
        return (0, 1) if a_y < b_y else (0, -1)
    elif a_y == b_y:
        return (1, 0) if a_x < b_x else (-1, 0)
    elif (b_y - a_y) / (b_x - a_x) > 0:
        return (1, 1) if a_x < b_x else (-1, -1)
    else:
        return (1, -1) if a_x < b_x else (-1, 1)

def paint_lines(lines: List[Line], skip_diagonals: bool) -> Dict[int, Set[Point]]:
    grid = {}
    count_lookup = {1: set()}
    for line in lines:
        step = determine_step(line)
        if skip_diagonals and abs(step[0] + step[1]) != 1:
            continue
        x, y = line.point_a
        while True:
            if (x, y) not in grid:
                grid[(x, y)] = 1
                count_lookup[1].add((x, y))
            else:
                count = grid[(x, y)]
                grid[(x, y)] = count + 1
                count_lookup[count].remove((x, y))
                if count + 1 not in count_lookup:
                    count_lookup[count + 1] = set()
                count_lookup[count + 1].add((x, y))
            if (x, y) == line.point_b:
                break
            x, y = x + step[0], y + step[1]
    return count_lookup

def sum_point_counts_2_or_greater(count_lookup: Dict[int, Set[Point]]) -> int:
    result = 0
    for count, val in count_lookup.items():
        if count >= 2:
            result += len(val)
    return result

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        lines = parse_input_data(raw_input)
        points_by_count = paint_lines(lines, True)
        part_1 = sum_point_counts_2_or_greater(points_by_count)
        assert part_1 == 7674
        print(f"The solution to Part 1 is {part_1}")

        points_by_count_with_diagnols = paint_lines(lines, False)
        part_2 = sum_point_counts_2_or_greater(points_by_count_with_diagnols)
        assert part_2 == 20898
        print(f"The solution to Part 2 is {part_2}")
