#!/usr/bin/env python3
import os
import time
from parse import parse
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_raw(day, SAMPLE).splitlines()

cut = _input.index('')
stacks_raw = _input[:cut]
movements = _input[cut+1:]

def filter_list(it):
    return list(filter(lambda x: (x != ' '), it))

stacks = list(map(filter_list, zip(*reversed([row[1::4] for row in stacks_raw[:-1]]))))

for m in movements:
    amount, src, dst = parse("move {:d} from {:d} to {:d}", m)
    for _ in range(amount):
        stacks[dst-1].append(stacks[src-1].pop())

print("Part 1: ", "".join([s[-1] for s in stacks]))

stacks = list(map(filter_list, zip(*reversed([row[1::4] for row in stacks_raw[:-1]]))))

for m in movements:
    amount, src, dst = parse("move {:d} from {:d} to {:d}", m)
    stacks[dst-1].extend(stacks[src-1][-amount:])
    del stacks[src-1][-amount:]

print("Part 2: ", "".join([s[-1] if s else "" for s in stacks]))
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
