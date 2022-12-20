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
    nodes = []
    id = 0
    for line in raw_lines:
        nodes.append(parse_line(id, line.rstrip()))
        id += 1
    return nodes

class ValveSystem:

    def __init__(self, nodes: List[Node], verbose: bool = False):
        name_lookup, id_lookup, id_bitmap = {}, {}, {}
        bit = 0
        for node in nodes:
            name_lookup[node.name] = node
            id_lookup[node.id] = node
            if node.rate > 0:
                id_bitmap[node.id] = 0x1 << bit
                bit += 1
        self.name_lookup = name_lookup
        self.id_lookup = id_lookup
        self.id_bitmap = id_bitmap
        self.begin = 0
        self.verbose = verbose

    def time_elapsed(self) -> int:
        return int(time.time() - self.begin)

    # top down dynamic programming model
    # (break down recursely and memoize intermediate states)
    def find_max_pressure_top_down(self, moves: int) -> int:
        self.dp = {}
        self.begin = time.time()        
        return self._top_down(self.name_lookup['AA'].id, 0, moves)

    def _top_down(self, me: int, state: int, moves: int) -> int:
        if moves == 0:
            return 0
        key = me, state, moves
        if key not in self.dp:
            node = self.id_lookup[me]
            best = 0
            for edge in node.edges:
                edge_id = self.name_lookup[edge].id
                best = max(best, self._top_down(edge_id, state, moves - 1))
            if me in self.id_bitmap:
                bit = self.id_bitmap[me]
                if not state & bit:
                    best = max(best, ((moves - 1) * node.rate) + self._top_down(me, state | bit, moves - 1))
            self.dp[key] = best
        return self.dp[key]

    # bottom up dynamic programming model
    # (more memory efficient because we can only need keep the last move's state)
    def find_max_pressure_with_elephant_bottoms_up(self, moves: int) -> int:
        node_count = len(self.id_lookup.keys())
        bitmap_count = len(self.id_bitmap.keys())
        self.begin = time.time()

        if self.verbose:
            print(f"Memory analysis:")
            print(f"me_locations= {node_count} elephant_locations= {node_count} value_states= 2 ^ {bitmap_count} turns= 2 moves= {moves} ...")
            total_mem = node_count ** 2 * 2 ** bitmap_count * 2
            print(f"Total memory required = {total_mem:,} integers")
            print(f"Total states = {total_mem * moves:,}")
            
            print("Init memory...", end="")
        dp = [[[[0] * node_count for _ in range(node_count)] for _ in range(2 ** bitmap_count)] for _ in range(2)]

        if self.verbose:
            print(f"done. [{self.time_elapsed()} seconds]")

        for m in range(1, moves + 1):
            for turn in [1, 0]:
                for state in range(2 ** bitmap_count):
                    for elephant in range(node_count):
                        for me in range(node_count):
                            best = 0
                            if turn == 0:  # me moves
                                node = self.id_lookup[me]
                                if me in self.id_bitmap:
                                    bit = self.id_bitmap[me]
                                    if not state & bit:
                                        best = max(best, ((m - 1) * node.rate) + dp[1][state | bit][elephant][me])
                                for edge in node.edges:
                                    edge_id = self.name_lookup[edge].id
                                    best = max(best, dp[1][state][elephant][edge_id])
                            else:  # elephant moves
                                node = self.id_lookup[elephant]
                                if elephant in self.id_bitmap:
                                    bit = self.id_bitmap[elephant]
                                    if not state & bit:
                                        best = max(best, ((m - 1) * node.rate) + dp[0][state | bit][elephant][me])
                                for edge in node.edges:
                                    edge_id = self.name_lookup[edge].id
                                    best = max(best, dp[0][state][edge_id][me])
                            dp[turn][state][elephant][me] = best

            if self.verbose:
                elapsed = time.time() - self.begin
                print(f"move completed: {m} [{self.time_elapsed()} seconds]")

        start = self.name_lookup['AA'].id
        return dp[0][0][start][start]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        nodes = parse_input_data(raw_input)
        valve_system = ValveSystem(nodes, True)
        part_1 = valve_system.find_max_pressure_top_down(30)
        assert part_1 == 2124
        print(f"The solution to Part 1 is {part_1}")
        print(f"Elapsed: {valve_system.time_elapsed()} seconds")
        print("\n")

        part_2 = valve_system.find_max_pressure_with_elephant_bottoms_up(26)
        assert part_2 == 2775
        print(f"The solution to Part 2 is {part_2}")
        print(f"Elapsed: {valve_system.time_elapsed()} seconds")
