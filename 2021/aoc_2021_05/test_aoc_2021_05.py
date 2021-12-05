#!/usr/bin/env python3

import re
from aoc_2021_05 import parse_input_data, paint_lines, sum_point_counts_2_or_greater

TEST_INPUT = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")

def test_lines_count_without_diagonals():
    lines = parse_input_data(TEST_INPUT)
    points_by_count = paint_lines(lines, True)
    rv = sum_point_counts_2_or_greater(points_by_count)
    assert rv == 5

def test_lines_count_with_diagonals():
    lines = parse_input_data(TEST_INPUT)
    points_by_count = paint_lines(lines, False)
    rv = sum_point_counts_2_or_greater(points_by_count)
    assert rv == 12

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
