#!/usr/bin/env python3

import re
from intcode import IntcodeComputer
from aoc_2019_09 import parse_input_data

LOGGING_ON = False

def test_produce_copy_of_self():
    test_data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    input = parse_input_data(test_data)
    ic = IntcodeComputer(input, [], logging=LOGGING_ON)
    ic.run_program()
    assert ic.output == input

def test_16_digit_output():
    test_data = "1102,34915192,34915192,7,4,7,99,0"
    input = parse_input_data(test_data)
    ic = IntcodeComputer(input, [], logging=LOGGING_ON)
    ic.run_program()
    assert ic.output[0] == 1219070632396864

def test_middle_number_output():
    test_data = "104,1125899906842624,99"
    input = parse_input_data(test_data)
    ic = IntcodeComputer(input, [], logging=LOGGING_ON)
    ic.run_program()
    assert ic.output[0] == 1125899906842624

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running: {symbol}()")
            globals()[symbol]()
    print("Done")
