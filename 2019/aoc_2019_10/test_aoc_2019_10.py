#!/usr/bin/env python

import re
from aoc_2019_10 import parse_input_data, find_max_observables

def test_case_one():
    test_data = '''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####'''
    input = parse_input_data(test_data)
    max, location = find_max_observables(input)
    loc_x, loc_y = location
    assert max == 33
    assert loc_x == 5
    assert loc_y == 8

def test_case_two():
    test_data = '''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''
    input = parse_input_data(test_data)
    max, location = find_max_observables(input)
    loc_x, loc_y = location
    assert max == 35
    assert loc_x == 1
    assert loc_y == 2

def test_case_three():
    test_data = '''.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..'''
    input = parse_input_data(test_data)
    max, location = find_max_observables(input)
    loc_x, loc_y = location
    assert max == 41
    assert loc_x == 6
    assert loc_y == 3

def test_case_four():
    test_data = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''
    input = parse_input_data(test_data)
    max, location = find_max_observables(input)
    loc_x, loc_y = location
    assert max == 210
    assert loc_x == 11
    assert loc_y == 13

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print("Running {symbol}()")
            globals()[symbol]()
    print("Done")