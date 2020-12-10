#!/usr/bin/env python3

"""
Advent of Code 2020 Day 10: Adapter Array

https://adventofcode.com/2020/day/10

Solution by Eric Colton
"""

def _count_routes_to_end(data: list, index: int, dp: dict):
    max_index = len(data) - 1
    if index == max_index:
        return 1
    if index not in dp:
        routes = 0
        if index + 1 <= max_index and data[index + 1] <= data[index] + 3:
            routes += _count_routes_to_end(data, index + 1, dp)
        if index + 2 <= max_index and data[index + 2] <= data[index] + 3:
            routes += _count_routes_to_end(data, index + 2, dp)
        if index + 3 <= max_index and data[index + 3] <= data[index] + 3:
            routes += _count_routes_to_end(data, index + 3, dp)
        dp[index] = routes
    return dp[index]

def count_routes_to_end(data: list):
    return _count_routes_to_end(data, 0, {})

def find_delta_counts(data: list) -> dict:
    deltas = {}
    last_value = 0
    for value in data:
        delta = value - last_value
        if delta > 3:
            raise Exception("Difference exceeds maximum of 3 ({})".format(delta))
        if delta in deltas:
            deltas[delta] += 1
        else:
            deltas[delta] = 1
        last_value = value
    return deltas

def parse_input_file(raw_input):
    return sorted([int(line.rstrip()) for line in raw_input])

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
        data.append(data[-1] + 3)
    deltas = find_delta_counts(data)
    part_1 = deltas[1] * deltas[3]
    assert part_1 == 2475
    print("Solution to Part 1 is {}".format(part_1))

    data_2 = data.copy()
    data_2.insert(0, 0)
    part_2 = count_routes_to_end(data_2)
    assert part_2 == 442136281481216
    print("Solution to Part 2 is {}".format(part_2))



