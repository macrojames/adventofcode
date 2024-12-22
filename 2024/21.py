#!/usr/bin/env python3
from collections import Counter
from functools import cache
from heapq import heapify, heappop, heappush
from itertools import product
from pprint import pprint

import time
import os.path
import re
from util import read_input_lines
import colorama

colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE:
    print(colorama.Fore.RED + "SAMPLE MODE")
else:
    print(colorama.Fore.GREEN + "SOLUTION MODE")

numeric_pad = {
    "7": (">v", "84"),
    "8": ("<v>", "759"),
    "9": ("<v", "86"),
    "4": ("^>v", "751"),
    "5": ("<^>v", "4862"),
    "6": ("<^v", "593"),
    "1": (">^", "24"),
    "2": ("^<>v", "5130"),
    "3": ("^v<", "6A2"),
    "0": ("^>", "2A"),
    "A": ("^<", "30"),
}

direction_pad = {"^": ("v>", "vA"), "A": ("<v", "^>"), "<": (">", "v"), "v": ("<^>", "<^>"), ">": ("^<", "Av")}


def shortest_path(start, end, pad):
    queue = [(0, start, [], "")]
    min_cost = {start: 0}
    found_paths = []

    while queue:
        cost, node, path, facing = heappop(queue)
        if node == end:
            found_paths.append((path, cost))
            # break
        for eingabe, ziel in zip(*pad[node]):
            new_cost = cost + 1  # + (2 if eingabe != facing else 0)
            # new_path = path + [neighbor]
            if ziel not in min_cost or new_cost < min_cost[ziel]:
                min_cost[ziel] = new_cost
                new_path = path + [eingabe]
                heappush(queue, (new_cost, ziel, new_path, eingabe))
            elif new_cost == min_cost[ziel]:
                new_path = path + [eingabe]
                heappush(queue, (new_cost, ziel, new_path, eingabe))
    return min_cost, [f for f, c in found_paths if c == min_cost.get(end)]


@cache
def get_numeric_route(start, end):
    return shortest_path(start=start, end=end, pad=numeric_pad)


@cache
def get_directional_route(start, end):
    return shortest_path(start=start, end=end, pad=direction_pad)


def get_numeric_solution(instructions):
    solution = []
    cost = []
    for start, digit in zip("A" + instructions, instructions):
        c, paths = get_numeric_route(start, digit)
        solution.append(["".join(_) + "A" for _ in paths])
        cost.append(c[digit] + 1)
    return sum(cost), solution


@cache
def get_directional_solution(instructions):
    solution = []
    cost = []
    for start, digit in zip("A" + instructions, instructions):
        c, paths = get_directional_route(start, digit)
        solution.append(["".join(_) + "A" for _ in paths])
        cost.append(c[digit] + 1)
    return sum(cost), solution


def part1():
    complexity = []
    for pin in inputs[:]:
        cost, paths = get_numeric_solution(pin)
        next_paths = [(cost, "".join(combination)) for combination in product(*paths)]
        heapify(next_paths)
        for i in range(2):
            step_paths = next_paths[:64]
            next_paths = []
            for old_costs, target in (heappop(step_paths) for _ in range(len(step_paths))):
                tcost, tpaths = get_directional_solution(target)
                target_paths = ("".join(combination) for combination in product(*tpaths))
                for _ in target_paths:
                    heappush(next_paths, (len(_), _))
        complexity.append(next_paths[0][0] * int(pin[:-1]))
    return sum(complexity)


p1 = part1()

print("Part 1: ", p1, p1 == (126384 if SAMPLE else 217662))
# print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
