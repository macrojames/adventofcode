#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
from collections import Counter

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")


def part1():
    intervals = [tuple(interval.split("-")) for interval in inputs[0].split(",")]
    invalids = 0
    for bottom, top in intervals:
        for i in range(int(bottom), int(top) + 1):
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                invalids += i
    return invalids

def part2():
    intervals = [tuple(interval.split("-")) for interval in inputs[0].split(",")]
    invalids = 0
    for bottom, top in intervals:
        for i in range(int(bottom), int(top) + 1):
            s = str(i)
            for splitter in [2,3,5,7,11,13,17]:
                if splitter > len(s): break
                if len(s) % splitter != 0: continue
                sz = len(s) // splitter
                parts = [s[_*sz:(_+1)*sz] for _ in range(len(s)//sz)]
                if len(set(parts)) == 1:
                    invalids += i
                    break
    return invalids


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
