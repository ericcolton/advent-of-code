#!/usr/bin/env python3

import re
from aoc_2022_04 import parse_input_data, fully_contained, count_matching, partially_contained

TEST_INPUT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")

def test_fully_contained():
    data = parse_input_data(TEST_INPUT)
    assert fully_contained(data[0]) == False
    assert fully_contained(data[1]) == False
    assert fully_contained(data[2]) == False
    assert fully_contained(data[3]) == True
    assert fully_contained(data[4]) == True
    assert fully_contained(data[5]) == False

    assert count_matching(data, fully_contained) == 2

def test_partially_contained():
    data = parse_input_data(TEST_INPUT)
    assert partially_contained(data[0]) == False
    assert partially_contained(data[1]) == False
    assert partially_contained(data[2]) == True
    assert partially_contained(data[3]) == True
    assert partially_contained(data[4]) == True
    assert partially_contained(data[5]) == True
    
    assert count_matching(data, partially_contained) == 4


if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
