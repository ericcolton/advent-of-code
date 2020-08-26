#!/usr/bin/env python3

import re
from aoc_2019_12 import parse_input_data, PlanetSystem

def build_system_in_initial_state():
    initial_positions_data = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""
    moons_initial_positions = parse_input_data(initial_positions_data)
    return PlanetSystem(moons_initial_positions)

def test_step_1():
    expected_positions_data = """<x= 2, y=-1, z= 1>
<x= 3, y=-7, z=-4>
<x= 1, y=-7, z= 5>
<x= 2, y= 2, z= 0>"""
    expected_velocities_data = """<x= 3, y=-1, z=-1>
<x= 1, y= 3, z= 3>
<x=-3, y= 1, z=-3>
<x=-1, y=-3, z= 1>"""
    expected_positions = parse_input_data(expected_positions_data)
    expected_velocities = parse_input_data(expected_velocities_data)
    ps_expected = PlanetSystem(expected_positions, expected_velocities)
    ps = build_system_in_initial_state()
    for _ in range(1):
        ps.time_step()
    assert ps == ps_expected

def test_step_2():
    expected_positions_data = """<x= 5, y=-3, z=-1>
<x= 1, y=-2, z= 2>
<x= 1, y=-4, z=-1>
<x= 1, y=-4, z= 2>"""
    expected_velocities_data = """<x= 3, y=-2, z=-2>
<x=-2, y= 5, z= 6>
<x= 0, y= 3, z=-6>
<x=-1, y=-6, z= 2>"""
    expected_positions = parse_input_data(expected_positions_data)
    expected_velocities = parse_input_data(expected_velocities_data)
    ps_expected = PlanetSystem(expected_positions, expected_velocities)
    ps = build_system_in_initial_state()
    for _ in range(2):
        ps.time_step()
    assert ps == ps_expected

def test_step_10():
    expected_positions_data = """<x= 2, y= 1, z=-3>
<x= 1, y=-8, z= 0>
<x= 3, y=-6, z= 1>
<x= 2, y= 0, z= 4>"""
    expected_velocities_data = """<x=-3, y=-2, z= 1>
<x=-1, y= 1, z= 3>
<x= 3, y= 2, z=-3>
<x= 1, y=-1, z=-1>"""
    expected_positions = parse_input_data(expected_positions_data)
    expected_velocities = parse_input_data(expected_velocities_data)
    ps_expected = PlanetSystem(expected_positions, expected_velocities)
    ps = build_system_in_initial_state()
    for _ in range(10):
        ps.time_step()
    assert ps == ps_expected

def test_returned_to_initial_state():
    ps = build_system_in_initial_state()
    ps_initial_state = ps.state()
    ps.time_step()
    step_count = 1
    while ps.state() != ps_initial_state:
        ps.time_step()
        step_count += 1
        if step_count > 2772:
            break
    assert step_count == 2772

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running {symbol}()")
            globals()[symbol]()
    print("Done")