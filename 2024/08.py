#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from collections import defaultdict
from itertools import combinations, permutations
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

antennas = defaultdict(set)
max_r = len(inputs) - 1
max_c = len(inputs[0]) - 1

for r, row in enumerate(inputs):
    for c, letter in enumerate(row):
        if letter == '.': continue
        antennas[letter].add((r, c))

def part1():
    antinodes = set()
    for letter, nodes in antennas.items():
        for (r1, c1), (r2, c2) in permutations(nodes, 2):  #combinations -> mirror up und down. permutations, vertauscht die deltas?!
            dr, dc = r1 - r2, c1 - c2
            anr, anc = (r1 + dr, c1 + dc)
            if 0 <= anr <= max_r and 0 <= anc <= max_c:
                antinodes.add((anr, anc))
    return antinodes

def part2():
    antinodes = set()
    for letter, nodes in antennas.items():
        for (r1, c1), (r2, c2) in permutations(nodes, 2):  #combinations -> mirror up und down. permutations, vertauscht die deltas?!
            dr, dc = r1 - r2, c1 - c2
            for i in range(1000):
                anr, anc = (r1 + i*dr, c1 + i*dc)
                if 0 <= anr <= max_r and 0 <= anc <= max_c:
                    antinodes.add((anr, anc))
                else:
                    break
    return antinodes

print("Part 1: ", len(part1()))
print("Part 1: ", len(part2()))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

