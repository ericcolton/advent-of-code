#!/usr/bin/env python3

"""
Advent of Code 2022 Day 16: Proboscidea Volcanium

https://adventofcode.com/2022/day/16

Solution by Eric Colton
"""

import re
import heapq
import time
from typing import List, Dict, Tuple
from collections import namedtuple

Node = namedtuple("Node", ['id', 'name', 'rate', 'edges'])

def parse_line(id: int, line: str) -> Tuple[str, Node]:
    match = re.match(r'Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ([\w\s,]+)', line)
    if not match:
        raise Exception("Unexpected line")
    edges = match.group(3).split(", ")
    return Node(id, match.group(1), int(match.group(2)), edges)

def parse_input_data(raw_lines: List[str]) -> List[Dict[str, Node]]:
    name_lookup, id_lookup = {}, {}
    id = 0
    for line in raw_lines:
        node = parse_line(id, line.rstrip())
        name_lookup[node.name] = node
        id_lookup[id] = node        
        id += 1
    return name_lookup, id_lookup

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

class WithElephant:
    def __init__(self, name_lookup, id_lookup):
        self.name_lookup = name_lookup
        self.id_lookup = id_lookup
        id_bitmap = {}
        i = 0
        for node in self.name_lookup.values():
            if node.rate > 0:
                id_bitmap[node.id] = 0x1 << i
                i += 1
        self.id_bitmap = id_bitmap
        self.dp = {}
        self.begin = time.time()

    def find_max_pressure_with_elephant(self, me, elephant, turn, moves, turned_on):
        if moves == 0:
            return 0
        key = me << 28 | elephant << 22 | turn << 21 | moves << 16 | turned_on << 0
        #key = me, elephant, turn, moves, turned_on
        if key not in self.dp:
            best = 0        
            if turn == 0:
                node = self.id_lookup[me]
                for edge in node.edges:
                    best = max(best, self.find_max_pressure_with_elephant(self.name_lookup[edge].id, elephant, 1, moves, turned_on))
                if node.rate > 0 and not self.id_bitmap[me] & turned_on:
                    new_on = turned_on | self.id_bitmap[me]
                    best = max(best, ((moves - 1) * node.rate) + self.find_max_pressure_with_elephant(me, elephant, 1, moves, new_on))
            else:
                node = self.id_lookup[elephant]
                for edge in node.edges:
                    best = max(best, self.find_max_pressure_with_elephant(me, self.name_lookup[edge].id, 0, moves - 1, turned_on))
                if node.rate > 0 and not self.id_bitmap[elephant] & turned_on:
                    new_on = turned_on | self.id_bitmap[elephant]
                    best = max(best, ((moves - 1) * node.rate) + self.find_max_pressure_with_elephant(me, elephant, 0, moves - 1, new_on))
            self.dp[key] = best
            len_dp_keys = len(self.dp.keys())
            if len_dp_keys % 1_000_000 == 0:
                print(f"dp keys = {len_dp_keys // 1_000_000} [{time.time() - self.begin}]")
        return self.dp[key]


if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        name_lookup, id_lookup = parse_input_data(raw_input)
        # part_1 = find_max_pressure(node_lookup, 'AA', 30, frozenset(), {})
        # assert part_1 == 2124
        # print(f"The solution to Part 1 is {part_1}")

        #part_2 = find_max_pressure_with_elephant(node_lookup, 'AA', 'AA', 0, 26, frozenset(), set(), set(), {})
        begin_time = time.time()
        game = WithElephant(name_lookup, id_lookup)
        part_2 = game.find_max_pressure_with_elephant(name_lookup['AA'].id, name_lookup['AA'].id, 0, 26, 0)
        elapsed = time.time() - begin_time
        print(f"The solution to Part 2 is {part_2} ({elapsed})")
        assert part_1 == 2124



        # part_2 = find_tuning_frequency(data, 4000000)
        # assert part_2 == 13213086906101
        #
