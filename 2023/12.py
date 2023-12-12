#!/usr/bin/env python3
import time
import re
from util import read_input_lines, bfs
from itertools import product

start_timer = time.time()

SAMPLE = True
DEBUG = True

inputs = read_input_lines('12', SAMPLE)
sources = [list(l.split(" ")[0]) for l in inputs]
mutations = [[int(x) for x in l.split(" ")[1].split(",")] for l in inputs]

def mutate(src, mutations):
    if DEBUG: print(f"Analyzing {"".join(src)} for {mutations}")
    solutions = []
    if not mutations or not src:
        return solutions
    current_mut = mutations[0]
    if len(mutations) > 1:
        rest_sum = sum(mutations[1:]) + len(mutations) - 1
    else:
        rest_sum = 0
    current_product = [list(p) for p in product('#?', repeat=current_mut)]

    for i in range(len(src) - rest_sum):
        if src[i] == '.': continue
        #if DEBUG: print(f"Checking if {current_mut} > {len(src) - i}: {current_mut > len(src) - i}")
        #if current_mut > len(src) - i: break
        if DEBUG: print(f"Checking if { src[i:i+current_mut]} in {current_product}: { src[i:i+current_mut] in current_product}")
        if src[i:i+current_mut] in current_product:
            down_sol = mutate(src[i + current_mut + 1:], mutations=mutations[1:])
            for sol in down_sol:
                solutions.append(f"{'.' * i + '#' * current_mut}{sol}")
            if not down_sol:
                solutions.append(f"{'.' * i + '#' * current_mut}")
    print(f"return {solutions}")
    return solutions


def part1():
    return sum([len(mutate(s, m)) for s, m in zip(sources, mutations)])


assert len(mutate(sources[0], mutations[0])) == 1
assert len(mutate(sources[1], mutations[1])) == 4
assert len(mutate(sources[5], mutations[5])) == 10


#print("Part 1: ", part1())
#print("Part 2: ", sum(travels.values()))

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
