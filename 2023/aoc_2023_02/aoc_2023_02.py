#!/usr/bin/env python3

"""
Advent of Code 2023 Day 2: Cube Conundrum

https://adventofcode.com/2023/day/2

Solution by Eric Colton
"""

import re
from typing import List, Dict
from functools import reduce

part_1_contents = {"red": 12, "green": 13, "blue": 14}

def does_game_pass(rounds: List[Dict[str, int]]) -> bool:
    for r in rounds:
        for (color, count) in r.items():
            if count <= part_1_contents[color]:
                continue
            return False
    return True

def power_min_game(rounds: List[Dict[str, int]]):
    contents = {"red": 0, "green": 0, "blue": 0}
    for r in rounds:
        for (color, count) in r.items():
            if count > contents[color]:
                contents[color] = count
    return reduce(lambda x, y: x * y, contents.values())

def find_sum_powers_min_contents(games: List[tuple[int, List[Dict[str, int]]]]) -> int:
    return sum(map(power_min_game, map(lambda g: g[1], games)))

def find_sum_passing_games(games: List[tuple[int, List[Dict[str, int]]]]) -> int:
    return sum(map(lambda g: g[0] if does_game_pass(g[1]) else 0, games))

def parse_input_data(raw_lines: str) -> List[str]:
    parsed_games = []
    for l in raw_lines:
        match = re.match(r'Game (\d+): (.+)', l.rstrip())
        if match:
            game_id, rounds = int(match.group(1)), match.group(2).split(';')
            parsed_rounds = []            
            for r in rounds:
                components = {}
                for component in r.split(','):
                    match2 = re.match(r'(\d+) (\w+)', component.lstrip())
                    if match2:
                        count, color = match2.group(1), match2.group(2)
                        components[color] = int(count)
                    else:
                        raise Exception('parse component error')
                parsed_rounds.append(components)
            parsed_games.append((game_id, parsed_rounds))
        else:
            raise Exception('parse line error')
    return parsed_games

if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_passing_games(data)
        assert part_1 == 2061
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_powers_min_contents(data)
        assert part_2 == 72596
        print(f"The solution to Part 2 is {part_2}")
