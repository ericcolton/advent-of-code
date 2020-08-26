#!/usr/bin/env python3

"""
Day 11: Space Police

https://adventofcode.com/2019/day/11
"""

from enum import IntEnum
from collections import defaultdict
from intcode import IntcodeComputer

class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Rotation(IntEnum):
    LEFT = 0
    RIGHT = 1

class PaintingRobot:

    def __init__(self, program: [int], input: [int] = []):
        self.computer = IntcodeComputer(program, input)
        self.reset()

    def reset(self):
        self.direction = Direction.NORTH
        self.location = 0, 0
        self.seen_locations = set()
        self.painted_state = defaultdict(int)
        self.computer.reset()

    def run(self, program_input: [int] = []):
        self.computer.input = program_input
        while True:
            if self.computer.run_program(interrupting=True):
                break
            self.painted_state[self.location] = self.computer.output.pop()
            if self.computer.run_program(interrupting=True):
                break
            self.rotate_and_move(Rotation(self.computer.output.pop()))
            self.computer.input = [self.painted_state[self.location]]

    def rotate_and_move(self, rotate: Rotation):
        self.seen_locations.add(self.location)

        if rotate == Rotation.LEFT:
            self.direction -= 1
        elif rotate == Rotation.RIGHT:
            self.direction += 1
        else:
            raise Exception("Unexpected rotation: {rotate}")
        self.direction %= 4

        if self.direction == Direction.NORTH:
            self.location = self.location[0], self.location[1] + 1
        elif self.direction == Direction.EAST:
            self.location = self.location[0] + 1, self.location[1]
        elif self.direction == Direction.SOUTH:
            self.location = self.location[0], self.location[1] - 1
        elif self.direction == Direction.WEST:
            self.location = self.location[0] - 1, self.location[1]
        else:
            raise Exception(f"Unexpected direction: {self.direction}")

def render_image(input: defaultdict(int)):
    white_tiles = list(filter(lambda x: input[x] == 1, input.keys()))
    min_x, min_y = min([i[0] for i in white_tiles]), min([i[1] for i in white_tiles])
    max_x, max_y = max([i[0] for i in white_tiles]), max([i[1] for i in white_tiles])
    rows = []
    for y in range(max_y, min_y - 1, -1):
        row = ''
        for x in range(min_x, max_x + 1):
            row += '#' if (x, y) in white_tiles else ' '
        rows.append(row)
    return rows

def parse_input_data(input: str) -> list:
    return [int(i) for i in input.rstrip().split(',')]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        input = parse_input_data(file.read())

    robot = PaintingRobot(input)
    robot.run([0])
    part_1 = len(robot.seen_locations)
    print(f"Solution to part 1: {part_1}")
    assert part_1 == 2441

    robot.reset()
    robot.run([1])
    part_2 = render_image(robot.painted_state)
    print("Solution to part 2:")
    [print(i) for i in part_2]
    assert part_2 == [
    '###  #### ###  #### ###  ###  #  #  ## ',
    '#  #    # #  # #    #  # #  # # #  #  #',
    '#  #   #  #  # ###  #  # #  # ##   #   ',
    '###   #   ###  #    ###  ###  # #  #   ',
    '#    #    # #  #    #    # #  # #  #  #',
    '#    #### #  # #    #    #  # #  #  ## ']
