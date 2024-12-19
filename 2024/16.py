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


def dijkstra_graph(graph, start, end, facing):
    nodes_open = PriorityQueue()
    nodes_open.put((0, (start[0], start[1], facing)))
    dist = {(start[0], start[1], facing): 0}
    previous = defaultdict(set)
    visited = set()

    while nodes_open:
        while not nodes_open.empty():
            _, node = nodes_open.get()
            if node not in visited:
                break
        else:
            break
        visited.add((node[0], node[1], facing))
        if node == end:
            break
        r, c, facing = node
        check_neighbors = [(r + dr, c + dc, dirs.index((dr, dc))) for dr, dc in [dirs[facing], dirs[(facing - 1) % 4], dirs[(facing + 1) % 4]] if (r + dr, c + dc) not in visited]
        for nr, nc, nf in check_neighbors:
            if not (0 <= nr < len(inputs) and 0 <= nc < len(inputs[0])): continue
            if inputs[nr][nc] == '#':
                visited.add((nr, nc, facing))
                dist[(nr, nc, nf)] = float("inf")
                continue
            new_dist = dist.get((r, c, facing)) + (1 if facing == nf else 1001)
            if new_dist < dist.get((nr, nc, nf), float("inf")):
                nodes_open.put((new_dist, (nr, nc, nf)))
                dist[(nr, nc, nf)] = new_dist
                previous[(nr, nc, nf)] = {(r, c, facing)}
    return dist, previous

def part1(start, end, facing):
    dist, path = dijkstra_graph(inputs, start, end, facing)
    return dist, path

x, path = part1(start, end, facing)
dists = [_ for _  in x.items() if _[1] != float("inf")]
print("Part 1: ",min([_ for k, _ in dists if k[0] == end[0] and k[1] == end[1]]))
pprint(path)
print("Part 2: ")

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

