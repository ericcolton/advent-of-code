#!/usr/bin/env python3

"""
Advent of Code 2021 Day 10: Smoke Basin

https://adventofcode.com/2021/day/10

Solution by Eric Colton
"""

import re
from collections import deque
from typing import List, Dict, Tuple, Optional

def parse_input_data(raw_input: List[str]) -> List[List[int]]:
    return [row.rstrip() for row in raw_input]

def find_first_corrupted(record: str) -> Optional[str]:
    stack = deque()
    for char in record:
        if char == '[' or char == '{' or char == '(' or char == '<':
            stack.append(char)
        elif char == ']' or char == '}' or char == ')' or char == '>':
            counter = stack.pop()
            if ((counter == '[' and char != ']') or
                (counter == '{' and char != '}') or
                (counter == '(' and char != ')') or
                (counter == '<' and char != '>')):
                return char
    return None

def find_completion(record: str) -> Optional[str]:
    stack = deque()
    for char in record:
        if char == '[' or char == '{' or char == '(' or char == '<':
            stack.append(char)
        elif char == ']' or char == '}' or char == ')' or char == '>':
            counter = stack.pop()
            if ((counter == '[' and char != ']') or
                (counter == '{' and char != '}') or
                (counter == '(' and char != ')') or
                (counter == '<' and char != '>')):
                return None
    completion = ""
    while len(stack) > 0:
        char = stack.pop()
        if char == '[':
            completion += ']'
        elif char == '{':
            completion += '}'            
        elif char == '(':
            completion += ')'
        elif char == '<':
            completion += '>'
    return completion

def collect_first_corrupted(records: List[str]) -> List[str]:
    first_corrupted = []
    for record in records:
        corrupted_char = find_first_corrupted(record)
        if corrupted_char:
            first_corrupted.append(corrupted_char)
    return first_corrupted

def score_first_corrupted(first_corrupted: List[str]) -> int:
    score = 0
    for corrupted in first_corrupted:
        if corrupted == ')':
            score += 3
        elif corrupted == ']':
            score += 57
        elif corrupted == '}':
            score += 1197
        elif corrupted == '>':
            score += 25137
        else:
            raise Exception(f"Unexpected corrupted char: {corrupted}")
    return score

def collect_completions(records: List[str]) -> List[str]:
    completions = []
    for record in records:
        completion = find_completion(record)
        if completion:
            completions.append(completion)
    return completions

def score_completion(completion: str) -> int:
    score = 0
    for char in completion:
        score *= 5
        if char == ')':
            score += 1
        elif char == ']':
            score += 2
        elif char == '}':
            score += 3
        elif char == '>':
            score += 4
        else:
            raise Exception(f"Unexpected completion char: '{char}'")
    return score

def score_completions(completions: List[str]) -> int:
    scores = [score_completion(c) for c in completions]
    return sorted(scores)[(len(scores) - 1)//2]


if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        records = parse_input_data(raw_input)
        first_corrupted = collect_first_corrupted(records)
        part_1 = score_first_corrupted(first_corrupted)
        assert part_1 == 243939
        print(f"The solution to Part 1 is {part_1}")

        completions = collect_completions(records)
        part_2 = score_completions(completions)
        assert part_2 == 2421222841
        print(f"The solution to Part 2 is {part_2}")


