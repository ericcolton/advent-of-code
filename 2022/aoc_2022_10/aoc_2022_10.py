#!/usr/bin/env python3

"""
Advent of Code 2022 Day 10: Cathode-Ray Tube

https://adventofcode.com/2022/day/10

Solution by Eric Colton
"""

import re
from typing import List, Tuple


class Instr:
    def __init__(self, length: int):
        self.length = length
    
    def op(self, param: int) -> int:
        raise Exception("must override base class")

class Noop (Instr):
    def __init__(self):
        super().__init__(1)
    
    def op(self, param: int) -> int:
        return param

class AddX (Instr):
    def __init__(self, val: int):
        super().__init__(2)
        self.val = val
    
    def op(self, param: int) -> int:
        return param + self.val
    
    def __str__(self) -> str:
        return self.__class__.__name__ + " " + str(self.val)

class Pipeline:
    def __init__(self, instrs: List[Instr]):
        self.instrs = instrs
        self.instr_counter = 0
        self.register = 1
        self.state = 0
        self.wait = 0
        self.pending_instr = None
        self.cycle_count = 0
        self.measurement_cycles = set([20, 60, 100, 140, 180, 220])
        self.signal_strength = 0
        self.crt_output = [[' '] * 40 for _ in range(7)]

    def run_x_clock_cycles(self, count: int) -> None:
        for i in range(count):
            self.run_clock_cycle()

    def run_all_clock_cycles(self) -> None:
        while self.run_clock_cycle():
            pass

    def imprint_to_crt(self) -> None:
        y, x = (self.cycle_count) // 40, (self.cycle_count) % 40
        regx = self.register
        hits = set([regx - 1, regx, regx + 1])
        self.crt_output[y][x] = '#' if x in hits else '.'
    
    def print_crt(self) -> None:
        return "\n".join(["".join(row) for row in self.crt_output])
    
    def run_clock_cycle(self) -> None:
        if self.instr_counter >= len(self.instrs):
            return False
        self.exec_cycle()
        self.imprint_to_crt()
        self.cycle_count += 1
        if self.cycle_count in self.measurement_cycles:
            self.signal_strength += self.cycle_count * self.register
        return True

    def exec_cycle(self) -> None:
        if self.wait > 0:
            self.wait -= 1
            return
        if self.pending_instr:
            self.register = self.pending_instr.op(self.register)
            self.pending_instr = None
        instr = self.instrs[self.instr_counter]
        self.instr_counter += 1
        
        if instr.length > 0:
            self.pending_instr = instr
            self.wait = instr.length - 1
        else:
            # noop
            pass


def parse_instr(line: str) -> Instr:
    if line == 'noop':
        return Noop()
    match = re.match(r'addx (\-?\d+)', line)
    if match:
        return AddX(int(match.group(1)))
    else:
        raise Exception("unknown instruction")

def parse_input_data(raw_lines: List[str]) -> List[Tuple[str, int]]:
    return [parse_instr(line.rstrip()) for line in raw_lines]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        instrs = parse_input_data(raw_input)
        pipeline = Pipeline(instrs)
        pipeline.run_all_clock_cycles()
        part_1 = pipeline.signal_strength
        print(f"The solution to Part 1 is {part_1}")        
        assert part_1 == 12640

        part_2 = pipeline.print_crt()
        print(f"The solution to Part 2 is \n{part_2}")

