#!/usr/bin/env python3

"""
Advent of Code 2023 Day 7: Camel Cards

https://adventofcode.com/2023/day/7

Solution by Eric Colton
"""

import re
from functools import cmp_to_key
from collections import Counter
from typing import List

card_rank_classic = {"2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,            
             "8": 8,            
             "9": 9,            
             "T": 10,
             "J": 11,           
             "Q": 12,           
             "K": 13,                        
             "A": 14,                                     
             }

card_rank_joker = card_rank_classic.copy()
card_rank_joker["J"] = 1

def hand_type(hand, use_jokers: bool):
    counter = Counter(hand)
    if use_jokers:
        j_count = counter["J"] if 'J' in counter else 0
        del counter["J"]
    else:
        j_count = 0

    counts = sorted(counter.values(), reverse=True)
    if len(counts) <= 1:
        return 7 # five of a kind
    elif len(counts) == 2:
        if counts[0] + j_count >= 4:
            return 6 # four of a kind
        else:
            return 5 #full house
    elif len(counts) == 3:
        if counts[0] + j_count >= 3:
            return 4 # three of a kind
        else:
            return 3 # two pair
    elif len(counts) == 4:
        return 2 # two of a kind
    else:
        return 1 # high card
    
def secondary_cmp(hand_a, hand_b, ranker):
    for i in range(5):
        if ranker[hand_a[i]] < ranker[hand_b[i]]:
            return -1
        if ranker[hand_a[i]] > ranker[hand_b[i]]:
            return 1
    assert(False)

def classic_comparator(x, y):
    a, b = x[0], y[0]
    a_hand_type, b_hand_type = hand_type(a, False), hand_type(b, False)
    if a_hand_type == b_hand_type:
        return secondary_cmp(a, b, card_rank_classic)
    return a_hand_type - b_hand_type

def joker_comparator(x, y):
    a, b = x[0], y[0]
    a_hand_type, b_hand_type = hand_type(a, True), hand_type(b, True)
    if a_hand_type == b_hand_type:
        return secondary_cmp(a, b, card_rank_joker)
    return a_hand_type - b_hand_type
    
def find_sum_of_winnings(data: List[tuple[str, int]], use_jokers: bool):
    comparator = joker_comparator if use_jokers else classic_comparator
    ranked_hands = sorted(data, key=cmp_to_key(comparator))
    rank, total = 1, 0
    for hand, bid in ranked_hands:
        total += bid * rank
        rank += 1
    return total

def parse_input_data(raw_lines: str) -> List[tuple[str, int]]:
    data = []
    for line in raw_lines:
        match = re.match(r'(\w\w\w\w\w) (\d+)', line.rstrip())
        data.append((match.group(1), int(match.group(2))))
    return data

if __name__ == '__main__':
   input_filename = __file__.strip('.py') + '_input.txt'
   with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        data = parse_input_data(raw_input)
        part_1 = find_sum_of_winnings(data, False)
        assert part_1 == 250946742
        print(f"The solution to Part 1 is {part_1}")

        part_2 = find_sum_of_winnings(data, True)
        assert part_2 == 251824095
        print(f"The solution to Part 2 is {part_2}")