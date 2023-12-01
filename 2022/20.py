#!/usr/bin/env python3
from copy import copy
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False
DEBUG = False

ENCRYPTION = 811589153

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

def mix(_input, encryption=1, cycles=1):
    base = [int(_.strip()) * encryption for _ in _input]
    mapping = {i: v for i, v in enumerate(base)}    # Unique values to push around
    target = list(mapping.keys())

    def translate(target, mapping):
        return [mapping[_] for _ in target]
    for cycle in range(cycles):
        for i, v in enumerate(base):
            target_pos = target.index(i)
            target_new_pos = target_pos + v
            if target_new_pos == 0: target_new_pos = len(base) - 1
            if target_new_pos > len(base) - 1 or target_new_pos < 0: target_new_pos = target_new_pos % (len(base) -1)
            target.pop(target_pos)
            target.insert(target_new_pos, i)

            if DEBUG:
                print(f"{v} moves\n{translate(target, mapping)}\n")

    zero_map = list(mapping.keys())[list(mapping.values()).index(0)]
    zero_index = target.index(zero_map)
    groves = 0
    for grove in [1000,2000,3000]:
        idx = (grove + zero_index) % len(base)
        groves += translate(target, mapping)[idx]
    return groves

print("Part 1: ", mix(_input))
print("Part 2: ", mix(_input, encryption=ENCRYPTION, cycles=10))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")


