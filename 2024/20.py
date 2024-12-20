#!/usr/bin/env python3
from collections import Counter
import time
import os.path
from util import read_input_lines, get_indices
import colorama
from heapq import heappush, heappop

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")

dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

start = end = None
for r, line in enumerate(inputs):
    c = line.find("E")
    if c > 0:
        end = (r, c)
    c = line.find("S")
    if c > 0:
        start = (r, c)


def shortest_path_cost(start, end, cheat=(-1, -1)):
    queue = [(0, start, [start])]
    min_cost = {start: 0}
    found_paths = []

    while queue:
        cost, node, path = heappop(queue)
        r, c = node
        if node == end:
            found_paths.append((path, cost))
            break
        for neighbor in [(r + dr, c + dc) for dr, dc in dirs]:
            nr, nc = neighbor
            if not (0 <= nr < len(inputs) and 0 <= nc < len(inputs[0])):
                continue
            if inputs[nr][nc] == "#" and (nr, nc) != cheat:
                continue
            new_cost = cost + 1
            new_path = path + [neighbor]
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heappush(queue, (new_cost, neighbor, new_path))
            elif new_cost == min_cost[neighbor]:
                heappush(queue, (new_cost, neighbor, new_path))

    return min_cost, found_paths


def shortest_path_fullcheatmode(start, end):
    queue = [(0, start)]
    min_cost = {start: 0}
    found_paths = []

    while queue:
        cost, node = heappop(queue)
        r, c = node
        if node == end:
            # found_paths.append((path, cost))
            break
        for neighbor in [(r + dr, c + dc) for dr, dc in dirs]:
            nr, nc = neighbor
            if not (0 <= nr < len(inputs) and 0 <= nc < len(inputs[0])):
                continue
            new_cost = cost + 1
            # new_path = path + [neighbor]
            if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                min_cost[neighbor] = new_cost
                heappush(queue, (new_cost, neighbor))
            elif new_cost == min_cost[neighbor]:
                heappush(queue, (new_cost, neighbor))
    return min_cost, found_paths


def part1():
    cheat_costs = {}
    cost, path = shortest_path_cost(start, end)
    no_cheat = cost[end]
    for r, line in enumerate(inputs[1:-1]):
        print(f"line {r}")
        for c in get_indices(line[:-1], "#"):
            if c == 0:
                continue
            cheat = (r + 1, c)
            cost, path = shortest_path_cost(start, end=end, cheat=cheat)
            if end not in cost or cost[end] > no_cheat:
                continue
            cheat_costs[cheat] = cost[end]
    saved = [no_cheat - _ for _ in cheat_costs.values() if _ < no_cheat]
    cnt = Counter(saved).items()
    print(cnt)
    return sum([v for k, v in cnt if k >= 100])


def part2():
    cheated_costs = {}
    cost, path = shortest_path_cost(start, end)

    for i, p1 in enumerate(path[0][0]):
        for j, p2 in enumerate(path[0][0][i + 1 :]):
            delta = abs((p2[0] - p1[0])) + abs((p2[1] - p1[1]))
            if delta <= 20:
                saved = (j + 1) - delta
                if saved >= (50 if SAMPLE else 100):
                    cheated_costs[(p1, p2)] = saved

    cnt = Counter(cheated_costs.values()).items()
    return sum([v for k, v in cnt])


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
