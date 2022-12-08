#!/usr/bin/env python3

import re
from aoc_2022_07 import parse_input_data, find_dir_sizes, find_sum_small_dir_sizes, find_best_deletion_candidate_size

TEST_INPUT = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")

def test_find_dir_size():
    data = parse_input_data(TEST_INPUT)
    total_size, dir_sizes = find_dir_sizes(data)
    total = find_sum_small_dir_sizes(dir_sizes)
    assert total == 95437

def test_find_best_deletion_candidate_size():
    data = parse_input_data(TEST_INPUT)
    total_size, dir_sizes = find_dir_sizes(data)
    best = find_best_deletion_candidate_size(total_size, dir_sizes)
    assert best == 24933642

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
