#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

dirs = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}

def part1():
    pos = (0, 0)
    visited = {pos}
    for c in inputs[0]:
        x, y = pos
        dx, dy = dirs[c]
        pos = (x+dx, y+dy)
        visited.add(pos)
    return len(visited)

def part2():
    pos = [(0, 0)] *2
    visited = [{(0, 0)}] * 2
    for i, c in enumerate(inputs[0]):
        x, y = pos[i % 2]
        dx, dy = dirs[c]
        pos[i % 2] = (x+dx, y+dy)
        visited[i % 2].add(pos[i % 2])
    return len(visited[0] | visited[1])



print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
