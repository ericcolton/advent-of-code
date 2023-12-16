#!/usr/bin/env python3

import re
from aoc_2023_08 import parse_input_data, count_simple_steps, count_simultaneous_steps

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

def test_sum_of_steps_one():
    data = parse_input_data(TEST_INPUT_1)
    rv = count_simple_steps(data)
    assert(rv == 2)

def test_sum_of_steps_two():
    data = parse_input_data(TEST_INPUT_2)
    rv = count_simple_steps(data)
    assert(rv == 6)    

def test_sum_of_simultaneous_steps():
    data = parse_input_data(TEST_INPUT_3)
    rv = count_simultaneous_steps(data)
    assert(rv == 6)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
