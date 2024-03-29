#!/usr/bin/env python3

"""
Advent of Code 2021 Day 16: Packet Decoder

https://adventofcode.com/2021/day/16

Solution by Eric Colton
"""

from enum import Enum
from typing import List, Deque, Optional
from collections import deque
from functools import reduce


class OpType(Enum):
    sum = 0
    product = 1
    min = 2
    max = 3
    literal = 4
    gt = 5
    lt = 6
    equal = 7


class BitStream:
    def __init__(self, hex_input: str):
        self.data = deque()
        for char in hex_input.rstrip():
            self.data.extend(self._hex_to_binary(char))

    def read(self, count: int) -> List[bool]:
        return [self.data.popleft() for _ in range(count)]

    def read_bit(self) -> bool:
        return self.data.popleft()

    def length(self) -> int:
        return len(self.data)

    def _hex_to_binary(self, char: str) -> List[bool]:
        oc = ord(char)
        if oc >= ord('0') and oc <= ord('9'):
            val = oc - ord('0')
        elif oc >= ord('A') and oc <= ord('F'):
            val = 10 + oc - ord('A')
        else:
            raise Exception(f"Unexpected input char: '{char}'")
        return [val & (1 << i) > 0 for i in range(3, -1, -1)]


class Packet:
    def __init__(self, version: int, type: int):
        self.version = version
        self.type = type

    def eval(self):
        raise Exception(f"Must override eval()")

    def version_sum(self):
        raise Exception(f"Must override version_sum()")

    def bin_to_dec(input: List[bool], value: int = 0) -> int:
        for bit in input:
            value <<= 1
            value += 1 if bit else 0
        return value


class PacketFactory:
    def build(stream: BitStream) -> Packet:
        version = Packet.bin_to_dec(stream.read(3))
        type = Packet.bin_to_dec(stream.read(3))
        if type == OpType.literal.value:
            return LiteralPacket(version, type, stream)
        else:
            return OperatorPacket(version, type, stream)


class LiteralPacket(Packet):
    def __init__(self, version: int, type: int, stream: BitStream):
        super().__init__(version, type)
        value = 0
        keep_going = True
        while keep_going:
            keep_going = stream.read_bit()
            value = Packet.bin_to_dec(stream.read(4), value)
        self.value = value

    def eval(self):
        return self.value

    def version_sum(self):
        return self.version


class OperatorPacket(Packet):
    def __init__(self, version, type, stream: BitStream):
        super().__init__(version, type)
        self.subpackets = []
        subpackets_length_type = stream.read_bit()
        if subpackets_length_type:
            # count specified
            subpackets_count = Packet.bin_to_dec(stream.read(11))
            for _ in range(subpackets_count):
                self.subpackets.append(PacketFactory.build(stream))
        else:
            # length specified
            subpackets_length = Packet.bin_to_dec(stream.read(15))
            start_data_length = stream.length()
            while stream.length() > start_data_length - subpackets_length:
                self.subpackets.append(PacketFactory.build(stream))

    def eval(self):
        results = list(map(lambda p: p.eval(), self.subpackets))
        if self.type == OpType.sum.value:
            return sum(results)
        elif self.type == OpType.product.value:
            return reduce(lambda a, b: a * b, results)
        elif self.type == OpType.min.value:
            return min(results)
        elif self.type == OpType.max.value:
            return max(results)
        elif self.type == OpType.gt.value:
            assert len(results) == 2
            return 1 if results[0] > results[1] else 0
        elif self.type == OpType.lt.value:
            assert len(results) == 2
            return 1 if results[0] < results[1] else 0
        elif self.type == OpType.equal.value:
            assert len(results) == 2
            return 1 if results[0] == results[1] else 0

    def version_sum(self):
        return self.version + sum(list(map(lambda p: p.version_sum(), self.subpackets)))


def parse_input_data(raw_input=List[str]) -> BitStream:
    return BitStream(raw_input[0].rstrip())


def recursively_sum_versions(packet: Packet) -> int:
    total = packet.version
    if isinstance(packet, OperatorPacket):
        total += sum(list(map(lambda p: recursively_sum_versions(p), packet.subpackets)))
    return total


if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        raw_input = file.readlines()
        stream = parse_input_data(raw_input)
        packet = PacketFactory.build(stream)
        part_1 = packet.version_sum()
        assert part_1 == 901
        print(f"The solution to Part 1 is {part_1}")

        part_2 = packet.eval()
        assert part_2 == 110434737925
        print(f"The solution to Part 2 is {part_2}")
