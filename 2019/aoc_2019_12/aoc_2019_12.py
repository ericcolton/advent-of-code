#!/usr/bin/env python3

import re
import math

"""
Advent of Code 2019 Day 12: The N-Body Problem

https://adventofcode.com/2019/day/12
"""

class Moon:

    def __init__(self, position: (int, int, int), velocity: (int, int, int) = (0, 0, 0)):
        self.position = position
        self.velocity = velocity

    def apply_gravity(self, other_moon):
        vx, vy, vz = self.velocity
        if self.position[0] < other_moon.position[0]:
            vx += 1
        elif self.position[0] > other_moon.position[0]:
            vx -= 1
        if self.position[1] < other_moon.position[1]:
            vy += 1
        elif self.position[1] > other_moon.position[1]:
            vy -= 1
        if self.position[2] < other_moon.position[2]:
            vz += 1
        elif self.position[2] > other_moon.position[2]:
            vz -= 1
        self.velocity = vx, vy, vz

    def update_position(self):
        px, py, pz = self.position
        px += self.velocity[0]
        py += self.velocity[1]
        pz += self.velocity[2]
        self.position = px, py, pz

    def energy(self):
        px, py, pz = self.position
        potential_energy = abs(px) + abs(py) + abs(pz)
        vx, vy, vz = self.velocity
        kinetic_energy = abs(vx) + abs(vy) + abs(vz)
        return potential_energy * kinetic_energy
    
    def __eq__(self, other_moon):
        return self.position == other_moon.position and self.velocity == other_moon.velocity

    def __hash__(self):
        return hash((self.position, self.velocity))

class PlanetSystem:

    def __init__(self, moon_positions: list, moon_velocities: list = None):
        if moon_velocities is None:
            self.moons = [Moon(p) for p in moon_positions]
        else:
            if len(moon_positions) != len(moon_velocities):
                raise Exception("Count of Moon positions must equal count of moon velocities")
            self.moons = []
            for i in range(len(moon_positions)):
                moon = Moon(moon_positions[i], moon_velocities[i])
                self.moons.append(moon)

    def time_step(self):
        self.apply_gravities()
        self.update_positions()
    
    def apply_gravities(self):
        for moon in self.moons:
            for other_moon in self.moons:
                if moon != other_moon:
                    moon.apply_gravity(other_moon)
        
    def update_positions(self):
        for moon in self.moons:
            moon.update_position()

    def contained_energy(self):
        return sum([m.energy() for m in self.moons])

    def state(self):
        return hash(self)

    def __hash__(self):
        return hash(frozenset(self.moons))

    def __eq__(self, other_system):
        return set(self.moons) == set(other_system.moons)

def isolate_axis_coordinates(position: (int, int, int), axis = str) -> tuple:
    x, y, z = position
    if axis == 'x':
        return x, 0, 0
    elif axis == 'y':
        return 0, y, 0
    elif axis == 'z':
        return 0, 0, z
    else:
        raise Exception(f"invalid dimension: {axis}")

def iterations_until_repeat_for_isolated_axis(positions: list, axis: str) -> list:
    axis_isolated_positions = [isolate_axis_coordinates(p, axis) for p in positions]
    ps = PlanetSystem(axis_isolated_positions)
    ps_initial_state = ps.state()
    ps.time_step()
    step_count = 1
    while ps.state() != ps_initial_state:
        ps.time_step()
        step_count += 1
    return step_count

def parse_input_data(input: str) -> list:
    data = []
    for line in input.split("\n"):
        match = re.search(r'<\s*x\s*=\s*(-?\d+)\s*,\s*y\s*=\s*(-?\d+)\s*,\s*z\s*=\s*(-?\d+)\s*>', line)
        if match:
            x, y, z = int(match.group(1)), int(match.group(2)), int(match.group(3))
            data.append((x, y, z))
        else:
            raise Exception(f"could not parse input line {line}")
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        moon_positions = parse_input_data(file.read())

    ps = PlanetSystem(moon_positions)
    for _ in range(1000):
        ps.time_step()
    part_1 = ps.contained_energy()
    print(f"Solution to part 1 is {part_1}")
    assert part_1 == 7471

    x_step_count = iterations_until_repeat_for_isolated_axis(moon_positions, 'x')
    y_step_count = iterations_until_repeat_for_isolated_axis(moon_positions, 'y')
    z_step_count = iterations_until_repeat_for_isolated_axis(moon_positions, 'z')

    lcm = x_step_count * y_step_count // math.gcd(x_step_count, y_step_count)
    part_2 = lcm * z_step_count // math.gcd(lcm, z_step_count)
    print(f"Solution to part 2 is {part_2}")
    assert part_2 == 376243355967784
