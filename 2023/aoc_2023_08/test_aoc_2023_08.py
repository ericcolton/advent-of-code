#!/usr/bin/env python3

import re
from typing import Dict
#from aoc_2023_08 import parse_input_data, 

TEST_INPUT_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".split("\n")

TEST_INPUT_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split("\n")

TEST_INPUT_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".split("\n")

def reached_end_state(nodes):
    for n in nodes:
        if n[2] != 'Z':
            return False
    return True

def count_simultaneous_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    count = 0
    nodes = []
    for key in lookup.keys():
        if key[2] == 'A':
            nodes.append(key)
    while not reached_end_state(nodes):
        dir = 0 if instrs[count % len(instrs)] == 'L' else 1
        for i in range(len(nodes)):
            nodes[i] = lookup[nodes[i]][dir]
        count += 1
    return count

def count_total_steps(data: tuple[str, Dict[str, tuple[str, str]]]) -> int:
    instrs, lookup = data
    count = 0
    node = 'AAA'
    while node != 'ZZZ':
        dir = 0 if instrs[count % len(instrs)] == 'L' else 1
        node = lookup[node][dir]
        count += 1
    return count

def parse_input_data(raw_lines: str) -> tuple[str, Dict[str, tuple[str, str]]]:
    instrs = raw_lines[0].rstrip()
    lookup = {}
    for i in range(2, len(raw_lines)):
        match = re.match(r'(\w\w\w) = \((\w\w\w), (\w\w\w)\)', raw_lines[i].rstrip())
        if match:
            lookup[match.group(1)] = (match.group(2), match.group(3))
        else:
            raise Exception("Unable to parse mapping")
    return (instrs, lookup)

def test_sum_of_steps_one():
    data = parse_input_data(TEST_INPUT_1)
    rv = count_total_steps(data)
    assert(rv == 2)

def test_sum_of_steps_two():
    data = parse_input_data(TEST_INPUT_2)
    rv = count_total_steps(data)
    assert(rv == 6)    

def test_sum_of_simultaneous_steps():
    data = parse_input_data(TEST_INPUT_3)
    rv = count_simultaneous_steps(data)
    assert(rv == 6)

# def test_sum_of_winnings_with_jokers():
#     data = parse_input_data(TEST_INPUT)
#     part_2 = find_sum_of_winnings(data, True)
#     assert(part_2 == 5905)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
