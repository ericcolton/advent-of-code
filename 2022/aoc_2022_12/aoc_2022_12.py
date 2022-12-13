#!/usr/bin/env python3

"""
Advent of Code 2022 Day 12: Hill Climbing Algorithm

https://adventofcode.com/2022/day/12

Solution by Eric Colton
"""

import re
from typing import List, Dict, Tuple, Set
from collections import deque

class Node:
    def __init__(self, y: int, x: int, char: str):
        self.y = y
        self.x = x
        self.is_start = False
        self.is_dest = False
        if char == 'S':
            self.height = 0
            self.is_start = True
        elif char == 'E':
            self.height = 25
            self.is_dest = True
        else:
            self.height = ord(char) - ord('a')

def get_neighbors(node: Node, data: Dict[Tuple, Dict], seen: Set[Node], going_down: bool) -> List[Node]:
    neighbors = []
    for neighbor_loc in [(node.y + 1, node.x), (node.y - 1, node.x), (node.y, node.x + 1), (node.y, node.x - 1)]:
        if neighbor_loc in data and neighbor_loc not in seen:
            neighbor = data[neighbor_loc]
            if ((going_down and neighbor.height >= node.height - 1)
                or (not going_down and neighbor.height <= node.height + 1)):
                seen.add(neighbor_loc)
                neighbors.append(neighbor)
    return neighbors

def find_efficient_path_from_start(data: List[List[int]], start_node: Node) -> int:
    count = 0
    seen = set([start_node])
    queue = deque([None, start_node])    
    while len(queue) > 1:
        current = queue.pop()
        if current == None:
            count += 1
            queue.appendleft(None)
            continue
        if current.is_dest:
            return count
        queue.extendleft(get_neighbors(current, data, seen, False))
    return -1

def find_efficient_path_from_any_a(data: List[List[int]], start_node: Node) -> int:
    count = 0
    seen = set([start_node])
    queue = deque([None, start_node])    
    while len(queue) > 1:
        current = queue.pop()
        if current == None:
            count += 1
            queue.appendleft(None)
            continue
        if current.height == 0:
            return count
        queue.extendleft(get_neighbors(current, data, seen, True))
    return -1

def parse_input_data(raw_lines: List[str]) -> List[List[int]]:
    data = {}
    start_node, dest_node = None, None
    for y, line in enumerate(raw_lines):
        for x, c in enumerate(line.rstrip()):
            node = Node(y, x, c)
            data[(y, x)] = node
            if node.is_start:
                start_node = node
            elif node.is_dest:
                dest_node = node

    if start_node is None:
        raise Exception("start node not found")
    elif dest_node is None:
        raise Exception("dest node not found")
    return data, start_node, dest_node

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data, start_node, dest_node = parse_input_data(raw_input)
        part_1 = find_efficient_path_from_start(data, start_node)
        assert part_1 == 481
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_efficient_path_from_any_a(data, dest_node)
        assert part_2 == 480
        print(f"The solution to Part 2 is {part_2}")

