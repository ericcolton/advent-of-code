#!/usr/bin/env python3

import re
from aoc_2019_06 import OrbitMap, parse_input_data

def test_count_total_orbits():
    test_data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    input = parse_input_data(test_data)
    om = OrbitMap(input)
    assert om.count_total_orbits() == 42

def test_calc_distance_between():
    test_data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
    input = parse_input_data(test_data)
    om = OrbitMap(input)
    assert om.calc_distance_between('YOU', 'SAN') == 4

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
