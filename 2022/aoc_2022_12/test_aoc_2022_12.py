#!/usr/bin/env python3

import re                                 
from aoc_2022_12 import parse_input_data, find_efficient_path_from_start, find_efficient_path_from_any_a

TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

def test_find_efficient_path_to_from_start():
  data, start_node, dest_node = parse_input_data(TEST_INPUT)
  path_length = find_efficient_path_from_start(data, start_node)
  assert path_length == 31

def test_find_efficient_path_from_any_a():
  data, start_node, dest_node = parse_input_data(TEST_INPUT)
  path_length = find_efficient_path_from_any_a(data, dest_node)
  assert path_length == 29

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
