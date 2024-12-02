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
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")


def is_safe(report):
    mode = ""
    for i, l in enumerate(report[:-1]):
        r = report[i+1]
        if r - l < -3:  return "--"
        elif r - l > 3:  return "++"
        elif r - l < 0:
            if mode == "+": return "+-"
            else: mode = "-"
        elif r - l > 0:
            if mode == "-": return "-+"
            else: mode = "+"
        else:  return "=="
    return mode

def is_safe_damped(report):
    cut_report = report
    i = 0
    while (x := is_safe(cut_report)) and x not in ["-", "+"]:
        cut_report = report[:i] + report [i+1:]
        i += 1
        if i > len(report):
            return "~~"
    return x

    
def part1():
    reports = [list(map(int, line.split(" "))) for line in inputs]
    finals = [is_safe(report) for report in reports]
    return Counter(finals)

def part2():
    reports = [list(map(int, line.split(" "))) for line in inputs]
    finals = [is_safe_damped(report) for report in reports]
    return Counter(finals)

result = part1()
print("Part 1: ", result["+"] + result["-"])
result = part2()
print("Part 2: ", result["+"] + result["-"])

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

