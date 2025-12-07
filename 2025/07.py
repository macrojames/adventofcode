#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines, find_all
from functools import cache
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

beams = {0: [inputs[0].find("S")], 1: [inputs[0].find("S")]}
height = len(inputs)

splitters = []

for r, line in enumerate(inputs):
    splitters.append(list(find_all(line, "^")))


def part1():
    splits = 0
    for r in range(1, height - 1):
        beams[r + 1] = list()
        for beam in set(beams[r]):
            if beam in splitters[r + 1]:
                beams[r + 1].append(beam - 1)
                beams[r + 1].append(beam + 1)
                splits += 1
            else:
                beams[r + 1].append(beam)
    return splits, beams


splits, beams = part1()
print("Part 1: ", splits)


@cache
def get_to(point):
    global beams
    ways = 0
    r, c = point
    if c not in beams[r]:
        return 0
    if r < 1:
        return 1
    if not splitters[r]:
        # skip useless lines
        return get_to((r - 1, c))

    if c + 1 < len(inputs[0]) and c + 1 in beams[r - 1] and c + 1 in splitters[r]:
        ways += get_to((r - 1, c + 1))
    if c - 1 >= 0 and c - 1 in beams[r - 1] and c - 1 in splitters[r]:
        ways += get_to((r - 1, c - 1))
    if c in beams[r - 1]:
        ways += get_to((r - 1, c))

    return ways


def part2(beams):
    return sum([get_to((height - 1, i)) for i in range(len(inputs[0]))])


print("Part 2: ", part2(beams))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
