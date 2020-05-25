#!/usr/bin/env python3

"""
Advent of Code 2019 Day 5: Day 5: Sunny with a Chance of Asteroids

https://adventofcode.com/2019/day/5
"""

import re
from aoc_helpers import get_input_filepath

INSTR_ADD = 1
INSTR_MULT = 2
INSTR_WRITE = 3
INSTR_READ = 4
INSTR_JUMP_IF_TRUE = 5
INSTR_JUMP_IF_FALSE = 6
INSTR_LESS_THAN = 7
INSTR_EQUALS = 8
INSTR_END = 99

class ComputerProcessor:

    def __init__(self, program):
        self.__program_start_state = program  

    def run_program(self):
      self.__program = self.__program_start_state.copy()
      self.__instr_ptr = 0
      self.output = []
      while self.__still_running():
        self.__exec_instr()

    def __exec_instr(self):
        (is_ptr_1, is_ptr_2, op) = self.__parse_current_instr()

        if op == INSTR_WRITE or op == INSTR_READ:
            if op == INSTR_WRITE:
                # immediate mode wouldn't make any sense here
                assert is_ptr_1
                location = self.__get_value(1)
                self.__program[location] = self.input
            elif op == INSTR_READ:
                self.output.append(self.__get_value(1, is_ptr_1))
            self.__instr_ptr += 2
            return

        if op == INSTR_JUMP_IF_TRUE or op == INSTR_JUMP_IF_FALSE:
            test_value = self.__get_value(1, is_ptr_1)
            if (test_value == 0) ^ (op == INSTR_JUMP_IF_TRUE):
                self.__instr_ptr = self.__get_value(2, is_ptr_2)
            else:
                self.__instr_ptr += 3
            return
        
        if op == INSTR_ADD or op == INSTR_MULT or op == INSTR_LESS_THAN or op == INSTR_EQUALS:
            input_1 = self.__get_value(1, is_ptr_1)
            input_2 = self.__get_value(2, is_ptr_2)
            dest = self.__get_value(3)
            if op == INSTR_ADD:
                result = input_1 + input_2
            elif op == INSTR_MULT:
                result = input_1 * input_2
            elif op == INSTR_LESS_THAN:
                result = (1 if input_1 < input_2 else 0)
            else: # op == INSTR_EQUALS:
                result = (1 if input_1 == input_2 else 0)
            self.__program[dest] = result
            self.__instr_ptr += 4
            return
        
        raise f"invalid op code '{op}'"

    def __get_value(self, offset, is_ptr=False):
        value = self.__program[self.__instr_ptr + offset]
        return self.__program[value] if is_ptr else value

    def __still_running(self):
        if self.__instr_ptr >= len(self.__program):
            raise "unexpected EOF"
        return self.__program[self.__instr_ptr] != INSTR_END

    def __parse_current_instr(self):
        op_code_str = str(self.__program[self.__instr_ptr]).zfill(4)
        match = re.search(r'(\d)(\d)\d(\d)', op_code_str)
        if not match:
            raise "Illegal instruction: '{op_code}'"
        return (not int(match.group(2)), not int(match.group(1)), int(match.group(3)))

def parse_input_line(line):
    return [int(i) for i in line.split(',')]

def parse_input_file(input_filepath):
    with open(input_filepath, 'r') as file:
        return parse_input_line(file.readline().rstrip())

if __name__ == "__main__":
    file_path = get_input_filepath(__file__)
    program = parse_input_file(file_path)
    cp = ComputerProcessor(program)
    cp.input = 1
    cp.run_program()
    solution_1 = cp.output[-1]
    cp.input = 5
    cp.run_program()
    solution_2 = cp.output[-1]
    print(f"Solution to Part 1 is: {solution_1}")
    print(f"Solution to Part 2 is: {solution_2}")
    assert solution_1 == 7566643
    assert solution_2 == 9265694
