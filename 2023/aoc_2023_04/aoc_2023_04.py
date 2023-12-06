#!/usr/bin/env python3

"""
Advent of Code 2023 Day 4: Scratchcards

https://adventofcode.com/2023/day/4

Solution by Eric Colton

"""

import re
from typing import List
from collections import deque

def count_cascading_scratchcards(data):
    queue = deque([i for i in range(1, len(data))])
    count = 0
    while(len(queue) > 0):
        index = queue.pop()
        count += 1
        winners, yours = data[index]
        score = len(winners & yours)
        for i in range(index, index + score):
            queue.appendleft(i + 1)
    return count

def count_total_points(data):
    total = 0
    for i in range(1, len(data)):
        winners, yours = data[i]
        score = len(winners & yours)
        total += 0 if score == 0 else 2 ** (score - 1)
    return total

def parse_input_data(raw_lines: str):
    cards = [None] # dummy
    for line in raw_lines:
        match = re.match(r'Card\s+(\d+)\:\s+(.*?)\s+\|\s+(.*)\s*$', line.rstrip())
        if match:
            winners = set(map(int, re.split(r'\s+', match.group(2))))
            yours = set(map(int, re.split(r'\s+', match.group(3))))
            cards.append((winners, yours))
        else:
            raise Exception('invalid card syntax')
    return cards

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = count_total_points(data)
        assert part_1 == 22488
        print(f"The solution to Part 1 is {part_1}")

        part_2 = count_cascading_scratchcards(data)
        assert part_2 == 7013204
        print(f"The solution to Part 2 is {part_2}")
