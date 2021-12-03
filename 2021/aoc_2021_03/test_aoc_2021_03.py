#!/usr/bin/env python3

import re
from aoc_2021_03 import parse_input_data, calculate_gamma_epsilon, calculate_oxygen_co2

TEST_INPUT = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")

def test_find_location():
    report = parse_input_data(TEST_INPUT)
    (gamma, epsilon) = calculate_gamma_epsilon(report)
    assert gamma == 22
    assert epsilon == 9

def test_oxygen():
    report = parse_input_data(TEST_INPUT)
    oxygen = calculate_oxygen_co2(report, True)
    assert oxygen == 23

def test_co2():
    report = parse_input_data(TEST_INPUT)
    co2 = calculate_oxygen_co2(report, False)
    assert co2 == 10

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
