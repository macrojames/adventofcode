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

def part1():
    visited = set()
    facing = 0
    r, c = start
    while 0 <= r < len(inputs) and 0 <= c < len(inputs[0]):
        visited.add((r, c))
        
        nr, nc = r + dirs[facing][0], c + dirs[facing][1]
        if (nr, nc) in blocks:
            facing = (facing + 1) % 4
            nr, nc = r + dirs[facing][0], c + dirs[facing][1]
        else:
            r, c = nr, nc

    return len(visited)



print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

