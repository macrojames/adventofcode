#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
from itertools import batched
from collections import deque
from math import sqrt, ceil, floor, prod

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines('06', SAMPLE)

times = map(int, re.findall("(\\d+)", inputs[0]))
times2 = map(int, re.findall("(\\d+)", inputs[0].replace(" ", "")))
dists = map(int, re.findall("(\\d+)", inputs[1]))
dists2 = map(int, re.findall("(\\d+)", inputs[1].replace(" ", "")))

def part1(times, dists):
    a = 1
    sol = []
    for t, d in zip(times, dists):
        # acceleration_time * acceleration * travel_time > dist
        # acceleration_time + travel_time = t    => travel_time = t - acceleration_time
        # Mit Wolframalpha umstellen
        at1 = 0.5 * (t - sqrt(a*t*t - 4 * d) / sqrt(a))
        at2 = 0.5 * (sqrt(a*t*t - 4 * d) / sqrt(a) + t)
        sol.append((ceil(at1), floor(at2)))
    return sol

print("Part 1: ", prod([1 + s[1] - s[0] for s in part1(times, dists)]))
print("Part 2: ", prod([1 + s[1] - s[0] for s in part1(times2, dists2)]))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
