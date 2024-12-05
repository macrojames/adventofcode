#!/usr/bin/env python3
import time
import os.path
from util import read_input_raw
import colorama
from collections import defaultdict
from functools import cmp_to_key
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_raw(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

rules_raw, reports_raw = inputs.split("\n\n")
rules_list = [tuple(e.split("|")) for e in rules_raw.split("\n")]
reports = [e.split(",") for e in reports_raw.split("\n")]
rules = defaultdict(set)
for l, r in rules_list:
    rules[l].add(r)

def is_valid(report):
    for i, page in enumerate(report):
        rest = set(report[i+1:])
        if rest - rules[page]:
            return False
    return True

def sorter(a, b):
    if b in rules[a]: return -1
    else: return 1   

def part1():
    return [rep[len(rep)//2] if is_valid(rep) else 0 for rep in reports]
def part2():
    return [0 if is_valid(rep) else sorted(rep, key=cmp_to_key(sorter))[len(rep)//2] for rep in reports]

print("Part 1: ", p := part1(), sum(map(int, p)))
print("Part 2: ", p := part2(), sum(map(int, p)))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

