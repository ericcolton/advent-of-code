#!/usr/bin/env python3

import re
from aoc_2022_11 import parse_input_data, find_product_two_most_active, exec_rounds

TEST_INPUT = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n")

def test_monkey_business_20_rounds():
    data, router = parse_input_data(TEST_INPUT)
    exec_rounds(data, router, True, 20)
    product = find_product_two_most_active(data)
    assert product == 10605

def test_monkey_business_10000_rounds():
    data, router = parse_input_data(TEST_INPUT)
    exec_rounds(data, router, False, 10000)
    product = find_product_two_most_active(data)
    assert find_product_two_most_active(data) == 2713310158

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
