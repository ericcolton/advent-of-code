#!/usr/bin/env python3

import re
from aoc_2022_08 import parse_input_data, find_visible
TEST_INPUT = """30373
25512
65332
33549
35390""".split("\n")

def test_find_num_visible_trees():
    data = parse_input_data(TEST_INPUT)
    visible = find_visible(data)
    print(visible)



# def test_find_best_deletion_candidate_size():
#     data = parse_input_data(TEST_INPUT)
#     total_size, dir_sizes = find_dir_sizes(data)
#     best = find_best_deletion_candidate_size(total_size, dir_sizes)
#     assert best == 24933642

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
