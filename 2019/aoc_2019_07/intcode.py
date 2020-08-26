#!/usr/bin/env python3

import re

INSTR_ADD = 1
INSTR_MULT = 2
INSTR_WRITE = 3
INSTR_READ = 4
INSTR_JUMP_IF_TRUE = 5
INSTR_JUMP_IF_FALSE = 6
INSTR_LESS_THAN = 7
INSTR_EQUALS = 8
INSTR_END = 99

INSTR_DESC = {
    INSTR_WRITE: "WRITE",
    INSTR_READ: "READ",
    INSTR_JUMP_IF_TRUE: "JUMP_T",
    INSTR_JUMP_IF_FALSE: "JUMP_F",
    INSTR_LESS_THAN: "LESS",
    INSTR_EQUALS: "EQUAL",
    INSTR_END: "END"
}

class IntcodeComputer:

    def __init__(self, program : [int], input : [int], logging=False):
        self.program_start_state = program
        self.input = input
        self.logging = logging
        self.halted = False
        self.reset()

    def reset(self):
      self.program = self.program_start_state.copy()
      self.instr_ptr = 0
      self.interrupt_flag = False
      self.halted = False
      self.output = []

    def run_program(self) -> bool:
        """Return true if program encounted an end instruction (otherwise false)"""
        while self.still_running():
            self.exec_instr()
            if self.interrupt_flag:
                self.interrupt_flag = False
                return False
        return True

    def exec_instr(self):
        (is_ptr_1, is_ptr_2, op) = self.parse_current_instr()

        if op == INSTR_WRITE or op == INSTR_READ:
            if op == INSTR_WRITE:
                # immediate mode wouldn't make any sense here
                assert is_ptr_1
                location, _ = self.get_value(1)
                self.log_instr(f"input {self.input[0]} to {location}")
                self.program[location] = self.input[0]
                del self.input[0]
                
            elif op == INSTR_READ:
                value, desc = self.get_value(1, is_ptr_1)
                self.log_instr(f"output {desc}")
                self.output.append(value)
                self.interrupt_flag = True
            self.instr_ptr += 2
            return

        if op == INSTR_JUMP_IF_TRUE or op == INSTR_JUMP_IF_FALSE:
            test_value, tv_desc = self.get_value(1, is_ptr_1)
            if (test_value == 0) ^ (op == INSTR_JUMP_IF_TRUE):
                dest, dest_desc = self.get_value(2, is_ptr_2)
                self.log_instr(f"testing [{self.instr_ptr+1}]{tv_desc} passed, goto [{self.instr_ptr+2}]{dest_desc}")
                self.instr_ptr = dest
            else:
                self.log_instr(f"testing {tv_desc} failed")
                self.instr_ptr += 3
            return

        if op == INSTR_ADD or op == INSTR_MULT or op == INSTR_LESS_THAN or op == INSTR_EQUALS:
            input_1, input_1_desc = self.get_value(1, is_ptr_1)
            input_2, input_2_desc = self.get_value(2, is_ptr_2)
            dest, _ = self.get_value(3)
            if op == INSTR_ADD:
                result = input_1 + input_2
                op_desc = '+'
            elif op == INSTR_MULT:
                result = input_1 * input_2
                op_desc = '*'
            elif op == INSTR_LESS_THAN:
                result = (1 if input_1 < input_2 else 0)
                op_desc = '<'
            else: # op == INSTR_EQUALS:
                result = (1 if input_1 == input_2 else 0)
                op_desc = '=='
            self.log_instr(f"{input_1_desc} {op_desc} {input_2_desc} = {result} -> {dest}")
            self.program[dest] = result
            self.instr_ptr += 4
            return
        
        if op == INSTR_END:
            self.log_instr()
            self.halted = True
            return

        raise f"invalid op code '{op}'"

    def get_value(self, offset, is_ptr=False):
        value = self.program[self.instr_ptr + offset]
        if is_ptr:
            pointed_value = self.program[value]
            return pointed_value, f"[{value}]{pointed_value}"
        else:
            return value, f"{value}"

    def still_running(self):
        if self.instr_ptr >= len(self.program):
            raise "unexpected EOF"
        return not self.halted

    def parse_current_instr(self):
        op_code = self.program[self.instr_ptr]
        # INSTR_END is the only two-digit op-code
        if op_code == INSTR_END:
            return 1, 1, INSTR_END
        match = re.search(r'(\d)(\d)\d(\d)', str(op_code).zfill(4))
        if not match:
            raise "Illegal instruction: '{op_code}'"
        return (not int(match.group(2)), not int(match.group(1)), int(match.group(3)))

    def log_instr(self, log_str=""):
        if self.logging:
            op = self.parse_current_instr()[2]
            op_desc = INSTR_DESC[op] if op in INSTR_DESC else ""
            print(f"[{self.instr_ptr}]\t{op_desc}\t{log_str}")
