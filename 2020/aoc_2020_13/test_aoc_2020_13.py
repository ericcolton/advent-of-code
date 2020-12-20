#!/usr/bin/env python3

import re
from aoc_2020_13 import parse_input_data, parse_bus_schedule, find_earliest_bus, find_first_sequential_schedule_start_time

TEST_INPUT_DATA = input_data = """939
7,13,x,x,59,x,31,19""".rsplit()

TEST_SCHEDULE_1 = "17,x,13,19"
TEST_SCHEDULE_2 = "67,7,59,61"
TEST_SCHEDULE_3 = "67,x,7,59,61"
TEST_SCHEDULE_4 = "67,7,x,59,61"
TEST_SCHEDULE_5 = "1789,37,47,1889"

def test_part_1():
    timestamp, buses = parse_input_data(TEST_INPUT_DATA)
    bus_id, wait_time = find_earliest_bus(timestamp, buses)
    assert bus_id * wait_time == 295

def test_part_2_basic_input():
    _, buses = parse_input_data(TEST_INPUT_DATA)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 1068781

def test_part_2_schedule_1():
    buses = parse_bus_schedule(TEST_SCHEDULE_1)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 3417

def test_part_2_schedule_2():
    buses = parse_bus_schedule(TEST_SCHEDULE_2)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 754018

def test_part_2_schedule_3():
    buses = parse_bus_schedule(TEST_SCHEDULE_3)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 779210

def test_part_2_schedule_4():
    buses = parse_bus_schedule(TEST_SCHEDULE_4)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 1261476

def test_part_2_schedule_5():
    buses = parse_bus_schedule(TEST_SCHEDULE_5)
    start_time = find_first_sequential_schedule_start_time(buses)
    assert start_time == 1202161486

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")