#!/usr/bin/env python3
import time
import re
from util import read_input_lines, bfs

start_timer = time.time()

SAMPLE = False
DEBUG = False

inputs_raw = read_input_lines('10', SAMPLE)
inputs = [list(_) for _ in inputs_raw]
MAX_R, MAX_C = len(inputs) - 1, len(inputs[0]) - 1 
baumarkt = {
    '-': [(0, 1), (0, -1)],
    '|': [(-1, 0), (1, 0)],
    'L': [(0, 1), (-1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
}
for r, l in enumerate(inputs):
    if (c := l.index('S') if l.count('S') else -1) > -1:
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
    sym = inputs[r][c]
    if sym == '.': return []
    for dr, dc in baumarkt[sym]:
        if r+dr >= 0 and r+dr <= MAX_R and c+dc >=0 and r+dr <= MAX_C:
            connected.append((r+dr, c+dc))
    return connected

def part1(start):
    costs = {}
    visited =  bfs(start, get_connected, exclude=[], costs=costs)
    return costs

def part2(start):
    visited =  bfs(start, get_connected, exclude=[])
    all_r = [r for r,c in visited]
    inside = []
    for r in range(min(all_r) + 1, max(all_r)):
        row_c = [c for _,c in visited if _ == r]
        for c in range(min(row_c) + 1, max(row_c)):
            if (r, c) not in visited:
                col_r = [r for r,_ in visited if _ == c]

                lefts = [inputs[r][dc] for dc in row_c if dc < c]  
                tops = [inputs[dr][c] for dr in col_r if dr < r]  
                #   
                #F----7
                #|F-7.|     3u 1o
                #LJ.L-J     0u 2o
                delta_r = {'|': 0, '.': 0, '-': 0, 'F': 1, '7': 1, 'J': -1, 'L': -1}
                delta_c = {'|': 0, '.': 0, '-': 0, 'F': 1, '7': -1, 'J': -1, 'L': 1}
                row_lower_half = sum(lefts.count(_) for _ in ['|', 'F', '7'])
                row_upper_half = sum(lefts.count(_) for _ in ['|', 'J', 'L'])
                col_left_half  = sum(tops.count(_) for _ in ['-', 'J', '7'])
                col_right_half = sum(tops.count(_) for _ in ['-', 'F', 'L'])
                if row_lower_half % 2 and row_upper_half % 2 and col_left_half % 2 and col_right_half % 2:
                    inside.append((r, c))
    return inside

print("Part 1: ", max(part1(start).values()))
print("Part 2: ", len(part2(start)))  


print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
