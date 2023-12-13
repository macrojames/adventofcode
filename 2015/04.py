#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from hashlib import md5

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)


def part1():
    key = inputs[0]
    hash = ""
    i = -1
    while not hash.startswith("00000"):
        i += 1
        hash = md5(f"{key}{i}".encode()).hexdigest()
        assert i < 1e7
    return i, hash

def part2():
    key = inputs[0]
    hash = ""
    i = -1
    while not hash.startswith("000000"):
        i += 1
        hash = md5(f"{key}{i}".encode()).hexdigest()
        assert i < 1e7
    return i, hash

print("Part 1: ", ret := part1())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s, {round(ret[0]/(time.time() - start_timer), 3)} hashes/s")

start_timer = time.time()
print("Part 2: ", ret2 := part2())
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s, {round(ret[0]/(time.time() - start_timer), 3)} hashes/s")

