#!/usr/bin/env python3
from collections import OrderedDict
import time
import os.path
from util import read_input_lines

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)[0]


def hasch(s):
    cv = 0
    for c in s:
        cv += ord(c) 
        cv *= 17
        cv %= 256
    return cv



def part1():
    t = 0
    for block in inputs.split(","):
        t += hasch(block)
    return t

def part2():
    boxes = {k: OrderedDict() for k in range(256)}
    for block in inputs.split(","):
        name = block.split("-")[0].split("=")[0]
        k = hasch(name)
        if "=" in block:
            focal = block.split("=")[1]
            boxes[k][name] = int(focal)
        elif "-" in block:
            if name in boxes[k]:
                del boxes[k][name]
        else: raise RuntimeError("Unexpected")

        # Focusing power
        s = 0
        for i in range(len(boxes)):
            if not boxes[i]: continue
            for slot, (h, focal) in enumerate(boxes[i].items()):
                s += ((i + 1) * (slot+1) * focal)

    return s

assert hasch('HASH') == 52

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
