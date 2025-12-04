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
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")


def part1():
    free = set()
    nodes = set([(c, r) for r, line in enumerate(inputs) for c, char in enumerate(line) if char == "@"])
    for c, r in nodes:
        adj = {(c + a, r + b) for a, b in [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (1, 1)]}
        matches = adj & nodes
        if len(matches) < 4:
            free.add((c, r))
    return len(free)


def part2():
    nodes = set([(c, r) for r, line in enumerate(inputs) for c, char in enumerate(line) if char == "@"])
    free = set()
    while nodes:
        removed = False
        for c, r in nodes:
            adj = {(c + a, r + b) for a, b in [(-1, -1), (-1, 0), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 0), (1, 1)]}
            matches = adj & nodes
            if len(matches) < 4:
                free.add((c, r))
                removed = True
        nodes -= free
        if not removed:
            return len(free)


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
