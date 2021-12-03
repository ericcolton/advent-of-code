#!/usr/bin/env python3

"""
Advent of Code 2021 Day 3: Dive!

https://adventofcode.com/2021/day/3

Solution by Eric Colton
"""

import re
from typing import List

def parse_input_data(raw_input: List[str]) -> List[str]:
    return [line.rstrip() for line in raw_input]

def convert_binary_to_decimal(binary_str: str) -> int:
    rv = 0
    for bit in binary_str:
        rv *= 2
        if bit == "1":
            rv += 1
    return rv

def calculate_gamma_epsilon(report: List[str]) -> tuple:
    bit_counts = [0] * len(report[0])
    for line in report:
        for i, bit in enumerate(line):
            if bit == "1":
                bit_counts[i] += 1
            elif bit != "0":
                raise Exception("Expected only 1 or 0")
    gamma, epsilon = "", ""
    for count in bit_counts:
        gamma += "1" if count > len(report) / 2 else "0"
        epsilon += "0" if count > len(report) / 2 else "1"
    return (convert_binary_to_decimal(gamma), convert_binary_to_decimal(epsilon))

def calculate_oxygen_co2(report: List[str], count_majority: bin) -> int:
    filtered_report = report
    for i in range(len(report[0])):
        count = sum([1 if line[i] == "1" else 0 for line in filtered_report])
        if count_majority:
            filter_bit = "1" if count >= len(filtered_report) / 2 else "0"
        else:
            filter_bit = "0" if count >= len(filtered_report) / 2 else "1"
        filtered_report = list(filter(lambda x: x[i] == filter_bit, filtered_report))
        if len(filtered_report) == 1:
            return convert_binary_to_decimal(filtered_report[0])
                
if __name__ == '__main__':
    input_filename = __file__.strip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        report = parse_input_data(raw_input)
        (gamma, epsilon) = calculate_gamma_epsilon(report)
        part_1 = gamma * epsilon
        assert part_1 == 1307354
        print(f"The solution to Part 1 is {part_1}")

        oxygen = calculate_oxygen_co2(report, True)
        co2 = calculate_oxygen_co2(report, False)
        part_2 = oxygen * co2
        assert part_2 == 482500
        print(f"The solution to Part 2 is {part_2}")
