#!/usr/bin/env python3

"""
Advent of Code 2019 Day 7: Amplification Circuit

https://adventofcode.com/2019/day/7
"""

from intcode import IntcodeComputer

def run_linked_computers(program, settings, logging=False):
    computers = [IntcodeComputer(program, [s], logging=logging) for s in settings]
    computers[0].input.append(0)
    halted = set()
    while len(halted) < len(computers):
        for i, computer in enumerate(computers):
            if computer in halted:
                continue
            prev_computer = computers[i - 1] if i > 0 else computers[-1]
            computer.input.extend(prev_computer.output)
            if computer.run_program():
                halted.add(computer)
            else:
                prev_computer.output = []
    return computers[-1].output[0]

def find_max_output_all_perms(program, unallocated: {int}, logging=False, _settings: [int] = []):
    if len(unallocated) == 0:
        return run_linked_computers(program, _settings, logging)
    max_output_seen = 0
    for setting in unallocated:
        _settings.append(setting)
        rv = find_max_output_all_perms(program, unallocated - {setting}, logging=logging, _settings=_settings)
        _settings.pop()
        max_output_seen = max(max_output_seen, rv)
    return max_output_seen

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        program = [int(x) for x in file.readline().rstrip().split(',')]
    part_1 = find_max_output_all_perms(program, set(range(5)))
    print(f"Solution to part 1 is {part_1}")
    assert part_1 == 45730
    part_2 = find_max_output_all_perms(program, set(range(5, 10)))
    print(f"Solution to part 2 is {part_2}")
    assert part_2 == 5406484
