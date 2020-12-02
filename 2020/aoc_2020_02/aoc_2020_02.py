#!/usr/bin/env python3

"""
Advent of Code 2020 Day 2: Password Philosophy

https://adventofcode.com/2020/day/2

Solution by Eric Colton
"""

import re
from collections import namedtuple

Entry = namedtuple('Entry', ['min', 'max', 'policy_char', 'text'])

def does_password_follow_policy_part_1(entry: Entry):
    count = 0
    for c in entry.text:
        if c == entry.policy_char:
            count += 1
            if count > entry.max:
                return False
    return count >= entry.min

def does_password_follow_policy_part_2(entry: Entry):
    if entry.min > len(entry.text) or entry.max > len(entry.text):
        return False
    min_char_match = entry.text[entry.min - 1] == entry.policy_char
    max_char_match = entry.text[entry.max - 1] == entry.policy_char
    return min_char_match ^ max_char_match

def count_passwords_following_policy(data, func):
    return len(list(filter(func, data)))

def parse_input_file(file):
    data = []
    expr = r'(\d+)\-(\d+)\s*(\w)\s*\:\s*(\w+)'
    for line in file:
        match = re.search(expr, line.rstrip())
        if match:
            data.append(Entry(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)))
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    part_1_matching_count = count_passwords_following_policy(data, does_password_follow_policy_part_1)
    print("Solution to Part 1 is {}".format(part_1_matching_count))

    part_2_matching_count = count_passwords_following_policy(data, does_password_follow_policy_part_2)
    print("Solution to Part 2 is {}".format(part_2_matching_count))