#!/usr/bin/env python3

"""
Advent of Code 2020 Day 17: Conway Cubes

https://adventofcode.com/2020/day/17
p
Solution by Eric Colton
"""

class ConwayCubeWorld:
    def __init__(self, initial_state, is_hypercube: bool = False):
        self.state = initial_state
        self.is_hypercube = is_hypercube

    def iterate(self):
        new_state = set()
        inactive_neighbors = set()
        for active_location in self.state:
            inactive_neighbors |= self.locate_inactive_neighbors(active_location)
            active_neighbors_count = self._count_active_neighbors(active_location)
            if active_neighbors_count == 2 or active_neighbors_count == 3:
                new_state.add(active_location)
        for inactive_neighbor in inactive_neighbors:
            if self._count_active_neighbors(inactive_neighbor) == 3:
                new_state.add(inactive_neighbor)
        self.state = new_state

    def total_active_count(self):
        return len(self.state)

    def locate_inactive_neighbors(self, location: tuple):
        x, y, z, a = location
        inactive_neighbors = set()
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                for nz in range(z - 1, z + 2):
                    a_range = range(a - 1, a + 2) if self.is_hypercube else range(a, a + 1)
                    for na in a_range:
                        if nx == x and ny == y and nz == z and na == a:
                            continue
                        if (nx, ny, nz, na) not in self.state:
                            inactive_neighbors.add((nx, ny, nz, na))
        return inactive_neighbors

    def _count_active_neighbors(self, location: tuple):
        x, y, z, a = location
        active_count = 0
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                for nz in range(z - 1, z + 2):
                    a_range = range(a - 1, a + 2) if self.is_hypercube else range(a, a + 1)
                    for na in a_range:
                        if nx == x and ny == y and nz == z and na == a:
                            continue
                        if (nx, ny, nz, na) in self.state:
                            active_count += 1
        return active_count

def parse_input(input):
    data = set()
    y = 0
    for line in input:
        for x, value in enumerate(line.rstrip()):
            if value == '#':
                data.add((x, y, 0, 0))
        y += 1
    return data

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input(file)
    world = ConwayCubeWorld(data)
    for _ in range(6):
        world.iterate()
    part_1 = world.total_active_count()
    assert part_1 == 295
    print("Solution to Part 1 is {}".format(part_1))

    world = ConwayCubeWorld(data, is_hypercube=True)
    for _ in range(6):
        world.iterate()
    part_2 = world.total_active_count()
    assert part_2 == 1972
    print("Solution to Part 2 is {}".format(part_2))
