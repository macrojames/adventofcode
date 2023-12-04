#!/usr/bin/env python3
import time
import re
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

splitter = re.compile(".*: ([\\d ]+) \\| ([\\d ]+)")
inputs = read_input_lines('04', SAMPLE)

winners = []
picks = []
copies = [1] * len(inputs)

for line in inputs:
    m = re.findall(splitter, line)
    if m:
        winners.append(set(int(x) for x in m[0][0].split(" ") if x))
        picks.append(set(int(x) for x in m[0][1].split(" ") if x))
    scores = [len(winners[i] & picks[i]) for i in range(len(picks))]

def part1():
    return sum([2**(x-1) for x in scores if x >= 1])

def part2():
    for i, s in enumerate(scores):
        if s > 0:   # range = s
            c = copies[i]   # count
            for j in range(i + 1, i + s + 1):
                if j >= len(copies):
                    break
                copies[j] += c
    return sum(copies)


print("Part 1: ", part1())
print("Part 2: ", part2())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


