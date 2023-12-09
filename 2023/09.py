#!/usr/bin/env python3
import time
import re
from util import read_input_lines
import numpy as np

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines('09', SAMPLE)

seqs = [np.array([int(x) for x in  _.split(" ")]) for _ in inputs]


def part1(seqs, idx=-1, left=False):
    results = []
    for seq in seqs:
        diffs = []
        i = 0
        while sum(diff := np.diff(seq, n=i)) != 0:
            i += 1
            diffs.append(diff[idx])
        if not left: 
            results.append(sum(diffs))
        else:
            diffs = np.array(diffs)
            diffs[1::2] *= -1   # negate every second
            results.append(sum(diffs))
    return results


print("Part 1: ", sum(part1(seqs, -1)))
print("Part 2: ", sum(part1(seqs, 0, left=True)))


print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
