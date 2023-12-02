#!/usr/bin/env python3

"""
Advent of Code 2023 Day 1: Trebuchet?!

https://adventofcode.com/2023/day/1

Solution by Eric Colton
"""

from typing import List

def build_trie(inc_words: bool) -> dict:
    lookup = {"1": 1,
              "2": 2,
              "3": 3,
              "4": 4,
              "5": 5,
              "6": 6,
              "7": 7,
              "8": 8,
              "9": 9,
             }

    if inc_words:
        words = {"one": 1,
                 "two": 2,
                 "three": 3,
                 "four": 4,
                 "five": 5,
                 "six": 6,
                 "seven": 7,
                 "eight" : 8,
                 "nine": 9,
                }
        lookup.update(words)
    trie = {}
    for (key, val) in lookup.items():
        node = trie
        for c in key:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["_"] = val
    return trie

def parse_input_data(raw_lines: str) -> List[str]:
    return list(map(lambda l: l.rstrip(), raw_lines))

def digits_inc_words(line: str, trie: dict) -> List[int]:
    digits = []
    i = 0
    while i < len(line):
        node = trie        
        j = i
        while j < len(line) and line[j] in node:
            node = node[line[j]]
            j += 1
        if "_" in node:
            digits.append(node["_"])
        i += 1
    return digits

def find_num_for_line(line: str, trie: dict) -> int:
    digits = digits_inc_words(line, trie)
    rv = int(f"{str(digits[0])}{str(digits[-1])}")
    return rv

def find_sum_all_lines(lines: List[str], inc_words: bool) -> int:
    return sum(map(lambda x: find_num_for_line(x, build_trie(inc_words)), lines))

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_all_lines(data, False)
        assert part_1 == 54916
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_all_lines(data, True)
        assert part_2 == 54728
        print(f"The solution to Part 2 is {part_2}")
