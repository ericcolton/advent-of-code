#!/usr/bin/env python3

import re
from aoc_2023_10 import parse_input_data, find_circular_route, total_encircled_points

TEST_INPUT_1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF""".split("\n")

TEST_INPUT_2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".split("\n")

def test_futhest_point_one():
    data = parse_input_data(TEST_INPUT_1)
    route = find_circular_route(data)
    rv = len(route.keys()) // 2
    assert(rv == 4)

def test_find_encircled_points_one():
    data = parse_input_data(TEST_INPUT_1)
    route = find_circular_route(data)
    rv = total_encircled_points(route, data)
    assert(rv == 1)

def test_find_encircled_points_two():
    data = parse_input_data(TEST_INPUT_2)
    route = find_circular_route(data)
    rv = total_encircled_points(route, data)
    assert(rv == 10)

if __name__ == '__main__':
   for symbol in dir():
       if re.match('^test_', symbol):
           print(f"running {symbol}()")
           globals()[symbol]()
   print("Done")
