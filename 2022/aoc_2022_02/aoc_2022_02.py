#!/usr/bin/env python3

"""
Advent of Code 2022 Day 2: Rock Paper Scissors

https://adventofcode.com/2022/day/2

Solution by Eric Colton
"""

from typing import List, Tuple

def parse_input_data(raw_lines: List[str]) -> List[Tuple[int, int]]:
    a, x = ord('A'), ord('X')
    return [(ord(line[0]) - a,  ord(line[2]) - x) for line in raw_lines]

def score_as_play(pair: Tuple[int, int]) -> int:
    a, b = pair
    if a == b:
        outcome = 3
    elif b == (a + 1) % 3:
        outcome = 6
    else:
        outcome = 0
    return outcome + b + 1

def score_as_outcome(pair: Tuple[int, int]) -> int:
    a, raw_outcome = pair
    outcome = 3 * raw_outcome
    if outcome == 0:
        b = (a - 1) % 3
    elif outcome == 3:
        b = a
    else:
        b = (a + 1) % 3
    return outcome + b + 1

def find_sum_scores(data: List[Tuple[int, int]], mode: bool) -> int:
    score_func = score_as_outcome if mode else score_as_play
    return sum([score_func(d) for d in data])

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_scores(data, False)
        assert part_1 == 12586
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_scores(data, True)
        assert part_2 == 13193
        print(f"The solution to Part 2 is {part_2}")
