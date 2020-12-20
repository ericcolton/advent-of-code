#!/usr/bin/env python3

"""
Advent of Code 2020 Day 13: Shuttle Search

https://adventofcode.com/2020/day/13

Solution by Eric Colton
"""

import re
from collections import namedtuple
from collections.abc import Iterable
from math import gcd

BusEntry = namedtuple('BusEntry', ['id','offset'])

def lcm(num1: int, num2: int):
    return num1 * num2 // gcd(num1, num2)

def find_first_sequential_schedule_start_time(buses: list, target: int = 0, index: int = 0, search_cadence: int = 1):
    if index == len(buses):
        return target
    bus = buses[index]
    while (target + bus.offset) % bus.id != 0:
        target += search_cadence
    return find_first_sequential_schedule_start_time(buses, target, index + 1, lcm(search_cadence, bus.id))

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
    for offset, entry in enumerate(schedule):
        if entry != 'x':
            buses.append(BusEntry(int(entry), offset))
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

    part_2 = find_first_sequential_schedule_start_time(buses)
    assert part_2 == 534035653563227
    print("Solution to Part 2 is {}".format(part_2))
