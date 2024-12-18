#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
from queue import PriorityQueue
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

max_c_incl = max_r_incl = 6 if SAMPLE else 70

corrupt = [tuple(map(int, _.split(","))) for _ in inputs]

def dijkstra_graph(blocked, start, end):
    nodes_open = PriorityQueue()
    nodes_open.put((0, start))
    dist = {start: 0}
    previous = {}
    visited = set()

    while nodes_open:
        while not nodes_open.empty():
            _, node = nodes_open.get()
            if node not in visited:
                break
        else:
            break
        visited.add(node)
        if node == end:
            break
        r, c = node
        check_neighbors = [(r + dr, c + dc) for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)] if (r + dr, c + dc) not in visited]
        for new_node in check_neighbors:
            if not (0 <= new_node[0] <= max_r_incl and 0 <= new_node[1] <= max_c_incl): continue
            if new_node in blocked:
                visited.add(new_node)
                dist[new_node] = float("inf")
                continue
            new_dist = dist.get(node) + 1
            if new_dist < dist.get(new_node, float("inf")):
                nodes_open.put((new_dist, new_node))
                dist[new_node] = new_dist
                previous[new_node] = node
    return dist, previous

def get_shortest_path(previous_dict, end):
    current = end
    path = [end]
    while prev := previous_dict.get(current):
        path.append(prev)
        current = prev
    return path[::-1]


def part1():
    l = 12 if SAMPLE else 1024
    dist, previous = dijkstra_graph(blocked=corrupt[:l], start=(0,0), end=(max_r_incl, max_c_incl))
    return dist

def part2():
    l = 12 if SAMPLE else 1024
    end=(max_r_incl, max_c_incl)
    while True:
        dist, previous = dijkstra_graph(blocked=corrupt[:l+1], start=(0,0), end=end)
        if end not in previous:
            break
        sp = get_shortest_path(previous, end=end)
        l = corrupt.index(next(_ for _ in corrupt[l:] if _ in sp))
    return corrupt[l]

print("Part 1: ", part1()[(max_r_incl, max_c_incl)])
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

