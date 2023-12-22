#!/usr/bin/env python3

import re
from aoc_2023_12 import parse_input_data, sum_all_arrangements, expand_data

TEST_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")

def test_sum_all_arrangements():
    data = parse_input_data(TEST_INPUT)
    rv = sum_all_arrangements(data)
    assert(rv == 21)

def test_sum_all_arrangements_expanded():
    data = parse_input_data(TEST_INPUT)
    expanded_data = expand_data(data)
    rv = sum_all_arrangements(expanded_data)
    assert(rv == 525152)

if __name__ == '__main__':
   for symbol in dir():
       if re.match('^test_', symbol):
           print(f"running {symbol}()")
           globals()[symbol]()
   print("Done")
