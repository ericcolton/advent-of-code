#!/usr/bin/env python3

"""
Advent of Code 2019 Day 8: Space Image Format

https://adventofcode.com/2019/day/8
"""

def coalesce_layers(layers: [str]) -> str:
    output = []
    for pos in range(len(layers[0])):
        for layer in layers:
            val = layer[pos]
            if val == '0' or val == '1':
                output.append(val)
                break
        else:
            raise f"Count not find value in any layer as position {pos}"
    return output

def render_image(layer, width, height):
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            val = layer[x + y * width]
            row.append('#' if val == '1' else ' ')
        rows.append(''.join(row))
    return "\n".join(rows)

def chunk(data: str, size: int):
    i = 0
    while i < len(data):
        chunk = data[i : i + size]
        if len(chunk) < size:
            raise "Invalid data size"
        yield chunk
        i += size

def interpret_image_layer_data(data: str, width: int, height: int) -> list:
    return list(chunk(data, width * height))

def find_min_layer_count(layers: [str], target : str):
    return min(layers, key=lambda x: x.count(target))

if __name__ == '__main__':
    input_filepath = __file__.rstrip('.py') + '_input.txt'
    with open(input_filepath, 'r') as file:
        input = file.read().rstrip()
    width, height = 25, 6
    layers = interpret_image_layer_data(input, width, height)
    min_0_layer = find_min_layer_count(layers, '0')
    part_1 = min_0_layer.count('1') * min_0_layer.count('2')
    print(f"Solution to part 1: {part_1}")
    assert part_1 == 1206
    
    part_2 = render_image(coalesce_layers(layers), width, height)
    print(f"Solution to part 2:\n{part_2}")
