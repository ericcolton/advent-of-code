#!/usr/bin/env python3

"""Advent of Code 2019 Day 01 - The Tyranny of the Rocket Equation."""

#import get_input_filepath from aoc_helpers

from aoc_helpers import get_input_filepath

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


def parse_input_file(filepath):
    with open(filepath, 'r') as file:
        return [int(line.rstrip()) for line in file]

if __name__ == "__main__":
    input_data = parse_input_file(get_input_filepath(__file__))

    spaceship = Spaceship()
    for i in input_data:
        spaceship.add_mass(i)

    print(f"The simple fuel required is {spaceship.simple_fuel_required()}")
    print(f"The complex fuel required is {spaceship.complex_fuel_required()}")

