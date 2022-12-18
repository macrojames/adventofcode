#!/usr/bin/env python3
import os
import time
from parse import parse
from util import read_input_lines, dijkstra_graph
start_timer = time.time()

SAMPLE = True

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)
temp_valves = [parse("Valve {name:l} has flow rate={rate:d}; tunnels lead to valves {targets}", l.replace("tunnel leads to valve ", "tunnels lead to valves ")).named for l in _input]
valves = {v['name']: {
        "rate": v['rate'],
        "targets": v['targets'].split(", ")
    }
for v in temp_valves}

sum_flow = 0
open_valves = set()
useful_valves = [_ for _ in valves if valves.get(_).get('rate')]
minutes = 30

def distance(valves, src, dst):
    dist, previous = dijkstra_graph(graph=valves,start=src, end=dst, get_cost=lambda x,y: 1)
    return dist[dst]

def projection_flow(valves, current_pos, avail_minutes):
    projection = {}
    for v in useful_valves:
        if v in open_valves: continue
        rate = valves.get(v).get('rate')
        lost_minutes_hinweg = distance(valves, current_pos, v) + 1
        projection[v] = max(0, rate * (avail_minutes - lost_minutes_hinweg ))
    return projection

for minute in range(minutes):
    current_flow = sum([valves.get(_).get('rate') for _ in open_valves])
    sum_flow += current_flow
    print(f" Valves {', '.join(open_valves)} are open, releasing {current_flow} pressure. Sum is {sum_flow}")
    print("Potential:", projection_flow(valves, 'AA', minutes-minute))
    pass

print("Part 1: ", distance(valves, "AA", "GG"))
print("Part 2: ", )
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
