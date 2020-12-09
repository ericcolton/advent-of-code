#!/usr/bin/env python3

"""
Advent of Code 2020 Day 9: Encoding Error

https://adventofcode.com/2020/day/9

Solution by Eric Colton
"""

def find_sum_max_and_min_in_range(lower_bound: int, upper_bound: int, data: list):
    return min(data[lower_bound:upper_bound + 1]) + max(data[lower_bound:upper_bound + 1])

def find_range_that_sums_to_index(index: int, data: list):
    for i in range(index - 1):
        for j in range(i + 2, index + 1):
            if sum(data[i:j]) == data[index]:
                return (i, j-1)
            elif sum(data[i:j]) > data[index]:
                break
    return (-1, -1)

def find_first_invalid_index(data: list, preamble_length: int) -> int:
    for i in range(preamble_length, len(data)):
        if not validate_index(i, data, preamble_length):
            return i
    return -1

def validate_index(index: int, data: list, preamble_length: int) -> bool:
    if index >= len(data) or preamble_length >= len(data):
        return False
    if index < preamble_length:
        return True
    for i in range(index - preamble_length, index - 1):
        for j in range(i + 1, index):
            if data[i] + data[j] == data[index]:
                return True
    return False

def parse_input_data(input_data: list):
    return [int(line.rstrip()) for line in input_data]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        input_data = file.readlines()
        data = parse_input_data(input_data)
    invalid_index = find_first_invalid_index(data, 25)
    assert invalid_index >= 0
    part_1 = data[invalid_index]
    assert part_1 == 3199139634
    print("Solution to Part 1 is {}".format(part_1))

    lower, upper = find_range_that_sums_to_index(invalid_index, data)
    part_2 = find_sum_max_and_min_in_range(lower, upper, data)
    assert part_2 == 438559930
    print("Solution to Part 2 is {}".format(part_2))