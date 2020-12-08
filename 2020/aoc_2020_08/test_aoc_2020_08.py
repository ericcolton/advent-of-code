#!/usr/bin/env python3

import re
from aoc_2020_08 import run_program_single_execution, mutate_jmp_nops_in_program_until_completion, parse_input_data

TEST_INPUT = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n')

def test_case_part_1():
    program = parse_input_data(TEST_INPUT)
    accumulator = run_program_single_execution(program).accumulator_value
    assert accumulator == 5

def test_case_part_2():
    program = parse_input_data(TEST_INPUT)
    accumulator = mutate_jmp_nops_in_program_until_completion(program)
    assert accumulator == 8


if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")