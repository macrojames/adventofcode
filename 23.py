#!/usr/bin/env python3
from copy import copy
import os
import time
from util import read_input_lines, read_input_raw
from collections import Counter
start_timer = time.time()

SAMPLE = False

day = os.path.basename(__file__).split(".py")[0]
_input = read_input_lines(day, SAMPLE)

elves = list()
dirs = 'NSWE'
mapping = {
    'N': {"checks": {(0, -1), (-1, -1), (1, -1)}, "move": (0, -1)},
    'S': {"checks": {(0, 1), (-1, 1), (1, 1)}, "move": (0, 1)},
    'W': {"checks": {(-1, -1), (-1, 0), (-1, 1)}, "move": (-1, 0)},
    'E': {"checks": {(1, -1), (1, 0), (1, 1)}, "move": (1, 0)},
}
all_edges = {(0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, -1)}


def get_neighbors(x, y, combinators: set[tuple]) -> set:
    """ Not limited @ 0 or any edge"""
    return {(x+nx, y+ny) for nx, ny in combinators}


def get_dimensions(elves):
    min_x = min([_[0] for _ in elves])
    max_x = max([_[0] for _ in elves])
    min_y = min([_[1] for _ in elves])
    max_y = max([_[1] for _ in elves])
    h = abs(max_y - min_y) + 1
    w = abs(max_x - min_x) + 1
    return min_x, max_x, min_y, max_y, h, w


def print_elves(elves):
    min_x, max_x, min_y, max_y, h, w = get_dimensions(elves)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x, y) in elves else ".", end="")
        print()
    print("--------------------------")


for y, line in enumerate(_input):
    for x, c in enumerate(line):
        if c == '#':
            elves.append((x, y))


def move(elves, init, max_moves=10):
    moves = init
    still = 0
    while moves < max_moves:
        proposal = copy(elves)
        for e, (x, y) in enumerate(elves):
            uniq_elves = set(elves)
        # proposal phase
            if not get_neighbors(x, y, all_edges) & uniq_elves:
                continue
            for i in range(4):
                d = dirs[(moves+i) % 4]
                if not get_neighbors(x, y, mapping[d]["checks"]) & uniq_elves:
                    dx, dy = mapping[d]["move"]
                    nx, ny = x+dx, y+dy
                    proposal[e] = (nx, ny)
                    break
        if proposal == elves:
            print("No moves")
            still = moves + 1
            break
    # clearing
        cn = Counter(proposal)
        cleared = [_ if cn[_] == 1 else elves[idx] for idx, _ in enumerate(proposal)]   # reset to old position if duplicate
    # moving
        elves = cleared
        moves += 1
        if not (moves % 20):
            splittime = time.time() - start_timer
            print("Move:", moves, moves//splittime, "m/s after ", splittime, "s")
        # print_elves(elves)
    return elves, still


elves, still = move(elves, init=0, max_moves=10)
min_x, max_x, min_y, max_y, h, w = get_dimensions(elves)
print("Part 1: ", f"{h}x{w} = {h*w}; elves = {len(elves)} => free {h*w - len(elves)}")
elves, still = move(elves, init=10, max_moves=100)
print("Part 2: ", still)
print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
