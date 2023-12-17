#!/usr/bin/env python3

import re
from aoc_2023_09 import parse_input_data, build_pyramids, sum_new_last_steps, sum_new_first_steps

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split("\n")

def test_sum_new_last_steps():
    data = parse_input_data(TEST_INPUT)
    pyramids = build_pyramids(data)
    rv = sum_new_last_steps(pyramids)
    assert(rv == 114)

def test_sum_new_first_steps():
    data = parse_input_data(TEST_INPUT)
    pyramids = build_pyramids(data)
    rv = sum_new_first_steps(pyramids)
    assert(rv == 2)

if __name__ == '__main__':
   for symbol in dir():
       if re.match('^test_', symbol):
           print(f"running {symbol}()")
           globals()[symbol]()
   print("Done")
