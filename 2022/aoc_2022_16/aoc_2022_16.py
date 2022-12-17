#!/usr/bin/env python3

"""
Advent of Code 2022 Day 16: Proboscidea Volcanium

https://adventofcode.com/2022/day/16

Solution by Eric Colton
"""

import re
import heapq
from typing import List, Dict, Tuple
from collections import namedtuple

Node = namedtuple("Node", ['name', 'rate', 'edges'])

def parse_line(line: str) -> Tuple[str, Node]:
    match = re.match(r'Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)', line)
    if not match:
        raise Exception("Unexpected line")
    edges = match.group(3).split(", ")
    return Node(match.group(1), int(match.group(2)), edges)

def parse_input_data(raw_lines: List[str]) -> List[Dict[str, Node]]:
    node_lookup = {}
    for line in raw_lines:
        node = parse_line(line.rstrip())
        node_lookup[node.name] = node
    return node_lookup

def find_max_pressure(node_lookup, name, moves, turned_on, dp):
    if moves == 0:
        return 0
    key = name, moves, turned_on
    if key not in dp:
        node = node_lookup[name]
        best = 0
        for edge in node.edges:
            best = max(best, find_max_pressure(node_lookup, edge, moves - 1, turned_on, dp))
        if node.rate > 0 and name not in turned_on:
            new_on =  set(turned_on)
            new_on.add(name)
            new_on = frozenset(new_on)
            best = max(best, ((moves - 1) * node.rate) + find_max_pressure(node_lookup, name, moves -1, new_on, dp))
        dp[key] = best
    return dp[key]

def find_max_pressure_with_elephant(node_lookup, me, elephant, turn, moves, turned_on, me_seen, elephant_seen, dp):
    if moves == 0:
        return 0
    key = me, elephant, turn, turned_on, moves
    if key not in dp:
        best = 0        
        if turn == 0:
            node = node_lookup[me]
            for edge in node.edges:
                if edge not in me_seen:
                    me_seen.add(me)
                    best = max(best, find_max_pressure_with_elephant(node_lookup, edge, elephant, 1, moves, turned_on, me_seen, elephant_seen, dp))
                    me_seen.remove(me)
            if node.rate > 0 and me not in turned_on:
                new_on = set(turned_on)
                new_on.add(me)
                new_on = frozenset(new_on)
                best = max(best, ((moves - 1) * node.rate) + find_max_pressure_with_elephant(node_lookup, me, elephant, 1, moves, new_on, set(), elephant_seen, dp))
        else:
            node = node_lookup[elephant]
            for edge in node.edges:
                if edge not in elephant_seen:
                    elephant_seen.add(elephant)
                    best = max(best, find_max_pressure_with_elephant(node_lookup, me, edge, 0, moves - 1, turned_on, me_seen, elephant_seen, dp))
                    elephant_seen.remove(elephant)
            if node.rate > 0 and elephant not in turned_on:
                new_on =  set(turned_on)
                new_on.add(elephant)
                new_on = frozenset(new_on)
                best = max(best, ((moves - 1) * node.rate) + find_max_pressure_with_elephant(node_lookup, me, elephant, 0, moves - 1, new_on, me_seen, set(), dp))
        dp[key] = best
    return dp[key]


if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        node_lookup = parse_input_data(raw_input)
        part_1 = find_max_pressure(node_lookup, 'AA', 30, frozenset(), {})
        assert part_1 == 2124
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_max_pressure_with_elephant(node_lookup, 'AA', 'AA', 0, 26, frozenset(), set(), set(), {})
        print(f"The solution to Part 2 is {part_2}")
        assert part_1 == 2124



        # part_2 = find_tuning_frequency(data, 4000000)
        # assert part_2 == 13213086906101
        #
