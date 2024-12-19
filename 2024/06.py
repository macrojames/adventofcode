#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines, get_indices
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
blocks = set()

for y, row in enumerate(inputs):
    for column in get_indices(row, "#"):
        blocks.add((y, column))
    if (column := row.find("^")) > 0:
        start = (y, column)

class LoopException(Exception):
    pass

def part1(blocks = set()):
    r, c = start
    facing = 0
    visited = set()
    visited_dir = set()
    while 0 <= r < len(inputs) and 0 <= c < len(inputs[0]):
        if (r, c, facing) in visited_dir:
            raise LoopException
        visited.add((r, c))
        visited_dir.add((r, c, facing))
        nr, nc = r + dirs[facing][0], c + dirs[facing][1]
        if (nr, nc) in (blocks):
            facing = (facing + 1) % 4
            nr, nc = r + dirs[facing][0], c + dirs[facing][1]
        else:
            r, c = nr, nc
    return visited

def part2(visited=set()):
    blockers = set()
    for r, c in visited:
        if (r, c) == start: continue
        try:
            _ = part1(blocks = blocks | {(r ,c)})
        except LoopException:
            blockers.add((r, c))

    return blockers

print("Part 1: ", len(visited := part1(blocks=blocks)))
print("Part 2: ", len(part2(visited=visited)))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

