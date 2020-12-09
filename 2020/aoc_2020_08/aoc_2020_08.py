#!/usr/bin/env python3

"""
Advent of Code 2020 Day 8: Handheld Halting

https://adventofcode.com/2020/day/8

Solution by Eric Colton
"""

import re
from collections import namedtuple

Instruction = namedtuple('Instruction', ['name', 'operand'])
ReturnStatus = namedtuple('ReturnStatus', ['completed', 'accumulator_value'])

def run_program_single_execution(program: list) -> ReturnStatus:
    accumulator = 0
    current_instr = 0
    seen_instructions = set()
    while current_instr not in seen_instructions:
        if current_instr == len(program):
            return ReturnStatus(True, accumulator)
        elif current_instr >= len(program):
            raise Exception("Invalid instruction index: {}".format(current_instr))

        instr = program[current_instr]
        seen_instructions.add(current_instr)
        if instr.name == 'acc':
            accumulator += instr.operand
        elif instr.name == 'jmp':
            current_instr += instr.operand
            continue
        elif instr.name == 'nop':
            pass
        else:
            raise Exception("Invalid Instruction: {}".format(instr.name))
        current_instr += 1
    return ReturnStatus(False, accumulator)

def mutate_jmp_nops_in_program_until_completion(program: list):
    nops, jmps = [], []
    for i, instr in enumerate(program):
        if instr.name == 'nop':
            nops.append(i)
        elif instr.name == 'jmp':
            jmps.append(i)

    for nop_index in nops:
        mod_program = program.copy()
        operand = program[nop_index].operand
        mod_program[nop_index] = Instruction('jmp', operand)
        return_status = run_program_single_execution(mod_program)
        if return_status.completed:
            return return_status.accumulator_value

    for jmp_index in jmps:
        mod_program = program.copy()
        operand = program[jmp_index].operand
        mod_program[jmp_index] = Instruction('nop', operand)
        return_status = run_program_single_execution(mod_program)
        if return_status.completed:
            return return_status.accumulator_value

    return -1

def parse_input_data(input_data: list):
    data = []
    for line in input_data:
        match = re.match(r'(\w+)\s*([\+\-])(\d+)', line.rstrip())
        if match:
            quantity = int(match.group(3))
            quantity = -1 * quantity if match.group(2) == '-' else quantity
            data.append(Instruction(match.group(1), quantity))
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        input_data = file.readlines()
        program = parse_input_data(input_data)
    part_1 = run_program_single_execution(program).accumulator_value
    assert part_1 == 1331
    print("Solution to Part 1 is {}".format(part_1))

    part_2 = mutate_jmp_nops_in_program_until_completion(program)
    print("Solution to Part 2 is {}".format(part_2))
    