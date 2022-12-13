#!/usr/bin/env python3

"""
Advent of Code 2022 Day 13: Distress Signal

https://adventofcode.com/2022/day/13

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

class Item:
    def __init__(self, content):
        self.content = content

def parse_list(line: str, index: int) -> Item:
    assert line[index] == '['
    content = []
    i = index + 1
    while line[i] != ']':
        if line[i] == '[':
            list_content, i = parse_list(line, i)
            content.append(list_content)
            continue
        if line[i] == ',':
            i += 1
            continue
        match = re.match(r'(\d+)', line[i:])
        if match:
            i += len(match.group(1))
            content.append(int(match.group(1)))
            continue
        raise Exception("Parse error")

    return Item(content), i + 1

def parse_input_data(raw_lines: List[str]) -> List[List[int]]:
    i = 0
    data = []
    while i < len(raw_lines):
        data.append((parse_list(raw_lines[i], 0)[0], parse_list(raw_lines[i+1], 0)[0]))
        i += 3
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        print(data)
        # part_1 = find_efficient_path_from_start(data, start_node)
        # assert part_1 == 481
        # print(f"The solution to Part 1 is {part_1}")

        # part_2 = find_efficient_path_from_any_a(data, dest_node)
        # assert part_2 == 480
        # print(f"The solution to Part 2 is {part_2}")

