#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import colorama
from heapq import heappush, heappop
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

start = end = None
for r, line in enumerate(inputs):
    c = line.find("E")
    if c > 0: end = (r, c)
    c = line.find("S")
    if c > 0: start = (r, c)

def shortest_path(start, end):
    queue = [(0, start, [start])]
    min_cost = {(start): 0}
    found_paths = []

    while queue:
        cost, node, path = heappop(queue)
        r, c = node
        if node == end:
            found_paths.append((path, cost))
            break
        for neighbor, new_facing in [((r + dr, c + dc), dirs.index((dr, dc))) \
                                     for dr, dc in dirs \
                                     if (r + dr, c + dc)]:
            nr, nc = neighbor
            if not (0 <= nr < len(inputs) and 0 <= nc < len(inputs[0])): continue
            if inputs[nr][nc] == '#': 
                continue
            new_cost = cost + 1
            new_path = path + [neighbor]
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[(neighbor, new_facing)] = new_cost
                heappush(queue, (new_cost, neighbor, new_path))
            elif new_cost == min_cost[neighbor]:
                heappush(queue, (new_cost, neighbor, new_path))

    return found_paths

def part1():
    return shortest_path(start, end)

print("Part 1: ", part1())
#print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

