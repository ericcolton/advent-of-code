#!/usr/bin/env python3

import re
from aoc_2020_11 import parse_input_file, iterate_until_stable, count_total_occupied

INPUT_DATA = input_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
""".rsplit()

def test_part_1():
    data = parse_input_file(INPUT_DATA)
    data = iterate_until_stable(data, True, 4)
    occupied_count = count_total_occupied(data)
    assert occupied_count == 37

def test_part_2():
    data = parse_input_file(INPUT_DATA)
    data = iterate_until_stable(data, False, 5)
    occupied_count = count_total_occupied(data)
    assert occupied_count == 26

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")