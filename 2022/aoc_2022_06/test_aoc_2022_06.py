#!/usr/bin/env python3

import re
from aoc_2022_06 import parse_input_data, find_start_marker

TEST_INPUT_1 = """mjqjpqmgbljsphdztnvjfqwrcgsmlb""".split("\n")
TEST_INPUT_2 = """bvwbjplbgvbhsrlpgdmjqwftvncz""".split("\n")
TEST_INPUT_3 = """nppdvjthqldpwncqszvftbrmjlhg""".split("\n")
TEST_INPUT_4 = """nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg""".split("\n")
TEST_INPUT_5 = """zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw""".split("\n")

def test_find_start_of_packet_marker():
    assert find_start_marker(parse_input_data(TEST_INPUT_1), 4) == 7
    assert find_start_marker(parse_input_data(TEST_INPUT_2), 4) == 5
    assert find_start_marker(parse_input_data(TEST_INPUT_3), 4) == 6
    assert find_start_marker(parse_input_data(TEST_INPUT_4), 4) == 10
    assert find_start_marker(parse_input_data(TEST_INPUT_5), 4) == 11

    assert find_start_marker(parse_input_data(TEST_INPUT_1), 14) == 19
    assert find_start_marker(parse_input_data(TEST_INPUT_2), 14) == 23
    assert find_start_marker(parse_input_data(TEST_INPUT_3), 14) == 23
    assert find_start_marker(parse_input_data(TEST_INPUT_4), 14) == 29
    assert find_start_marker(parse_input_data(TEST_INPUT_5), 14) == 26

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
