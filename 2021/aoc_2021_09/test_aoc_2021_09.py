#!/usr/bin/env python3

import re
from aoc_2021_09 import parse_input_data, find_low_points, sum_risk_levels, find_basin_sizes, product_three_largest_basins

TEST_INPUT = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

def test_sum_risk_levels():
    grid = parse_input_data(TEST_INPUT)
    low_points = find_low_points(grid)
    summ = sum_risk_levels(grid, low_points)
    assert summ == 15

def test_find_product_three_largest_basins():
    grid = parse_input_data(TEST_INPUT)
    low_points = find_low_points(grid)
    basin_sizes = find_basin_sizes(grid, low_points)
    product = product_three_largest_basins(basin_sizes)
    assert product == 1134

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
