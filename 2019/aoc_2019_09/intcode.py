#!/usr/bin/env python3

import re
import time
import enum
from collections import defaultdict

INSTR_ADD = 1
INSTR_MULT = 2
INSTR_WRITE = 3
INSTR_READ = 4
INSTR_JUMP_IF_TRUE = 5
INSTR_JUMP_IF_FALSE = 6
INSTR_LESS_THAN = 7
INSTR_EQUALS = 8
INSTR_SET_BASE = 9
INSTR_END = 99

INSTR_DESC = {
    INSTR_WRITE: "WRITE",
    INSTR_READ: "READ",
    INSTR_JUMP_IF_TRUE: "J_TRUE",
    INSTR_JUMP_IF_FALSE: "J_FALSE",
    INSTR_LESS_THAN: "LESS",
    INSTR_EQUALS: "EQUAL",
    INSTR_SET_BASE: "BASE",
    INSTR_END: "END"
}

class LocationMode(enum.IntEnum):
    POINTER = 0
    IMMEDIATE = 1
    RELATIVE = 2

class IntcodeComputer:

    def __init__(self, raw_program : [int], input : [int], logging=False, slow_mode=False):
        self.program_start_state = defaultdict(int)
        for i in range(len(raw_program)):
            self.program_start_state[i] = raw_program[i]
        self.input = input
        self.logging = logging
        self.slow_mode = slow_mode
        self.halted = False
        self.reset()

    def reset(self):
        self.program = self.program_start_state.copy()
        self.instr_ptr = 0
        self.mem_rel_base = 0
        self.interrupt_flag = False
        self.halted = False
        self.output = []

    def run_program(self, interrupting=False) -> bool:
        """Return true if program encounted an end instruction (otherwise false)"""
        while self.still_running():
            self.exec_instr()
            if interrupting and self.interrupt_flag:
                self.interrupt_flag = False
                return False
            if self.slow_mode:
                time.sleep(0.5)
        return True

    def exec_instr(self):
        (mode_1, mode_2, mode_3, op) = self.parse_current_instr()

        # Handle length=1 instructions
        if op == INSTR_END:
            self.log_instr(1, "HALT")
            self.halted = True
            return

        # Handle length=2 instructions
        if op == INSTR_WRITE or op == INSTR_READ or op == INSTR_SET_BASE:
            if op == INSTR_WRITE:
                location, location_desc = self.get_location(1, mode_1)
                self.log_instr(2, f"input {self.input[0]} to {location_desc}{location}")
                self.program[location] = self.input[0]
                del self.input[0]
            elif op == INSTR_READ:
                value, desc = self.get_value(1, mode_1)
                self.log_instr(2, f"output {desc}")
                self.output.append(value)
                self.interrupt_flag = True
            elif op == INSTR_SET_BASE:
                value, desc = self.get_value(1, mode_1)
                self.mem_rel_base += value
                self.log_instr(2, f"offset mem base by {desc} to {self.mem_rel_base}")
            self.instr_ptr += 2
            return

        # Handle length=3 instructions
        if op == INSTR_JUMP_IF_TRUE or op == INSTR_JUMP_IF_FALSE:
            test_value, tv_desc = self.get_value(1, mode_1)
            if (test_value == 0) ^ (op == INSTR_JUMP_IF_TRUE):
                dest, dest_desc = self.get_value(2, mode_2)
                self.log_instr(3, f"testing {tv_desc} passed, goto {dest_desc}")
                self.instr_ptr = dest
            else:
                self.log_instr(3, f"testing {tv_desc} failed")
                self.instr_ptr += 3
            return

        # Handle length=4 instructions
        if op == INSTR_ADD or op == INSTR_MULT or op == INSTR_LESS_THAN or op == INSTR_EQUALS:
            input_1, input_1_desc = self.get_value(1, mode_1)
            input_2, input_2_desc = self.get_value(2, mode_2)
            dest, dest_desc = self.get_location(3, mode_3)
            punc = "="
            if op == INSTR_ADD:
                result = input_1 + input_2
                op_desc = '+'
            elif op == INSTR_MULT:
                result = input_1 * input_2
                op_desc = '*'
            elif op == INSTR_LESS_THAN:
                result = (1 if input_1 < input_2 else 0)
                op_desc = '<'
                punc = ","
            else: # op == INSTR_EQUALS:
                result = (1 if input_1 == input_2 else 0)
                op_desc = '=='
                punc = ","
            self.log_instr(4, f"{input_1_desc} {op_desc} {input_2_desc} {punc} {result} -> {dest_desc}")
            self.program[dest] = result
            self.instr_ptr += 4
            return

        raise Exception(f"invalid op code '{op}'")

    def get_value(self, offset: int, mode: LocationMode):
        if mode == LocationMode.IMMEDIATE:
            value = self.program[self.instr_ptr + offset]
            return value, f"{value}"
        elif mode == LocationMode.RELATIVE or mode == LocationMode.POINTER:
            location, desc = self.get_location(offset, mode)
            pointed_value = self.program[location]
            return pointed_value, f"{desc}{pointed_value}"
        else:
            raise Exception(f"unexpected operand type {mode}")

    def get_location(self, offset: int, mode: LocationMode):
        location_value = self.program[self.instr_ptr + offset]
        if mode == LocationMode.POINTER:
            return location_value, f"[{location_value}]"
        elif mode == LocationMode.IMMEDIATE:
            raise Exception("Cannot use 'Immediate' mode for finding a location")
        elif mode == LocationMode.RELATIVE:
            location_value_expr = f"+{location_value}" if location_value >= 0 else f"{location_value}"
            return self.mem_rel_base + location_value, f"R[{self.mem_rel_base}{location_value_expr}]"
        else:
            raise Exception(f"unexpected operand type {mode}")

    def still_running(self):
        if self.instr_ptr >= len(self.program):
            raise Exception("unexpected EOF")
        return not self.halted

    def parse_current_instr(self):
        op_code = self.program[self.instr_ptr]
        # INSTR_END is the only two-digit op-code
        if op_code == INSTR_END:
            return 1, 1, 1, INSTR_END
        match = re.search(r'^(\d)(\d)(\d)\d(\d)$', str(op_code).zfill(5))
        if not match:
            raise Exception("Illegal instruction: '{op_code}'")
        rv = (LocationMode(int(match.group(3))), LocationMode(int(match.group(2))), LocationMode(int(match.group(1))), int(match.group(4)))
        return rv

    def log_instr(self, length, log_str=""):
        if self.logging:
            raw_desc = ','.join([str(self.program[i]) for i in range(self.instr_ptr, self.instr_ptr + length)])
            raw_desc += (30 - len(raw_desc)) * ' '
            op = self.parse_current_instr()[2]
            op_desc = INSTR_DESC[op] if op in INSTR_DESC else ""
            print(f"[{self.instr_ptr}]\t{raw_desc}\t{op_desc}\t{log_str}")
