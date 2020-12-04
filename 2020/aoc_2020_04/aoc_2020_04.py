#!/usr/bin/env python3

"""
Advent of Code 2020 Day 4: Passport Processing

https://adventofcode.com/2020/day/4

Solution by Eric Colton
"""

import re

REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
YEAR_FIELDS = set(['byr', 'iyr', 'eyr'])
EYE_COLORS = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

def validate_entry(entry: dict, validate_values: bool):
    for field in REQUIRED_FIELDS:
        if field not in entry:
            return False
        if not validate_values:
            continue
        value = entry[field]
        if field in YEAR_FIELDS:
            if not re.fullmatch(r'\d{4}', value):
                return False
            i_value = int(value)
            if field == 'byr':
                if i_value < 1920 or i_value > 2002:
                    return False
            elif field == 'iyr':
                if i_value < 2010 or i_value > 2020:
                    return False
            elif field == 'eyr':
                if i_value < 2020 or i_value > 2030:
                    return False
        elif field == 'hgt':
            m = re.fullmatch(r'(\d+)(cm|in)', value)
            if m:
                if m.group(2) == 'cm':
                    cm = int(m.group(1))
                    if cm < 150 or cm > 193:
                        return False
                elif m.group(2) == 'in':
                    inches = int(m.group(1))
                    if inches < 59 or inches > 76:
                        return False
                else:
                    return False
            else:
                return False
        elif field == 'hcl':
            if not re.fullmatch(r'\#([a-f\d]{6})', value):
                return False
        elif field == 'ecl':
            if value not in EYE_COLORS:
                return False
        elif field == 'pid':
            if not re.fullmatch(r'\d{9}', value):
                return False
    return True

def count_valid_entries(data: list, validate_values):
    return len(list(filter(lambda x: validate_entry(x, validate_values), data)))

def parse_input_file(file):
    data = []
    current_entry = {}
    regex = r'\s*(\w+):(\S+)\s*'
    for line in file:
        line = line.rstrip()
        if len(line) == 0:
            if len(current_entry) > 0:
                data.append(current_entry)
                current_entry = {}
            continue
        for m in re.findall(regex, line):
            key, val = m
            current_entry[key] = val
    if len(current_entry) > 0:
        data.append(current_entry)
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    part_1 = count_valid_entries(data, False)
    print("Solution to Part 1 is {}".format(part_1))

    part_2 = count_valid_entries(data, True)
    print("Solution to Part 2 is {}".format(part_2))