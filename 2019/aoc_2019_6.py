#!/usr/bin/env python3

class Node:

    def __init__(self, name):
        self.__name = name
        self.__known_distance_to_root = -1
        self.parent = None

    def distance_to_root(self):
        if self.__known_distance_to_root < 0:
            self.__known_distance_to_root = self.parent.distance_to_root() + 1 if self.parent else 1
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

def parse_input(raw_input: str = None) -> list:
    if raw_input:
        input_lines = [i.rstrip() for i in raw_input.split("\n")]
    else:
        with open('aoc_2019_6_input.txt', 'r') as f:
            input_lines = [l.rstrip() for l in f.readlines()]

    return [i.split(')') for i in input_lines]

test_data1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

test_data2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""

if __name__ == '__main__':
    #input = parse_input(test_data1)
    #input = parse_input(test_data2)
    input = parse_input()
    om = OrbitMap(input)
    solution_1 = om.count_total_orbits()
    print(f"Solution to part 1 is {solution_1}")
    assert solution_1 == 317557
    solution_2 = om.calc_distance_between('YOU', 'SAN')
    print(f"Solution to part 2 is {solution_2}")
    assert solution_2 == 481
