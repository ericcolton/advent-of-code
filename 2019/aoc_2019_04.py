#!/usr/bin/env python3

"""
Advent of Code 2019 Day 4: Secure Container

https://adventofcode.com/2019/day/4
"""

from aoc_helpers import get_input_filepath

def follows_simple_double_rule(digits):
    prev_digit = 0
    for d in digits:
        if d == prev_digit:
            return True
        else:
            prev_digit = d
    return False

def follows_complex_double_rule(digits):
    prev_digit = -1
    current_sequence_length = 0
    for d in digits:
        if d == prev_digit:
            current_sequence_length += 1
        else:
            if current_sequence_length == 2:
                return True
            else:
                current_sequence_length = 1
        prev_digit = d
    return current_sequence_length == 2

def find_next_candidate(digits, index=-1):
    if index == -1:
        index = len(digits) - 1
    if digits[index] == 9:
        if index == 0:
            raise Exception("overflow error")
        find_next_candidate(digits, index - 1)
        digits[index] = digits[index - 1]
    else:
        digits[index] += 1

def find_match_count(input_min, input_max):
    simple_match_count = 0
    complex_match_count = 0
    digits = [int(x) for x in str(input_min)]
    while True:
        candidate = int(''.join(str(x) for x in digits))
        if candidate > input_max:
            break
        if follows_simple_double_rule(digits):
            simple_match_count += 1
        if follows_complex_double_rule(digits):
            complex_match_count += 1
        find_next_candidate(digits)
    return (simple_match_count, complex_match_count)

def parse_input_file(input_filepath):
    with open(input_filepath, 'r') as file:
        line = file.readline().rstrip()
        (range_min, range_max) = line.split('-')
        return (int(range_min), int(range_max))

if __name__ == "__main__":
    file_path = get_input_filepath(__file__)
    (input_min, input_max) = parse_input_file(file_path)
    (results_1, results_2) = find_match_count(input_min, input_max)
    print(f"Solution to Part 1 is: {results_1}")
    print(f"Solution to Part 2 is: {results_2}")

