#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

letters = {k:set() for k in "XMAS"}

for y, line in enumerate(inputs):
    for x, c in enumerate(line):
        letters[c].add((y,x))


def part1():
    match = []
    for cy, cx in letters["X"]:
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if (cy + 1*dy, cx + 1*dx) in letters["M"] and \
                   (cy + 2*dy, cx + 2*dx) in letters["A"] and \
                   (cy + 3*dy, cx + 3*dx) in letters["S"]:
                    match.append((cy, cx))
    return len(match)

def part2():
    match = []
    for cy, cx in letters["A"]:
        adj = set([(cy -1, cx -1), (cy + 1, cx + 1), (cy + 1, cx -1), (cy -1, cx + 1)])
        m = adj & letters["M"]
        s = adj & letters["S"]
        if len(m) == 2 and len(s) == 2:
            lm = list(m)
            if lm[0][0] == lm[1][0] or lm[0][1] == lm[1][1]:
                # nicht diago
                match.append((cy, cx))
    return len(match)


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

