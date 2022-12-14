#!/usr/bin/env python3

import re
from aoc_2022_13 import parse_input_data, find_sum_ordered_indicies, flatten_pairs, append_dividers, sort_packets_and_multiply_divider_placements

TEST_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".split("\n")

def test_identify_ordered_pairs():
        data = parse_input_data(TEST_INPUT)
        summ = find_sum_ordered_indicies(data)
        assert summ == 13

def test_sort_packets():
    data = parse_input_data(TEST_INPUT)
    flat_list = flatten_pairs(data)
    flat_list = append_dividers(flat_list)
    product = sort_packets_and_multiply_divider_placements(flat_list)
    assert product == 140

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
