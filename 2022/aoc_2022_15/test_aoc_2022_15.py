#!/usr/bin/env python3

import re
from aoc_2022_15 import parse_input_data, intersections_on_y, find_sum_ranges_coverage_area, find_tuning_frequency

TEST_INPUT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")

def test_find_unavailable_y_spaces():
    data = parse_input_data(TEST_INPUT)
    intervals = intersections_on_y(data, 10)
    summ = find_sum_ranges_coverage_area(intervals)
    assert summ == 26

def test_find_tuning_frequency():
        data = parse_input_data(TEST_INPUT)
        tuning_freq = find_tuning_frequency(data, 20)
        assert tuning_freq == 56000011

# def test_fill_sand_until_full():
#     data = parse_input_data(TEST_INPUT)
#     r = Reservoir()
#     draw_rock_lines(r, data)
#     r.max_y += 1
#     count = add_sand_until_full(r)
#     assert count == 93

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
