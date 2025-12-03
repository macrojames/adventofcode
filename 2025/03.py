#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

def part1():
    sum = 0
    for line in inputs:
        d1, d2 = 0, 0
        l, r = 0, len(line)
        d1 = max(line[l: r-1])
        l = line.find(d1) + 1
        d2 = max(line[l: r])
        sum += (10* int(d1)) + int(d2)
    return sum

def part2():
    sum = 0
    for line in inputs:
        digits = []
        l, r = 0, len(line)
        for i in range(12):
            digits.append(max(line[l: r-(11-i)]))
            l = line.find(digits[-1], l) + 1
        num = "".join(digits)
        sum += int(num)
    return sum

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

