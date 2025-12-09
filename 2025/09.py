#!/usr/bin/env python3
from math import sqrt
import time
import os.path
from util import read_input_lines
from itertools import combinations
from math import prod
import colorama
import shapely

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


def area(p0, p1):
    return (1 + abs(p0[0] - p1[0])) * (1 + abs(p0[1] - p1[1]))


areas = {(p0, p1): area(p0, p1) for p0, p1 in combinations(nodes, 2) if not p0 == p1}
sorted_areas = list((d, p) for (p, d) in sorted(areas.items(), key=lambda x: -x[1]))


def part1():
    return list(sorted_areas)[0][0]


def part2():
    polygon = shapely.Polygon(nodes)
    for area, (p0, p1) in sorted_areas:
        rect = shapely.Polygon([p0, (p0[0], p1[1]), p1, (p1[0], p0[1])])
        if rect.covered_by(polygon):
            return area, (p0, p1)
    raise Exception


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
