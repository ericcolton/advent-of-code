#!/usr/bin/env python3

import re
from aoc_2022_09 import parse_input_data, find_tail_visited_count, KnotMap
TEST_INPUT_1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

TEST_INPUT_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")

def test_find_tail_spaces_len_2_visited_count():
    instrs = parse_input_data(TEST_INPUT_1)
    knot_map = KnotMap(2)
    knot_map.exec_instrs(instrs)
    count = find_tail_visited_count(knot_map)
    assert count == 13

def test_find_tail_spaces_len_10_visited_count():
    instrs = parse_input_data(TEST_INPUT_1)
    knot_map = KnotMap(10)
    knot_map.exec_instrs(instrs)
    count = find_tail_visited_count(knot_map)
    assert count == 1

def test_find_tail_spaces_len_10_visited_count_input_2():
    instrs = parse_input_data(TEST_INPUT_2)
    knot_map = KnotMap(10)
    knot_map.exec_instrs(instrs)
    count = find_tail_visited_count(knot_map)
    assert count == 36

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
