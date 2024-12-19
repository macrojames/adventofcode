#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from collections import Counter, defaultdict
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")


def parts(num=25):
    state = [int(_) for _ in inputs[0].split(" ")]
    current = Counter(state)
    stones = 0
    for i in range(num):
        updates = Counter()
        updates[1] = current[0]
        for n in current.keys():
            if n == 0: continue
            mid, rem = divmod(len(str(n)), 2)
            if mid >= 1 and rem == 0:
                updates[int(str(n)[:mid])] += current[n]
                updates[int(str(n)[mid:])] += current[n]
            else:
                updates[n * 2024] += current[n]
        current = updates
    return current

print("Part 1: ", sum(parts(25).values()))
print("Part 2: ", sum(parts(75).values()))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

