#!/usr/bin/env python3

import re
from aoc_2022_03 import parse_input_data, find_sum_outliers, identify_outlier, find_3_intersection, find_sum_3_intersections

TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

def test_identify_outliers():
    data = parse_input_data(TEST_INPUT)
    assert identify_outlier(data[0]) == 16
    assert identify_outlier(data[1]) == 38
    assert identify_outlier(data[2]) == 42
    assert identify_outlier(data[3]) == 22
    assert identify_outlier(data[4]) == 20
    assert identify_outlier(data[5]) == 19

    assert find_sum_outliers(data) == 157

def test_find_3_intersection():
    data = parse_input_data(TEST_INPUT)
    assert find_3_intersection(data[0], data[1], data[2]) == 18
    assert find_3_intersection(data[3], data[4], data[5]) == 52
    
    assert find_sum_3_intersections(data) == 70

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
