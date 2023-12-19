#!/usr/bin/env python3
from math import prod
from pprint import pprint
import time
import os.path
from util import read_input_lines
import colorama
import re
from itertools import product, chain

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

# hdj{m>838:A,pv}
ruleset = {}
parts_a = []
for line in inputs:
    if m := re.match("(\w+)\{(.+)\}", line):
        ruleset[m[1]] = m[2].split(",")
    elif m := re.match("{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line):
        parts_a.append({"x": int(m[1]), "m": int(m[2]), "a": int(m[3]), "s": int(m[4])})
    else:
        # newline
        pass

def next_rule(part: dict, rules:list[str]) -> tuple:
    for rule in rules:
        try:
            cond, target = rule.split(":")
        except:
            # Final rule
            return rule, True
        key, op, value = re.match("(\w)([<>])(\d+)", cond).groups()
        if op == '<' and part[key] < int(value):
            return target, False
        elif op == '>' and part[key] > int(value):
            return target, False
        else:
            pass
    raise RuntimeError("No Rule accepted")

def get_result(part):
    current_rule = 'in'
    while current_rule not in ['A', 'R']:
        current_rule, _ = next_rule(part, ruleset[current_rule])
    return current_rule


def part1(parts):
    results = []
    for part in parts:
        results.append(get_result(part))
    return sum([sum(_.values()) for i, _ in enumerate(parts) if results[i] == 'A'])


def part2():

    def resolve_ranges(ranges, current_rule = 'in'):
        def combis(ranges):
            return prod(_[1] + 1 - _[0] for _ in ranges.values())

        if current_rule == 'R': return 0
        if current_rule == 'A': return combis(ranges)

        c = 0
        for rule in ruleset[current_rule]:
            if rule.count(":") == 0:
                # No condition
                c += resolve_ranges(ranges, rule)
                continue

            cond, target = rule.split(":")
            key, op, value = re.match("(\w)([<>])(\d+)", cond).groups()
            value = int(value)
            # muss evtl slicen.
            x0, x1 = ranges[key]
            if op == '<':
                good = (x0, value - 1)
                bad = (value, x1)
            else:
                good = (value + 1, x1)
                bad = (x0, value)
            if good[0] <= good[1]:      # valide Sortierung
                temp = ranges.copy()
                temp[key] = good
                c += resolve_ranges(temp, target)
            if bad[0] <= bad[1]:
                # mismatch bleibt in den ranges
                ranges[key] = bad
            else: 
                break
        return c

    
    ranges = {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}
    return resolve_ranges(ranges, 'in')


print("Part 1: ", part1(parts_a))
range_mul = part2()
print("Part 2: ", range_mul)

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

