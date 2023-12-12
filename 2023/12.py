#!/usr/bin/env python3
import time
import re
from util import read_input_lines, bfs
from itertools import combinations

start_timer = time.time()

SAMPLE = True
DEBUG = True

inputs = read_input_lines('12', SAMPLE)
sources = [list(l.split(" ")[0]) for l in inputs]
mutations = [[int(x) for x in l.split(" ")[1].split(",")] for l in inputs]

def mutate(src, mutations):

    pass


def part1():
    return sum([len(mutate(s, m)) for s, m in zip(sources, mutations)])



print(mutate(sources[0], mutations[0]))
#print("Part 1: ", part1())
#print("Part 2: ", sum(travels.values()))

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
