#!/usr/bin/env python3

import re
from aoc_2023_01 import parse_input_data, find_sum_all_lines

TEST_INPUT_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split("\n")

TEST_INPUT_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")

def test_simple_filter():
    data = parse_input_data(TEST_INPUT_1)
    assert(find_sum_all_lines(data, False) == 142)

def test_inc_words():
    data = parse_input_data(TEST_INPUT_2)
    assert(find_sum_all_lines(data, True) == 281)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
