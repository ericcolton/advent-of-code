#!/usr/bin/env python3

import re
from aoc_2021_15 import parse_input_data, find_length_min_path, Grid

TEST_INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")

def test_find_length_min_path():
    grid_data = parse_input_data(TEST_INPUT)
    grid = Grid(grid_data, False)
    min_length = find_length_min_path(grid)
    assert min_length == 40

def test_find_length_min_path_with_expanded_grid():
    grid_data = parse_input_data(TEST_INPUT)
    grid = Grid(grid_data, True)
    min_length = find_length_min_path(grid)
    assert min_length == 315

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
