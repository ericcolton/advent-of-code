#!/usr/bin/env python3

"""
Advent of Code 2021 Day 12: Passage Pathing

https://adventofcode.com/2021/day/12

Solution by Eric Colton
"""

import re
from typing import List, Dict, Tuple, Set, Optional

def parse_input_line(line: str) -> Tuple[str, str]:
    match = re.fullmatch(r'(\w+)\-(\w+)', line)
    if match:
        return (match.group(1), match.group(2))
    raise Exception(f"Could not parse input line: {line.rstrip()}")

def parse_input_data(raw_input: List[str]) -> List[Tuple[str, str]]:
    return [parse_input_line(l.rstrip()) for l in raw_input]

def build_graph(edges: List[Tuple[str, str]]) -> Tuple[Dict[str, Set[str]], Set[str]]:
    graph = {}
    big_nodes = set()
    for edge in edges:
        if edge[0] == edge[0].upper():
            big_nodes.add(edge[0])
        if edge[1] == edge[1].upper():
            big_nodes.add(edge[1])
        if edge[0] not in graph:
            graph[edge[0]] = set()
        graph[edge[0]].add(edge[1])
        if edge[1] not in graph:
            graph[edge[1]] = set()
        graph[edge[1]].add(edge[0])
    return graph, big_nodes

def find_all_paths(graph: Dict[str, Set[str]], big_nodes: Set[str], allowing_double_visit: bool = False):

    def backtrack(node: str):
        
        if node == 'end':
            paths.append('-'.join(current_path))
            return

        nonlocal double_visit
        for edge in graph[node]:
            if edge not in big_nodes:
                if edge in seen:
                    if (allowing_double_visit and
                        double_visit == None and
                        edge != 'start' and
                        edge != 'end'):
                        double_visit = edge
                    else:
                        continue
            seen.add(edge)
            current_path.append(edge)
            backtrack(edge)
            current_path.pop()
            if double_visit == edge:
                double_visit = None
            else:
                seen.discard(edge)

    paths = []
    current_path = ['start']
    seen = set(['start'])
    double_visit = None
    backtrack('start')
    return len(paths)

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        edges = parse_input_data(raw_input)
        graph, big_nodes = build_graph(edges)
        part_1 = find_all_paths(graph, big_nodes)
        assert part_1 == 5252
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_all_paths(graph, big_nodes, True)
        assert part_2 == 147784
        print(f"The solution to Part 1 is {part_2}")

