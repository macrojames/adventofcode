#!/usr/bin/env python3
from queue import PriorityQueue
import time
import os.path
import colorama
from util import in_bounds, read_input_lines, dirs
colorama.init()

start_timer = time.time()
SAMPLE = True
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

grid = []

max_r, max_c = len(inputs) - 1, len(inputs[0]) -1
for r, row in enumerate(inputs):
    grid.append([int(_) for _ in row])


def dijkstra(grid, start, end, get_cost):
    
    nodes_open = PriorityQueue()
    nodes_open.put((0, start))
    dist = {start: 0}
    previous = {}
    visited = set()
    while nodes_open:
        while not nodes_open.empty():
            w, node = nodes_open.get()
            if node not in visited:
                break
        else:
            break
        visited.add(node)
        #if (node[0], node[1]) == end:
        #    break
        check_neighbors = [(node[0] + dr, node[1] + dc, dr, dc) for dr, dc in dirs.values() if (node[0] + dr, node[1] + dc, dc, dr) not in visited]
        for neighbor in check_neighbors:
            nr, nc, dr, dc = neighbor
            if not in_bounds(neighbor[0], neighbor[1], max_r, max_c):
                continue
            new_dist = w + get_cost(neighbor, node, grid, previous)
            if new_dist == float('inf'):    # Abbruchmöglichkeit durch cost implementierung
                continue
            if new_dist < dist.get(neighbor, float('inf')):
                nodes_open.put((new_dist, neighbor))
                dist[neighbor] = new_dist
                previous[neighbor] = node
                
    return dist, previous


def part1(start, end):
    def get_next(new:tuple, current:tuple, grid:list[list[int]], previous:dict):
        dr, dc = new[2], new[3]
        c = current
        for i in range(3):
            if c in previous:
                p = previous[c]
                pr, pc = p[2], p[3]
                if pr != dr or pc != dc:
                    return grid[new[0]][new[1]]
                c = p
            else:
                return grid[new[0]][new[1]]
        else:
            return float('inf')


    dist, prev = dijkstra(grid, start, end, get_next)
    path = []
    c = [(r,c,dr,dc) for r,c,dr,dc in dist if r==end[0] and c==end[1]][0]
    while c in prev:
        p = prev[c]
        path.append((p[0], p[1]))
        c = p

    print_grid(grid, path)
    return min([v for k, v in dist.items() if k[0] == end[0] and k[1] == end[1]] + [float('inf')])

def print_grid(grid, path):
    for r, line in enumerate(inputs):
        for c, _ in enumerate(line):
            if (r, c) in path: char = f"{colorama.Fore.GREEN}{grid[r][c]}"
            else: char = f"{colorama.Fore.RED}{grid[r][c]}"
            print(char, end="")
        print()

def part2():
    pass
end = (max_r, max_c)
p1 = part1((0,0,0,0), end)

#assert p1 == 46 if SAMPLE else 7185, f"{p1=}"    # falsche Antwort
print("Part 1: ", p1)

#p2 = part2()
#assert p2 == 51 if SAMPLE else 7616, f"{p2=}"    # falsche Antwort
#print("Part 2: ", p2)

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
