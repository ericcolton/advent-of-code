#!/usr/bin/env python3

"""
Advent of Code 2019 Day 6: Universal Orbit Map

https://adventofcode.com/2019/day/6
"""

class Node:

    def __init__(self, name):
        self.__name = name
        self.__known_distance_to_root = -1
        self.parent = None

    def distance_to_root(self):
        if self.__known_distance_to_root < 0:
            self.__known_distance_to_root = self.parent.distance_to_root() + 1 if self.parent else 0
        return self.__known_distance_to_root

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

class OrbitMap:

    def __init__(self, input):
        self.__node_lookup = {}
        for i in input:
            self.__process_entry(i)

    def count_total_orbits(self):
        return sum([n.distance_to_root() for n in self.__node_lookup.values()])

    def calc_distance_between(self, name_1, name_2):
        path_1 = self.__path_to_root(name_1)
        path_2 = self.__path_to_root(name_2)
        return len(path_1 ^ path_2) - 2

    def __path_to_root(self, name):
        node = self.__get_node(name)
        if not node.parent:
            return set()
        path = set()
        while node:
            path.add(node)
            node = node.parent
        return path

    def __process_entry(self, entry):
        name_1, name_2 = entry
        node_1 = self.__get_node(name_1)
        node_2 = self.__get_node(name_2)
        node_2.parent = node_1

    def __get_node(self, name):
        if name in self.__node_lookup:
            return self.__node_lookup[name]
        else:
            node = Node(name)
            self.__node_lookup[name] = node
            return node

def parse_input_data(data: str):
    return [line.rstrip().split(')') for line in data.rstrip().split("\n")]

if __name__ == '__main__':
    input_filepath = __file__.rstrip('.py') + '_input.txt'
    with open(input_filepath, 'r') as file:
        input = parse_input_data(file.read())
    om = OrbitMap(input)
    part_1 = om.count_total_orbits()
    print(f"Part 1 solution is {part_1}")
    assert part_1 == 315757
    part_2 = om.calc_distance_between('YOU', 'SAN')
    print(f"Part 2 solution is {part_2}")
    assert part_2 == 481
