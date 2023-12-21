#!/usr/bin/env python3

import re
from aoc_2023_11 import parse_input_data, expand_universe, count_total_lengths

TEST_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")

def test_total_lengths_with_expansion_2():
    data = parse_input_data(TEST_INPUT)
    expanded_stars = expand_universe(data, 2)
    rv = count_total_lengths(expanded_stars)
    assert(rv == 374)

def test_total_lengths_with_expansion_10():
    data = parse_input_data(TEST_INPUT)
    expanded_stars = expand_universe(data, 10)
    rv = count_total_lengths(expanded_stars)
    assert(rv == 1030)

def test_total_lengths_with_expansion_100():
    data = parse_input_data(TEST_INPUT)
    expanded_stars = expand_universe(data, 100)
    rv = count_total_lengths(expanded_stars)
    assert(rv == 8410)

if __name__ == '__main__':
   for symbol in dir():
       if re.match('^test_', symbol):
           print(f"running {symbol}()")
           globals()[symbol]()
   print("Done")
