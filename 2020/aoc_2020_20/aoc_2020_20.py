#!/usr/bin/env python3

"""
Advent of Code 2020 Day 20: Jurassic Jigsaw

https://adventofcode.com/2020/day/20

Solution by Eric Colton
"""

import re
from functools import reduce

SEA_MONSTER_PROFILE = """
..................#.
#....##....##....###
.#..#..#..#..#..#..."""

class Tile:
    def __init__(self, id: int, content):
        self.id = id
        self.base_content = content
        self.reoriented_base_content = content
        self.content = content
        self.corner_locations = None
        self.current_rotation = 0
        self.build_signatures()

    def build_signatures(self):
        self.top = self._build_signature(self.content[0])
        self.bottom = self._build_signature(self.content[-1])
        self.left = self._build_signature([entry[0] for entry in self.content])
        self.right = self._build_signature([entry[-1] for entry in self.content])

    def orient_to(self, orientation):
        self.content = self.base_content
        if orientation & 1:
            self.flip_horizontally()
        if orientation & 2:
            self.flip_vertically()
        self.reoriented_base_content = self.content
        self.build_signatures()

    def rotate_to(self, rotation: int):
        if self.current_rotation == rotation:
            return
        content = [i.copy() for i in self.reoriented_base_content]
        for _ in range((rotation - self.current_rotation) % 4):
            new_content = [i.copy() for i in content]
            for i in range(len(content)):
                for j in range(len(content[i])):
                    new_content[i][j] = content[-j - 1][i]
            content = [i.copy() for i in new_content]
        self.content = content
        self.build_signatures()

    def flip_vertically(self):
        for i in range(len(self.content) // 2):
            self.content[i], self.content[-i - 1] = self.content[-i - 1], self.content[i]

    def flip_horizontally(self):
        for i in range(len(self.content)):
            for j in range(len(self.content[i]) // 2):
                self.content[i][j], self.content[i][-j - 1] = self.content[i][-j - 1], self.content[i][j]

    def linkable_with_edges(self, available_edges):
        return (self.top in available_edges or
            self.bottom in available_edges or
            self.left in available_edges or
            self.right in available_edges)

    def _build_signature(self, elements: list):
        total = 0
        for i, value in enumerate(reversed(list(elements))):
            if value:
                total += 2 ** i
        return total

class PuzzleBuilder:

    def __init__(self, tiles: set):
        self.initial_tiles = tiles
        self.build_success = False
        self.corner_locations = None
        self.side_length = int(len(tiles) ** 0.5)
        if self.side_length ** 2 != len(tiles):
            raise Exception("Number of pieces must be square")

    def build(self):
        initial_tile = reduce(lambda a, b: a if a.id < b.id else b, self.initial_tiles)
        unlinked_tiles = self.initial_tiles.copy()
        unlinked_tiles.remove(initial_tile)
        self.tile_for_location = {}
        self.tile_for_location[(0, 0)] = initial_tile
        self.location_for_tile = {}
        self.location_for_tile[initial_tile] = (0, 0)
        if self._build(set([initial_tile]), unlinked_tiles):
            self.build_success = True
            return True
        return False

    def ordered_tiles(self):
        if not self.build_success:
            raise Exception("Cannot fetched ordered tiles without build success")
        min_x, min_y, _, _ = self._find_corner_locations()
        ordered_tiles = []
        for y in range(min_y, min_y + self.side_length):
            row = []
            for x in range(min_x, min_x + self.side_length):
                row.append(self.tile_for_location[(x, y)])
            ordered_tiles.append(row)
        return list(reversed(ordered_tiles))

    def can_be_placed(self, candidate_tile: 'Tile', candidate_location: tuple):
        hits = 0
        x, y = candidate_location
        above = x, y + 1
        if above in self.tile_for_location:
            hits += 1
            above_tile = self.tile_for_location[above]
            if above_tile.bottom != candidate_tile.top:
                return False
        below = x, y - 1
        if below in self.tile_for_location:
            hits += 1
            below_tile = self.tile_for_location[below]
            if below_tile.top != candidate_tile.bottom:
                return False
        to_the_left = x - 1, y
        if to_the_left in self.tile_for_location:
            hits += 1
            to_the_left_tile = self.tile_for_location[to_the_left]
            if to_the_left_tile.right != candidate_tile.left:
                return False
        to_the_right = x + 1, y
        if to_the_right in self.tile_for_location:
            hits += 1
            to_the_right_tile = self.tile_for_location[to_the_right]
            if to_the_right_tile.left != candidate_tile.right:
                return False
        if hits == 0:
            raise Exception("Location {} should link to at least one tile".format(candidate_location))
        return True

    def corner_tile_ids_product(self):
        if not self.build_success:
            raise Exception("Corners can only be queried once built")
        min_x, min_y, max_x, max_y = self._find_corner_locations()
        corner_tiles = [\
            self.tile_for_location[(min_x, min_y)], \
            self.tile_for_location[(min_x, max_y)], \
            self.tile_for_location[(max_x, min_y)], \
            self.tile_for_location[(max_x, max_y)], \
            ]
        return reduce(lambda a, b: a * b, map(lambda a: a.id, corner_tiles))

    def _calculate_available_edges(self, linked_tiles: set):
        available_edges = set()
        for tile in linked_tiles:
            x, y = self.location_for_tile[tile]
            if (x, y + 1) not in self.tile_for_location:
                available_edges.add(tile.top)
            if (x, y - 1) not in self.tile_for_location:
                available_edges.add(tile.bottom)
            if (x - 1, y) not in self.tile_for_location:
                available_edges.add(tile.left)
            if (x + 1, y) not in self.tile_for_location:
                available_edges.add(tile.right)
        return available_edges

    def _build(self, linked_tiles: set, unlinked_tiles: set):
        if len(unlinked_tiles) == 0:
            return True
        available_edges = self._calculate_available_edges(linked_tiles)
        for linked_tile in linked_tiles:
            linked_location = self.location_for_tile[linked_tile]
            for unlinked_tile in unlinked_tiles:
                for orientation in range(4):
                    unlinked_tile.orient_to(orientation)
                    for rotation in range(4):
                        unlinked_tile.rotate_to(rotation)
                        if not unlinked_tile.linkable_with_edges(available_edges):
                            continue
                        for side in range(4):
                            new_location = self._side_available(linked_location, side)
                            if new_location:
                                if self.can_be_placed(unlinked_tile, new_location):
                                    self.location_for_tile[unlinked_tile] = new_location
                                    self.tile_for_location[new_location] = unlinked_tile
                                    self._reset_corner_locations()
                                    linked_tiles_copy = linked_tiles.copy()
                                    unlinked_tiles_copy = unlinked_tiles.copy()
                                    linked_tiles_copy.add(unlinked_tile)
                                    unlinked_tiles_copy.remove(unlinked_tile)
                                    rv = self._build(linked_tiles_copy, unlinked_tiles_copy)
                                    if rv:
                                        return True
                                    else:
                                        del self.location_for_tile[unlinked_tile]
                                        del self.tile_for_location[new_location]
                                        self._reset_corner_locations()
        return None

    def _reset_corner_locations(self):
        self.corner_locations = None

    def _find_corner_locations(self):
        if self.corner_locations:
            return self.corner_locations
        min_x, min_y, max_x, max_y = 0, 0, 0, 0
        for location in self.tile_for_location.keys():
            x, y = location
            min_x, min_y = min(min_x, x), min(min_y, y)
            max_x, max_y = max(max_x, x), max(max_y, y)
        self.corner_locations = min_x, min_y, max_x, max_y
        return self.corner_locations

    def _side_available(self, location, side):
        x, y = location
        if side == 0:
            candidate = x, y + 1
        elif side == 1:
            candidate = x + 1, y
        elif side == 2:
            candidate = x, y - 1
        elif side == 3:
            candidate = x - 1, y
        else:
            raise Exception("Illegal side: '{}'".format(side))
        min_x, min_y, max_x, max_y = self._find_corner_locations()
        if max_x - x > self.side_length or \
        min_x + x > self.side_length or \
        max_y - y > self.side_length or \
        min_y + y > self.side_length:
            return None
        return None if candidate in self.tile_for_location else candidate

def generate_combined_tile(ordered_tiles: list):
    rows = []
    for y_tile in range(len(ordered_tiles)):
        for y_char in range(1, len(ordered_tiles[y_tile][0].content) - 1):
            row = []
            for x_tile in range(len(ordered_tiles[y_tile])):
                tile = ordered_tiles[y_tile][x_tile]
                for x_char in range(1, len(tile.content[y_char]) - 1):
                    row.append(tile.content[y_char][x_char])
            rows.append(row)
    return Tile(0, rows)

def parse_sea_monster():
    iterator = iter(SEA_MONSTER_PROFILE.split("\n"))
    next(iterator) # ignore first line
    rows = []
    for line in iterator:
        rows.append([1 if c == '#' else 0 for c in line.rstrip("\n")])
    return rows

def count_non_sea_monster_positives(tile: Tile):
    sea_monster = parse_sea_monster()
    non_sea_monster_count_low_watermark = -1
    for orientation in range(4):
        tile.orient_to(orientation)
        for rotation in range(4):
            tile.rotate_to(rotation)
            sm_counter = 0
            sm_marked = set()
            for y in range(len(tile.content) - len(sea_monster)):
                tile_row = tile.content[y]
                for x in range(len(tile_row) - len(sea_monster[0])):
                    sm_found = True
                    for sm_y in range(len(sea_monster)):
                        for sm_x in range(len(sea_monster[sm_y])):
                            if sea_monster[sm_y][sm_x] == 1:
                                if not tile.content[y + sm_y][x + sm_x] == 1:
                                    sm_found = False
                                    break
                        if not sm_found:
                            break
                    if sm_found:
                        sm_counter += 1
                        for sm_y in range(len(sea_monster)):
                            for sm_x in range(len(sea_monster[sm_y])):
                                if sea_monster[sm_y][sm_x] == 1:
                                    sm_marked.add((y + sm_y, x + sm_x))
            non_sea_monster_count = 0
            for y in range(len(tile.content)):
                for x in range(len(tile.content[y])):
                    if tile.content[y][x] and not (y, x) in sm_marked:
                        non_sea_monster_count += 1

            if non_sea_monster_count_low_watermark > 0:
                non_sea_monster_count_low_watermark = min(non_sea_monster_count_low_watermark, non_sea_monster_count)
            else:
                non_sea_monster_count_low_watermark = non_sea_monster_count
    return non_sea_monster_count_low_watermark

def parse_input(input):
    tiles = set()
    current_tile_id, current_tile_contents = None, None
    line_count = -1
    for line in input:
        line = line.rstrip()
        line_count += 1
        header_match = re.search(r'Tile (\d+):', line)
        if header_match:
            current_tile_id = int(header_match.group(1))
            current_tile_contents = []
            continue
        elif line == '':
            if not current_tile_id:
                raise Exception("unexpected empty line")
            tiles.add(Tile(current_tile_id, current_tile_contents))
            current_tile_id, current_tile_contents = None, None
        else:
            content_match = re.fullmatch(r'([\#\.]+)', line)
            if content_match:
                current_tile_contents.append([1 if c == '#' else 0 for c in line])
            else:
                raise Exception("unexpected content: '{}' on line {}".format(line, line_count))
    if current_tile_id and current_tile_contents:
        tiles.add(Tile(current_tile_id, current_tile_contents))
    return tiles

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input(file)
        puzzle_builder = PuzzleBuilder(data)
        puzzle_builder.build()
        part_1 = puzzle_builder.corner_tile_ids_product()
        assert part_1 == 32287787075651
        print("The solution to Part 1 is {}".format(part_1))

        ordered_tiles = puzzle_builder.ordered_tiles()
        combined_tile = generate_combined_tile(ordered_tiles)
        part_2 = count_non_sea_monster_positives(combined_tile)
        assert part_2 == 1939
        print("The solution to Part 2 is {}".format(part_2))
