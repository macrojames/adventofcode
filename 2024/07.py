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

challenge = {}
for line in inputs:
    k, numbers = line.split(": ")
    challenge[int(k)] = [int(_) for _ in numbers.split(" ")]


def get_a_solution(start, target, pool, concat=False):
    if not pool: return False
    current = pool[0]
    if len(pool) == 1: 
        # pool exhausted
        if start + current == target or start * current == target:
            return True
        if concat and int(f"{start}{current}") == target:
            return True
        return False
    # Optimizer?
    if start + current > target: return False
    return get_a_solution(start + current, target, pool[1:], concat=concat) or \
           get_a_solution(start * current, target, pool[1:], concat=concat) or \
           (concat and get_a_solution(int(f"{start}{current}"), target, pool[1:], concat=concat))

def part1():
    possibles = set()
    for target, pool in challenge.items():
        if get_a_solution(pool[0], target, pool[1:]): possibles.add(target)
    return possibles
def part2():
    possibles = set()
    for target, pool in challenge.items():
        if get_a_solution(pool[0], target, pool[1:], concat=True): possibles.add(target)
    return possibles


print("Part 1: ", sum(part1()))
print("Part 2: ", sum(part2()))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

