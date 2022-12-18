#!/usr/bin/env python3
import os
import time
from util import read_input_lines, read_input_raw
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)
#cubes = {tuple(map(int, _.split(","))): 6 for _ in _input}
cubes = set([tuple(map(int, _.split(","))) for _ in _input])
max_x, max_y, max_z = max([_[0] for _ in cubes]), max([_[1] for _ in cubes]), max([_[2] for _ in cubes])
print(f"Dimension: {max_x}x{max_y}x{max_z}")


def check_neighbors(cube_pos, blocked):
    x, y, z = cube_pos
    sides = 6
    if (x-1, y, z) in blocked:
        sides -= 1
    if (x+1, y, z) in blocked:
        sides -= 1
    if (x, y-1, z) in blocked:
        sides -= 1
    if (x, y+1, z) in blocked:
        sides -= 1
    if (x, y, z-1) in blocked:
        sides -= 1
    if (x, y, z+1) in blocked:
        sides -= 1
    return sides


def get_adj_cubes(cube_pos):
    n = []
    x, y, z = cube_pos
    if x-1 >= 0:
        n.append((x-1, y, z))
    if x+1 <= max_x:
        n.append((x+1, y, z))
    if y-1 >= 0:
        n.append((x, y-1, z))
    if y+1 <= max_y:
        n.append((x, y+1, z))
    if z-1 >= 0:
        n.append((x, y, z-1))
    if z+1 <= max_z:
        n.append((x, y, z+1))
    return n


def bfs(node, exclude):
    visited = set()  # List for visited nodes.
    queue = []  # Initialize a queue
    visited.add(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        for neighbour in get_adj_cubes(m):
            if neighbour not in visited and neighbour not in exclude:   # can't visit cubes
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


outside = bfs((0, 0, 0), exclude=cubes)
pockets = set()
outer_world = cubes | outside
for x in range(max_x):
    for y in range(max_y):
        for z in range(max_z):
            if (x+1, y+1, z+1) not in outer_world:
                pockets.add((x+1, y+1, z+1))

sides = 0
for c in cubes:
    sides += check_neighbors(c, cubes)
print("Part 1: ", sides)

sides = 0
exclude = cubes | pockets
for c in cubes:
    sides += check_neighbors(c, exclude)
print("Part 2: ", sides)
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
