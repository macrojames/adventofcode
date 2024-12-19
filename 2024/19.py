#!/usr/bin/env python3
from functools import cache
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

towels = sorted([_.strip() for _ in inputs[0].split(",")], key=len)
designs = inputs[2:]

@cache
def find_path(design, early_exit=False):
    paths = 0
    for t in towels:
        if design.startswith(t):
            if len(t) == len(design):
                paths += 1
                if early_exit: return paths
            elif path := find_path(design[len(t):], early_exit=early_exit):
                paths += path
                if early_exit: return paths
    return paths

def part1(early_exit=True):#
    possible = []
    for design in designs:
        if path := find_path(design, early_exit=early_exit):
            possible.append(design)
    return possible

def part2(designs, early_exit=False):#
    possible = 0
    for design in designs:
        if path := find_path(design, early_exit=early_exit):
            possible += path
    return possible

print("Part 1: ", len(good := part1()))
print("Part 2: ", part2(designs=good))


print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

