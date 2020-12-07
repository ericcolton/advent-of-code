#!/usr/bin/env python3

"""
Advent of Code 2020 Day 7: Handy Haversacks

https://adventofcode.com/2020/day/6

Solution by Eric Colton
"""

import re
from collections import namedtuple

BagEntry = namedtuple('BagEntry', ['name', 'quantity'])
BagContents = namedtuple('BagContents', ['name', 'contents'])

def find_sum_contained(name: str, lookup: dict):
    total = 1
    for bag_contents in lookup[name]:
        total += bag_contents.quantity * find_sum_contained(bag_contents.name, lookup)
    return total

def find_parent_nodes(name: str, lookup: dict):
    nodes = set([name])
    for edge_name in lookup[name]:
        nodes = nodes.union(find_parent_nodes(edge_name, lookup))
    return nodes

def find_sum_parent_nodes(name: str, lookup: dict):
    parents = find_parent_nodes(name, lookup)
    parents.remove(name)
    return len(parents)

def build_parent_lookup(data: list):
    lookup = {}
    for contents_record in data:
        if contents_record.name not in lookup:
            lookup[contents_record.name] = set()
        for edge in contents_record.contents:
            if edge.name not in lookup:
                lookup[edge.name] = set()
            lookup[edge.name].add(contents_record.name)
    return lookup

def build_container_lookup(data: list):
    lookup = {}
    for contents_record in data:
        if contents_record.name not in lookup:
            lookup[contents_record.name] = set()
        for edge in contents_record.contents:
            if edge.name not in lookup:
                lookup[edge.name] = set()
            lookup[contents_record.name].add(edge)
    return lookup

def parse_input_file(file):
    data = []
    for line in file:
        line = line.rstrip()
        match = re.match(r'([\w\s]+?) bags contain ([\w\s,]+)\.', line)
        if match:
            name = match.group(1)
            content_strs = match.group(2).split(', ')
            contents = []
            for entry in content_strs:
                if entry == 'no other bags':
                    continue
                sub_match = re.match(r'(\d+) ([\w\s]+?) bags?', entry)
                if sub_match:
                    contents.append(BagEntry(sub_match.group(2), int(sub_match.group(1))))
                else:
                    raise Exception("Unable to parse entry: '{}'".format(line))
            data.append(BagContents(name, contents))
        else:
            raise Exception("Unable to parse line: '{}'".format(line))
    return data

if __name__ == '__main__':
    input_file_name = __file__.rstrip('.py') + '_input.txt'
    with open(input_file_name, 'r') as file:
        data = parse_input_file(file)
    parent_lookup = build_parent_lookup(data)
    part_1 = find_sum_parent_nodes('shiny gold', parent_lookup)
    assert part_1 == 144
    print("Solution to part 1 is {}".format(part_1))

    container_lookup = build_container_lookup(data)
    part_2 = find_sum_contained('shiny gold', container_lookup) - 1 # remove shiny gold
    assert part_2 == 5956
    print("Solution to part 2 is {}".format(part_2))