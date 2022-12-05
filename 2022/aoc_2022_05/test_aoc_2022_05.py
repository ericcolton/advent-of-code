#!/usr/bin/env python3

import re
from aoc_2022_05 import parse_input_data, run_instrs, top_of_stacks

TEST_INPUT = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")

def test_move_individually():
    state, instrs = parse_input_data(TEST_INPUT)
    run_instrs(state, instrs, False)
    assert top_of_stacks(state) == 'CMZ'

def test_in_bulk():
    state, instrs = parse_input_data(TEST_INPUT)
    run_instrs(state, instrs, True)
    assert top_of_stacks(state) == 'MCD'

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
