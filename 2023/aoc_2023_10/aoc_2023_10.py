#!/usr/bin/env python3

"""
Advent of Code 2023 Day 10: Pipe Maze

https://adventofcode.com/2023/day/10

Solution by Eric Colton
"""

import re

def total_encircled_points(route, data):
    points_inside, is_inside, border_type = 0, False, 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if (y, x) in route:
                if route[(y, x)] == '|':
                    assert border_type == 0
                    is_inside = not is_inside
                elif route[(y, x)] == '-':
                    assert border_type != 0
                elif route[(y, x)] == 'F':
                    assert border_type == 0
                    border_type = -1
                elif route[(y, x)] == 'L':
                    assert border_type == 0
                    border_type = 1
                elif route[(y, x)] == 'J':
                    assert border_type != 0
                    if border_type == -1:
                        is_inside = not is_inside
                    border_type = 0
                elif route[(y, x)] == '7':
                    assert border_type != 0
                    if border_type == 1:
                        is_inside = not is_inside
                    border_type = 0
            elif is_inside:
                points_inside += 1
    return points_inside

def find_exits(point, data):
    exits, dirs = [], []
    py, px = point
    point_sym = data[py][px]
    for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        # ignore incongruous pipes
        if point_sym == '-' and delta not in set([(0, -1), (0, 1)]):
            continue
        elif point_sym == '|' and delta not in set([(1, 0), (-1, 0)]):
            continue
        elif point_sym == '7' and delta not in set([(1, 0), (0, -1)]):
            continue
        elif point_sym == 'F' and delta not in set([(1, 0), (0, 1)]):
            continue
        elif point_sym == 'J' and delta not in set([(-1, 0), (0, -1)]):
            continue
        elif point_sym == 'L' and delta not in set([(-1, 0), (0, 1)]):
            continue

        new_y, new_x = py + delta[0], px + delta[1]
        # ignore the boundaries
        if new_y < 0 or new_y >= len(data) or new_x < 0 or new_x >= len(data[py]):
            continue
        # include in exits if the pipe type matches
        dest_sym = data[new_y][new_x]
        if ((delta == (1, 0) and dest_sym in set(['S', 'J', 'L', '|'])) or
            (delta == (-1, 0) and dest_sym in set(['S', '7', 'F', '|'])) or
            (delta == (0, 1) and dest_sym in set(['S', 'J', '7', '-'])) or
            (delta == (0, -1) and dest_sym in set(['S', 'L', 'F', '-']))):
            exits.append((new_y, new_x))
            dirs.append(delta)
    return exits, dirs

def sym_for_exit_dirs(dirs):
    dirs_set = set(dirs)
    if dirs_set == set([(0, -1), (0, 1)]):
        return '-'
    elif dirs_set == set([(1, 0), (-1, 0)]):
        return '|'
    elif dirs_set == set([(1, 0), (0, -1)]):
        return '7'
    elif dirs_set == set([(1, 0), (0, 1)]):
        return 'F'
    elif dirs_set == set([(-1, 0), (0, -1)]):
        return 'J'
    elif dirs_set == set([(-1, 0), (0, 1)]):
        return 'L'
    else:
        assert False

def find_circular_route(data):
    # find start point
    start = None
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'S':
                start = (y, x)
                break
        if start != None:
            break
    assert start != None

    # identify / confirm two routes away from start
    exits, dirs = find_exits(start, data)
    assert len(exits) == 2
    prev, point = start, exits[1]
    route = {start: sym_for_exit_dirs(dirs)}
    while point != start:
        exits, _ = find_exits(point, data)
        route[point] = data[point[0]][point[1]]
        assert len(exits) == 2
        assert prev in exits
        nextp = exits[1] if exits[0] == prev else exits[0]
        prev, point = point, nextp
    return route

def parse_input_data(raw_lines: str):
    return [line.rstrip() for line in raw_lines]

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        route = find_circular_route(data)
        part_1 = len(route.keys()) // 2
        assert part_1 == 6701
        print(f"The solution to Part 1 is {part_1}")

        part_2 = total_encircled_points(route, data)
        assert part_2 == 303
        print(f"The solution to Part 2 is {part_2}")
