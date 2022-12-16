#!/usr/bin/env python3

"""
Advent of Code 2022 Day 15: Beacon Exclusion Zone

https://adventofcode.com/2022/day/15

Solution by Eric Colton
"""

import re
import heapq
from typing import List, Tuple
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
DimRange = namedtuple("DimRange", ['start', 'end'])

def parse_line(line: str) -> Tuple[Point, Point]:
    match = re.match(r'Sensor at x=(\-?\d+), y=(\-?\d+): closest beacon is at x=(\-?\d+), y=(\-?\d+)', line)
    if not match:
        raise Exception("Unexpected line")
    return (Point(int(match.group(1)), int(match.group(2))), Point(int(match.group(3)), int(match.group(4))))

def parse_input_data(raw_lines: List[str]) -> List[Tuple[Point, Point]]:
    return [parse_line(line.rstrip()) for line in raw_lines]

def find_manhattan_distance(a: Point, b: Point) -> int:
    return abs(a.x - b.x) + abs(a.y - b.y)

def find_y_intersection(pair: Tuple[Point, Point], y_intersect: int) -> DimRange:
    sensor, beacon = pair
    sb_dist = find_manhattan_distance(sensor, beacon)
    diff = sb_dist - abs(sensor.y - y_intersect)
    if diff >= 0:
        return DimRange(sensor.x - diff, sensor.x + diff)
    return None

def intersections_on_y(data: List[Tuple[Point, Point]], y_intersect: int) -> List[DimRange]:
    return list(filter(lambda x: x != None, [find_y_intersection(pair, y_intersect) for pair in data]))

def find_flattened_ranges(ranges: List[DimRange]) -> List[DimRange]:
    ranges = sorted(ranges, key=lambda i: i[0])
    output = []
    heap = [ranges[0].end]
    start = ranges[0].start
    for r in ranges[1:]:
        while len(heap) > 0 and heap[0] < r.start:
            end = heapq.heappop(heap)
            if len(heap) == 0:
                output.append(DimRange(start, end))
                start = r.start
        heapq.heappush(heap, r.end)
    while len(heap) > 1:
        heapq.heappop(heap)
    output.append(DimRange(start, heapq.heappop(heap)))
    return output
    
def find_sum_ranges_coverage_area(ranges: List[DimRange]):
    return sum(map(lambda r: r.end - r.start, find_flattened_ranges(ranges)))

def constrict_ranges(ranges: List[DimRange], max_dim: int) -> List[DimRange]:
    output = []
    for r in ranges:
        if r.end < 0:
            continue
        elif r.start > max_dim:
            break
        start = 0 if r.start < 0 else r.start
        end = max_dim if r.end > max_dim else r.end
        output.append(DimRange(start, end))
    return output

def tuning_freq(x: int, y: int) -> int:
    return x * 4000000 + y

def find_tuning_frequency(data: List[Tuple[Point, Point]], max_dim: int) -> int:
    for y in range(max_dim + 1):
        flat_ranges = find_flattened_ranges(intersections_on_y(data, y))
        constricted_ranges = constrict_ranges(flat_ranges, max_dim)
        if len(constricted_ranges) == 1:
            if constricted_ranges[0].start == 1:
                return tuning_freq(0, y)
            elif constricted_ranges[0].end == max_dim - 1:
                return tuning_freq(max_dim, y)
        elif len(constricted_ranges) == 2:
            x = constricted_ranges[0].end + 1
            assert constricted_ranges[1].start == x + 1
            return tuning_freq(x, y)
        else:
            raise Exception("Unexpected possible tuning frequencies")
    raise Exception("Unable to find distress signal")

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        intervals = intersections_on_y(data, 2000000)
        part_1 = find_sum_ranges_coverage_area(intervals)
        assert part_1 == 5240818
        print(f"The solution to Part 1 is {part_1}")        

        part_2 = find_tuning_frequency(data, 4000000)
        assert part_2 == 13213086906101
        print(f"The solution to Part 2 is {part_2}")
