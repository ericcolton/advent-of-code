#!/usr/bin/env python3

"""
Advent of Code 2022 Day 11: Monkey in the Middle

https://adventofcode.com/2022/day/11

Solution by Eric Colton
"""

import re
import heapq
from typing import List, Tuple
from collections import deque
from functools import reduce

class MonkeyRouter:
    def __init__(self):
        self.lookup = {}
        self._common_divisor = None

    def add(self, id: int, monkey: object):
        self.lookup[id] = monkey
    
    def route(self, id, item):
        self.lookup[id].give(item)
    
    def common_divisor(self) -> int:
        if self._common_divisor is None:
            self._common_divisor = reduce(lambda a, b: a * b, map(lambda x: x.test, self.lookup.values()), 1)
        return self._common_divisor

class Monkey:
    def __init__(self, id: int, starting_items, op, test, dest_true, dest_false):
        self.id = id
        self.items = deque(starting_items)
        self.op = op
        self.test = test
        self.dest_true = dest_true
        self.dest_false = dest_false
        self.inspected_count = 0

    def give(self, item: int):
        self.items.append(item)

    def exec(self, router: MonkeyRouter, reduce: bool):
        while len(self.items) > 0:
            old = self.items.popleft()
            self.inspected_count += 1
            new = eval(self.op)
            if reduce:
                new //= 3
            new %= router.common_divisor()
            if new % self.test == 0:
                router.route(self.dest_true, new)
            else:
                router.route(self.dest_false, new)

    def __str__(self):
        return (f"Starting items: {self.items}\n"
        + f"Operation: {self.op}\n"
        + f"Test: {self.test}\n"
        + f"If true: {self.dest_true}\n"
        + f"If false: {self.dest_false}\n")

def parse_item(lines: List[str]) -> Monkey:

    match_id = re.match(r'Monkey (\d+):', lines[0].rstrip())
    if match_id:
        id = int(match_id.group(1))
    else:
        raise Exception("Unrecognized monkey identifier")

    match_start = re.match(r'\s*Starting items: ([\d,\s]+)', lines[1].rstrip())
    if match_start:
        starting_items = list(map(lambda x: int(x), match_start.group(1).split(", ")))
    else:
        raise Exception("Unrecognized starting items")

    match_op = re.match(r'\s*Operation: new = ([\w,\s\+\*\d]+)', lines[2].rstrip())
    if match_op:
        op = match_op.group(1)
    else:
        raise Exception("Unrecognized operation")

    match_test = re.match(r'\s*Test: divisible by (\d+)', lines[3].rstrip())
    if match_test:
        test = int(match_test.group(1))
    else:
        raise Exception("Unrecognized test")

    match_if_true = re.match(r'\s*If true: throw to monkey (\d+)', lines[4].rstrip())
    if match_if_true:
        dest_true = int(match_if_true.group(1))
    else:
        raise Exception("Unrecognized if true condition")

    match_if_false = re.match(r'\s*If false: throw to monkey (\d+)', lines[5].rstrip())
    if match_if_false:
        dest_false = int(match_if_false.group(1))
    else:
        raise Exception("Unrecognized if false condition")

    return Monkey(id, starting_items, op, test, dest_true, dest_false)

def parse_input_data(raw_lines: List[str]) -> Tuple[List[Monkey], MonkeyRouter]:
    line_index = 0
    data = []
    router = MonkeyRouter()
    while line_index < len(raw_lines):
        monkey = parse_item(raw_lines[line_index:line_index+6])
        data.append(monkey)
        router.add(monkey.id, monkey)
        line_index += 7
    return data, router

def exec_rounds(data, router, reduce, count):
    for i in range(count):
        for monkey in data:
            monkey.exec(router, reduce)

def find_product_two_most_active(data: List[Monkey]) -> int:
    heap = list(map(lambda x: -x.inspected_count, data))
    heapq.heapify(heap)
    return heapq.heappop(heap) * heapq.heappop(heap)


if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data, router = parse_input_data(raw_input)
        exec_rounds(data, router, True, 20)
        part_1 = find_product_two_most_active(data)
        assert part_1 == 50172
        print(f"The solution to Part 1 is {part_1}")

        data, router = parse_input_data(raw_input)
        exec_rounds(data, router, False, 10000)
        part_2 = find_product_two_most_active(data)
        print(f"The solution to Part 2 is {part_2}")
        assert part_2 == 11614682178
