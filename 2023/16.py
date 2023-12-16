#!/usr/bin/env python3
from collections import deque
import time
import os.path
from util import read_input_lines, dirs, in_bounds

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

deflectors = dict()
max_r, max_c = len(inputs) - 1, len(inputs[0]) -1
for r, row in enumerate(inputs):
    for c, char in enumerate(row):
        if char != '.':
            deflectors[(r, c)] = char

def part1(beams):
    encounters = set()
    tiles = dict()
    while beams:
        r, c, d = beams.popleft()
        if (r, c, d) in encounters:
            continue
        if (r, c) not in tiles: 
            tiles[(r,c)] = 1
        encounters.add((r,c,d))

        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc

        if (nr, nc) in deflectors:
            deflection = deflectors.get((nr, nc))
            if deflection == '/': 
                d = {'N': 'E', 'S': 'W', 'W': 'S', 'E': 'N'}[d]
                beams.append((nr, nc, d))
            elif deflection == '\\':
                d = {'N': 'W', 'S': 'E', 'W': 'N', 'E': 'S'}[d]
                beams.append((nr, nc, d))
            elif deflection == '-':
                if d in ['W', 'E']:
                    beams.append((nr, nc, d))
                else:
                    beams.append((nr, nc, 'W'))
                    beams.append((nr, nc, 'E'))
            elif deflection == '|':
                if d in ['N', 'S']:
                    beams.append((nr, nc, d))
                else:
                    beams.append((nr, nc, 'N'))
                    beams.append((nr, nc, 'S'))
        elif in_bounds(nc, nr, max_r, max_c):
            beams.append((nr, nc, d))
        else:
            # Beam left the pattern
            #print("Beam left @", r, c, d)
            continue
    #print_grid(tiles)
    return len(tiles)


def print_grid(tiles):
    for r, line in enumerate(inputs):
        for c, _ in enumerate(line):
            if (r, c) in deflectors: char = deflectors[(r, c)]
            elif (r, c) in tiles: char = '#'
            else: char = '.'
            print(char, end="")
        print()

def part2():
    m = 0
    for r in range(max_r + 1):
        beams = deque([(r, 0, "E")])
        step = part1(beams)
        m = max(step, m)
        beams = deque([(r, max_c, "W")])
        step = part1(beams)
        m = max(step, m)
    for c in range(max_c + 1):
        beams = deque([(0, c, "S")])
        step = part1(beams)
        m = max(step, m)
        beams = deque([(max_r, c, "N")])
        step = part1(beams)
        m = max(step, m)

    return m

start = [(0,0, "E")] if (0, 0) not in deflectors else [(0,0, "S") if deflectors[(0,0)] in ['|', '\\'] else (0,0,'N')]
beams = deque(start)
p1 = part1(beams)

assert p1 == 46 if SAMPLE else 7185, f"{p1=}"    # falsche Antwort
print("Part 1: ", p1)

p2 = part2()
assert p2 == 51 if SAMPLE else 7616, f"{p2=}"    # falsche Antwort
print("Part 2: ", p2)

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
