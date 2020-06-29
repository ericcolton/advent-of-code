#!/usr/bin/env python3

import re
from aoc_2019_08 import interpret_image_layer_data, coalesce_layers, render_image

def test_coalesce():
    test_data = "0222112222120000"
    layers = interpret_image_layer_data(test_data, 2, 2)
    output = render_image(coalesce_layers(layers), 2, 2)
    assert output == " #\n# "

if __name__ == '__main__':
    for symbol in dir():
        if re.search('^test_', symbol):
            print(f"Running: {symbol}()")
            globals()[symbol]()
    print("Done")


