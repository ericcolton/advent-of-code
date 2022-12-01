#!/usr/bin/env python3

import re
from aoc_2022_01 import parse_input_data, find_sum_highest_calories

TEST_INPUT = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000""".split("\n")

def test_elf_calories():
    data = parse_input_data(TEST_INPUT)
    assert sum(data[0]) == 6000
    assert sum(data[1]) == 4000
    assert sum(data[2]) == 11000
    assert sum(data[3]) == 24000
    assert sum(data[4]) == 10000

def test_top_3_elf_calories():
    data = parse_input_data(TEST_INPUT)
    assert find_sum_highest_calories(data, 3) == 45000

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
