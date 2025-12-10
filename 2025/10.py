#!/usr/bin/env python3
from functools import cache, reduce
import operator
import time
import os.path
from util import read_input_lines
from itertools import combinations, combinations_with_replacement
reduce
import colorama
import re
import heapq

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")
#[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
config = []
for line in inputs:
    matches = re.findall(r"\[([\.#]+)\] ([\(\)\d, ]+) \{(.+)\}", line)
    lights, raw_switches, raw_joltage =  matches[0]
    switches, switches_list, joltage = [], [], 0
    for switch in raw_switches.split(" "):
        int_s = 0
        for n in re.findall(r"\d+", switch):
            int_s += 2**int(n)
        switches.append(int_s)
    int_s = 0
    
    joltage=tuple(map(int, re.findall(r"\d+", raw_joltage)))
    for switch in raw_switches.split(" "):
        s = [0]*len(joltage)
        for n in re.findall(r"\d+", switch):
            s[int(n)] = 1
        switches_list.append(tuple(s))
    
    config.append({
        "light": int("0b" + lights.replace(".", "0").replace("#", "1")[::-1], 2),
        "switches": switches,
        "switches_list": switches_list,
        "joltage": joltage
    })

def part1():
    total = 0
    for c in config:
        i = 1
        while True:
            if any((c.get("light") == reduce(operator.xor, combi) for combi in combinations(c.get("switches"), i))):
                total += i
                break
            i += 1
    return total




def shortest_combination(vectors, target):
    dimension = len(target)
    # Startzustand: (Anzahl Vektoren, aktuelle Summe, Kombination)
    queue = [(0, [0] * dimension, [])]
    visited = set()
    best = None

    while queue:
        count, current_sum, combination = heapq.heappop(queue)
        if tuple(current_sum) == target:
            if best is None or count < best[0]:
                best = (count, combination)
            continue
        if best is not None and count >= best[0]:
            continue
        state = tuple(current_sum)
        if state in visited:
            continue
        visited.add(state)

        for i, v in enumerate(vectors):
            new_sum = [cs + vi for cs, vi in zip(current_sum, v)]
            if all(ns <= t for ns, t in zip(new_sum, target)):
                heapq.heappush(queue, (count + 1, new_sum, combination + [v]))
    return best[1] if best else None


def part2():
    total = 0
    for n, c in enumerate(config):
        steps = len(shortest_combination(c.get("switches_list"), c.get("joltage")))
        total += steps
        print(f"{n+1}/{len(config)}: {steps}")
    return total

print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

