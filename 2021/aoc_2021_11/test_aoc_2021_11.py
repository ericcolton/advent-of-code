#!/usr/bin/env python3

import re
from aoc_2021_11 import parse_input_data, simulate_rounds, simulate_until_all_flash

TEST_INPUT = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

def test_count_flashes_100_rounds():
    grid = parse_input_data(TEST_INPUT)
    count = simulate_rounds(grid, 100)
    assert count == 1656

def test_count_first_time_all_flash():
    grid = parse_input_data(TEST_INPUT)
    count = simulate_until_all_flash(grid)
    assert count == 195

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
