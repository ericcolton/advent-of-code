#!/usr/bin/env python3

"""
Advent of Code 2020 Day 5: Binary Boarding

https://adventofcode.com/2020/day/5

Solution by Eric Colton
"""

import re
from collections import namedtuple

Seat = namedtuple('Seat', ['row_identifier', 'column_identifier'])

def decode_identifier(identifier: str, high_char: str):
    total = 0
    for index in range(len(identifier)):
        if identifier[index] == high_char:
            power = len(identifier) - index - 1
            total += 2 ** power
    return total

def calculate_seat_id(seat: Seat) -> int:
    row = decode_identifier(seat.row_identifier, 'B')
    column = decode_identifier(seat.column_identifier, 'R')
    return row * 8 + column

def find_max_seat_id(data: list) -> int:
    return max(map(calculate_seat_id, data))

def find_empty_seat_id(data: list) -> int:
    filled_seats = set(map(calculate_seat_id, data))
    for i in range(min(filled_seats) + 1, max(filled_seats)):
        if i not in filled_seats:
            return i
    return -1

def parse_input_file(file) -> list:
    data = []
    for line in file:
        line = line.rstrip()
        match = re.match(r'([FB]{7})([LR]{3})', line)
        if match:
            data.append(Seat(match.group(1), match.group(2)))
        else:
            raise Exception("could not parse row: '{}'".format(line))
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    part_1 = find_max_seat_id(data)
    assert part_1 == 994
    print("Solution to Part 1 is {}".format(part_1))

    part_2 = find_empty_seat_id(data)
    assert part_2 == 741
    print("Solution to Part 2 is {}".format(part_2))

