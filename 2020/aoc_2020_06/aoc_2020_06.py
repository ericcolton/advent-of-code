#!/usr/bin/env python3

"""
Advent of Code 2020 Day 6: Custom Customs

https://adventofcode.com/2020/day/6

Solution by Eric Colton
"""

from functools import reduce

def sum_anyone_in_group(data: list):
    return sum([len(reduce(lambda x, y: x.union(y), group)) for group in data])

def sum_everyone_in_group(data: list):
    return sum([len(reduce(lambda x, y: x.intersection(y), group)) for group in data])

def parse_input_file(file):
    data = []
    current_group = []
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            if len(current_group) > 0:
                data.append(current_group)
                current_group = []
                continue
        current_group.append(set([c for c in line]))
    if len(current_group) > 0:
        data.append(current_group)
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    part_1 = sum_anyone_in_group(data)
    assert part_1 == 6662
    print("Solution to Part 1 is {}".format(part_1))

    part_2 = sum_everyone_in_group(data)
    assert part_2 == 3382
    print("Solution to Part 2 is {}".format(part_2))

    