#!/usr/bin/env python3

import re
from functools import reduce

class Tile:
    def __init__(self, id: int, content):
        self.id = id
        self.content = content
        self.build_signatures()
        
    def build_signatures(self):
        self.top = self._build_signature(self.content[0])
        self.bottom = self._build_signature(list(reversed(self.content[-1])))
        self.left = self._build_signature(list(reversed([entry[0] for entry in self.content])))
        self.right = self._build_signature([entry[-1] for entry in self.content])
        self.signatures = [self.top, self.bottom, self.left, self.right]

    def _build_signature(self, elements: list):
        total = 0
        for i, value in enumerate(reversed(list(elements))):
            if value:
                total += 2 ** i
        return total

class DisjointSet:
    def __init__(self):
        self.nodes = {}

    def add_connection(self, id_a: int, id_b: int):
        id_a_root = id_a
        while id_a_root in self.nodes:
            id_a_root = self.nodes[id_a_root]
        id_b_root = id_b
        while id_b_root in self.nodes:
            id_b_root = self.nodes[id_b_root]
        if id_a_root != id_b_root:
            self.nodes[id_a_root] = id_b_root

    def result_sets(self):
        results = {}
        for id in self.nodes.keys():
            id_root = id
            while id_root in self.nodes:
                id_root = self.nodes[id_root]
            if id_root in results:
                results[id_root].add(id)
            else:
                results[id_root] = set([id_root, id])
        return results.values()

def build_graph(data: set):
    signature_lookup = {}
    for tile in data:
        for signature in tile.signatures:
            if signature in signature_lookup:
                signature_lookup[signature].add(tile)
            else:
                signature_lookup[signature] = set([tile])
    
    disjoint_set = DisjointSet()
    unconnected_tiles = data.copy()
    for signature in signature_lookup.keys():
        if len(signature_lookup[signature]) == 1:
            pass
        elif len(signature_lookup[signature]) == 2:
            tile_iter = iter(signature_lookup[signature])
            tile_a, tile_b = next(tile_iter), next(tile_iter)
            disjoint_set.add_connection(tile_a.id, tile_b.id)
            if tile_a in unconnected_tiles:
                unconnected_tiles.remove(tile_a)
            if tile_b in unconnected_tiles:
                unconnected_tiles.remove(tile_b)
        else:
            count = len(signature_lookup[signature])
            raise Exception("unexpected {} matches on signature {}".format(count, signature))
    result_sets = disjoint_set.result_sets()
    print(result_sets)
    return result_sets

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
        graph = build_graph(data)