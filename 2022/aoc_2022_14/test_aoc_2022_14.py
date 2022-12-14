#!/usr/bin/env python3

import re
from aoc_2022_14 import parse_input_data, draw_rock_lines, add_sand_until_overflow, add_sand_until_full, Reservoir

TEST_INPUT = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")

def test_fill_sand_until_overflow():
    data = parse_input_data(TEST_INPUT)
    r = Reservoir()
    draw_rock_lines(r, data)
    count = add_sand_until_overflow(r)
    assert count == 24

def test_fill_sand_until_full():
    data = parse_input_data(TEST_INPUT)
    r = Reservoir()
    draw_rock_lines(r, data)
    r.max_y += 1
    count = add_sand_until_full(r)
    assert count == 93

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
