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
    current = 50
    counter = 0
    for instruction in inputs:
        d = instruction[0]
        num = int(instruction[1:])
        if d == 'L': current -= num
        elif d == 'R': current += num
        current %= 100
        if current == 0: counter += 1
    return counter

def part2():
    current = 50
    counter = 0
    for instruction in inputs:
        d = instruction[0]
        num = int(instruction[1:])
        old = current
        if d == 'L': current -= num
        elif d == 'R': current += num

        print(f"{old} -> {current} by {d}{num}")
        print(f"{abs(current) // 100} {current % 100} => ", end="")
        steps = abs(current) // 100
        if old > 0 and current <=0:
            steps += 1
        counter += steps
        current %= 100
        print(f" +{steps} = {counter}")
    return counter

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

