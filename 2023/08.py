#!/usr/bin/env python3
import time
import re
from util import read_input_lines

start_timer = time.time()

SAMPLE = False
DEBUG = True

inputs = read_input_lines('08' if not SAMPLE else '08-2', SAMPLE)

instructions = [0 if _=='L' else 1 for _ in inputs[0]]
mapping = {
    _.split("=")[0].strip(): re.match("\\(([A-Z0-9]{3}), ([A-Z0-9]{3})\\)", _.split("=")[1].strip()).groups()
for _ in inputs[2:]}


def route(s, e):
    start = mapping[s]
    end = mapping[e]
    current = start
    pointer = 0
    while current != end:
        instruction = instructions[pointer % len(instructions)]
        current = mapping[current[instruction]]
        pointer += 1
    return pointer

def part1(s, e):
    return route(s,e)


def part2():
    starts = [_ for _ in mapping.keys() if _.endswith('A')]
    ends = set([_ for _ in mapping.keys() if _.endswith('Z')])
    currents = [_ for _ in starts]

    pointer = 0
    while set(currents) - set(ends):
        instruction = instructions[pointer % len(instructions)]
        for i, current_node in enumerate(currents):
            currents[i] = mapping[current_node][instruction]
        pointer += 1
        if DEBUG and pointer <= 10 or pointer % 1024 == 0:
            print(f"Step {pointer}: {currents}")

    return pointer

#print("Part 1: ", part1("AAA", "ZZZ"))  
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
