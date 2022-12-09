#!/usr/bin/env python3

import re
from aoc_2022_09 import parse_input_data, find_tail_visited_count, KnotMap
TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

def test_find_tail_spaces_visited_count():
    instrs = parse_input_data(TEST_INPUT)
    knot_map = KnotMap()
    knot_map.exec_instrs(instrs)
    count = find_tail_visited_count(knot_map)
    assert count == 13

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
