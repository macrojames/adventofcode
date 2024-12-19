#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from queue import PriorityQueue
from collections import defaultdict
import colorama
from pprint import pprint
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
facing = 3

for r, line in enumerate(inputs):
    c = line.find("E")
    if c > 0: end = (r, c)
    c = line.find("S")
    if c > 0: start = (r, c)

def all_shortest_paths(start, start_facing, end):
    queue = [(0, start, [start], start_facing)]
    min_cost = {(start, start_facing): 0}
    found_paths = []

    while queue:
        cost, node, path, facing = queue.pop(0)
        r, c = node
        if node == end:
            found_paths.append((path, facing, cost))
            continue
        for neighbor, new_facing in [((r + dr, c + dc), dirs.index((dr, dc))) \
                                     for dr, dc in [dirs[facing], dirs[(facing - 1) % 4], dirs[(facing + 1) % 4]] \
                                     if (r + dr, c + dc) and (r + dr, c + dc)]:
            nr, nc = neighbor
            if not (0 <= nr < len(inputs) and 0 <= nc < len(inputs[0])): continue
            if inputs[nr][nc] == '#': 
                continue
            new_cost = cost + (1 if facing == new_facing else 1001)
            new_path = path + [neighbor]
            if (neighbor, new_facing) not in min_cost or new_cost < min_cost[(neighbor, new_facing)]:
                min_cost[(neighbor, new_facing)] = new_cost
                queue.append((new_cost, neighbor, new_path, new_facing))
            elif new_cost == min_cost[(neighbor, new_facing)]:
                queue.append((new_cost, neighbor, new_path, new_facing))

    return found_paths

 
path = all_shortest_paths(start, facing, end)
print("Part 1: ", cost := min([_[2] for _ in path]))
print("Part 2: ", len(set([x for _ in path if _[2] == cost for x in _[0]])))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

