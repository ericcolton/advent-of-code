#!/usr/bin/env python3

import math
from collections import defaultdict
from functools import reduce

ANGLE_TOLERANCE_DIGITS = 7

def get_relative_angle(origin: (int, int), candidate: (int, int)) -> float:
    origin_x, origin_y = origin
    cand_x, cand_y = candidate
    rel_x, rel_y = cand_x - origin_x, cand_y - origin_y
    return round(math.atan2(rel_y, rel_x), ANGLE_TOLERANCE_DIGITS)
    
def bucket_peers_by_angle(origin: (int, int), peers: [(int, int)]) -> dict:
    peers_by_angle = defaultdict(list)
    for peer in peers:
        if origin != peer:
            peers_by_angle[get_relative_angle(origin, peer)].append(peer)
    return peers_by_angle
        
def find_max_observables(input: [(int, int)]) -> int:
    max_observables_count = 0
    max_observables_location = 0, 0
    for origin in input:
        observables_count = len(bucket_peers_by_angle(origin, input).keys())
        if observables_count > max_observables_count:
            max_observables_count = observables_count
            max_observables_location = origin
    return max_observables_count, max_observables_location

def angle_sort_key(angle):
    if angle > math.pi / 2:
        return angle - 2 * math.pi
    return angle

def find_destory_order(location: (int, int), peers: [(int, int)]) -> list:
    peers_by_angle = bucket_peers_by_angle(location, all_nodes)
    max_rotations = 0
    for peers_at_angle in peers_by_angle.values():
        peers_at_angle.sort(key=lambda peer: peer[0] - location[0] + peer[1] - location[1])
        max_rotations = max(max_rotations, len(peers_at_angle))

    destroyed = []
    for _ in range(max_rotations):
        for angle in sorted(peers_by_angle.keys(), key=angle_sort_key, reverse=True):
            peers_at_angle = peers_by_angle[angle]
            if len(peers_at_angle) > 0:
                destroyed.append(peers_at_angle.pop(0))
    return destroyed

def parse_input_data(input: str):
    nodes = []
    rows = input.split("\n")
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '#':
                nodes.append((x, y))
    return nodes


    
if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        input_str = file.read()
    all_nodes = parse_input_data(input_str)
    part_1, location = find_max_observables(all_nodes)
    print(f"Solution for Part 1: {part_1}")
    assert part_1 == 347

    destroy_order = find_destory_order(location, all_nodes)
    part_2 = destroy_order[200]
    print(f"Solution to part 2 is {part_2}")
