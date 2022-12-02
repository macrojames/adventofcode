#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = True

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

print("Part 1: ", )
print("Part 2: ", )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
