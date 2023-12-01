#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
from math import prod
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

visible = set()
grid = [[int(c) for c in line] for line in _input]


# oben nach unten
for x in range(len(grid[0])):
    size = -1
    for y in range(len(grid)):
        if grid[y][x] > size:
            size = grid[y][x]
            visible.add((y,x))
        if size == 9:
            break

# unten nach oben
for x in range(len(grid[0])):
    size = -1
    for y in range(len(grid) - 1, - 1, -1):
        if grid[y][x] > size:
            size = grid[y][x]
            visible.add((y,x))
        if size == 9:
            break

# links nach rechts
for y in range(len(grid)):
    size = -1
    for x in range(len(grid[y])):
        if grid[y][x] > size:
            size = grid[y][x]
            visible.add((y,x))
        if size == 9:
            break

# rechts nach links
for y in range(len(grid)):
    size = -1
    for x in range(len(grid[0]) - 1, - 1, -1):
        if grid[y][x] > size:
            size = grid[y][x]
            visible.add((y,x))
        if size == 9:
            break

max_view = 0
for y, row in enumerate(grid):
    for x, size in enumerate(row):
        current_view = [0, 0, 0, 0]     # links, rechts, oben, unten
        for i in range(1, x + 1):
            current_view[0] += 1
            if row[x-i] >= size:
                break
        
        for i in range(x + 1, len(row)):
            current_view[1] += 1
            if row[i] >= size:
                break
        
        for i in range(1, y + 1):
            current_view[2] += 1
            if grid[y-i][x] >= size:
                break

        for i in range(y + 1, len(grid)):
            current_view[3] += 1
            if grid[i][x] >= size:
                break

        if prod(current_view) > max_view:
            print("x: ", x, "y:", y, "view:", current_view, "prod:", prod(current_view))
            max_view = prod(current_view)


print("Part 1: ", len(visible))
print("Part 2: ", max_view)
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
