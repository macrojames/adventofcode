#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)[0]

i = 2
while len(set(_input[i:i+4])) < 4:
    i += 1
j = 0
while len(set(_input[j:j+14])) < 14:
    j += 1

print("Part 1: ", i + 4)
print("Part 2: ", j + 14) 
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
