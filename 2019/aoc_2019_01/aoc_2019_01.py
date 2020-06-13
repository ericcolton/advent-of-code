#!/usr/bin/env python3

"""
Advent of Code 2019 Day 01 - The Tyranny of the Rocket Equation.

https://adventofcode.com/2019/day/1
"""

class Spaceship():
    def __init__(self):
        self.__simple_fuel_required = 0
        self.__complex_fuel_required = 0

    def add_mass(self, mass):
        """ Updates feul requirements for added mass """
        if not isinstance(mass, int):
            raise TypeError("requires int input")

        # Solve simple fuel
        base_fuel = self.__fuel_for_mass(mass)
        self.__simple_fuel_required += base_fuel

        # Solve fuel for fuel
        fuel_for_fuel = 0
        fuel_for_iteration = self.__fuel_for_mass(base_fuel)
        while fuel_for_iteration > 0:
            fuel_for_fuel += fuel_for_iteration
            fuel_for_iteration = self.__fuel_for_mass(fuel_for_iteration)
        
        self.__complex_fuel_required += base_fuel + fuel_for_fuel

    def simple_fuel_required(self):
        return self.__simple_fuel_required
    
    def complex_fuel_required(self):
        return self.__complex_fuel_required

    def __fuel_for_mass(self, mass):
        return mass // 3 - 2

if __name__ == "__main__":
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        input_data = [int(line.rstrip()) for line in file]

    spaceship = Spaceship()
    for i in input_data:
        spaceship.add_mass(i)

    part_1 = spaceship.simple_fuel_required()
    print(f"Part 1 Solution: {part_1}")
    assert part_1 == 3287620
    part_2 = spaceship.complex_fuel_required()
    print(f"Part 2 Solution: {part_2}")
    assert part_2 == 4928567
