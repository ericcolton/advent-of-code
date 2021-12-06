#!/usr/bin/env python3

import re
from aoc_2021_06 import parse_input_data, iterate_days, consolidate_by_age

TEST_INPUT = "3,4,3,1,2".split("\n")

def test_iterate_80_days():
    ages = parse_input_data(TEST_INPUT)
    count_by_age = consolidate_by_age(ages)
    iterate_days(count_by_age, 80)
    total_count = sum(count_by_age.values())
    assert total_count == 5934

def test_iterate_256_days():
    ages = parse_input_data(TEST_INPUT)
    count_by_age = consolidate_by_age(ages)
    iterate_days(count_by_age, 256)
    total_count = sum(count_by_age.values())
    assert total_count == 26984457539

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
