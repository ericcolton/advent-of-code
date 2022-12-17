#!/usr/bin/env python3

import re
from aoc_2022_16 import parse_input_data, find_max_pressure, find_max_pressure_with_elephant

TEST_INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".split("\n")

def test_max_pressure():
    node_lookup = parse_input_data(TEST_INPUT)
    max_pressure = find_max_pressure(node_lookup, 'AA', 30, frozenset(), {})
    assert max_pressure == 1651

def test_max_pressure_with_elephant():
    node_lookup = parse_input_data(TEST_INPUT)
    max_pressure = find_max_pressure_with_elephant(node_lookup, 'AA', 'AA', 0, 26, frozenset(), set(), set(), {})
    assert max_pressure == 1707

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
