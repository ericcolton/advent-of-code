#!/usr/bin/env python3

import re
from aoc_2021_02 import parse_input_data, calculate_location, calculate_location_with_aim

TEST_INPUT = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")

def test_find_location():
    commands = parse_input_data(TEST_INPUT)
    (distance, depth) = calculate_location(commands)
    assert distance == 15
    assert depth == 10

def test_find_location_with_aim():
    commands = parse_input_data(TEST_INPUT)
    (distance, depth) = calculate_location_with_aim(commands)
    assert distance == 15
    assert depth == 60

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
