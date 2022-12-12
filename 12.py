#!/usr/bin/env python3
import os
import time
from util import dijkstra, read_input_lines, read_input_raw, arr2d_get_idx, arr2d_get_near_idx, arr2d_get_all_idx
from queue import PriorityQueue
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)
grid = [list(_) for _ in _input]
start = arr2d_get_idx(grid, "S")
end = arr2d_get_idx(grid, "E")
all_a = arr2d_get_all_idx(grid, "a") + [start]

def get_cost(src, dst):
    ord_src = ord(src) if src.islower() else ord('a')    # Start always == a
    ord_dst = ord(dst) if dst.islower() else ord('z')    # End: doesn't matter, no effort
    cost = 1 if (ord_dst - ord_src) <= 1 else 10E9
    return cost

def get_cost2(src, dst):
    if dst == 'a':    # bricht ab bei falschem Ziel
        return float('inf')
    else:
        return get_cost(src, dst)
def get_cost3(src, dst):
    if dst == 'a':
        return 0
    else:
        return get_cost(src, dst)


dist, previous = dijkstra(grid, start, end, get_cost)
print("Part 1:", dist[end])

dist, previous = dijkstra(grid, start, end, get_cost3)
node = previous[end]
path = [node]
while grid[node[0]][node[1]] != 'a':
   y,x = previous.get(node)
   
   info = [y,x, grid[y][x]]
   path.append(info)
   node = previous[node]
print("Part 2a:", len(path))

#results = []
#for a in all_a:
#    dist, previous = dijkstra(grid, a, end, get_cost2)
#    if end in dist:
#        results.append((a, dist[end]))
#print("Part 2: ", sorted(results, key=lambda x:x[1])[0][1])
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
