#!/usr/bin/env python3

"""
Advent of Code 2020 Day 14: Docking Data

https://adventofcode.com/2020/day/14

Solution by Eric Colton
"""

import re
from collections import namedtuple
from collections import defaultdict

MaskCommand = namedtuple('MaskCommand', ['mask'])
MemCommand = namedtuple('MemCommand', ['location', 'value'])

INSTR_SIZE = 36

class Program:
    def __init__(self, commands: list):
        self.commands = commands

    def run_with_masking_values(self):
        self.memory = defaultdict(int)
        self.mask = 'X' * INSTR_SIZE
        for command in self.commands:
            if type(command) is MaskCommand:
                self.mask = command.mask
            elif type(command) is MemCommand:
                command_value = command.value
                output_value = 0
                for index in range(INSTR_SIZE):
                    index_value = 2 ** (INSTR_SIZE - index - 1)
                    bit_set = False
                    if command_value >= index_value:
                        command_value -= index_value
                        bit_set = True
                    if self.mask[index] == '1':
                        bit_set = True
                    elif self.mask[index] == '0':
                        bit_set = False
                    if bit_set:
                        output_value += index_value
                self.memory[command.location] = output_value
            else:
                raise Exception("Unknown commands: '{}'".format(command))

    def run_with_masking_addresses(self):
        self.memory = defaultdict(int)
        self.mask = 'X' * INSTR_SIZE
        for command in self.commands:
            if type(command) is MaskCommand:
                self.mask = command.mask
            elif type(command) is MemCommand:
                address_value = command.location
                output_addresses = [0]
                for index in range(INSTR_SIZE):
                    index_value = 2 ** (INSTR_SIZE - index - 1)
                    bit_set = False
                    if address_value >= index_value:
                        address_value -= index_value
                        bit_set = True
                    if self.mask[index] == 'X':
                        for addr in output_addresses.copy():
                            output_addresses.append(addr + index_value)
                    elif self.mask[index] == '1' or bit_set:
                        for i in range(len(output_addresses)):
                            output_addresses[i] += index_value
                for addr in output_addresses:
                    self.memory[addr] = command.value
            else:
                raise Exception("Unknown commands: '{}'".format(command))

    def sum_all_memory(self):
        return sum(self.memory.values())

def parse_input(input):
    data = []
    for line in input:
        line = line.rstrip()
        mask_match = re.match(r'mask = ([01X]+)', line)
        if mask_match:
            data.append(MaskCommand(mask_match.group(1)))
            continue
        mem_match = re.match(r'mem\[(\d+)\] = (\d+)', line)
        if mem_match:
            data.append(MemCommand(int(mem_match.group(1)), int(mem_match.group(2))))
            continue
        raise Exception("Cannot recognize command '{}'".format(line))
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input(file)
        program = Program(data)
        program.run_with_masking_values()
        part_1 = program.sum_all_memory()
        assert part_1 == 9615006043476
        print("Solution to Part 1 is {}".format(part_1))

        program.run_with_masking_addresses()
        part_2 = program.sum_all_memory()
        assert part_2 == 4275496544925
        print("Solution to Part 2 is {}".format(part_2))
