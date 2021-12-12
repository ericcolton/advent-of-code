#!/usr/bin/env python3

import re
from aoc_2021_12 import parse_input_data, build_graph, find_all_paths

TEST_INPUT_1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

TEST_INPUT_2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split("\n")

TEST_INPUT_3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".split("\n")

def test_find_all_paths_1():
    edges = parse_input_data(TEST_INPUT_1)
    graph, big_nodes = build_graph(edges)
    paths_count = find_all_paths(graph, big_nodes)
    assert paths_count == 10

def test_find_all_paths_1_with_double_visit():
    edges = parse_input_data(TEST_INPUT_1)
    graph, big_nodes = build_graph(edges)
    paths_count = find_all_paths(graph, big_nodes, True)
    assert paths_count == 36

def test_find_all_paths_2():
    edges = parse_input_data(TEST_INPUT_2)
    graph, big_nodes = build_graph(edges)
    paths_count = find_all_paths(graph, big_nodes)
    assert paths_count == 19

def test_find_all_paths_3():
    edges = parse_input_data(TEST_INPUT_3)
    graph, big_nodes = build_graph(edges)
    paths_count = find_all_paths(graph, big_nodes)
    assert paths_count == 226

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
