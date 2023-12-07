#!/usr/bin/env python3

import re
from functools import cmp_to_key
from collections import Counter
from aoc_2023_07 import parse_input_data, find_sum_of_winnings

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")

card_rank = {"2": 2,
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

def hand_type(hand):
    counter = Counter(hand)
    counts = sorted(counter.values(), reverse=True)
    if len(counts) == 1:
        return 7 # five of a kind
    elif len(counts) == 2:
        if counts[0] == 4:
            return 6 # four of a kind
        else:
            return 5 #full house
    elif len(counts) == 3:
        if counts[0] == 3:
            return 4 # three of a kind
        else:
            return 3 # two pair
    elif len(counts) == 4:
        return 2 # two of a kind
    else:
        return 1 # high card
    
def hand_type_with_jokers(hand):
    counter = Counter(hand)
    j_count = counter["J"] if 'J' in counter else 0
    del counter["J"]
    counts = sorted(counter.values(), reverse=True)
    if len(counts) - j_count <= 1:
        return 7 # five of a kind
    elif len(counts) - j_count == 2:
        if counts[0] + j_count == 4:
            return 6 # four of a kind
        else:
            return 5 #full house
    elif len(counts) == 3 - j_count:
        if counts[0] + j_count == 3:
            return 4 # three of a kind
        else:
            return 3 # two pair
    elif len(counts) - j_count == 4:
        return 2 # two of a kind
    else:
        return 1 # high card
    
def secondary_cmp(hand_a, hand_b):
    for i in range(5):
        if card_rank[hand_a[i]] < card_rank[hand_b[i]]:
            return -1
        if card_rank[hand_a[i]] > card_rank[hand_b[i]]:
            return 1
    assert(False)

def camel_comparator(x, y):
    a, b = x[0], y[0]
    a_hand_type, b_hand_type = hand_type(a), hand_type(b)
    if a_hand_type == b_hand_type:
        return secondary_cmp(a, b)
    return a_hand_type - b_hand_type

def joker_comparator(x, y):
    a, b = x[0], y[0]
    a_hand_type, b_hand_type = hand_type_with_jokers(a), hand_type_with_jokers(b)
    if a_hand_type == b_hand_type:
        return secondary_cmp(a, b)
    return a_hand_type - b_hand_type
    
def find_sum_of_winnings(data, use_jokers):
    comparator = joker_comparator if use_jokers else camel_comparator
    ranked_hands = sorted(data, key=cmp_to_key(comparator))
    rank, total = 1, 0
    for hand, bid in ranked_hands:
        total += bid * rank
        rank += 1
    return total

def parse_input_data(raw_lines: str):
    data = []
    for line in raw_lines:
        match = re.match(r'(\w\w\w\w\w) (\d+)', line.rstrip())
        data.append((match.group(1), int(match.group(2))))
    return data

# def test_product_of_ways_to_win():
#     data = parse_input_data(TEST_INPUT)
#     part_1 = find_sum_of_winnings(data, False)
#     assert(part_1 == 6440)

def test_ways_to_win():
    data = parse_input_data(TEST_INPUT)
    part_2 = find_sum_of_winnings(data, True)
    assert(part_2 == 5905)

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
