#!/usr/bin/env python3
from collections import defaultdict, deque
import time
import os.path
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

connections = [tuple(_.split("-")) for _ in inputs]
nmap = defaultdict(set)
for l, r in connections:
    nmap[l].add(r)
    nmap[r].add(l)


def part1():
    triplets = set()
    for k in (_ for _ in nmap.keys() if _.startswith("t")):
        for peer in nmap[k]:
            for p in nmap[peer]:
                if p in nmap[k]:
                    triplets.add(tuple(sorted([k, peer, p])))

    return len(triplets)


def part2():
    import networkx as nx

    G = nx.Graph()
    G.add_edges_from(connections)
    return ",".join(sorted(sorted(nx.find_cliques(G), key=len)[-1]))


print("Part 1: ", part1())
print("Part 2: ", part2())

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")
