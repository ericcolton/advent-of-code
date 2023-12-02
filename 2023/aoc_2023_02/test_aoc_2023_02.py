#!/usr/bin/env python3

import re
from aoc_2023_02 import parse_input_data, find_sum_passing_games, find_sum_powers_min_contents

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split("\n")

def test_sum_passing_games():
    data = parse_input_data(TEST_INPUT)
    part_1 = find_sum_passing_games(data)
    assert(part_1 == 8)

def test_sum_powers_min_contents():
    data = parse_input_data(TEST_INPUT)
    part_2 = find_sum_powers_min_contents(data)
    assert(part_2 == 2286)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
