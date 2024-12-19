#!/usr/bin/env python3
import time
import os.path
from util import read_input_lines
import re
import colorama
colorama.init()
start_timer = time.time()
SAMPLE = os.environ.get("SAMPLE", "True") == "True"
DEBUG = True
inputs = read_input_lines(os.path.splitext(os.path.basename(__file__))[0], SAMPLE)
if SAMPLE: print(colorama.Fore.RED + "SAMPLE MODE")
else: print(colorama.Fore.GREEN + "SOLUTION MODE")

max_x, max_y = (11, 7) if SAMPLE else (101, 103)

robots = []

for line in inputs:
    robots.append(tuple(map(int, re.findall("\-{0,1}\d+", line))))


def print_grid(g):
    for y in range(max_y):
        for x in range(max_x):
            print(len([_ for _ in g if _[0] == x and _[1] == y]) or '.', end="")
        print()
    print()


def part1():
    after = []
    sectors = [0, 0, 0, 0, 0]
    moves = 100
 
    for x, y, vx, vy in robots:
        nx, ny = (x + (moves * vx)) % max_x, (y + (moves * vy)) % max_y
        if nx < max_x//2 and ny < max_y//2: sec = 1
        elif nx < max_x//2 and ny > max_y//2: sec = 2
        elif nx > max_x//2 and ny < max_y//2: sec = 3
        elif nx > max_x//2 and ny > max_y//2: sec = 4
        else: sec = 0
        sectors[sec] +=1
        after.append((nx, ny, sec))
    print_grid(after)
    return sectors[1] * sectors[2] * sectors[3] * sectors[4] 

def get_noise(g):
    x_noise = [len([_ for _ in g if _[0] == x]) for x in range(max_x)]
    y_noise = [len([_ for _ in g if _[1] == y]) for y in range(max_y)]
    return max_x - x_noise.count(0), max_y - y_noise.count(0), max(x_noise), max(y_noise)

def part2(robots):
    moves = 1
    move = 0
    max_sec  = 0
    while True:
        sectors = [0]*120
        after = []
        move += 1
        for x, y, vx, vy in robots:
            nx, ny = (x + (moves * vx)) % max_x, (y + (moves * vy)) % max_y
            after.append((nx, ny, vx, vy))
            sec = (ny // 10) * 10 + nx // 10 
            sectors[sec] += 1 
        max_sec = max(max(sectors), max_sec)
        print(f"{move}: {max(sectors), sectors.index(max(sectors))} {max_sec}")
        robots = after
        if max(sectors) > 75:
            print_grid(after)
            break
    return move 


print("Part 1: ", part1())
print("Part 2: ", part2(robots))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

