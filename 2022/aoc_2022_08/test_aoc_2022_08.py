#!/usr/bin/env python3

import re
from aoc_2022_08 import parse_input_data, find_visible, find_visible_trees_count, find_max_visible_distance
TEST_INPUT = """30373
25512
65332
33549
35390""".split("\n")

def test_find_num_visible_trees():
    data = parse_input_data(TEST_INPUT)
    visible = find_visible(data)
    visible_count = find_visible_trees_count(visible)
    assert visible_count == 21

def test_find_max_visibility():
    data = parse_input_data(TEST_INPUT)
    best_visibility = find_max_visible_distance(data)
    assert best_visibility == 8

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
