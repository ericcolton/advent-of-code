#!/usr/bin/env python3

import re
from functools import reduce

class Tile:
    def __init__(self, id: int, content):
        self.id = id
        self.location = 0, 0
        self.content = content
        self.build_signatures()
        self.top, self.bottom, self.left, self.right = None, None, None, None
    
    def build_signatures(self):
        self.top_sig = self._build_signature(self.content[0])
        self.bottom_sig = self._build_signature(list(reversed(self.content[-1])))
        self.left_sig = self._build_signature(list(reversed([entry[0] for entry in self.content])))
        self.right_sig = self._build_signature([entry[-1] for entry in self.content])
    
    def try_to_link_with_tile(self, other_tile: 'Tile'):
        for _ in range(4):
            if self.link(other_tile):
                return True
            other_tile.flip_horizontally()
            if self.link(other_tile):
                return True
            other_tile.flip_vertically()
            if self.link(other_tile):
                return True
            other_tile.flip_horizontally()
            if self.link(other_tile):
                return True
            other_tile.flip_vertically()
            other_tile.rotate()
        return False

    def link(self, other_tile: 'Tile'):
        x, y = self.location
        if self.top_sig and self.top_sig == other_tile.bottom_sig:
            self.top = other_tile
            self.top_sig = None
            other_tile.bottom_sig = None
            other_tile.location = x, (y + 1)
            return True
        elif self.bottom_sig and self.bottom_sig == other_tile.top_sig:
            self.bottom = other_tile
            self.bottom_sig = None
            other_tile.top_sig = None
            other_tile.location = x, (y - 1)
            return True
        elif self.left_sig and self.left_sig == other_tile.right_sig:
            self.left = other_tile
            self.left_sig = None
            other_tile.right_sig = None
            other_tile.location = (x - 1), y
            return True
        elif self.right_sig and self.right_sig == other_tile.left_sig:
            self.right = other_tile
            self.right_sig = None
            other_tile.left_sig = None
            other_tile.location = (x + 1), y
            return True
        return False

    def rotate(self):
        new_content = [i.copy() for i in self.content]
        for i in range(len(new_content)):
            for j in range(len(new_content[i])):
                new_content[i][j] = self.content[-j - 1][i]
        self.content = new_content
        self.build_signatures()
    
    def flip_vertically(self):
        for i in range(len(self.content) // 2):
            self.content[i], self.content[-i - 1] = self.content[-i - 1], self.content[i]
        self.build_signatures()

    def flip_horizontally(self):
        for i in range(len(self.content)):
            for j in range(len(self.content[i]) // 2):
                self.content[i][j], self.content[i][-j - 1] = self.content[i][-j - 1], self.content[i][j]
        self.build_signatures()

    def __str__(self):
        rv = ''
        for line in self.content:
            output_line = ''
            for c in line:
                output_line += str(c)
            rv += output_line + "\n"
        return rv

    def _build_signature(self, elements: list):
        total = 0
        for i, value in enumerate(reversed(list(elements))):
            if value:
                total += 2 ** i
        return total

# class DisjointSet:
#     def __init__(self):
#         self.nodes = {}

#     def add_connection(self, id_a: int, id_b: int):
#         id_a_root = id_a
#         while id_a_root in self.nodes:
#             id_a_root = self.nodes[id_a_root]
#         id_b_root = id_b
#         while id_b_root in self.nodes:
#             id_b_root = self.nodes[id_b_root]
#         if id_a_root != id_b_root:
#             self.nodes[id_a_root] = id_b_root

#     def result_sets(self):
#         results = {}
#         for id in self.nodes.keys():
#             id_root = id
#             while id_root in self.nodes:
#                 id_root = self.nodes[id_root]
#             if id_root in results:
#                 results[id_root].add(id)
#             else:
#                 results[id_root] = set([id_root, id])
#         return results.values()

class CornersRecorder:
    def __init__(self, location: tuple):
        self.min_x = location[0]
        self.min_y = location[1]
        self.max_x = location[0]
        self.max_y = location[1]

    def incorporate(self, other_cr: 'CornersRecorder') -> None:
        if other_cr:
            self.min_x = min(self.min_x, other_cr.min_x)
            self.min_y = min(self.min_y, other_cr.min_y)
            self.max_x = max(self.max_x, other_cr.max_x)
            self.max_y = max(self.max_y, other_cr.max_y)

def find_corners(tile: Tile, seen: dict = None) -> CornersRecorder:
    if not seen:
        seen = set([tile])
    elif tile in seen:
        return None
    else:
        seen.add(tile)
    corners_recorder = CornersRecorder(tile.location)
    print("location: {}".format(tile.location))
    if tile.top:
        corners_recorder.incorporate(find_corners(tile.top, seen))
    if tile.bottom:
        corners_recorder.incorporate(find_corners(tile.bottom, seen))
    if tile.left:
        corners_recorder.incorporate(find_corners(tile.left, seen))
    if tile.right:
        corners_recorder.incorporate(find_corners(tile.right, seen))
    return corners_recorder

def build_graph(data: set):
    initial_tile = next(iter(data))
    print(initial_tile)
    linked_tiles = set([initial_tile])
    unlinked_tiles = data.copy() - linked_tiles
    linked_locations = {}
    while len(unlinked_tiles) > 0:
        print("remaining: {}".format(len(unlinked_tiles)))
        just_linked_tile = None        
        for linked_tile in linked_tiles:
            for unlinked_tile in unlinked_tiles:
                if linked_tile.try_to_link_with_tile(unlinked_tile):
                    just_linked_tile = unlinked_tile
                    if just_linked_tile.location not in linked_locations:
                        print("\tlocations: {}".format(linked_locations))
                        linked_locations[just_linked_tile.location] = just_linked_tile.id
                    else:
                        raise Exception("location {} already linked".format(just_linked_tile.location))
                    break
            if just_linked_tile:
                break
        if just_linked_tile:
            linked_tiles.add(just_linked_tile)
            unlinked_tiles.remove(just_linked_tile)
        else:
            count = len(unlinked_tiles)
            raise Exception("Could not link remaining {} tile{}".format(count, 's' if count > 1 else ''))

    print(locations)
    corners = find_corners(initial_tile)
    print(corners)

def parse_input(input):
    tiles = set()
    current_tile_id, current_tile_contents = None, None
    for line in input:
        line = line.rstrip()
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
                raise Exception("unexpected content: '{}'".format(line))
    if current_tile_id and current_tile_contents:
        tiles.add(Tile(current_tile_id, current_tile_contents))
    return tiles

if __name__ == '__main__':
    input_filename = __file__.rstrip('.py') + '_input.txt'
    with open(input_filename, 'r') as file:
        data = parse_input(file)
        build_graph(data)