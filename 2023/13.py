#!/usr/bin/env python3
import time
import re
from util import read_input_lines, split_list, line_diff

start_timer = time.time()

SAMPLE = False
DEBUG = False

inputs = read_input_lines('13', SAMPLE)
grids = split_list(inputs, '')

def get_axis(grid):
    axis = set()
    for i in range(0, len(grid) - 1):
        max_delta = min(i, len(grid) - 1 - i - 1)    # len = 10, max_i = 9 -> letzte Spiegelung 8/9 (über range garantiert)
        possible_axis = all(grid[i - delta] == grid[i + 1 + delta] for delta in range(max_delta + 1))
        if possible_axis:
            axis.add(i + 1)

    return axis


def get_smudged_axis(grid, max_diff = 0):
    for i in range(0, len(grid)):
        max_delta = min(i, len(grid) - 1 - i - 1) 
        block1 = grid[i - max_delta: i + 1][::-1]
        block2 = grid[i+1:i+1 + max_delta +1]
        diff = sum(line_diff(block1[_], block2[_]) for _ in range(len(block1)))
        if diff == 1:
            return {i+1}
    return {}

def solve(fn):
    axis_value = 0
    for i, grid in enumerate(grids):
        axis_h = fn(grid)
        if not axis_h:
            axis_v = fn(list(zip(*grid)))
            if DEBUG: print("Vertical:", axis_v)
        else: 
            if DEBUG: print("Horizontal:", axis_h)
            axis_v = {}
        add_value = sum(100 * _ for _ in axis_h) + sum(axis_v)
        axis_value += add_value
        assert add_value > 0
        if DEBUG: print("Grid", i, " - ", add_value)
    return axis_value


print("Part 1: ", solve(get_axis))
print("Part 2: ", solve(get_smudged_axis))

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
