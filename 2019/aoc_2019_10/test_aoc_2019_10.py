#!/usr/bin/env python3

import re
from aoc_2019_10 import parse_input_data, find_max_observables, find_destory_order

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


def test_case_four_destroy_order():
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
    location = (11, 13)
    destroy_order = find_destory_order(location, input)

    assert destroy_order[0] == (11, 12)
    assert destroy_order[1] == (12, 1)
    assert destroy_order[2] == (12, 2)
    assert destroy_order[9] == (12, 8)
    assert destroy_order[19] == (16, 0)
    assert destroy_order[49] == (16, 9)
    assert destroy_order[99] == (10, 16)
    assert destroy_order[198] == (9, 6)
    assert destroy_order[199] == (8, 2)
    assert destroy_order[200] == (10, 9)
    assert destroy_order[298] == (11, 1)

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")
