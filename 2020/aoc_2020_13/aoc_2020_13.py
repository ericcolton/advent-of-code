#!/usr/bin/env python3

"""
Advent of Code 2020 Day 13: Shuttle Search

https://adventofcode.com/2020/day/13

Solution by Eric Colton
"""

import re
from collections import namedtuple
from collections.abc import Iterable

BusEntry = namedtuple('BusEntry', ['id','prefix_gap'])

def _bus_times_are_sequential(buses: list, target: int, index: int):
    if index == len(buses):
        return True
    bus = buses[index]
    adjusted_target = target + bus.prefix_gap
    if adjusted_target % bus.id == 0:
        return _bus_times_are_sequential(buses, adjusted_target + 1, index + 1)
    return False

def find_sequential_schedule_start_time(buses: list, base_target: int = 0, index: int = 0):
    if index == len(buses):
        return base_target
    elif index == 0:
        return find_sequential_schedule_start_time(buses, buses[0], 1)
    bus = buses[index]
    target = base_target
    while True:
        if (target + bus.prefix_gap + 1) % bus.id == 0:
            return find_sequential_schedule_start_time(buses, target, index + 1)
        target += base_target

# def _bus_times_are_sequential(buses: list, target: int, index: int):
#     if index == len(buses):
#         return True
#     bus = buses[index]
#     adjusted_target = target + bus.prefix_gap
#     if adjusted_target % bus.id == 0:
#         return _bus_times_are_sequential(buses, adjusted_target + 1, index + 1)
#     return False

# def find_sequential_schedule_start_time(buses: list):
#     target = 0
#     while not _bus_times_are_sequential(buses, target + 1, 1):
#         target += buses[0].id
#     return target

def find_earliest_bus(timestamp: int, buses: list):
    if len(buses) == 0:
        return -1, -1
    for i, bus in enumerate(buses):
        wait_time = bus.id - timestamp % bus.id
        if i == 0 or wait_time < min_wait_time:
            min_wait_time = wait_time
            bus_id_with_min_wait_time = bus.id
    return bus_id_with_min_wait_time, min_wait_time

def parse_bus_schedule(line: str):
    schedule = re.findall(r'(\w+),?', line)
    buses = []
    gap = 0
    for entry in schedule:
        if entry == 'x':
            gap += 1
        else:
            buses.append(BusEntry(int(entry), gap))
            gap = 0
    return buses

def parse_input_data(file: Iterable):
    timestamp, buses = 0, []
    for i, line in enumerate(file):
        if i == 0:
            timestamp = int(line.rstrip())
        elif i == 1:
            buses_line = line.rstrip()
            buses = parse_bus_schedule(buses_line)
        else:
            break
    return timestamp, buses

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        timestamp, buses = parse_input_data(file)
    bus_id, wait_mins = find_earliest_bus(timestamp, buses)
    part_1 = bus_id * wait_mins
    assert part_1 == 2165
    print("Solution to Part 1 is {}".format(part_1))

    part_2 = find_sequential_schedule_start_time(buses)
    print("Solution to Part 2 is {}".format(part_2))


