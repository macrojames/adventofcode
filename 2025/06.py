#!/usr/bin/env python3
from math import prod
import time
import os.path
from util import read_input_lines_no_strip
import colorama

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines_no_strip(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")


def part1():
    nums = []
    for line in inputs[:-1]:
        nums.append(list(map(int, line.split())))

    operators = inputs[-1].split()
    total = 0
    for i, op in enumerate(operators):
        if op == "+":
            total += sum([row[i] for row in nums])
        elif op == "*":
            total += prod([row[i] for row in nums])
    return total


def part2():
    total = 0
    block_starts = []
    operators = []
    for i, op in enumerate(inputs[-1]):
        if op in ["+", "*"]:
            block_starts.append(i)
            operators.append(op)
    for i, start in enumerate(block_starts):
        end = block_starts[i + 1] - 1 if i + 1 < len(block_starts) else len(inputs[-1])
        strings = [line[start:end] for line in inputs[:-1]]
        nums = list(map(int, ("".join(_) for _ in zip(*strings))))
        if operators[i] == "+":
            total += sum(nums)
        elif operators[i] == "*":
            total += prod(nums)
    return total


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
