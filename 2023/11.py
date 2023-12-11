#!/usr/bin/env python3
import time
import re
from util import read_input_lines, bfs
from itertools import combinations

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines('11', SAMPLE)
grid = [list(r) for r in inputs]
MAX_R, MAX_C = len(inputs) - 1, len(inputs[0]) - 1 

galaxies = set()
travels = {}
expandable_rows, expandable_cols = [], []
for r, row in enumerate(grid):
    for c, _ in enumerate(row):
        if grid[r][c] == '#': galaxies.add((r, c))
    if row.count('#') == 0: expandable_rows.append(r)

for c, col in enumerate(list(map(list, zip(*grid)))):    # https://stackoverflow.com/questions/6473679/transpose-list-of-lists
    if col.count('#') == 0: expandable_cols.append(c)

def part1(expand_factor=1):
    for path in combinations(galaxies, r=2):
        (r1, c1), (r2,c2) = path
        dr = abs(r2 - r1)
        dc = abs(c2 - c1)
        expanded_r = [expand_factor -1 for _ in expandable_rows if min(r1, r2) < _ < max(r1, r2)]
        expanded_c = [expand_factor -1 for _ in expandable_cols if min(c1, c2) < _ < max(c1, c2)]
        travels[path] = dr + dc  + sum(expanded_r) + sum(expanded_c)
    return travels

travels = part1(2)

print("Part 1: ", sum(travels.values()))
travels = part1(1000000)

print("Part 2: ", sum(travels.values()))

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
