#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
import re
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

def part1():
    text = "".join(inputs)
    groups = re.findall("mul\\((\d{1,3}),(\d{1,3})\\)", text)
    result = 0
    for l, r in groups:
        result += int(l) * int(r)
    return result


def part2():
    mode = 'do()'
    text = "".join(inputs)
    groups = re.findall("(don't\\(\\)|do\\(\\))|mul\\((\d{1,3}),(\d{1,3})\\)", text)
    result = 0
    for cmd, l, r in groups:
        if cmd:
            mode = cmd
            continue
        if mode == 'do()':
            result += int(l) * int(r)
    return result

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

