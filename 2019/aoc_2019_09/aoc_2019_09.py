#!/usr/bin/env python3

"""
Advent of Code 2019 Day 9: Sensor Boost

https://adventofcode.com/2019/day/9
"""

from intcode import IntcodeComputer

def parse_input_data(input: str) -> [int]:
    return [int(i) for i in input.rstrip().split(',')]

if __name__ == '__main__':
    input_filepath = __file__.rstrip('.py') + '_input.txt'
    with open(input_filepath, 'r') as file:
        input = parse_input_data(file.read())
    ic = IntcodeComputer(input, [1], logging=False)
    ic.run_program()
    part_1 = ic.output.pop(0)
    print(f"Solution to part 1 is: {part_1}")
    assert part_1 == 2682107844

    ic = IntcodeComputer(input, [2], logging=False)
    ic.run_program()
    part_2 = ic.output.pop(0)
    print(f"Solution to part 2 is: {part_2}")
    assert part_2 == 34738