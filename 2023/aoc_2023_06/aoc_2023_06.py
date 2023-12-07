#!/usr/bin/env python3

"""
 Advent of Code 2023 Day 6: Wait For It

https://adventofcode.com/2023/day/6

Solution by Eric Colton
"""

import re
from typing import Set, Dict, List

def product_of_ways_to_win(data: List[tuple[int, int]]) -> int:
    wins_product = 1
    for race in data:
        time, winning_distance = race
        wins = 0
        for speed in range(1, time):
            distance = speed * (time - speed)
            if distance > winning_distance:
                wins += 1
        wins_product *= wins
    return wins_product

def parse_input_data(raw_lines: str) -> tuple[List[tuple[int, int]], List[tuple[int, int]]]:
    time_match = re.match(r'Time\:\s+(.+)', raw_lines[0].rstrip())
    if time_match:
        times = re.split(f'\s+', time_match.group(1))
    else:
        raise Exception('Invalid time input')
    distance_match = re.match(r'Distance\:\s+(.+)', raw_lines[1].rstrip())    
    if distance_match:
        distances = re.split(f'\s+', distance_match.group(1))
    else:
        raise Exception('Invalid distance input')
    seperated, combined = [], []
    for i in range(len(times)):
        seperated.append((int(times[i]), int(distances[i])))
    combined = [(int("".join(times)), int("".join(distances)))]
    return seperated, combined

if __name__ == '__main__':
   input_filename = __file__.strip('.py') + '_input.txt'
   with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = product_of_ways_to_win(data[0])
        assert part_1 == 316800
        print(f"The solution to Part 1 is {part_1}")

        part_2 = product_of_ways_to_win(data[1])
        assert part_2 == 45647654
        print(f"The solution to Part 2 is {part_2}")