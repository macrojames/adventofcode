#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from collections import Counter

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

def is_nice(s):
    c = Counter(s)
    if sum(c.get(_, 0) for _ in 'aeiou') < 3: return False
    if not any(s[_] == s[_+1] for _ in range(len(s) - 1)): return False
    if any(_ in s for _ in ['ab', 'cd', 'pq', 'xy']): return False
    print(s, "is nice")
    return True

def is_nicer(s: str):
    if not any(s.count(s[_:_+2], _+2) for _ in range(len(s) - 2)): return False
    if not any(s[_] == s[_+2] and s[_] != s[_+1] for _ in range(len(s) - 2)): return False
    print(s, "is nicer")
    return True

def part1():
    return sum(1 if is_nice(s) else 0 for s in inputs)

def part2():
    return sum(1 if is_nicer(s) else 0 for s in inputs)


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
