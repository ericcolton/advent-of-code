#!/usr/bin/env python3

import re
from aoc_2021_16 import parse_input_data, recursively_sum_versions, PacketFactory, BitStream, LiteralPacket, OperatorPacket

TEST_INPUT_LITERAL = """D2FE28""".split("\n")
TEST_INPUT_OPERATOR_1 = """38006F45291200""".split("\n")
TEST_INPUT_OPERATOR_2 = """EE00D40C823060""".split("\n")

TEST_INPUT_SUM_1 = """8A004A801A8002F478""".split("\n")
TEST_INPUT_SUM_2 = """620080001611562C8802118E34""".split("\n")
TEST_INPUT_SUM_3 = """C0015000016115A2E0802F182340""".split("\n")
TEST_INPUT_SUM_4 = """A0016C880162017C3686B18A3D4780""".split("\n")

def test_build_literal_packet():
    stream = parse_input_data(TEST_INPUT_LITERAL)
    packet = PacketFactory.build(stream)
    assert isinstance(packet, LiteralPacket)
    assert packet.value == 2021

def test_build_operator_packet_by_length():
    stream = parse_input_data(TEST_INPUT_OPERATOR_1)
    packet = PacketFactory.build(stream)
    assert isinstance(packet, OperatorPacket)
    assert len(packet.subpackets) == 2
    assert packet.subpackets[0].value == 10
    assert packet.subpackets[1].value == 20

def test_build_operator_packet_by_count():
    stream = parse_input_data(TEST_INPUT_OPERATOR_2)
    packet = PacketFactory.build(stream)
    assert isinstance(packet, OperatorPacket)
    assert len(packet.subpackets) == 3
    assert packet.subpackets[0].value == 1
    assert packet.subpackets[1].value == 2
    assert packet.subpackets[2].value == 3

def test_version_sum_1():
    stream = parse_input_data(TEST_INPUT_SUM_1)
    packet = PacketFactory.build(stream)
    total = recursively_sum_versions(packet)
    assert total == 16

def test_version_sum_2():
    stream = parse_input_data(TEST_INPUT_SUM_2)
    packet = PacketFactory.build(stream)
    total = recursively_sum_versions(packet)
    assert total == 12

def test_version_sum_3():
    stream = parse_input_data(TEST_INPUT_SUM_3)
    packet = PacketFactory.build(stream)
    total = recursively_sum_versions(packet)
    assert total == 23

def test_version_sum_4():
    stream = parse_input_data(TEST_INPUT_SUM_4)
    packet = PacketFactory.build(stream)
    total = recursively_sum_versions(packet)
    assert total == 31

if __name__ == '__main__':
    for symbol in dir():
        if re.match('^test_', symbol):
            print(f"running {symbol}()")
            globals()[symbol]()
    print("Done")
