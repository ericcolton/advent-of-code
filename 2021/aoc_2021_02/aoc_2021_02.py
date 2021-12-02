#!/usr/bin/env python3

"""
Advent of Code 2021 Day 2: Dive!

https://adventofcode.com/2021/day/2

Solution by Eric Colton
"""

import re
from typing import List
from collections import namedtuple

Command = namedtuple('Command', ['direction', 'magnitude'])
command_regex = re.compile(r'(\w+)\s(\d+)')

def parse_line(line: str) -> Command:
    match = re.fullmatch(command_regex, line.rstrip())
    if match:
        magnitude = int(match.group(2))
        direction = match.group(1)
        if direction == 'forward':
            return Command('F', magnitude)
        elif direction == 'up':
            return Command('U', magnitude)
        elif direction == 'down':
            return Command('D', magnitude)
        else:
            raise Exception(f"Unknown direction in command: {direction}")

def parse_input_data(raw_lines: List[str]) -> List[int]:
    return [parse_line(line) for line in raw_lines]

def calculate_location(commands: List[Command]) -> tuple:
    distance, depth = 0, 0
    for command in commands:
        if command.direction == 'F':
            distance += command.magnitude
        elif command.direction == 'U':
            depth -= command.magnitude
        elif command.direction == 'D':
            depth += command.magnitude
        else:
            raise Exception(f"Unexpected direction: {command.direction}")
    return (distance, depth)

def calculate_location_with_aim(commands: List[Command]) -> tuple:
    distance, depth, aim = 0, 0, 0
    for command in commands:
        if command.direction == 'F':
            distance += command.magnitude
            depth += aim * command.magnitude
        elif command.direction == 'U':
            aim -= command.magnitude            
        elif command.direction == 'D':
            aim += command.magnitude
        else:
            raise Exception(f"Unexpected direction: {command.direction}")
    return (distance, depth)

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        commands = parse_input_data(raw_input)
        (distance_1, depth_1) = calculate_location(commands)
        part_1 = distance_1 * depth_1
        assert part_1 == 1714680
        print(f"The solution to Part 1 is {part_1}")

        (distance_2, depth_2) = calculate_location_with_aim(commands)
        part_2 = distance_2 * depth_2
        assert part_2 == 1963088820
        print(f"The solution to Part 2 is {part_2}")
