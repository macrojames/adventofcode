#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)[0]


def part1():
    return inputs.count("(") - inputs.count(")")


print("Part 1: ", part1())
#print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
