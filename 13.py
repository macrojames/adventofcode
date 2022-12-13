#!/usr/bin/env python3
import json
import os
import time
from util import read_input_lines, read_input_raw
from functools import cmp_to_key
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_raw(day, SAMPLE)

pairs = [(json.loads(block.split("\n")[0]), json.loads(block.split("\n")[1])) for block in _input.split("\n\n")]
div1 = [[2]]
div2 = [[6]]
part2 = [item for pair in pairs for item in pair] + [div1, div2]

def compare_part2(a,b):
    return 1 if not compare(a,b) else -1

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b
    elif isinstance(a, list) and isinstance(b, list):
        for new_a, new_b in zip(a, b):
            cmp = compare(new_a, new_b)
            if cmp is not None:
                return cmp
        if len(a) == len(b): return None
        return len(a) < len(b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

results1 = [compare(*pair) for pair in pairs]
part1 = sum([i+1 for i,r in enumerate(results1) if r])
print("Part 1: ", part1)

part2.sort(key=cmp_to_key(compare_part2))
print("Part 2: ", (part2.index(div1) + 1) *  (part2.index(div2) + 1) )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
