#!/usr/bin/env python3

"""
Advent of Code 2022 Day 5: Supply Stacks

https://adventofcode.com/2022/day/5

Solution by Eric Colton
"""

import re
from collections import deque
from typing import List, Tuple, Set, Deque

def parse_input_data(raw_lines: List[str]) -> Tuple[List[Deque], List[Tuple]]:
    print(len(raw_lines[0]))
    state = [deque([]) for _ in range((len(raw_lines[0]) + 1) // 4)]
    instrs = []
    for line in raw_lines:
        match_stack = re.search(r'\[', line)
        match_instr = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if match_stack:
            for i in range(1, len(line), 4):
                if line[i].isalpha():
                    state[(i - 1)//4].appendleft(line[i])
        elif match_instr:
            count, src, dest = int(match_instr.group(1)), int(match_instr.group(2)), int(match_instr.group(3))
            instrs.append((count, src - 1, dest - 1))
    return state, instrs

def run_instrs(state: List[Deque], instrs: List[Tuple], move_in_bulk: bool):
    for instr in instrs:
        count, src, dest = instr
        buffer = [state[src].pop() for _ in range(count)]
        if move_in_bulk:
            buffer = reversed(buffer)
        state[dest].extend(buffer)

def top_of_stacks(state: List[Deque]) -> str:
    return "".join([state[i][-1]for i in range(len(state))])

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        state, instrs = parse_input_data(raw_input)
        run_instrs(state, instrs, False)
        part_1 = top_of_stacks(state)
        print(part_1)
        assert part_1 == 'CNSZFDVLJ'
        print(f"The solution to Part 1 is {part_1}")

        state, instrs = parse_input_data(raw_input)
        run_instrs(state, instrs, True)
        part_2 = top_of_stacks(state)
        print(part_2)
        assert part_2 == 'QNDWLMGNS'
        print(f"The solution to Part 2 is {part_2}")

