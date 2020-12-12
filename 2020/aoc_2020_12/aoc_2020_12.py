#!/usr/bin/env python3

"""
Advent of Code 2020 Day 12: Rain Risk

https://adventofcode.com/2020/day/12

Solution by Eric Colton
"""

import re
from collections import namedtuple

Instruction = namedtuple('Instruction', ['type', 'quantity'])

class Ferry:
    
    def __init__(self, vector_x:int, vector_y:int, waypoint_mode: bool = False):
        self.vector_x = vector_x
        self.vector_y = vector_y
        self.location_x = 0
        self.location_y = 0
        self.waypoint_mode = waypoint_mode

    def execute_instructions(self, instructions:list):
        for i in instructions:
            self.execute(i)
    
    def execute(self, instruction:Instruction):
        if instruction.type == 'F':
            self.location_x += self.vector_x * instruction.quantity
            self.location_y += self.vector_y * instruction.quantity
        elif instruction.type == 'R':
            for _ in range(instruction.quantity // 90):
                self.turn_right()
        elif instruction.type == 'L':
            for _ in range(instruction.quantity // 90):
                self.turn_left()
        elif self.handle_location_update(instruction):
            return
        else:
            raise Exception("Unknown instruction type '{}'".format(instruction.type))
    
    def handle_location_update(self, instruction) -> bool:
        quantity = instruction.quantity
        if instruction.type == 'N':
            if self.waypoint_mode:
                self.vector_y += quantity                
            else:
                self.location_y += quantity
        elif instruction.type == 'S':
            if self.waypoint_mode:
                self.vector_y -= quantity
            else:
                self.location_y -= quantity
        elif instruction.type == 'E':
            if self.waypoint_mode:
                self.vector_x += quantity
            else:
                self.location_x += quantity
        elif instruction.type == 'W':
            if self.waypoint_mode:
                self.vector_x -= quantity
            else:            
                self.location_x -= quantity
        else:
            return False
        return True

    def turn_right(self):
        self.vector_x, self.vector_y = self.vector_y, -1 * self.vector_x
    
    def turn_left(self):
        self.vector_x, self.vector_y = -1 * self.vector_y, self.vector_x

    def manhattan_distance(self):
        return abs(self.location_x) + abs(self.location_y)

def parse_input_file(file):
    data = []
    for line in file:
        line = line.rstrip()
        match = re.fullmatch(r'([NSEWLRF])(\d+)', line)
        if match:
            data.append(Instruction(match.group(1), int(match.group(2))))
        else:
            raise Exception("Unable to parse instruction: '{}'".format(line))
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input_file(file)
    ferry_1 = Ferry(1, 0)
    ferry_1.execute_instructions(data)
    part_1 = ferry_1.manhattan_distance()
    assert part_1 == 858
    print("Solution to Part 1 is {}".format(part_1))

    ferry_2 = Ferry(10, 1, True)
    ferry_2.execute_instructions(data)
    part_2 = ferry_2.manhattan_distance()
    assert part_2 == 39140
    print("Solution to Part 2 is {}".format(part_2))

