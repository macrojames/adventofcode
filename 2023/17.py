#!/usr/bin/env python3

import heapq
import time
import os.path
import colorama
from util import in_bounds, read_input_lines, dirs
colorama.init()

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

grid = []

max_r, max_c = len(inputs) - 1, len(inputs[0]) -1
for r, row in enumerate(inputs):
    grid.append([int(_) for _ in row])


def part1(start, end, min_steps=0, max_steps=3):
    q = []
    heapq.heappush(q, (0, (*start, 0, 0, 0)))   # heatloss, (r, c, dr, dc, n)
    visited = set()
    while q:
        heatloss, (r, c, dr, dc, n) = heapq.heappop(q)

        if 0 < n < min_steps:
            possible = {(dr, dc)}
        else:
            possible = {(1, 0), (0, 1), (-1, 0), (0, -1)}
        if n >= max_steps:
            possible.remove((dr, dc))
        if (-dr, -dc) in possible:
            possible.remove((-dr, -dc)) # no reverse

        for ndr, ndc in possible:
            nr, nc = r + ndr, c + ndc
            nn = n + 1 if ndr == dr and ndc == dc else 1

            if not in_bounds(nr, nc, max_r, max_c):
                continue
            if (nr, nc, ndr, ndc, nn) in visited:
                continue

            heapq.heappush(q, ((heatloss + grid[nr][nc], (nr, nc, ndr, ndc, nn))))
            visited.add((nr, nc, ndr, ndc, nn))

            if (nr, nc) == end and nn >= min_steps:
                return heatloss + grid[nr][nc], visited
    return 


def print_grid(grid, visited):
    path = [(_[0], _[1]) for _  in visited]
    for r, line in enumerate(inputs):
        for c, _ in enumerate(line):
            if (r, c) in path: char = f"{colorama.Fore.GREEN}{grid[r][c]}"
            else: char = f"{colorama.Fore.RED}{grid[r][c]}"
            print(char, end="")
        print()

def part2():
    p2, visited = part1((0,0), (max_r, max_c), min_steps=4, max_steps=10)
    #print_grid(grid, visited)
    return p2

p1, visited = part1((0,0), (max_r, max_c))

#assert p1 == 46 if SAMPLE else 7185, f"{p1=}"    # falsche Antwort
print("Part 1: ", p1)

#p2 = part2()
#assert p2 == 51 if SAMPLE else 7616, f"{p2=}"    # falsche Antwort
print("Part 2: ", part2())

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
