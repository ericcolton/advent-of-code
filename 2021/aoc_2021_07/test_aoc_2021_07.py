#!/usr/bin/env python3

import re
from aoc_2021_07 import parse_input_data, find_optimal_candidates, find_median, find_fuel_required_plustorial, find_fuel_required_linear

TEST_INPUT = """16,1,2,0,4,2,7,1,2,14""".split("\n")

def test_min_fuel_simple():
    positions = parse_input_data(TEST_INPUT)
    median = find_median(positions)
    min_fuel = find_fuel_required_linear(positions, median)
    assert min_fuel == 37

def test_min_fuel_plustorial():
    positions = parse_input_data(TEST_INPUT)
    candidates = find_optimal_candidates(positions)
    min_fuel = part_2 = min(list(map(lambda loc: find_fuel_required_plustorial(positions, loc), candidates)))
    assert min_fuel == 168

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
