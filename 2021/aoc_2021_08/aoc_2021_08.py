#!/usr/bin/env python3

"""
Advent of Code 2021 Day 8: Seven Segment Search

https://adventofcode.com/2021/day/8

Solution by Eric Colton
"""

import re
import math
from typing import List, Dict

def parse_input_data(raw_input: List[str]) -> List[int]:
    all_digits, output_digits = [], []
    for line in raw_input:
        match = re.match(r'(.*?)\s\|\s(.*)', line.rstrip())
        if match:
            all_digits.append(match.group(1).split())
            output_digits.append([''.join(sorted(list(word))) for word in match.group(2).split()])
    return all_digits, output_digits

def count_1_4_7_8(output_digits: List[str]) -> int:
    summ = 0
    target_lengths = set([2, 3, 4, 7])
    for record in output_digits:
        for digit in record:
            if len(digit) in target_lengths:
                summ += 1
    return summ

def build_translation(record: List[str]) -> Dict[str, int]:
    lengths = {}
    translation = {'abcdefg': 8}
    for word in record:
        if len(word) not in lengths:
            lengths[len(word)] = []
        lengths[len(word)].append(set(list(word)))                
    translation[''.join(sorted(lengths[2][0]))] = 1
    translation[''.join(sorted(lengths[3][0]))] = 7
    translation[''.join(sorted(lengths[4][0]))] = 4
    used = set()
    for i, len_six in enumerate(lengths[6]):
        intersection_4 = len_six & lengths[4][0]
        if len(intersection_4) == 4:
            translation[''.join(sorted(len_six))] = 9
            used.add(i)
            continue
        intersection_2 = len_six & lengths[2][0]
        if len(intersection_2) == 1:
            translation[''.join(sorted(len_six))] = 6
            br = next(iter(intersection_2))
            tr = next(iter(lengths[2][0] ^ intersection_2))
            used.add(i)
            continue
    for i, len_six in enumerate(lengths[6]):
        if i not in used:
            translation[''.join(sorted(len_six))] = 0
    for len_five in lengths[5]:
        if tr in len_five and br in len_five:
            translation[''.join(sorted(len_five))] = 3
        elif br in len_five:
            translation[''.join(sorted(len_five))] = 5
        else:
            translation[''.join(sorted(len_five))] = 2
    return translation

def build_translations(records: List[List[str]]) -> List[Dict[str, int]]:
    return [build_translation(r) for r in records]

def record_total(translation: Dict[str, int], record):
    total = 0
    for word in record:
        total *= 10
        total += translation[word]
    return total

def translate_and_sum_output(translations, output_digits):
    return sum(map(lambda i: record_total(translations[i], output_digits[i]), range(len(output_digits))))

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        (all_digits, output_digits) = parse_input_data(raw_input)
        part_1 = count_1_4_7_8(output_digits)
        assert part_1 == 452
        print(f"The solution to Part 1 is {part_1}")

        translations = build_translations(all_digits)
        part_2 = translate_and_sum_output(translations, output_digits)
        assert part_2 == 1096964
        print(f"The solution to Part 2 is {part_2}")
