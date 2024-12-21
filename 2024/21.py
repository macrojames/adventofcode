#!/usr/bin/env python3
from heapq import heappop, heappush
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
            found_paths.append(path)
            break
        for eingabe, ziel in zip(*pad[node]):
            new_cost = cost + 1 + (0 if eingabe in "<>" else 0.6) + (0 if facing == eingabe else 0.6)
            # new_path = path + [neighbor]
            if ziel not in min_cost or new_cost < min_cost[ziel]:
                min_cost[ziel] = new_cost
                new_path = path + [eingabe]
                heappush(queue, (new_cost, ziel, new_path, eingabe))
            elif new_cost == min_cost[ziel]:
                new_path = path + [eingabe]
                heappush(queue, (new_cost, ziel, new_path, eingabe))
    return min_cost, found_paths


def get_numeric_route(start, end):
    return shortest_path(start=start, end=end, pad=numeric_pad)


def get_directional_route(start, end):
    return shortest_path(start=start, end=end, pad=direction_pad)


def get_directions(instructions, start="A"):
    route = []
    for inst in instructions:
        for digit in inst:
            route.extend(get_directional_route(start, digit)[1][0] + ["A"])
            start = digit
    return route


def part1():
    routes = {}
    for pin in inputs:
        start = "A"
        route = []
        for digit in pin:
            route.extend(get_numeric_route(start, digit)[1][0] + ["A"])
            start = digit
        routes[pin] = get_directions(get_directions(route))
        # routes[pin] = [route, a := get_directions(route), get_directions(a)]
    return routes


p1 = part1()
l = [int(re.findall("\d+", k)[0]) * len(path) for k, path in p1.items()]
x = sum(l)
pprint({k: ["".join(_) for _ in v] for k, v in p1.items()}, depth=3, width=400)
print("Part 1: ", x, x < 218806)  # False high
# print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
