#!/usr/bin/env python3

import re
from aoc_2021_13 import parse_input_data, execute_folds, print_dots

TEST_INPUT = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")

def test_positions_of_dots_on_paper_folded_once():
    dots, folds = parse_input_data(TEST_INPUT)
    execute_folds(dots, folds[:1])
    dot_count = len(dots)
    assert dot_count == 17

def test_printout_of_dots_after_folding():
    dots, folds = parse_input_data(TEST_INPUT)
    execute_folds(dots, folds)
    printout = print_dots(dots)
    assert printout == """#####
#...#
#...#
#...#
#####
"""

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
