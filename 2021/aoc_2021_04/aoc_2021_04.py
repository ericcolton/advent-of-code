#!/usr/bin/env python3

"""
Advent of Code 2021 Day 4: Giant Squid

https://adventofcode.com/2021/day/4

Solution by Eric Colton
"""

from typing import List

class BingoCard:
    def __init__(self, grid: List[List[int]]):
        self.marked = set()
        self.lookup = {}
        for y in range(5):
            for x in range(5):
                self.lookup[grid[y][x]] = (y, x)
        
    def mark_number(self, number) -> bool:
        if number in self.lookup:
            y, x = self.lookup[number]
            self.marked.add((y, x))

            entire_row = True
            for x_scan in range(5):
                if (y, x_scan) not in self.marked:
                    entire_row = False
                    break
            if entire_row:
                return True
            
            entire_column = True
            for y_scan in range(5):
                if (y_scan, x) not in self.marked:
                    entire_column = False
                    break
            if entire_column:
                return True
            return False
    
    def score(self) -> List[int]:
        rv = 0
        for key, val in self.lookup.items():
            if val not in self.marked:
                rv += key
        return rv

    def reset(self):
        self.marked.clear()

def parse_input_data(raw_input: List[str]) -> tuple:
    numbers_draw = list(map(lambda x: int(x), raw_input[0].rstrip().split(',')))
    bingo_cards = []
    for i in range(2, len(raw_input), 6):
        grid = []
        for row in range(5):
            grid.append(list(map(lambda x: int(x), raw_input[i + row].rstrip().split())))
        bingo_cards.append(BingoCard(grid))
    return (numbers_draw, bingo_cards)

def play_bingo_to_win(numbers_draw: List[int], bingo_cards: List[BingoCard]) -> int:
    for number in numbers_draw:
        for bingo_card in bingo_cards:
            if bingo_card.mark_number(number):
                return bingo_card.score() * number
    return None

def play_bingo_to_lose(numbers_draw: List[int], bingo_cards: List[BingoCard]) -> int:
    last_score_to_win = None
    completed = set()
    for number in numbers_draw:
        to_pop = []
        for bingo_card in bingo_cards:
            if bingo_card not in completed and bingo_card.mark_number(number):
                last_score_to_win = bingo_card.score() * number
                completed.add(bingo_card)
    return last_score_to_win
                
if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        (numbers_draw, bingo_cards) = parse_input_data(raw_input)
        part_1 = play_bingo_to_win(numbers_draw, bingo_cards)
        assert part_1 == 58412
        print(f"The solution to Part 1 is {part_1}")

        for card in bingo_cards:
            card.reset()
        
        (numbers_draw, bingo_cards) = parse_input_data(raw_input)
        part_2 = play_bingo_to_lose(numbers_draw, bingo_cards)
        assert part_2 == 10030
        print(f"The solution to Part 2 is {part_2}")
