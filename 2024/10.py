#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines, get_indices
from collections import defaultdict
from functools import lru_cache

import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

grid = [list(map(int, [i if i != '.' else '-1' for i in _])) for _ in inputs]
numbers = defaultdict(set)
for r, line in enumerate(grid):
    for i in range(10):
        numbers[i] |= set([(r, c) for c in get_indices(line, i)])

@lru_cache(maxsize=None)
def find_ways(start, next_level):
    r, c = start
    results = []
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= r+dr < len(grid) and 0 <= c+dc < len(grid[0]):
            if grid[r+dr][c+dc] == next_level:
                if next_level == 9: results.append([(r+dr, c+dc)])
                else:
                    for subpath in find_ways((r+dr, c+dc), next_level=next_level + 1):
                        results.append([(r+dr, c+dc)] + subpath)
    return results

def part1():    
    paths = []
    for point in numbers[0]:
        goals = set()
        all_paths = find_ways(point, 1)
        for subpath in all_paths:
            if len(subpath) == 9 and subpath[8] not in goals:
                goals.add(subpath[8])
                paths.append([point] + subpath)
    return paths

def part2():    
    paths = []
    for point in numbers[0]:
        goals = set()
        all_paths = find_ways(point, 1)
        for subpath in all_paths:
            paths.append([point] + subpath)
    return paths

p = part1()
print("Part 1: ", len(p))
print("Part 2: ", len(part2()))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

