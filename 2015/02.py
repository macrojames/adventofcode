#!/usr/bin/env python3
from math import prod
import time
import os.path
from util import read_input_lines

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

# 2*l*w + 2*w*h + 2*h*l

def part1():
    s = 0
    for present in inputs:
        l, w, h  = map(int, present.split("x"))
        s += 2*l*w + 2*w*h + 2*h*l
        s += min(l*w, w*h, h*l)
    return s

def part2():
    s = 0
    for present in inputs:
        p = list(map(int, present.split("x")))
        _1, _2 = sorted(p)[:2]
        s += 2 * _1 + 2 * _2
        s += prod(p)
    return s

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
