#!/usr/bin/env python3
import os
from util import read_input_lines, read_input_raw

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_raw(day, SAMPLE)
blocks = _input.split("\n\n")

sum_elves = [sum([int(piece) for piece in carry.split("\n")]) for carry in blocks]

print("Part 1: ", max(sum_elves))
print("Part 2: ", sum(sorted(sum_elves)[-3:]))


