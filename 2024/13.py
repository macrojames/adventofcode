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

games = []
for i in range(1+ (len(inputs) // 4)):
    '''
    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    '''
    game_match = re.match("Button A: X\+(\d+), Y\+(\d+)Button B: X\+(\d+), Y\+(\d+)Prize: X=(\d+), Y=(\d+)", "".join(inputs[i*4:i*4+4:]))
    games.append(tuple(map(int, game_match.groups())))


def solve(game, scale=0):
    # (1) px = a * x1 + b * x2   
    # (2) py = a * y1 + b * y2
    x1, y1, x2, y2, px, py = game
    px += scale
    py += scale

    det = x1 * y2 - x2 * y1
    # Darf nicht null sein
    if det == 0:
        raise ZeroDivisionError

    # Compute a and b
    a = (y2 * px - x2 * py) / det
    b = (-y1 * px + x1 * py) / det

    return a, b

def part1():
    return [solve(game) for game in games]

def part2():
    return [solve(game, scale = 10000000000000) for game in games]


print("Part 1: ", int(sum([(3*a + b) for a, b in part1() if a % 1 == 0 and b % 1 == 0])))
print("Part 2: ", int(sum([(3*a + b) for a, b in part2() if a % 1 == 0 and b % 1 == 0])))

print(f"{colorama.Fore.BLUE}Time elapsed: {round(time.time() - start_timer, 3)}s")

