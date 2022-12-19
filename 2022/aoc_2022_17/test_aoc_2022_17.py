#!/usr/bin/env python3

import re
from aoc_2022_17 import parse_input_data, run_tetris

TEST_INPUT = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""".split("\n")

def test_2022_rocks():
    data = parse_input_data(TEST_INPUT)
    height = run_tetris(data, 2022)
    assert height == 3068

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
