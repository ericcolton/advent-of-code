#!/usr/bin/env python3

"""
Advent of Code 2020 Day 11: Seating System

https://adventofcode.com/2020/day/11

Solution by Eric Colton
"""

def count_total_occupied(data: list):
    return sum(sum(map(lambda x: 1 if x == 1 else 0, row_data)) for row_data in data)

def count_occupied_neighbors(row: int, col: int, data: list, adjacent_only: bool):
    deltas = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    occupied_count = 0
    for delta_row, delta_col in deltas:
        adjusted_row, adjusted_col = row, col
        while True:
            adjusted_row += delta_row
            adjusted_col += delta_col
            if (adjusted_row < 0 or
                adjusted_row >= len(data) or
                adjusted_col < 0 or
                adjusted_col >= len(data[0])):
                break
            elif data[adjusted_row][adjusted_col] == 1:
                occupied_count += 1
                break
            elif data[adjusted_row][adjusted_col] == 0:
                break
            if adjacent_only:
                break
    return occupied_count

def iterate_round(data: list, adjacent_only: bool, full_threshold: int):
    next_round = []
    update_occurred = False
    for row, row_data in enumerate(data):
        next_row = []
        for col, state in enumerate(row_data):
            if state == -1:
                next_state = -1
            else:
                next_state = state                
                if state == 0 and count_occupied_neighbors(row, col, data, adjacent_only) == 0:
                    next_state = 1
                    update_occurred = True
                if state == 1 and count_occupied_neighbors(row, col, data, adjacent_only) >= full_threshold:
                    next_state = 0
                    update_occurred = True
            next_row.append(next_state)
        next_round.append(next_row)
    return (update_occurred, next_round)

def iterate_until_stable(data: list, adjacent_only: bool, full_threshold: int):
    while True:
        update_occurred, data = iterate_round(data, adjacent_only, full_threshold)
        if not update_occurred:
            return data

def parse_input_file(file):
    return [[0 if char == 'L' else -1 for char in line.rstrip()] for line in file]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        orig_data = parse_input_file(file)
    part_1_data = iterate_until_stable(orig_data.copy(), True, 4)
    part_1 = count_total_occupied(part_1_data)
    assert part_1 == 2277
    print("Solution to Part 1 is {}".format(part_1))

    part_2_data = iterate_until_stable(orig_data.copy(), False, 5)
    part_2 = count_total_occupied(part_2_data)
    assert part_2 == 2066
    print("Solution to Part 2 is {}".format(part_2))