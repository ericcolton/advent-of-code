#!/usr/bin/env python3

"""
Advent of Code 2021 Day 13: Transparent Origami

https://adventofcode.com/2021/day/13

Solution by Eric Colton
"""

import re
from collections import namedtuple
from typing import List, Dict, Tuple, Set, Optional

Dot = namedtuple('Dot', ['x', 'y'])
Fold = namedtuple('Fold', ['axis', 'dimension'])

def parse_dot(line: str) -> Dot:
    match = re.fullmatch(r'(\d+),(\d+)', line)
    if match:
        return Dot(int(match.group(1)), int(match.group(2)))
    raise Exception(f"Could not parse dot input: '{line}'")

def parse_fold(line: str) -> Fold:
    match = re.fullmatch(r'fold along ([xy])=(\d+)', line)
    if match:
        return Fold(match.group(1), int(match.group(2)))
    raise Exception(f"Could not parse fold input: '{line}'")

def parse_input_data(raw_input: List[str]) -> Tuple[Set[Dot], List[Fold]]:
    delimiter = None
    for i, line in enumerate(raw_input):
        if line == "" or line == "\n":
            delimiter = i
            break
    if delimiter == None:
        raise Exception(f"No dots/folds delimiter found in input")
    return (set([parse_dot(l.rstrip()) for l in raw_input[:delimiter]]),
            [parse_fold(l.rstrip()) for l in raw_input[delimiter + 1:]])

def execute_fold(dots: Set[Dot], fold: Fold) -> None:
    require_folding = []
    if fold.axis == 'x':
        for dot in dots:
            if dot.x > fold.dimension:
                require_folding.append(dot)
            elif dot.x == fold.dimension:
                raise Exception(f"Dot should not fall on fold x-axis dot={dot} fold={fold}")
        for dot in require_folding:
            dots.remove(dot)
            new_x = 2 * fold.dimension - dot.x
            if new_x < 0:
                raise Exception(f"Bad fold calculation dot={dot} fold={fold}")
            dots.add(Dot(new_x, dot.y))
    elif fold.axis == 'y':
        for dot in dots:
            if dot.y > fold.dimension:
                require_folding.append(dot)
            elif dot.y == fold.axis:
                raise Exception(f"Dot should not fall on fold axis dot={dot} fold={fold}")
        for dot in require_folding:
            dots.remove(dot)
            new_y = 2 * fold.dimension - dot.y
            if new_y < 0:
                raise Exception(f"Bad fold calculation dot={dot} fold={fold}")
            dots.add(Dot(dot.x, new_y))
    else:
        raise Exception(f"Unexpected fold axis: '{fold.axis}'")

def execute_folds(dots: Set[Dot], folds: List[Fold]) -> None:
    [execute_fold(dots, fold) for fold in folds]

def print_dots(dots: Set[Dot]) -> str:
    max_x, max_y = -1, -1
    dot_locations = set()
    printout = ""
    for dot in dots:
        max_x = max(max_x, dot.x)
        max_y = max(max_y, dot.y)
        dot_locations.add((dot.x, dot.y))
    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += "#" if (x, y) in dot_locations else "."
        printout += row + "\n"
    return printout

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        dots, folds = parse_input_data(raw_input)
        execute_folds(dots, folds[:1])
        part_1 = len(dots)
        assert part_1 == 847
        print(f"The solution to Part 1 is {part_1}")

        execute_folds(dots, folds[1:])
        part_2 = print_dots(dots)
        assert part_2 == """###...##..####.###...##..####..##..###.
#..#.#..#....#.#..#.#..#.#....#..#.#..#
###..#......#..#..#.#....###..#..#.###.
#..#.#.....#...###..#....#....####.#..#
#..#.#..#.#....#.#..#..#.#....#..#.#..#
###...##..####.#..#..##..####.#..#.###.
"""
        print("The solution to Part 1 is:")
        print(part_2)
