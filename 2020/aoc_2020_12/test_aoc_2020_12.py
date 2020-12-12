#!/usr/bin/env python3

import re
from aoc_2020_12 import parse_input_file, Ferry

INPUT_DATA = input_data = """F10
N3
F7
R90
F11""".rsplit()

def test_part_1():
    data = parse_input_file(INPUT_DATA)
    ferry = Ferry(1, 0)
    ferry.execute_instructions(data)
    manhattan_distance = ferry.manhattan_distance()
    assert manhattan_distance == 25

def test_part_2():
    data = parse_input_file(INPUT_DATA)
    ferry = Ferry(10, 1, True)
    ferry.execute_instructions(data)
    manhattan_distance = ferry.manhattan_distance()
    assert manhattan_distance == 286

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")