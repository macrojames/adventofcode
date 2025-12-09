#!/usr/bin/env python3
from math import sqrt
import time
import os.path
from util import read_input_lines
from itertools import combinations
from math import prod
import colorama
import numpy as np

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
ITERS = 10 if SAMPLE else 1000
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")

nodes = []
for line in inputs:
    nodes.append(tuple(map(int, line.split(","))))


def distance(p0, p1):
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)


distances = {(p0, p1): distance(p0, p1) for p0, p1 in combinations(nodes, 2) if not p0 == p1}
sorted_distances = ((d, p) for (p, d) in sorted(distances.items(), key=lambda x: x[1]))

networks = []


def part1():
    for i, (d, (p0, p1)) in enumerate(sorted_distances):
        if i == ITERS:
            break
        connect_network(p0, p1)

    return prod([len(_) for _ in sorted(networks, key=lambda x: -len(x))[:3]])


def connect_network(p0, p1):
    found = {0: None, 1: None}
    if SAMPLE:
        print(f"Testing: {[p0, p1]}")
    for idx, n in enumerate(networks):
        # HOW TO JOIN 2 NETS ?!
        if p0 in n:
            found[0] = idx
        if p1 in n:
            found[1] = idx
        if all([_ is not None for _ in found.values()]):
            break
    else:
        # kein Break oben, also eigenes Network
        if all([_ is None for _ in found.values()]):
            networks.append([p0, p1])
            if SAMPLE:
                print(f"New Network: {[p0, p1]}")
            return
    if found[0] != found[1] and all([_ is not None for _ in found.values()]):
        # join
        if SAMPLE:
            print(f"Joining Network: {networks[found[0]]}")
        networks[found[0]].extend(networks.pop(found[1]))
    else:
        if found[0] == found[1]:
            if SAMPLE:
                print(f"Skipped {p0=} and {p1=} in Network: {networks[found[0]]}")
        elif found[0] is not None:
            networks[found[0]].append(p1)
            if SAMPLE:
                print(f"Added {p1=} Network: {networks[found[0]]}")
        elif found[1] is not None:
            if SAMPLE:
                print(f"Added {p0=} Network: {networks[found[1]]}")
            networks[found[1]].append(p0)


def part2():
    i = 0
    for _, (p0, p1) in sorted_distances:
        connect_network(p0, p1)
        i += 1
        if SAMPLE and i % 20:
            print("Iteration:", i)
        if len(networks) == 1 and len(networks[0]) == len(nodes):
            return p0[0] * p1[0]
    raise Exception("NOPE")


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
