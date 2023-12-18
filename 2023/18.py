#!/usr/bin/env python3
from collections import deque
from itertools import batched
import time
import os.path
from util import in_bounds, read_input_lines, shoelace_area_outer
import colorama

colorama.init()

start_timer = time.time()
SAMPLE = False
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)

dirs = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}

instructions = [tuple(row.split(" ")) for r, row in enumerate(inputs)]


def fill(holes):
    rs, cs = sorted([r for r, c in holes]), sorted([c for r, c in holes])
    min_r, max_r = min(rs), max(rs)
    min_c, max_c = min(cs), max(cs)
    lim_u, lim_d = min_r - 1, max_r + 1
    lim_l, lim_r = min_c - 1, max_c + 1
    area = (lim_r - lim_l + 1) * (lim_d - lim_u + 1)

    void = set()
    q = deque([(lim_u, lim_l)])
    while q:
        cr, cc = q.popleft()
        for dr, dc in dirs.values():
            nr, nc = cr + dr, cc + dc
            if (nr, nc) in void:
                continue
            if (nr, nc) in holes:
                continue
            if lim_u <= nr <= lim_d and lim_l <= nc <= lim_r:
                void.add((nr, nc))
                q.append((nr, nc))

    return area - len(void), void


def part1():
    hole = set()
    pos = (0, 0)
    for direction, count, _ in instructions:
        dr, dc = dirs[direction]
        for c in range(int(count)):
            hole.add(pos)
            pos = pos[0] + dr, pos[1] + dc
    filled, void = fill(holes=hole)
    return filled


def hexdec(encoded):
    hex_count = encoded[2:7]
    direction = ["R", "D", "L", "U"][int(encoded[7])]
    return int(hex_count, 16), direction


def part2():
    pos = (0, 0)
    points = [pos]
    sum_count = 0
    for _, _, encoded in instructions:
        count, direction = hexdec(encoded)
        dr, dc = dirs[direction]
        sum_count += count
        pos = pos[0] + count * dr, pos[1] + count * dc
        points.append(pos)

    return int(shoelace_area_outer(points))


def print_grid(visited1, visited2):
    rs, cs = [r for r, c in visited2], [c for r, c in visited2]

    print(f"{min(rs)} - {max(rs) + 1}")
    for r in range(min(rs), max(rs) + 1):
        for c in range(min(cs), max(cs) + 1):
            if (r, c) in visited1 and (r, c) in visited2:
                char = f"{colorama.Fore.RED}X"
            elif (r, c) in visited1:
                char = f"{colorama.Fore.GREEN}#"
            elif (r, c) in visited2:
                char = f"{colorama.Fore.RED}."
            else:
                char = f"{colorama.Fore.BLUE}."
            print(char, end="")
        print()


print("Part 1: ", part1())
print(f"Part 2: {part2()}")

print(f"Time elapsed: {round(time.time() - start_timer, 3)}s")
