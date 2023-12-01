#!/usr/bin/env python3
import os
import time
from parse import parse
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

elves = [parse("{:d}-{:d},{:d}-{:d}", _).fixed for _ in _input]

overlaps, overlaps2 = 0,0 
for e in elves:
    a = set(list(range(e[0], e[1] + 1)))
    b = set(list(range(e[2], e[3] + 1)))
    overlaps += len( a | b) == max(len(a), len(b)) 
    overlaps2 += len( a | b) != len(a) + len(b) 

print("Part 1: ", overlaps)
print("Part 2: ",overlaps2 )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
