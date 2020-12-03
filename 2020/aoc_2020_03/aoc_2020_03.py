#!/usr/bin/env python3

"""
Advent of Code 2020 Day 3: Toboggan Trajectory

https://adventofcode.com/2020/day/3
Solution by Eric Colton
"""

from functools import reduce

def trees_encountered(data: list, trajectory: tuple):
    if len(data) == 0:
        return 0
    y_position, x_position = 0, 0        
    x_mod = len(data[0])
    tree_count = 0
    while y_position < len(data):
        if data[y_position][x_position % x_mod]:
            tree_count += 1
        x_position += trajectory[0]
        y_position += trajectory[1]
    return tree_count

def parse_input_file(file):
    data = []
    for line in file:
        data.append([c == '#' for c in line.rstrip()])
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + "_input.txt"
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    part_1 = trees_encountered(data, (3, 1))
    print("Solution to part 1 is {}".format(part_1))

    routes = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
    part_2 = reduce(lambda x, y: x * trees_encountered(data, y), routes, 1)
    print("Solution to part 2 is {}".format(part_2))
