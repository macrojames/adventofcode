#!/usr/bin/env python3
import time
import re
from util import read_input_lines, bfs
import numpy as np

start_timer = time.time()

SAMPLE = True
DEBUG = True

inputs_raw = read_input_lines('10', SAMPLE)
inputs = [list(_) for _ in inputs_raw]
MAX_R, MAX_C = len(inputs) - 1, len(inputs[0]) - 1 
baumarkt = {
    '|': [(0, 1), (0, -1)],
    '-': [(-1, 0), (1, 0)],
    'L': [(0, 1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}
for r, l in enumerate(inputs):
    if (c := l.count('S') and l.index('S') or -1) > -1:
        start = (r, c)
        top, bottom, left, right = False, False, False, False
        top = inputs[r-1][c] in ['|', '7', 'F']
        bottom = inputs[r+1][c] in ['|', 'L', 'J']
        left = inputs[r][c-1] in ['-', 'L', 'F']
        right = inputs[r][c+1] in ['-', 'J', '7']
        if top and bottom: start_val = '|'
        elif top and left: start_val = 'J'
        elif top and right: start_val = 'L'
        elif bottom and left: start_val = '7'
        elif bottom and right: start_val = 'F'
        elif left and right: start_val = '-'
        inputs[r][c] = start_val
assert start

def get_connected(pos):
    connected = []
    r, c = pos
    for dr, dc in baumarkt[inputs[r][c]]:
        if r+dr >= 0 and r+dr <= MAX_R and c+dc >=0 and r+dr <= MAX_C:
            connected.append((r+dr, c+dc))
    return connected

def part1(start):
    costs = {}
    visited =  bfs(start, get_connected, exclude=[], costs=costs)
    return costs


print("Part 1: ", costs:=part1(start))
for r in range(MAX_R + 1):
    for c in range(MAX_C + 1):
        print(costs.get((r,c), '.'))
#print("Part 2: ", part1())


print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
