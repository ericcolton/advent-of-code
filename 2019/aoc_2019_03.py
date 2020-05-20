#!/usr/bin/env python3

"""
Advent of Code Day 3: Crossed Wires

https://adventofcode.com/2019/day/3
"""

from aoc_helpers import get_input_filepath

class InvalidDirectionError(Exception):
    pass

class CircuitChecker():
    
    def record_circuit(self, circuit):
        """Mark this circuit as recorded for use against future comparision"""
        self.__recorded_positions = {}        
        self.__run_circuit(circuit, self.__record_position)

    def compare_circuit(self, circuit):
        """Compare this circuit against the recorded circuit"""
        self.__cross_exists = False
        self.__best_distance_to_origin = -1
        self.__best_wire_length = -1
        self.__run_circuit(circuit, self.__compare_position)
    
    def best_distance_to_origin(self):
        return self.__best_distance_to_origin

    def best_wire_length(self):
        return self.__best_wire_length

    def __run_circuit(self, circuit, op):
        (current_x, current_y, current_length) = (0, 0, 0)
        for instruction in circuit:
            for _ in range(instruction['distance']):
                if instruction['direction'] == 'U':
                    current_y += 1
                elif instruction['direction'] == 'D':
                    current_y -= 1
                elif instruction['direction'] == 'L':
                    current_x -= 1
                elif instruction['direction'] == 'R':                    
                    current_x += 1
                else:
                    raise InvalidDirectionError(f"invalid direction: {instruction['direction']}")
                current_length += 1
                op(current_x, current_y, current_length)

    def __record_position(self, x, y, length):
        position = self.__position(x, y)
        if position not in self.__recorded_positions:
            self.__recorded_positions[position] = length

    def __compare_position(self, x, y, length):
        position = self.__position(x, y)
        if position in self.__recorded_positions:
            manhattan_distance = abs(x) + abs(y)
            sum_wire_lengths = length + self.__recorded_positions[position]
            if self.__cross_exists:
                if manhattan_distance < self.__best_distance_to_origin:
                    self.__best_distance_to_origin = manhattan_distance
                if sum_wire_lengths < self.__best_wire_length:
                    self.__best_wire_length = sum_wire_lengths
            else:
                self.__cross_exists = True
                self.__best_distance_to_origin = manhattan_distance
                self.__best_wire_length = sum_wire_lengths

    def __position(self, x, y):
        return f"{x},{y}"

def parse_entry(entry):
    return {
        'direction': entry[0],
        'distance': int(entry[1:]),
    }

def parse_input_file(input_filepath):
    with open(input_filepath, 'r') as file:
        line_1 = file.readline().rstrip()
        input_1 = [parse_entry(i) for i in line_1.split(',')]
        line_2 = file.readline().rstrip()
        input_2 = [parse_entry(j) for j in line_2.split(',')]
        return (input_1, input_2)

if __name__ == "__main__":
    file_path = get_input_filepath(__file__)
    (input_1, input_2) = parse_input_file(file_path)
    cc = CircuitChecker()
    cc.record_circuit(input_1)
    cc.compare_circuit(input_2)
    print(f"Solution to Part 1 is: {cc.best_distance_to_origin()}")
    print(f"Solution to Part 2 is: {cc.best_wire_length()}")

